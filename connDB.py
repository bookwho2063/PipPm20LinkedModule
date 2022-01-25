# -*- coding: utf-8 -*-

import sys, os
import pymssql
from win32api import GetComputerName

class connDB:

    def __init__(self):
        self.server = GetComputerName() + "\PMPLUS20"
        self.user = "withpharm"
        self.password = "withpm2022@"
        self.dbName = "master"

    def openDB(self):
        """
        MS-SQL DB 커넥션 OPEN
        :return:
        """
        print("(로그) DB Connection 을 수행합니다.")
        try:
            self.conn = pymssql.connect(self.server, self.user, self.password, self.dbName, charset='utf8')
            self.cursor = self.conn.cursor()
            print("(로그) DB Connection 수행을 완료하였습니다.")
        except Exception as e:
            print("(에러) DB Connection 중 오류가 발생하였습니다.")
            print("(에러 Detail) ", e)


    def closeDB(self):
        """
        MS-SQL DB 커넥션 CLOSE
        :return:
        """
        print("(로그) DB Disconnection 을 수행합니다.")
        try:
            self.conn.close()
        except Exception as e:
            print("(에러) DB Disconnection 중 오류가 발생하였습니다.")
            print("(에러 Detail) ", e)

    def queryRollback(self):
        """
        직전 쿼리를 롤백 처리한다.
        :return:
        """
        try:
            self.conn.rollback()
        except Exception as e:
            print("(에러) Query Rollback 중 오류가 발생하였습니다.")
            print("(에러 Detail) ", e)

    def sendQuery(self, queryMsg):
        """
        쿼리 발송 처리
        :param queryMsg:
        :return: 결과 데이터 Row 전체
        """
        print("(로그) DB Query 를 수행합니다.")
        print("(Query) ", queryMsg)
        try:
            self.cursor.execute(queryMsg)
            resultRow = self.cursor.fetchall()
        except Exception as e:
            print("(에러) sendQuery 중 오류가 발생하였습니다.")
            print("(에러 Detail) ", e)

        return resultRow

if __name__ == "__main__":
    print("connDB.py call")

    db = connDB()
    db.openDB()

    # 1 conn 으로 반복 쿼리 동작 여부 테스트
    for idx in range(1, 10):
        resultRow = db.sendQuery('SELECT * FROM PM_MAIN.dbo.TPHARM_INFO;')
        print(idx, "==================================================")
        for data in resultRow:
            print(data[0])
            print(data[1])
            print(data[2])
            print(data[3])
            print(data[4])
            print(data[5])
            print("==================================================")

    os.system("pause")