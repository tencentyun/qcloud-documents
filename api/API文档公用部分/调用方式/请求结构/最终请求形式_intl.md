### Construction Rule
A Tencent Cloud API request URL is constructed as follows:
> **https://+request domain name+request path+?+final request parameter string**

The elements of each URL are described as follows:
-  **Request domain name:** It varies with the product or product module to which the API belongs. For example, the request domain name for the Tencent Cloud CVM API for querying instance list (DescribeInstances) is: `cvm.api.qcloud.com`. For more information about the request domain names for different products, see the relevant API documents.
-  **Request path:** The request path for the product to which the Tencent Cloud API belongs. Each product has a fixed path. For example, the request path for Tencent Cloud CVM is always `/v2/index.php`.
- **Final request parameter string:** The API request parameter string consists of common request parameters and API request parameters.

### Use Case
The final request URL for a Tencent Cloud API is as follows:
Taking the Tencent Cloud CVM API [Query Instance List](/doc/api/229/831) (DescribeInstances) as example, the first 6 parameters are common request parameters, and the last 6 ones are API request parameters.

```
https://cvm.api.qcloud.com/v2/index.php?
Action=DescribeInstances
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature       //Common request parameters
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003      //API request parameters
```

