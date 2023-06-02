## 功能描述

ModifyM3U8Token 接口用于在加密 M3U8 的 key uri 中增加 Token。

## 请求

#### 请求示例

```plaintext
GET /modifym3u8token?object=&token= HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-type: application/xml
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                | 类型      | 是否必选 | 默认值 | 限制   |
| :------------- | :----- | :---------------------------------- | :-------- | :------- | :------| :------|
| object  | 无 | M3U8 文件的对象名 | String | 是    | 无 | 无 |
| token | 无 | 需要嵌入 M3U8 key uri中的 token | String | 是 | 无 | 长度小于2048个 UTF-8字符 |



#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为二进制流，包含完整 M3U8 文件的内容展示如下：

```plaintext
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-KEY:METHOD=AES-128,URI="http://website.com/aes.key?Ciphertext=xxxxx&KMSRegion=ap-guangzhou",IV=0x00000000000000000000000000000000
#EXTINF:11.333333,
test-00000.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:9.416667,
test-00001.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:9.375000,
test-00002.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:11.291667,
test-00003.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:3.500000,
test-00004.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXT-X-ENDLIST
```


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
GET /modifym3u8token?expires=3600&object=test.m3u8&token=abc HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-type: application/xml
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-ci
x-ci-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZm****

#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-KEY:METHOD=AES-128,URI="http://website.com/aes.key?Ciphertext=xxxxx&KMSRegion=ap-guangzhou&token=abc",IV=0x00000000000000000000000000000000
#EXTINF:11.333333,
test-00000.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:9.416667,
test-00001.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:9.375000,
test-00002.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:11.291667,
test-00003.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXTINF:3.500000,
test-00004.ts?q-sign-algorithm=sha1&q-ak=&q-sign-time=&q-key-time=&q-header-list=host&q-url-param-list=&q-signature=&x-cos-security-token=
#EXT-X-ENDLIST
```

