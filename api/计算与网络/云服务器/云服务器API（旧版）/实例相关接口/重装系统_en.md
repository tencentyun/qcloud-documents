## 1. API Description

This API (ResetInstances) is used to reinstall the operating system on the specified instance.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>


* If you have specified an image ID, the reinstallation is performed with the specified image. Otherwise, the image used by the current instance is used.
* The system disk will be formatted and reset. Please ensure that there is no important file in the system disk.
* As the operating system is switched between Linux and Windows, the system disk ID of the instance will change, and the snapshot associated with the system disk can't be used to roll back and recover data.
* If no password is specified, a random password will be issued via internal message.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](/doc/api/229/831) API.
| imageType | No | Int | Image type. <br>1: Private image<br>2: Public image<br>3: Service Marketplace image<br>4: Shared image. <br>The default is 2. It should be specified with imageId. |
| imageId| No | String| Image ID.  By default, the current image of the instance is used for the reinstallation. If an image ID is specified, the specified image is used. The image ID can be obtained from unImgId in the returned field of [DescribeImages](http://cloud.tencent.com/document/api/213/1272) API (which includes common public image IDs). It should be specified with imageType. |
| password | No | String | Instance password. Linux instance's password should be a combination of 8-16 characters comprised of at least two of the following types: letters [a-z, A-Z], numbers [0-9], and special symbols [( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' , . ? / ]. Windows instance's password should be a combination of 12-16 characters comprised of at least three of the following types: lowercase letters [a-z], uppercase letters [A-Z], numbers [0-9] and special symbols [( ) &#96; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. |
| needSecurityAgent | No | Int | Install Security Agent; 0: Do not install; 1: Install; Install by default.
| needMonitorAgent | No | Int | Install Monitor Agent; 0: Do not install; 1: Install; Install by default.
| rootSize | No | Int | System drive size (GB). The rootSize remains unchanged by default.

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| requestId | Int | Request task ID. |

## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
| OperationConstraints.InvaildInstanceStatus | Instance status is incorrect or the attempt to obtain the instance status failed|
| OperationFail.AllResourceOpFailed | The operation performed on the resource failed |
| OperationConstraints.AccountBalanceNotEnough | Your balance is insufficient. Please top up first |
| OperationFail.SystemBusy | System is busy with resource purchase | 

## 5. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ResetInstances
  &instanceId=qcvm12345
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>


Output

Refer to [Format of Returned Results of Ordinary Asynchronous Task API](http://cloud.tencent.com/doc/api/229/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F#1.-普通异步任务接口返回格式)






