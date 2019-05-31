>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 

本接口 (CreateImage) 用于将实例系统盘的当前状态制作成全新的镜像，使用此镜像可以快速创建实例。

接口请求域名：image.api.qcloud.com

* 镜像服务目前免费。
* 目标实例需要在关机状态下才可以创建自定义镜像。
* 每个地域最多只支持创建10个自定义镜像。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/document/api/213/6976) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceId| 是| String| 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API 返回值中的 unInstanceId 获取。
|imageName   |是   |String |镜像名称，名称不能和已存在的镜像名称重复。命名规则：1-16个英文、数字、连接线“-”。
|imageDescription |否   |String |镜像描述信息。命名规则：只能包含0-64个中文、英文、数字、连接线"-"、下划线"_"。

 

## 3. 输出参数
 

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的 [模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
|requestId|Int|任务 ID。

 
## 4. 示例
 
输入

<pre>
  https://image.api.qcloud.com/v2/index.php?Action=CreateImage
  &instanceId=ins-12345678
  &imageName=test
  &imageDescription=desc
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

```
{
  "code" : 0,
  "message" : "ok",
  "requestId" : 24534341
}

```




