## 使用SCF实现日志文件的统计分析

在本Demo中，我们用到了无服务器云函数 SCF，对象存储 COS，MySQL数据库。其中，对象存储 COS 用来存储需要分析的日志文件，云函数 SCF 实现从 COS 下载日志文件并进行统计分析，把分析的结果写入到MySQL数据库中。


### 步骤一 创建 COS Bucket

首先要到 COS 的控制台创建一个 Bucket，我们可以命名为 loganalysis，并选择“北京”地域，权限选择“公有读-私有写”。

### 步骤二 创建 MySQL数据库

由于数据库需要花钱购买，您可以选择在北京地域购买最便宜的[“云数据库MySQL入门机型”](https://cloud.tencent.com/act/event/cdbbasic.html)，价格为12元/月。

### 步骤三 创建云函数 SCF

首先确保在您的系统中已经安装好了 Python 运行环境和pip工具，然后在本地创建需要放置函数代码的文件夹，并通过命令行进入该目录下，安装数据库操作相关的库，可以直接执行命令：
```
pip install cos-python-sdk-v5 -t .
pip install pymysql -t .
pip install cryptography -t .
```
在函数代码文件夹的根目录下，创建 Python 文件，可以命名为：LogAnalysis.py，并使用如下示例代码：
```
# -*- coding: utf-8 -*-
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError

from datetime import datetime
from time import time
import re
import operator
import pymysql.cursors
import logging

# MySql数据库
Host='******' #如bj-cdb-cj9w3q53.sql.tencentcdb.com
User='xxxxx'
Password='xxxxx'
Port= 63054
DB=u'******' # 如SCF_Demo

# COS
appid = ********  # 请替换为您的 APPID
secret_id = u'********'  # 请替换为您的 SecretId
secret_key = u'********'  # 请替换为您的 SecretKey
region = u'ap-beijing'
token = ''

config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)
logger = logging.getLogger()


def main_handler(event, context):
    # Authentication Information
    print("Start Request {}", datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'))

    # Start downloading from COS
    for record in event['Records']:
        try:
            bucket = record['cos']['cosBucket']['name'] + '-' + str(appid)
            key = record['cos']['cosObject']['key']
            key = key.replace('/' + str(appid) + '/' + record['cos']['cosBucket']['name'] + '/', '', 1)
            download_path = '/tmp/{}'.format(key)
            print("Key is " + key)
            print("Get from [%s] to download file [%s]" % (bucket, key))
            try:
                response = client.get_object(Bucket=bucket, Key=key, )
                response['Body'].get_stream_to_file(download_path)
            except CosServiceError as e:
                print(e.get_error_code())
                print(e.get_error_msg())
                print(e.get_resource_location())
                return "Download log fail"
            logger.info("Download file [%s] Success" % key)
        except Exception as e:
            print(e)
            raise e
            return "Access COS Fail"

        print("Start analyzing data {}", datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlList = {}
        statuelist = {}
        terminalList = {}
        timeList = {"24/May/2018 10:00-10:30": 0, "24/May/2018 10:30-11:00": 0}

        fileObject = open(download_path, 'rU')
        try:
            for line in fileObject:
                # Count URL
                URLstart = re.search("GET", line)
                URLend = re.search("mp4", line)
                if URLstart and URLend:
                    url = line[URLstart.end() + 1: URLend.end()]
                    if url in urlList:
                        urlList[url] += 1
                    else:
                        urlList[url] = 1

                # Count Statue code
                Statuestart = re.search("HTTP/1.1", line)
                if Statuestart:
                    StatueCode = line[Statuestart.end() + 2: Statuestart.end() + 5]
                    if StatueCode in statuelist:
                        statuelist[StatueCode] += 1
                    else:
                        statuelist[StatueCode] = 1

                # Count Terminal Device
                Terminalstart = re.search("\"-\"", line)
                TerminalEnd = re.search("\"-\" \"-\"", line)
                if Terminalstart and TerminalEnd:
                    terminal = line[Terminalstart.end() + 2: TerminalEnd.start() - 2]
                    if terminal in terminalList:
                        terminalList[terminal] += 1
                    else:
                        terminalList[terminal] = 1

                # Count Timelist
                Timestarter = re.search("\[", line)
                if Timestarter:
                    if int(line[Timestarter.end() + 15: Timestarter.end() + 17]) > 30:
                        timeList["24/May/2018 10:30-11:00"] += 1
                    else:
                        timeList["24/May/2018 10:00-10:30"] += 1

        finally:
            fileObject.close()

        # Sort Result according to frequence
        URL_sorted_res = sorted(urlList.items(), key=operator.itemgetter(1), reverse=True)
        Statue_sorted_res = sorted(statuelist.items(), key=operator.itemgetter(1), reverse=True)
        Terminal_sorted_res = sorted(terminalList.items(), key=operator.itemgetter(1), reverse=True)
        Time_sorted_res = sorted(timeList.items(), key=operator.itemgetter(1), reverse=True)

        URLres = []
        Statueres = []
        Terminalres = []
        Timeres = []

        for i in range(3):
            URLres.append(URL_sorted_res[i])
            Statueres.append(Statue_sorted_res[i])
            Terminalres.append(Terminal_sorted_res[i])

        for i in range(2):
            Timeres.append(Time_sorted_res[i])

        print("Analyzing Successfully, Start writing to database {}",
              datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'))

        connection = pymysql.connect(host=Host,
                                     user=User,
                                     password=Password,
                                     port=Port,
                                     db= DB,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Clean dirty data
                cursor.execute("DROP TABLE IF EXISTS url")
                cursor.execute("DROP TABLE IF EXISTS state")
                cursor.execute("DROP TABLE IF EXISTS terminal")
                cursor.execute("DROP TABLE IF EXISTS time")
                cursor.execute("CREATE TABLE url (URL TEXT NOT NULL, Count INT)")
                cursor.execute("CREATE TABLE state (StateCode TEXT NOT NULL, Count INT)")
                cursor.execute("CREATE TABLE terminal (Terminal TEXT NOT NULL, Count INT)")
                cursor.execute("CREATE TABLE time (Timestatue TEXT NOT NULL, Count INT)")

                sql = "INSERT INTO `url` (`URL`, `Count`) VALUES (%s, %s)"
                for i in range(len(URLres)):
                    cursor.execute(sql, (URLres[i][0], URLres[i][1]))

                sql = "INSERT INTO `state` (`StateCode`, `Count`) VALUES (%s, %s)"
                for i in range(len(Statueres)):
                    cursor.execute(sql, (Statueres[i][0], Statueres[i][1]))

                sql = "INSERT INTO `terminal` (`Terminal`, `Count`) VALUES (%s, %s)"
                for i in range(len(Terminalres)):
                    cursor.execute(sql, (Terminalres[i][0], Terminalres[i][1]))

                sql = "INSERT INTO `time` (`Timestatue`, `Count`) VALUES (%s, %s)"
                for i in range(len(Timeres)):
                    cursor.execute(sql, (Timeres[i][0], Timeres[i][1]))

            connection.commit()

        finally:
            connection.close()

        print("Write to database successfully {}", datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'))
        return "LogAnalysis Success"
```
注意：在使用本段代码的时候，需要把 appid、secret_id和secret_key 替换为您自己的 appid、secret_id和secret_key 后方能使用，您可以在“账号信息”中查看对应信息。

保存后，回到根目录下，对所有文件进行打包，注意不是对外层的文件夹打包；另外还需要保证：LogAnalysis.py存在于根目录下，压缩包需要为zip格式。
打包完成后，我们就可以前往云函数 SCF 控制台进行部署。选择“北京”地域，单击“创建函数”，命名函数为 Demo3_LogAnalysis，函数超时时间修改为10s，内存默认128M即可。单击“下一步”，选择“本地上传zip包”，注意执行方法填写为：LogAnalysis.main_handler，“保存”后单击“下一步”，选择触发方式为COS触发，选择步骤一中创建好的Bucket: loganalysis，事件类型为文件上传，单击“保存”后，再单击“完成”，完成函数部署。

在这里，您也可以直接下载[git](https://github.com/Masonlu/SCF-Demo/tree/master/Demo3_LogAnalysis)中提供的项目文件，并打成zip包，通过控制台创建函数并完成部署，注意：
1.在打zip包的时候，请不要包含“demo-scf1.txt”和“demo-scf2.txt”，否则zip包有可能会超过5MB；2.在“函数代码”中需修改appid、secret_id和secret_key并保存。

### 步骤四 测试函数功能
进入COS控制台，选择创建好的Bucket:loganalysis,点击“上传文件”，选择[git](https://github.com/Masonlu/SCF-Demo/tree/master/Demo3_LogAnalysis)中提供的样例日志文件demo-scf1.txt，然后上传。回到 SCF 控制台查看执行结果，在“日志”中可以看到打印出来的日志信息。然后前往MySQL管理界面，查看分析结果。回到COS控制台，选择上传demo-scf2.txt，然后查看SCF的执行结果和MySQL中的分析结果。
这里可以根据用户自身的日志格式编写具体的处理方法，数据库的写方法也可以改成增量写。

