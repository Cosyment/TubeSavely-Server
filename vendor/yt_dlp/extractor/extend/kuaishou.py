import re

import fake_useragent
import requests
from urllib.parse import urlparse, parse_qs

from .base import BaseParser, VideoAuthor, VideoInfo


class KuaiShou(BaseParser):
    """
    快手
    """

    def parse_share_url(self, share_url: str) -> VideoInfo:
        user_agent = fake_useragent.UserAgent(os=["ios"]).random
        # 获取跳转前的信息, 从中获取视频ID, cookie
        # with httpx.AsyncClient(follow_redirects=False) as client:
        #     redirect_response = client.get(
        #         share_url,
        #         headers={
        #             "User-Agent": user_agent,
        #             "Referer": "https://v.kuaishou.com/",
        #         },
        #     )
        redirect_response = requests.get(
            share_url,
            headers={
                "User-Agent": user_agent,
                "Referer": "https://v.kuaishou.com/",
            },
            allow_redirects=False,  # 禁止自动重定向，以获取重定向响应
        )
        redirect_url = redirect_response.headers.get("Location", "")
        if not redirect_url:
            raise Exception("failed to get parse video ID from share URL")

        # redirect_response.cookies 直接用于下面的请求会触发反爬虫验证, 处理成字典没有这个问题
        format_cookie_map = {}
        for cookie_id, cookie_val in redirect_response.cookies.items():
            format_cookie_map[cookie_id] = cookie_val
        video_id = redirect_url.split("?")[0].split("/")[-1]

        post_data = {
            "fid": "0",
            "shareResourceType": "PHOTO_OTHER",
            "shareChannel": "share_copylink",
            "kpn": "KUAISHOU",
            "subBiz": "BROWSE_SLIDE_PHOTO",
            "env": "SHARE_VIEWER_ENV_TX_TRICK",
            "h5Domain": "m.gifshow.com",
            "photoId": video_id,
            "isLongVideo": False,
        }
        # with httpx.AsyncClient() as client:
        #     response = client.post(
        #         "https://m.gifshow.com/rest/wd/photo/info?kpn=KUAISHOU&captchaToken=",
        #         headers={
        #             "Origin": "https://m.gifshow.com",
        #             "Referer": redirect_url,
        #             "Content-Type": "application/json",
        #             "User-Agent": user_agent,
        #         },
        #         cookies=format_cookie_map,
        #         json=post_data,
        #     )
        #     response.raise_for_status()
        match = re.search(r'/short-video/(?P<id>[a-zA-Z0-9_-]+)', redirect_url)
        if match:
            video_id = match.group('id')
            link = urlparse(redirect_url)
            params = parse_qs(link.query)
            response = requests.post('https://v.m.chenzhongtech.com/rest/wd/photo/info?kpn=KUAISHOU',
                                     headers={'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br',
                                              'content-type': 'application/json',
                                              'Origin': 'https://v.m.chenzhongtech.com',
                                              'Referer': redirect_url,
                                              'Sec-Ch-Ua': '"Not_A_Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                                              'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
                                              'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1',
                                              'User-Agent': fake_useragent.UserAgent(os='windows').random,
                                              'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did={}'.format(params.get('ztDid'))},
                                     json={
                                         "fid": params.get('fid'),
                                         "shareToken": params.get('shareToken'),
                                         "shareObjectId": params.get('shareObjectId'),
                                         "shareMethod": "TOKEN",
                                         "shareId": params.get('shareId'),
                                         "shareResourceType": "PHOTO_OTHER",
                                         "shareChannel": "share_copylink",
                                         "kpn": "KUAISHOU",
                                         "subBiz": "BROWSE_SLIDE_PHOTO",
                                         "env": "SHARE_VIEWER_ENV_TX_TRICK",
                                         "h5Domain": "v.m.chenzhongtech.com",
                                         "photoId": video_id,
                                         "isLongVideo": False,
                                     })
        else:
            response = requests.post(
                "https://m.gifshow.com/rest/wd/photo/info?kpn=KUAISHOU&captchaToken=",
                headers={
                    "Origin": "https://m.gifshow.com",
                    "Referer": redirect_url,
                    "Content-Type": "application/json",
                    "User-Agent": user_agent,
                },
                cookies=format_cookie_map,  # 传递 cookies 参数
                json=post_data,  # 通过 json 参数自动序列化字典为 JSON 格式
            )

        json_data = response.json()
        data = json_data["photo"]

        # 获取视频地址
        video_url = ""
        if "mainMvUrls" in data and len(data["mainMvUrls"]) > 0:
            video_url = data["mainMvUrls"][0]["url"]

        # 获取图集
        ext_params_atlas = data.get("ext_params", {}).get("atlas", {})
        atlas_cdn_list = ext_params_atlas.get("cdn", [])
        atlas_list = ext_params_atlas.get("list", [])
        images = []
        if len(atlas_cdn_list) > 0 and len(atlas_list) > 0:
            for atlas in atlas_list:
                images.append(f"https://{atlas_cdn_list[0]}/{atlas}")

        video_info = VideoInfo(
            video_url=video_url,
            cover_url=data["coverUrls"][0]["url"],
            title=data["caption"],
            author=VideoAuthor(
                uid="",
                name=data["userName"],
                avatar=data["headUrl"],
            ),
            images=images,
        )
        return video_info

    async def parse_video_id(self, video_id: str) -> VideoInfo:
        raise NotImplementedError("快手暂不支持直接解析视频ID")
