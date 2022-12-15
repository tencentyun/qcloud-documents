## 操作场景
您不仅可以 [使用控制台配置日志采集](https://cloud.tencent.com/document/product/457/36771)，还可通过自定义资源（CustomResourceDefinitions，CRD）的方式配置日志采集。CRD 支持采集容器标准输出、容器文件和主机文件，支持多种日志采集格式。支持投递到 CLS 和 CKafka 等不同消费端。

## 前提条件
已在容器服务控制台的 **[运维功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=8)** 中开启日志采集，操作详情见 [开启日志采集](https://cloud.tencent.com/document/product/457/83871)。


## CRD 介绍

### 结构总览

```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig                 ## 默认值
metadata:
  name: test					## CRD资源名，在集群内唯一
spec:
  clsDetail:					## 投递到CLS的配置
    ...
  inputDetail:                  ## 采集数据源配置
    ...
  kafkaDetail:					## 投递到 ckafka 或者自建kafka配置
    ...
status:							## CRD资源状态
  status: ""
  code: ""						## 调用接口出错时，接口返回的错误码
  reason: ""					## 出错原因
```


### clsDetail 字段说明

>! topic 指定后不允许修改。


```yaml
  clsDetail:
    ## 自动创建日志主题，需要同时指定日志集和主题的name
    logsetName: test                    ## CLS日志集的name，若无该name的日志集，会自动创建，若有，会在该日志集下创建日志主题
    topicName: test                     ## CLS日志主题的name，若无该name的日志主题，会自动创建
	
	# 选择已有日志集日志主题， 如果指定了日志集未指定日志主题，则会自动创建一个日志主题
    logsetId: xxxxxx-xx-xx-xx-xxxxxxxx  ## CLS日志集的ID，日志集需要在CLS中提前创建
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx   ## CLS日志主题的ID，日志主题需要在CLS中提前创建，且没有被其它采集配置占用
	
    logType: json_log  ## 日志采集格式，json_log代表 json 格式，delimiter_log代表分隔符格式，minimalist_log代表单行全文格式，multiline_log代表多行全文格式，fullregex_log代表完全正则格式。默认为minimalist_log
	logFormat: xxx                      ## 日志格式化方式
	period: 30					        ## 生命周期，单位天，可取值范围1~3600。取值为3640时代表永久保存
	partitionCount:                     ## Integer 类型，日志主题分区个数。默认创建1个，最大支持创建10个分区。
	tags:                             ## 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持9个标签键值对，同一个资源只能绑定到同一个标签键下。
	 - key: xxx							  ## 标签key
	 value: xxx                      ## 标签value
	autoSplit: false					## boolen 类型，是否开启自动分裂，默认值为true
	maxSplitPartitions:
	storageType: hot.                  ## 日志主题的存储类型，可选值 hot（标准存储），cold（低频存储）；默认为hot。
	excludePaths:                      ## 采集黑名单路径列表
	  - type: File						  ##  类型，选填File或Path 
	      value: /xx/xx/xx/xx.log         ## type 对应的值
	indexs: 							 ## 创建 topic 时可自定义索引方式和字段
	  - indexName:   ## 需要配置键值或者元字段索引的字段，元字段Key无需额外添加__TAG__.前缀，与上传日志时对应的字段Key一致即可，腾讯云控制台展示时将自动添加__TAG__.前缀
	      indexType:  ## 字段类型，目前支持的类型有：long、text、double
	      tokenizer:  ## 字段的分词符，其中的每个字符代表一个分词符；仅支持英文符号及\n\t\r；long及double类型字段需为空；text类型字段推荐使用 @&?|#()='",;:<>[]{}/ \n\t\r\ 作为分词符；
	      sqlFlag:   ## boolen 字段是否开启分析功能
	      containZH: ## boolen 是否包含中文
	region: ap-xxx                     ## topic 所在地域，用于跨地域投递
    userDefineRule: xxxxxx             ## 用户自定义采集规则，Json格式序列化的字符串
    extractRule: {}                    ## 提取、过滤规则。 如果设置了ExtractRule，则必须设置LogType
```

### inputDetail 字段说明
```yaml
  inputDetail:
    type: container_stdout   ## 采集日志的类型，包括container_stdout（容器标准输出）、container_file（容器文件）、host_file（主机文件）

    containerStdout:        ## 容器标准输出
      namespace: default    ## 采集容器的kubernetes命名空间。支持多个命名空间，如果有多个命名空间使用","分隔，如：default,namespace。 如果不指定，代表所有命名空间。注意：与 excludeNamespace 不能同时指定
      excludeNamespace: nm1,nm2   ## 排除采集容器的kubernetes命名空间。支持多个命名空间，如果有多个命名空间使用","分隔，如：nm1,nm2。 如果不指定，代表所有命名空间。 注意：与 namespace 不能同时指定
	  nsLabelSelector: environment in (production),tier in (frontend) ## 根据命名空间label 筛选符合的 namespace
      allContainers: false       ## 是否采集指定命名空间中的所有容器的标准输出。注意:allContainers=true 时不能同时指定 workloa，includeLabels 和 excludeLabels
      container: xxx             ## 采集日志的容器名，为空时，代表采集所有符合容器的日志名。 注意：与 
      excludeLabels:  ## 采集不包含包含指定label的Pod，与workload，namespace 和 excludeNamespace 不能同时指定
        key2: value2  ## 支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被排除，注意输入多个value值时请使用逗号隔开。如果同时指定了 includeLabels，则匹配与 includeLabels 交集的pod

      includeLabels:  ## 采集包含指定label的Pod，与workload，namespace 和 excludeNamespace 不能同时指定
        key: value1   ## 收集规则收集的日志会带上metadata，并上报到消费端。支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被匹配，注意输入多个value值时请使用逗号隔开。 如果同时指定了 excludeLabels，则匹配与 excludeLabels 交集的pod
		
      metadataLabels:            ## 指定具体哪些pod label被当做元数据采集，如果不指定，则采集所有pod label为元数据
      - label1
      customLabels:              ## 用户自定义metadata
        label: l1
	  
      workloads:
      - container: xxx    ## 要采集的容器名，如果不指定，代表workload Pod中的所有容器
        kind: deployment  ## workload类型，支持deployment、daemonset、statefulset、job、cronjob
        name: sample-app  ## workload的名字
        namespace: prod   ## workload的命名空间
		
    containerFile:  ## 容器内文件
      namespace: default      ## 采集容器的kubernetes命名空间，必须指定一个命名空间	  
      excludeNamespace: nm1,nm2   ## 排除采集容器的kubernetes命名空间。支持多个命名空间，如果有多个命名空间使用","分隔，如：nm1,nm2。 如果不指定，代表所有命名空间。 注意：与 namespace 不能同时指定
      nsLabelSelector: environment in (production),tier in (frontend) ## 根据命名空间label 筛选符合的 namespace
      container: xxx          ## 采集日志的容器名，为 * 时，代表采集所有符合容器的日志名
      logPath: /var/logs      ## 日志文件夹，不支持通配符
      filePattern: app_*.log  ## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
      customLabels:   ## 用户自定义metadata
        key: value
      excludeLabels:  ## 采集不包含包含指定label的Pod，与workload不能同时指定
        key2: value2  ## 支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被排除，注意输入多个value值时请使用逗号隔开。如果同时指定了 includeLabels，则匹配与 includeLabels 交集的pod

      includeLabels:  ## 采集包含指定label的Pod，与workload不能同时指定
        key: value1   ## 收集规则收集的日志会带上metadata，并上报到消费端。支持匹配同一个key下多个value值的pod，例填写enviroment = production,qa表示当key为enviroment，value值为production或qa时，均会被匹配，注意输入多个value值时请使用逗号隔开。 如果同时指定了 excludeLabels，则匹配与 excludeLabels 交集的pod
      metadataLabels:        ## 指定具体哪些pod label被当做元数据采集，如果不指定，则采集所有pod label为元数据
      - label1               ## pod label
      workload:
        container: xxx       ## 要采集的容器名，如果不指定，代表workload Pod中的所有容器
        name: sample-app     ## workload的名字

    hostFile:                ## 节点文件路径
      filePattern: '*.log'   ## 日志文件名，支持通配符 * 和 ? ，* 表示匹配多个任意字符，? 表示匹配单个任意字符
      logPath: /tmp/logs     ## 日志文件夹，不支持通配符
      customLabels:          ## 用户自定义metadata
        label1: v1
```

**extractRule 对象说明**

| 名称 | 类型 | 必填项 | 描述 |
|---------|---------|---------|---------|
| timeKey | String | 否 | 时间字段的 key 名字，time_key 和 time_format 必须成对出现。 |
| timeFormat | String | 否 | 时间字段的格式，参考 C 语言的 strftime 函数对于时间的格式说明输出参数。 |
| delimiter | String | 否 | 分隔符类型日志的分隔符，只有 log_type 为 delimiter_log 时有效。 |
| logRegex | String | 否 | 整条日志匹配规则，只有 log_type 为 fullregex_log 时有效。|
| beginningRegex	 | String | 否 | 行首匹配规则，只有 log_type 为 multiline_log 或 fullregex_log 时有效。|
| unMatchUpload | String | 否 | 解析失败日志是否上传，true 表示上传，false 表示不上传。 |
| unMatchedKey | String | 否 | 失败日志的 key。 |
| backtracking | String | 否 | 增量采集模式下的回溯数据量，默认-1（全量采集），0 表示增量。 |
| keys | Array of String | 否 | 取的每个字段的 key 名字，为空的 key 代表丢弃这个字段，只有 log_type 为 delimiter_log 时有效，json_log 的日志使用 json 本身的 key。 |
| filterKeys | Array of String | 否 | 需要过滤日志的 key，与 FilterRegex 按下标进行对应。 |
| filterRegex | Array of String | 否 | 需要过滤日志的 key 对应的 regex，与 FilterKeys 按下标进行对应。 |
| isGBK | String | 否 | 是否为 Gbk 编码。0: 否，1: 是。<br>注意：此字段可能返回 null，表示取不到有效值。 |
| jsonStandard | String | 否 | 是否为标准 json。0: 否，1: 是。<br>注意：此字段可能返回 null，表示取不到有效值。 |


### kafkaDetail 字段说明
``` yaml
  kafkaDetail:
    brokers: x.x.x.x:p    ## 必填，broker地址，一般是域名:端口，多个地址以“,”分隔
    topic: test		      ## 
    kafkaType: CKafka     ## kafka 类型, CKafka - ckafka，SelfBuildKafka - 自建kafka
    instanceId: xxxx      ## 当 kafkaType = CKafka， 设置ckafka实例 id
	   logType: minimalist_log ## kafka 日志解析类型，"minimalist_log" 或 "" 单行全文，"multiline_log" 多行全文，"json" json 格式
    timestampFormat: xxx   ## 时间戳的格式，默认是double
    timestampKey: xxx      ## 时间戳的key值，默认是"@timestamp"
	metadata:
	  formatType: default   ## metatdata 格式。 "default" 默认格式（与 eks kafka 采集器相同），"filebeat" filebeat 格式，"fluent-bit" fluent-bit 格式
    messageKey:            ## 支持指定一个Key，将日志投递到指定分区。默认不开启，日期随机投放；开启后带有同样Key的日志，将投递到相同的分区里。支持选择Pod字段作为Key，以Pod name为例，请选择Field>metadata.name
      value: Field        ## 必填，topicID
      valueFrom:
        fieldRef: 
          fieldPath: metadata.name ##  当key为Field时可选 metadata.name,metadata.namespace,spec.nodeName,spec.serviceAccountName
```



### status 字段说明

| status | 说明 |
|---------|---------|
| 状态为空 | 初始状态 |
| Synced | 采集配置处理成功 |
| Stale | 采集配置处理失败 |


## CRD 示例
### 配置容器标准输出 CRD 示例
<dx-tabs>
::: 所有容器
**指定命名空间**

```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: "test"
spec:
  clsDetail:
    .......
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
  inputDetail:
    containerStdout:
      allContainers: true
      namespace: default,kube-public
    type: container_stdout

```

**排除命名空间**

```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: "test"
spec:
  clsDetail:
    ........
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
  inputDetail:
    containerStdout:
      allContainers: true
      excludeNamespace: kube-system,kube-node-lease
    type: container_stdout

```
:::
::: 指定工作负载
```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: "test"
spec:
  clsDetail:
    ......
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
  inputDetail:
    containerStdout:
      allContainers: false
      workloads:
      - container: prod
        kind: deployment
        name: sample-app
        namespace: kube-system
    type: container_stdout
```

:::
::: 指定 Pod Labels
``` yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: test
spec:
  clsDetail:
    ......
    topicId: xxxxxx-xx-xx-xx-xxxxxxxx
  inputDetail:
    containerStdout:
      container: prod
      excludeLabels:
        key2: v2
      includeLabels:
        key1: v1
      namespace: default,kube-system
    type: container_stdout
```
:::
</dx-tabs>


### 配置容器文件路径 CRD 示例
<dx-tabs>
::: 指定工作负载

```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: test
spec:
  clsDetail:
    .......
    topicId: xxxx-xx-xx-xx-xxxx
  inputDetail:
    containerFile:
      container: prod
      filePattern: '*.log'
      logPath: /tmp/logs
      namespace: kube-system
      workload:
        kind: deployment
        name: sample-app
    type: container_file
```
:::
::: 指定 Pod Labels
```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  name: test
spec:
  clsDetail:
    .......
    topicId: xxxx-xx-xx-xx-xxxx
  inputDetail:
    containerFile:
      container: prod
      filePattern: '*.log'
      includeLabels:
        key1: v1
      excludeLabels:
        key2: v2
      logPath: /tmp/logs
      namespace: default,kube-public
    type: container_file
```
:::
</dx-tabs>

### 配置节点文件路径 CRD 示例
```yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata:
  creationTimestamp: "2022-03-13T12:48:49Z"
  generation: 4
  name: test
  resourceVersion: "11729531"
  selfLink: /apis/cls.cloud.tencent.com/v1/logconfigs/test
  uid: 233f4b72-cfef-4a43-abb8-e4d033185097
spec:
  clsDetail:
    .......
    topicId: xxxx-xx-xx-xx-xxxx
  inputDetail:
    hostFile:
      customLabels:
        testmetadata: v1
      filePattern: '*.log'
      logPath: /var/logs
    type: host_file
```
