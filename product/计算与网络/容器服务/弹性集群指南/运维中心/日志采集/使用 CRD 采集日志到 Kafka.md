

弹性容器服务 EKS 不仅支持上传日志到 CLS，也支持采集日志到自建 Kafka 或者 CKafka。

## 创建 CRD
若需要采集日志到 Kafka，只需定义 CRD 即可。具体模版如下：

```
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig                          ## 默认值
metadata:
  name: test                             ## CRD资源名，在集群内唯一
spec:
  kafkaDetail:
    brokers: xxxxxx       # 必填，broker地址，一般是域名:端口，多个地址以“,”分隔
    topic: xxxxxx         # 必填，topicID        
    messageKey:           # 选填，指定pod字段作为key上传到指定分区
      valueFrom:
        fieldRef:
          fieldPath: metadata.name   
				timestampKey:            #时间戳的key，默认是@timestamp
    timestampFormat:              #时间戳的格式，默认是double
  inputDetail:
    type: container_stdout                  ## 采集日志的类型，包括container_stdout（容器标准输出）、container_file（容器文件）

    containerStdout:                        ## 容器标准输出
      namespace: default                    ## 采集容器的kubernetes命名空间，如果不指定，代表所有命名空间
      allContainers: false                  ## 是否采集指定命名空间中的所有容器的标准输出
      container: xxx                        ## 采集日志的容器名，此处可填空
      includeLabels:                        ## 采集包含指定label的Pod
        k8s-app: xxx                        ## 只采pod标签中配置"k8s-app=xxx"的pod产生的日志，与workloads、allContainers=true不能同时指定
      workloads:                            ## 要采集的容器的Pod所属的kubernetes workload
      -namespace: prod                      ## workload的命名空间
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
  
```




## 注意事项
若无法采集日志，请销毁重建 Pod 重试。

