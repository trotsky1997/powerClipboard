
import translators as ts
from src.trans.iciba import iciba
from src.trans.BaiduTranslate import baidu, baidudeep
from src.trans.sogou import translate as sogou
from src.trans.xiaoniu import xiaoniuTrans

vendors = ["google", "tencent", "alibaba",
           "youdao", "baidu", "bing", "iciba", "sougou", "xiaoniu", "baidu2"]  # "deepl",
# vendors = ["raw","deepl","sougou"]
engines = {
    "google": ts.google,
    "tencent": ts.tencent,
    "alibaba": ts.alibaba,
    "deepl": ts.deepl,
    "youdao": ts.youdao,
    "baidu": baidu,
    "bing": ts.bing,
    "iciba": iciba,
    "sougou": sogou,
    "baidu2": baidudeep,
    "xiaoniu": xiaoniuTrans,
}


def mt(val="", vendor="google", from_language='en', to_language='zh'):
    engine = engines[vendor]
    try:
        result = engine(val, from_language=from_language,
                        to_language=to_language)
    except:
        result = 'Failed.'
    # print(result)
    return result
