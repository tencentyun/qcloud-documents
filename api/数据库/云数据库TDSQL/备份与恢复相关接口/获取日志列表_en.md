## 1. API Description
This API (CdbTdsqlGetLog) is used to acquire the list of various logs of a database.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| type | Yes | Int | 1: binlog; 2: cold backup; 3: errlog; 4:slowlog |
| dbMode | No | Int | 0: Standard; 1: Distributed (currently not available, thus the parameter is not applicable) |

## 3. Output Parameters

The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976). The following only provides the formats of returned values for the "data" field.

| Parameter Name | Type | Description |
|---------|---------|---------|
| id | Int | Instance ID |
| type | Int | 1: binlog; 2: cold backup; 3: errlog; 4:slowlog |
| total | Int | Total number of logs |
| files | Array | Information including uri, length, mtime (modification time) and so on |
| vpcpreifx | String | If the instance is in a VPC network, the download address is the URI prefixed by this string |
| normalpreifx | String | If the instance is in an ordinary network, the download address is the URI prefixed by this string |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| EINSTANCEDELETED | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| GetInstanceInfoFailed | Failed to acquire instance information |
| CheckDbInfoFailed | Failed to check database information |
| HDFSError | HDFS error |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlGetLog
&cdbInstanceId=40732
&type=1
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": 40732,
        "type": 1,
        "total": 1,
        "files": [
            {
                "uri": "/1/noshard_108/set_1468578840_203059/1468578832/859932065/000001/5ce7d1a8f26c2dfcf1de22d4e9792b11b0b0057450684d266e1bf9a8aa6ea272",
                "length": 5253724,
                "mtime": 1468822981
            }
        ],
        "vpcpreifx": "http://169.254.0.27:8083",
        "normalpreifx": "http://10.66.255.253:8083"
    }
}
```


