## 背景说明
云函数是腾讯云为企业和开发者们提供的无服务器执行环境，具体可参见 [云函数 SCF](https://cloud.tencent.com/product/scf)，下文简称 SCF。

CDW 常见使用场景是将消息中间件的信息同步到 CDW 后再进行分析。本文提供了一种便捷的方法，即使用 SCF 实时的将 Kafka 中的数据导入到 CDW，无需用户维护任何服务。

## 注意事项
- 该云函数目前只能将腾讯云 CKafka 作为数据源，暂不支持自建 Kafka。
- 该云函数目前只能将 CDW 中的某一张表作为目标数据写入，如果有多张表的需求，请按照以下流程每张表创建对应的云函数。

## 使用步骤

###  步骤一：创建函数

在 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=4) 中选择【函数服务】>【新建】，在“新建函数”页面中选择【运行环境】为“Python3.6”，【模糊搜索】中搜索关键词“ckafka”，选择模板函数“CKafka 数据加载到 CDW”，设置完成后单击【下一步】。
![](https://main.qcloudimg.com/raw/6115e15c0f228d08caeea72f59961262.png)
进入“函数配置”页面后，在“高级配置”中进行【环境配置】和【网络配置】，配置如下：
- **环境配置**
 - 内存：根据实际运行情况来设置，默认为128MB。当导入过程中出现内存不足的问题时，需调大内存。
 - 环境变量：
<table>
	<thead>
	<tr>
	<th>参数</th>
	<th>必填</th>
	<th>说明</th>
	</tr>
	</thead>
<tbody>
	<tr>
		<td>DB_DATABASE</td>
		<td>是</td>
		<td>数据库名</td>
	</tr>
	<tr>
		<td>DB_HOST</td>
		<td>是</td>
		<td>如果函数是私有网络，并且和 CDW 是在同一子网，则可以填写 CDW 的内网 IP，否则需要填写外网 IP，并配置白名单</td>
	</tr>
	<tr>
		<td>DB_USER</td>
		<td>是</td>
		<td>用户名</td>
	</tr>
	<tr>
		<td>DB_PASSWORD</td>
		<td>是</td>
		<td>用户密码</td>
	</tr>
	<tr>
		<td>DB_SCHEMA</td>
		<td>是</td>
		<td>模式名，如果创建表的时候未指定，通常是 public</td>
	</tr>
	<tr>
		<td>DB_TABLE</td>
		<td>是</td>
		<td>表名</td>
	</tr>
	<tr>
		<td>DB_PORT</td>
		<td>否</td>
		<td>CDW 端口，默认为5436</td>
	</tr>
	<tr>
		<td>MSG_SEPARATOR</td>
		<td>否</td>
		<td>CKafka 中消费的分隔符，默认为逗号，也就是 csv 格式</td>
	</tr>
</tbody>
</table>
- **网络配置**
 - 私有网络：建议**启用**私有网络，并将 VPC 和子网的值配置的与 CDW 相同。
 ![](https://main.qcloudimg.com/raw/528bf58229140b1e263bd2135d0a59c6.png)
 下图为 CDW 对应的值。
![](https://main.qcloudimg.com/raw/69f95bd32b0a9057f9880dd6bf22e859.png)
 - 公网访问：建议同时**启用**公网访问。

### 步骤二：配置触发器

在 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=4) 的【函数服务】列表中，单击函数列表新建的函数名，进入函数详情页面。选择页面左侧【触发管理】>【创建触发器】创建新触发器。其中【触发方式】需设置为“Ckafka 触发”，如下图所示：
![](https://main.qcloudimg.com/raw/3ad13178a24acf0e9a5cee2d630b3457.png)

关于触发器参数配置可以参考 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)。
