## 操作场景
日志采集功能是容器服务 TKE 为用户提供的集群内日志采集工具，可以将集群内服务或集群节点特定路径文件的日志发送至 [腾讯云日志服务 CLS](https://cloud.tencent.com/product/cls)、[消息队列 CKafka](https://cloud.tencent.com/document/product/597)。日志采集功能适用于需要对 Kubernetes 集群内服务日志进行存储和分析的用户。

日志采集功能需要为每个集群手动开启并配置采集规则。日志采集功能开启后，日志采集 Agent 会在集群内以 DaemonSet 的形式运行，并根据用户通过日志采集规则配置的采集源、CLS 日志主题和日志解析方式，从采集源进行日志采集，将日志内容发送到日志消费端。您可根据以下操作开启日志采集功能：
- [开启日志采集](#open)
- [采集容器标准输出日志](#stout)
- [采集容器文件日志](#insideDocker)
- [采集节点文件日志](#inside)



## 前提条件
- 请在开启前保证集群节点上有足够资源。开启日志采集功能会占用您集群的部分资源。
  - 占用 CPU 资源：0.11 - 1.1核，日志量过大时可根据情况自行调大。
  - 占用内存资源：24 - 560MB，日志量过大时可根据情况自行调大。
  - 日志长度限制：单条512K，如超过会截断。
- 若使用日志采集功能，请确认 Kubernetes 集群内节点能够访问日志消费端。且以下日志采集功能仅支持 Kubernetes 1.10 及以上版本集群。

## 概念

- **日志采集 Agent**：TKE 用于采集日志信息的 Agent，采用 Loglistener，在集群内以 DaemonSet 的方式运行。
- **日志规则**：用户可以使用日志规则指定日志的采集源、日志主题、日志解析方式和配置过滤器。
  - 日志采集 Agent 会监测日志采集规则的变化，变化的规则会在最多10s内生效。
  - 多条日志采集规则不会创建多个 DaemonSet，但过多的日志采集规则会使得日志采集 Agent 占用的资源增加。
- **日志源**：包含指定容器标准输出、容器内文件以及节点文件。
  - 在采集容器标准输出日志时，用户可选择所有容器、或指定工作负载和指定 Pod Labels 内的容器服务日志作为日志的采集源。
  - 在采集容器文件路径日志时，用户可指定工作负载或 Pod Labels 内容器的文件路径日志作为采集源。
  - 在采集节点文件路径日志时，用户可设定日志的采集源为节点文件路径日志。
- **消费端**：用户选择日志服务 CLS 的日志集和日志主题作为消费端。
- **提取模式**：日志采集 Agent 支持将采集到的日志以单行文本、JSON、分隔符、多行文本和完全正则的形式发送至用户指定的日志主题。
- **过滤器**：开启过滤器后可以根据用户指定的规则采集部分日志，key 支持完全匹配，过滤规则支持正则匹配，如仅采集 ErrorCode = 404 的日志。

## 操作步骤
[](id:open)
### 开启日志采集

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**运维功能管理** > **功能管理**。
2. 在“功能管理”页面上方选择地域，单击需要开启日志采集的集群右侧的**设置**。如下图所示：
![](https://main.qcloudimg.com/raw/e71f52765488cfc7ca687d66decda6fc.png)
3. 在“设置功能”页面，单击日志采集**编辑**，开启日志采集后确认。如下图所示：
![](https://main.qcloudimg.com/raw/f87cfe050bae7b41730bef999873d28c.png)

### 配置日志规则

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**运维功能管理** > **日志规则**。
2. 在“日志采集”页面上方选择地域和需要配置日志采集规则的集群，单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/613b3a7d3be13dd04f4290dc4182b1c0.png)
3. 在“新建日志采集规则”页面中，选择采集类型，并配置日志源。目前采集类型支持**容器标准输出**、**容器文件路径**和**节点文件路径**。
<dx-tabs>
::: 采集容器标准输出日志
选择**容器标准输出**采集类型，并根据需求配置日志源。该类型日志源支持一次选择多个 Namespace 的工作负载。如下图所示：
![](https://main.qcloudimg.com/raw/be30d351e22a44945daabc6166480d3f.png)

:::
::: 采集容器内文件日志 
选择**容器文件路径**采集类型，并配置日志源。如下图所示：
![](https://main.qcloudimg.com/raw/887763942bdc76c78f220bdc98d0508d.png)
采集文件路径支持文件路径和通配规则，例如当容器文件路径为 `/opt/logs/*.log`，可以指定采集路径为 `/opt/logs`，文件名为 `*.log`。
<dx-alert infotype="notice" title="">
如果选择采集类型为“容器文件路径”时，对应的“容器文件路径”<b>不能为软链接</b>，否则会导致软链接的实际路径在采集器的容器内不存在，采集日志失败。
</dx-alert>



	

:::
::: 采集节点文件日志
选择**节点文件路径**采集类型，用户可根据实际需求进行添加自定义的 “metadata” ，将采集到的日志信息附加指定 Key-Value 形式的 “metadata”，附加 metadata 将会添加到日志记录中。如下图所示：

>! 一个节点日志文件只能被一个日志主题采集。
>
![](https://main.qcloudimg.com/raw/6cd447c70be92c95c614c9604cd90484.png)
路径支持文件路径和通配规则，例如当需要采集所有文件路径形式为 `/opt/logs/service1/*.log`，`/opt/logs/service2/*.log`，可以指定采集路径的文件夹为 `/opt/logs/service*`，文件名为 `*.log`。
:::
</dx-tabs>
<dx-alert infotype="explain" title="">
对于容器的标准输出及容器内文件（非 hostPath 挂载），除了原始的日志内容， 还会带上容器或 kubernetes 相关的元数据（例如：产生日志的容器 ID）一起上报到 CLS，方便用户查看日志时追溯来源或根据容器标识、特征（例如：容器名、labels）进行检索。
容器或 kubernetes 相关的元数据请参考下方表格：
<table>
	<tr>
		<th>字段名</th> <th>含义</th>
	</tr>
	<tr>
		<td>container_id</td> <td>日志所属的容器 ID。</td>
	</tr>
	<tr>
		<td>container_name</td> <td>日志所属的容器名称。</td>
	</tr>
	<tr>
		<td>image_name</td> <td>日志所属容器的镜像名称 IP。</td>
	</tr>
	<tr>
		<td>namespace</td> <td>日志所属 pod 的 namespace。</td>
	</tr>
	<tr>
		<td>pod_uid</td> <td>日志所属 pod 的 UID。</td>
	</tr>
	<tr>
		<td>pod_name</td> <td>日志所属 pod 的名字。</td>
	</tr>
	<tr>
		<td>pod_lable_{label name}</td> <td>日志所属 pod 的 label（例如一个 pod 带有两个 label：app=nginx，env=prod，
则在上传的日志会附带两个 metedata：pod_label_app:nginx，pod_label_env:prod）。
</td>
	</tr>
</table>

</dx-alert>

4. 配置日志服务消费端。
<dx-tabs>
::: 配置日志消费端为 CLS
选择日志集和相应的日志主题，可以选择新建和已有日志主题。如下图所示：
![](https://main.qcloudimg.com/raw/509611a957414671931b226a1b005b63.png)
>!
>- 日志服务 CLS 目前只能支持同地域的容器集群进行日志采集上报。
>- 若日志主题下已存在500个日志主题，则不能新建日志主题。
>
:::
::: 配置日志消费端为 CKafka
支持用户选择写入 CKafka 或用户自建 Kafka ，当选择 CKafka 时，需要填写实例 ID 和实例 Topic ；当选择自建 Kafka 时，需按要求填写 Broker 地址和 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/db8dca5860ed168e47fcaf63046a2a65.png)
>!
>- 如果 Kafka 实例与节点不在同一个 VPC 下，会提示创建 Kafka 实例接入点后再进行日志投递。
>- 在集群的 daemonSet 资源中，选择 kube-system 命名空间，找到 tke-log-agent pod 下的 kafkalistener 容器，可以查询 kafka 采集器的日志。
>

支持在高级设置内通过指定 Key 值将日志投递到指定分区，该功能默认不开启，日志随机投放，当开启后，带有同样 Key 值的日志，将投递到相同的分区。支持输入 TimestampKey（默认@timestamp）和指定时间戳格式。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4d2bb5f6d5b94f3741e39858a88346f8.png)

:::
</dx-tabs>

5. 单击**下一步**，选择日志提取模式。如下图所示：
>! 
> - 一个日志主题目前仅支持一个采集配置，请保证选用该日志主题的所有容器的日志都可以接受采用所选的日志解析方式。若在同一日志主题下新建了不同的采集配置，旧的采集配置会被覆盖。
> - 当前仅投递到 CLS 支持配置日志解析方式。
>
![](https://main.qcloudimg.com/raw/b15c556730c7abc404a5127baaf4caf4.png)
<table>
<thead>
<tr>
<th>解析模式</th>
<th>说明</th>
<th>相关文档</th>
</tr>
</thead>
<tbody><tr>
<td>单行全文</td>
<td>一条日志仅包含一行的内容，以换行符 \n 作为一条日志的结束标记，每条日志将被解析为键值为 <strong>CONTENT</strong> 的一行完全字符串，开启索引后可通过全文检索搜索日志内容。日志时间以采集时间为准。</td>
<td><a href="https://cloud.tencent.com/document/product/614/17421">单行全文格式</a></td>
</tr>
<tr>
<td>多行全文</td>
<td>指一条完整的日志跨占多行，采用首行正则的方式进行匹配，当某行日志匹配上预先设置的正则表达式，就认为是一条日志的开头，而下一个行首出现作为该条日志的结束标识符，也会设置一个默认的键值 <strong>CONTENT</strong>，日志时间以采集时间为准。支持自动生成正则表达式。</td>
<td><a href="https://cloud.tencent.com/document/product/614/17422">多行全文格式</a></td>
</tr>
<tr>
<td>单行 - 完全正则</td>
<td>指将一条完整日志按正则方式提取多个 key-value 的日志解析模式，您需先输入日志样例，其次输入自定义正则表达式，系统将根据正则表达式里的捕获组提取对应的 key-value。支持自动生成正则表达式。</td>
<td><a href="https://cloud.tencent.com/document/product/614/32817">单行 - 完全正则格式</a></td>
</tr>
<tr>
<td>多行 - 完全正则</td>
<td>适用于日志文本中一条完整的日志数据跨占多行（例如 Java 程序日志），可按正则表达式提取为多个 key-value 键值的日志解析模式，您需先输入日志样例，其次输入自定义正则表达式，系统将根据正则表达式里的捕获组提取对应的 key-value。支持自动生成正则表达式。</td>
<td><a href="https://cloud.tencent.com/document/product/614/52366">多行-完全正则格式</a></td>
</tr>
<tr>
<td>JSON</td>
<td>JSON 格式日志会自动提取首层的 key 作为对应字段名，首层的 value 作为对应的字段值，以该方式将整条日志进行结构化处理，每条完整的日志以换行符 \n 为结束标识符。</td>
<td><a href="https://cloud.tencent.com/document/product/614/17419">JSON 格式</a></td>
</tr>
<tr>
<td>分隔符</td>
<td>指一条日志数据可以根据指定的分隔符将整条日志进行结构化处理，每条完整的日志以换行符 \n 为结束标识符。日志服务在进行分隔符格式日志处理时，您需要为每个分开的字段定义唯一的 key，无效字段即无需采集的字段可填空，不支持所有字段均为空。</td>
<td><a href="https://cloud.tencent.com/document/product/614/17420">分隔符格式</a></td>
</tr>
</tbody></table>

6. 根据需求开启过滤器并配置规则，并单击**完成**，完成创建。如下图所示：
![](https://main.qcloudimg.com/raw/221a78291098e8b403aa89244332ebb1.png)


### 更新日志规则
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**运维功能管理** > **日志规则**。
2. 在“日志采集”页面上方选择地域和需要更新日志采集规则的集群，单击右侧的**编辑收集规则**。如下图所示：
![](https://main.qcloudimg.com/raw/aa25a298fe368695f536818197a6dfe7.png)
3. 根据需求更新相应配置，单击**完成**，完成更新。
>! 日志集和日志主题不可更新。
