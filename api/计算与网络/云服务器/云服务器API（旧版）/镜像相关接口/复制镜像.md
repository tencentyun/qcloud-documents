>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (SyncCvmImage) 用于将自定义镜像同步到其它地区。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>

* 镜像服务目前免费。
* 用户可以把自定义镜像同步到不同地区。
* 每个地域最多只支持创建10个自定义镜像。
* 可以通过 [DescribeImages](http://cloud.tencent.com/document/api/213/1272) 接口查询镜像同步情况，对于其中 status 为 4 和 5 的情况，则分别表示同步（目的地域）和复制中（源地域）的镜像。
* 不支持北美地区。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。
 
| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| srcRegion| 是| String| 源镜像所属地域，填写代号，如gz，sh。可从 [DescribeProductRegionList](https://cloud.tencent.com/doc/api/229/1286) API获取。
| imgIdList.n| 是| String| 镜像ID。可通过 [DescribeImages](/document/product/213/1272) 接口返回值中的 unImgId 获取（此接口支持同时传入多个ID。此参数的具体格式可参考API[简介](https://cloud.tencent.com/doc/api/229/568)的`id.n`一节）。
| dstRegion.n| 是| String| 需要同步到的地域，填写代号，如gz，sh。|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
 

## 4. 示例
 
输入
<pre>
  https://image.api.qcloud.com/v2/index.php?Action=SyncCvmImage
  &srcRegion=gz
  &imgIdList.0=1
  &dstRegion.0=sh
  &desRegion.1=hk
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "code": 0,
    "message": ""
}
```





