>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[查询可用区](https://cloud.tencent.com/document/api/213/1286)。

本接口 (DescribeZones) 用于查询可用区信息。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>


## 2. 输入参数

本接口无接口请求参数，只需传入公共请求参数即可，见[公共请求参数](/doc/api/244/4183)页面。
<font style="color:red">注意：此接口必须传入公共请求参数中的Region参数。</font>

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 请求ID。|
| TotalCount| Integer| 可用区数量。|
| ZoneSet| array of [Zone](/doc/product/213/6091) objects| 可用区列表。|


## 4. 错误码

详见[公共错误码](https://cloud.tencent.com/document/api/213/10146)。


## 5. 示例

输入

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeZones
&Version=2017-03-12
&Region=ap-guangzhou
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

<pre>
{
    "Response": {
        "TotalCount": 3,
        "ZoneSet": [
            {
                "Zone": "ap-guangzhou-1",
                "ZoneName": "广州一区",
                "ZoneId": "100001",
                "ZoneState": "UNAVAILABLE"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": "100002",
                "ZoneState": "AVAILABLE"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": "100003",
                "ZoneState": "AVAILABLE"
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
</pre>
