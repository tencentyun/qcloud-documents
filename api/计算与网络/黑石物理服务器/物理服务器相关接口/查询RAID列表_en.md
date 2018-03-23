## 1. API Description

This API (DescribeDeviceClassRaid) is used to acquire the corresponding RAID method of the device class.
Domain for API request: <font style="color:red">bm.api.qcloud.com</font>



## 2. Input Parameters
None



## 3. Output Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> data
<td> Object
<td> The raid json Object of various devices. Please see the example for detailed data structure. Structure is described in the table below.
<tr>
<td> data.n1
<td> String
<td> n1,n2...refer to the device class, such as M10, B6. The value is the description of the RAID.
<tr>
<td> data.n1.raidId
<td> String
<td> raid ID, the value is information of the RAID. Please see the following table.
</tbody></table>

</b></th>Information structure of RAID</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> deviceClass
<td> String
<td> Device class, such as M10, B6.
<tr>
<td> raidId
<td> String
<td> raidId.
<tr>
<td> diskSize
<td> String
<td> Disk size.
<tr>
<td> partition
<td> Object
<td> Partition information (unit: GB).
<tr>
<td> unFormatPartition
<td> String
<td> Partition that is not formatted. None by default.
<tr>
<tr>
<td> raid
<td> String
<td> raid level.
<tr>
<tr>
<td> raidDisplay
<td> String
<td> Displayed name of the raid level.
<tr>
<tr>
<td> description
<td> String
<td> Description.
<tr>
</tbody></table>



## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |



## 5. Example
Input
```
https://bm.api.qcloud.com/v2/index.php?Action=DescribeDeviceClassRaid&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC&Nonce=48476&Timestamp=1476436689&Region=bj&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "B6": {
            "1": {
                "deviceClass": "B6",
                "raidId": "1",
                "diskSize": "600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "All disks form up as RAID 0, fast read speed but no redundancy. This level is suitable for applications that have high requirements for reading data but low requirement for data security"
            }
        },
        "M10": {
            "1": {
                "deviceClass": "M10",
                "raidId": "1",
                "diskSize": "3600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3568
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "All disks form up as RAID 0, fast read speed but no redundancy. This level is suitable for applications that have high requirements for reading data but low requirement for data security"
            },
            "2": {
                "deviceClass": "M10",
                "raidId": "2",
                "diskSize": "3300G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3268
                },
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "All disks form up as RAID 5. This solution takes storage performance, data security and storage cost into consideration at the same time, and is suitable for scenarios where a large amount of data is expected to be read while less data is written"
            }
        }
    }
}
```


