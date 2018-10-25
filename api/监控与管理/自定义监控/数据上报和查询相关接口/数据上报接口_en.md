## 1. API Description

This API (PutMonitorData) is used to report data.

1. **This API supports HTTP protocol only, and its domain name port is 8080**.
2. Currently, the domain name "receiver.monitor.tencentyun.com" can only be accessed within Tencent CVM.
3. Region filed in this API is the region where CVM resides in.

Domain name: **receiver.monitor.tencentyun.com:8080**




## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is PutMonitorData.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Namespace | Yes | String	| Namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| Data | Yes | Array | The reported data needs to be encapsulated using JSON format |

"data" is composed as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| dimensions | Yes | Array | Dimension key and value group. The dimension key needs to be identical with the dimension name queried by calling API <a href="/doc/api/255/创建指标" title="Create Metric">Create Metric</a>. Dimension value group can be customized |
| metricName | Yes | String | Metric name. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| value | Yes | Float | Specific data |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. If failed, error codes can be found in section 7 |
| message | String | Error message |

## 4. Example
Input
```
http://receiver.monitor.tencentyun.com:8080/v2/index.php?Action=PutMonitorData
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&Namespace=cvm
&Data=[{"dimensions":{"diskname":"disk1","ip":"172.31.58.160"},"metricName":"diskusage","value":30}]
```
Output
```
{
"code":0,
"message":"OK"
}
```



## 5. Generate Signature field for this API
The signature method of this API is different from that of any other API, as shown below:
For step "2. Generate signature string" of <a href="/doc/api/255/签名方法" title="Signature Method">Signature Method</a>, there are two differences.

### 5.1 Input parameters are different in " Sorting parameters"
In step "2.1 Sorting parameters" of <a href="/doc/api/255/签名方法" title="Signature Method">Signature Method</a>
**The input parameters for this API only contain the following fields:**

| Parameter Name | Description| Parameter Value| 
|---------|---------|---------|
| Action | Method name | PutMonitorData | 
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current time stamp | 1408704141 | 
| Nonce | A random positive integer | 345122 | 
| Region | Region where the instance resides in | gz | 

The result in which parameters are sorted in lexicographical order is as follows:
```		
{
		'Action' : 'PutMonitorData',
		'Nonce' : 345122,
		'Region' : 'gz',
		'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
		'Timestamp' : 1408704141
}
```

### 5.2 Request CVM is different in "Generating original signature string
In step "2.3 Generating original signature string" of <a href="/doc/api/255/签名方法" title="Signature Method">Signature Method</a>
The request CVM in this API:  **receiver.monitor.tencentyun.com**
The resulting string is:
```		
GETreceiver.monitor.tencentyun.com/v2/index.php?Action=PutMonitorData&Nonce=345122&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141
```		

Other steps are the same with those in <a href="/doc/api/255/签名方法" title="Signature Method">Signature Method</a>.


## 6. Example of Data Reporting API (Python)

POST method
``` 
{
	"Action": "PutMonitorData",
	"SecretId": "xxxxxxx",
	"Region": "sh",
	"Timestamp": 1402992826,
	"Nonce": 345122,
	"Signature": "mysignature",
	"Namespace": "pc",
	"Data":[{"dimensions":{"diskname":"sda","ip":"172.31.58.160"},"metricName":"diskusage","value":0.3}]
}

```

``` 
#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import time
import json
import random
import hmac
import hashlib

class NwsSender:
        def init(self):
                self.url='http://receiver.monitor.tencentyun.com:8080/v2/index.php'
                self.timeout=10
        def send_data(self,json_data):
                try:
                        req=urllib2.Request(self.url)
                        req.add_header('Content-Type','application/json')
                        timeout=self.timeout
                        data=json.dumps(json_data)
                        http_ret=urllib2.urlopen(req,data,timeout)
                        response=http_ret.read()
                        try:
                                json_resp=json.loads(response)
                                retcode=int(json_resp["code"])
                                if retcode!=0:
                                        print "send error,retcode:%d,msg:%s,data:%s" % (retcode,json_resp['message'],data)
                                else:
                                        print "send succ,data:%s" % response
                        except ValueError,e:
                                print 'value error:%s' % response
                except urllib2.URLError,e:
                        print "send error"+str(e)+data
def main():
        secretId="AKDuXhrYW5ilcFO11bakwWTF7ogwCl8ugEY"
        secretKey="tsPHxrAB8fhffaGNmHZDjNSsBm3Ewdm"
        region='sh'
        data={
                "SecretId":secretId,
                "Namespace":"pc",
                "Region":region,
                "Data":[
                        {"dimensions":{"diskname":"sda","ip":"172.31.58.160"},
                         "metricName":"diskusage",
                         "value":0.3
                        }
                        ]
                }
        sender=NwsSender()
        sender.init()
        while True:
                ts=int(time.time())
                nonce=random.randint(10000,100000)
                text="POSTreceiver.monitor.tencentyun.com/v2/index.php?Action=PutMonitorData&Nonce=%d&Region=%s&SecretId=%s&Timestam
p=%d" % (nonce,region,secretId,ts)
                data['Timestamp']=ts
                data['Nonce']=nonce
                data['Signature']=hmac.new(secretKey,text,hashlib.sha1).digest().encode("base64").rstrip('\n')
                sender.send_data(data)
                time.sleep(3)
if __name__=='__main__':
        main()
```
				
				
GET method (Finally, parameters need to be encoded using UrlEncode)
 ``` 
http://receiver.monitor.tencentyun.com:8080/v2/index.php?Action=PutMonitorData&SecretId=xxxxxxx&Region=sh&Timestamp=1402992826&Nonce=345122&Signature=mysignature
&Namespace=name1
&Data=[{"dimensions":{"diskname":"sda","ip":"172.31.58.160"},"metricName":"diskusage","value":0.3}]
 ``` 
 
 ``` 
#! /usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
import json
import random
import hmac
import hashlib

class NwsSender:
        def init(self):
                self.url='http://receiver.monitor.tencentyun.com:8080/v2/index.php'
                self.timeout=10
        def send_data(self,data):
                try:
                        req=urllib2.Request(url=self.url+ "?" + data)
                        timeout=self.timeout
                        http_ret=urllib2.urlopen(req, timeout = timeout)
                        response=http_ret.read()
                        try:
                                json_resp=json.loads(response)
                                retcode=int(json_resp["code"])
                                if retcode!=0:
                                        print "send error,retcode:%d,msg:%s,data:%s" % (retcode,json_resp['message'],data)
                                else:
                                        print "send succ,data:%s" % response
                        except ValueError,e:
                                print 'value error:%s' % response
                except urllib2.URLError,e:
                        print "send error"+str(e)+data


def main():
        secretId="AKIDDuYW5ilcFO1bakwWTF7og1wCl8ugEY"
        secretKey="tsfzPHxrffaGNmHZDjNSsBm23Ewdm"
        region='sh'
        data={
                "SecretId":secretId,
                "Namespace":"name1",
                "Region":region,
                }
        Data=[
                {"dimensions":{"diskname":"sda","ip":"172.31.58.160"},
                 "metricName":"diskusage",
                 "value":0.3
                }
                ]

        data["Data"]=json.dumps(Data)
        sender=NwsSender()
        sender.init()
        while True:
                ts=int(time.time())
                nonce=random.randint(10000,100000)
                text="GETreceiver.monitor.tencentyun.com/v2/index.php?Action=PutMonitorData&Nonce=%d&Region=%s&SecretId=%s&Timestamp
=%d" % (nonce,region,secretId,ts)
                data['Timestamp']=ts
                data['Nonce']=nonce
                data['Signature']=hmac.new(secretKey,text,hashlib.sha1).digest().encode("base64").rstrip('\n')
                xx = urllib.urlencode(data)  
                sender.send_data(xx)
                time.sleep(3)
```

If data is reported successfully, the output is:
```
{
"code":0,
"message":"OK"
}
```


## 7. Error Codes
| Error Code | Description |
|---------|---------|
|0	   | CVM has successfully received the data |
|1000	| HTTP method is not supported. You cannot send request using POST or GET method |
|1001|	Failed CGI request. CGI of this request is not supported |
|1002	| Service is not ready. Try again later |
|1003	| CVM internal logic failed |
|1004	| Request content does not exist |
|1005	| Request content is not in JSON format |
|1006	| Too many SecretId requests received within the time period. CVM protection mechanism sets a limit on frequency |
|1007	| Exception in frequency limitation feature of CVM |
|1008	| Client is blocked by CVM |
|1009	| Missing parameter |
|1010	| Incorrect parameter type |
|1011	| Invalid client ID (authentication failed) |
|1012	| The API called does not conform to the API specifications |
|1013	| Invalid parameter |
|1014	| Data is discarded because routing information is missing |
|1015	| Length of data exceeds the upper limit |
|1016	| Invalid Namespace |
|1017	| Dimension verification failed |
|1018	| The number of metrics sent within the time period exceeds the upper limit |
|1019	| Valid metric data is not reported |
|1020	| Length of dimension or metric name exceeds the limit |
|1021	| Invalid time stamp |

