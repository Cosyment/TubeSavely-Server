import json
from urllib.parse import unquote

import requests
from parsel import Selector

from .base import BaseParser, VideoAuthor, VideoInfo


class DouYin(BaseParser):
    """
    抖音 / 抖音火山版
    """

    def parse_share_url(self, share_url: str) -> VideoInfo:
        # async with httpx.AsyncClient(follow_redirects=True) as client:
        #     response = await client.get(share_url, headers=self.get_default_headers())
        #     response.raise_for_status()
        response = requests.get(share_url, headers=self.get_default_headers(), allow_redirects=False)
        response.raise_for_status()

        sel = Selector(response.text)
        render_data = sel.css("script#RENDER_DATA::text").get(default="")
        if len(render_data) <= 0:
            raise Exception("failed to parse render data from HTML")
        render_data = unquote(render_data)  # urldecode

        json_data = json.loads(render_data)
        data = json_data["app"]["videoInfoRes"]["item_list"][0]

        # 获取图集图片地址
        images = []
        # 如果data含有 images，并且 images 是一个列表
        if "images" in data and isinstance(data["images"], list):
            # 获取每个图片的url_list中的第一个元素，非空时添加到images列表中
            for img in data["images"]:
                if (
                        "url_list" in img
                        and isinstance(img["url_list"], list)
                        and len(img["url_list"]) > 0
                        and len(img["url_list"][0]) > 0
                ):
                    images.append(img["url_list"][0])

        # 获取视频播放地址
        video_url = data["video"]["play_addr"]["url_list"][0].replace("playwm", "play")
        # 如果图集地址不为空时，因为没有视频，上面抖音返回的视频地址无法访问，置空处理
        if len(images) > 0:
            video_url = ""

        # 获取重定向后的mp4视频地址
        # 图集时，视频地址为空，不处理
        video_mp4_url = ""
        if len(video_url) > 0:
            video_mp4_url = self.get_video_redirect_url(video_url)

        video_info = VideoInfo(
            video_url=video_mp4_url,
            cover_url=data["video"]["cover"]["url_list"][0],
            title=data["desc"],
            description=data["desc"],
            images=images,
            author=VideoAuthor(
                uid=data["author"]["sec_uid"],
                name=data["author"]["nickname"],
                avatar=data["author"]["avatar_thumb"]["url_list"][0],
            ),
        )
        return video_info

    def get_video_redirect_url(self, video_url: str) -> str:
        # async with httpx.AsyncClient(follow_redirects=False) as client:
        #     response = await client.get(video_url, headers=self.get_default_headers())
        # return response.headers.get("location", "")
        response = requests.get(video_url, headers=self.get_default_headers(), allow_redirects=False)
        return response.headers.get('location', "")

    def parse_video_id(self, video_id: str) -> VideoInfo:
        req_url = f"https://www.iesdouyin.com/share/video/{video_id}/"
        return self.parse_share_url(req_url)
