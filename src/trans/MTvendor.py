
import translators as ts
from src.trans.iciba import iciba
from src.trans.BaiduTranslate import baidu
from src.trans.sogou import translate as sogou
from src.trans.xiaoniu import xiaoniuTrans
import time

vendors = ["google", "tencent", "alibaba", "deepl",
           "youdao", "baidu", "bing", "iciba", "sougou", "xiaoniu", "baidu2"]  # "deepl",
# vendors = ["raw","deepl","sougou"]
engines = {
    "google": ts.google,
    "tencent": ts.tencent,
    "alibaba": ts.alibaba,
    "deepl": ts.deepl,
    "youdao": ts.youdao,
    "baidu": ts.baidu,
    "bing": ts.bing,
    "iciba": iciba,
    "sougou": sogou,
    "baidu2": baidu,
    "xiaoniu": xiaoniuTrans,
}


def mt(val="", vendor="google", from_language='en', to_language='zh'):
    engine = engines[vendor]
    try:
        result = engine(val, from_language=from_language,
                        to_language=to_language)
    except:
        try:
            sub = vendors[int(time.time()) % len(vendors)]
            result = engines[sub](val, from_language=from_language,
                                  to_language=to_language)
        except:
            result = 'Failed.'
    # print(result)
    return result
