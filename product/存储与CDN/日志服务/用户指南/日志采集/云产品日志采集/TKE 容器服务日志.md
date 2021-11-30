## 简介
TKE 容器服务用户可以直接在控制台，通过配置日志收集规则进行集群内日志的收集，并将收集到的日志发送至日志服务 CLS 的指定日志主题。基于日志收集功能，使用日志服务平台可进行集群服务日志的实时检索、消费、投递等功能。

## 接入步骤

### 1. 创建日志集和日志主题

登录 [日志服务控制台](https://console.cloud.tencent.com/cls) 新建日志集及日志主题。创建日志主题时，由于容器服务的日志有独立的采集能力，日志主题无需开启【使用 LogListener】。详情请参见  [创建日志集和日志主题](https://cloud.tencent.com/document/product/614/34340)。
![](https://main.qcloudimg.com/raw/89000135b617388b74d09c309acf33c7.png)
>!目前 TKE 容器集群的日志只能投递到同地域的日志服务。



### 2.关联 TKE 容器服务集群

 （1）登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击左侧导航栏【日志采集】。在日志采集页面上方选择地域与集群后，单击【新建】。
（2）新建日志收集规则。
![](https://main.qcloudimg.com/raw/1e5f4a44d4f1df9da059c726fe3b6ccb.png)
规则配置项说明如下：
<table>
   <tr>
      <th>配置项</th>
      <th>详情</th>
   </tr>
   <tr>
      <td>收集规则名称</td>
      <td>最长63个字符，只能包含小写字母、数字及分隔符("-")，且必须以小写字母开头，数字或小写字母结尾<br>配置名称设置后不可修改</td>
   </tr>
   <tr>
      <td>类型</td>
			<td>支持三种采集类型：<a href="#log1">采集容器标准输出日志</a>、<a href="#log2">采集容器内文件日志</a>、<a href="#log3">采集主机内文件日志</a>
   </tr>
   <tr>
      <td>日志源</td>
      <td>可选择采集所有容器日志或指定的容器日志</td>
   </tr>
   <tr>
      <td>消费端</td>
      <td>选择日志服务 CLS</td>
   </tr>
   <tr>
      <td>日志服务实例</td>
      <td>选择日志集和日志主题</td>
   </tr>
</table>

>?TKE 容器服务支持三种采集类型，下面详细介绍这三种采集类型的配置。

<span id="log1"></span>
#### 采集容器标准输出日志

用户可以通过配置将 Kubernetes 集群内指定容器的标准输出日志投递到日志服务 CLS 中，投递的日志内容会附加相关的 Kubernetes metadata，包括容器所属 pod 的 label 和 annotation 等信息。

（1）在新建日志收集规则页面，选择【容器标准输出】采集类型，并配置日志源。
 ![](https://main.qcloudimg.com/raw/5796b7217dfe8ac055c9df6b3e8c81e2.png)
（2）选择容器标准输出采集类型时，会默认为每条日志添加以下 metadata，其中 log 为原始日志信息。且该类型日志源支持一次选择多个 Namespace 的工作负载。

| 字段名                    | 含义                        |
| ------------------------- | --------------------------- |
| docker.container_id       | 日志所属的 container ID     |
| kubernetes.annotations    | 日志所属 pod 的 annotations |
| kubernetes.container_name | 日志所属的 container name   |
| kubernetes.host           | 日志所属 pod 所在的机器 IP  |
| kubernetes.labels         | 日志所属 pod 的 labels      |
| kubernetes.namespace_name | 日志所属 pod 的 namespace   |
| kubernetes.pod_id         | 日志所属 pod 的 ID          |
| kubernetes.pod_name       | 日志所属 pod 的名字         |
| log                       | 原始日志信息                |


<span id="log2"></span>
#### 采集容器内文件日志

用户可以通过配置将集群内指定 pod 内文件的日志投递到日志服务 CLS 中，投递日志格式为 JSON 格式，并会附加相关的 Kubernetes metadata，包括容器所属 pod 的 label 和 annotation 等信息。

>!目前仅支持采集存储在 volume 的日志文件，即需要在工作负载创建时挂载 emptyDir、hostpath 等 volume，并将日志文件存到指定 volume。

（1）指定【容器文件路径】采集类型，并配置日志源。
用户可以通过指定日志文件的路径来采集 pod 上相应路径的日志文件，路径支持文件路径和通配规则，例如`/var/log/nginx.log`或`/var/lib/docker/containers/*/*.log`。
![](https://main.qcloudimg.com/raw/b687319b7962daf2f3d3100da8a0e873.png)
（2）选择容器文件路径采集类型时，会默认为每条日志添加以下 metadata，其中 message 为原始日志信息。且该类型日志源不支持选择多个 Namespace 的工作负载。

| 字段名                    | 含义                        |
| ------------------------- | --------------------------- |
| docker.container_id       | 日志所属的 container ID     |
| kubernetes.annotations    | 日志所属 pod 的 annotations |
| kubernetes.container_name | 日志所属的 container name   |
| kubernetes.host           | 日志所属 pod 所在的机器 IP  |
| kubernetes.labels         | 日志所属 pod 的 labels      |
| kubernetes.namespace_name | 日志所属 pod 的 namespace   |
| kubernetes.pod_id         | 日志所属 pod 的 ID          |
| kubernetes.pod_name       | 日志所属 pod 的名字         |
| file                      | 源日志文件                  |
| message                   | 原始日志信息                |


<span id="log3"></span>
#### 采集主机内文件日志

用户可以通过配置将集群内所有节点的指定主机路径的日志投递到日志服务 CLS，投递日志格式为 JSON 格式，并会附加用户指定的 metadata，包括日志来源文件的路径和用户自定义的 metadata。

（1）在新建日志采集规则页面，指定【节点文件路径】采集类型。
用户可以通过指定日志文件的路径来采集集群内节点上相应路径的日志文件，路径支持文件路径和通配规则，例如 `/var/log/nginx.log`或`/var/lib/docker/containers/*/*.log`。
![](https://main.qcloudimg.com/raw/5637ea176ee4b8d79ac868ce3b56b61a.png)
（2）用户可根据实际需求进行添加自定义的 “metadata” ，将采集到的日志信息附加指定 Key-Value 形式的 “metadata”，作为日志信息的 metadata 标记。
附加 metadata 将会以 json field 的形式添加到日志记录中。
![](https://main.qcloudimg.com/raw/911a62604d4347869985f557e35d6660.png)
例如：
- 当不指定附加 metadata 时，采集到的日志如下图所示：
![](https://main.qcloudimg.com/raw/efcef670013f184cc5b32f21dd9f3e6a.png)
- 当用户指定附加 metadata 时，采集到的日志如下图所示：
![](https://main.qcloudimg.com/raw/4cb172b191581b00e6f7c77eecba9e70.png)

相比不指定附加 Metadata 时，附加 Metadata 的 json 日志增加了 keyservice。
日志 metadata 含义如下表：

| 字段名     | 含义           |
| ---------- | -------------- |
| path       | 日志的来源文件 |
| message    | 日志信息       |
| 自定义 key | 自定义 value   |



### 3.检索 TKE 容器日志

**前提条件**：检索日志前需先开启并配置索引规则，详情请参见  [开启索引](<https://cloud.tencent.com/document/product/614/16981>) 。

（1）登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏单击【日志检索】，进入检索页面。
（2）选择关联容器服务的日志主题，单击【搜索】进行查询。

![](https://main.qcloudimg.com/raw/6ac34f2032a4e7b16eb9d142cd03f342.png)






