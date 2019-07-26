>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (RestartInstances) 用于重启一个或者多个实例。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 简单传递 instanceId 即可，支持批量的ID。
* 实例中正在运行的某些应用程序可能会导致普通关机失败，可以添加 forceStop 参数以允许 API 在关机失败后采用强制关机策略，默认不会强制关机。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceIds.n| 是| String| 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API返回值中的 unInstanceId 获取；此接口支持同时传入多个ID。此参数的具体格式可参考API[简介](https://cloud.tencent.com/doc/api/229/568)的`id.n`一节。
| forceStop| 否| Int |是否强制关机。若为 0，则走普通关机流程；若为 1 则是强制关机。默认为0。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| detail| Array| 参见：[批量异步任务接口返回格式](http://cloud.tencent.com/doc/api/229/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F#2.-批量异步任务接口返回格式)。|

## 4. 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见[CVM错误码](/document/product/213/6982)页面。

|错误码|描述|
|---|---|
|OperationConstraints.InvaildInstanceStatus|实例状态不正确或获取实例状态失败（EC_CVM_STATUS_ERROR）|

## 5. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=RestartInstances
  &instanceIds.0=ins-r8hr2upy
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

参见：[批量异步任务接口返回格式](http://cloud.tencent.com/doc/api/229/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F#2.-批量异步任务接口返回格式)





