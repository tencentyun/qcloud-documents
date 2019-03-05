Tencent Cloud API authenticates each access request, so each request is required to include signature information in the common request parameters for user authentication. The signature is generated with user's security credentials, which consist of a SecretId and a SecretKey. If you don't have security credentials, apply for the credentials from the Tencent Cloud official website. Otherwise, you will not be able to call the cloud APIs.

## Applying for Security Credentials
Before using Tencent Cloud's APIs for the first time, you need to apply for security credentials on **Tencent Cloud Console** -> **[API Key Management](https://console.cloud.tencent.com/cam/capi)**. Security credentials consist of a SecretId and a SecretKey, where:

- **SecretId** is used to identify the API caller;
- **SecretKey** is a key used to encrypt signature string and verify the signature string by the server.

>**Note:**
>API key is very important for building Tencent Cloud API requests. With Tencent Cloud APIs, you can work with all of your Tencent Cloud resources under your account. For the security of your property and services, keep the key well and change it regularly (after changing the key, be sure to delete the old one as soon as possible).


#### How to apply for security credentials

1. Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).
2. Click **Cloud Products**, and select **Cloud API Key** under **Management Tools** to go to the cloud API key management page.
![](//mc.qcloudimg.com/static/img/a771465c47830d54730f8f431d586991/image.png)
3. On the [API Key Management](https://console.cloud.tencent.com/capi) page, click **New Key** to create a pair of SecretId/SecretKey.
>**Note:**
> - A developer account can have two pairs of SecretId/SecretKey at most.
> - The QQ accounts added as sub-users by a developer can apply for different security credentials on different developer consoles.
> - The security credentials of a sub-user can only be used to call some of cloud APIs.

## Generate a Signature String
With the SecretId and SecretKey, a signature string can be generated. The following is the process for generating a signature string:

![](//mc.qcloudimg.com/static/img/3a3a616ba175bb95be68123d86715e77/image.png)

Suppose that you have the following SecretId and SecretKey:
SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
SecretKey: Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

>**Note:**
>This is just an example. You need to proceed with your actual SecretId, SecretKey and request parameters.

For example, when you call Tencent Cloud CVM's API [View Instance List](https://cloud.tencent.com/document/product/213/9388) (DescribeInstances), the request parameters are as follows:

| Parameter Name | Description | Parameter Value | 
|---------|---------|---------|
| Action | Method name | DescribeInstances | 
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current timestamp | 1465185768 | 
| Nonce | A random positive integer | 11886 | 
| Region | The region where the instance resides | ap-guangzhou | 
| SignatureMethod | Signature method | HmacSHA256 | 
| InstanceIds.0 | ID of the instance to be queried | ins-09dx96dg | 

### 1. Sort parameters
First, sort all the request parameters in an ascending lexicographical order by their names. (This is like sorting words in a dictionary in an ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, then by their second letters if their first letters are the same, and so on). You can complete the sorting process using relevant sorting functions in the programming language, such as the ksort function in PHP. The parameters in the example are sorted as follows:

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
### 2. Construct a request string
This step is to generate a request string.
Format the request parameters sorted in the previous step as `"parameter name"="parameter value"`. For example, if the parameter value of `"Action"` is `"DescribeInstances"`, the resulting format is `Action=DescribeInstances`.
>**Note:**
>1. "Parameter value" is the original value, instead of the URL encoded value.
>2. Any underscore in the Key of input parameter needs to be replaced with ".". But the underscore in Value does not. For example, `Placement_Zone=CN_GUANGZHOU` needs to be converted to `Placement.Zone=CN_GUANGZHOU`.

Then, join the formatted parameters together with`"&"`to generate the final request string (ignore the line breaks in the text):

```
Action=DescribeInstances
&InstanceIds.0=ins-09dx96dg
&Nonce=11886
&Region=ap-guangzhou
&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
&SignatureMethod=HmacSHA256
&Timestamp=1465185768
```

### 3. Construct the original signature string
This step is used to generate the original signature string.
The original signature string is constructed as follows:
> **Request method+Request CVM+Request path+?+Request string**

Description of parameters:
* **Request method:** The POST and GET methods are supported. In this case, a GET request is used. The methods must be in upper-case.
* **Request CVM: **The CVM domain name. The domain name for request varies with the product or product module to which the API belongs. For example, for Tencent Cloud CVM's API for querying instance list (DescribeInstances), the domain name for request is: `cvm.api.qcloud.com`. For more information on the domain names for requests in different products, please see the description of each API.
* **Request path:** This is the request path for the Tencent Cloud product corresponding to the API. Each product has a fixed path. For example, the request path for Tencent Cloud CVM is always `/v2/index.php`.
* **Request string:** The request string generated in the previous step.


The resulting original signature string in the above example is as follows (ignore the line breaks in the text):
```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
&InstanceIds.0=ins-09dx96dg
&Nonce=11886
&Region=ap-guangzhou
&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
&SignatureMethod=HmacSHA256
&Timestamp=1465185768
```

### 4. Generate the signature string
This step is to generate the signature string.
>**Note:** 
>You can compute a signature using two methods: HmacSHA256 and HmacSHA1. The signature string is generated with the signature algorithm you specified (parameter SignatureMethod). If you specify HmacSHA256 as SignatureMethod, the signature is computed using HmacSHA256. But in other cases, HmacSHA1 is used.

Sign the **original signature string** obtained in the previous step with signature algorithm (HmacSHA256 or HmacSHA1), and then encode the generated signature string with Base64 to obtain the final signature string.

In this example, PHP language is used and the signature algorithm is **HmacSHA256**. Therefore, the code for generating the signature string is as follows (If another programming language is used, the original signature string in the above example can be used for verification, as long as the signature string generated is the same as the one in the example):

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

Similarly, if you specify **HmacSHA1** as the signature algorithm, the code for generating the signature string is as follows:
```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Nonce=11886&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&SignatureMethod=HmacSHA1&Timestamp=1465185768';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:
```
nPVnY6njQmwQ8ciqbPl5Qe+Oru4=
```


## Encode the Signature String
The generated signature string cannot be directly used as the request parameter, and needs to be URL encoded.
For example, the signature string generated in the previous step `0EEm/HtGRr/VJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s=` is converted to `0EEm%2FHtGRr%2FVJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s%3D` after being encoded. The resulting request parameter for signature string (Signature) is `0EEm%2FHtGRr%2FVJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s%3D`, which will be used to generate the final request URL.
>**Note:**
>If GET method is used, all request parameters need to be URL encoded. In addition, some language libraries can encode URLs automatically. Repeated encoding will cause the failure of signature verification.

## Failure of Authentication
The errors that may occur when the authentication fails are listed below:

| Error Code | Error Type | Error Description |
|---------|---------|---------|
| 4100 | Authentication failed | Authentication failed. Make sure the Signature in your request parameters is computed correctly as described in the above steps. Be sure to encode the Signature with URL encoding before initiating the request. |
| 4101 | No access to this API | The sub-user is not authorized by the developer to call the API. Contact the developer for authorization. For more information, please see [Authorization Policy](/doc/product/378/4513). |
| 4102 | No access to the resources operated in the API | The user is not authorized by the developer to access some resource in the requested resources. Check the message field for the ID of the resource the user does not have access to.</br> Contact the developer for authorization. For more information, please see [Authorization Policy](/doc/product/378/4513). |
| 4103 | This API is unavailable for non-developer's SecretId | The sub-user with this SecretId cannot call this API. Only the developer has the access to this API. |
| 4104 | SecretId does not exist | The SecretId used for the signature does not exist, or the key status is incorrect. Make sure the API key is valid and enabled. |
| 4110 | Authentication failed | Permission verification failed. Make sure you have the access to this resource. |
| 4500 | Replay attack error | The parameter Nonce cannot be the same in two requests, and the difference between the Timestamp and Tencent server time should not be greater than 2 hours. |

