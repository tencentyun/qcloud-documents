## Overview
This API is used to detect the liveness of a face in a static photo uploaded by a user. Compared with dynamic liveness detection, static liveness detection does not require moving lips, shaking head, or winking for recognition.

## Billing
This service is under free public trial and will be charged from January 1, 2018.
For more information, please see [Billing](/document/product/641/12401).


## Description
| Concept     | Description               |
| ------ | ---------------- |
| appid | Project ID, the unique identifier for the accessed project |
><font color="#0000cc">**Note:** </font>
 If the developer is using V1, appid is the appid generated with the version.

## API Form

Protocols: http and https are supported.

API: `http://recognition.image.myqcloud.com/face/livedetectpicture`
API: `https://recognition.image.myqcloud.com/face/livedetectpicture`


## header of Request Packet
This API uses http protocol and supports specifying image URL and uploading local image files.
All requests must contain the header information listed in the following table:

| Parameter Name | Value | Description |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host | recognition.image.myqcloud.com | Server domain name |
| Content-Length | Total length of the packet | Total length of the entire request packet in Bytes |
| Content-Type | application/json or multipart/form-data | Choose based on APIs |
| Authorization | Authentication signature | Signature for [**Authentication**](/document/product/641/12409) |

><font color="#0000cc">**Notes:** </font>
 (1) Each request packet should not exceed 6 MB.
 (2) All APIs use the POST method.
 (3) Animations like .gif are not supported.

## Request Parameters
If image is used, the multipart/form-data format will be applied. Otherwise, the application/json format is applied.

| Parameter Name | Required | Type | Description |
| ------------- | ---- | ------ | ------------------------------------- |
| appid | Required | string | Project ID |
| image | Optional | binary | Image content |
| url | Optional | string | You can provide either the image or URL. If both of them are provided, URL should prevail. |

## Response
| Field | Type | Description |
| --------------- | ------ | ------------------------- |
| data.score | Int | Liveness score. Value range: [0, 100]. It is recommended to set the liveness threshold to 90, and the threshold can be adjusted based on specific scenarios. |
| code | Int | Error code |
| message | String | Error description |


## Example

### Request Packet Using URL:

```
POST  /face/livedetectpicture HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: service.image.myqcloud.com
Content-Length: 117
Content-Type: "application/json"

{"appid":"1000001","sign":"123456","url":"http://test-123456.image.myqcloud.com/test.jpg"}
```

### Request Packet Using Image:

```
POST /face/livedetectpicture HTTP/1.1Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==Host: service.image.myqcloud.comContent-Length: 641Content-Type: multipart/form-data;boundary=--------------acebdf13572468
----------------acebdf13572468
Content-Disposition: form-data; name="appid";
123456----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="face.jpg"
Content-Type: image/jpeg
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx----------------acebdf13572468--

```

### Response Packet:

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 168
Content-Type: application/json
{
  "data":{
    "score":30,
  },
  "code":0,
  "message":"OK"

```

## Error Codes
| **Error Code** | **Description** |
| ------- | ------------------------ |
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
| 107 | Authentication service is unavailable |
| 108 | Authentication service is unavailable |
| 213 | Internal error |
| -4006 | Failed to extract features of the selfie in the video |
| -4007 | Failed to compare selfies in the video |
| -4009 | Failed to extract features of the card image |
| -4010 | Failed to calculate the similarity between the selfie and the card image |
| -4015 | Facial detection of selfie failed|
| -4016 | Selfie decoding failed |
| -4017 | Facial detection of card image failed |
| -4018 | Card image decoding failed |
| -5001 | Invalid video |
| -5002 | Lip reading failed |
| -5005 | Insufficient parsing for selfie|
| -5007 | No sound in the video |
| -5008 | Voice recognition failed |
| -5009 | Facial detection of video failed. No mouth or face |
| -5010 | Failed to capture lip movements |
| -5011 | Liveness detection failed (all other errors relating to liveness detection are classified into this type of error) |
| -5012 | Too much noise in the video |
| -5013 | The sound in the video is too low |
| -5014 | Invalid level parameter in liveness detection |
| -5015 | Video resolution is too low. The minimum resolution is 320*480 |
| -5801 | ID card number or name is missing in the request |
| -5802 | Service is unavailable due to server internal error |
| -5803 | ID card number is inconsistent with name |
| -5804 | Invalid ID card number |
| -5805 | No image or failed to download the image from URL |
| -5806 | Incorrect format of ID card number or name |
| -5807 | Invalid ID card information |

For more information on other API error codes, please see [**Error Codes**](/document/product/641/12410).










