## Types of Server APIs:
There are two types of Tencent Cloud VOD server APIs:
1. Common server APIs: All request parameters are in UTF-8 characters. These APIs follow the general Tencent Cloud API specification and can use Tencent Cloud standard server SDK;
2. APIs for data uploading: Request content contains binary data. These APIs cannot use Tencent Cloud standard SDK, VOD service provides specialized server SDK to simplify the calling process.

## Request Structure (Common Server APIs)

### Service Domain
vod.api.qcloud.com.

### Communication Protocol
HTTPS.

### Request Method
POST and GET requests are both supported, but cannot be used at the same time. This means that:
1. If you use GET method, all parameters need to be passed via QueryString;
2. If you use POST method, all parameter are acquired from RequestBody, parameters in QueryString will be ignored;
3. Parameter format rule is the same for these two methods;
4. Generally, GET method is recommended. If the parameter strings are too long, POST method is recommended.

### Character Encoding
The UTF-8 encoding is always used.

### Server SDK
To simplify the calling process and to avoid complicated authentication parameter generation, it is recommended for developers to use server SDK to initiate the calling process.

## Request Structure (Data Upload APIs)

### Service Domain
Vod2.qcloud.com

### Communication Method
HTTP/HTTPS.

### Request Method
POST

### Server SDK
Common server API oriented SDK cannot be used to upload binary data. For this reason, we provide specialized SDK for local video uploading. Refer to Local Video Upload for details.

## Common Parameters
Common parameters are used for user identification and API authentication. Unless it's necessary, these parameters will not be described in API descriptions. The parameters must be carried in each request in order to successfully initiate the request.

Common server APIs and data upload APIs all have the same common parameters.

| Name | Type | Description | Required |
|---------|---------|---------|---------|
| Action | String | Name of the API command, for example:  DescribeClass | Yes |
| Region | String | Region parameter, used to identify the region to which the instance you want to operate belongs. See the section below for available values. You can enter "gz" for VOD service | Yes |
| Timestamp | UInt | The current UNIX timestamp | Yes |
| Nonce | UInt | A random positive integer that is used in conjunction with Timestamp to prevent replay attacks. | Yes |
| SecretId | String | SecretId and SecretKey that are applied for from Tencent Cloud platform, used for identification. SecretKey will be used to generate Signature. Refer to the [API Authentication](/doc/api/257/接口鉴权 "接口鉴权") page for details | Yes |
| Signature | String | Request signature, used to verify the validity of the request. Refer to the [API Authentication](/doc/api/257/接口鉴权 "接口鉴权") page for details | Yes |

The available values for "Region" in Tencent Cloud are as follows:

| Region | Region |
|---------|---------|
| bj | Beijing |
| gz | Guangzhou |
| sh | Shanghai |
| hk | Hong Kong |
| ca | North America |

Here's a typical API request: Action=DescribeVodPlayUrls. It means to acquire detailed information of the video.

```
https://vod.api.qcloud.com/v2/interface.php?Action=DescribeVodPlayUrls
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&fileId=1234567
```
Here, fileID is a command parameter which belongs to this API. The rest are common parameters.

## API Response
Unless otherwise specified, the returned value of each request will contain the following fields:

| Name | Type | Description |
|---------|---------|---------|---------|
| code | Int | Returned error code. 0 indicates success, while any other values indicate failure. For detailed meanings of error codes, refer to the Error Codes page |
| message | String | Request result |

For example, the possible result for calling the above API is shown below:

```
{
    "code": 0,
    "message": "",
    "playSet": [
        {
            "url": "http://vcloud1200.tc.qq.com/1200_5b9688d481d8b811095d30a78cf44c4285026a4c.f0.mp4",
            "definition": 0,
            "vbitrate": 2332000,
            "vheight": 576,
            "vwidth": 1024
        }
    ]
}
```

