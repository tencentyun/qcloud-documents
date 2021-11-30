## 1. API Description
This API (GetCdbDeviceMonitorInfo) is used to query the monitoring information for the day of the cloud database physical machine. <font style="color:red">**Currently you can only query the instance with the highest configuration(Memory: 488GB, Volume: 6TB)**</font>.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/doc/api/253/1739' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbDeviceMonitorInfo.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| count5Min | No | Int | Returns the last count5Min 5-minute monitoring data of the day; all 5-minute monitoring data of the day are returned by default; the minimum value is 1 and the maximum value is 288 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Object | Instance monitoring data |
data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cpu | Object | Average cpu load (* 100) within 60 seconds | 
| net | Object | Instance network monitoring data | 
| mem | Object | Instance memory monitoring data | 
| disk | Object | Instance disk monitoring data |
cpu is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| load | Array | Instance CPU monitoring data | 
| rate | Object | Instance CPU average usage | 
| rate.total | Array | The overall average usage of the instance CPU in 60 seconds |
| rate.0 | Array | Average usage of cpu 0 in 60 seconds (percentage of CPU in non-idle state) | 
| rate.1 | Array | Average usage of cpu 1 in 60 seconds (percentage of CPU in non-idle state) |
net is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| pkg_in | Array | Number of NIC inbound packets within 60 seconds | 
| pkg_out | Array | Number of NIC outbound packets within 60 seconds | 
| flow_in | Array | Inbound traffic in 60 seconds. Unit: KB | 
| flow_out | Array | Outbound traffic in 60 seconds. Unit: KB | 
| conn | Array | Number of tcp connections collected every 4 minutes | 
mem is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | Array | Value of "total" in the "Mem:" line in free command. Collected every 4 minutes. Unit: KB | 
| used | Array | Value of "used" in "Mem:" line in free command. Collected every 4 minutes. Unit: KB | 
disk is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| util_max | Array | An average percentage of time used for IO operations per second in 60 seconds (the maximum value among all partitions is taken) | 
| await_time_max | Array | Average waiting time for each device I/O operation in 60 seconds (* 100). (The maximum value among all partitions is taken) | 
| read | Array | The total number of read operations completed per second for all disks in 60 seconds (* 100) | 
| write | Array | The total number of write operations completed per second for all disks in 60 seconds (* 100) | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error description |
|---------|---------|---------|
| 9638 | NoSupportQuery | The instance is not running or is not a cloud database physical machine |
| 9572 | InstanceNotExists | Instance does not exist |
| 9013 | InternalError | System internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbDeviceMonitorInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&count5Min=1
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "cpu":{
            "load":[
                "8"
            ],
            "rate":{
                "total":[
                    "3"
                ],
                "0":[
                    "5"
                ],
                "1":[
                    "4"
                ],
                "2":[
                    "4"
                ],
                "3":[
                    "2"
                ]
            }
        },
        "mem":{
            "total":[
                "32740732"
            ],
            "used":[
                "32493912"
            ]
        },
        "net":{
            "pkg_in":[
                "0"
            ],
            "pkg_out":[
                "0"
            ],
            "flow_in":[
                "0"
            ],
            "flow_out":[
                "0"
            ],
            "conn":[
                "39"
            ]
        },
        "disk":{
            "util_max":[
                "0"
            ],
            "await_time_max":[
                "240"
            ],
            "read":[
                "0"
            ],
            "write":[
                "251"
            ]
        }
    }
}
```


