## 功能概述

 对象存储通过数据万象 **RecognizeLogo** 接口实现对图片内电商 Logo 的识别，返回图片中 Logo 的名称、坐标、置信度分值。

>! 当前 Logo 识别的图片限制为：图片格式支持 PNG、JPEG、JPG，图片大小不超过10MB，图片宽高大于50像素 x 50像素。
>

## 请求语法

```shell
GET /?ci-process=RecognizeLogo&detect-url=<detect-url> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 

## 请求内容

| 参数名称     | 描述                                                         | 类型   | 是否必选 |
| :----------- | :----------------------------------------------------------- | :----- | :------- |
| ObjectKey    | 对象文件名，例如：folder/document.jpg。                      | String | 是       |
| ci-process   | 数据万象处理能力，Logo 识别固定为 RecognizeLogo。                | String | 是       |
| detect-url   | 您可以通过填写 `detect-url` 处理任意公网可访问的图片链接。不填写 `detect-url` 时，后台会默认处理 `ObjectKey` ，填写了 `detect-url` 时，后台会处理 `detect-url` 链接，无需再填写 `ObjectKey`  `detect-url` 示例：`http://www.example.com/abc.jpg` ，需要进行 UrlEncode，处理后为`http%25253A%25252F%25252Fwww.example.com%25252Fabc.jpg`。 | String | 否       |
| ignore-error | 当此参数为1时，针对文件过大等导致处理失败的场景，会直接返回原图而不报错。 | int    | 否       |

>! 
> - 通过 ObjectKey 进行商品抠图为内网操作，不会产生额外的外网流量。
> - 通过 detect-url 进行商品抠图，会产生图片所在源站对应的外网流量。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                   | 类型      |
| :----------------- | :----- | :--------------------- | :-------- |
| RecognitionResult  | 无     | 保存 Logo 识别结果的容器。 | Container |

Response 的内容：

| 节点名称（关键字） | 父节点            | 描述                                     | 类型      |
| :----------------- | :---------------- | :--------------------------------------- | :-------- |
| Status             | RecognitionResult | Logo 识别结果。0表示未识别到，1表示识别到。 | Int       |
| LogoInfo           | RecognitionResult | Logo 识别结果，可能有多个。                 | Container |

LogoInfo 节点内容：

| 节点名称（关键字） | 父节点   | 描述                                              | 类型      |
| :----------------- | :------- | :------------------------------------------------ | :-------- |
| Name               | LogoInfo | Logo 的名称。                                        | String    |
| Sorce              | LogoInfo | Logo 的置信度，取值范围为[0-100]。值越高概率越大。 | String    |
| Location           | LogoInfo | 图中识别到 Logo 的坐标。                              | Container |

Location 节点内容：

| 节点名称（关键字） | 父节点   | 描述                      | 类型   |
| :----------------- | :------- | :------------------------ | :----- |
| Point              | Location | Logo 坐标点（X 坐标，Y 坐标）。 | String |

## 实际案例

#### 案例一：对存储桶内的图片进行 Logo 识别

内容识别相关接口需要携带签名访问，并与获取参数以“&”连接，示例如下：

```plaintext
https://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?q-sign-algorithm=<signature>?ci-process=RecognizeLogo
```

>? `<signature>`为签名部分，获取方式请参考 [请求签名](https://cloud.tencent.com/document/product/436/7778)。
>

#### 响应示例

```xml
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



#### 案例二：对第三方图片进行 Logo 识别

将第三方图片（链接为`http://www.example.com/abc.jpg`）在下载时进行 Logo 识别，示例如下：

```
https://examples-1251000004.cos.ap-shanghai.myqcloud.com/?q-sign-algorithm=<signature>?ci-process=RecognizeLogo&detect-url=http%25253A%25252F%25252Fwww.example.com%25252Fabc.jpg
```

