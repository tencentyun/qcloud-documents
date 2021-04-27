## 操作场景
EKS 日志采集功能可以将集群内服务的日志发送至 [日志服务 CLS](https://cloud.tencent.com/product/cls) 或用户自建 Kafka，适用于需要对 EKS 集群内服务日志进行存储和分析的用户。本文介绍如何使用弹性容器服务 EKS 提供的集群内日志采集功能。


EKS 日志采集功能需要在创建工作负载时手动开启。您可根据以下操作开启日志采集功能：
  - [配置日志采集](#output)
  - [配置日志消费端](#output2)
  - [通过 yaml 配置日志采集](#yaml)
  - [更新日志采集](#new)

## 说明事项
EKS 日志采集功能开启后，日志采集 Agent 根据您配置的采集路径和消费端，将采集到的日志以 JSON 的形式发送到您指定的消费端。消费端及采集路径说明如下：
  - **消费端**：日志采集服务支持 Kafka 或 CLS 作为日志的消费端。
  - **采集路径**：需要采集的日志的路径。采集路径支持采集标准输出（stdout）和绝对路径，支持 * 通配，多个采集路径以“,”分隔。 

## 前提条件

- 需确认 Kubernetes 集群能够访问日志消费端。
- 日志长度限制为单条2M，如果超过则会截断。
  <dx-alert infotype="notice" title="">
若日志输出速率过快，为避免 OOM，需要调整此参数配置，详情请参见 [如何调整日志采集配置](https://cloud.tencent.com/document/product/457/54614)。
</dx-alert>




## 操作步骤


### 配置日志采集[](id:output)
EKS 日志采集功能采集到的日志信息将会以 JSON 格式输出到您指定的消费端，并会附加相关的 Kubernetes metadata，包括容器所属 pod 的 label 和 annotation 等信息。具体操作步骤如下：
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【弹性集群】。
2. 进入“弹性集群”页面，选择需要日志采集的集群 ID，进入集群管理页面。
3. 在左侧“工作负载”中选择需要的工作负载类型，进入对应页面后选择【新建】。
4. 在“实例内容器”中选择【显示高级设置】，并勾选“开启”日志采集。如下图所示：
![](https://main.qcloudimg.com/raw/0ef3ce835e4d30651a48f54df9b23acb.png)
5. 参考以下信息进行日志消费端配置，您可选择 CLS 或 Kafka 作为日志消费端。如下图所示：
  - 推荐选择 [日志服务 CLS](https://cloud.tencent.com/product/cls) 为消费端，并选择日志集和日志主题。若无合适的日志集，请参考 [配置日志服务 CLS 作为日志消费端](#output2)。
   - 若选择 Kafka 为消费端，请参考 [配置 Kafka 作为日志消费端](#output2)。
![](https://main.qcloudimg.com/raw/4a0e6bef8d5b0c800dfdb6de9104fe4c.png)
6. 选择角色或者密钥进行授权。
>! 
 - 同一 pod 下的容器只能选择同一种授权方式，以您最后修改的授权方式为准。例如第一个容器选择了密钥授权，第二个选择了角色授权，最终两个容器都是角色授权。
 - 同一 pod 下的容器只能选择同一个角色授权。
>
<dx-tabs>
::: 角色授权
 - 选择具有访问日志服务 CLS 权限的角色名称，如下图所示：
![](https://main.qcloudimg.com/raw/eb325a52c59486e1051a381ee8ae135d.png)
 - 若无合适的角色，创建过程参考以下步骤：
  1. 登录访问管理控制台，在左侧导航栏选择【[角色](https://console.cloud.tencent.com/cam/role)】。
  2. 在“角色”页面，单击【新建角色】。
  3. 在“选择角色载体” 弹窗中，选择【腾讯云产品服务】，进入【新建自定义角色】页面。
  4. 在“输入角色载体信息”步骤中，选择**绑定【云服务器（cvm）】载体**，单击【下一步】。
  <dx-alert infotype="notice" title="">
必须选择【云服务器（cvm）】作为角色载体，选择容器服务则无法完成授权。
  </dx-alert>
  5. 在“配置角色策略”步骤中，选择【QcloudCLSAccessForApiGateWayRole】策略，单击【下一步】。
  6. 在“审阅”步骤中，输入您的角色名称，审阅您即将创建角色的相关信息，单击【完成】后即完成自定义角色创建。详情请参见 [创建角色](https://cloud.tencent.com/document/product/598/19381)。
:::
::: 密钥授权
- 选择您利用账号 API 密钥的 SecretId 和 SecretKey 作为变量值进行创建的集群 Secret 配置名称。
![](https://main.qcloudimg.com/raw/90103c9759c3e2df9bd6f66a507e60fb.png)
- 若无合适的 Secret，需新建 Secret。详情请参见 [Secret 管理](https://cloud.tencent.com/document/product/457/31718)。其中 SecretId 和 SecretKey 可在 [API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。
>! API 密钥对应的用户需具备访问日志服务 CLS 的权限。若无 API 密钥，需新建 API 密钥。详情请参见 [访问密钥](https://cloud.tencent.com/document/product/598/40487)。
:::
</dx-tabs>
7. 配置采集路径。如下图所示：
![](https://main.qcloudimg.com/raw/7b9799a0d2a6d1200318dfc35243ea52.png)
至此已完成日志采集功能配置，您可按需进行该工作负载的其他配置。


### 配置日志消费端[](id:output2) 
EKS 日志采集功能支持指定用户自建的 Kafka 实例、日志服务 CLS 指定的日志主题作为日志内容的消费端。日志采集 Agent 会将采集到的日志发送到指定 Kafka 的指定 Topic 或指定的 CLS 日志主题。

<dx-tabs>
::: 配置Kafka作为日志消费端
选择 Kafka 作为日志采集的消费端，推荐使用 CKafka，消费、生产方式与原生版体验一致，并支持配置告警。
在容器配置中填写 Kafka 的 Broker 地址及 Topic，需要保证集群内所有资源都能够访问用户指定的 Kafka Topic。如下图所示：
![](https://main.qcloudimg.com/raw/2a226f61d5db3a048f804e83d3f0debb.png)
>! Kafka 的 Topic 配置中 `cleanup.policy` 参数需选择 delete，选择 compact 会导致 CLS 无法上报到 Kafka 而造成数据丢失。如下图所示：
![](https://main.qcloudimg.com/raw/c3f3a6f892b9c07cb24f7e210db5f80e.png)
:::
::: 配置CLS作为日志消费端
- 日志服务 CLS 目前只能支持同地域的容器集群进行日志采集上报。详情请参见 [创建日志集和日志主题](https://cloud.tencent.com/document/product/614/34340#3.-.E5.88.9B.E5.BB.BA.E6.97.A5.E5.BF.97.E9.9B.86.E5.92.8C.E6.97.A5.E5.BF.97.E4.B8.BB.E9.A2.98)。
- 打开日志主题的【日志索引】。如下图所示：
![](https://main.qcloudimg.com/raw/a8413fb410367e01acfa9ff62e7a291d.png)
:::
</dx-tabs>

[](id:yaml)
### 通过 yaml 配置日志采集 [](id:yaml)
本文提供采集日志到 Kafka、通过 secret 采集日志到 CLS 和通过 role 采集日志到 CLS 三种方式，请按需选择：
>! 若 yaml 中同时配置了密钥和角色授权，pod 实际上采用的是角色授权。

<dx-tabs>
::: 采集日志到Kafka
通过增加环境变量开启日志采集。
```shell
apiVersion: apps/v1beta2
kind: Deployment
metadata:
   annotations:
     deployment.kubernetes.io/revision: "1"
labels:
     k8s-app: kafka
     qcloud-app: kafka
   name: kafka
   namespace: default
spec:
   replicas: 1
   selector:
     matchLabels:
       k8s-app: kafka
       qcloud-app: kafka
  template:
metadata:
       annotations:
         eks.tke.cloud.tencent.com/cpu: "0.25"
         eks.tke.cloud.tencent.com/mem: "0.5Gi"
labels:
         k8s-app: kafka
         qcloud-app: kafka
     spec:
       containers:
       - env:
         - name: EKS_LOGS_OUTPUT_TYPE
           value: kafka
         - name: EKS_LOGS_KAFKA_BROKERS
           value: 10.0.16.42:9092
         - name: EKS_LOGS_KAFKA_TOPIC
           value: eks
         - name: EKS_LOGS_METADATA_ON
           value: "true"
         - name: EKS_LOGS_LOG_PATHS
           value: stdout,/tmp/busy*.log
         image: busybox:latest
         command: ["/bin/sh"]
         args: ["-c", "while true; do echo hello world; date; echo hello >> /tmp/busy.log; sleep 1; done"]
         imagePullPolicy: Always
         name: while
         resources:
           requests:
             cpu: 250m
             memory: 512Mi
```
**字段说明：**
<table>
	<tr>
		<th>字段名</th> <th>含义</th>
	</tr>
	<tr>
		<td>EKS_LOGS_OUTPUT_TYPE</td> <td>消费端支持 kafka 和 cls，根据该 key 判断是否启用日志收集。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOG_PATHS</td> <td>日志路径，支持 stdout（表示采集标准输出）和绝对路径，支持 * 通配，多个路径用“,”分隔。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_METADATA_ON</td> <td>支持 true 或 false。不填写则默认为 true。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_KAFKA_TOPIC</td> <td>日志主题。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_KAFKA_BROKERS</td> <td>kafka brokers，ip1:port1，ip1:port2，ip2:port2格式，多个用“,”分隔。对外用此环境变量，EKS_LOGS_KAFKA_HOST 以后不再对外可见。</td>
	</tr>
</table>
:::


::: 通过secret采集日志到CLS
#### 创建 secret[](id:z)
>! 以下示例为通过 yaml 手动创建 secret。如通过控制台创建 secret，则不需要进行64编码，详情请参考 [secret 管理](https://cloud.tencent.com/document/product/457/31718)。
>
通过 kubectl 执行以下命令，获取进行 base64编码的 secretid 和 secretkey。其中，secretid 及 secretkey 请替换为您账号的 secretid 和 secretkey，可在 [API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。
```shell
$ echo -n 'secretid' | base64
c2VjcmV0aWQ=
$ echo -n 'secretkey' | base64
c2VjcmV0a2V5
```
通过 yaml 手动创建 secret。secretid 及 secretkey 请使用在 [创建 secret](#z) 步骤中获取的值进行填写。
```shell
apiVersion: v1
kind: Secret
metadata:
   name: secretidkey
data:
   secretid: 
   secretkey: 
```

#### 创建deployment
通过增加环境变量开启日志采集。
```shell
apiVersion: apps/v1beta2
kind: Deployment
metadata:
   annotations:
     deployment.kubernetes.io/revision: "1"
   labels:
     k8s-app: cls
     qcloud-app: cls
   name: cls
   namespace: default
spec:
   replicas: 1
   selector:
     matchLabels:
       k8s-app: cls
       qcloud-app: cls
   template:
     metadata:
       annotations:
         eks.tke.cloud.tencent.com/cpu: "0.25"
         eks.tke.cloud.tencent.com/mem: "0.5Gi"
       labels:
         k8s-app: cls
         qcloud-app: cls
     spec:
       containers:
       - env:
         - name: EKS_LOGS_OUTPUT_TYPE
           value: cls
         - name: EKS_LOGS_LOGSET_NAME
           value: eks
         - name: EKS_LOGS_TOPIC_ID
           value: 617c8270-e8c8-46e2-a90b-d94c4bebe519
         - name: EKS_LOGS_SECRET_ID
           valueFrom:
             secretKeyRef:
               name: secretidkey
               key: secretid
         - name: EKS_LOGS_SECRET_KEY
           valueFrom:
             secretKeyRef:
               name: secretidkey
               key: secretkey
         - name: EKS_LOGS_LOG_PATHS
           value: stdout,/tmp/busy*.log
         - name: EKS_LOGS_METADATA_ON
           value: "true"
         image: busybox:latest
         command: ["/bin/sh"]
         args: ["-c", "while true; do echo hello world; date; echo hello >> /tmp/busy.log; sleep 1; done"]
         imagePullPolicy: Always
         name: hello
       - env:
         - name: EKS_LOGS_OUTPUT_TYPE
           value: cls
         - name: EKS_LOGS_LOGSET_NAME
           value: eks
         - name: EKS_LOGS_TOPIC_ID
           value: 617c8270-e8c8-46e2-a90b-d94c4bebe519
         - name: EKS_LOGS_SECRET_ID
           valueFrom:
             secretKeyRef:
               name: secretidkey
               key: secretid
         - name: EKS_LOGS_SECRET_KEY
           valueFrom:
             secretKeyRef:
               name: secretidkey
               key: secretkey
         - name: EKS_LOGS_LOG_PATHS
           value: stdout,/tmp/busy*.log
         - name: EKS_LOGS_METADATA_ON
           value: "true"
         image: busybox:latest
         command: ["/bin/sh"]
         args: ["-c", "while true; do echo hello world; date; echo hello >> /tmp/busy.log; sleep 1; done"]
         imagePullPolicy: Always
         name:world
```

**字段说明：**
<table>
<tr>
<th>字段名</th> <th>含义</th>
</tr>
<tr>
<td>EKS_LOGS_OUTPUT_TYPE</td> <td>消费端支持 kafka 和 cls，根据该 key 判断是否启用日志收集。</td>
</tr>
<tr>
<td>EKS_LOGS_LOG_PATHS</td> <td>日志路径，支持 stdout（表示采集标准输出）和绝对路径，支持 * 通配，多个路径用“,”分隔。</td></tr>
<tr>
<td>EKS_LOGS_METADATA_ON</td> <td>支持 true 或 false。不填写则默认为 true。</td>
</tr>
<tr>
<td>EKS_LOGS_LOGSET_NAME</td> <td>CLS 日志集名称。</td>
</tr>
<tr>
	<td>EKS_LOGS_TOPIC_ID</td> <td>CLS 日志集的主题 ID。</td>
</tr>
</tr>
<td>EKS_LOGS_SECRET_ID</td> <td>SecretId。</td>
</tr>
<tr>
<td>EKS_LOGS_SECRET_KEY</td> <td>SecretKey。</td>
</tr>
</tr>
</table>

:::



::: 通过role采集日志到CLS
#### 创建角色  
在 [访问管理控制台](https://console.cloud.tencent.com/cam/role) 新建角色，选择【腾讯云产品服务】，绑定【云服务器 CVM】载体，选择【QcloudCLSAccessForApiGateWayRole】策略。详情请参考 [创建角色](https://cloud.tencent.com/document/product/598/19381)。
在 pod template 中新增 annotation，指定 role 的名称，获取该 role 包含的权限策略。
```shell
template:
   metadata:
     annotations:
       eks.tke.cloud.tencent.com/role-name: "eks-pushlog"
```
#### 创建deployment
```shell
apiVersion: apps/v1beta2
kind: Deployment
metadata:
   annotations:
     deployment.kubernetes.io/revision: "1"
   labels:
     k8s-app: cls
     qcloud-app: cls
   name: cls
   namespace: default
spec:
   replicas: 1
   selector:
     matchLabels:
       k8s-app: cls
       qcloud-app: cls
   template:
     metadata:
       annotations:
         eks.tke.cloud.tencent.com/cpu: "0.25"
         eks.tke.cloud.tencent.com/mem: "0.5Gi"
         eks.tke.cloud.tencent.com/role-name: "eks-pushlog"
       labels:
         k8s-app: cls
         qcloud-app: cls
     spec:
       containers:
       - env:
         - name: EKS_LOGS_OUTPUT_TYPE
           value: cls
         - name: EKS_LOGS_LOGSET_NAME
           value: eks
         - name: EKS_LOGS_TOPIC_ID
           value: 617c8270-e8c8-46e2-a90b-d94c4bebe519
         - name: EKS_LOGS_LOG_PATHS
           value: stdout,/tmp/busy*.log
         - name: EKS_LOGS_METADATA_ON
           value: "true"
         image: busybox:latest
         command: ["/bin/sh"]
         args: ["-c", "while true; do echo hello world; date; echo hello >> /tmp/busy.log; sleep 1; done"]
         imagePullPolicy: Always
         name: hello
       - env:
         - name: EKS_LOGS_OUTPUT_TYPE
           value: cls
         - name: EKS_LOGS_LOGSET_NAME
           value: eks
         - name: EKS_LOGS_TOPIC_ID
           value: 617c8270-e8c8-46e2-a90b-d94c4bebe519
         - name: EKS_LOGS_LOG_PATHS
           value: stdout,/tmp/busy*.log
         - name: EKS_LOGS_METADATA_ON
           value: "true"
         image: busybox:latest
         command: ["/bin/sh"]
         args: ["-c", "while true; do echo hello world; date; echo hello >> /tmp/busy.log; sleep 1; done"]
         imagePullPolicy: Always
         name: world
```
**字段说明：**
<table>
	<tr>
		<th>字段名</th> <th>含义</th>
	</tr>
	<tr>
		<td>EKS_LOGS_OUTPUT_TYPE</td> <td>消费端支持 kafka 和 cls，根据该 key 判断是否启用日志收集。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOG_PATHS</td> <td>日志路径，支持 stdout（表示采集标准输出）和绝对路径，支持 * 通配，多个路径用“,”分隔。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_METADATA_ON</td> <td>支持 true 或 false。不填写则默认为 true。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOGSET_NAME</td> <td>CLS 日志集名称。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_TOPIC_ID</td> <td>CLS 日志集的主题 ID。</td>
	</tr>
	</tr>
</table>
:::
</dx-tabs>



### 更新日志采集 [](id:new)
您可通过控制台和 yaml 更新日志采集，请参考以下步骤：



<dx-tabs>
::: 通过控制台更新日志采集
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【弹性集群】。
2. 选择需要配置日志采集的集群 ID，进入集群管理页面。
3. 选择左侧【工作负载】，单击需要更新日志采集的工作负载所在行右侧的【更新Pod配置】>【显示高级设置】，修改对应的配置。如下图所示：
![](https://main.qcloudimg.com/raw/a5f93ff2724f199619f998b1b2040be1.png)
4. 单击【完成】即可更新。

:::


::: 通过yaml更新日志采集
找到需要更新日志采集的工作负载对应的 yaml，根据配置对应变量名的变动修改相应的变量值，变量名对应的含义可在 [配置日志采集](#yaml) 查看。
:::
</dx-tabs>

