from src.clipboard_cooker import cook_clipboard_pic
from aip import AipOcr


def pic2text(*args, **kwargs):
    client = AipOcr("21478454", "x6IitgGYUNAMAZliI3nhoaoR",
                    "hwAy2FkcTv0GFdTLMYbhDdh9P1nfLE37")
    ans = cook_clipboard_pic(client.basicGeneral)
    ans0 = [i['words'] for i in ans['words_result']]
    ans = " ".join(ans0)
    # #print(ans)
    return ans
    # except:
    #     pass
