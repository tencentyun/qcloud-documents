本文为您介绍通过 RESTful API 方式访问 TcaplusDB 表的操作。

通过注册游戏、开通服务、添加表步骤后，您就有了属于自己的 TcaplusDB 业务数据表，通过获取到的访问点信息就能够对业务数据表进行读写访问。本示例将分别采用 SetRecord 和 GetRecord 接口对目标表进行写和读操作。

>!相关操作需要在用户腾讯云账号下申请的 CVM 中进行。

在本例中，假设获取到如下接入点信息，并且在 ZoneId 为1的部署单元中创建了表 tb_online。
* AppId：2
* AppKey：3aa84dd773826cd655e9f24a249d68bb
* RESTful 接入点：10.123.9.70:31002
* ZoneId：1

## 写操作
通过如下 HTTP 请求向表中写入一条数据。对应的请求 url、HTTP 请求头、请求数据和回包如下：

```
HTTP Method: POST
req_url:
http://10.123.9.70:31002/ver1.0/apps/2/zones/1/tables/tb_online/records
HTTP header:
[
 "x-tcaplus-target:Tcaplus.SetRecord", 
 "x-tcaplus-version:Tcaplus3.32.0", 
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82", 
 "x-tcaplus-result-flag:1", 
 "x-tcaplus-data-version-check:1", 
 "x-tcaplus-data-version:-1", 
 "x-tcaplus-idl-type:Protobuf"
]
Data:
{
 "ReturnValues": "user define data", 
 "Record": {
  "name": "tcaplus_user", 
  "lockid": [
   50, 
   60, 
   70, 
   80, 
   90, 
   100
  ], 
  "pay": {
   "pay_times": 184, 
   "total_money": 100000, 
   "pay_id": 12000, 
   "auth": {
    "pay_keys": "njaklhewunfasdjnuonawef", 
    "update_time": 1544018596
   }
  }, 
  "region": 10, 
  "uin": 1024, 
  "is_available": true, 
  "gamesvrid": 5000, 
  "logintime": 100
 }
}
----------------------------------------
Resp Status 200
cost:9 ms
Response
{
 "ReturnValues": "aaaaaaaaaa", 
 "RecordVersion": 1, 
 "ErrorMsg": "Succeed", 
 "ErrorCode": 0, 
 "Record": {
  "name": "tcaplus_user", 
  "lockid": [
   50, 
   60, 
   70, 
   80, 
   90, 
   100
  ], 
  "pay": {
   "pay_times": 184, 
   "total_money": 100000, 
   "pay_id": 12000, 
   "auth": {
    "pay_keys": "njaklhewunfasdjnuonawef", 
    "update_time": 1544018596
   }
  }, 
  "region": 10, 
  "uin": 1024, 
  "is_available": true, 
  "gamesvrid": 5000, 
  "logintime": 100
 }
}
```

## 读操作

通过如下 HTTP 请求将上一步写入的记录读取出来。对应的请求 url、HTTP 请求头和回包如下：

```
HTTP Method: GET
req_url:
http://10.123.9.70:31002/ver1.0/apps/2/zones/1/tables/tb_online/records?keys=%7B%22region%22%3A%2010%2C%20%22name%22%3A%20%22tcaplus_user%22%2C%20%22uin%22%3A%201024%7D
HTTP 请求Header:
[
 "x-tcaplus-target:Tcaplus.GetRecord", 
 "x-tcaplus-version:Tcaplus3.32.0", 
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82", 
 "x-tcaplus-idl-type:protobuf"
]
----------------------------------
应答状态 200
Response:
{
 "RecordVersion": 2, 
 "Record": {
  "name": "tcaplus_user", 
  "lockid": [
   50, 
   60, 
   70, 
   80, 
   90, 
   100
  ], 
  "pay": {
   "pay_times": 184, 
   "total_money": 100000, 
   "pay_id": 12000, 
   "auth": {
    "pay_keys": "njaklhewunfasdjnuonawef", 
    "update_time": 1544018596
   }
  }, 
  "region": 10, 
  "uin": 1024, 
  "is_available": true, 
  "gamesvrid": 5000, 
  "logintime": 100
 }, 
 "ErrorMsg": "Succeed", 
 "ErrorCode": 0
}
```

## 示例程序

以下通过简单的 Python 代码来实现上面所演示的两个功能。更多的表操作请参考 [Tcaplus RESTful API 接口文档](https://cloud.tencent.com/document/product/596/31664)。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : tcaplus
# created : 2018.11.12
##########################
import sys
import time
import OS
import json
import pycurl
import StringIO
import hashlib
from urllib import unquote, quote 

############################################
#用户的app和表信息
CGI_URL = "http://xx.xx.xx.xx:xxxxx/ver1.0"
APP_ID_INT = 2
ZONE_ID_INT = 1
GAME_KEY_STR = "xxxxxxxxxxxx"
TABLE_NAME_STR = "tb_online"
############################################

def op_get(url, header):
    '''发送HTTP Get请求'''
    ret = None
    curl_fp = None

    try:  
        curl = pycurl.Curl()
        curl.setopt(pycurl.HTTPHEADER, header)
        curl.setopt(pycurl.CONNECTTIMEOUT, 60)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.CUSTOMREQUEST, "GET")
        curl_fp = StringIO.StringIO()
        curl.setopt(pycurl.URL, url.encode('utf-8'))
        curl.setopt(curl.WRITEFUNCTION, curl_fp.write)
        curl.perform()
        ret = json.loads(curl_fp.getvalue())
        print "Resp Status %d" %(curl.getinfo(pycurl.RESPONSE_CODE))
        return ret
    except pycurl.error, err_msg:
        print err_msg
    finally:
        if curl_fp:
            curl_fp.close()
        curl.close()

def op_put(url, header, content):
    '''发送http put请求'''
    ret = None
    try:
        curl = pycurl.Curl()
        curl.setopt(pycurl.HTTPHEADER, header)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.MAXREDIRS, 5)
        curl.setopt(pycurl.CONNECTTIMEOUT, 60)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.HTTPPROXYTUNNEL, 1)
        curl_fp = StringIO.StringIO()
        curl.setopt(pycurl.CUSTOMREQUEST, "PUT")
        curl.setopt(curl.POSTFIELDS, content)
        curl.setopt(pycurl.URL, str(url))
        curl.setopt(curl.WRITEFUNCTION, curl_fp.write)
        curl.perform()

        ret = json.loads(curl_fp.getvalue())
        print "Resp Status %d" %(curl.getinfo(pycurl.RESPONSE_CODE))
    except pycurl.error, err_msg:
        print err_msg
    finally:
        if curl_fp:
            curl_fp.close()
        curl.close()
    return ret

def test_GetRecord():
    #填充key字段
    keys ={"uin":1024,
           "name":"tcaplus_user",
           "region":10}

    #填充 HTTP header
    header = []
    header.append("x-tcaplus-target:Tcaplus.GetRecord")
    header.append("x-tcaplus-version:Tcaplus3.32.0")
    header.append("x-tcaplus-pwd-md5:%s" %(hashlib.md5(GAME_KEY_STR).hexdigest()))
    header.append("x-tcaplus-idl-type:protobuf")

    #设置请求url
    #select属性需要urlencode处理
    req = '%s/apps/%d/zones/%d/tables/%s/records?keys=%s' \
                    %(CGI_URL, APP_ID_INT, ZONE_ID_INT, TABLE_NAME_STR, quote(json.dumps(keys)))

    print "req_url:\n%s" %req
    print "HTTP header:"
    print header
    #发送get请求
    ret = op_get(req, header)
    print "Response:"
    print ret

def test_SetRecord():
    #填充 HTTP header
    header = []
    header.append("x-tcaplus-target:Tcaplus.SetRecord")
    header.append("x-tcaplus-version:Tcaplus3.32.0")
    header.append("x-tcaplus-pwd-md5:%s" %(hashlib.md5(GAME_KEY_STR).hexdigest()))
    header.append("x-tcaplus-result-flag:1")
    header.append("x-tcaplus-data-version-check:1")
    header.append("x-tcaplus-data-version:-1")
    header.append("x-tcaplus-idl-type:Protobuf")

    str_user_buff = "test user buff"
    print "user buff len:%s" %(len(str_user_buff))

    #需要设置的数据记录
    data = {}
    data["Record"] = {}
    data["Record"]["uin"] = 1024
    data["Record"]["name"] = "tcaplus_user"
    data["Record"]["region"] = 10
    data["Record"]["gamesvrid"] = 5000
    data["Record"]["logintime"] = 100
    data["Record"]["lockid"] = [50, 60, 70, 80, 90, 100]
    data["Record"]["is_available"] = True
    data["Record"]["pay"] = {}
    data["Record"]["pay"]["pay_id"] = 12000
    data["Record"]["pay"]["pay_times"] = 184
    data["Record"]["pay"]["total_money"] = 100000
    data["Record"]["pay"]["auth"] = {}
    data["Record"]["pay"]["auth"]["pay_keys"] = "njaklhewunfasdjnuonawef"
    data["Record"]["pay"]["auth"]["update_time"] = 1544018596
    data["ReturnValues"] = str_user_buff

    #填充请求
    req = '%s/apps/%d/zones/%d/tables/%s/records' \
                    %(CGI_URL, APP_ID_INT, ZONE_ID_INT, TABLE_NAME_STR)
    req_data_str = json.dumps(data)
    print "req_url:\n %s" %req
    print "Http header:"
    print header
    print "Data:"
    print '-' * 40
    print data
    print '-' * 40
    ret = op_put(req, header, req_data_str)
    print "Response"
    print ret

if __name__=='__main__':
    test_SetRecord()
    print '*' * 40
    test_GetRecord()
```
