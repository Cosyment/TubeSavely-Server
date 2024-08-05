from urllib.parse import urlparse, parse_qs

import requests

from .base import BaseParser, VideoAuthor, VideoInfo
import vendor.yt_dlp.extractor.extend


class DouPai(BaseParser):
    """
    逗拍
    """

    def parse_share_url(self, share_url: str) -> VideoInfo:
        # video_id = self.get_val_from_url_by_query_key(share_url, "id")
        video_id = vendor.yt_dlp.extractor.extend.get_val_from_url_by_query_key(share_url, 'id')

        return self.parse_video_id(video_id)

    def parse_video_id(self, video_id: str) -> VideoInfo:
        req_url = f"https://v2.doupai.cc/topic/{video_id}.json"
        # async with httpx.AsyncClient() as client:
        #     response = await client.get(req_url, headers=self.get_default_headers())
        #     response.raise_for_status()
        response = requests.get(req_url, headers=self.get_default_headers())
        response.raise_for_status()

        json_data = response.json()
        data = json_data["data"]

        video_info = VideoInfo(
            video_url=data["videoUrl"],
            cover_url=data["imageUrl"],
            title=data["name"],
            author=VideoAuthor(
                uid=data["userId"]["id"],
                name=data["userId"]["name"],
                avatar=data["userId"]["avatar"],
            ),
        )
        return video_info