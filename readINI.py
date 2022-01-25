# -*- coding: utf-8 -*-

import configparser
from configparser import SafeConfigParser
import pprint, os, sys

class readINI:

    def __init__(self, iniFilePath):
        self.iniPath = iniFilePath

    def readINIFile(self):
        """
        INI 파일을 읽어 옵니다.
        :return:
        """
        try:
            print("##### " + self.iniPath + "경로의 INI 파일을 불러옵니다.")
            config = configparser.ConfigParser()
            config.read(self.iniPath, encoding='utf-8')
            sections = config.sections()

            pprint.pprint(sections)     # section 정보 출력 테스트
        except Exception as e:
            print("##### INI 파일 읽기 실패!!")
            print("##### Error Msg :: " + e)

        return config

    def writeINIFile(self, sectionName, optionName, value):
        """
        INI 설정정보를 업데이트 처리합니다.
        :return: 처리결과 True/False
        """
        try:
            print("##### " + self.iniPath + "경로의 INI 파일을 업데이트 합니다.")
            parser = SafeConfigParser()
            parser.read(self.iniPath)
            parser.set(sectionName, optionName, str(value))

            with open(self.iniPath, "w+") as configFile:
                parser.write(configFile)

            return self.readINIFile()      # INI 다시 불러오기
        except Exception as e:
            print("##### INI 파일 업데이트 실패!!")
            print("##### Error Msg :: " + e)

if __name__ == "__main__":
    print('readINI')
    iniData = readINI('resources/drxsolution.ini')
    iniConfig = iniData.readINIFile()

    dbid = iniConfig['DRXS']['TEST']      # 개별 불러오기
    print('BEFORE dbId :: ')
    print(dbid)

    # INI 정보 업데이트
    iniConfig = iniData.writeINIFile('DRXS', 'TEST', 'YES')

    dbid = iniConfig['DRXS']['TEST']  # 개별 불러오기
    print('AFTER dbId :: ')
    print(dbid)


