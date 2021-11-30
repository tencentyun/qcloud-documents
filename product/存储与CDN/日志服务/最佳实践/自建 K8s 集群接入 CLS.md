## 简介
日志服务 （Cloud Log Service， CLS）支持采集自建 K8s 集群上的日志，在进行日志采集前，需要在 K8s 自建集群上通过 CRD 定义日志采集配置（LogConfig），并部署安装 Log-Provisioner，Log-Agent，以及 LogListener。针对使用腾讯云容器服务（Tencent Kubernetes Engine ,TKE）的用户， 可参见 [TKE 开启日志采集](https://cloud.tencent.com/document/product/457/36771) 文档，通过控制台快速接入并使用日志服务。


## 前提条件

- 已创建 Kubernetes 1.10 及以上版本集群。
- 已开通日志服务， 创建日志集和日志主题，且获取日志主题 ID（topicId）。
详细配置请参见 [创建日志主题](https://cloud.tencent.com/document/product/614/41035) 文档。
- 已获取日志主题所在地域的域名（CLS_HOST）。
详细 CLS 域名列表请参见 [可用地域](https://cloud.tencent.com/document/product/614/18940) 文档。
- 已获取访问 CLS 侧鉴权所需的 API 密钥 ID（TmpSecretId）以及 API 密钥 Key（TmpSecretKey）。
可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 查看。

## K8s 日志采集原理
K8s 集群上部署日志采集主要涉及 Log-Provisioner，Log-Agent，LogListener 三个组件，以及一个 LogConfig 采集配置。
- LogConfig：日志采集配置，定义了日志在哪里被采集， 采集后如何解析， 以及解析后投递至哪个 CLS 日志主题中。
- Log-Provisioner： 将 LogConfig 中定义日志采集配置信息同步至 CLS。
- Log-Agent：监听 LogConfig 和节点上容器的变化， 动态计算容器中的日志文件在节点宿主机上的实际位置。
- LogListener：采集节点宿主机上的相应日志文件内容，解析并上传至 CLS。


## 操作流程
<dx-steps>
- <a href="#crd">定义 LogConfig 资源类型</a>
- <a href="#logconfig_def">定义 LogConfig 对象</a>
- <a href="#logconfig_create">创建 LogConfig 对象</a>
- <a href="#configmap">配置 CLS 鉴权 ConfigMap</a>
- <a href="#log-provisioner">部署 Log-Provisioner</a>
- <a href="#log-agent">部署 Log-Agent 和 Loglistener</a>
</dx-steps>

## 操作步骤

### 步骤1：定义 LogConfig 资源类型[](id:crd)

使用 K8s 中的 Custom Resource Definition（CRD）定义 LogConfig 资源类型。 
以 Master 节点路径 /usr/local/ 为例，使用 wget 命令下载 CRD.yaml 声明文件，使用 kubectl 定义 LogConfig 资源类型。
```shell
wget https://mirrors.tencent.com/install/cls/k8s/CRD.yaml
kubectl create -f /usr/local/CRD.yaml
```

### 步骤2：定义 LogConfig 对象[](id:logconfig_def)

通过创建 LogConfig 对象定义日志采集配置。以 Master 节点路径/usr/local/为例，使用 wget 命令下载 LogConfig.yaml 声明文件。
```shell
wget https://mirrors.tencent.com/install/cls/k8s/LogConfig.yaml
```
LogConfig.yaml 声明文件主要分为如下两部分：
- clsDetail：定义日志解析格式，以及目标日志主题 ID（topicId）。
- inputDetail：定义采集日志源，即日志从哪里被采集。

>! 配置时，请将 clsDetail 中的 topicId 项修改为您创建的日志主题 ID。


#### 日志解析格式

<dx-tabs>
::: 单行全文格式 [](id:single_line)
单行全文日志是指一行日志内容为一条完整的日志。日志服务在采集的时候，将使用换行符 \n 来作为一条日志日志的结束符。为了统一结构化管理，每条日志都会存在一个默认的键值\_\_CONTENT\_\_，但日志数据本身不再进行日志结构化处理，也不会提取日志字段，日志属性的时间项由日志采集的时间决定。

假设一条日志原始数据为：
```
Tue Jan 22 12:08:15 CST 2019 Installed: libjpeg-turbo-static-1.2.90-6.el7.x86_64
```

LogConfig 配置参考示例如下：
```yaml
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
::: 多行全文格式 [](id:multi_line)
多行全文日志是指一条完整的日志数据可能跨占多行（例如 Java  stacktrace）。在这种情况下，以换行符 \n 为日志的结束标识符就显得有些不合理，为了能让日志系统明确区分开每条日志，采用首行正则的方式进行匹配，当某行日志匹配上预先设置的正则表达式，就认为是一条日志的开头，而下一个行首出现作为该条日志的结束标识符.

多行全文也会设置一个默认的键值\_\_CONTENT\_\_，但日志数据本身不再进行日志结构化处理，也不会提取日志字段，日志属性的时间项由日志采集的时间决定。

假设一条多行日志原始数据为：
```
2019-12-15 17:13:06,043 [main] ERROR com.test.logging.FooFactory:
java.lang.NullPointerException
    at com.test.logging.FooFactory.createFoo(FooFactory.java:15)
    at com.test.logging.FooFactoryTest.test(FooFactoryTest.java:11)
```

LogConfig 配置的参考如下：
```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  clsDetail:
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    # 多行日志
    logType: multiline_log
    extractRule:
      # 只有以日期时间开头的行才被认为是新一条日志的开头，否则就添加换行符\n并追加到当前日志的尾部
      beginningRegex: \d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\s.+
```

采集到日志服务的数据为：
```
__CONTENT__:2019-12-15 17:13:06,043 [main] ERROR com.test.logging.FooFactory:\njava.lang.NullPointerException\n    at com.test.logging.FooFactory.createFoo(FooFactory.java:15)\n    at com.test.logging.FooFactoryTest.test(FooFactoryTest.java:11)
```
:::
::: 单行-完全正则格式 [](id:single_full_regex)
单行完全正则格式通常用来处理结构化的日志，指将一条完整日志按正则方式提取多个 key-value 的日志解析模式。

假设一条日志原始数据为：
```
10.135.46.111 - - [22/Jan/2019:19:19:30 +0800] "GET /my/course/1 HTTP/1.1" 127.0.0.1 200 782 9703 "http://127.0.0.1/course/explore?filter%5Btype%5D=all&filter%5Bprice%5D=all&filter%5BcurrentLevelId%5D=all&orderBy=studentNum" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"  0.354 0.354
```

LogConfig 配置的参考如下：
```
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
      keys:  ['remote_addr','time_local','request_method','request_url','http_protocol','http_host','status','request_length','body_bytes_sent','http_referer','http_user_agent','request_time','upstream_response_time']
```

采集到日志服务的数据为：
```
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
```
:::
::: 多行-完全正则格式 [](id:multi_full_regex)
多行-完全正则模式适用于日志文本中一条完整的日志数据跨占多行（例如 Java 程序日志），可按正则表达式提取为多个 key-value 键值的日志解析模式。若不需要提取 key-value，请参阅多行全文格式进行配置。

假设一条日志原始数据为：
```
[2018-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened
   at TestPrintStackTrace.f(TestPrintStackTrace.java:3)
   at TestPrintStackTrace.g(TestPrintStackTrace.java:7)
   at TestPrintStackTrace.main(TestPrintStackTrace.java:16)
```

LogConfig 配置的参考如下：
```yaml
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
          keys: ['time','level','msg']
```

根据提取的 key，采集到日志服务的数据为：
```
time： 2018-10-01T10:30:01,000`
level： INFO`
msg：java.lang.Exception: exception happened
   at TestPrintStackTrace.f(TestPrintStackTrace.java:3)
   at TestPrintStackTrace.g(TestPrintStackTrace.java:7)
   at TestPrintStackTrace.main(TestPrintStackTrace.java:16)
```
:::
::: JSON 格式 [](id:json)
JSON 格式日志会自动提取首层的 key 作为对应字段名，首层的 value 作为对应的字段值，以该方式将整条日志进行结构化处理，每条完整的日志以换行符\n为结束标识符。

假设一条 JSON 日志原始数据为：
```
{"remote_ip":"10.135.46.111","time_local":"22/Jan/2019:19:19:34 +0800","body_sent":23,"responsetime":0.232,"upstreamtime":"0.232","upstreamhost":"unix:/tmp/php-cgi.sock","http_host":"127.0.0.1","method":"POST","url":"/event/dispatch","request":"POST /event/dispatch HTTP/1.1","xff":"-","referer":"http://127.0.0.1/my/course/4","agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0","response_code":"200"}
```

LogConfig 配置的参考如下：
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  clsDetail:
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    # JSON格式日志
    logType: json_log
```

采集到日志服务的数据为：
```
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
:::
::: 分隔符格式 [](id:delimiter)
分隔符日志是指一条日志数据可以根据指定的分隔符将整条日志进行结构化处理，每条完整的日志以换行符 \n 为结束标识符。日志服务在进行分隔符格式日志处理时，您需要为每个分开的字段定义唯一的 key。

假设您的一条日志原始数据为：
```
10.20.20.10 ::: [Tue Jan 22 14:49:45 CST 2019 +0800] ::: GET /online/sample HTTP/1.1 ::: 127.0.0.1 ::: 200 ::: 647 ::: 35 ::: http://127.0.0.1/
```

LogConfig 配置的参考如下：
```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
  clsDetail:
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
    # 分隔符日志
    logType: delimiter_log
    extractRule:
      # 分隔符
      delimiter: ':::'
      # 提取的key列表，与被分割的字段一一对应
      keys: ['IP','time','request','host','status','length','bytes','referer']
```

采集到日志服务的数据为：
```
IP: 10.20.20.10
bytes: 35
host: 127.0.0.1
length: 647
referer: http://127.0.0.1/
request: GET /online/sample HTTP/1.1
status: 200
time: [Tue Jan 22 14:49:45 CST 2019 +0800]
```
:::
</dx-tabs>


#### 日志源

CLS 支持以下几种集群日志源：

<dx-tabs>
::: 容器标准输出 [](id:pod_stdout)
示例1：采集 default 命名空间中的所有容器的标准输出
```yaml
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

示例2：采集 production 命名空间中属于 ingress-gateway deployment 的 pod 中的容器的标准输出
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

示例3：采集 production 命名空间中 pod 标签中包含 “k8s-app=nginx” 的 pod 中的容器的标准输出
```yaml
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
:::
::: 容器文件 [](id:pod_file)
示例1：采集 production 命名空间中属于 ingress-gateway deployment 的 pod 中的 nginx 容器中 /data/nginx/log/ 路径下名为 access.log 的文件
```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
spec:
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

示例2：采集 production 命名空间中 pod 标签包含 “k8s-app=ingress-gateway” 的 pod 中的 nginx 容器中 /data/nginx/log/ 路径下名为 access.log 的文件
```yaml
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
:::
::: 主机文件 [](id:node_file)
示例: 采集主机 /data/ 路径下所有 .log 文件
```yaml
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
:::
:::
</dx-tabs>

### 步骤3：创建 LogConfig 对象 [](id:logconfig_create)

由于 [步骤2：定义 LogConfig 对象](#logconfig_def) 定义了 LogConfig.yaml 声明文件，我们可以使用 kubectl 命令创建 LogConfig 对象。
```shell
kubectl create -f /usr/local/LogConfig.yaml
```

### 步骤4：配置 CLS 鉴权 ConfigMap [](id:configmap)

将日志从自建 K8s 集群上传至 CLS 涉及鉴权，需要创建 ConfigMap 用于存储 **API 密钥 ID** 与 **API 密钥 KEY**。

1. 以 Master 节点路径 /usr/local/ 为例，使用 wget 命令下载 ConfigMap.yaml 声明文件。
```shell
wget https://mirrors.tencent.com/install/cls/k8s/ConfigMap.yaml
```
>! 配置时，请将 ConfigMap.yaml 中的 **TmpSecretId** 和 **TmpSecretKey** 配置为您的 **API 密钥 ID** 和 **API 密钥 KEY**。
2. 使用 kubectl 命令创建 ConfigMap 对象。
```shell
kubectl create -f /usr/local/ConfigMap.yaml
```


### 步骤5：部署 Log-Provisioner [](id:log-provisioner)

Log-Provisioner 负责发现并监听 LogConfig 资源中 CLS 消费端信息，日志采集规则，以及日志文件路径，并同步至 CLS。 

1. 以 Master 节点路径 /usr/local/ 为例，使用 wget 命令下载 Log-Provisioner.yaml 声明文件。
```shell
wget https://mirrors.tencent.com/install/cls/k8s/Log-Provisioner.yaml
```
>! 配置时，请将 Log-Provisioner.yaml 中环境变量 env 下的 **CLS_HOST** 字段配置为目标日志主题所在地域的域名。 不同地域的域名请参见 [可用地域](https://cloud.tencent.com/document/product/614/18940) 文档。同时， 环境变量 env 下的 **CLUSTER_ID** 字段需配置为与您账号下的所有机器组名称不同的任意名称。 您可在 CLS 控制台中的机器组管理页面查看您账号下的所有机器组。
>
2. 使用 kubectl 以 Deployment 的方式部署 Log-Provisioner。
```shell
kubectl create -f /usr/local/Log-Provisioner.yaml
```


### 步骤6：部署 Log-Agent 和 Loglistener [](id:log-agent)

集群的日志采集主要分为两个部分， 一个是 Log-Agent，一个是 Loglistener：
- Log-Agent 负责拉取集群中 LogConfig 中的日志源信息，并计算容器日志在宿主机上映射的绝对路径。
- Loglistener 负责采集与解析宿主机日志文件路径下的日志文件，并上传至 CLS。


1. 以 Master 节点路径 /usr/local/ 为例，使用 wget 命令下载 Log-Agent 和 Loglistener 的声明文件。
```shell
wget https://mirrors.tencent.com/install/cls/k8s/Log-Agent.yaml
```
>! 
> - 置时，请将 Log-Agent.yaml 中环境变量 env 下的 **CLS_HOST** 字段配置为目标日志主题所在地域的域名。 不同地域的域名请参见 [可用地域](https://cloud.tencent.com/document/product/614/18940) 文档。同时， 环境变量 env 下的 **CLUSTER_ID** 字段需配置为与您账号下的所有机器组名称不同的任意名称。 您可在 CLS 控制台中的机器组管理页面查看您账号下的所有机器组。
> - 如果宿主机的 docker 根目录不在 /var/lib/docker（即在宿主机的根目录）下，需要在 Log-Agent.yaml 声明文件中把 docker 的根目录映射到容器中，如下图所示，将 /data/docker 挂载到容器中：
> ![](https://main.qcloudimg.com/raw/7a6dd1f80f7e33cdf2f4db3695f15555.png)
2. 使用 kubectl 命令，以 DaemonSet 的方式部署 Log-Agent 和 Loglistener。
```shell
kubectl create -f /usr/local/Log—Agent.yaml
```

## 后续操作

至此， 即完成了集群日志采集的所有部署。您可以前往 [CLS 控制台 > 检索分析](https://console.cloud.tencent.com/cls/search) 查看采集上来的日志。
![](https://main.qcloudimg.com/raw/f101fbb8db69e5a98821ca8691d198a1.png)
