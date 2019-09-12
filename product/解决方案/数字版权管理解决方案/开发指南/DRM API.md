## DRM API

DRM 所有 API 都是基于云 API 的标准协议的，详细请参阅 [云API ](https://cloud.tencent.com/product/api) 和 [云API文档](https://cloud.tencent.com/document/api/1000/30698)。

### 获取点播 DRM 加密密钥

**接口**：[DescribeKeys](https://cloud.tencent.com/document/api/1000/30707)
**请求参数**：
```json
{
    "DrmGetKeyPara":{
        "DrmType":"xxx",//widevine/fairplay
        "ContentId":"test123"
        "Tracks":["video","audio"],
        "RsaPublicKey":"LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDcmJBUmhXamRTZjlWTGtpZGZGdHhkbzJjUwpOak9PTExhdjdaRWZZSzJtd2NZQ3BqRmtDaG41bi8xcHM2LzcwZjlBRUs1Mmt5T0lSVTVzR0hqcjZEMEgrUUFzCndJZnBya1NzV0krSS9hTGYrM2l0b0tIb0Y5eWRTMEhneHdEcUM0dWRTRFFzRmxKczFTNHZEdm5WbG1IRGNJSkIKdDBLTzZoSVJ4Z2F3bmVxUHN3SURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo=" //base64 encrypted public key
    }
}
```

生成公钥，请参考“相关参考”章节。
**响应**：
```json
{
  "Response": {
    "ContentId": "test",
    "Keys": [
      {
        "Iv": "tHUB8M/yvRcHswxRm74hb/ej+q4amjEg0/m8F82ezbg=",
        "Key": "7CiNq5Q+fYTBAIySw/gglnNNeBmw6uQ76erIvD3IQj0=",
        "KeyId": "0c366a3173584fb693be0218c27d4532",
        "Track": "VIDEO"
      },
      {
        "Iv": "tHUB8M/yvRcHswxRm74hb/ej+q4amjEg0/m8F82ezbg=",
        "Key": "7CiNq5Q+fYTBAIySw/gglnNNeBmw6uQ76erIvD3IQj0=",
        "KeyId": "0c366a3173584fb693be0218c27d4532",
        "Track": "AUDIO"
      }
    ],
    "Pssh": "",
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
    "SessionKey": "l2XuCkQx288LFBlbDeKuQ1tfW5LOC2mbRfcAvhD8byFmIq8sqTQ+KA/UMrJyk1lImqgodiOuv+fmVTNbb06IY9vILtBDaN3Ek5/x2c0HUJ3k+kL4gMxOvKmAe/F0+qr0Kbl9CVx6YRntXWcWqD+IJ18D76+tQD1aBP8tS5pwV6Q="
    }
}
```

### 生成 DRM 播放许可证

**接口**：[CreateLicense](https://cloud.tencent.com/document/api/1000/30711)
**请求参数**：
```json
{
    "DrmType":"widevine",//widevine/fairplay
    "LicenseRequest":"xxx", //base64 编码的license请求
    "ContentType":"LiveVideo"//表明是点播还是直播
}
```
**响应**：
```json
{
    "Response":{
        "RequestId":"xxx",
        "License":"xxx",//base64 encoded playback license
    }
}
```

### 使用 DRM 加密 API

**接口**：[StartEncryption](https://cloud.tencent.com/document/api/1000/30709)
**请求参数**：
```json
{
        "CosEndPoint":"cos.ap-hongkong.myqcloud.com",
        "CosSecretId":"xxx",  #客户cos用SecretId
        "CosSecretKey":"xxx",     #客户cos用key
        "DrmType":"fairplay",
        "SourceObject":{
            "BucketName":"drm-unencrypt-1251697373",
            "ObjectName":"in.mp4"
            },
        "OutputObjects":[
            {
                "BucketName":"drm-encrypt-1251697373",
                "ObjectName":"out.m3u8",
                "Para":{"Type":"m3u8"}
            },
            {
                "BucketName":"drm-encrypt-1251697373",
                "ObjectName":"out.ts",
                "Para":{"Type":"audio"}
            },
            ]
}
```

**响应**：
```json
{
    "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
}
```

**加密结果回调**：
```json
{
    "DrmEncryptInfo":{
        "CosEndPoint":"cos.ap-hongkong.myqcloud.com",
        "DrmType":"fairplay",
        "OutputObjects":[
            {
                "BucketName":"drm-encrypt-1251697373",
                "ObjectName":"out.m3u8",
                "Para":{
                    "Type":"m3u8"
                }
            },
            {
                "BucketName":"drm-encrypt-1251697373",
                "ObjectName":"out.ts",
                "Para":{
                    "Type":"video"
                }
            }
        ],
        "CosSecretId":"xxx",
        "CosSecretKey":"xxx",
        "SourceObject":{
            "BucketName":"drm-unencrypt-1251697373",
            "ObjectName":"in.mp4"
        }
    },
    "Code":-26,
    "Message":"encrypt failed",
    "RequestId":"3fcd0191-2668-43e0-932f-26891d425540"
}
```

