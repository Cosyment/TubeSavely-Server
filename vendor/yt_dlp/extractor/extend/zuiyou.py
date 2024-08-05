import requests

from .base import BaseParser, VideoAuthor, VideoInfo
import vendor.yt_dlp.extractor.extend

class ZuiYou(BaseParser):
    """
    最右
    """

    def parse_share_url(self, share_url: str) -> VideoInfo:
        # video_id = self.get_val_from_url_by_query_key(share_url, "pid")
        video_id = vendor.yt_dlp.extractor.extend.get_val_from_url_by_query_key(share_url, "pid")
        return self.parse_video_id(video_id)

    def parse_video_id(self, video_id: str) -> VideoInfo:
        int_video_id = int(video_id)
        req_url = "https://share.xiaochuankeji.cn/planck/share/post/detail"
        post_data = {
            "h_av": "5.2.13.011",
            "pid": int_video_id,
        }
        # async with httpx.AsyncClient(follow_redirects=True) as client:
        #     response = await client.post(
        #         req_url, headers=self.get_default_headers(), json=post_data
        #     )
        #     response.raise_for_status()
        response = requests.get(req_url, headers=self.get_default_headers(), json=post_data)
        response.raise_for_status()

        json_data = response.json()
        data = json_data["data"]["post"]
        video_key = str(data["imgs"][0]["id"])

        video_info = VideoInfo(
            video_url=data["videos"][video_key]["url"],
            cover_url=data["videos"][video_key]["cover_urls"][0],
            title=data["content"],
            author=VideoAuthor(
                uid=str(data["member"]["id"]),
                name=data["member"]["name"],
                avatar=data["member"]["avatar_urls"]["origin"]["urls"][0],
            ),
        )
        return video_info
