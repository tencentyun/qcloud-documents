## 1. 接口描述
 
本接口 (UpdateInstanceBandwidthHour) 用于调整按量计费实例的公网带宽。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 立即生效，支持升级与降级。
* 只针对按量计费实例，包年包月实例调整带宽需要使用 [UpdateInstanceBandwidth](https://cloud.tencent.com/doc/api/229/1251) API。
* 带宽值最小可为0Mpbs，按流量计费实例带宽最大为100Mbps；按带宽计费模式实例最大为200Mbps；专用宿主机的实例最大宽带为1000Mbps。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/doc/api/229/1230)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceId| 是| String| 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API返回值中的 unInstanceId 获取。
|bandwidth |是 |Int |带宽值(Mpbs)；按流量计费则为宽带峰值。

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
 

## 4. 示例
 
输入

```
  https://cvm.api.qcloud.com/v2/index.php?Action=UpdateInstanceBandwidthHour
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &bandwidth=8
  &<公共请求参数>
```

输出

```

{
    "code": 0,
    "message": "ok"
}
```





