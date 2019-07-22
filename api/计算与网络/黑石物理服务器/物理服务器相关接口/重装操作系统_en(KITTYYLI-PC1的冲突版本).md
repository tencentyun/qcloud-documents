>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>


## 1. API Description
 
This API (ReloadDeviceOs) is used to re-install CPM's operating system.

Domain for API request: <font style="color:red">bm.api.cloud.tencent.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | Unique device ID. You can acquire device information by using the [Query Servers (DescribeDeviceList)](/doc/api/456/6728) API. |
| passwd | Yes | String | Password. The password must contain 8-16 characters, with at least two types of characters out of three (letters, numbers or symbols !@#$%&^*()).  |
| osTypeId | No | Int | Operating system type ID. You can acquire operating system information by using the [Query List of Operating Systems (DescribeOs)](/doc/api/456/6727) API. |
| raidId | No | Int | RAID type ID. You can acquire RAID information by using the [Query RAID Method of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/product/386/7370) API. |
| agentIds | No | Array | Indicates which agent services are to be installed. Available values for agentId: 2: Monitor agent<br/>; 3: Security agent<br/> |
| sysRootSpace | No | Int | System disk root partition size. Default is 10 G. For the size of system disk, please see the [Query RAID Method of Device Class and System Disk Size (DescribeDeviceClassPartition)](/document/product/386/7370) API |
| sysSwaporuefiSpace | No | Int | The size of swap partition or /boot/efi partition of system disk. When the machine boots in UEFI mode, the partition is /boot/efi with a default size of 2 G. The partition is swap for normal machines, in which case you don't need to specify this partition. To determine whether the machine boots in UEFI mode, please see the [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636) API |
| sysUsrlocalSpace | No | Int | Size of /usr/local partition. This partition does not exist by default.  |
| sysDataSpace | No | Int | Size of /data partition. Any remaining space of the system disk will be allocated to the /data partition.  |
| isZoning | No | Int | wheather to format the disk. 0: no; 1: yes.  1 is default. |
| vpcId | No | Int | allocate into other vpc and subnet. keep inact by default if you ignore the parameter of 'vpcId' and 'subnetId'. |
| subnetId | No | Int | allocate into other vpc and subnet. keep inact by default if you ignore the parameter of 'vpcId' and 'subnetId'. |

You can left the operating system type and RAID type empty, in which case the current operating system and RAID type of the machine will be used.
An empty agentIds means monitor and security agents are not installed.


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Obj | Returned asynchronous operation ID

## 4. Module Error Codes

| code | codeDesc | Description |
|------|------| -----|
| 9001 | InternalError.DbError | Error occurred when operating the database |
| 9005 | InternalError.RbmqError | Operating system queue error |
| 10001 | InvalidParameter | Invalid parameter |
| 12002 | OperationDenied.IncorrectInstanceStatus | Cannot re-install operating system for the device |
| 12003 | OperationDenied.RaidNotSupport | Specified RAID type is not supported by the device |

 

## 5. Example
 
Input

<pre>`https://domain/v2/index.php?Action=ReloadDeviceOs`
  &instanceId=cpm-34xs43xs
  &passwd=34x@#23A
  &osTypeId=2
  &raidId=4
  &agentIds.1=2
  &agentIds.2=3
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

```
{
  "code": 0,
  "message": "OK",
  "data": {
       "taskId": 101
   }
}

```
