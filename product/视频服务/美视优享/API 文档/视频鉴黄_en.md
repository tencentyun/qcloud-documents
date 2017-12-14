Developers can try Porn Detection out on [Try-out Platform](http://cloud.tencent.com/event/pd). Account registration is not required on the platform.

## Basic Concepts

| Concept     | Description               |
| ------ | ---------------- |
| appid  | Project ID that uniquely identifies the accessing project |
| bucket | Name of the space added by developer       |

> **Note:**
> If the developer is using V1, appid is the APPID generated with the version.

## Description

Porn Detection API uses HTTP protocol and supports multiple URLs and local images, with a maximum of 20 images or URLs supported for each request.
**API:**  `http://service.image.myqcloud.com/detection/porn_detect`
**Method:**  POST

## Porn Detection for Images/URLs

### Request syntax


```
POST /detection/porn_detect HTTP/1.1
Authorization: Signature
Host: service.image.myqcloud.com
Content-Length: ContentLength
Content-Type: "application/json"

{
    "appid": "appid",
    "bucket": "bucket",
    "url_list": [
        "url",
        "url"
    ]
}
```

**HTTP header of request packet:**

| Parameter             | Required | Description                              |
| -------------- | ---- | ------------------------------- |
| Host           | Yes    | Access domain name: service.image.myqcloud.com |
| Authorization  | Yes    | Authentication signature. For more information, see [Authentication](https://cloud.tencent.com/document/product/275/3805)                  |
| Content-Type   | Yes    | Standard application/JSON             |
| Content-Length | Yes    | Total length of HTTP body                    |

**HTTP body of request packet:**

| Parameter     | Required | Type     | Description      |
| ------ | ---- | ------ | ------- |
| appid  | Yes   | Uint  | Business ID |
| bucket | Yes  | String | Image space  |
| url   | Yes  | String | List of image URLs |

### Response

**HTTP body of response (in JSON format):**

| Parameter     | Required | Type     |
| ----------- | ------ | ------------ |
| result_list | JSON array | As described in the following table |

**result_list (JSON array) is composed as follows:**

| Parameter      | Type     | Description           |
| ------- | ------ | ------------ |
| code | Int | Server error code. 0: successful |
| message | String | Message returned by server |
| url      | String | URL of the current image    |
| data    |        | As described in the following table |

**Field data is composed as follows:**

| Parameter      | Type     | Description           |
| ------------- | ------ | ---------------------------------------- |
| result        | Int    | Identification result for reference. 0: normal; 1: pornographic; 2: suspected |
| confidence    | Double | |Confidence for the image to be identified as pornographic. Range: 0-100. It is an overall score derived from normalScore, hotScore and pornScore |
| normal_score |Double | Score for normal images                               |
| hot_score     | Double | Score for sexy images                               |
| porn_score    | Double | Score for pornographic images                              |
| forbid_status | Int    | Blocked or not. 0: normal; 1: blocked (only the images stored in Cloud Image can be blocked)  |

> **Notes:**
> 1. When result=0, the image is normal.
> 2. When result= 1, the image is identified as a 100% prohibited image; if the image is stored in Cloud Image, it will be directly blocked.
> 3. When result=2, the image is a suspected one (it is likely to be a pornographic image). Currently, any image with a confidence between 83 and 91 (inclusive) is identified as suspected.

### Example

**HTTP request:**

```
POST /detection/porn_detect HTTP/1.1
Authorization: FCHXddYbhZEBfTeZ0j8mn9Og16JhPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJiUkp3Sk5zbTN3V1lEeHN1JnQ9MTQ2ODQ3NDY2MiZyPTU3MiZ1PTAmYj10ZXN0YnVja2V0JmU9MTQ3MTA2NjY2Mg==
Host: service.image.myqcloud.com
Content-Length: 238
Content-Type: "application/json"

{
    "appid": 10000379,
    "bucket": "testbucket",
    "url_list": [
        "http://www.bz55.com/uploads/allimg/140805/1-140P5162300-50.jpg",
        "http://img.taopic.com/uploads/allimg/130716/318769-130G60P30462.jpg"
    ]
}
```

**HTTP body of response (in application/JSON format):**

```
{
    "result_list": [
        {
            "code": 0,
            "message": "success",
            "url": "http://www.bz55.com/uploads/allimg/140805/1-140P5162300-50.jpg",
            "data": {
                "result": 0,
                "forbid_status": 0,
                "confidence": 12.509,
                "hot_score": 87.293,
                "normal_score": 12.707,
                "porn_score": 0.0
            }
        },
        {
            "code": 0,
            "message": "success",
            "url": "http://img.taopic.com/uploads/allimg/130716/318769-130G60P30462.jpg",
            "data": {
                "result": 0,
                "forbid_status": 0,
                "confidence": 14.913,
                "hot_score": 99.997,
                "normal_score": 0.003,
                "porn_score": 0.0
            }
        }
    ]
}
```

## Porn detection for image files

**Description: **In porn detection for image files, one or more files are uploaded using HTML forms, with file content encoded in multiple forms (multipart/form-data).

### Request Syntax

```
POST /detection/porn_detect HTTP/1.1
Content-Type: multipart/form-data;boundary=-------------------------acebdf13572468
Authorization: Signature
Host: service.image.myqcloud.com
Content-Length: ContentLength

---------------------------acebdf13572468
Content-Disposition: form-data; name="appid";

appid
---------------------------acebdf13572468
Content-Disposition: form-data; name="bucket";

bucket
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[0]"; filename="image _1.jpg"
Content-Type: image/jpeg

image_content
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[1]"; filename="image _2.jpg "
Content-Type: image/jpeg

image_content
---------------------------acebdf13572468--
```

**HTTP header of request packet:**

| Parameter             | Required | Description                              |
| -------------- | ---- | ------------------------------- |
| Host           | Yes    | Access domain name: service.image.myqcloud.com |
| Authorization  | Yes    | Authentication signature. For more information, see [Authentication](https://cloud.tencent.com/document/product/275/3805)    |
| Content-Type   | Yes    | Standard application/JSON             |
| Content-Length | Yes    | Total length of HTTP body                    |

**Form fields: **

| Parameter     | Required | Type         | Description                                       |
| ------ | ---- | ---------- | ---------------------------------------- |
| appid | Yes    | Uint       | Business ID |
| bucket | Yes    | String     | Image space                                     |
| image  | Yes    | Image/Jpeg | Image file. Multiple files are supported. The parameter name must be `image[0]`, `image[1]`, etc. A filename needs to be specified for each image. |

### Response

**HTTP body of response (in JSON format):**

| Parameter      | Type     | Description           |
| ----------- | ------ | ------------ |
| result_list | JSON array | As described in the following table |

**result_list (JSON array) is composed as follows:**

| Parameter      | Type     | Description           |
| -------- | ------ | ----------------------------- |
| code | Int | Server error code. 0: successful |
| message | String | Message returned by server |
| filename | String | Filename of the current image. It is identical to the one in request packet |
| data    |        | As described in the following table |

**Field data is composed as follows:**

| Parameter      | Type     | Description           |
| ------------- | ------ | ---------------------------------------- |
| result        | Int    | Identification result for reference. 0: normal; 1: pornographic; 2: suspected |
| confidence    | Double | |Confidence for the image to be identified as pornographic. Range: 0-100. It is an overall score derived from normalScore, hotScore and pornScore |
| normal_score |Double | Score for normal images                               |
| hot_score     | Double | Score for sexy images                               |
| porn_score    | Double | Score for pornographic images                              |
| forbid_status | Int    | Blocked or not. 0: normal; 1: blocked (only the images stored in Cloud Image can be blocked)  |

> **Notes:**
> 1. When result=0, the image is normal.
> 2. When result=1, the image is identified as a prohibited one.
> 3. When result=2, the image is a suspected one (there is a high probability that it is pornographic). Currently, any image with a confidence between 83 and 91 (inclusive) is identified as suspected.

### Example

**HTTP request:**

```
POST /detection/ porn_detect HTTP/1.1
Content-Type:multipart/form-data;boundary=-------------------------acebdf13572468
Authorization:FCHXddYbhZEBfTeZ0j8mn9Og16JhPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJiUkp3Sk5zbTN3V1lEeHN1JnQ9MTQ2ODQ3NDY2MiZyPTU3MiZ1PTAmYj10ZXN0YnVja2V0JmU9MTQ3MTA2NjY2Mg==
Host: service.image.myqcloud.com
Content-Length: 61478

---------------------------acebdf13572468
Content-Disposition: form-data; name="appid";

10000379
---------------------------acebdf13572468
Content-Disposition: form-data; name="bucket";

testbucket
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[0]"; filename="1.jpg"
Content-Type: image/jpeg

<@INCLUDE *D:\185839ggh0oedgnog04g0b.jpg.thumb.jpg*@>
---------------------------acebdf13572468
Content-Disposition: form-data; name="image[1]"; filename="2.jpg"
Content-Type: image/jpeg

<@INCLUDE *D:\200132svnmybmhbmmgbmga.jpg.thumb.jpg*@>
---------------------------acebdf13572468
```

**HTTP body of response (in application/JSON format):**

```
{
    "result_list": [
        {
            "code": 0,
            "message": "success",
            "filename": "1.jpg",
            "data": {
                "result": 1,
                "forbid_status": 0,
                "confidence": 96.853,
                "hot_score": 0.0,
                "normal_score": 0.0,
                "porn_score": 100.0
            }
        },
        {
            "code": 0,
            "message": "success",
            "filename": "2.jpg",
            "data": {
                "result": 0,
                "forbid_status": 0,
                "confidence": 41.815,
                "hot_score": 19.417,
                "normal_score": 0.077,
                "porn_score": 80.506
            }
        }
    ]
}
```

##Error Codes

| Error Code | Description |
| ----- | ----------------------------------- |
| 3     | Incorrect request                               |
| 4     | Signature is empty                                |
| 5     | Incorrect signature string                               |
| 6     | APPID/bucket/URL does not match                 |
| 7     | Failed to encode signature (internal error)                        |
| 8     | Failed to decode signature (internal error)                        |
| 9     | Signature expired                               |
| 10    | APPID does not exist                            |
| 11    | SecretId does not exist                         |
| 12    | APPID does not match                            |
| 13    | Replay attack                                |
| 14    | Signature failed                                |
| 15    | Operation performed too frequently. Frequency control triggered                          |
| 16    | Internal error                                |
| 17    | Unknown error                                |
| 200   | Internal packing failed                              |
| 201   | Internal unpacking failed                               |
| 202   | Internal link failed                              |
| 203   | Internal processing timed out                              |
| -1300 | Image is empty                                |
| -1308 | Failed to download image with URL                           |
| -1400 | Invalid image format                             |
| -1403 | Failed to download image                             |
| -1404 | Unable to recognize image                              |
| -1505 | Incorrect URL format                             |
| -1506 | Image download timed out                              |
| -1507 | Unable to access the image server the URL points to                    |
| -5062 | The image the URL points to has been marked as inappropriate and cannot be accessed (only for the images stored in Tencent Cloud) |
