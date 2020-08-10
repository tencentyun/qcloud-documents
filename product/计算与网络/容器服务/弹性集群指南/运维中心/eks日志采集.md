## 操作场景
本文介绍如何使用弹性容器服务（EKS）提供的集群内日志采集功能。

EKS 日志采集功能可以将集群内服务的日志发送至 Kafka 或者 [腾讯云日志服务（CLS）](https://cloud.tencent.com/product/cls)，适用于需要对 EKS 集群内服务日志进行存储和分析的用户。

EKS 日志采集功能需要在创建工作负载时为每个弹性集群手动开启。您可根据以下操作开启日志采集功能：
  - [配置日志采集](#output)
  - [配置日志消费端](#output2)
  - [通过 yaml 配置日志采集](#yaml)
  - [更新日志采集](#new)

开启后，日志采集 Agent 根据您配置的采集路径和消费端，将采集到的日志以 JSON 的形式发送到您指定的消费端。
  - **消费端**：日志采集服务支持 Kafka 或 CLS 作为日志的消费端。
  - **采集路径**：需要采集的指定容器日志的路径。采集路径支持采集标准输出（stdout）和绝对路径，支持*通配。多个采集路径以“,”分隔。 

## 前提条件

- 需确认 Kubernetes 集群内节点能够访问日志消费端。
- 日志长度限制为单条512K，如果超过则会截断。


## 操作步骤

<span id="output"></span>
### 配置日志采集 
EKS 日志采集功能支持采集 Kubernetes 集群内指定容器的标准输出日志，您可以根据自己的需求，灵活配置采集规则。
采集到的日志信息将会以 JSON 格式输出到您指定的消费端，并会附加相关的 Kubernetes metadata，包括容器所属 pod 的 label 和 annotation 等信息。
#### 配置方法
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【弹性集群】。
2. 进入“弹性集群”页面，选择需要日志采集的集群 ID，进入集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/03630ec2d809e0de61ece19cf3eb63a9.png)
3. 在左侧“工作负载”中选择需要的工作负载类型，选择【新建】。
4. 在“实例内容器”中点击【显示高级设置】，并【开启】日志采集。如下图所示：
![](https://main.qcloudimg.com/raw/0ef3ce835e4d30651a48f54df9b23acb.png)
5. 配置日志消费端，推荐以 [日志服务（CLS）](https://cloud.tencent.com/product/cls) 为消费端，并选择日志集和日志主题。若无合适的日志集，请参考 [配置日志服务 CLS 作为日志消费端](#step1) 完成日志集的创建。
   若选择 Kfaka 为消费端，请参考 [配置 Kafka 作为日志消费端](#step2)。
![](https://main.qcloudimg.com/raw/bd701d18315e8ca09c91adb5c1994081.png)
6. 选择 SecretId 和 SecretKey 进行日志采集授权。
    第一列：选择您以 [API 密钥](https://console.cloud.tencent.com/cam/capi) 中 SecretId 和 SecretKey 作为变量值进行创建的集群配置 Secret 名称。
    第二列：选择“Secret”相应的变量名。
	![](https://main.qcloudimg.com/raw/d03939b8078bc2c789c17ff17a689bac.png)
>! 
 - API 密钥对应的用户必须允许日志服务（CLS）。
 - 若无 API 密钥，需新建 API 密钥。详情请参见 [访问密钥](https://cloud.tencent.com/document/product/598/40487)。
 - 若无合适的 secret，需新建 secret。详情请参见 [Secret 管理](https://cloud.tencent.com/document/product/457/31718)。
>
7. 配置采集路径。例如 `/var/log/nginx.log` 或 `/var/lib/docker/containers//.log`。如下图所示：
![](https://main.qcloudimg.com/raw/7b9799a0d2a6d1200318dfc35243ea52.png)
8. 完成以上步骤后，日志采集功能配置完成，可继续工作负载的其他配置。

<span id="output2"></span>
### 配置日志消费端 
EKS 日志采集功能支持指定用户自建的 Kafka 实例、日志服务 CLS 指定的日志主题作为日志内容的消费端。日志采集 Agent 会将采集到的日志发送到指定 Kafka 的指定 Topic 或指定的 CLS 日志主题。
#### 配置 Kafka 作为日志消费端 <span id="step2"></span> 
选择 Kafka 作为日志采集的消费端，填写 Kafka 的 Broker 地址及 Topic，需要保证集群内所有资源都能够访问用户指定的 Kafka Topic。如下图所示：
![](https://main.qcloudimg.com/raw/2a226f61d5db3a048f804e83d3f0debb.png)
#### 配置 CLS 作为日志消费端<span id="step1"></span> 
>!日志服务 CLS 目前只能支持同地域的容器集群进行日志采集上报。详情请参见 [创建日志集和日志主题](https://cloud.tencent.com/document/product/614/34340)。
>
创建日志集时，由于弹性容器服务的日志有独立的采集能力，新建日志集不需要开启【使用LogListener】。如下图所示：
![](https://main.qcloudimg.com/raw/7444cb3e96707452a021188c9a3d83e2.png)
打开日志主题的【日志索引】。如下图所示：
![](https://main.qcloudimg.com/raw/a8413fb410367e01acfa9ff62e7a291d.png)
<span id="yaml"></span>

### 通过 yaml 配置日志采集 
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【弹性集群】。
2. 进入“弹性集群”页面，选择需要日志采集的集群 ID，进入集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/03630ec2d809e0de61ece19cf3eb63a9.png)
3. 在左侧“工作负载”中选择需要的工作负载类型，选择【更多】>【编辑YAML】，进入编辑 YAML页面。或者直接点击【YAML创建资源】。
例如，选择【工作负载】 >【Deployment】>【更多】>【编辑YAML】。如下图所示：
![](https://main.qcloudimg.com/raw/aecacfad7deea5b77522584fcf4ba4f2.png)
4. 在 “更新Deployment” 页面，编辑 YAML，通过新增环境变量的方式配置。有以下三种方式，

#### 方式1：采集日志到 Kafka
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
		<td>EKS_LOGS_OUTPUT_TYPE</td> <td>消费端支持 kafka 和 cls，根据这个 key 判断是否启用日志收集。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOG_PATHS</td> <td>日志路径，支持“stdout”（表示采集标准输出）和绝对路径，支持*通配，多个路径用“,”分隔。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_METADATA_ON</td> <td>支持 true 或 false。可不写，不写默认为 true。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_KAFKA_TOPIC</td> <td>日志主题。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_KAFKA_BROKERS</td> <td>kafka brokers，ip1:port1，ip1:port2，ip2:port2格式，多个用“,”分隔。对外用此环境变量，EKS_LOGS_KAFKA_HOST 以后不再对外可见。</td>
	</tr>

</table>

#### 方式2：通过 secret 采集日志到 cls  
##### 创建 secret
通过 kubectl 执行以下命令，获取进行 base64编码的 secretid 和 secretkey，详情请参考 [secret 管理](https://cloud.tencent.com/document/product/457/31718)。请替换为对应的 secretid 和 secretkey。
```shell
$ echo -n 'secretid' | base64
c2VjcmV0aWQ=
$ echo -n 'secretkey' | base64
c2VjcmV0a2V5
```
通过 yaml 创建 secret，此处的 secretid 和 secretkey 和上面的 secretid 和 secretkey 保持一致。请替换为对应的 secretid 和 secretkey。
```shell
apiVersion: v1
kind: Secret
metadata:
  name: secretidkey
data:
  secretid: c2VjcmV0aWQ=
  secretkey: c2VjcmV0a2V5
```
##### 创建deployment
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
		<td>EKS_LOGS_OUTPUT_TYPE</td> <td>消费端支持 kafka 和cls，根据这个 key 判断是否启用日志收集。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOG_PATHS</td> <td>日志路径，支持“stdout”（表示采集标准输出）和绝对路径，支持*通配，多个路径用“,”分隔。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_METADATA_ON</td> <td>支持 true 或 false。可不写，不写默认为 true。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOGSET_NAME</td> <td>cls 日志集名称。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_TOPIC_ID</td> <td>cls 日志集的主题 id。</td>
	</tr>
	</tr>
	<td>EKS_LOGS_SECRET_ID</td> <td>SecretId。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_SECRET_KEY</td> <td>SecretKey。</td>
	</tr>
	</tr>
</table>

#### 方式3：通过 role 采集日志到 cls
##### 创建 role
在 [访问管理控制台](https://console.cloud.tencent.com/cam/role) 创建 role，创建 role 时选择腾讯云产品服务，绑定云服务器 CVM 载体，详情请参考 [创建角色](https://cloud.tencent.com/document/product/598/19381)。
如果需要日志采集，请在【策略】>【新建自定义策略】>【按策略语法创建】中添加如下策略，并将此策略关联到上述新建角色，详情请参考 [创建策略](https://cloud.tencent.com/document/product/598/37739)。
```shell
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cls:pushLog"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```
pod template 中新增 annotation，指定 role 的名称，获取该 role 包含的权限策略。
```shell
template:
  metadata:
    annotations:
      eks.tke.cloud.tencent.com/role-name: "eks-pushlog"
```
##### 创建deployment
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
		<td>EKS_LOGS_OUTPUT_TYPE</td> <td>消费端支持 kafka 和 cls，根据这个 key 判断是否启用日志收集。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOG_PATHS</td> <td>日志路径，支持“stdout”（表示采集标准输出）和绝对路径，支持*通配，多个路径用“,”分隔。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_METADATA_ON</td> <td>支持 true 或 false。可不写，不写默认为 true。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_LOGSET_NAME</td> <td>cls 日志集名称。</td>
	</tr>
	<tr>
		<td>EKS_LOGS_TOPIC_ID</td> <td>cls 日志集的主题 id。</td>
	</tr>
	</tr>
</table>
5. 添加完成后，单击【完成】，即可更新 YAML，增加日志配置。
<span id="new"></span>

### 更新日志采集 
您可通过控制台和 yaml 更新日志采集，请参考以下步骤：
#### 通过控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【弹性集群】。
2. 选择需要配置日志采集的集群 ID，进入集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/7804c43acd5314be619f59c9a819b73a.png)
3. 点击左侧【工作负载】，在需要更新日志采集的工作负载中，单击【更新Pod配置】。如下图所示：
![](https://main.qcloudimg.com/raw/9c5291c32f9f3c1f995c7ddde069a260.png)
4. 在环境变量中，根据配置对应变量名的变动修改相应的变量值，变量名对应的含义可在上一小节查看。如下图所示：
![](https://main.qcloudimg.com/raw/d20ebcca7992a47edd1f2317be9b0b26.png)
5. 修改完成之后，点击【完成】即可。

#### 通过 yaml 
找到需要更新日志采集的工作负载对应的 yaml，根据配置对应变量名的变动修改相应的变量值，变量名对应的含义可在上一小节查看。
