from .acfun import AcFun
from .base import VideoInfo, VideoSource
from .doupai import DouPai
from .douyin import DouYin
from .haokan import HaoKan
from .huya import HuYa
from .kuaishou import KuaiShou
from .lishipin import LiShiPin
from .lvzhou import LvZhou
from .meipai import MeiPai
from .pipigaoxiao import PiPiGaoXiao
from .pipixia import PiPiXia
from .quanmin import QuanMin
from .quanminkge import QuanMinKGe
from .sixroom import SixRoom
from .weibo import WeiBo
from .weishi import WeiShi
from .xigua import XiGua
from .xinpianchang import XinPianChang
from .zuiyou import ZuiYou
from urllib.parse import parse_qs, urlparse

# 视频来源与解析器的映射关系
video_source_info_mapping = {
    VideoSource.AcFun: {
        "domain_list": ["www.acfun.cn", "m.acfun.cn"],
        "parser": AcFun,
    },
    VideoSource.DouPai: {
        "domain_list": ["doupai.cc"],
        "parser": DouPai,
    },
    VideoSource.DouYin: {
        "domain_list": ["v.douyin.com"],
        "parser": DouYin,
    },
    VideoSource.HaoKan: {
        "domain_list": [
            "haokan.baidu.com",
            "haokan.hao123.com",
        ],
        "parser": HaoKan,
    },
    VideoSource.HuYa: {
        "domain_list": ["v.huya.com","www.huya.com"],
        "parser": HuYa,
    },
    VideoSource.KuaiShou: {
        "domain_list": ["v.kuaishou.com", "www.kuaishou.com"],
        "parser": KuaiShou,
    },
    VideoSource.LiShiPin: {
        "domain_list": ["www.pearvideo.com"],
        "parser": LiShiPin,
    },
    VideoSource.LvZhou: {
        "domain_list": ["weibo.cn"],
        "parser": LvZhou,
    },
    VideoSource.MeiPai: {
        "domain_list": ["meipai.com"],
        "parser": MeiPai,
    },
    VideoSource.PiPiGaoXiao: {
        "domain_list": ["h5.pipigx.com"],
        "parser": PiPiGaoXiao,
    },
    VideoSource.PiPiXia: {
        "domain_list": ["h5.pipix.com"],
        "parser": PiPiXia,
    },
    VideoSource.QuanMin: {
        "domain_list": ["xspshare.baidu.com"],
        "parser": QuanMin,
    },
    VideoSource.QuanMinKGe: {
        "domain_list": ["kg.qq.com"],
        "parser": QuanMinKGe,
    },
    VideoSource.SixRoom: {
        "domain_list": ["6.cn"],
        "parser": SixRoom,
    },
    VideoSource.WeiBo: {
        "domain_list": ["weibo.com"],
        "parser": WeiBo,
    },
    VideoSource.WeiShi: {
        "domain_list": ["isee.weishi.qq.com"],
        "parser": WeiShi,
    },
    VideoSource.XiGua: {
        "domain_list": ["v.ixigua.com", "www.ixigua.com"],
        "parser": XiGua,
    },
    VideoSource.XinPianChang: {
        "domain_list": ["xinpianchang.com"],
        "parser": XinPianChang,
    },
    VideoSource.ZuiYou: {
        "domain_list": ["share.xiaochuankeji.cn"],
        "parser": ZuiYou,
    },
}


def parse_video_share_url(share_url: str) -> VideoInfo:
    """
    解析分享链接, 获取视频信息
    :param share_url: 视频分享链接
    :return:
    """
    source = ""
    for item_source, item_source_info in video_source_info_mapping.items():
        for item_url_domain in item_source_info["domain_list"]:
            if item_url_domain in share_url:
                source = item_source
                break
        if source:
            break

    if not source:
        raise ValueError(f"share url [{share_url}] does not have source config")

    url_parser = video_source_info_mapping[source]["parser"]
    if not url_parser:
        raise ValueError(f"source {source} has no video parser")

    _obj = url_parser()
    video_info = _obj.parse_share_url(share_url)
    return video_info


def parse_video_id(source: VideoSource, video_id: str) -> VideoInfo:
    """
    解析视频ID, 获取视频信息
    :param source: 视频来源
    :param video_id: 视频id
    :return:
    """
    if not video_id or not source:
        raise ValueError("video_id or source is empty")

    id_parser = video_source_info_mapping[source]["parser"]
    if not id_parser:
        raise ValueError(f"source {source} has no video parser")

    _obj = id_parser()
    video_info = _obj.parse_video_id(video_id)
    return video_info


def get_val_from_url_by_query_key(url: str, query_key: str) -> str:
    """
    从url的query参数中解析出query_key对应的值
    :param url: url地址
    :param query_key: query参数的key
    :return:
    """
    url_res = urlparse(url)
    url_query = parse_qs(url_res.query, keep_blank_values=True)

    try:
        query_val = url_query[query_key][0]
    except KeyError:
        raise KeyError(f"url中不存在query参数: {query_key}")

    if len(query_val) == 0:
        raise ValueError(f"url中query参数值长度为0: {query_key}")

    return url_query[query_key][0]
