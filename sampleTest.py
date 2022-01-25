# -*- coding: utf-8 -*-

import sys, os
import pymssql

from win32api import GetComputerName


class codeTest:
    """
    코드 샘플을 테스트 하는 클래스
    """

    def __init__(self):
        self.server = GetComputerName()+"\PMPLUS20"
        self.user = "withpharm"
        self.password = "withpm2022@"
        self.dbName = "master"


    def connMdfDB(self):
        """
        MDF DB Connection
        :return:
        """
        print("connMdfDB call")
        print("PC-NAME :: ", GetComputerName())
        try:
            cnxn = pymssql.connect(self.server, self.user, self.password, self.dbName, charset='utf8')
            print("커넥션 완료")
            print(cnxn)
            cursor = cnxn.cursor()

            cursor.execute('SELECT * FROM PM_MAIN.dbo.TPHARM_INFO;')
            print("쿼리 돌린다.")
            row = cursor.fetchall()

            for data in row:
                print(data[0])
                print(data[1])
                print(data[2])
                print("==================================================")

            print("conn close")
            cnxn.close()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    print("HI")
    tClass = codeTest()
    tClass.connMdfDB()