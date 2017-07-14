## 1. API Description
This API (EipBmQueryTask) is used to query the asynchronous task status of EIP, with the focus on the progress of such operations as binding and unbinding.
 
Domain: eip.api.qcloud.com


## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| requestId | Yes | Int | The requestId returned by EIP asynchronous task. For more information, please see the output of [EipBmDelete]() |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes]().  |
| message | String | Error message |
| data | Array | Return an array |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.status | Int | Current task status: 0 - Succeeded, 1 - Failed, 2 - In progress |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| -8000 | DesErr | An error occurred in process system |
| -8001 | DesInBusy | System is busy |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &Action=EipBmQueryTask
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>&requestId=2383049
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "status": 0
    }
}

```


