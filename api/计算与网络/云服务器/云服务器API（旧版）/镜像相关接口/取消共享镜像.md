>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (CancelShareImage) 用于取消共享镜像。

接口请求域名：image.api.qcloud.com

* 镜像服务目前免费。
* 每个自定义镜像最多可共享给50个账户；取消共享可以释放账户的配额。
* 要完全取消分享，请先 [查询共享人](https://cloud.tencent.com/doc/api/229/2391) 获取该镜像共享给的全部账户，并在调用时全部指定。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/document/api/213/6976) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| imageId | 是 | String | 镜像ID，可通过 [DescribeImages](http://cloud.tencent.com/document/api/213/1272) 接口返回字段中的 unImgId 获取。|
| uinList.n | 是 | String | 被取消共享的账号（此接口支持同时传入多个ID。此参数的具体格式可参考API [简介](https://cloud.tencent.com/doc/api/229/568) 的`id.n`一节）。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的 [模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
 
## 4. 示例
输入
<pre>
https://image.api.qcloud.com/v2/index.php?Action=CancelShareImage
&imageId=img-jgggrva9
&uinList.0=877354327
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "code":"0",
    "message":""
}
```





