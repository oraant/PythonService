from lib import service_guarder
from lib import service

import win32serviceutil
import win32service
import win32event
import servicemanager
import time
import sys, os

class PythonService(service.WinService):

    _svc_name_ = "TTTTT"  # 服务名
    _svc_display_name_ = "TTTTTTTTTTTTT"  # 服务在windows系统中显示的名称
    _svc_description_ = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"  # 服务的描述

    def main(self):
        for i in range(10):
            with open(r'E:\debug.log', 'a') as f:
                f.write(str(i))
            # print(i)
            time.sleep(1)

if __name__ == '__main__':
    PythonService.parse_command_line()