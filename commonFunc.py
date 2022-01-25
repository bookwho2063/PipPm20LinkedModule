# -*- coding: utf-8 -*-

import sys, os, time

class commonFunc:
    def __init__(self):
        pass

    def getTime(self):
        now = time.localtime()
        self.nowTime =" [%04d-%02d-%02d %02d:%02d:%02d] " % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        return self.nowTime