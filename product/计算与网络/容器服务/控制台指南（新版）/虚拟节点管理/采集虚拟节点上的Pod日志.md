


本文主要介绍 TKE 集群中调度至虚拟节点的 Pod 如何采集日志，包括：
- [采集日志至 CLS](#toCLS)
- [采集日志至 Kafka](#toKafka)



## 采集日志至 CLS[](id:toCLS)

#### 服务角色授权
在采集虚拟节点上的 Pod 日志至 CLS 之前，需要进行服务角色授权，以保证将日志正常上传到 CLS。

操作步骤如下：
1. 登录**访问管理控制台** > **[角色](https://console.cloud.tencent.com/cam/role)**。
2. 在角色页面单击**新建角色**。
3. 在“选择角色载体”中，选择**腾讯云产品服务** > **容器服务(tke)** > **容器服务-EKS日志采集**，并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/3ccf4f76b4b0ca6d0b6ffad90c8a62d0.png)
4. 确认角色策略，单击**下一步**。
5. 审阅角色策略，单击**完成**，即可完成为该账号配置该角色。




#### 配置日志采集

服务角色授权完成后，需要开启 TKE 日志采集功能，并配置相应的日志采集规则。例如，指定工作负载采集和指定 pod labels 采集。详情可参见 [通过控制台使用 CRD 配置日志采集](https://cloud.tencent.com/document/product/457/36771)。



## 采集日志至 Kafka[](id:toKafka)

若需要采集虚拟节点上的 Pod 的日志至自建 Kafka 或者 CKafka，需要您自行配置 CRD，定义采集源及消费端，CRD 配置完成后，Pod 自带的采集器会依照规则进行日志采集。
CRD 具体配置如下所示：
<dx-codeblock>
::: yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig                          ## 默认值
metadata:
  name: test                                ## CRD资源名，在集群内唯一
spec:
  kafkaDetail:
    brokers: xxxxxx       # 必填，broker地址，一般是域名:端口，多个地址以“,”分隔
    topic: xxxxxx         # 必填，topicID        
    messageKey:           # 选填，指定pod字段作为key上传到指定分区
      valueFrom:
        fieldRef:
          fieldPath: metadata.name   
				timestampKey:            #时间戳的key，默认是@timestamp
    timestampFormat:       #时间戳的格式，默认是double
  inputDetail:
    type: container_stdout                  ## 采集日志的类型，包括container_stdout（容器标准输出）、container_file（容器文件）

    containerStdout:                        ## 容器标准输出
      namespace: default                    ## 采集容器的kubernetes命名空间，如果不指定，代表所有命名空间
      allContainers: false                  ## 是否采集指定命名空间中的所有容器的标准输出
      container: xxx                        ## 采集日志的容器名，此处可填空
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
:::
</dx-codeblock>




