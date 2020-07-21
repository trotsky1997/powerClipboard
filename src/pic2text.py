from src.clipboard_cooker import cook_clipboard_pic
from aip import AipOcr

APP_ID = ""
API_ID = ""
API_KEY = ""

def pic2text(*args, **kwargs):

    client = AipOcr(APP_ID, API_ID,
                    API_ID)
    ans = cook_clipboard_pic(client.basicGeneral)
    ans0 = [i['words'] for i in ans['words_result']]
    ans = "".join(ans0)
    # print(ans)
    return ans
