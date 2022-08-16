## 功能描述

查询模板。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateTranscodeTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求

#### 请求示例

```shell
GET /template HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                             | 类型    | 必选 |
| :----------------- | :----- | :------------------------------- | :------ | :--- |
| tag                | 无     | 模板类型，默认值：All             | String  | 否   |
| category           | 无     | Official（系统预设模板），Custom（自定义模板），默认值：Custom | String  | 否   |
| ids                | 无     | 模板 ID，以`,`符号分割字符串      | String  | 否   |
| name               | 无     | 模板名称前缀                     | String  | 否   |
| pageNumber         | 无     | 第几页，默认值：1                 | Integer | 否   |
| pageSize           | 无     | 每页个数，默认值：10              | Integer | 否   |

tag 支持以下几种类型:

| 模板类型 | tag |
| :----------------- | :----- |
| 语音识别          | SpeechRecognition |


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
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Name>TemplateName</Name>
        <Tag>SpeechRecognition</Tag>
        <SpeechRecognition>
            <EngineModelType>16k_zh</EngineModelType>
            <ResTextFormat>1</ResTextFormat>
            <FilterDirty>0</FilterDirty>
            <FilterModal>1</FilterModal>
            <ConvertNumMode>0</ConvertNumMode>
            <SpeakerDiarization>1</SpeakerDiarization>
            <SpeakerNumber>0</SpeakerNumber>
            <FilterPunc>0</FilterPunc>
            <OutputFileType>txt</OutputFileType>
        </SpeechRecognition>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
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
| TemplateList       | Response | 模板数组                        | Container 数组 |

对于不同的模板类型，TemplateList 内容同创建模板接口的 Response，请参照以下链接：
- <a href="https://cloud.tencent.com/document/product/460/78939#Response" target="_blank">语音识别</a>


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

**案例一：按照模板 ID 维度查询**

#### 请求

```shell
GET /template?ids=t1847cd4ca57f543e89f551dbe68169eb9,t1a30a323f55434a29b25bf2a16bdf5f59,C HTTP/1.1
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
    <TemplateList>
        <TemplateId>t1847cd4ca57f543e89f551dbe68169eb9</TemplateId>
        <Name>TemplateName</Name>
        <Tag>SpeechRecognition</Tag>
        <SpeechRecognition>
            <EngineModelType>16k_zh</EngineModelType>
            <ResTextFormat>1</ResTextFormat>
            <FilterDirty>0</FilterDirty>
            <FilterModal>1</FilterModal>
            <ConvertNumMode>0</ConvertNumMode>
            <SpeakerDiarization>1</SpeakerDiarization>
            <SpeakerNumber>0</SpeakerNumber>
            <FilterPunc>0</FilterPunc>
            <OutputFileType>txt</OutputFileType>
        </SpeechRecognition>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
    <TemplateList>
        <TemplateId>t1a30a323f55434a29b25bf2a16bdf5f59</TemplateId>
        <Name>TemplateName</Name>
        <Tag>SpeechRecognition</Tag>
        <SpeechRecognition>
            <EngineModelType>8k_zh_s</EngineModelType>
            <ResTextFormat>1</ResTextFormat>
            <FilterDirty>0</FilterDirty>
            <FilterModal>1</FilterModal>
            <ConvertNumMode>0</ConvertNumMode>
            <SpeakerDiarization>1</SpeakerDiarization>
            <SpeakerNumber>0</SpeakerNumber>
            <FilterPunc>0</FilterPunc>
            <OutputFileType>txt</OutputFileType>
        </SpeechRecognition>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
    <NonExistTIDs>
        <TemplateId>C</TemplateId>
    </NonExistTIDs>
</Response>
```

**案例二：按照分页列表维度查询**

#### 请求

```shell
GET /template?pageSize=10&pageNumber=1 HTTP/1.1
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
        <TemplateId>t1847cd4ca57f543e89f551dbe68169eb9</TemplateId>
        <Name>TemplateName</Name>
        <Tag>SpeechRecognition</Tag>
        <SpeechRecognition>
            <EngineModelType>16k_zh</EngineModelType>
            <ResTextFormat>1</ResTextFormat>
            <FilterDirty>0</FilterDirty>
            <FilterModal>1</FilterModal>
            <ConvertNumMode>0</ConvertNumMode>
            <SpeakerDiarization>1</SpeakerDiarization>
            <SpeakerNumber>0</SpeakerNumber>
            <FilterPunc>0</FilterPunc>
            <OutputFileType>txt</OutputFileType>
        </SpeechRecognition>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
    <TemplateList>
        <TemplateId>t1a30a323f55434a29b25bf2a16bdf5f59</TemplateId>
        <Name>TemplateName</Name>
        <Tag>SpeechRecognition</Tag>
        <SpeechRecognition>
            <EngineModelType>8k_zh_s</EngineModelType>
            <ResTextFormat>1</ResTextFormat>
            <FilterDirty>0</FilterDirty>
            <FilterModal>1</FilterModal>
            <ConvertNumMode>0</ConvertNumMode>
            <SpeakerDiarization>1</SpeakerDiarization>
            <SpeakerNumber>0</SpeakerNumber>
            <FilterPunc>0</FilterPunc>
            <OutputFileType>txt</OutputFileType>
        </SpeechRecognition>
        <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
        <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
    </TemplateList>
</Response>
```
