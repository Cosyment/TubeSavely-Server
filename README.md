# TubeSavely

TubeSavely is an open-source Python project that provides an API service for parsing video information from various video hosting websites. It leverages the powerful [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) library to extract video details and download links.

## Features

- Parse video information from multiple video hosting platforms
- Provide direct download links for videos
- RESTful API for easy integration with other applications
- Simple deployment for self-hosted solutions

## Requirements

- Python 3.12 or higher
- yt-dlp 2024.07.09 or higher

## Installation

1. Clone the repository:git clone https://github.com/Cosyment/TubeSavely.git
   cd TubeSavely
2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install the required dependencies:
   pip install -r requirements.txt

## Usage

1. Start the API server:
   python app.py
2. Send a POST request to the `/parse` endpoint with the video URL:
   `curl -X POST http://localhost:5000/parse -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'`
3. The API will respond with JSON containing the parsed video information and download links.

## API Documentation

### POST /parse

Parse video information from a given URL.

**Request Body:**
```json
{
"url": "https://www.example.com/video"
}
```
**Response:**
~~~json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": "39091936",
    "formats": [
      {
        "format_id": "0",
        "format_index": null,
        "url": "https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/96be72289633296f-b49c69b688c2be9d889dac961da9d965-hls_360p_2.m3u8?pkey=ABCza86_-9cRur8DgFYCXgavZiC-QSPT3sjJPpf9fGYF1TyN2mXb7bBNA_2G9C3B37362lvwMFu9DIU0HxoLP5ND_0YeulSP6AiXfA3P08YV4NSzjg0vE6oPvhx-6uEw4xEP2QnKzRmMBfC9soUKYdidGmLQoC63pQJ2snymsAXoDc0MzD7hbGcQVmUC93_ogdo_gXiy2CuNeRxkzgZL2WyhKvXJvCFw2m_hv0dSfFPaVjy3CDJY0X5O6kYe7UzcN3c&safety_id=AAI4KIcJFUCxquYcnXjvK_Hv",
        "ext": "mp4",
        "protocol": "m3u8_native",
        "preference": null,
        "quality": null,
        "has_drm": false,
        "fps": 30,
        "width": 640,
        "height": 360,
        "tbr": 480,
        "resolution": "640x360",
        "dynamic_range": "SDR",
        "aspect_ratio": 1.78,
        "filesize_approx": 21387000,
        "cookies": "_did=web_634527202E5E01FA; Domain=.acfun.cn; Path=/; Expires=1754404186; safety_id=AAI4KIcJFUCxquYcnXjvK_Hv; Domain=.acfun.cn; Path=/; Expires=1722954585",
        "http_headers": {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "en-us,en;q=0.5",
          "Sec-Fetch-Mode": "navigate",
          "Referer": "https://www.acfun.cn/"
        },
        "video_ext": "mp4",
        "audio_ext": "none",
        "vbr": null,
        "abr": null,
        "format": "0 - 640x360"
      },
      {
        "format_id": "1",
        "format_index": null,
        "url": "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/96be72289633296f-932d841fd1b2d80683fe2410947450db-hls_540p_2.m3u8?pkey=ABD8wozYhNd2sjsTV4EJVcVvFi27YDWqcTuNAa2YhuUFXLptTv992aZ7OILUfgXaaWZKrDilnCjMZ8-Sm7wQVGz2MfnlGLuTLxOZ6KSBPToK22e-Iyqp7H6PcG94OQKJK1t3dFWEMhY5dK52oqRavtFv-q_qOgF6l5BJWBwyEHPuEJDC-ln0_C0qiYe6SsDJ23lrvVd1pN66pzOI7IjH3kH4OdbST43YoTtHsldxtAth6HZ1AuIl_mt7Lmd6lzorcuI&safety_id=AAI4KIcJFUCxquYcnXjvK_Hv",
        "ext": "mp4",
        "protocol": "m3u8_native",
        "preference": null,
        "quality": null,
        "has_drm": false,
        "fps": 30,
        "width": 960,
        "height": 540,
        "tbr": 804,
        "resolution": "960x540",
        "dynamic_range": "SDR",
        "aspect_ratio": 1.78,
        "filesize_approx": 35823225,
        "cookies": "_did=web_634527202E5E01FA; Domain=.acfun.cn; Path=/; Expires=1754404186; safety_id=AAI4KIcJFUCxquYcnXjvK_Hv; Domain=.acfun.cn; Path=/; Expires=1722954585",
        "http_headers": {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "en-us,en;q=0.5",
          "Sec-Fetch-Mode": "navigate",
          "Referer": "https://www.acfun.cn/"
        },
        "video_ext": "mp4",
        "audio_ext": "none",
        "vbr": null,
        "abr": null,
        "format": "1 - 960x540"
      },
      {
        "format_id": "2",
        "format_index": null,
        "url": "https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/96be72289633296f-cfac4e7055daaecc6c802a4a434f9105-hls_720p_2.m3u8?pkey=ABB5Mb5jU2soVD6Cc2VeCH0bRkt5ngjEhFwgUTjdZ5-2ru8iQG9JWIBi1ObT6lnAKiT1LYpMQntNBMHH0Cr2ZPGQg1i1KyD1bYmai9GoJ2SYY3xgw8elyX1GktDnBFZhkp1d9LFkpT9RSzwYtNQ9Lm1x2vSkUcIn57VKZgHNXPt3Ywn70gsGAj7uED5Xv3Kzhn1HgKt3MvRwSZHbZ2UEqW9FeeLnJMHnHsbN-rcd8S3FIxBptSwrMy4LEDE2Hg0tL7s&safety_id=AAI4KIcJFUCxquYcnXjvK_Hv",
        "ext": "mp4",
        "protocol": "m3u8_native",
        "preference": null,
        "quality": null,
        "has_drm": false,
        "fps": 30,
        "width": 1280,
        "height": 720,
        "tbr": 1394,
        "resolution": "1280x720",
        "dynamic_range": "SDR",
        "aspect_ratio": 1.78,
        "filesize_approx": 62111412,
        "cookies": "_did=web_634527202E5E01FA; Domain=.acfun.cn; Path=/; Expires=1754404186; safety_id=AAI4KIcJFUCxquYcnXjvK_Hv; Domain=.acfun.cn; Path=/; Expires=1722954585",
        "http_headers": {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "en-us,en;q=0.5",
          "Sec-Fetch-Mode": "navigate",
          "Referer": "https://www.acfun.cn/"
        },
        "video_ext": "mp4",
        "audio_ext": "none",
        "vbr": null,
        "abr": null,
        "format": "2 - 1280x720"
      },
      {
        "format_id": "3",
        "format_index": null,
        "url": "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/96be72289633296f-36be6c261fa57cfa2128c6fde7020787-hls_1080p_2.m3u8?pkey=ABBu9jSr-O0SF4zXF1DZCq3LYYIMHq9Y5HYb6jyty2espxdmJtZwfOa9b1CYxiwgrj9rD6Q8QxRjPXW3_JA4nTHNs_28nhXZaqvOYYADCqvcO5L4Ey3O885vHakySZNCi_Af398CXwp047H5dWkrNxeYQO_xU-Sm-Cj_-OolgGECbcm1Zoc6QCsjItRc9qcBrn_uU1ItWYvf4dfD8o3qaW-KRqEAWRmfAQSUVmTeZjkTJ1Xo6yZ0xC5HCCO9AHg27hA&safety_id=AAI4KIcJFUCxquYcnXjvK_Hv",
        "ext": "mp4",
        "protocol": "m3u8_native",
        "preference": null,
        "quality": null,
        "has_drm": false,
        "fps": 30,
        "width": 1920,
        "height": 1080,
        "tbr": 2312,
        "resolution": "1920x1080",
        "dynamic_range": "SDR",
        "aspect_ratio": 1.78,
        "filesize_approx": 103014050,
        "cookies": "_did=web_634527202E5E01FA; Domain=.acfun.cn; Path=/; Expires=1754404186; safety_id=AAI4KIcJFUCxquYcnXjvK_Hv; Domain=.acfun.cn; Path=/; Expires=1722954585",
        "http_headers": {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "en-us,en;q=0.5",
          "Sec-Fetch-Mode": "navigate",
          "Referer": "https://www.acfun.cn/"
        },
        "video_ext": "mp4",
        "audio_ext": "none",
        "vbr": null,
        "abr": null,
        "format": "3 - 1920x1080"
      }
    ],
    "subtitles": {

    },
    "duration": 356.45,
    "timestamp": 1665125258,
    "http_headers": {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-us,en;q=0.5",
      "Sec-Fetch-Mode": "navigate",
      "Referer": "https://www.acfun.cn/"
    },
    "title": "客人故意不做措施，让艺妓怀孕了，结果接客更方便",
    "thumbnail": "https://tx-free-imgs.acfun.cn/newUpload/71166724_1c624ec486304fa78a3328a79e7a8598.jpeg?imageslim",
    "description": null,
    "uploader": "飞电解说",
    "uploader_id": "71166724",
    "tags": [
      "吐槽",
      "电影杂谈"
    ],
    "view_count": 140962,
    "like_count": 606,
    "comment_count": 65,
    "original_url": "https://m.acfun.cn/v/?ac=39091936",
    "webpage_url": "https://www.acfun.cn/v/ac39091936",
    "webpage_url_basename": "ac39091936",
    "webpage_url_domain": "acfun.cn",
    "extractor": "AcFunVideo",
    "extractor_key": "AcFunVideo",
    "playlist": null,
    "playlist_index": null,
    "thumbnails": [
      {
        "url": "https://tx-free-imgs.acfun.cn/newUpload/71166724_1c624ec486304fa78a3328a79e7a8598.jpeg?imageslim",
        "id": "0"
      }
    ],
    "display_id": "39091936",
    "fulltitle": "客人故意不做措施，让艺妓怀孕了，结果接客更方便",
    "duration_string": "5:56",
    "upload_date": "20221007",
    "release_year": null,
    "requested_subtitles": null,
    "_has_drm": null,
    "epoch": 1722868192,
    "format_id": "3",
    "format_index": null,
    "url": "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/96be72289633296f-36be6c261fa57cfa2128c6fde7020787-hls_1080p_2.m3u8?pkey=ABBu9jSr-O0SF4zXF1DZCq3LYYIMHq9Y5HYb6jyty2espxdmJtZwfOa9b1CYxiwgrj9rD6Q8QxRjPXW3_JA4nTHNs_28nhXZaqvOYYADCqvcO5L4Ey3O885vHakySZNCi_Af398CXwp047H5dWkrNxeYQO_xU-Sm-Cj_-OolgGECbcm1Zoc6QCsjItRc9qcBrn_uU1ItWYvf4dfD8o3qaW-KRqEAWRmfAQSUVmTeZjkTJ1Xo6yZ0xC5HCCO9AHg27hA&safety_id=AAI4KIcJFUCxquYcnXjvK_Hv",
    "ext": "mp4",
    "protocol": "m3u8_native",
    "preference": null,
    "quality": null,
    "has_drm": false,
    "fps": 30,
    "width": 1920,
    "height": 1080,
    "tbr": 2312,
    "resolution": "1920x1080",
    "dynamic_range": "SDR",
    "aspect_ratio": 1.78,
    "filesize_approx": 103014050,
    "cookies": "_did=web_634527202E5E01FA; Domain=.acfun.cn; Path=/; Expires=1754404186; safety_id=AAI4KIcJFUCxquYcnXjvK_Hv; Domain=.acfun.cn; Path=/; Expires=1722954585",
    "video_ext": "mp4",
    "audio_ext": "none",
    "vbr": null,
    "abr": null,
    "format": "3 - 1920x1080"
  }
}
~~~



## App

[TubeSavely](https://github.com/Cosyment/TubeSavely)

[ios&macos](https://apps.apple.com/cn/app/tubesavely/id6503423677)

## Thanks

[yt-dlp](https://github.com/yt-dlp/yt-dlp)



## 激活系统Python虚拟环境

执行这个命令时，shell会话将被配置为使用虚拟环境中的Python解释器和库，而不是系统默认的Python版本。任何Python相关的命令都会使用虚拟环境中的Python解释器和库。可以安装、升级和卸载包，而不会影响系统级别的Python环境。e.g.

创建并激活当前项目虚拟环境
~~~
python3 -m venv /path/to/your/project/venv  #创建
source /Users/Waiting/PycharmProjects/TubeSavely/venv/bin/python/bin/activate #激活
~~~

查看当前虚拟环境路径

~~~
echo $PYTHONPATH
~~~

退出虚拟环境

~~~
deactivate
~~~

生成当前虚拟环境所有依赖库列表文件

~~~
pip freeze > requirements.txt
~~~

安装requirements.txt

~~~
pip install -r requirements.txt
