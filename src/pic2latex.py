from src.clipboard_cooker import cook_clipboard_pic
import json


def pic2latex(*args, **kwargs):
    res = cook_clipboard_pic(gunner)
    res = json.loads(res.content.decode('UTF-8'))
    if "latex_styled" in res:
        return res["latex_styled"]
    else:
        return res['text']


def uriGen(pri):
    import base64
    ans = "data:image/bmp;base64," + base64.b64encode(pri).decode()
    return ans


def gunner(pri):
    import requests
    url = "https://www.latexlive.com:5001/api/mathpix/posttomathpix"
    data = {"src": uriGen(pri),
            "ocr": ["math", "text"],
            "formats": ["latex_styled"],
            "format_options": {
            "latex_styled": {
                "transforms": ["rm_spaces"]
            }}}
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "15464",
        "Content-Type": "application/json",
        "DNT": "1",
        "Host": "www.latexlive.com:5001",
        "Origin": "https://www.latexlive.com",
        "Referer": "https://www.latexlive.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    # print(res)
    return res


if __name__ == "__main__":
    print(pic2latex())
