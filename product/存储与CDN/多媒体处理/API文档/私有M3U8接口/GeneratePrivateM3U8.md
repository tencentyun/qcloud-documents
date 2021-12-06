## 功能描述

GeneratePrivateM3U8 接口用于获取私有 M3U8 ts 资源的下载授权。

## 请求

#### 请求示例

```shell
GET /pm3u8?expires=&object= HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-type: application/xml
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体

该请求无请求体。

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                | 类型      | 是否必选 | 限制   |
| :----------------- | :----- | :---------------------------------- | :-------- | :------- | :------|
| object            | 无     | M3U8 文件的对象名 | String | 是       | 无 |
| expires            | 无     | 私有 ts 资源 url 下载凭证的相对有效期，单位秒 | String | 是       | [3600,43200] |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

#### 响应体

该响应体返回为 二进制流，包含完整 M3U8 文件的内容展示如下：

```shell
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:0
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

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求

```shell
GET /pm3u8?expires=3600&object=test.m3u8 HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-type: application/xml
```

#### 响应

```shell
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
#EXTINF:11.333333,
test-00000.ts?q-sign-algorithm=sha1&q-ak=AKIDIJinagBeqYfuCEWtH_uG7psMUd7KwrOCNVt9BcEVtxZyh5xHaQLe5YUDpHjfGrfT&q-sign-time=1630396953%3B1630397953&q-key-time=1630396953%3B1630397953&q-header-list=host&q-url-param-list=&q-signature=8a276a2ffd0916e3cd20eea6b1e27e4d76cfebad&x-cos-security-token=vNezC3DD9EDD0zq4uCYCL0F6G7fAvADa726dc8d25238537889b30b03908c3f63vCUb2WUG0VL9dV8ZyypuNd5NOq0jbHoLS22CVn02nT2DohbRGhFlhy3BabKIhp57Ygh-tPeMmwI4HyvjK4RLolrC7kGnYKpCZnwm-j-Np_6RdGU6lsSyrdWXn867w1jUdQVfmillQiLz_dourCyHkTpC4p1yhnmON93WyWsxCzPDKBYCJn03vxW-3HuvPZ_EXdagHcVA21TYU_6AI6Ul6mAby8TVKh1ATl0cHUGh3DZGCPgax9eZyfqhvliAr2OLqEbIexT1qPFDIni4gZytbGCJPUF1C-h-WBLkdEU4sZR7S_PnOhhF6wbvIHCgFlzA6mIb3c5F_FonsHBmk97R-nFegDd5W21hqesT_1fy5JE8qbkYR5jsVKLKVppqsHZZ4xkW62oe5yeoQAA75-NhpfmZtopvWII91Wpen6F9360
#EXTINF:9.416667,
test-00001.ts?q-sign-algorithm=sha1&q-ak=AKIDIJinagBeqYfuCEWtH_uG7psMUd7KwrOCNVt9BcEVtxZyh5xHaQLe5YUDpHjfGrfT&q-sign-time=1630396953%3B1630397953&q-key-time=1630396953%3B1630397953&q-header-list=host&q-url-param-list=&q-signature=f57ad61c6c5b2402b24e35109682a7e107a1b4c3&x-cos-security-token=vNezC3DD9EDD0zq4uCYCL0F6G7fAvADa726dc8d25238537889b30b03908c3f63vCUb2WUG0VL9dV8ZyypuNd5NOq0jbHoLS22CVn02nT2DohbRGhFlhy3BabKIhp57Ygh-tPeMmwI4HyvjK4RLolrC7kGnYKpCZnwm-j-Np_6RdGU6lsSyrdWXn867w1jUdQVfmillQiLz_dourCyHkTpC4p1yhnmON93WyWsxCzPDKBYCJn03vxW-3HuvPZ_EXdagHcVA21TYU_6AI6Ul6mAby8TVKh1ATl0cHUGh3DZGCPgax9eZyfqhvliAr2OLqEbIexT1qPFDIni4gZytbGCJPUF1C-h-WBLkdEU4sZR7S_PnOhhF6wbvIHCgFlzA6mIb3c5F_FonsHBmk97R-nFegDd5W21hqesT_1fy5JE8qbkYR5jsVKLKVppqsHZZ4xkW62oe5yeoQAA75-NhpfmZtopvWII91Wpen6F9360
#EXTINF:9.375000,
test-00002.ts?q-sign-algorithm=sha1&q-ak=AKIDIJinagBeqYfuCEWtH_uG7psMUd7KwrOCNVt9BcEVtxZyh5xHaQLe5YUDpHjfGrfT&q-sign-time=1630396953%3B1630397953&q-key-time=1630396953%3B1630397953&q-header-list=host&q-url-param-list=&q-signature=c38952fae80f9aa22005315c913c8154a780e6a8&x-cos-security-token=vNezC3DD9EDD0zq4uCYCL0F6G7fAvADa726dc8d25238537889b30b03908c3f63vCUb2WUG0VL9dV8ZyypuNd5NOq0jbHoLS22CVn02nT2DohbRGhFlhy3BabKIhp57Ygh-tPeMmwI4HyvjK4RLolrC7kGnYKpCZnwm-j-Np_6RdGU6lsSyrdWXn867w1jUdQVfmillQiLz_dourCyHkTpC4p1yhnmON93WyWsxCzPDKBYCJn03vxW-3HuvPZ_EXdagHcVA21TYU_6AI6Ul6mAby8TVKh1ATl0cHUGh3DZGCPgax9eZyfqhvliAr2OLqEbIexT1qPFDIni4gZytbGCJPUF1C-h-WBLkdEU4sZR7S_PnOhhF6wbvIHCgFlzA6mIb3c5F_FonsHBmk97R-nFegDd5W21hqesT_1fy5JE8qbkYR5jsVKLKVppqsHZZ4xkW62oe5yeoQAA75-NhpfmZtopvWII91Wpen6F9360
#EXTINF:11.291667,
test-00003.ts?q-sign-algorithm=sha1&q-ak=AKIDIJinagBeqYfuCEWtH_uG7psMUd7KwrOCNVt9BcEVtxZyh5xHaQLe5YUDpHjfGrfT&q-sign-time=1630396953%3B1630397953&q-key-time=1630396953%3B1630397953&q-header-list=host&q-url-param-list=&q-signature=b7fed1e31254da2be9c25a662dc4eead2d4dbae7&x-cos-security-token=vNezC3DD9EDD0zq4uCYCL0F6G7fAvADa726dc8d25238537889b30b03908c3f63vCUb2WUG0VL9dV8ZyypuNd5NOq0jbHoLS22CVn02nT2DohbRGhFlhy3BabKIhp57Ygh-tPeMmwI4HyvjK4RLolrC7kGnYKpCZnwm-j-Np_6RdGU6lsSyrdWXn867w1jUdQVfmillQiLz_dourCyHkTpC4p1yhnmON93WyWsxCzPDKBYCJn03vxW-3HuvPZ_EXdagHcVA21TYU_6AI6Ul6mAby8TVKh1ATl0cHUGh3DZGCPgax9eZyfqhvliAr2OLqEbIexT1qPFDIni4gZytbGCJPUF1C-h-WBLkdEU4sZR7S_PnOhhF6wbvIHCgFlzA6mIb3c5F_FonsHBmk97R-nFegDd5W21hqesT_1fy5JE8qbkYR5jsVKLKVppqsHZZ4xkW62oe5yeoQAA75-NhpfmZtopvWII91Wpen6F9360
#EXTINF:3.500000,
test-00004.ts?q-sign-algorithm=sha1&q-ak=AKIDIJinagBeqYfuCEWtH_uG7psMUd7KwrOCNVt9BcEVtxZyh5xHaQLe5YUDpHjfGrfT&q-sign-time=1630396953%3B1630397953&q-key-time=1630396953%3B1630397953&q-header-list=host&q-url-param-list=&q-signature=aedf39d58f5669367f3f6b709238956efe2b9b2f&x-cos-security-token=vNezC3DD9EDD0zq4uCYCL0F6G7fAvADa726dc8d25238537889b30b03908c3f63vCUb2WUG0VL9dV8ZyypuNd5NOq0jbHoLS22CVn02nT2DohbRGhFlhy3BabKIhp57Ygh-tPeMmwI4HyvjK4RLolrC7kGnYKpCZnwm-j-Np_6RdGU6lsSyrdWXn867w1jUdQVfmillQiLz_dourCyHkTpC4p1yhnmON93WyWsxCzPDKBYCJn03vxW-3HuvPZ_EXdagHcVA21TYU_6AI6Ul6mAby8TVKh1ATl0cHUGh3DZGCPgax9eZyfqhvliAr2OLqEbIexT1qPFDIni4gZytbGCJPUF1C-h-WBLkdEU4sZR7S_PnOhhF6wbvIHCgFlzA6mIb3c5F_FonsHBmk97R-nFegDd5W21hqesT_1fy5JE8qbkYR5jsVKLKVppqsHZZ4xkW62oe5yeoQAA75-NhpfmZtopvWII91Wpen6F9360
#EXT-X-ENDLIST
```

