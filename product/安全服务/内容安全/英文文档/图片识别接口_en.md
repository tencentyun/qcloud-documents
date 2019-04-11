## API Description

This API is used to identify whether an image contains pornographic contents, sexy contents, malicious contents identified by OCR, sensitive contents, politicians, terrorism and violence, illegal contents, bloody contents or others.

Protocol: `HTTPS`

Domain name: `upload-csec.api.qcloud.com`

API Name: `ContentSecurity.Image.Recognition`

## Request Parameters

> **Note:**
> All of the following parameters are very important to identify the malicious intent. Lack of any one may affect the identification result.

<table>
<tr>
<th>Parameter Name</th>
<th>Type</th>
<th>Description</th>
</tr>
<tr>
<td colspan=3>API common field</td>
</tr>
<tr>
<td>Action</td>
<td>String</td>
<td>Name of the API for the desired operation (ContentSecurity.Image.Recognition)</td>
</tr>
<tr>
<td>Region</td>
<td>String</td>
<td>Region parameter, indicating the region to which the instance to be operated belongs. For more information, please see <a href="https://cloud.tencent.com/document/product/213/6091">Regions and Availability Zones</a>.  </td>
</tr>
<tr>
<td>Timestamp</td>
<td>Uint</td>
<td>The current UNIX timestamp that records the time at which the API request was initiated.</td>
</tr>
<tr>
<td>Nonce</td>
<td>Uint</td>
<td>A random positive integer that is used in conjunction with Timestamp to prevent replay attacks.</td>
</tr>
<tr>
<td>SecretId</td>
<td>String</td>
<td>The SecretID which is used for identifying identity and applied for on Cloud API Key . A SecretID corresponds to a unique SecretKey, which is used to generate the request Signature. For more information, please see <a href="https://cloud.tencent.com/document/api/377/4214">Signature Method</a>.</td>
</tr>
<tr>
<td>Signature</td>
<td>String</td>
<td>Request signature, which is used to verify the validity of the request. It is generated based on input parameters. For more information, please see <a href="https://cloud.tencent.com/document/api/377/4214">Signature Method</a>.</td>
</tr>
<tr>
<td colspan=3>Basic field: Required</td>
</tr>
<tr>
<td>filename</td>
<td>String</td>
<td>File name</td>
</tr>
<tr>
<td colspan=3>Basic field: It is required to select at least one from two options.</td>
</tr>
<tr>
<td>fileUrl</td>
<td>String</td>
<td>URL of a file</td>
</tr>
<tr>
<td>fileContent</td>
<td>String</td>
<td>Base64 encoded value of the image content</td>
</tr>
<tr>
<td colspan=3>Other optional fields</td>
</tr>
<tr>
<td>category</td>
<td>String</td>
<td>Detection type. It uses the default value (pornDetection) if left empty. For multi-type detection, "|" can be used for connection, such as pornDetection/OCR.</td>
</tr>
<tr>
<td colspan=3>Optional parameters of field "category"</td>
</tr>
<tr>
<td>pornDetection</td>
<td>String</td>
<td>Pornography detection</td>
</tr>
<tr>
<td>OCR</td>
<td>String</td>
<td>OCR text recognition</td>
</tr>
<tr>
<td>political</td>
<td>String</td>
<td>Politician detection</td>
</tr>
<tr>
<td>QRCode</td>
<td>String</td>
<td>QR code detection</td>
</tr>
<tr>
<td>liveScene</td>
<td>String</td>
<td>Smoking detection</td>
</tr>
<tr>
<td>violentTerrorism</td>
<td>String</td>
<td>Terrorist and violence content detection</td>
</tr>
</table>

## Response Parameters


| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. </br>0: Successful; </br>Other values: Failed. </br>For more information, please see the Error Codes page. |
| codeDesc | String | Error code at business side. </br>For a successful operation, "Success" is returned. </br>In case of an error, a message describing the reason for the error is returned. |
| message | String | Module error message description depending on API. |
| data | Array | Details of identified contents. For more information, please see [data Parameter Type Description](#shuju). |
<span id="shuju"></span>
**data Parameter Type Description**

| Name | Type | Description |
|---------|---------|---------|
| category | String | Identification type. For more information, please see [category Description](#c). |
| label | String | Identification type subtab |
| confidence | Int | Possibility of being identified as label |
| suggestion | String | pass: Approved</br>review: Manual review</br>block: Not allowed to be spread |
| subcode | Int | Specific service error code. For more information, please see the [subcode Description](#b). |
| content | Array | The returned result of OCR or QRCode recognition |
| candidates | Array | Recognition of faces similar to those of politicians |
| candidates.confidence | Int | The confidence of politician face recognition |
| candidates.name | String | Name of recongnized politician with similar face |

<span id="b"></span>
**subcode Description**

| Error Code | Description |
|---------|---------|
| -1102 | Image decoding failed |
| -1308 | Failed to download image with URL |
| -1403 | Failed to download image |
| -5208 | Internal service error |
<span id="c"></span>
**category Description**

| category | Tag | Description |
|---------|---------|---------|
| pornDetection | porn | Pornographic contents |
| pornDetection | hot | Sexy contents |
| pornDetection | breast | Breasts are highlighted. |
| pornDetection | ass | Buttocks or thighs are highlighted. |
| pornDetection | bareBody | Nude bodies |
| pornDetection | unrealHotPeople | Fictional person |
| OCR | OCR | OCR recognition |
| OCR | UgcAntiSpam | OCR text recognition |
| political | political | Identify a politician or a custom person |
| violentTerrorism | terrorists | Militants |
| violentTerrorism | knife | Knives |
| violentTerrorism | guns | Guns |
| violentTerrorism | blood | Bloody actions |
| violentTerrorism | fire | Fire |
| violentTerrorism | flag | Flags |
| violentTerrorism | crowd | Crowd gathering |
| QRCode | QRCode | Identify QR code |
| liveScene | smoke | Smoking |

## Sample Codes

```
{
    "code": 0,
    "message": "NoError",
    "codeDesc": "Success",
    "data":[
        {
            "confidence": 20, 
            "category": "pornDetection", 
            "suggestion": "block", 
            "subCode": "0", 
            "label": "porn"
        },
        {
            "confidence": 30, 
            "category": "pornDetection",
            "suggestion": "pass", 
            "subCode": "0", 
            "label": "hot"
        },
        {
            "confidence": 50, 
            "category": "pornDetection",
            "suggestion": "pass", 
            "subCode": "0", 
            "label": "breast"
        },
        {
            "confidence": 50, 
            "category": "pornDetection",
            "suggestion": "pass", 
            "subCode": "0", 
            "label": "ass"
        },
        {
            "confidence": 50, 
            "category": "pornDetection",
            "suggestion": "pass", 
            "subCode": "0", 
            "label": "bareBody"
        },
        {
            "confidence": 50,
            "category": "pornDetection",
            "suggestion": "pass", 
            "subCode": "0", 
            "label": "unrealHotPeople"
        },
        {
            "confidence": 100,
            "category": "OCR",
            "suggestion": "block", 
            "label": "ocr",
            "subCode": "0", 
            "ocrMsg": "Add contact into WeChat to watch pornographic videos"
        },
        {
            "confidence": 100,
            "category": "OCR",
            "suggestion": "block", 
            "label": "UgcAntiSpam	",
            "subCode": "0"
        },
        {
            "confidence": 80,
            "category": "political",
            "suggestion": "block", 
            "label": "political",
            "subCode": "0", 
            "candidates":[{"confidence":80,"name":"Xi Jinping"}, {"confidence":70,"name":"Li Keqiang"}]
        },
        {
            "confidence": 100,
            "category": "QRCode",
            "suggestion": "block", 
            "label": "QRCode",
            "subCode": "0", 
            "candidates":["http://u.wechat.com/EGn4HWqn3jXK8xvx52uUYRE","http://u.wechat.com/EGn4HWqn3jXK8xvx52uUYkE"]
        },
        {
            "confidence": 70,
            "category": "liveScene",
            "suggestion": "block", 
            "subCode": "0", 
            "label": "smoke"
        }
    ]
}
```



