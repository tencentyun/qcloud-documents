本文将为您介绍如何通过 <dx-tag-link link="https://cloud.tencent.com/document/product/248/51287" tag="API">创建告警策略接口</dx-tag-link> 和 <dx-tag-link link="https://cloud.tencent.com/document/product/248/40421" tag="API">绑定策略对象</dx-tag-link> 创建告警策略并绑定告警对象。







## 准备工作[](id:preparationsteps)

在调用创建 <dx-tag-link link="https://cloud.tencent.com/document/product/248/51287" tag="API">创建告警策略接口</dx-tag-link> 前需要准备以下入参资料。



<dx-tabs>
::: 准备个人密钥
 1. 登录访问管理控制台 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面。
 2. 单击**显示**即可获取 SecretKey。
 ![](https://main.qcloudimg.com/raw/6ba975475ddd17f82bca8100eb2efb19.png)

> ?如未创建密钥，请单击**新建密钥**创建密钥。
 :::
 ::: 准备告警策略类型
 通过 <dx-tag-link link="https://cloud.tencent.com/document/product/248/48683" tag="API">查询所有名字空间</dx-tag-link> 可以查询到所有策略类型。步骤如下：
1. 进入 [API Explorer 在线调用控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=DescribeAllNamespaces)，参考下表填写输入参数。
<table>
	<tr>
	<th>参数名称</th>
	<th>说明</th>
	</tr>
	<tr>
		<td>SecretId、SecretKey</td>
		<td>填写准备好的 SecretId、SecretKey</td>
	</tr>
	<tr>
		<td>Region</td>
		<td>选择对应的地域</td>
	</tr>
	<tr>
		<td>SceneType</td>
		<td>填写：ST_ALARM</td>
	</tr>
	<tr>
		<td>Module</td>
		<td>填写：monitor</td>
	</tr>
	<tr>
		<td>MonitorTypes.N </td>
		<td>非必填，无需填写</td>
	</tr>
</table>
3. 单击**在线调用** > **发送请求**，获取响应结果。返回结果中 Response.QceNamespacesNew.N.Id 即创建告警策略需要的 Namespace。如下图为查看云服务器告警策略类型：
![](https://main.qcloudimg.com/raw/19edabd3808c034c318845ae835ebc7f.png)
<dx-alert infotype="notice" title="">
此处 Namespace 为告警策略类型，与拉取监控数据时的云产品 Namespace 不同。
</dx-alert>
:::
::: 准备指标列表
通过 <dx-tag-link link="https://cloud.tencent.com/document/product/248/51283" tag="API">查询告警指标列表</dx-tag-link> 可以查询到策略类型下的所有告警指标。

1. 进入 [API Explorer 在线调用控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=DescribeAlarmMetrics)，参考下表填写输入参数。
<table>
	<tr>
	<th>参数名称</th>
	<th>说明</th>
	</tr>
	<tr>
		<td>SecretId、SecretKey</td>
		<td>填写准备好的 SecretId、SecretKey</td>
	</tr>
	<tr>
		<td>Region</td>
		<td>选择对应的地域</td>
	</tr>
	<tr>
		<td>Module</td>
		<td>填写：monitor</td>
	</tr>
		<tr>
		<td>MonitorType</td>
		<td>填写：MT_QCE</td>
	</tr>
	<tr>
		<td>Namespace</td>
		<td>填写“准备告警策略类型”步骤获取的告警策略类型，即返回结果中的 Response.QceNamespacesNew.N.Id</td>
	</tr>
</table>
2. 单击右侧**在线调用** > **发送请求**，获取响应结果。返回结果中 Response.Metrics.N 即该策略类型下的所有告警指标。如下图为获取云服务器指标列表：
 ![](https://main.qcloudimg.com/raw/da93d3e304a016a3ce7c7e4081835426.png)
:::
::: 准备事件列表
通过 <dx-tag-link link="https://cloud.tencent.com/document/product/248/51284" tag="API">查询告警事件列表</dx-tag-link> 可以查询到策略类型下的所有告警指标。

1. 进入 [API Explorer 在线调用控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=DescribeAlarmEvents&SignVersion=)，参考下表填写输入参数。
<table>
	<tr>
	<th>参数名称</th>
	<th>说明</th>
	</tr>
	<tr>
		<td>SecretId、SecretKey</td>
		<td>填写准备好的 SecretId、SecretKey</td>
	</tr>
	<tr>
		<td>Region</td>
		<td>选择对应的地域</td>
	</tr>
	<tr>
		<td>Module</td>
		<td>填写：monitor</td>
	</tr>
	<tr>
		<td>Namespace</td>
		<td>填写“准备告警策略类型”步骤获取的告警策略类型，即返回结果中的 Response.QceNamespacesNew.N.Id</td>
	</tr>
</table>
2. 单击**在线调用** > **发送请求**，获取响应结果。返回结果 Response.Events.N.EventName 即告警策略需要的 EventName。
  ![](https://main.qcloudimg.com/raw/de44fb8113250229bfbf5d7985b381da.png)
   :::
</dx-tabs>


## 实践步骤

本文提供以下示例，为您介绍如何使用  <dx-tag-link link="https://cloud.tencent.com/document/product/248/51287" tag="API">创建告警策略接口</dx-tag-link>等接口创建云服务器-基础监控告警策略。

### 创建告警策略[](id:createalarm)

1. 登录[ API Explorer 在线调试控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=CreateAlarmPolicy&SignVersion=)。
2. 将 [准备好的个人密钥](#preparationsteps) 对应复制到对应的 SecretId、SecretKey 文本框。
3. 在**输入参数**配置项找到 Region，选择相关地域。
4. 在 Module 中填写“monitor”，PolicyName 中填写策略名称（策略名称由您自定义），MonitorType 中填写“MT_QCE”。
5. 在 Namespace 中填写上述 [准备告警策略类型](#preparationsteps) 步骤中获取的告警策略类型。例如，云服务器-基础监控告警策略类型为 cvm_device。
6. 在云服务器-基础监控场景下 Remark、Enable 为选填，ProjectId 为必填。
	- **Remark**：备注，可不填。
	- **Enable**：是否启用告警策略。0=停用，1=启用。可不传，默认为1。
	- **ProjectId**：项目 Id。云服务器-基础监控需填写**0** 。
> ? ProjectId 项目 Id，-1=无项目，0=默认项目，根据策略类型而定可不传，默认为-1。例如部分告警策略类型下无项目概念（例如私有网络），可使用默认传参-1 。若该告警策略类型有项目概念（例如云服务器-基础监控），默认传参-1会报错，入参需要修改为0。
7. Condition 配置说明如下：
<table>
<thead>
<tr>
<th>参数名称</th>
<th>是否必填</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>IsUnionRule</td>
<td>是</td>
<td>指标触发与或条件，0=或，1=与，或表示触发任一条件时发送告警，与为触发所有条件后发送告警</td>
</tr>
<tr>
<td>Rules.N</td>
<td>是</td>
<td>告警触发条件列表。可参考在线调用 AlarmPolicyRule 参数说明进行配置<ul><li> <strong>MetricName</strong>：填写 <a href="#preparationsteps">准备指标列表</a> 步骤返回中的 MetricName（Metrics.N.MetricName）</li><li><strong>Period</strong>：填写 <a href="#preparationsteps">准备指标列表</a> 步骤返回中的 Period（Metrics.N.MetricConfig.Period）</li><li><strong>Operator</strong>：填写 <a href="#preparationsteps">准备指标列表</a> 步骤返回中的 Operator（Metrics.N.MetricConfig.Operator）</li><li><strong>Value</strong>：填写阈值，不需要填写单位，例如80</li><li><strong>ContinuePeriod</strong>：填写 <a href="#preparationsteps">准备指标列表</a> 步骤返回中的 ContinuePeriod（Metrics.N.MetricConfig.ContinuePeriod）</li><li><strong>NoticeFrequency</strong>：告警频率（按秒计算）。参数说明：告警间隔，0=不重复 ；300=每5分钟告警一次； 600=每10分钟告警一次 ；900=每15分钟告警一次 1800=每30分钟告警一次；3600=每1小时告警一次； 7200=每2小时告警一次 ；10800=每3小时告警一次； 21600=每6小时告警一次； 43200=每12小时告警一次 ；86400=每1天告警一次</li><li><strong>IsPowerNotice</strong>：告警频率是否指数增长，0=否，1=是</li><li>其他参数无需填写</li></ul></td>
</tr>
</tbody></table>
8. 如需触发事件告警，需要填 EventCondition 参数。在 EventCondition 下，**仅需要**在 Rules.N.MetricName 中填写 <a href="#preparationsteps">准备事件列表</a> 步骤获得的 **EventName**，其他参数可不填。
9. 在 NoticeIds.N 填写告警通知模板 Id ，例如 notice-qvq836vc。可通过 <dx-tag-link link="https://cloud.tencent.com/document/product/248/51280" tag="API">查询通知模板列表</dx-tag-link> 获得。
10. 填写完以上参数后，单击**在线调用** > **发送请求**，如下图为成功创建云服务器—基础监控告警策略。
![](https://main.qcloudimg.com/raw/c671b947114a3058b57918b7b1a44d01.png)
11. 创建成功后，即可在云监控控制台 [告警策略](https://console.cloud.tencent.com/monitor/alarm2/policy) 页面查看该告警策略。
![](https://main.qcloudimg.com/raw/f40337bf7649bc856c56dc76893f4c39.png)




### 绑定告警对象

1. 登录 [API Explorer 在线调试控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=BindingPolicyObject&SignVersion=)。
2. 将 [准备好的个人密钥](#spreparationsteps) 对应复制到对应的 SecretId、SecretKey 文本框。
3. 在**输入参数**配置项找到 Region，选择相关地域。
4. 在 Module 中填写“monitor”。
5. 在 GroupId 中填写0。
6. InstanceGroupId 和 Dimensions  选一项填写，说明如下：
	- **InstanceGroupId：**实例分组 ID。如需按照实例分组绑定告警对象，则需要传实例分组 ID（例如1234），可在云监控控制台 [实例分组](https://console.cloud.tencent.com/monitor/instanceGroup) 页面中，单击对应的实例名称获取，如下图所示：
		![](https://main.qcloudimg.com/raw/5ae5c7e894c88a133063909901ee562f.png)
	- **Dimensions.N：** 如需按照实例 ID 绑定告警策略，则需要填写 Dimensions。说明如下：
<table>
<thead>
<tr>
<th>参数名称</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>RegionId、Region</td>
<td>请参见 <a href="https://cloud.tencent.com/document/product/248/50863">实例地域说明</a>，例如广州，RegionId 为1，Region 为 gz</td>
</tr>
<tr>
<td>Dimensions</td>
<td>填写云服务器实例 ID，可通过 <dx-tag-link link="https://cloud.tencent.com/document/product/213/15728" tag="API">查看实例列表</dx-tag-link> 获取。入参格式为：{"unInstanceId":"ins-xxxxxxxx'"}。</td>
</tr>
<tr>
<td>EventDimensions</td>
<td>填写实例全局唯一 ID，可通过 <dx-tag-link link="https://cloud.tencent.com/document/product/213/15728" tag="API">查看实例列表</dx-tag-link> 获取。入参格式为：{"uuid":"9d51a69e-0e4a-4120-ae58-9c073c851e24"}</td>
</tr>
</tbody></table>
7. 在 PolicyId 中填写 [创建告警策略](#createalarm) 步骤返回的 PolicyId（Response.PolicyId）。例如 policy-zg2sk27j。
8. 填写完以上参数后，单击**在线调用** > **发送请求**，如下图即成功绑定告警策略。
   ![](https://main.qcloudimg.com/raw/bc9a7ff9a297cf8667bf2adcd6f965e9.png)
9. 创建成功后， 即可在云监控控制台 [告警策略](https://console.cloud.tencent.com/monitor/alarm2/policy) 页面查看对应告警策略关联实例数量。
   ![](https://main.qcloudimg.com/raw/1807139db99cc2eac68d6a6ce3b8331c.png)



