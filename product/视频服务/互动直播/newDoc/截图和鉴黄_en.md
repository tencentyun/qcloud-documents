## Feature Description

* ILVB platform provides two services: Screenshot and Porn Detection. You can enable them based on your needs.<br/>
Screenshot:<br/>
This service captures user uplink data (including data from camera and screen sharing) as screenshots and store them. You can send the download links for these screenshots to users via screenshot callback.<br/>
Porn detection:<br/>
This service calls the Tencent Cloud Image service to detect porn content from stored screenshots and scores them, while notifying users about screenshots containing porn content through porn detection callback.
* When you enable porn detention service, the big screen monitor display feature will also be enabled by default. Log in to [Monitor Backend](http://jh.live.qcloud.com/) to view the displayed images and relevant porn detection information.

## Console Configuration

#### 1. Enable Service 

![](https://mc.qcloudimg.com/static/img/5f583de77788f98af47b60a9553c14b5/1.png)

From the ILVB console, find the sdkappid for which you want to enable screenshot porn detection service and click **Application Configuration** to go to **Porn Detection Configuration** page.<br/>
The service is disabled by default. Click **Edit** to see the enable switch. When the service is enabled, the system automatically creates a pair of keys (secretId and secretKey) used for generating signature.

##### 1.1 Enable Screenshot Feature

![](https://mc.qcloudimg.com/static/img/b70f58eba309927a1c27e823f53e8bcc/2.png)

By default, a user must provide screenshot callback address when enabling screenshot feature only. For more information on how to use screenshot callback, please see section 2.1. Default screenshot capture frequency is 10 seconds. Four options will because available in the future (5s/10s/30s/60s). After you have entered the information, check the **I agree to the 'Tencent Cloud Terms of Service'** and click **OK** to enable screenshot feature.

##### 1.2 Enable Screenshot and Porn Detection

By default, a user must provide porn detection callback address when enabling porn detection feature. For more information on how to use porn detection callback, please see section 3.1.<br/>
The user can determine whether screenshot callback and operation callback (used to ban rooms) are required. You can leave the corresponding address empty if it is not needed.<br/>
After you have entered the information, check the **I agree to the 'Tencent Cloud Terms of Service'** and click **OK** to enable screenshot and porn detection feature.

#### 2. Acquire Screenshots
Currently, screenshots can only be acquired via screenshot callback.

##### 2.1 Screenshot Callback Service

##### (1) Description
Screenshot callback service actively calls back stored screenshot information (user name, room number, download link and so on) to user according to the screenshot callback address provide by the user.

##### (2) API Description
Protocol: HTTP<br/>
Domain Name: (Callback domain name provided by user)<br/>
Request Type: POST<br/>
Data Format: JSON<br/>

* Request Parameters

Parameter Name  | Required  | Type |  Description
:-----: | :-----: | :-----: |:-----: 
userid | Yes | string | Username` (encoded using base64, after which the special character "$" is replaced by "$1", and "\" is replaced by "$2")`
groupnum | Yes | UInt | Room number
sdkappid | Yes | UInt | sdkappid
filename | Yes | string | File name
url | Yes | string | Image download link
timestamp | Yes | string | Timestamp
sign | Yes | string | Request signature. See appendix for how to calculate signature

* Response Parameters

Parameter Name  |  Type |  Description
:-----: | :-----: |:-----: 
code | UInt | 0: Successfully received. 1: Process failed

* Example

Request

```
{
   "userid": "dXNlcjE",
   "groupnum": 123456,
   "sdkappid": 1400000000
   "filename": "dXNlcjE_123456_1400000000_1481701566.jpg",
   "url": "http://xxx.com/ab_140000000/20161214/dXNlcjE/15/dXNlcjE_123456_1400000000_1481701566.jpg",
   "timestamp": "1481701566",
   "sign": "e22fd6bcb979d78933acdc5863f0334a"
}
```

Response

```
{
    "code": 0
}
```

#### 3. Acquire Auto Porn Detection Result

##### 3.1 Porn Detection Callback Service

##### (1) Description

The porn detection callback service actively calls back suspicious image information (user name, room number, download link and so on) detected by Cloud Image service to user according to the porn detection callback address provided by the user.

##### (2) API Description

Protocol: HTTP<br/>
Domain Name: (Callback domain name provided by user)<br/>
Request Type: POST<br/>
Data Format: JSON<br/>

* Request Parameters<br/>
HTTP header<br/>
Porn detection callback includes HMAC-SHA1 signature in its HTTP request header. The signature is used for passing identity verification information, users can perform authentication by verifying this signature. The HTTP request header contains the following three parameters:

Parameter Name  |  Required |  Type | Description
:-----: | :-----: |:-----: | :-----:
TPD-SecretID | Yes | string | secretId used to generate signature
TPD-CallBack-Auth | Yes | string | Signature calculated by using HMAC-SHA1 algorithm. See appendix for calculation method
TPD-CallBack-Version | Yes | string | Version number of callback protocol. The current protocol version is v2

HTTP body<br/>

Parameter Name  |  Required |  Type | Description
:-----: | :-----: |:-----: | :-----:
userid | Yes | string | Username` (encoded using base64, after which the special character "$" is replaced by "$1", and "\" is replaced by "$2")`
roomId | Yes | UInt | Room number
img | Yes | string | Image download link
type | Yes | Array | Image type.  Porn detection result determined by the service.  0: Normal image. 1: Porn image. 2: Hot image. 4: OCR-identified malicious content 
confidence | Yes | Number | Confidence level for the image to be considered as porn. Range: 0-100. An overall score based on normalScore, hotScore, pornScore. Images with a confidence above 83 are considered as suspicious images
normalScore | Yes | Number | Score for normal images
hotScore | Yes | Number | Score for hot images
pornScore | Yes | Number | Score for porn images
level | Yes | Number | Image level
ocrMsg | Yes || OCR identification information for image (if available)
screenshotTime | Yes | Number | Screenshot time (UNIX timestamp. Unit: second)
sendTime | Yes | Number | Time when request was sent (UNIX timestamp. Unit: second) 
abductionRisk | Yes | Array | An array containing AbductionRisk structure

* Response Parameters

Parameter Name  |  Type |  Description
:-----: | :-----: |:-----: 
code | UInt | 0: Successfully received. 1: Process failed. 2: Incorrect signature

* Example

HTTP header format:<br/>

```
        "TPD-SecretID": AYID5JH4f1rYNT1XzIjTMCQCg9QZ
        "TPD-CallBack-Auth": sSOna1XcIDwgNRSm1b3D6scfFJk=
        "TPD-CallBack-Version": v2
```
Input data format:

```
    {
        "id": 20001,
        "roomId" : 234,
        "userid": "VXNlcg==",
        "img" : "http://dasdas.***.888",
        "type" : [1],
        "confidence" : 10,
        "normalScore": 0,
        "pornScore": 100,
        "hotScore": 0,
        "level" : 0,
        "screenshotTime" : 1477366280,
        "ocrMsg":""
        "sign" : "XXXXX" 
        "sendTime":1481010889,
        "abductionRisk":[  
            {  
                "level":4,   /*Risk level*/
                "type":2001  /*Risk type*/
            },
            {  
                "level":3,
                "type":2002
            }
        ]
    }
```

Response

```
{
    "code": 0
}
```

#### 4. Use Big Screen Monitor Feature

Big screen monitor feature is enabled by default when user enables porn detection. Log in to [Monitor Backend](http://jh.live.qcloud.com/) to view screenshots and non-interactive stream display (non-interactive stream push must be initiated) of LVB users from the big screen monitor. You can sort the displays based on suspicion level.

##### 4.1 View Images

Select **Image View** as viewing method.

##### 4.2 View Videos

Select **Video View** as viewing method.

#### 5. Price

Screenshot and porn detection are paid services. Screenshot service: 0.1 CNY per thousand images; porn detection service: 1.3 CNY per thousand images.  [Billing Details](https://cloud.tencent.com/document/product/268/5129#3..E6.88.AA.E5.9B.BE.E9.89.B4.E9.BB.84.E5.8A.9F.E8.83.BD.E8.AE.A1.E8.B4.B9)


### Appendix

#### Callback Signature Calculation Method

1. Acquire the original string from the HTTP request body
2. Acquire callback secret key (secretKey) from the console
3. Use the secretKey to calculate signature for the original string obtained in step 1, via HMACSHA1 algorithm
4. Use base64 to encode the generated binary signature string to acquire the final signature

For example:
Assume that we acquired the following body from HTTP request:

```json
{"sendTime":1481010889,"tid":20001,"roomId":234,"userId":"TestUser","img":"http://dasdas.***.888","type":[1],"confidence":10,"normalScore":0,"pornScore":100,"hotScore":0,"level":0,"screenshotTime":1477366280,"ocrMsg":"","abductionRisk":[{"level":4,"type":2001},{"level":3,"type":2002}]}
```

The following example shows how to calculate signature with PHP.

```php
$secret_key='6zkty7DvD8vfG3XEkV21VKV8Qpqh6SZK'
$jsonBody='{"sendTime":1481010889,"tid":20001,"roomId":234,"userId":"TestUser","img":"http://dasdas.***.888","type":[1],"confidence":10,"normalScore":0,"pornScore":100,"hotScore":0,"level":0,"screenshotTime":1477366280,"ocrMsg":"","abductionRisk":[{"level":4,"type":2001},{"level":3,"type":2002}]}'
$signature = base64_encode(hash_hmac('SHA1',$jsonBody,$secret_key, true));
```

The final signature is acquired.

#### Cloud Image Smart Porn Detection Scoring System

Normal image score:  Range: 0-100. Normal image probability score determined by Cloud Image. A higher score indicates that the image conforms to normal image standards better;<br/>
Hot image score:  Range: 0-100.  Hot image probability score determined by Cloud Image. A higher score indicates that the image has a higher sexy level;<br/>
Porn image score:  Range: 0-100.  Hot image probability score determined by Cloud Image. A higher score indicates that the image has a higher porn level;<br/>
Porn image confidence level:  Range: 0-100.  Overall score based on the three scores mentioned above. A score above 83 means the image is suspicious;<br/>
It is recommended to use porn image confidence level to determine porn images.


