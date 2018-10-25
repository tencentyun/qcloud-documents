## 1. API Description
Domain name: cvm.api.qcloud.com
API name: DescribeInstanceImageInfo

View the information on the image associated with an instance

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| uInstanceIds.n (uInstanceIds is a list, whose elements need to be entered as input parameters) | Yes | String | Instance ID. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message | String | Error message |
| data | Array | Description (to be added) |
| data.unImgId | String | Description (to be added) | 
| data.uInstanceId | String | Description (to be added) | 


## 4. Example
Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceImageInfo
&uInstanceIds.0=ins-898kaj40
&uInstanceIds.1.ins-m1fmc400=
&<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":[
        {
            "unImgId":"img-bemx4xck",
            "uInstanceId":"ins-898kaj40"
        }
    ]
}
```


