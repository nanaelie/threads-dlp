import re
import pathlib
from datetime import datetime

def get_username(url: str) -> str | None:
    usernames = re.findall(r'/@([a-zA-Z._]+)/', url)
    if usernames:
        username = usernames[0]
        return username
    else:
        return None

def get_extension(url: str) -> str:
    pass

def strftime():
    return datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

def out_path(url):
    uname = get_username(url)
    strtime = strftime()
    path = '@' + uname + '-' + strtime if uname else strtime
    return path

