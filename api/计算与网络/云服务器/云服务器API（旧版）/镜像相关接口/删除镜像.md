>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 

本接口 (DeleteImages) 用于删除一个或者多个镜像。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>


* 当镜像状态为创建中和使用中状态时, 不可以删除。
* 每个地域最多只支持创建10个自定义镜像，删除镜像可以释放账户的配额。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| imageIds.n | 是 | String | 镜像ID，可通过 [DescribeImages](http://cloud.tencent.com/document/api/213/1272) 接口返回字段中的 unImgId 获取；此接口支持同时传入多个镜像ID（此接口支持同时传入多个ID。此参数的具体格式可参考API[简介](https://cloud.tencent.com/doc/api/229/568)的`id.n`一节）。


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
 
 

## 4. 示例
 
输入
<pre>
  https://image.api.qcloud.com/v2/index.php?Action=DeleteImages
  &imageIds.0=img-xxxxxxxx
  &imageIds.1=img-xxxxxxxx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
参见：[批量异步任务接口返回格式](http://cloud.tencent.com/doc/api/229/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F#2.-批量异步任务接口返回格式)





