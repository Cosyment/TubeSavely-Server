from contextlib import asynccontextmanager

import requests
import uvicorn
from fastapi import FastAPI, Depends
import redis.asyncio as redis

from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

from vendor import yt_dlp
from vendor.yt_dlp.extractor.extend import parse_video_share_url
from urllib.parse import urlparse


@asynccontextmanager
async def lifespan(_: FastAPI):
    redis_connection = redis.from_url("redis://127.0.0.1:6379", encoding="utf8")
    await FastAPILimiter.init(redis_connection)
    yield
    await FastAPILimiter.close()


app = FastAPI(lifespan=lifespan)


async def rate_limiter():
    return RateLimiter(times=1, seconds=5)


@app.get("/test", dependencies=[Depends(rate_limiter)])
async def test(params: str):
    return {"hi": params}


@app.get('/parse', dependencies=[Depends(rate_limiter)])
async def parse(url: str):
    try:
        if urlparse(url).scheme in ['http', 'https'] or url.startswith('www.'):
            # if url.__contains__("x.com") or url.__contains__("youtube.com") or url.__contains__(
            #         "youtu.be") or url.__contains__("facebook.com") or url.__contains__("tiktok.com"):
            #     return {'code': 401, 'msg': 'Not Supported'}
            return {'code': 200, 'msg': 'success', 'data': dispatch(url)}
        return {'code': 400, 'msg': f'the parameter {url} is invalid.'}
    except Exception as e:
        return {"code": 500, "msg": f"{str(e)}"}


def dispatch(url: str):
    try:
        data = yt_dlp_parse(url)
        if data is None:
            data = openapi_parse(url)
        return data
    except Exception as e:
        print(f'parse exception {str(e)}')
        raise e


def yt_dlp_parse(url: str):
    try:
        # ydl_opts = {
        #     'format': 'best',  # 你可以根据需要设置不同的选项
        #     'outtmpl': '/Users/Waiting/Downloads/video/video.%(ext)s'  # 设置输出路径模板
        # }
        with yt_dlp.YoutubeDL() as ydl:
            data = ydl.extract_info(url, download=False)
            # ydl.download(url)
            # data = extend_parse(url)
            # 存在播放地址
            if 'formats' in data:
                return data
            else:
                return yt_dlp_extend_parse(url)
    except Exception as e:
        print(f'yt_dlp parse exception {str(e)}')
        return yt_dlp_extend_parse(url)


def yt_dlp_extend_parse(url: str):
    try:
        video_info = parse_video_share_url(share_url=url)
        if hasattr(video_info, 'video_url'):
            data = {
                'title': video_info.title,
                'formats': [{
                    'url': video_info.video_url,
                    "ext": "mp4",
                    "video_ext": "mp4",
                }],
                'url': video_info.video_url,
                'original_url': url,
                'thumbnail': video_info.cover_url,
                'uploader': video_info.author.name
            }
            return data
        else:
            print(f'yt_dlp extend parse exception no video_url field')
            return None
    except KeyError as error:
        print(f'yt_dlp extend parse KeyError exception {str(error)}')
        return None
    except Exception as e:
        print(f'yt_dlp extend parse exception {str(e)}')
        return None


def openapi_parse(url: str):
    response = requests.get(f'https://proxy.layzz.cn/lyz/getAnalyse?token=rzwewdzrckc-auther-523ddd&link={url}')
    json_data = response.json()
    if 'data' in json_data:
        data = {
            'title': json_data['data']['desc'],
            'formats': [{
                'url': json_data['data']['playAddr'],
                "ext": "mp4",
                "video_ext": "mp4",
            }],
            'url': json_data['data']['playAddr'],
            'original_url': url,
            'thumbnail': json_data['data']['cover'],
            'music': json_data['data']['music']
        }
        return data
    if json_data is None:
        response = requests.post('http://api.xiaofany.com/api/v1/remark', params={
            'client_id': "16655792287608",
            'sign': "6B089F0A6E25D98D4196A57CFE0A23F2",
            'url': url
        })
        json_data = response.json()
        if 'data' in json_data:
            data = {
                'title': json_data['data']['desc'],
                'formats': [{
                    'url': json_data['data']['playAddr'],
                    "ext": "mp4",
                    "video_ext": "mp4",
                }],
                'url': json_data['data']['playAddr'],
                'original_url': url,
                'thumbnail': json_data['data']['cover'],
                'music': json_data['data']['music']
            }
            return data
    else:
        print('{}'.format(json_data['message']))
        raise json_data['message']


def main():
    uvicorn.run('main:app', host="0.0.0.0", port=9527, reload=True)


if __name__ == '__main__':
    # 运行fastapi程序
    main()
