本文将为您介绍如何通过 <dx-tag-link link="https://cloud.tencent.com/document/api/248/51287" tag="API">创建告警策略接口</dx-tag-link> 和 <dx-tag-link link="https://cloud.tencent.com/document/api/248/40421" tag="API">绑定策略对象</dx-tag-link> 创建告警策略并绑定告警对象。


<dx-tag-link link="https://cloud.tencent.com/document/api/248/40421" tag="API">绑定策略对象</dx-tag-link>

## 准备工作

在调用创建 <dx-tag-link link="https://cloud.tencent.com/document/api/248/51287" tag="API">创建告警策略接口（CreateAlarmPolicy）</dx-tag-link> 前需要准备以下入参资料。



<dx-tabs>
::: 准备个人密钥
 1. 登录 [访问管理控制台-API 密钥管理](https://console.cloud.tencent.com/cam/capi)。
 2. 单击【显示】即可获取 SecretKey  。
 ![](https://main.qcloudimg.com/raw/6ba975475ddd17f82bca8100eb2efb19.png)

> ?如未创建密钥，请单击【新建密钥】即可创建密钥。
 :::
 ::: 准备告警策略类型
 通过 <dx-tag-link link="https://cloud.tencent.com/document/api/248/48683" tag="API">查询所有名字空间</dx-tag-link> 可以查询到所有策略类型。步骤如下：
1. 进入 [API Explorer 在线调用控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=DescribeAllNamespaces)，参考下表填写输入参数。
<table>
	<tr>
	<th>参数名称</th>
	<th>说明</th>
	</tr>
	<tr>
		<td>SecretId、SecretKey</td>
		<td>填写准备好的 SecretId、SecretKe</td>
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
		<td>非必填，不需要填写</td>
	</tr>
</table>
3. 单击【在线调用】>【发送请求】，获取响应结果。返回结果中 Response.QceNamespacesNew.N.Id即创建告警策略需要的 Namespace。如下图为查看云服务器告警策略类型：
   ![](https://main.qcloudimg.com/raw/19edabd3808c034c318845ae835ebc7f.png)

<dx-alert infotype="notice" title="">
此处 Namespace 为告警策略类型，与拉取监控数据时的云产品 Namespace 不同。
</dx-alert>

:::
::: 准备指标列表
通过 [API 查询告警指标列表]( https://cloud.tencent.com/document/api/248/51283)可以查询到策略类型下的所有告警指标。

1. 进入 [API Explorer 在线调用控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=DescribeAlarmMetrics)，参考下表填写输入参数。
<table>
	<tr>
	<th>参数名称</th>
	<th>说明</th>
	</tr>
	<tr>
		<td>SecretId、SecretKey</td>
		<td>填写准备好的 SecretId、SecretKe</td>
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
2. 点击右侧【在线调用】<【发送请求】，获取响应结果。返回结果中Response.Metrics.N即该策略类型下的所有告警指标。如下图为获取云服务器指标列表：
  ![](https://main.qcloudimg.com/raw/da93d3e304a016a3ce7c7e4081835426.png)
:::
::: 准备事件列表
通过 [API 查询告警事件列表]( https://cloud.tencent.com/document/api/248/51284)可以查询到策略类型下的所有告警指标。

1. 进入 [API Explorer 在线调用控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=DescribeAlarmEvents&SignVersion=))，参考下表填写输入参数。
<table>
	<tr>
	<th>参数名称</th>
	<th>说明</th>
	</tr>
	<tr>
		<td>SecretId、SecretKey</td>
		<td>填写准备好的 SecretId、SecretKe</td>
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
2. 点击右侧【在线调用】<【发送请求】，获取响应结果。返回结果 Response.Events.N.EventName 即告警策略需要的 EventName。
   ![](https://main.qcloudimg.com/raw/de44fb8113250229bfbf5d7985b381da.png)
   :::
</dx-tabs>


## 实践步骤

下列将通过Demo演示，为您介绍如何使用  [创建告警策略接口（CreateAlarmPolicy）](https://cloud.tencent.com/document/api/248/48683) 等接口创建云服务器-基础监控告警策略。

### 创建告警策略

1. 登录[ API Explorer 在线调试控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=CreateAlarmPolicy&SignVersion=)。
2. 将 准备好的个人密钥 对应复制到对应的 SecretId、SecretKey 文本框。
3. 在【输入参数】配置项找到 Region，选择相关地域。
4. 在 Module 中填写“monitor”，PolicyName 中填写策略名称（策略名称由您自定义），MonitorType 中填写“MT_QCE”。
5. 在 Namespace 中填写上述【准备告警策略类型】步骤中获取的告警策略类型，例如 云服务器-基础监控告警策略类型为：cvm_device。
6. 在云服务器-基础监控场景下 Remark、Enable 为选填，ProjectId 为必填。

- Remark 为备注，可不填。
- Enable为是否启用告警策略 0=停用 1=启用，可不传，默认为1。
- ProjectId 为项目 Id。云服务器-基础监控需填写 **0** 。

> ? ProjectId为项目 Id，-1=无项目 0=默认项目，根据策略类型而定可不传，默认为-1。例如有些告警策略类型下没有项目概念（如私有网络），可使用默认传参 -1 。若该告警策略类型有项目概念（如云服务器-基础监控），默认传参-1会报错，入参需要修改为0。

7. Condition 配置说明如下：

| 参数名称    | 是否必填 | 说明                                                         |
| ----------- | -------- | ------------------------------------------------------------ |
| IsUnionRule | 是       | 指标触发与或条件，0=或，1=与，或表示触发任一条件时发送告警，与为触发所有条件后发送告警。 |
| Rules.N     | 是       | 告警触发条件列表。可参考在线调用 AlarmPolicyRule 参数说明进行配置。<li> **MetricName**：填写【准备指标列表】步骤返回中的MetricName（Metrics.N.MetricName）。</li><li>**Period**：填写【准备指标列表】步骤返回中的 Period（Metrics.N.MetricConfig.Period）。</li><li>**Operator**：填写【准备指标列表】步骤返回中的 Operator（Metrics.N.MetricConfig.Operator）。</li><li>**Value**：填写阈值，不需要填写单位，如：80。</li><li>**ContinuePeriod**：填写【准备指标列表】步骤返回中的 ContinuePeriod（Metrics.N.MetricConfig.ContinuePeriod）。</li><li>**NoticeFrequency**：告警频率（按秒计算），参考参数说明：告警间隔 0=不重复 ；300=每5分钟告警一次； 600=每10分钟告警一次 ；900=每15分钟告警一次 1800=每30分钟告警一次；3600=每1小时告警一次； 7200=每2小时告警一次 ；10800=每3小时告警一次； 21600=每6小时告警一次； 43200=每12小时告警一次 ；86400=每1天告警一次；<li>**IsPowerNotice**：告警频率是否指数增长 0=否 1=是。</li><li>其它参数不需要填写</li> |

8. 如果要触发事件告警，需要填 EventCondition 参数。在EventCondition下，**仅需要**在 Rules.N.MetricName 中填写【准备事件列表】步骤获得的**EventName**，其他参数不填。
9. 在 NoticeIds.N 填写告警通知模板 Id ，如notice-qvq836vc。可通过 [API 查询通知模板列表](https://cloud.tencent.com/document/api/248/51280)获得。
10. 填写完以上参数后，单击【在线调用】<【发送请求】，如下图为成功创建云服务器—基础监控告警策略。
    ![](https://main.qcloudimg.com/raw/c671b947114a3058b57918b7b1a44d01.png)
    11.创建成功后，即可在 [云监控-告警策略控制台](https://console.cloud.tencent.com/monitor/alarm2/policy)查看该告警策略。
    ![](https://main.qcloudimg.com/raw/f40337bf7649bc856c56dc76893f4c39.png)

### 绑定告警对象

1. 登录[ API Explorer 在线调试控制台](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=BindingPolicyObject&SignVersion=)。
2. 将 准备好的个人密钥 对应复制到对应的 SecretId、SecretKey 文本框
3. 在【输入参数】配置项找到 Region，选择相关地域。
4. 在 Module 中填写“monitor”。
5. 在 GroupId 中填写0。
6. InstanceGroupId 和 Dimensions  选一项填写，说明如下：

- **InstanceGroupId：**实例分组 ID。如需按照实例分组绑定告警对象，则需要传实例分组ID，如：1234，可在 [云监控-实例分组控制台](https://console.cloud.tencent.com/monitor/instanceGroup)中，点击对应的实例名称获取，如下图 。
  ![](https://main.qcloudimg.com/raw/5ae5c7e894c88a133063909901ee562f.png)
- **Dimensions.N：** 如需按照实例 ID 绑定告警策略，则需要填写 Dimensions。说明如下：

| 参数名称         | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| RegionId、Region | 请参考 [实例地域说明](https://cloud.tencent.com/document/product/248/50863)，如广州 RegionId为1，Region为gz |

|Dimensions|填写云服务器实例ID，可通过 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 获取。入参格式为：{"unInstanceId":"ins-xxxxxxxx'"}。
|EventDimensions|填写实例全局唯一ID，可通过 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 获取。入参格式为：{"uuid":"9d51a69e-0e4a-4120-ae58-9c073c851e24"}|

7. 在 PolicyId 中填写【创建告警策略】步骤返回的 PolicyId（Response.PolicyId）。例如：policy-zg2sk27j。
8. 填写完以上参数后，单击【在线调用】<【发送请求】，如下图即成功绑定告警策略。
   ![](https://main.qcloudimg.com/raw/bc9a7ff9a297cf8667bf2adcd6f965e9.png)
   创建成功后， [云监控-告警策略控制台](https://console.cloud.tencent.com/monitor/alarm2/policy) 查看对应告警策略关联实例数量。
   ![](https://main.qcloudimg.com/raw/1807139db99cc2eac68d6a6ce3b8331c.png)



