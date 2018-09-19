## 1. 接口描述
 本接口(DescribeAccountVpcAttributes)用于查询账号网络属性。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeAccountVpcAttributes。
 

无入参
 
 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data.supportedPlatforms | String | only-vpc：默认vpc用户，默认vpc用户所有带网络属性的云资源都是在私用网络下的；classic：基础网络用户，基础网络用户所有带网络属性的资源都是在基础网络下的。|

  ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
无特殊错误码

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeAccountVpcAttributes
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data":{
      "supportedPlatforms":"only-vpc"
    }
}

```

