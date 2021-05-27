

## 操作场景
在弹性容器服务 EKS 中，用户可以 [通过环境变量配置日志采集](https://cloud.tencent.com/document/product/457/47200)，按行采集日志、不解析。也可以通过自定义资源定义（CustomResourceDefinitions，CRD）的方式配置日志采集。

CRD 对 Pod 无侵入性，支持单行、多行、分隔符、完全正则、JSON 等多种日志解析方式，将标准输出、容器内文件日志发送至 [腾讯云日志服务 CLS](https://cloud.tencent.com/product/cls)，提供检索分析、可视化应用、日志下载消费等服务。推荐使用 CRD 配置日志采集。

使用 CRD 配置日志采集功能需要为每个集群手动开启并配置采集规则，采集器将根据日志采集规则配置的采集源、CLS 日志主题及日志解析方式，从采集源进行日志采集，将日志内容发送到 CLS 并存储。您可根据以下操作使用 CRD 配置 EKS 集群的日志采集功能：
<dx-steps>
-[首次授权](#role)
-[开启日志采集](#open)
-[配置日志规则](#rules)
-[配置消费端](#cls)
-[配置日志提取模式](#index)
</dx-steps>

#### 注意事项
- 使用 CRD 配置日志采集目前只对2021年5月25号后新建的 Pod 生效，若需为旧 Pod 配置日志采集，请销毁重建。
- 若采集的 Pod 同时配置环境变量及 CRD 采集日志，会造成重复采集、重复计费。故使用 CRD 配置日志采集时，请删除相关环境变量。


## 概念

- **日志规则**：用户可以使用日志规则指定日志的采集源、消费端、日志解析方式、配置过滤器及上传解析失败等能力。日志采集器会监测日志采集规则的变化，变化的规则会在最多10s内生效。
- **日志源**：包含指定容器标准输出及容器内文件。
  - 在采集容器标准输出日志时，用户可选择所有容器、或指定工作负载和指定 Pod Labels 内的容器服务日志作为日志的采集源。
  - 在采集容器文件路径日志时，用户可指定工作负载或 Pod Labels 内容器的文件路径日志作为采集源。
- **消费端**：用户选择日志服务 CLS 的日志集和日志主题作为消费端。
- **提取模式**：日志采集 Agent 支持将采集到的日志以单行文本、JSON、分隔符、多行文本和完全正则的形式发送至用户指定的日志主题。
- **过滤器**：开启过滤器后可以根据用户指定的规则采集部分日志，key 支持完全匹配，过滤规则支持正则匹配，例如仅采集 ErrorCode = 404 的日志。
- **上传解析失败**：开启后，所有解析失败的日志，均以作为键名称（Key），原始日志内容作为值（Value）进行上传。关闭时会丢弃失败的日志。

## 操作步骤



### 首次授权[](id:role)
首次使用 EKS 集群的日志采集功能，需要您对 CLS 等相关权限进行授权，以保证将日志正常上传到 CLS。
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=4)，选择左侧导航栏中的【集群运维】>【[功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=1)】。
2. 在“功能管理”页面上方选择地域和弹性集群，单击需要开启日志采集的集群右侧的【设置】。如下图所示：
![](https://main.qcloudimg.com/raw/4a625f7cda4ca608159c3c4e0f15cbd1.png)
3. 在“设置功能”页面，单击【访问管理】，为服务授权。如下图所示：
![](https://main.qcloudimg.com/raw/8c3f6748b1d87090b63cc861fe373537.png)
完成授权后，会默认为您的账号绑定角色 TKE_QCSLinkedRoleInEKSLog，该角色配置的预设策略为 QcloudAccessForTKELinkedRoleInEKSLog。

>?您只需在首次使用日志采集功能时进行授权，后续使用无需再操作。若您删除了以上角色，则会再次触发授权操作。



### 开启日志采集[](id:open)

完成授权后，即可开启日志采集。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=4)，选择左侧导航栏中的【集群运维】>【[功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=1)】。
2. 在“功能管理”页面上方选择地域和弹性集群，单击需要开启日志采集的集群右侧的【设置】。如下图所示：
![](https://main.qcloudimg.com/raw/4a625f7cda4ca608159c3c4e0f15cbd1.png)
3. 在“设置功能”页面，单击日志采集【编辑】，开启日志采集后确认。如下图所示：
![](https://main.qcloudimg.com/raw/88454cdd6de6339f0ed64f7f7eb18a16.png)




### 配置日志规则[](id:rules)

开启日志采集后，需要配置日志规则，确认日志源、消费端、日志解析方式等。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=4)，选择左侧导航栏中的【集群运维】>【[日志规则](https://console.cloud.tencent.com/tke2/ops/list?rid=1)】。
2. 在“日志采集”页面上方选择地域和需要配置日志采集规则的 EKS 集群，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/307070e947388d07be7b8e84a5514b54.png)
3. 在“新建日志采集规则”页面中，选择采集类型，并配置日志源、消费端、日志解析方式。目前采集类型支持 [容器标准输出](#stout) 和 [容器文件路径](#insideDocker)。
<dx-tabs>
::: 采集容器标准输出日志[](id:stout)
选择【容器标准输出】采集类型，并根据自身需求，配置日志源。如下图所示：
![](https://main.qcloudimg.com/raw/984aacd9e22c15e680ac4db195ea1f58.png)
该类型日志源支持采集：
- **所有容器**：所有 Namespace 或某个 Namespace 下的所有容器。
- **指定工作负载**：某 Namespace 下，指定工作负载下的某些容器，并支持添加多个 Namespace。
- **指定 Pod Labels**：某 Namespace 下，指定多个 Pod Labels，采集符合该 Lables 的所有容器。

:::
::: 采集容器内文件日志[](id:insideDocker) 
选择【容器文件路径】采集类型，并根据自身需求，配置日志源。如下图所示：
![](https://main.qcloudimg.com/raw/c0f209f865f75e99b9009f3cd8d610e5.png)
该类型日志源支持采集：
- **指定工作负载**：某 Namespace 下，指定工作负载下的容器的指定文件路径。
- **指定 Pod Labels**：某 Namespace 下，指定多个 Pod Labels，采集符合该 Labels 的所有容器的指定文件路径。

采集文件路径支持文件路径和通配规则，例如当容器文件路径为 `/opt/logs/*.log`，可以指定采集路径为 `/opt/logs`，文件名为 `*.log`。

:::
</dx-tabs>
<dx-alert infotype="explain" title="">
对于容器的标准输出及容器内文件，除了原始的日志内容，还会带上容器或 kubernetes 相关的元数据（例如，产生日志的 Pod name）一起上报到 CLS，方便用户查看日志时追溯来源或根据容器标识、特征（例如，容器名、Labels）进行检索。
容器或 kubernetes 相关的元数据请参考下方表格：
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
		<td>pod_ip</td> <td>日志所属 pod 的IP。</td>
	</tr>
	<tr>
		<td>pod_lable_{label name}</td> <td>日志所属 pod 的 label（例如一个 pod 带有两个 label：app=nginx，env=prod，
则在上传的日志会附带两个 metedata：pod_label_app:nginx，pod_label_env:prod）。
</td>
	</tr>
</table>
</dx-alert>
4. [](id:cls)配置日志服务 CLS 为消费端。选择日志集和相应的日志主题，建议选择自动新建日志主题。如下图所示：
![](https://main.qcloudimg.com/raw/509611a957414671931b226a1b005b63.png)
<dx-alert infotype="notice" title="">
- 日志服务 CLS 目前只能支持同地域的容器集群进行日志采集上报。
- 日志集和日志主题在日志规则完成后不可更新。
</dx-alert>
5. [](id:index)单击【下一步】，选择日志提取模式。如下图所示：
![](https://main.qcloudimg.com/raw/0be038e165d1823f7fdfedc32ef054e4.png)
<dx-fold-block title="<b>多类提取模式说明</b>">
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
<td>指一条完整的日志跨占多行，采用首行正则的方式进行匹配，当某行日志匹配上预先设置的正则表达式，就认为是一条日志的开头，而下一个行首出现作为该条日志的结束标识符，也会设置一个默认的键值 <strong>CONTENT</strong>，日志时间以采集时间为准。支持 <a href="#auto">自动生成正则表达式</a>。</td>
<td><a href="https://cloud.tencent.com/document/product/614/17422">多行全文格式</a></td>
</tr>
<tr>
<td>单行 - 完全正则</td>
<td>指将一条完整日志按正则方式提取多个 key-value 的日志解析模式，您需先输入日志样例，其次输入自定义正则表达式，系统将根据正则表达式里的捕获组提取对应的 key-value。支持 <a href="#auto">自动生成正则表达式</a>。</td>
<td><a href="https://cloud.tencent.com/document/product/614/32817">单行 - 完全正则格式</a></td>
</tr>
<tr>
<td>多行 - 完全正则</td>
<td>适用于日志文本中一条完整的日志数据跨占多行（例如 Java 程序日志），可按正则表达式提取为多个 key-value 键值的日志解析模式，您需先输入日志样例，其次输入自定义正则表达式，系统将根据正则表达式里的捕获组提取对应的 key-value。支持 <a href="#auto">自动生成正则表达式</a>。</td>
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
</dx-fold-block>
<dx-fold-block title="<b>正则表达式自动生成说明</b>">
[](id:auto)为方便您的使用，在选择**多行 - 完全正则**、**单行 - 完全正则**、**多行全文**的提取模式时，支持**根据日志样例自动生成正则表达式**。
以**单行 - 完全正则**为例，使用步骤如下：
![](https://main.qcloudimg.com/raw/a6818396ad433e6c4b295bd265153d7b.png)
1. 单击【正则表达式自动生成】。
2. 在“正则表达式自动生成”弹窗中，选中日志样例中需要提取的字段，填写 key 值。
3. 单击【确认提取】，即可生成该字段对应的正则表达式，并自动填写提取结果。重复此操作，直至日志完全被提取完成。
</dx-fold-block>
<dx-alert infotype="notice" title=""> 
一个日志主题目前仅支持一个采集配置，请保证选用该日志主题的所有容器的日志都可以接受采用所选的日志解析方式。若在同一日志主题下新建了不同的采集配置，旧的采集配置会被覆盖。
</dx-alert>
6. 根据自身需求开启其他功能。
	- 开启过滤器，并配置规则。
	开启后，仅采集符合过滤器规则的日志，Key 支持完全匹配，过滤规则支持正则匹配，如仅采集 ErrorCode = 404 的日志；
	- 开启上传解析失败日志。
	开启后，所有解析失败的日志，均以作为键名称（Key），原始日志内容作为值（Value）进行上传。关闭时会丢弃失败的日志。
7. 单击【完成】，完成创建。


### 更新日志规则

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=4)，选择左侧导航栏中的【集群运维】>【[日志规则](https://console.cloud.tencent.com/tke2/ops/list?rid=1)】。
2. 在“日志规则”页面中，选择需要更新的日志规则，单击右侧的【编辑收集规则】。如下图所示：
   ![](https://main.qcloudimg.com/raw/bfac9108c4725bef36c4df1a65d800e7.png)
3. 根据需求更新相应配置，单击【完成】，完成更新。



## 常见问题
如遇问题，您可先查询 [弹性集群日志采集相关问题](https://cloud.tencent.com/document/product/457/54778)。如果您的问题仍未解决，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1TKE&step=1) 联系我们。
