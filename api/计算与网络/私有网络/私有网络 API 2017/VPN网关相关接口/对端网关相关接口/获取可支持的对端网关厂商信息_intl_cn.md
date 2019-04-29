## 1. 接口描述
本接口(DescribeUserGwVendor)用于获取可支持的对端网关厂商信息。
接口请求域名：<font style='color:red'>vpc.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为DescribeUserGwVendor。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|无|无|无|无|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data | Array | 返回的信息 |
| data.platform | String | 平台 | 
| data.software | String | 软件版本| 
| data.vendorname | String | 供应商 | 

## 4. 错误码表
该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">vpc错误码</a>

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeUserGwVendor
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "platform":"ios",
            "software":"V15.4",
            "vendorname":"cisco"
        },
        {
            "platform":"comware",
            "software":"V1.0",
            "vendorname":"h3c"
        }
    ]
}
```

