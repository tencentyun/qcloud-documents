## 概述

JSON 格式日志会自动提取首层的 key 作为对应字段名，首层的 value 作为对应的字段值，以该方式将整条日志进行结构化处理，每条完整的日志以换行符`\n`为结束标识符。

#### 示例

假设您的一条 JSON 日志原始数据为：

```shell
{"remote_ip":"10.135.46.111","time_local":"22/Jan/2019:19:19:34 +0800","body_sent":23,"responsetime":0.232,"upstreamtime":"0.232","upstreamhost":"unix:/tmp/php-cgi.sock","http_host":"127.0.0.1","method":"POST","url":"/event/dispatch","request":"POST /event/dispatch HTTP/1.1","xff":"-","referer":"http://127.0.0.1/my/course/4","agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0","response_code":"200"}
```

经过日志服务结构化处理后，该条日志将变为如下：

```shell
agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0
body_sent: 23
http_host: 127.0.0.1
method: POST
referer: http://127.0.0.1/my/course/4
remote_ip: 10.135.46.111
request: POST /event/dispatch HTTP/1.1
response_code: 200
responsetime: 0.232
time_local: 22/Jan/2019:19:19:34 +0800
upstreamhost: unix:/tmp/php-cgi.sock
upstreamtime: 0.232
url: /event/dispatch
xff: -
```

## 采集配置

### 1. 登录控制台

登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中，单击【日志集管理】。

### 2. 新建 LogListener 采集

选择目标日志集，单击【新建日志主题】，输入日志主题名称：test-json ，单击 【确定】。 
![](https://main.qcloudimg.com/raw/26ea3416512e4cae85350b289f916ce6.png)

### 3. 配置 LogListener 采集

单击 LogListener 采集的日志主题，在采集配置界面中单击右上角【编辑】按钮，进入到编辑模式，开启【采集状态】和【使用 LogListener】。
![](https://main.qcloudimg.com/raw/0d02833b9ee198a584dadd68f9c6de9c.png)

### 4. 配置日志文件采集路径

日志采集路径格式为 **[目录前缀表达式]**/\*\*/**[文件名表达式]** ，LogListener 会按照 **[目录前缀表达式]** 匹配所有符合规则的公共前缀路径，并监听这些目录（包含子层目录）下所有符合 **[文件名表达式]** 规则的日志文件，参数详细说明如下：

| 字段     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 目录前缀 | 日志文件前缀目录结构，仅支持通配符 \* 和 ? ，\* 表示匹配多个任意字符，? 表示匹配单个任意字符 |
| /**/     | 表示当前目录以及所有子目录                                   |
| 文件名   | 日志文件名，仅支持通配符 \* 和 ? ，\* 表示匹配多个任意字符，? 表示匹配单个任意字符 |

>常用配置模式参考：
>[公共目录前缀]/\*\*/[公共文件名前缀]\*
>[公共目录前缀]/\*\*/*[公共文件名后缀]
>[公共目录前缀]/\*\*/[公共文件名前缀]\*[公共文件名后缀]
>[公共目录前缀]/\*\*/\*[公共字符串]\*

填写示例：

| 序号 | 目录前缀表达式 | 文件名表达式 | 说明                                                         |
| ---- | -------------- | ------------ | ------------------------------------------------------------ |
| 1.   | /var/log/nginx | access.log   | 此例中，日志路径配置为`/var/log/nginx/**/access.log`，LogListener 将会监听`/var/log/nginx`前缀路径下所有子目录中以`access.log`命名的日志文件 |
| 2.   | /var/log/nginx | \*.log       | 此例中，日志路径配置为`/var/log/nginx/**/*.log`，LogListener 将会监听`/var/log/nginx`前缀路径下所有子目录中以`.log`结尾的日志文件 |
| 3.   | /var/log/nginx | error\*      | 此例中，日志路径配置为`/var/log/nginx/**/error*`，LogListener 将会监听`/var/log/nginx`前缀路径下所有子目录中以`error`开头命名的日志文件 |

>!
>1. 多层目录和通配符配置方式依赖2.2.2及以上版本的 loglistener，为兼容低版本 loglistener 路径配置修改方式，用户可切换旧配置进行历史修改，旧采集路径方式不支持多目录采集。
>2. 一个日志文件只能被一个日志主题采集。
>3. LogListener 不支持监听软连接方式的日志文件和 NFS、CIFS 等共享文件目录上的日志文件。

### 5. 关联机器组

从机器组列表中选择目标机器组，将其与当前日志主题进行关联，值得注意的是，关联的机器组与日志主题所在的地域需保持一致。操作详情请参阅 [如何创建机器组](https://cloud.tencent.com/document/product/614/17412#.E5.88.9B.E5.BB.BA.E6.9C.BA.E5.99.A8.E7.BB.84) 文档。
![](https://main.qcloudimg.com/raw/3bca76c93bfa640563bef85f6aa6dbf9.png)

### 6. JSON 模式选择

键值提取模式选择 **JSON**。
![](https://main.qcloudimg.com/raw/c4e8d572fc070dd6085ab82bb0d1545c.png)

### 7. 采集时间配置

> - 日志时间单位为：秒。
> - 日志的时间属性有两种方式来定义：采集时间和原始时间戳。
> - 采集时间：日志的时间属性由日志服务 CLS 采集该条日志的时间决定。
> - 原始时间戳：日志的时间属性由原始日志中时间戳决定。

#### 7.1 采集时间作为日志的时间属性

保持采集时间状态为开启状态即可，如图： 
![](https://main.qcloudimg.com/raw/316ea52b35187d1dcce8af6f020f819b.png)

#### 7.2 日志的原始时间戳作为日志时间属性

关闭采集时间状态，在时间键和时间格式解析处，填写原始时间戳的时间键以及对应的时间解析格式。时间解析格式详情参见 [配置时间格式](https://cloud.tencent.com/document/product/614/38614)。
![img](https://main.qcloudimg.com/raw/6eb891575ad26c82fa4b466e0bb53b9c.png)

这里举例说明时间格式解析规则填写：
例1：日志样例原始时间戳：`10/Dec/2017:08:00:00`，解析格式为：`%d/%b/%Y:%H:%M:%S`。
例2：日志样例原始时间戳：`2017-12-10 08:00:00`，解析格式为：`%Y-%m-%d %H:%M:%S`。
例3：日志样例原始时间戳：`12/10/2017, 08:00:00`，解析格式为：`%m/%d/%Y, %H:%M:%S`。

>!日志时间支持以秒为单位，若时间格式填写错误日志时间将以采集时间为准。

### 8. 过滤器条件

过滤器旨在您根据业务需要添加日志采集过滤规则，帮助您筛选出有价值的日志数据。过滤规则为 Perl 正则表达式，所创建的过滤规则为命中规则，即匹配上正则表达式的日志才会被采集上报。

对于 JSON 格式日志，可以根据所解析成的键值对配置过滤规则。例如，您希望原始 JSON 格式日志内容中 response_code 为 400 或 500 的所有日志数据被采集，那么 key 处配置 response_code ，过滤规则处配置 400|500 。

>! 多条过滤规则之间关系是"与"逻辑；若同一 key 名配置多条过滤规则，规则会被覆盖。

### 9. 检索结果

登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中，单击【日志检索】，输入日志集与日志主题，单击【搜索】，系统将开始检索日志。
![](https://main.qcloudimg.com/raw/a81934f054d00abcf605db24ddf5ad04.png)

>!检索必须开启索引配置，否则无法进行检索。
