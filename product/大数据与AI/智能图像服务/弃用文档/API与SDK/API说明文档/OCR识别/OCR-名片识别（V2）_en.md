## Overview

The business card OCR is used to return identified field information based on the business card image uploaded by a user. More than 20 fields can be identified, as shown below:

Name, Title, Department, Company, Address, Zip code, Email, Website, Mobile, Tel, Fax, QQ, MSN, WeChat, Weibo, Company account, logo, and others.

>Note: If the developer is using V1, please see [Business Card OCR (V1)](/document/product/641/12423).


## Calling URL

Both HTTP and HTTPS protocols are supported:

`http://recognition.image.myqcloud.com/ocr/businesscard`

> Note: There may be more than one item for each field. The actually returned contents depend on the card content.

## HTTP Request Format

This OCR API uses http protocol and supports specifying image URL and uploading local image files.

### Header Information

| Parameter Name | Value | Description |
| -------------- | --------------------------------------- | ---------------------------------------- |
| Host | recognition.image.myqcloud.com | Tencent cloud intelligent image recognition server domain name |
| Content-Length | Total length of the packet | Total length of the entire request packet in Bytes |
| Content-Type | application/json or multipart/form-data | Choose based on APIs |
| Authorization | Authentication signature | Multiple valid signatures for authentication. For more information about the method for generating authentication signatures, please see [Authentication Signature](/document/product/641/12409) |

> Notes: 
> (1) Each request packet should not exceed 6 MB.
> (2) All APIs use the POST method.
> (3) Animations like .gif are not supported.

### Request Parameter

| Parameter Name | Required | Type | Description |
| ------------- | ----------- | ------------- | ---------------------------------  |
| appid | Required | string | AppId applied on Tencent cloud |
| bucket | Optional | string | Image space |
| image | Required | image/jpeg, etc. | Image files. Multiple files can be specified at the same time. The parameter name must be a string beginning with "image", such as "image[0]", "image[1]". The strings are sorted in lexicographical order in the response http body. A filename must be specified for each image, whose value can be empty. The response http body will return the filename value set by the user. |
| url_list | Required | String array | List of image URLs. You need to enter either image or URL. If both of them are entered, URL should prevail. |

### Example - Using URL

```
POST /ocr/businesscard HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 187
Content-Type: application/json

{
  "appid":"123456",
  "bucket":"test",
  "url_list":["http://yoututest-1251966477.cossh.myqcloud.com/mingpian.jpg"]
}
```

### Example - Using Image File

```
POST /ocr/businesscard HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 735
Content-Type: multipart/form-data;boundary=--------------acebdf13572468

----------------acebdf13572468
Content-Disposition: form-data; name="appid";

123456
----------------acebdf13572468
Content-Disposition: form-data; name="bucket";

test
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="mingpian.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```


## Returned Value
### Response

| Field | Type | Description |
| ----------- | ------- | ------------ |
| result_list | json array | As described in the following table |

result_list (json array) is composed as follows:

| Field | Type | Description |
| ------- | ------ | ------------ |
| code | int | Server error code. 0: successful |
| message | string | Message returned by server |
| url | string | If URL is selected as the request parameter, the URL of the current image is returned |
| filename | string | If image is selected as the request parameter, the filename of the current image is returned |
| data | array (item) | As described in the following table |

Field data is composed as follows:

item description

| Field | Type | Description |
| ---------------- | ------ | ---------------------- |
| item | string | Field string |
| value | string | The identified field information |
| confidence | double | The confidence level of the identified field information. Value range: [0.0, 1.0]. |

### Example

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "filename": "Business card 2.jpg",
            "data": [
                {
                    "item": "Name",
                    "value": "Wen Xingtao",
                    "confidence": 0.9994000196456908
                },
                {
                    "item": "Title",
                    "value": "Senior Solution Architect",
                    "confidence": 0.9758999943733216
                },
                {
                    "item": "Department",
                    "value": "Cloud Product Department",
                    "confidence": 0.9998999834060668
                },
                {
                    "item": "Company",
                    "value": "Tencent",
                    "confidence": 0.8555999994277954
                },
                {
                    "item": "Address",
                    "value": "F1, Building A, Tencent Building Of ChengDu, No. 198, Tianfu 3rd Street, Hi-tech District, Chengdu, 610041",
                    "confidence": 0.5228000283241272
                },
                {
                    "item": "Email",
                    "value": "timwen@tencent.com",
                    "confidence": 0.9995999932289124
                },
                {
                    "item": "Mobile",
                    "value": "+86-18109023170",
                    "confidence": 0.9914000034332277
                },
                {
                    "item": "Tel",
                    "value": "9761758",
                    "confidence": 0.9998999834060668
                },
                {
                    "item": "Tel",
                    "value": "+86-28-85225111 Ext 51468",
                    "confidence": 0.9078999757766724
                },
                {
                    "item": "Fax",
                    "value": "+86-28-85980512",
                    "confidence": 0.9944000244140624
                }
            ]
        }
    ]
}
```


## Error Codes
| Error Code | Description |
| ----- | -------------------------- |
| 3 | Incorrect request |
| 4 | Signature is empty |
| 5 | Incorrect signature string |
| 6 | The appid/bucket in the signature does not match the target |
| 9 | Signature expired |
| 10 | appid does not exist |
| 11 | secretid does not exist |
| 12 | appid and secretid do not match |
| 13 | Replay attack |
| 14 | Signature verification failed |
| 15 | Operation performed too frequently. Frequency control triggered |
| 16 | Bucket does not exist |
| 21 | Invalid parameter |
| 23 | Oversized request packet |
| 24 | No permissions |
| 25 | The purchased resources run out |
| 107 | Internal error of authentication service |
| 108 | Authentication service is unavailable |
| 213 | Internal error |
| -1102 | Image decoding failed |
| -1300 | Image is empty |
| -1301 | Parameter is empty |
| -1304 | Parameter is too long |
| -1308 | Failed to download image |
| -5201 | Insufficient text on your card |
| -5202 | Tilt angle of text line is too large |
| -5203 | Business card is obscure|
| -5204 | Failed to recognize the name on the business card |
| -5205 | Failed to recognize the phone number on the business card |
| -5206 | The uploaded image is not a business card |
| -5207 | Detection or recognition failed |
| -5208 | Internal error in business card OCR service |


For more information on other API error codes, please see [**Error Codes**](/document/product/641/12410).
