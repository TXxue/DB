# -*- coding: utf-8 -*-
'''
    @File        test  dblib MysqlConnector
    @Author
    @Created On 2018-04-04
    @Updated On 2018-04-08
'''
import os
import sys
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)

from dblib.MysqlConnector import MysqlConnector
import time
reload(sys)
sys.setdefaultencoding('utf8')


def main():
    xmlpath = '../conf/SysSet.xml'
    testTable = "TestTable"

    start_time = time.time()

    db = MysqlConnector(xmlpath)

    # # create table
    # ret = db.create_test(testTable)
    # if not ret:
    #     print("create table [%s] failed!!!" % testTable)
    # print("create table [%s] succeed!!!" % testTable)

    # # insert info
    # for i in range(0, 10):
    #     insertInfo = {'Name':'aa_'+str(i), 'Num':i, 'Content': 'aabbccdd_'+str(i)*6, 'Time':int(time.time())}
    #     db.insert_test(testTable, insertInfo)
    # for i in range(10, 20):
    #     insertInfo = {'Name':'bb_'+str(i), 'Num':i, 'Content': 'aabbccdd_'+str(i)*6, 'Time':int(time.time())}
    #     db.insert_test(testTable, insertInfo)

    end_time = time.time()
    print("Insert  time: %d" % (end_time-start_time))

    # find_one
    queryInfo = {'filed':'Num', 'value': '5'}
    result = db.find_one_test(testTable, queryInfo)
    print("find_one_test : ", result)

    # find_many
    queryInfo = {'filed':'Name', 'value': 'aa'}
    # queryInfo = {'filed':'Num', 'value': '5'}
    result2 = db.find_many_test(testTable, queryInfo, limit=10)
    for item in result2:
        print(item)

    print("\n")
    result2 = db.find_test(testTable, startid=3)
    for item in result2:
        print(item)

    lastNum = db.get_last_Id_test(testTable)
    print("The last Id: %s"% str(lastNum))



if __name__ == "__main__":
    main()