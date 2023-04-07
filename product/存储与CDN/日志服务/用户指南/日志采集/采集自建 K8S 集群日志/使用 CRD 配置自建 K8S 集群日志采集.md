## 简介
日志服务 （Cloud Log Service， CLS）支持采集自建 K8s 集群上的日志，在进行日志采集前，需要在 K8s 自建集群上通过 CRD 定义日志采集配置（LogConfig），并部署安装 Log-Provisioner，Log-Agent，以及 LogListener。针对使用腾讯云容器服务（Tencent Kubernetes Engine ,TKE）的用户， 可参见 [TKE 开启日志采集](https://cloud.tencent.com/document/product/457/36771) 文档，通过控制台快速接入并使用日志服务。


## 前提条件

- 已创建 Kubernetes 1.10 及以上版本集群。
- 已配置自建 K8S 采集所需的云 API 权限，详情请参见 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374) 文档。
- 已开通日志服务， 创建日志集和日志主题，且获取日志主题 ID（topicId）。
详情请参见 [创建日志主题](https://cloud.tencent.com/document/product/614/41035) 文档。
- 已获取日志主题所在地域的域名（CLS_HOST）。
详细 CLS 域名列表请参见 [可用地域](https://cloud.tencent.com/document/product/614/18940) 文档。
- 已获取访问 CLS 侧鉴权所需的 API 密钥 ID（TmpSecretId）以及 API 密钥 Key（TmpSecretKey）。
可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 查看。


## K8s 日志采集原理
K8s 集群上部署日志采集主要涉及 Log-Provisioner，Log-Agent，LogListener 三个组件，以及一个 LogConfig 采集配置。
- LogConfig：日志采集配置，定义了日志在哪里被采集， 采集后如何解析， 以及解析后投递至哪个 CLS 日志主题中。
- Log-Agent：监听 LogConfig 和节点上容器的变化， 动态计算容器中的日志文件在节点宿主机上的实际位置。
- Log-Provisioner： 将 LogConfig 中定义日志采集配置信息同步至 CLS。
- LogListener：采集节点宿主机上的相应日志文件内容，解析并上传至 CLS。


## 操作流程
<dx-steps>

- <a href="#install_LogListener">自建 K8S 集群安装 LogListener</a>
- <a href="#logconfig_def">定义 LogConfig 对象</a>
- <a href="#logconfig_create">创建 LogConfig 对象</a>
</dx-steps>

## 操作步骤

### 步骤1： 自建 K8S 集群安装 LogListener[](id:install_LogListener)

首先，您需要在自建 Kubernetes 集群上安装 LogListener 组件，从而将日志收集到 CLS。详情请参见 [自建 K8S 集群安装 LogListener](https://cloud.tencent.com/document/product/614/64566) 文档。


### 步骤2：定义 LogConfig 对象[](id:logconfig_def)

通过CRD定义 LogConfig 对象中的日志采集配置。以 Master 节点路径/usr/local/为例，使用 wget 命令下载 LogConfig.yaml CRD声明文件。

```shell
wget https://mirrors.tencent.com/install/cls/k8s/LogConfig.yaml
```
LogConfig.yaml 声明文件主要分为如下两部分：
- clsDetail：CLS投递配置。
- inputDetail：日志源配置。

```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig                               ## 默认值
metadata:
  name: test						      	## CRD资源名，在集群内唯一
spec:
  clsDetail:							  	## 投递到CLS的配置
    ...
  inputDetail:                                ## 日志源配置
    ...
```

#### clsDetail（CLS投递配置）字段说明


```yaml
  clsDetail:
    # 自动创建日志主题，需要同时指定日志集和主题的name。定义后不可修改
    logsetName: test                      	## CLS日志集的name，若无该name的日志集，会自动创建，若有，会在该日志集下创建日志主题
    topicName: test                     	  ## CLS日志主题的name，若无该name的日志主题，会自动创建
	# 选择已有日志集日志主题， 如果指定了日志集未指定日志主题，则会自动创建一个日志主题。定义后不可修改
    logsetId: xxxxxx-xx-xx-xx-xxxxxxxx  	  ## CLS日志集的ID，日志集需要在CLS中提前创建
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx   	  ## CLS日志主题的ID，日志主题需要在CLS中提前创建，且没有被其它采集配置占用
    region: ap-xxx                        	## topic 所在地域，用于跨地域投递
    # 自动创建日志主题时， 定义日志主题配置。 定义后不可修改
    period: 30					        	## 生命周期，单位天，可取值范围1~3600。取值为3640时代表永久保存
    storageType: hot                  		## 日志主题的存储类型，可选值 hot（标准存储），cold（低频存储）；默认为hot。
    HotPeriod: 7                              ## 沉降周期，单位天。可取值范围1~3600。仅在storageType:hot时生效
    partitionCount:                       	## Integer 类型，日志主题分区个数。默认创建1个，最大支持创建10个分区。
    autoSplit: true					   	## boolen 类型，是否开启自动分裂，默认值为true
    maxSplitPartitions:	10		     	## Integer 类型，最大分裂数量。
    tags:                             		## 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持9个标签键值对，同一个资源只能绑定到同一个标签键下。
      - key: xxx						  	## 标签key
        value: xxx                        	## 标签value
    # 定义采集规则
    logType: json_log  			   		## 日志解析格式，json_log代表 json 格式，delimiter_log代表分隔符格式，minimalist_log代表单行全文格式，multiline_log代表多行全文格式，fullregex_log代表单行完全正则格式，multiline_fullregex_log代表多行完全正则格式。默认为minimalist_log
    logFormat: xxx                        	## 日志格式化方式
    excludePaths:                     		## 采集黑名单路径列表
      - type: File							##  类型，选填File或Path 
        value: /xx/xx/xx/xx.log           	## type 对应的值
    userDefineRule: xxxxxx             	   ## 用户自定义采集规则，Json格式序列化的字符串
    extractRule: {}                   		## 提取、过滤规则。 如果设置了ExtractRule，则必须设置LogType，详情参考extractRule对象说明
    AdvancedConfig:				   		## 高级采集配置
      MaxDepth: 1					     	## 最大目录深度
      FileTimeout: 60				     	## 文件超时属性
    # 定义索引配置。定义后不可修改
    indexs: 							  	## 创建 topic 时可自定义索引方式和字段
      - indexName:   				 		## 需要配置键值或者元字段索引的字段，元字段Key无需额外添加__TAG__.前缀，与上传日志时对应的字段Key一致即可，腾讯云控制台展示时将自动添加__TAG__.前缀
        indexType:  		      			## 字段类型，目前支持的类型有：long、text、double
        tokenizer:  				  		## 字段的分词符，其中的每个字符代表一个分词符；仅支持英文符号及\n\t\r；long及double类型字段需为空；text类型字段推荐使用 @&?|#()='",;:<>[]{}/ \n\t\r\ 作为分词符；
        sqlFlag:   				   		## boolen 字段是否开启分析功能
        containZH: 	       				## boolen 是否包含中文
```

**extractRule 对象说明**

| 名称           | 类型            | 必填项 | 描述                                                         |
| -------------- | --------------- | ------ | ------------------------------------------------------------ |
| timeKey        | String          | 否     | 日志时间戳使用日志中的指定字段。该配置为空则使用日志实际采集时间。time_key 和 time_format 必须成对出现。 |
| timeFormat     | String          | 否     | 时间字段的格式，参考 C 语言的 strftime 函数对于时间的格式说明输出参数。 |
| delimiter      | String          | 否     | 分隔符类型日志的分隔符，只有 log_type 为 delimiter_log 时有效。 |
| logRegex       | String          | 否     | 整条日志匹配规则，只有 log_type 为 fullregex_log 时有效。    |
| beginningRegex | String          | 否     | 行首匹配规则，只有 log_type 为 multiline_log 或 multiline_fullregex_log 时有效。 |
| unMatchUpload  | String          | 否     | 解析失败日志是否上传，true 表示上传，false 表示不上传。      |
| unMatchedKey   | String          | 否     | 解析失败日志的 key。                                         |
| backtracking   | String          | 否     | 增量采集模式下的回溯数据量，默认-1（全量采集），0 表示增量。 |
| keys           | Array of String | 否     | 取的每个字段的 key 名字，为空的 key 代表丢弃这个字段，只有 log_type 为 delimiter_log, fullregex_log，multiline_fullregex_log时有效，json_log 的日志使用 json 本身的 key。 |
| filterKeys     | Array of String | 否     | 需要过滤日志的 key，与 FilterRegex 按下标进行对应。          |
| filterRegex    | Array of String | 否     | 需要过滤日志的 key 对应的 regex，与 FilterKeys 按下标进行对应。 |
| isGBK          | String          | 否     | 是否为 Gbk 编码。0: 否，1: 是。<br>注意：此字段可能返回 null，表示取不到有效值。 |



#### 日志采集规则配置示例

#### <dx-tabs>
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


#### inputDetail（日志源）字段说明

```yaml
  inputDetail:
    type: container_stdout   			    	## 指定采集日志的类型，包括container_stdout（容器标准输出）、container_file（容器文件）、host_file（主机文件）
    containerStdout:        				 	## 容器标准输出配置，仅在type:container_stdout时生效
      namespace: default   			 	 	## 采集容器的kubernetes命名空间。支持多个命名空间，如果有多个命名空间使用","分隔，如：default,namespace。 如果不指定，代表所有命名空间。注意：与 excludeNamespace 不能同时指定
      excludeNamespace: nm1,nm2   		   	## 排除采集容器的kubernetes命名空间。支持多个命名空间，如果有多个命名空间使用","分隔，如：nm1,nm2。 如果不指定，代表所有命名空间。 注意：与 namespace 不能同时指定
	  nsLabelSelector: environment in (production),tier in (frontend) ## 根据命名空间label 筛选符合的 namespace
      allContainers: false      			 	## 是否采集指定命名空间中的所有容器的标准输出。注意:allContainers=true 时不能同时指定 workload，includeLabels 和 excludeLabels
      containerOperator: in                      ## container选择方式， 包含填in，排除填not in
      container: xxx             				## 指定采集或不采集日志的容器名
      includeLabels:  					   	## 采集包含指定label的Pod，与workload不能同时指定
        key: value1   					   	## 支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被匹配，注意输入多个value值时请使用逗号隔开。 如果同时指定了 excludeLabels，则匹配与 excludeLabels 交集的pod
      excludeLabels:  						   ## 采集不包含包含指定label的Pod，与workload，namespace 和 excludeNamespace 不能同时指定
        key2: value2  					   	## 支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被排除，注意输入多个value值时请使用逗号隔开。如果同时指定了 includeLabels，则匹配与 includeLabels 交集的pod
      metadataLabels:            				## 指定具体哪些pod label被当做元数据采集，如果不指定，则采集所有pod label为元数据
      - label1
      metadataContainer:					 	## 指定具体哪些容器环境相关元数据被采集，如果不指定，则采集所有容器环境相关元数据（namespace,pod_name,pod_ip,pod_uid,container_id,container_name,image_name）
      - namespace
      customLabels:              				## 用户自定义metadata
        label: l1
      workloads:						 		## 采集指定命名空间 -> 指定工作负载类型中 -> 指定工作负载 -> 指定容器中的日志
      - container: xxx    			   		## 要采集的容器名，如果不指定，代表workload Pod中的所有容器
        containerOperator: in                    ## container选择方式， 包含填in，排除填not in
        kind: deployment  			   		## workload类型，支持deployment、daemonset、statefulset、job、cronjob
        name: sample-app  			   		## workload的名字
        namespace: prod   			   		## workload的命名空间
		
    containerFile:  				 			## 容器内文件配置，仅在type:container_file时生效
      namespace: default      			   	## 采集容器的kubernetes命名空间，必须指定一个命名空间	  
      excludeNamespace: nm1,nm2   	       	## 排除采集容器的kubernetes命名空间。支持多个命名空间，如果有多个命名空间使用","分隔，如：nm1,nm2。 如果不指定，代表所有命名空间。 注意：与 namespace 不能同时指定
      nsLabelSelector: environment in (production),tier in (frontend) ## 根据命名空间label 筛选符合的 namespace
      containerOperator: in                      ## container选择方式， 包含填in，排除填not in
      container: xxx          			   	## 采集日志的容器名，为 * 时，代表采集所有符合容器的日志名
      logPath: /var/logs      			   	## 日志文件夹，不支持通配符
      filePattern: app_*.log 					## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
      includeLabels:  					   	## 采集包含指定label的Pod，与workload不能同时指定
        key: value1   					   	## 收集规则收集的日志会带上metadata，并上报到消费端。支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被匹配，注意输入多个value值时请使用逗号隔开。 如果同时指定了 excludeLabels，则匹配与 excludeLabels 交集的pod
      excludeLabels:  					   	## 采集不包含包含指定label的Pod，与workload不能同时指定
        key2: value2 							## 支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被排除，注意输入多个value值时请使用逗号隔开。如果同时指定了 includeLabels，则匹配与 includeLabels 交集的pod
      metadataLabels:        		        	## 指定具体哪些pod label被当做元数据采集，如果不指定，则采集所有pod label为元数据
      - namespace
      metadataContainer:				     	## 指定具体哪些容器环境相关元数据被采集，如果不指定，则采集所有容器环境相关元数据（namespace,pod_name,pod_ip,pod_uid,container_id,container_name,image_name）
      customLabels:   					   	## 用户自定义metadata
        key: value
      workload:
    	container: xxx    	  			 	## 要采集的容器名，如果不指定，代表workload Pod中的所有容器
        containerOperator: in                    ## container选择方式， 包含填in，排除填not in
        kind: deployment  				   	## workload类型，支持deployment、daemonset、statefulset、job、cronjob
        name: sample-app  					   ## workload的名字
        namespace: prod					  	## workload的命名空间

    hostFile:                					## 节点文件路径，仅在type:host_file时生效
      filePattern: '*.log'   					## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
      logPath: /tmp/logs     					## 日志文件夹，不支持通配符
      customLabels:          					## 用户自定义metadata
        label1: v1
```

### 日志源配置示例

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
        kind: deployment
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

[步骤2：定义 LogConfig 对象](#logconfig_def) 定义了 LogConfig.yaml 声明文件，我们可以基于LogConfig.yaml 声明文件，使用 kubectl 命令创建 LogConfig 对象。

```shell
kubectl create -f /usr/local/LogConfig.yaml
```
## 后续操作

至此， 即完成了集群日志采集的所有部署。您可以前往 [CLS 控制台 > 检索分析](https://console.cloud.tencent.com/cls/search) 查看采集上来的日志。
![](https://main.qcloudimg.com/raw/f101fbb8db69e5a98821ca8691d198a1.png)
