>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
本接口 (DescribeZoneAbility) 用于查询可用区的能力，包括[CBS云硬盘](https://cloud.tencent.com/document/product/439/6329)和[VPC虚拟网络](https://cloud.tencent.com/doc/product/215/535)两种能力查询。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。
 
| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| zoneId| 是| Int| 可用区ID。
| capacity.n| 是| String| 要查询的能力；目前支持CBS和VPC两种能力查询（此接口支持同时传入多个ID。此参数的具体格式可参考API[简介](https://cloud.tencent.com/doc/api/229/568)的`id.n`一节）。


## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| capacitySet| Array| 返回能力信息列表。|


其中 capacitySet 是一个能力信息的集合，单个能力信息数据结构如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| capacity| Array| 能力项。
| isSupported| Int| 是否满足；0为不满足，1为满足。

## 4. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeZoneAbility
  &zoneId=800001
  &capacity.1=cbs
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

```
{
    "code" : 0,
    "message" : "",
    "capacitySet" : [
        {
            "isSupported" : 1,
            "capacity" : [
                "cbs"
            ]
        }
    ]
}
```





