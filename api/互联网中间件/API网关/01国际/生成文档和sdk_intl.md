## API Description

This API (GenerateApiDocument) is used to generate an API document and an SDK automatically. A document and an SDK are generated for a service in an environment.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ------------- |
| serviceId | Yes | String | The unique ID of the service for which the document is to be created. |
| language | Yes | String | The language of the SDK to be created. Only python and javascript are supported. |
| environment | Yes | String | The service environment of the SDK to be created. |

## Output Parameters
| Parameter Name | Type | Description |
| ------------ | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| documentURL | String | The generated document is stored in COS. This output parameter returns the download link of the generated document. |
| sdkURL | String | The generated SDK is stored in COS. This output parameter returns the download link of the generated SDK. |

## Example 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=GenerateApiDocument
&serviceId=service-xxxx
&language=python
&environment=release
```
The returned results are as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
    "documentURL":"http://api-document-1253970226.cosgz.myqcloud.com/service-xxxx.zip",
	"sdkURL":"http://api-sdk-python-1253970226.cosgz.myqcloud.com/service-xxxx.zip",
}
```





