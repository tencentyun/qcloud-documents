>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (ReturnInstance) 用于主动退还实例。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 按量付费的实例，如不主动销毁将一直运行；在不使用该实例时，需要主动退还。
* 只能支持主动退还按量计费类型的实例，包年包月实例如有误创建需要退还的情况还请发[工单系统](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7)。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。
 
| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceId| 是| String| 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API返回值中的 unInstanceId 获取。


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|

## 4. 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见[CVM错误码](/document/product/213/6982)页面。

|错误码|描述|
|---|---|
OperationConstraints.InvaildInstanceStatus|实例状态不正确或获取实例状态失败

## 5. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ReturnInstance
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

```
{
    "code": 0,
    "message": "ok"
}
```




