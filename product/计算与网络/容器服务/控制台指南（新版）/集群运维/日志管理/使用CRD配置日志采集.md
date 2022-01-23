## 操作场景
用户不仅可以 [使用控制台配置日志采集](https://cloud.tencent.com/document/product/457/36771)，还可通过自定义资源定义（CustomResourceDefinitions，CRD）的方式配置日志采集。CRD 支持采集容器标准输出、容器文件和主机文件，支持多种日志采集格式。支持投递到 CLS 和 CKafka 等不同消费端。

## 前提条件
已在容器服务控制台的 **[功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=8)** 中开启日志采集，详情参见 [开启日志采集](https://cloud.tencent.com/document/product/457/36771)。



## 创建 CRD 投递日志到 CLS 
您只需要定义 LogConfig CRD 即可创建采集配置，log-agent 根据 LogConfig CRD 的变化修改相应的日志服务 CLS 日志主题，并设置绑定的机器组。CRD 的格式如下:
``` yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig                              ## 默认值
metadata:
  name: test                                ## CRD资源名，在集群内唯一
spec:
  clsDetail:
    # 注意：topic指定后不允许修改
    # 自动创建日志主题，需要同时指定日志集和主题的name
    logsetName: test                        ## CLS日志集的name，若无该name的日志集，会自动创建，若有，会在该日志集下创建日志主题
    topicName: test                         ## CLS日志主题的name，若无该name的日志主题，会自动创建
     
    # 选择已有日志主题
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx       ## CLS日志主题的ID，日志主题需要在CLS中提前创建，且没有被其它采集配置占用
    logType: minimalist_log                 ## 日志采集格式，json_log代表 json 格式，delimiter_log代表分隔符格式，minimalist_log代表单行全文格式，multiline_log代表多行全文格式，fullregex_log代表完全正则格式
    extractRule:                            ## 提取、过滤规则
      ...
  inputDetail:
    type: container_stdout                  ## 采集日志的类型，包括container_stdout（容器标准输出）、container_file（容器文件）、host_file（主机文件）
    
    containerStdout:                        ## 容器标准输出
      namespace: default                    ## 采集容器的kubernetes命名空间，如果不指定，代表所有命名空间
      allContainers: false                  ## 是否采集指定命名空间中的所有容器的标准输出
      container: xxx                        ## 采集日志的容器名，为空时，代表采集所有符合容器的日志名
      includeLabels:                        ## 采集包含指定label的Pod
        k8s-app: xxx                        ## 只采pod标签中配置"k8s-app=xxx"的pod产生的日志，与workloads、allContainers=true不能同时指定
      workloads:                            ## 要采集的容器的Pod所属的kubernetes workload
      - namespace: prod                     ## workload的命名空间
        name: sample-app                    ## workload的名字
        kind: deployment                    ## workload类型，支持deployment、daemonset、statefulset、job、cronjob
        container: xxx                      ## 要采集的容器名，如果不指定，代表workload Pod中的所有容器
	
    containerFile:                          ## 容器内文件
      namespace: default                    ## 采集容器的kubernetes命名空间，必须指定一个命名空间
      container: xxx                        ## 采集日志的容器名，为 * 时，代表采集所有符合容器的日志名
     includeLabels:                         ## 采集包含指定label的Pod
        k8s-app: xxx                        ## 只采pod标签中配置"k8s-app=xxx"的pod产生的日志，与workload不能同时指定
      workload:                             ## 要采集的容器的Pod所属的kubernetes workload
        name: sample-app                    ## workload的名字                  
        kind: deployment                    ## workload类型，支持deployment、daemonset、statefulset、job、cronjob
      logPath: /opt/logs                    ## 日志文件夹，不支持通配符
      filePattern: app_*.log                ## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
     
    hostFile:                               ## 主机文件
      logPath: /opt/logs                    ## 日志文件夹，支持通配符
      filePattern: app_*.log                ## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
      customLablels:
        k1: v1
```
<dx-alert infotype="notice" title="">
如果选择采集类型为“容器文件路径”时，对应的“容器文件路径”<b>不能为软链接</b>，否则会导致软链接的实际路径在采集器的容器内不存在，采集日志失败。
</dx-alert>


### 配置 CLS 日志解析格式
<dx-tabs>
::: 单行全文格式
单行全文日志是指一行日志内容为一条完整的日志。日志服务在采集的时候，将使用换行符 `\n` 来作为一条日志日志的结束符。为了统一结构化管理，每条日志都会存在一个默认的键值 `__CONTENT__`，但日志数据本身不再进行日志结构化处理，也不会提取日志字段，日志属性的时间项由日志采集的时间决定。详情请参见 [单行全文格式](https://cloud.tencent.com/document/product/614/17421)。

假设一条日志原始数据为：
```
Tue Jan 22 12:08:15 CST 2019 Installed: libjpeg-turbo-static-1.2.90-6.el7.x86_64
```
LogConfig 配置参考示例如下：
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  clsDetail:
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    # 单行日志
    logType: minimalist_log
```
采集到日志服务的数据为：
```
__CONTENT__:Tue Jan 22 12:08:15 CST 2019 Installed: libjpeg-turbo-static-1.2.90-6.el7.x86_64
```
:::
::: 多行全文格式
多行全文日志是指一条完整的日志数据可能跨占多行（例如 Java stacktrace）。该情况下无法使用换行符 `\n` 作为日志的结束标识符，为了使日志系统明确区分每条日志，采用首行正则的方式进行匹配，当某行日志匹配预先设置的正则表达式，即为一条日志的开头，而下一行首出现则作为该条日志的结束标识符。多行全文也会设置一个默认的键值 `__CONTENT__`，但日志数据本身不再进行日志结构化处理，也不会提取日志字段，日志属性的时间项由日志采集的时间决定。详情请参见 [多行全文格式](https://cloud.tencent.com/document/product/614/17422)。

假设一条多行日志原始数据为：
<dx-codeblock>
:::  log
2019-12-15 17:13:06,043 [main] ERROR com.test.logging.FooFactory:
java.lang.NullPointerException
     at com.test.logging.FooFactory.createFoo(FooFactory.java:15)
     at com.test.logging.FooFactoryTest.test(FooFactoryTest.java:11)
:::
</dx-codeblock>
LogConfig 配置的参考如下：
<dx-codeblock>
:::  yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec: 
  clsDetail: 
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    #多行日志
    logType: multiline_log
    extractRule: 
      #只有以日期时间开头的行才被认为是新一条日志的开头，否则就添加换行符\n并追加到当前日志的尾部
      beginningRegex: \d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\s.+
:::
</dx-codeblock>
采集到日志服务的数据为：
<dx-codeblock>
:::  log
\_\_CONTENT__:2019-12-15 17:13:06,043 [main] ERROR com.test.logging.FooFactory:\njava.lang.NullPointerException\n    at com.test.logging.FooFactory.createFoo(FooFactory.java:15)\n    at com.test.logging.FooFactoryTest.test(FooFactoryTest.java:11)
:::
</dx-codeblock>
:::
::: 单行-完全正则格式
完全正则格式通常用来处理结构化的日志，指将一条完整日志按正则方式提取多个 key-value 的日志解析模式。详情请参见  [完全正则格式](https://cloud.tencent.com/document/product/614/32817)。
假设一条日志原始数据为：
<dx-codeblock>
:::  log
10.135.46.111 - - [22/Jan/2019:19:19:30 +0800] "GET /my/course/1 HTTP/1.1" 127.0.0.1 200 782 9703 "http://127.0.0.1/course/explore?filter%5Btype%5D=all&filter%5Bprice%5D=all&filter%5BcurrentLevelId%5D=all&orderBy=studentNum" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"  0.354 0.354
:::
</dx-codeblock>
LogConfig 配置的参考如下：
<dx-codeblock>
:::  yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec: 
  clsDetail: 
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    # 完全正则格式
    logType: fullregex_log
    extractRule: 
      # 正则表达式，会根据()捕获组提取对应的value
      logRegex: (\S+)[^\[]+(\[[^:]+:\d+:\d+:\d+\s\S+)\s"(\w+)\s(\S+)\s([^"]+)"\s(\S+)\s(\d+)\s(\d+)\s(\d+)\s"([^"]+)"\s"([^"]+)"\s+(\S+)\s(\S+).*
      beginningRegex: (\S+)[^\[]+(\[[^:]+:\d+:\d+:\d+\s\S+)\s"(\w+)\s(\S+)\s([^"]+)"\s(\S+)\s(\d+)\s(\d+)\s(\d+)\s"([^"]+)"\s"([^"]+)"\s+(\S+)\s(\S+).*
      # 提取的key列表，与提取的value的一一对应
      keys:   ['remote_addr','time_local','request_method','request_url','http_protocol','http_host','status','request_length','body_bytes_sent','http_referer','http_user_agent','request_time','upstream_response_time']
:::
</dx-codeblock>
采集到日志服务的数据为：
<dx-codeblock>
:::  log
body_bytes_sent: 9703
http_host: 127.0.0.1 
http_protocol: HTTP/1.1
http_referer: http://127.0.0.1/course/explore?filter%5Btype%5D=all&filter%5Bprice%5D=all&filter%5BcurrentLevelId%5D=all&orderBy=studentNum
http_user_agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0
remote_addr: 10.135.46.111 
request_length: 782
request_method: GET
request_time: 0.354
request_url: /my/course/1
status: 200
time_local: [22/Jan/2019:19:19:30 +0800]
upstream_response_time: 0.354
:::
</dx-codeblock>
:::
::: 多行-完全正则格式
多行-完全正则模式适用于日志文本中一条完整的日志数据跨占多行（例如 Java 程序日志），可按正则表达式提取为多个 key-value 键值的日志解析模式。若不需要提取 key-value，请参阅多行全文格式进行配置。详情请参见  [多行-完全正则格式](https://cloud.tencent.com/document/product/614/52366)。

假设一条日志原始数据为：
<dx-codeblock>
:::  log
[2018-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened
   at TestPrintStackTrace.f(TestPrintStackTrace.java:3)
   at TestPrintStackTrace.g(TestPrintStackTrace.java:7)
   at TestPrintStackTrace.main(TestPrintStackTrace.java:16)
:::
</dx-codeblock>
LogConfig 配置的参考如下：
<dx-codeblock>
:::  yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec: 
  clsDetail: 
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
		#多行-完全正则格式
		logType: multiline_fullregex_log
		extractRule: 
      #行首完全正则表达式，只有以日期时间开头的行才被认为是新一条日志的开头，否则就添加换行符\n并追加到当前日志的尾部
			beginningRegex: \[\d+-\d+-\w+:\d+:\d+,\d+\]\s\[\w+\]\s.*
      #正则表达式，会根据()捕获组提取对应的value
      logRegex: \[(\d+-\d+-\w+:\d+:\d+,\d+)\]\s\[(\w+)\]\s(.*)
			# 提取的 key 列表，与提取的 value 的一一对应
			keys: 
      - time 
      - level 
      - msg 
:::
</dx-codeblock>
根据提取的 key，采集到日志服务的数据为：
<dx-codeblock>
:::  log
time： 2018-10-01T10:30:01,000`
level： INFO`
msg：java.lang.Exception: exception happened
   at TestPrintStackTrace.f(TestPrintStackTrace.java:3)
   at TestPrintStackTrace.g(TestPrintStackTrace.java:7)
   at TestPrintStackTrace.main(TestPrintStackTrace.java:16)
:::
</dx-codeblock>
:::
::: JSON\s格式
JSON 格式日志会自动提取首层的 key 作为对应字段名。首层的 value 作为对应的字段值，以该方式将整条日志进行结构化处理，每条完整的日志以换行符 `\n` 为结束标识符。详情请参见  [JSON 格式](https://cloud.tencent.com/document/product/614/17419)。

假设一条 JSON 日志原始数据为：
<dx-codeblock>
:::  log
{"remote_ip":"10.135.46.111","time_local":"22/Jan/2019:19:19:34 +0800","body_sent":23,"responsetime":0.232,"upstreamtime":"0.232","upstreamhost":"unix:/tmp/php-cgi.sock","http_host":"127.0.0.1","method":"POST","url":"/event/dispatch","request":"POST /event/dispatch HTTP/1.1","xff":"-","referer":"http://127.0.0.1/my/course/4","agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0","response_code":"200"}
:::
</dx-codeblock>
LogConfig 配置的参考如下：
<dx-codeblock>
:::  log
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  clsDetail:
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    # JSON格式日志
    logType: json_log
:::
</dx-codeblock>
采集到日志服务的数据为：
<dx-codeblock>
:::  log
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
:::
</dx-codeblock>
:::
::: 分隔符格式
分隔符日志是指一条日志数据可以根据指定的分隔符将整条日志进行结构化处理，每条完整的日志以换行符 `\n` 为结束标识符。日志服务在进行分隔符格式日志处理时，您需要为每个分开的字段定义唯一的 key。详情请参见 [分隔符格式](https://cloud.tencent.com/document/product/614/17420)。

假设原始日志为：
<dx-codeblock>
:::  log
10.20.20.10 ::: [Tue Jan 22 14:49:45 CST 2019 +0800] ::: GET /online/sample HTTP/1.1 ::: 127.0.0.1 ::: 200 ::: 647 ::: 35 ::: http://127.0.0.1/
:::
</dx-codeblock>
LogConfig 配置的参考如下：
<dx-codeblock>
:::  yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec: 
  clsDetail: 
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    #分隔符日志
    logType: delimiter_log
    extractRule: 
      #分隔符
      delimiter: ':::'
      #提取的key列表，与被分割的字段一一对应
      keys: ['IP','time','request','host','status','length','bytes','referer']
:::
</dx-codeblock>
采集到日志服务的数据为：
<dx-codeblock>
:::  log
IP: 10.20.20.10 
bytes: 35
host: 127.0.0.1 
length: 647
referer: http://127.0.0.1/
request: GET /online/sample HTTP/1.1
status: 200
time: [Tue Jan 22 14:49:45 CST 2019 +0800]
:::
</dx-codeblock>
:::
</dx-tabs>





## 创建 CRD 投递日志到 CKafka
当前支持通过配置 CRD 采集 TKE 上的 Pod 日志至自建 Kafka 或者 CKafka，需要按如下配置自行定义日志源及日志消费端，CRD 配置完成后，日志采集器会按规则进行日志采集。
CRD 具体配置如下：
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig                          ## 默认值
metadata:
  name: test                                ## CRD资源名，在集群内唯一
spec:
  kafkaDetail:
    kafkaType:       ## 必填，kafka 类型，“ckafka” 表示ckafka，“” 表示自建 kafka
      type: string
    instanceId:     ## ckafka实例ID
      type: string
    brokers: xxxxxx       ## 必填，broker地址，一般是域名:端口，多个地址以“,”分隔
    topic: xxxxxx         ## 必填，topic名称        
    messageKey:           ## 选填，指定pod字段作为key上传到指定分区
      valueFrom:
        fieldRef:
          fieldPath: metadata.name   
    timestampKey:          ## 时间戳的key，默认是@timestamp
    timestampFormat:       ## 时间戳的格式，默认是double
  inputDetail:
    type: container_stdout                  ## 采集日志的类型，包括container_stdout（容器标准输出）、container_file（容器文件）

    containerStdout:                        ## 容器标准输出
      namespace: default                    ## 采集容器的kubernetes命名空间，如果不指定，代表所有命名空间
      allContainers: false                  ## 是否采集指定命名空间中的所有容器的标准输出
      container: xxx                        ## 采集日志的容器名，此处可不填
      includeLabels:                        ## 采集包含指定label的Pod
        k8s-app: xxx                        ## 只采pod标签中配置"k8s-app=xxx"的pod产生的日志，与workloads、allContainers=true不能同时指定
      workloads:                            ## 要采集的容器的Pod所属的kubernetes workload
      - namespace: prod                     ## workload的命名空间
        name: sample-app                    ## workload的名字
        kind: deployment                    ## workload类型，支持deployment、daemonset、statefulset、job、cronjob
        container: xxx                      ## 要采集的容器名，如果填空，代表workload Pod中的所有容器

    containerFile:                          ## 容器内文件
      namespace: default                    ## 采集容器的kubernetes命名空间，必须指定一个命名空间
      container: xxx                        ## 采集日志的容器名，此处可填*
      includeLabels:                        ## 采集包含指定label的Pod
        k8s-app: xxx                        ## 只采pod标签中配置"k8s-app=xxx"的pod产生的日志，与workload不能同时指定
      workload:                             ## 要采集的容器的Pod所属的kubernetes workload
        name: sample-app                    ## workload的名字                  
        kind: deployment                    ## workload类型，支持deployment、daemonset、statefulset、job、cronjob
      logPath: /opt/logs                    ## 日志文件夹，不支持通配符
      filePattern: app_*.log                ## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
     
      ...
```


## 采集日志的类型
### 容器标准输出
#### 示例1：采集 default 命名空间中的所有容器的标准输出
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  inputDetail:
    type: container_stdout
    containerStdout:
      namespace: default
      allContainers: true
 ...
```

#### 示例2：采集 production 命名空间中属于 ingress-gateway deployment 的 pod 中的容器的标准输出
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  inputDetail:
    type: container_stdout
    containerStdout:
      allContainers: false
      workloads:
      - namespace: production
        name: ingress-gateway
        kind: deployment
  ...
```

#### 示例3：采集 production 命名空间下 pod 标签中包含 “k8s-app=nginx” 的 pod 中的容器的标准输出
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  inputDetail:
    type: container_stdout
    containerStdout:
      namespace: production
      allContainers: false
      includeLabels:
        k8s-app: nginx
  ...
```

### 容器文件
#### 示例1：采集 production 命名空间下属于 ingress-gateway deployment 的 pod 中的 nginx 容器中 `/data/nginx/log/` 路径下名为 `access.log` 的文件
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  topicId: xxxxxx-xx-xx-xx-xxxxxxxx
  inputDetail:
    type: container_file
    containerFile:
      namespace: production
      workload:
        name: ingress-gateway
        type: deployment
      container: nginx
      logPath: /data/nginx/log
      filePattern: access.log
  ...
```

#### 示例2：采集 production 命名空间下 pod 标签包含 “k8s-app=ingress-gateway” 的 pod 中的 nginx 容器中 `/data/nginx/log/` 路径下名为 `access.log` 的文件
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  inputDetail:
    type: container_file
    containerFile:
      namespace: production
      includeLabels:
        k8s-app: ingress-gateway
      container: nginx
      logPath: /data/nginx/log
      filePattern: access.log
  ...
```

### 主机文件
#### 示例：采集主机 `/data/` 路径下所有 `.log` 文件
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  inputDetail:
    type: host_file
    hostFile:
      logPath: /data
      filePattern: *.log
  ...
```

### 元数据（Metadata）
容器标准输出（container_stdout）以及容器文件（container_file），除原始的日志内容外，还需携带容器场景的元数据（例如产生日志的容器 ID）一起上报至日志服务。方便用户查看日志时追溯来源或根据容器标识、特征（例如容器名及 labels）进行检索。
元数据如下表：
<table>
	<tr>
		<th>字段名</th> <th>含义</th>
	</tr>
	<tr>
		<td>cluster_id</td> <td>日志所属的集群 ID。</td>
	</tr>
	<tr>
		<td>container_name</td> <td>日志所属的容器名称。</td>
	</tr>
	<tr>
		<td>container_id</td> <td>日志所属的容器 ID。</td>
	</tr>
	<tr>
		<td>image_name</td> <td>日志所属容器的镜像名称 IP。</td>
	</tr>
	<tr>
		<td>namespace</td> <td>日志所属 Pod 的 namespace。</td>
	</tr>
	<tr>
		<td>pod_uid</td> <td>日志所属 Pod 的 UID。</td>
	</tr>
	<tr>
		<td>pod_name</td> <td>日志所属 Pod 的名字。</td>
	</tr>
	<tr>
		<td>pod_ip</td> <td>日志所属 Pod 的 IP。</td>
	</tr>
	<tr>
		<td>pod_lable_{label name}</td> <td>日志所属 Pod 的 label（例如一个 Pod 带有两个 label：app=nginx，env=prod，
则在上传的日志会附带两个 metedata：pod_label_app:nginx，pod_label_env:prod）。
</td>
	</tr>
</table>





