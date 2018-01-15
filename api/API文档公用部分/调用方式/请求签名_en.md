The Tencent Cloud API authenticates each access request. Each request is required to include the Signature in its common request parameters for user authentication. The Signature is generated with the user's security credential that consists of a SecretId and a SecretKey. Users who have no security credential can apply for one on Tencent Cloud official website. Otherwise, the Cloud API cannot be called.

## Apply for Security Credential
Before using Tencent Cloud's API for the first time, you need to apply for a security credential on "Tencent Cloud Console" > "[API Key Management](https://console.cloud.tencent.com/cam/capi)". A security credential consists of a SecretId and a SecretKey as follows:

- **SecretId** is used to identify the API caller;
- **SecretKey** is a key used to encrypt signature string and verify the signature string by the server.

>**Note:**
>API private key is an important credential when building Tencent Cloud API requests. With Tencent Cloud APIs, you can operate all of your Tencent Cloud resources under your account. To keep your property and services secure, please keep the private key well and change it on a timely basis (after you do so, remember to delete the old key in time).


### Application Procedure for Getting a Security Credential

1. Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).
2. Click "Cloud Products", and choose "Cloud API Key" under "Management Tool" to access the Cloud API key management page.
![](//mc.qcloudimg.com/static/img/a771465c47830d54730f8f431d586991/image.png)
3. On the [API Key Management](https://console.cloud.tencent.com/capi) page, click "New Key" to create a pair of SecretId/SecretKey.
>**Note:**
> - A developer account can have two pairs of SecretId/SecretKey at most.
> - QQ accounts that are added as sub-users by a developer can apply for different security credentials on different developer consoles.
> - For now, the security credential of a sub-user can only be used to call some of cloud APIs.

## Generate a Signature String
With the SecretId and SecretKey, a signature string can be generated. The detailed procedure of how to generate a signature string is described as follows:

![](//mc.qcloudimg.com/static/img/3a3a616ba175bb95be68123d86715e77/image.png)

Suppose that you have the following SecretId and SecretKey:
SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
SecretKey=Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

>**Note:**
>This is just an example. You need to proceed with your actual SecretId, SecretKey and request parameters.

Let's take Tencent Cloud CVM as an example. When the user calls the API of Tencent Cloud CVM's [View Instance List](https://cloud.tencent.com/document/product/213/9388) (DescribeInstances), the request parameters are as follows:

| Parameter Name | Description | Parameter Value | 
|---------|---------|---------|
| Action | Method name | DescribeInstances | 
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current timestamp | 1465185768 | 
| Nonce | A random positive integer | 11886 | 
| Region | Region where the instance resides in | ap-guangzhou | 
| SignatureMethod | Signature Method | HmacSHA256 | 
| InstanceIds.0 | ID of the instance to be queried | ins-09dx96dg | 

### 1. Sort Parameters
First, sort all the request parameters in ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, and then sort the parameters with the same first letter by their second letters, and so on. You can complete the sorting with the relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

```
{
    "Action" : "DescribeInstances",
    "Nonce" : 11886,
    "Region" : "ap-guangzhou",
    "SecretId" : "AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA",
    "SignatureMethod" : "HmacSHA256",
    "Timestamp" : 1465185768,
    "InstanceIds.0" : "ins-09dx96dg"
}
```
Any other programming language can be used to sort these parameters as long as the same result is produced.
### 2. Generate a Request String
This step is to generate a request string.
Format the above sorted request parameters as `"parameter name"="parameter value"`. Let's take the parameter `"Action"` as an example. If the parameter value is `"DescribeInstances"`, the resulting format is `Action=DescribeInstances`.
>**Note:**
>1. "Parameter value" is the original value instead of URL encoded value.
> 2. Any underscore in the input parameters needs to be converted to ".". However, the underscore in Value does not need to be converted. For example, `Placement_Zone=CN_GUANGZHOU` needs to be converted to `Placement.Zone=CN_GUANGZHOU`.

Then, join the formatted parameters together by "&" to generate the final request string (please ignore line breaks in the following text):

```
Action=DescribeInstances
&InstanceIds.0=ins-09dx96dg
&Nonce=11886
&Region=ap-guangzhou
&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
&SignatureMethod=HmacSHA256
&Timestamp=1465185768
```

### 3. Generate an Original Signature String
This step is used to generate an original signature string.
The construction rule of an original signature string is as follows:
> **Request Method + Request CVM Server + Request Path + ? + Request String**

Description of the parameter structure:
* **Request method:** The POST and GET methods are supported. In this case, a GET request is used. Please note that the methods must be in upper-case.
* **Request CVM Server:**namely CVM Server domain name. The request domain name is determined by the product or the product module to which the API belongs. This domain name is different for different products or product modules. For example, the request domain name for Tencent Cloud CVM API for querying instance lists (DescribeInstances) is: `cvm.api.qcloud.com`. For more information of product request domain names, please see the description for each API.
* **Request path:** This is the request path for the corresponding Tencent Cloud API product. Each product usually corresponds to one fixed path. For example, the request path for Tencent Cloud CVM is always `/v2/index.php`.
* **Request string:** namely the request string generated in the previous step.


Thus, the result of generating the original signature string in the said example is as follows (please ignore line breaks in the following text):
```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
&InstanceIds.0=ins-09dx96dg
&Nonce=11886
&Region=ap-guangzhou
&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
&SignatureMethod=HmacSHA256
&Timestamp=1465185768
```

### 4. Generate a Signature String
This step is used to generate a signature string.
>**Note:** 
> There are two methods to calculate a signature, that is, HmacSHA256 and HmacSHA1. A signature string will be generated with the signature algorithm (namely the SignatureMethod parameter) specified by you. When HmacSHA256 is taken as SignatureMethod, the signature will be calculated with HmacSHA256, while in other cases, the signature will be calculated with HmacSHA1.

Sign the **original signature string** obtained in the previous step with HMAC-SHA1 algorithm, and then encode the generated signature string with Base64 to obtain the final signature string.

Let's take PHD language as an example. Because the signature algorithm of **HmacSHA256** is adopted in this example, the codes used to generate the signature string are as follows (when the signature string program is developed in other programming languages, the original signature string in the said example can be used for verification; if the resulting signature string is the same with that in the example, the program will be acceptable):

```php
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Nonce=11886&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&SignatureMethod=HmacSHA256&Timestamp=1465185768';
$signStr = base64_encode(hash_hmac('sha256', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:

```
0EEm/HtGRr/VJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s=
```

Similarly, when **HmacSHA1** is taken as the signature algorithm, the codes of the resulting signature string are as follows:
```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Nonce=11886&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&SignatureMethod=HmacSHA1&Timestamp=1465185768';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The final signature string is as follows:
```
nPVnY6njQmwQ8ciqbPl5Qe+Oru4=
```


## Encode a Signature String
The generated signature string cannot be directly used as a request parameter, and needs to be encoded with URL encoding.
For example, if the signature string generated in the previous step is `0EEm/HtGRr/VJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s=`, it is converted to `0EEm%2FHtGRr%2FVJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s%3D` after being encoded. Therefore, the resulting signature string request parameter (Signature) is `0EEm%2FHtGRr%2FVJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s%3D`, which will be used to generate the final request URL.
>**Note:**
>If GET method is used, all request parameters need to be encoded with URL encoding. Some language libraries will automatically encode URLs. Reduplicate encoding will cause signature authentication to fail.

## Authentication failed
The following table lists possible errors when authentication fails:

| Error Code | Error Type | Error Description |
|---------|---------|---------|
| 4100 | Identity verification failed | Identity verification failed. Please make sure that the Signature in the request parameter is calculated correctly according to the said procedure., especially note that a request can be initiated again only after the Signature has been encoded with URL encoding. |
| 4101 | Not authorized by the developer to access this API | The sub-user is not authorized to call this API. Please contact the developer for authorization. For more information, please see [Authorization Policy](/doc/product/378/4513). |
| 4102 | Not authorized by the developer to access the resources operated by this API | The user is not authorized by the developer to access some of the requested resources. Please check the message field for the ID of resources that you're not authorized to access. </br> Please contact the developer for authorization. For more information, please see [Authorization Policy](/doc/product/378/4513). |
| 4103 | This API is currently not available for non-developer's SecretId | The sub-user with this SecretID cannot call this API. Only the developer is authorized to call this API. |
| 4104 | SecretId does not exist | Non-existence of SecretId used for signature may also be caused by incorrect private key status. Please make sure the API key is valid and is not disabled. |
| 4110 | Authentication Failed | Permission verification failed. Please make sure you are permitted to access this resource. |
| 4500 | Replay attack error | Please note that the parameters of Nonce in two requests should not be identical and the time difference between the Timestamp and Tencent CVM should not be greater than 2 hours. |

