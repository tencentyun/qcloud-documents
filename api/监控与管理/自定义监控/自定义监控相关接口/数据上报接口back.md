## 1. 接口描述
域名:receiver.monitor.tencentyun.com
接口名:PutMonitorData
上报数据
备注：目前只支持腾讯云服务器内部访问该域名，香港地区暂时不支持自定义监控的功能。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
|Action|是|String| 操作接口名|系统规定参数，此处取值：PutMonitorData|
| SecretId | 是 | String |用户秘钥|用户自定义|
| Region | 是 | String | 数据上报地区|用户自定义|
| Timestamp | 是 | Int | linux时间戳|用户自定义|
| Signature | 是 | String	| 用户生成的签名,生成方法见6数据上报的步骤|用户自定义|
| Namespace | 是 | String	| 命名空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
|Nonce|是|Int|随机正整数|用户自定义|
|Data|是|Array|上报的数据需要封装成json格式|用户自定义|



## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|

## 4. 示例
输入
<pre>
http://monitor.api.qcloud.com/v2/index.php?Action=PutMonitorData
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&Namespace=web_site
&Data=[{“dimensions”:{“d1”:”v1”,”d2”:”v2”,”d3”:”v3”,”d4”:”v4”,”d5”:”v5”},”metricName”:”metric1”,”value”:123},…]
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
"code":0,
"message":"OK"
}
```
## 5. 返回码
0	       服务器接收数据OK
1000	HTTP的方法不支持，即非post或get的方法请求
1001	错误的CGI请求，该请求的CGI不支持
1002	服务未就绪，稍后重试
1003	服务器内部逻辑失败
1004	请求内容不存在
1005	请求内容不是json格式
1006	时段内该SecretId请求过多，服务器保护机制限频
1007	服务器限频功能异常
1008	客户端被服务器屏蔽
1009	参数缺失
1010	参数类型错误
1011	客户端身份非法（鉴权失败）
1012	调用接口不符合API规范
1013	参数无效
1014	路由信息缺失导致数据丢弃
1015	数据长度超过上限
1016	Namespace非法
1017	dimension验证失败
1018	时段内发送的指标数量超过上限
1019	未上报有效指标数据
1020	dimension或metric名字超长
1021	时间戳非法

## 6.数据上报的步骤
1) 对下面的参数按key做字典升序排序
    {
        'Action' : 'PutMonitorData',
        'Nonce' : 345122,
        'Region' : 'gz',
        'SecretId' : 'xxxxxxx',
        'Timestamp' : 1408704141
    }
2) 拼接请求字符串：把上一步排序好的请求参数, 格式化成 k=v，然后用"&"拼接在一起 Action=PutMonitorData&Nonce=345122&Region=gz&SecretId= xxxxxxx&Timestamp=1408704141
3) 拼接签名原文字符串
拼接Signature签名原文时需要如下参数:
请求方法: 支持 POST 和 GET 方式, 这里架设为 GET 请求, 注意 GET 为全大写
请求主机: receiver.monitor.tencentyun.com
请求路径: /v2/index.php
请求字符串: 即前 2 步生成的请求字符串
签名原文的拼接规则为:
请求方法 + 请求主机 +请求路径 + ? + 请求字符串
GETreceiver.monitor.tencentyun.com/v2/index.php?Action=PutMonitorData&Nonce= 345122&Region=gz&SecretId= xxxxxxx&Timestamp=1408704141

4) 生成签名：使用 HMAC-SHA1 算法对上面步骤中获得的“签名原文字符串”进行签名，将生成的签名串使用Base64进行编码，获得最终的签名串
5) 请求参数中添加 Signature 参数, 参数值为上一步生成的签名串, 如果是使用GET方法，则对所有请求参数的参数值做URL编码
6) 通过云安全鉴权接口验证签名，验证成功时获得用户的appId；验证失败时，直接丢弃数据，不作appId维度的数据统计 

## 7.数据上报接口示例（Python）

POST方式
    {
        “Action”: “PutMonitorData”,
        “SecretId”: “xxxxxxx”,
        “Region”: “gz”,
        “Timestamp”: 1402992826,
        “Nonce”: 345122,
        “Signature”: “mysignature”,
        “Namespace”: “web_site”,
        “Data”:[{“dimensions”:{“d1”:”v1”,”d2”:”v2”,”d3”:”v3”,”d4”:”v4”,”d5”:”v5”},”metricName”:”metric1”,”value”:123},…]
    }

    class NWSSender:
        def init(self):
            self.url = 'http://127.0.0.1:8000/report.cgi'
            self.timeout = 0.5 
        def send_data(self, json_data):
            try:
                req = urllib2.Request(self.url)
                req.add_header('Content-Type','application/json')
                timeout = self.timeout
                data = json.dumps(json_data)
                http_ret = urllib2.urlopen(req, data, timeout)
                response = http_ret.read()
                try:
                    json_resp = json.loads(response)
                    retcode = int(json_resp["code"])
                    if retcode != 0:
                        print "nws send error, retcode : %d, msg : %s, data : %s" % (retcode, json_resp["message"], data)
                    else:
                        print "nws send succ, data : %s" % str(data)
                except ValueError,e:
                    print "nws send error, got a invalid json response : %s" % response
            except urllib2.URLError,e:
                print "send data error , error :%s, data : %s" % (str(e), data)
    def main():
        interval = 10
        data = { 
            "SecretId": "xxxxxxx",
            "Namespace":"test",
            "Region": "gz",
            "Data":[{
                    "dimensions": {"d2":"v2", "d3":"v3", "d1":"v1" },
                    "metricName": "m1",
                    "value": 200 
                },  
                {   
                    "dimensions": {"d2":"v2", "d3":"v3", "d1":"v1" },
                    "metricName": "m2",
                    "value": 100  
                }]  
        }   
        sender = NWSSender()
        sender.init()
        while True:
            ts = int(time.time())
            nonce = random.randint(10000, 100000);
            plaintext = "POSTreceiver.monitor.tencentyun.com/v2/index.php?Action=PutMonitorData&Nonce=%d&Region=gz&SecretId=xxxxxxx&Timestamp=%d" % (nonce, ts) 
            data['Timestamp'] = ts
            data['Nonce'] =123
            data['Signature'] = hmac.new('Mw6IJbcSxLaXX4XoyObu89Jera7e1p83', plaintext, hashlib.sha1).digest().encode("base64").rstrip('\n')
            sender.send_data(data)
            time.sleep(interval)
    if __name__ == '__main__':
        main()
				
				
GET方式（最后需对参数进行UrlEncode）

    http://receiver.monitor.tencentyun.com/v2/index.php?Action=PutMonitorData&SecretId=xxxxxxx&Region=gz&Timestamp=1402992826&Nonce=345122&Signature=mysignature
    &Namespace=web_site
    &Data=[{“dimensions”:{“d1”:”v1”,”d2”:”v2”,”d3”:”v3”,”d4”:”v4”,”d5”:”v5”},”metricName”:”metric1”,”value”:123},…]

    class NWSSender:
        def init(self):
            self.url = 'http://127.0.0.1:8000/report.cgi'
            self.timeout = 0.5 
        def send_data(self, data):
            try:
                req = urllib2.Request(self.url + "?" + data)
                timeout = self.timeout
                http_ret = urllib2.urlopen(req, timeout=timeout)
                response = http_ret.read()
                try:
                    json_resp = json.loads(response)
                    retcode = int(json_resp["code"])
                    if retcode != 0:
                        print "nws send error, retcode : %d, msg : %s, data : %s" % (retcode, json_resp["message"], data)
                    else:
                        print "nws send succ, data : %s" % str(data)
                except ValueError,e:
                    print "nws send error, got a invalid json response : %s" % response
            except urllib2.URLError,e:
                print "send data error , error :%s, data : %s" % (str(e), data)
    def main():
        interval = 10
        data = { 
            "SecretId": "xxxxxx",
            "Namespace":"test",
            "Region": "gz"
        }   
        Data = [{
                    "dimensions": {"d2":"v2", "d3":"v3", "d1":"v1" },
                    "metricName": "m1",
                    "value": 200 
                },  
                {   
                    "dimensions": {"d2":"v2", "d3":"v3", "d1":"v1" },
                    "metricName": "m2",
                    "value": 100  
                }]  
        data["Data"] = json.dumps(Data)
        sender = NWSSender()
        sender.init()
        while True:
            ts = int(time.time())
            nonce = random.randint(10000, 100000);
            plaintext = "GETreceiver.monitor.tencentyun.com/report.cgi?Action=PutMonitorData&Nonce=%d&Region=gz&SecretId=xxxxxx&Timestamp=%d" % (nonce, ts) 
            data['Timestamp'] = ts
            data['Nonce'] = nonce
            data['Signature'] = hmac.new('Mw6IJbcSxLaXX4XoyObu89Jera7e1p83', plaintext, hashlib.sha1).digest().encode("base64").rstrip('\n')
            sender.send_data(urllib.urlencode(data))
            time.sleep(interval)
    if __name__ == '__main__':
        main()
