## 1. 接口描述
本接口(DescribeUserCvmOverview)用于获取开发商各地域cvm的概览信息列表。
接口请求域名：<font style='color:red'>cvm.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/372/4153' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为DescribeUserCvmOverview。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| regionIds.n (regionIds 为数组，此处入参需要填写数组元素 ) | 是 | String | 地域ID列表|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data | Array | 描述（待补充） |
| data.appId | Int | 描述（待补充）| 
| data.regionId | Int | 描述（待补充）| 
| data.newFlag | Int | 描述（待补充）| 
| data.validCvmNum | Int | 描述（待补充）| 


## 4. 示例
输入
```
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeUserCvmOverview
&regionIdList.0=1
&regionIdList.2=2
&COMMON_PARAMS
```
输出
```
{
    "code":"0",
    "message":"",
    "data":[
        {
            "appId":"1351000042",
            "regionId":"1",
            "newFlag":"1",
            "validCvmNum":"1"
        },
        {
            "appId":"1351000042",
            "regionId":"2",
            "newFlag":"0",
            "validCvmNum":"0"
        }
    ]
}
```

