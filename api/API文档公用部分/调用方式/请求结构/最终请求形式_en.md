### Construction Rule
The construction rule for Tencent Cloud API request URLs:
> **https:// + request domain name + request path + ? +final request parameter string**

Component description:
-  **Request domain name:** The request domain name is determined by the product or the product module to which the API belongs. This domain name varies with different products or product modules. For example, the request domain name for Tencent Cloud CVM API for querying instance lists (DescribeInstances) is: `cvm.api.qcloud.com`. For more information on product request domain names, please see the description for each API.
-  **Request path:** This is the request path for the corresponding Tencent Cloud API product. Each product usually corresponds to one fixed path. For example, the request path for Tencent Cloud CVM is always `/v2/index.php`.
- **Final request parameter string:** The API request parameter string includes common request parameters and API request parameters.

### Example
The format of a final request URL for Tencent Cloud API is as follows:
Take the Tencent Cloud CVM API [Query Instance List](/doc/api/229/831) (DescribeInstances) as an example, the first 6 parameters are common request parameters, while the last 6 ones are API request parameters.

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

