from typing import Tuple
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    calendar_cookie: str = ""    # 填写微信公众号的cookie
    calendar_token: str = ""   # 填写微信公众号的token
    calendar_api_list: list = ["https://api.03c3.cn/api/zb", "https://api.jun.la/60s.php?format=image", "http://bjb.yunwj.top/php/tp/60.jpg"]   # 填写api地址
