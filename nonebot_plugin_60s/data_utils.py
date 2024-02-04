import asyncio
from typing import Dict, List, Any
import aiofiles
from nonebot.log import logger
import json
from nonebot import require
require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store


data_file = store.get_data_file("nonebot_plugin_60s","data.json")
lock = asyncio.Lock()

def get_datas():
    subscribe_list = json.loads(data_file.read_text(
    "utf-8")) if data_file.is_file() else {}
    return subscribe_list
def save_subscribe(subscribe_list: Any):
    data_file.write_text(json.dumps(subscribe_list), encoding="utf-8")