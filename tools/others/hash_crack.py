# coding=utf-8
from core import BestKaliTools
from core import BestKaliToolssCollection


class HashBuster(BestKaliTools):
    TITLE = "Hash Buster"
    DESCRIPTION = "Features: \n " \
                  "Automatic hash type identification \n " \
                  "Supports MD5, SHA1, SHA256, SHA384, SHA512"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Hash-Buster.git",
        "cd Hash-Buster;make install"
    ]
    RUN_COMMANDS = ["buster -h"]
    PROJECT_URL = "https://github.com/s0md3v/Hash-Buster"


class HashCrackingTools(BestKaliToolssCollection):
    TITLE = "Hash cracking tools"
    TOOLS = [HashBuster()]
