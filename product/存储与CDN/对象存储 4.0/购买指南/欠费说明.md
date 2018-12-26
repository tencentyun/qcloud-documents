## 账单周期

下表是对象存储计费项和对应的计费（账单）周期介绍。

<table>
   <tr>
      <th>计费项</td>
      <th>计费周期</td>
   </tr>
   <tr>
      <td>存储容量</td>
      <td rowspan="3">按月计费</td>
   </tr>
   <tr>
      <td>请求数</td>

   </tr>
   <tr>
      <td>数据取回量</td>

   </tr>
   <tr>
      <td>流量</td>
      <td>按日计费</td>
   </tr>
</table>

## 欠费停服

当您的账户发生欠费时，对象存储 COS 会在24小时后停止服务，您的数据可以继续保留120天，如果在此期间未进行续费使账户余额大于等于0， 您的数据将会被销毁。

请在收到欠费通知后，及时前往控制台 [充值中心](https://console.cloud.tencent.com/account/recharge) 进行充值，以免影响您的业务。

如您对消费明细有疑问，可以在控制台 [资源账单](https://console.cloud.tencent.com/account/resources) 页面查阅和核对您的消费明细，操作方式请查阅 [查询消费明细](https://cloud.tencent.com/document/product/436/30357) 文档。

如您对具体的扣费项有疑问，可以参考 [COS 计费说明](https://cloud.tencent.com/document/product/436/16871) 了解具体的计费项含义及计费规则。

您还可以通过计费中心的**余额告警**功能，自行设定欠费预警。详细信息请参阅 [余额预警指引](https://cloud.tencent.com/document/product/555/9942)。

>!
> 1. 欠费停服后，**数据占用的存储容量会持续计费**，直到销毁数据。
> 2. 销毁数据后，不可恢复。
> 3. 用户续费使账户余额大于等于0后，服务会自动开启。
> 4. 存储在 COS 的数据若不再使用，请及时删除，以免继续扣费。


