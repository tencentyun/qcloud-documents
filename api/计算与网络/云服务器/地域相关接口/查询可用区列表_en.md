## 1. API Description

Note: This API has been updated. For more information on the old APIs, please see [Query Availability Zones](https://cloud.tencent.com/document/api/213/1286).

This API (DescribeZones) is used to query availability zones.

Domain name for API request: cvm.api.qcloud.com


## 2. Input Parameters

No API request parameters are available for this API. You can only specify common request parameters. For more information, please see [Common Request Parameters](/doc/api/244/4183).
Note: You must specify the parameter Region in the common request parameter for this API.

## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Request ID. |
| TotalCount | Integer | Number of availability zones. |
| ZoneSet | Array of [Zone]() objects | List of availability zones. |


## 4. Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/api/213/10146).


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeZones
&Version=2017-03-12
&Region=ap-guangzhou
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "TotalCount": 3,
        "ZoneSet": [
            {
                "Zone": "ap-guangzhou-1",
                "ZoneName": "Guangzhou Zone 1",
                "ZoneId": "100001",
                "ZoneState": "UNAVAILABLE"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "Guangzhou Zone 2",
                "ZoneId": "100002",
                "ZoneState": "AVAILABLE"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "Guangzhou Zone 3",
                "ZoneId": "100003",
                "ZoneState": "AVAILABLE"
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
</pre>

