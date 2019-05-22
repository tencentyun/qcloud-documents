Tencent Cloud API authenticates each access request, so each request is required to include the Signature in the common request parameters for user identity authentication.
The signature is generated with user's security credentials, which consist of a SecretId and a SecretKey. If you don't have security credentials, apply for the credentials on the [Cloud API Key page](https://console.cloud.tencent.com/capi). Otherwise, you will not be able to call the cloud APIs.

## 1. Apply for Security Credentials
Before using Tencent Cloud's APIs for the first time, you need to apply for security credentials by going to [Cloud API Key](https://console.cloud.tencent.com/capi) page.
Security credential consists of a SecretId and a SecretKey, where:
> SecretId: Used to identify the API caller.
> SecretKey: Used for signature string encryption, and signature string verification by server.
> <font color='red'>The security credential must be kept confidential to avoid leakage.</font>

Apply for security credentials by following the steps below:

(1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/).

(2) Go to the [Cloud API Key ](https://console.cloud.tencent.com/capi) page.

(3) On the [Cloud API Key](https://console.cloud.tencent.com/capi) page, click **+Create Key** to create a pair of SecretId/SecretKey.

> <font color='red'>A developer account can have two pairs of SecretId/SecretKey at most.</br></font>


## 2. Generate the Signature String

With the SecretId and SecretKey, a signature string can be generated. The following shows how to generate a signature string:

Suppose that you have the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3EXAMPLE

**Note: This information is only for demonstration purpose. Make sure you proceed with your actual SecretId and SecretKey.**

For example, if you call the API "View CVM Instance List" (DescribeInstances), the possible request parameters are as follows:

| Parameter Name | Description | Parameter Value |
|---------|---------|---------|
| Action | Method name |  DescribeInstances |
| SecretId | Key ID |  AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE |
| Timestamp | Current timestamp |  1465185768 |
| Nonce | A random positive integer |  11886 |
| Region | The region where the instance resides |  ap-guangzhou |
| InstanceIds.0 | ID of the instance to be queried |  ins-09dx96dg |
| Offset | Offset | 0 |
| Limit | Maximum number of output results | 20 |
| Version | API version | 2017-03-12 |


### 2.1 Sort parameters

First, sort all the request parameters in an ascending lexicographical order (ASCII code) by their names. Notes: (1) Parameters are sorted by their names instead of their values; (2) The parameters are sorted in ASCII code order but not in an alphabetical order nor by values, for example, InstanceIds.2 should rank behind InstanceIds.12. You can complete the sorting process using relevant sorting functions in programming language, such as the ksort function in PHP. The parameters in the example are sorted as follows:

```
{
    'Action' : 'DescribeInstances',
    'InstanceIds.0' : 'ins-09dx96dg',
    'Limit' : 20,
    'Nonce' : 11886,
    'Offset' : 0,
    'Region' : 'ap-guangzhou',
    'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE',
    'Timestamp' : 1465185768,
    'Version': '2017-03-12',
}
```
Any other programming language can be used to sort these parameters as long as the same result is produced.

### 2.2. Generate the request string

This step is used to generate the request string.
Format the request parameters sorted in the previous step as "parameter name"="parameter value". For example, if the parameter value of "Action" is "DescribeInstances", the resulting format is Action=DescribeInstances.
**Note: "Parameter value" is the original value, instead of the URL encoded value.**

Then, join the formatted parameters together with "&" to generate the final request string:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.3. Generate the original signature string
This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

(1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Please note that the methods must be all in uppercase.
(2) Request CVM: The request domain name for View Instance List (DescribeInstances) is cvm.tencentcloudapi.com. The actual request domain name varies with the module to which the API belongs. For more information, please see the relevant API description.
3. Request path: The request path of the current version of cloud API is always /.
(4) Request string: The request string generated in the previous step.

The original signature string is constructed as follows:
> request method + request host + request path + ? + request string

The resulting string is:

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.4. Generate the signature string
This step is to generate the signature string.
Sign the **original signature string** obtained in the previous step using HMAC-SHA1 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

For example, the code is as follows if written in PHP:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3EXAMPLE';
$srcStr = 'GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:

```
EliP9YW3pW28FpsEdkXt/+WcGeI=
```

Any other programming language can be used as long as the signature generated is the same as the one in the example, which can be verified using the original signature string in the above example.

## 3. Encode the Signature String

The generated signature string cannot be directly used as the request parameter, and needs to be URL encoded.
**Note: If GET method is used, or if POST method is used and Content-Type is application/x-www-form-urlencoded, all request parameters need to be URL encoded. Non-ASCII characters should be encoded with UTF-8 before they can be URL encoded.**
For example, the signature string "EliP9YW3pW28FpsEdkXt/+WcGeI=" generated in the previous step is converted to the final signature string request parameter (Signature): "EliP9YW3pW28FpsEdkXt%2f%2bWcGeI%3d", which will be used to generate the final request URL.

## 4. Authentication Failure
The following authentication error codes may be returned depending on the actual situation.

| Error Code | Description |
|----------|---------|
| AuthFailure.SignatureExpire | Signature expired |
| AuthFailure.UnauthorizedOperation | Request failed to be authorized via CAM |
| AuthFailure.SecretIdNotFound | Key does not exist |
| AuthFailure.SignatureFailure | Invalid signature |
| AuthFailure.TokenFailure | token error |
| AuthFailure.MFAFailure | MFA error |
| AuthFailure.InvalidSecretId | Invalid key (it is not a cloud API key) |

## 5. Signature Demonstration

When calling the API 3.0 in practice, you should use the corresponding Tencent Cloud SDK 3.0 which encapsulates the signature process, so that you only need to focus on the specific APIs provided by the product during development. For more information, please see [SDK Center](https://cloud.tencent.com/document/sdk). The following programming languages are supported:

* [Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [JavaScript](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)

To make the signature process more clear, we use the Java language in the following example to implement the above signature process. The request domain name, the API and the parameters are all subject to the above signature process.

### Java

```java
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Random;
import java.util.TreeMap;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class TencentCloudAPIDemo {
    private final static String CHARSET = "UTF-8";

    public static String sign(String s, String key, String method) throws Exception {
        Mac mac = Mac.getInstance(method);
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(CHARSET), mac.getAlgorithm());
        mac.init(secretKeySpec);
        byte[] hash = mac.doFinal(s.getBytes(CHARSET));
        return DatatypeConverter.printBase64Binary(hash);
    }

    public static String getStringToSign(TreeMap<String, Object> params) {
        StringBuilder s2s = new StringBuilder("GETcvm.tencentcloudapi.com/?");
        // TreeMap is used to guarantee the lexicographic sorting order of parameters as required in the signature process.
        for (String k : params.keySet()) {
            s2s.append(k).append("=").append(params.get(k).toString()).append("&");
        }
        return s2s.toString().substring(0, s2s.length() - 1);
    }

    public static String getUrl(TreeMap<String, Object> params) throws UnsupportedEncodingException {
        StringBuilder url = new StringBuilder("https://cvm.tencentcloudapi.com/?");
        // It is not necessary to sort parameters in the actual request URL.
        for (String k : params.keySet()) {
            // The request string should be URL-encoded. Since the key is comprised of letters only, its value must be URL-encoded.
            url.append(k).append("=").append(URLEncoder.encode(params.get(k).toString(), CHARSET)).append("&");
        }
        return url.toString().substring(0, url.length() - 1);
    }

    public static void main(String[] args) throws Exception {
        TreeMap<String, Object> params = new TreeMap<String, Object>(); // TreeMap can realize auto-sorting
        // A random number should be used for the actual call, for example: params.put("Nonce", new Random().nextInt(java.lang.Integer.MAX_VALUE));
        params.put("Nonce", 11886); // Common parameters
        // The current system time should be used for the actual call, for example: params.put("Timestamp", System.currentTimeMillis() / 1000);
        params.put("Timestamp", 1465185768); // Common parameters
        params.put("SecretId", "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"); // Common parameters
        params.put("Action", "DescribeInstances"); // Common parameters
        params.put("Version", "2017-03-12"); // Common parameters
        params.put("Region", "ap-guangzhou"); // Common parameters
        params.put("Limit", 20); // Business parameters
        params.put("Offset", 0); // Business parameters
        params.put("InstanceIds.0", "ins-09dx96dg"); // Business parameters
        params.put("Signature", sign(getStringToSign(params), "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE", "HmacSHA1")); // Common parameters
        System.out.println(getUrl(params));
    }
}
```

The resulting URL: `https://cvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Signature=EliP9YW3pW28FpsEdkXt%2F%2BWcGeI%3D&Timestamp=1465185768&Version=2017-03-12`

Note: Since the key in the example is fictitious and the timestamp is not the current system time, the authentication error "The signature expired" will be returned when you open this URL in a browser or call it with a command, such as curl. To get a URL that can be returned normally, replace the SecretId and SecretKey in the example with the real key, and use the current system timestamp as the Timestamp.

