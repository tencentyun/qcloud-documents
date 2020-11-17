## 1. API Description
This API (CdbTdsqlModifyConfig) is used to modify database parameters.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlModifyConfig.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| config.n (config is an array. The input parameters here are the array elements) | Yes | String | List of parameters, of which each element is a combination of Param and Value. See example |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976). The following only provides the formats of returned values for the "data" field.

If successful, the information of affected parameter is returned. Otherwise the reason for failure is returned.
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| EINSTANCEDELETED | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| OssOpertaionFailed | OSS internal failure|
| InstanceHasBeenLocked | TDSQL is locked by another flow |
| GetDbconfigFailed | Failed to acquire parameter |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlModifyConfig
&cdbInstanceId=40732
&config.0.Param=auto_increment_increment
&config.0.Value=2
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": 40732,
        "config": [
            {
                "param": "auto_increment_increment",
                "code": 0
            }
        ]
    }
}
```


