## 功能描述

查询海报合成模板列表接口。


## 请求

#### 请求示例

```shell
GET /posterproduction/template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                             | 类型    | 必选 |
| :----------------- | :----- | :------------------------------- | :------ | :--- |
| pageNumber         | 无     | 第几页，默认值:1                 | Integer | 否   |
| pageSize           | 无     | 每页个数，默认值:10              | Integer | 否   |
| categoryIds        | 无     | 模板分类ID，支持传入多个，以`,`符号分割字符串                         | String    | 否   |
| type           | 无     | Official(系统预设模板)，Custom(自定义模板)，All(所有模板)，默认值: Custom | String  | 否   |




## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateId>A</TemplateId>
        <Height></Height>
        <Width></Width>
        <Name></Name>
        <Thumb></Thumb>
    </TemplateList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                            | 类型      |
| :----------------- | :------- | :------------------------------ | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 模板总数                        | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber  | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize    | Int       |
| TemplateList       | Response | 模板数组，Container中参数为模板具体参数  | Container 数组 |




#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
GET /posterproduction/template HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: test-1234567890.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 14 Jul 2022 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TemplateList>
        <TemplateId>62e27c0cd73bf6bb0e903721</TemplateId>
		<width>1280</width>,
		<height>720</height>
	    <name>央视频下载观看1<name>
		<thumb>https://static.taishan.qq.com/xrdnest/psd/e9c62e867425f9188f86a319b1fd7a96/5db75609b417e6c77ff14ba2252e2a24.png?imageMogr2/thumbnail/!50p/format/webp</thumb>
    </TemplateList>
    <TemplateList>
        <TemplateId>62e279bad73bf6bb0e903707</TemplateId>
		<width>1125</width>,
		<height>1125</height>
	    <name>0点折上折<name>
		<thumb>https://static.taishan.qq.com/xrdnest/psd/e9c62e867425f9188f86a319b1fd7a96/f2d919c4d3a1d3dd4ab26bcaa5996940.png?imageMogr2/thumbnail/!50p/format/webp</thumb>
    </TemplateList>
</Response>
```
