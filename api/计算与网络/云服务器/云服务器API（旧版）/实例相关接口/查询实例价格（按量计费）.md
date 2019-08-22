>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (InquiryInstancePriceHour) 用于获取实例价格(按量计费)。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 仅支持<font color="red">按量计费实例</font>的价格查询，包年包月实例使用 [InquiryInstancePrice](https://cloud.tencent.com/doc/api/229/1349)。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

* 参数存在具体的范围限制。欲获取更详细的参数信息。用户可以参考[此API](https://cloud.tencent.com/doc/api/229/1248)

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| cpu| 是| Int| 实例核数。CPU与内存具体的配比限制参见[CVM实例配置](/document/product/213/2177)。
| mem| 是| Int| 实例内存大小(GB)。CPU与内存具体的配比限制参见[CVM实例配置](/document/product/213/2177)。
| imageId| 是| String| 镜像ID。可通过 [查询镜像](https://cloud.tencent.com/doc/api/229/查询可用的镜像列表) 接口(链接包含公共镜像名称ID对应表)返回字段中的 unImgId获取。|
| imageType| 是| Int| 镜像类型。 1：私有镜像、2：公共镜像、3：服务市场、4: 共享镜像。imageType必须要imageid实际类型匹配。 |
| bandwidthType| 否| String|带宽的类型。PayByHour：按带宽使用时长计费  <br>PayByTraffic：按流量计费。<br> 默认为按使用时长计费。网络计费模式的区别可以参看[购买网络带宽](https://cloud.tencent.com/doc/product/213/509)。|
| bandwidth| 否| Int| 公网带宽(Mbps)，当按流量计费时为公网带宽峰值。默认为0|
| storageSize| 是| Int| 数据盘大小(GB)。步长为10，0表示不要数据盘。关于数据盘的最大大小请参考[硬盘产品简介](https://cloud.tencent.com/doc/product/213/498)。|
| storageType| 否| Int| 数据盘类型。1:本地硬盘、2:普通云硬盘，默认为本地硬盘。关于数据盘的类型选择请参考[硬盘产品简介](https://cloud.tencent.com/doc/product/213/498)。|
| goodsNum| 否| Int| 购买实例数量。默认为1, 最大100|





## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| data |   Array | 返回列表 |

**Data列表结构**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| bandwidth | Array | 带宽详细。|
| cvm | Array | 实例详细。|

**CVM、bandwidth列表结构**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| price | String | 价格。|
| price_unit | String | 价格单位。|


## 4. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=InquiryInstancePriceHour
  &cpu=1
  &mem=1
  &bandwidthType=PayByTraffic
  &bandwidth=2
  &storageSize=10
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

```
{
    "code": 0,
    "message": "",
    "data": {
        "cvm": {
            "price": "0.28",
            "price_unit": "HOUR"
        },
        "bandwidth": {
            "price": "1.60",
            "price_unit": "GB"
        }
    }
}
```





