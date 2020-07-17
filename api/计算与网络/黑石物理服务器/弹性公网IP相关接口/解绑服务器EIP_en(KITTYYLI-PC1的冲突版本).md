>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 1. API Description
This API (bmUnBindRs) is used to unbind an EIP from a CPM. After the EIP is unbound, inactivity fee will still be charged for it, so please [release and clean up](/document/product/386/6676) it in a timely manner .
 
Domain: <font style="color:red">eip.api.qcloud.com</font>
 

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipId | No | String | EIP instance ID |
| instanceId | No | String | CPM Instance ID, which can be obtained from the "instanceID" in the returned fields of API [DescribeDevice](/doc/api/456/6728) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return asynchronous task information. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [EipBmQueryTask](/doc/api/456/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 9032 | InternalCgwErr | Internal API error |
| 30009 | EipNotExist | The EIP does not exist |
| 30010 | EipStateCannotOp | The EIP is not allowed to be unbound under current status |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &Action=bmUnBindRs
  &instanceId=cpm-xxxxxx&eipId=eip-vvvvvvv

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 100000
    }
}

```


