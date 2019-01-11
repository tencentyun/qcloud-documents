## 概述

JSON 格式日志会自动提取首层的 key 作为对应字段名，首层的 value 作为对应的字段值，以该方式将整条日志进行结构化处理，每条完整的日志以换行符`\n`为结束标识符。

### 示例
假设您的一条 json 日志原始数据为：
```
{"remote_ip":"10.135.46.123","time_local":"21/Dec/2018:17:06:56 +0800","body_sent":142,"responsetime":0.961,"upstreamtime":"0.961","upstreamhost":"unix:/tmp/php-cgi.sock","http_host":"127.0.0.1","method":"GET","url":"/admin/cloud/ad","request":"GET /admin/cloud/ad HTTP/1.1","xff":"-","referer":"http://127.0.0.1/admin/","agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0","response_code":"200"}
```

经过日志服务结构化处理后，该条日志将变为如下：

```
agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0
body_sent: 334
http_host: 127.0.0.1
method: POST
referer: http://127.0.0.1/admin/
remote_ip: 10.135.46.111
request: POST /admin/operation/analysis HTTP/1.1
response_code: 200
responsetime: 0.219
time_local: 21/Dec/2018:17:06:56 +0800
upstreamhost: unix:/tmp/php-cgi.sock
upstreamtime: 0.219
url: /admin/operation/analysis
xff: - 
```
## 采集配置

### 1. 登录控制台

登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，左侧选择【日志集管理】。

### 2. 新建 LogListener 采集

选择目标日志集，单击【新建日志主题】，输入日志主题名称：test-json ，单击 【确定】即可。
![](https://main.qcloudimg.com/raw/33a572bbd59fb6c35f2937a1e124e38d.png)

### 3. 配置 LogListener 采集

单击 LogListener 采集的日志主题，在采集配置界面中单击右上角【编辑】按钮，进入到编辑模式，然后开启**采集状态**和**使用 LogListener**。 
![](https://main.qcloudimg.com/raw/b8d6b810b8958dc1504e1db3d05490f4.png)

### 4. 配置日志文件采集路径

采集路径处需要填写需要采集的完整路径，而非目录格式（即需要以 / 开头，非 / 结尾），文件名支持正则，目前暂不支持通配符。

>!采集路径中仅允许日志文件名称使用正则，目录不支持正则。

#### 配置方式
|方式|路径|
| ------------------------ | ------------------ |
| 使用绝对路径匹配日志文件 | /usr/local/nginx/logs/example.com.access.log |
| 使用正则匹配日志文件 | /usr/local/nginx/logs/.*.access.log          |

### 5. 关联机器组

从机器组列表中选择目标机器组，将其与当前日志主题进行关联，值得注意的是，关联的机器组与日志主题所在的地域需保持一致。操作详情请参阅 [如何创建机器组](https://cloud.tencent.com/document/product/614/17412#.E5.88.9B.E5.BB.BA.E6.9C.BA.E5.99.A8.E7.BB.84) 文档。
![](https://main.qcloudimg.com/raw/769ab308eaf3f59d9de97fcb358a9a83.png)

### 6. JSON 模式选择

键值提取模式选择 **JSON**。
![](https://main.qcloudimg.com/raw/c043a155c49a655b443fce56a7a910c8.png)

### 7. 采集时间配置

>?
>- 日志时间单位为：秒。
>- 日志的时间属性有两种方式来定义：采集时间和原始时间戳。
>- 采集时间：日志的时间属性由日志服务 CLS 采集该条日志的时间决定。
>- 原始时间戳：日志的时间属性由原始日志中时间戳决定。

#### 7.1 采集时间作为日志的时间属性

保持采集时间状态为开启状态即可，如图：
![](https://main.qcloudimg.com/raw/837a8946234f580f977f623dd6df5e7a.png)

#### 7.2 日志的原始时间戳作为日志时间属性

关闭采集时间状态，填写原始时间戳的时间键以及对应的时间解析格式，转换格式支持 strftime 的所有函数。
![](https://main.qcloudimg.com/raw/c548153ae42a2329b9be91b4b1c10178.png)

这里举例说明时间格式解析规则填写：  
例1：日志样例原始时间戳：`10/Dec/2017:08:00:00`，解析格式为：`%d/%b/%Y:%H:%M:%S`。
例2：日志样例原始时间戳：`2017-12-10 08:00:00`，解析格式为：`%Y-%m-%d %H:%M:%S`。  
例3：日志样例原始时间戳：`12/10/2017, 08:00:00`，解析格式为：`%m/%d/%Y, %H:%M:%S`。  

>!日志时间支持以秒为单位，若时间格式填写错误日志时间将以采集时间为准。

### 8. 过滤器条件

过滤器旨在您根据业务需要添加日志采集过滤规则，帮助您方便筛选出有价值的日志数据。对于JSON格式日志，可以根据所解析成的键值对配置过滤规则，过滤规则为正则表达式。所创建的过滤规则为命中规则，即匹配上正则表达式的日志才会被采集上报。

例如，您希望指定 status = 400或500的日志数据被采集。key 处配置 status，过滤规则处配置（400|500）。

### 9. 检索结果

登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，左侧导航栏单击【日志检索】，然后在日志检索界面选择日志集与日志主题，单击【搜索】，即可检索日志。
![](https://main.qcloudimg.com/raw/f9d5c022abf274fb9bb6b71b386c9d3c.png)

>!检索必须开启索引配置，否则无法进行检索。
