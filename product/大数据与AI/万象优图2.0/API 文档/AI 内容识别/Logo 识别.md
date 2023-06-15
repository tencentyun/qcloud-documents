## 功能概述

腾讯云数据万象通过 **RecognizeLogo** 接口实现对图片内电商 Logo 的识别，返回图片中 Logo 的名称、坐标、置信度分值。，返回图片中Logo的名称、坐标、置信度分值。图片Logo识别请求包属于 GET 请求，请求时需要携带签名。

> 当前Logo识别的图片限制为：图片格式支持 PNG、JPEG、JPG，图片大小不超过5MB，图片宽高大于32像素 x 32像素，小于7680像素 x 7680像素。

## 请求语法

```shell
GET /?ci-process=RecognizeLogo&detect-url=<detect-url> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization:Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

## 请求内容

| 参数名称       | 描述                              | 类型     | 是否必选 |
|:---------- |:------------------------------- |:------ |:---- |
| ci-process | 数据万象处理能力，Logo识别固定为RecognizeLogo | String | 是    |
| detect-url | 待检查图片url，需要进行urlencode          | String | 是    |

### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

### 请求体

该请求无请求体。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

### 响应体

该响应体返回为 **application/xml** 数据，具体的数据内容如下：

| 节点名称（关键字）         | 父节点 | 描述            | 类型        |
|:----------------- |:--- |:------------- |:--------- |
| RecognitionResult | 无   | 保存Logo识别结果的容器 | Container |

Response 的内容：

| 节点名称（关键字） | 父节点               | 描述                      | 类型        |
|:--------- |:----------------- |:----------------------- |:--------- |
| Status    | RecognitionResult | Logo识别结果。0表示未识别到，1表示识别到 | Int       |
| LogoInfo  | RecognitionResult | Logo识别结果，可能有多个          | Container |

LogoInfo 节点内容：

| 节点名称（关键字） | 父节点      | 描述                             | 类型        |
|:--------- |:-------- |:------------------------------ |:--------- |
| Name      | LogoInfo | Logo的名称                        | String    |
| Sorce     | LogoInfo | Logo的置信度，取值范围为[0-100]。值越高概率越大。 | Int       |
| Location  | LogoInfo | 图中识别到Logo的坐标                   | Container |

Location 节点内容：

| 节点名称（关键字） | 父节点      | 描述               | 类型     |
|:--------- |:-------- |:---------------- |:------ |
| Point     | Location | Logo坐标点（X坐标,Y坐标） | String |

## 示例

#### 请求

```shell
GET /?ci-process=RecognizeLogo&detect-url=xxx HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Date: xxxxx
Authorization:XXXXXXXXXXXX
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 414641
Date: xxxxxx
Server: tencent-ci
x-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<RecognitionResult>
    <Status>1</Status>
    <LogoInfo>
      <Name>xxxxxxxx</Name>
      <Sorce>99</Sorce>
      <Location>
        <Point>100,100</Point>
        <Point>100,200</Point>
        <Point>200,200</Point>
        <Point>200,100</Point>
      </Location>
    </LogoInfo>
    <LogoInfo>
      <Name>xxxxxxxx</Name>
      <Sorce>95</Sorce>
      <Location>
        <Point>1000,1000</Point>
        <Point>1000,2000</Point>
        <Point>2000,2000</Point>
        <Point>2000,1000</Point>
      </Location>
    </LogoInfo>
</RecognitionResult>
```
