本文将介绍如何在控制台配置自建 K8S 环境的日志采集规则并投递到 [腾讯云日志服务 CLS](https://cloud.tencent.com/product/cls)。
## 使用场景
自建 K8S 日志采集功能是为用户提供的非腾讯云 Kubernetes 集群内的日志采集工具，可以将集群内服务或集群节点特定路径文件的日志发送至 腾讯云日志服务 CLS。日志采集功能适用于需要对  Kubernetes 集群内服务日志进行存储和分析的用户。
日志采集功能需要为每个集群手动开启并配置采集规则。日志采集功能开启后，日志采集 Agent 会在集群内以 DaemonSet 的形式运行，并根据用户通过日志采集规则配置的采集源、CLS 日志主题和日志解析方式，从采集源进行日志采集，将日志内容发送到日志消费端。您可根据以下操作开启日志采集功能。
## 前提条件
- 已开通腾讯云日志服务。
- 在 自建 K8S 集群上安装部署好采集器 LogListener，安装 LogListener 请参考 [自建 K8S 集群安装 LogListener](https://cloud.tencent.com/document/product/614/64566)。
- 配置好相应的日志上报权限，权限配置请参考 [使用自建 K8S 上传数据](https://cloud.tencent.com/document/product/614/68374)。

## 操作步骤
### 创建日志采集规则
### 进入 CLS 控制台配置 自建 K8S 采集规则
#### **步骤**1**：选择日志主题**
- 如果您想选择新的日志主题，可执行如下操作：登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
	1. 在左侧导航栏中，单击**概览**，进入概览页面。
	2. 在其他日志栏下，找到 K8S 自建集群采集，单击**立即接入** 。
	![](https://qcloudimg.tencent-cloud.cn/raw/444335c3abd0216bd271a277db4edaf9.png)
	3. 在创建日志主题页面，根据实际需求，输入日志主题名称，配置日志保存时间等信息，单击**下一步** 。
- 如果您想选择现有的日志主题，可执行如下操作：登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
  1. 在左侧导航栏中，单击**日志主题**，选择需要投递的日志主题，进入日志主题管理页面。
  2. 选择**采集配置**页签，在 **K8S 自建集群采集**配置栏下单击**新增**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/33fede5f1882de6794b3999968400199.png)

#### **步骤** 2 **：机器组配置**
在"机器组管理"页面，勾选需要与当前日志主题进行绑定的机器组，单击**下一步**，即可进入采集配置阶段，更多详情请参阅 [管理机器组](https://cloud.tencent.com/document/product/614/17412)。
![](https://qcloudimg.tencent-cloud.cn/raw/41edf54faada6c693cd7d99e1bfba031.png)
#### **步骤**3**：**自建 K8S 集群采集配置**采集配置**
- 日志源配置  
 1. 采集规则名称：您可以自定义日志收集规则名称。  
 1. 选择采集类型，并配置日志源。
 目前采集类型支持容器标准输出、容器文件路径和节点文件路径。
   - 容器标准输出日志
日志源支持**所有容器**、**指定工作负载**、**指定 Pod Lables** 三种类型。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/60eed298d3cd4ef8bb8556faf50fe592.png)
![](https://qcloudimg.tencent-cloud.cn/raw/fa82aae32f818eb6d1082ed6750c6e3f.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e281138b15c97c2380679e813d18a11f.png)
   - 容器内文件日志 
      - 日志源支持**指定工作负载**、**指定 Pod Lables** 两种类型。
      - 采集文件路径支持文件路径和通配规则，例如当容器文件路径为 `/opt/logs/*.log`，可以指定采集路径为 `/opt/logs`，文件名为 `*.log`。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dce6dca775d49d89de635e175cc3953d.png)
![](https://qcloudimg.tencent-cloud.cn/raw/591e2d927995b0cba95a22ac168fc3db.png)
<dx-alert infotype="notice" title="">
“容器文件路径” <b>不能为软链接</b>，否则会导致软链接的实际路径在采集器的容器内不存在，采集日志失败。
</dx-alert>
   - 节点文件日志
      - 采集路径支持以文件路径和通配规则的方式填写，例如当需要采集所有文件路径形式为 `/opt/logs/service1/*.log`，`/opt/logs/service2/*.log`，可以指定采集路径的文件夹为 `/opt/logs/service*`，文件名为 `*.log`。
![](https://qcloudimg.tencent-cloud.cn/raw/aa11708dd718105178e9976f53191ea4.png)

 1. 元数据配置
除了原始的日志内容， 日志服务还会带上容器或 kubernetes 相关的元数据（例如：产生日志的容器 ID）一起上报到 CLS，方便用户查看日志时追溯来源或根据容器标识、特征（例如：容器名、labels）进行检索。您可以自行选择是否需要上报这些元数据，按需勾选上传。
容器或 kubernetes 相关的元数据请参考下方表格：
<table>
	<tr>
		<th  width=24%>字段名</th> <th width=71%>含义</th>
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

>? 如果想采集部分 podlabel，需要手动输入想要的 label key (可以输入多个，每输入一个以回车结束)，命中的话会采集。
>
-  解析规则配置  
 1. 配置采集策略。您可以选择**全量**或者**增量**。
	- 全量：全量采集指从日志文件的开头开始采集。
	- 增量：增量采集指从距离文件末尾1M处开始采集（若日志文件小于1M，等价于全量采集）。
 2. 编码模式：支持**UTF-8**和**GBK**。
 3.  提取模式：支持多种类型的提取模式，详情如下：
<table>
<thead>
<tr>
<th width="15%">解析模式</th>
<th width="60%">说明</th>
<th width="20%">相关文档</th>
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
- 过滤器：LogListener 仅采集符合过滤器规则的日志，Key 支持完全匹配，过滤规则支持正则匹配，如仅采集 `ErrorCode = 404` 的日志。您可以根据需求开启过滤器并配置规则。
	<dx-alert infotype="explain" title="">
	一个日志主题目前仅支持一个采集配置，请保证选用该日志主题的所有容器的日志都可以接受采用所选的日志解析方式。若在同一日志主题下新建了不同的采集配置，旧的采集配置会被覆盖。
	</dx-alert>  
	
单击**下一步**，完成自建 K8S 集群日志采集规则创建。 
#### **步骤**4**：索引配置**
在索引配置页面，配置如下信息：
- 索引状态：确认是否开启。
- 全文索引：确认是否需要设置大小写敏感。全文分词符：默认为"@&()='",;:\<\>[]{}/ \n\t\r"，确认是否需要修改。
- 是否包含中文：确认是否开启。
- 键值索引：默认关闭，您可根据 key 名按需进行字段类型、分词符以及是否开启统计分析的配置。若您需要开启键值索引，可打开开关。
![](https://qcloudimg.tencent-cloud.cn/raw/e71f7b32e963da0f87de75093287e92f.png)
>!
>- 检索必须开启索引配置，否则无法检索。
>- 索引规则编辑后仅对新写入的日志生效，已有数据不会更新。
