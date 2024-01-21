# coding=utf-8
import os
from time import sleep

from core import BestKaliTools
from core import BestKaliToolssCollection


class UpdateTool(BestKaliTools):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update BestKaliTools", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/BestKaliTools/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/BestKaliTools/;"
                  "mkdir BestKaliTools;"
                  "cd BestKaliTools;"
                  "git clone https://github.com/Z4nzu/BestKaliTools.git;"
                  "cd BestKaliTools;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(BestKaliTools):
    TITLE = "Uninstall BestKaliTools"
    DESCRIPTION = "Uninstall BestKaliTools"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("BestKaliTools started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/BestKaliTools/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/BestKaliTools/;")
        print("\nBestKaliTools Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(BestKaliToolssCollection):
    TITLE = "Update or Uninstall | BestKaliTools"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
