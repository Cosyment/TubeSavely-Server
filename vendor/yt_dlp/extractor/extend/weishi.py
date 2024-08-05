from urllib.parse import urlparse, parse_qs

import requests

from .base import BaseParser, VideoAuthor, VideoInfo
import vendor.yt_dlp.extractor.extend


class WeiShi(BaseParser):
    """
    微视
    """

    def parse_share_url(self, share_url: str) -> VideoInfo:
        # video_id = self.get_val_from_url_by_query_key(self,share_url, "id")
        video_id = vendor.yt_dlp.extractor.extend.get_val_from_url_by_query_key(share_url, "id")
        return self.parse_video_id(video_id)

    def parse_video_id(self, video_id: str) -> VideoInfo:
        req_url = (
            "https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage"
            f"?feedid={video_id}"
        )
        # async with httpx.AsyncClient() as client:
        #     response = await client.get(req_url, headers=self.get_default_headers())
        response = requests.get(req_url, headers=self.get_default_headers())
        response.raise_for_status()

        json_data = response.json()
        # 接口返回错误
        if json_data["ret"] != 0:
            raise Exception(json_data["msg"])
        # 视频状态错误
        if len(json_data["data"]["errmsg"]) > 0:
            raise Exception(json_data["data"]["errmsg"])

        data = json_data["data"]["feeds"][0]

        video_info = VideoInfo(
            video_url=data["video_url"],
            cover_url=data["images"][0]["url"],
            title=data["feed_desc_withat"],
            author=VideoAuthor(
                uid=data["id"],
                name=data["poster"]["nick"],
                avatar=data["poster"]["avatar"],
            ),
        )
        return video_info
