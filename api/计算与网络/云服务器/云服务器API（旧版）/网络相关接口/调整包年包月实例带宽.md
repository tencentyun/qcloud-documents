>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (UpdateInstanceBandwidth) 用于调整包年包月实例的公网带宽。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 只针对包年包月实例和[带宽包](https://cloud.tencent.com/doc/product/213/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AE%A1%E7%90%86%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98#1.-.E4.BB.80.E4.B9.88.E6.98.AF.E5.B8.A6.E5.AE.BD.E5.8C.85.E6.A8.A1.E5.BC.8F.EF.BC.9F)用户。按量计费实例调整带宽需要使用 [UpdateInstanceBandwidthHour](https://cloud.tencent.com/doc/api/229/1345) API。
* 只允许升级带宽，不允许降低带宽值。
* 按流量计费实例带宽最大为100Mbps；按带宽计费模式实例最大为200Mbps；专用宿主机的实例最大宽带为1000Mbps。
* <font style="color:red">只支持按带宽计费方式。</font>

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceId| 是| String| 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API返回值中的 unInstanceId 获取。
| bandwidth| 是| Int| 升级后的带宽值(Mbps)。升级后的带宽不能小于当前带宽；带宽包用户可调整为65535，并且可以升高或者降低（0-65535）。
| startTime| 是| String| 起始时间。格式如：2016-10-30，该时间不能早于当前时间；如果是今天则为立即生效。
| endTime| 是| String| 终止时间。格式如：2017-11-30，修改带宽的有效期包含此日期，该时间不能晚于实例过期的时间；实例的到期时间可以使用 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API查询。


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| dealIds| Array| 生成的订单号，用于查询执行情况。


## 4. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=UpdateInstanceBandwidth
  &instanceId=qcvm12345
  &bandwidth=2
  &startTime=2014-07-20
  &endTime=2014-08-20
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

 * 注意，如果该实例的网络为按流量计费模式，没有dealIds。

```

  {
      "code" : 0,
      "message" : "ok",
      "dealIds":[
          12194872988
      ]
  }

```





