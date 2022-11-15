## 功能描述

提交多个任务。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CreateAnimationTemplate&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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
POST /jobs HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体：

```shell
<Request>
    <Input>
        <Object>input/demo.mp4</Object>
    </Input>
    <Operation>
        <Tag>Animation</Tag>
        <TemplateId>t1f16e1dfbdc994105b31292d45710642a</TemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/animation.gif</Object>
        </Output>
        <UserData>This is my Animation job.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <Operation>
        <Tag>Transcode</Tag>
        <TemplateId>t1995d523e42df4c5e858f244b4174360c</TemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/transcode.mp4</Object>
        </Output>
        <UserData>This is my Trancode job.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <Operation>
        <Tag>SmartCover</Tag>
        <SmartCover>
            <Format>jpg</Format>
            <Width>1280</Width>
            <Height>960</Height>
            <Count>5</Count>
            <DeleteDuplicates>true</DeleteDuplicates>
        </SmartCover>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/smartcover-${Number}.jpg</Object>
        </Output>   
        <UserData>This is my SmartCover job.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | -------- |
| Request            | 无     | 保存请求的容器 | Container | 是       |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                    | 类型      | 是否必选 |
| ------------------ | ------- | ----------------------- | --------- | -------- |
| Input              | Request | 待操作的媒体信息        | Container | 是       |
| Operation          | Request | 操作规则，个数不超过6个 | Container | 是       |
| QueueId            | Request | 任务所在的队列 ID       | String    | 是       |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述       | 类型   | 是否必选 |
| ------------------ | ------------- | ---------- | ------ | -------- |
| Object             | Request.Input | 媒体文件名 | String | 是       |

对于不同的任务类型，Operation 的内容不同，请参照以下链接：
- <a href="https://cloud.tencent.com/document/product/460/76913#operation" target="_blank">音视频转码</a>
- <a href="https://cloud.tencent.com/document/product/460/78248#operation" target="_blank">极速高清转码</a>
- <a href="https://cloud.tencent.com/document/product/460/76900#operation" target="_blank">视频转动图</a>
- <a href="https://cloud.tencent.com/document/product/460/76910#operation" target="_blank">视频截帧</a>
- <a href="https://cloud.tencent.com/document/product/460/76909#operation" target="_blank">智能封面</a>
- <a href="https://cloud.tencent.com/document/product/460/76901#operation" target="_blank">音视频拼接</a>
- <a href="https://cloud.tencent.com/document/product/460/76918#operation" target="_blank">人声分离</a>
- <a href="https://cloud.tencent.com/document/product/460/76915#operation" target="_blank">精彩集锦</a>
- <a href="https://cloud.tencent.com/document/product/460/76907#operation" target="_blank">SDR to HDR</a>
- <a href="https://cloud.tencent.com/document/product/460/76916#operation" target="_blank">视频增强</a>
- <a href="https://cloud.tencent.com/document/product/460/76912#operation" target="_blank">超分辨率</a>
- <a href="https://cloud.tencent.com/document/product/460/76908#operation" target="_blank">音视频转封装</a>
- <a href="https://cloud.tencent.com/document/product/460/76902#operation" target="_blank">数字水印</a>
- <a href="https://cloud.tencent.com/document/product/460/76903#operation" target="_blank">提取数字水印</a>
- <a href="https://cloud.tencent.com/document/product/460/76917#operation" target="_blank">视频标签</a>
- <a href="https://cloud.tencent.com/document/product/460/76904#operation" target="_blank">获取媒体信息</a>
- <a href="https://cloud.tencent.com/document/product/460/76911#operation" target="_blank">音视频流分离</a>
- <a href="https://cloud.tencent.com/document/product/460/76906#operation" target="_blank">视频质量分析</a>
- <a href="https://cloud.tencent.com/document/product/460/76914#operation" target="_blank">语音合成</a>
- <a href="https://cloud.tencent.com/document/product/460/76905#operation" target="_blank">音频降噪</a>


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j682b9662f84611ecb8546d80f2baf56f</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Tag>Animation</Tag>
            <TemplateId>t1f16e1dfbdc994105b31292d45710642a</TemplateId>
            <TemplateName>animation_demo</TemplateName>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/animation.gif</Object>
            </Output>
            <UserData>This is my Animation job.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j68427030f84611ecb8546d80f2baf56f</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Tag>Transcode</Tag>
            <TemplateId>t1995d523e42df4c5e858f244b4174360c</TemplateId>
            <TemplateName>transcode_demo</TemplateName>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/transcode.mp4</Object>
            </Output>
            <UserData>This is my Trancode job.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j6842765cf84611ecb8546d80f2baf56f</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Tag>SmartCover</Tag>
            <SmartCover>
                <Format>jpg</Format>
                <Width>1280</Width>
                <Height>960</Height>
                <Count>5</Count>
                <DeleteDuplicates>true</DeleteDuplicates>
            </SmartCover>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/smartcover-${Number}.jpg</Object>
            </Output>   
            <UserData>This is my SmartCover job.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述           | 类型      |
| :----------------- | :------- | :------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息 | Container 数组 |

对于不同的任务类型，JobsDetail 的内容不同，请参照以下链接：
- <a href="https://cloud.tencent.com/document/product/460/76913#jobsDetail" target="_blank">音视频转码</a>
- <a href="https://cloud.tencent.com/document/product/460/78248#jobsDetail" target="_blank">极速高清转码</a>
- <a href="https://cloud.tencent.com/document/product/460/76900#jobsDetail" target="_blank">视频转动图</a>
- <a href="https://cloud.tencent.com/document/product/460/76910#jobsDetail" target="_blank">视频截帧</a>
- <a href="https://cloud.tencent.com/document/product/460/76909#jobsDetail" target="_blank">智能封面</a>
- <a href="https://cloud.tencent.com/document/product/460/76901#jobsDetail" target="_blank">音视频拼接</a>
- <a href="https://cloud.tencent.com/document/product/460/76918#jobsDetail" target="_blank">人声分离</a>
- <a href="https://cloud.tencent.com/document/product/460/76915#jobsDetail" target="_blank">精彩集锦</a>
- <a href="https://cloud.tencent.com/document/product/460/76907#jobsDetail" target="_blank">SDR to HDR</a>
- <a href="https://cloud.tencent.com/document/product/460/76916#jobsDetail" target="_blank">视频增强</a>
- <a href="https://cloud.tencent.com/document/product/460/76912#jobsDetail" target="_blank">超分辨率</a>
- <a href="https://cloud.tencent.com/document/product/460/76908#jobsDetail" target="_blank">音视频转封装</a>
- <a href="https://cloud.tencent.com/document/product/460/76902#jobsDetail" target="_blank">数字水印</a>
- <a href="https://cloud.tencent.com/document/product/460/76903#jobsDetail" target="_blank">提取数字水印</a>
- <a href="https://cloud.tencent.com/document/product/460/76917#jobsDetail" target="_blank">视频标签</a>
- <a href="https://cloud.tencent.com/document/product/460/76904#jobsDetail" target="_blank">获取媒体信息</a>
- <a href="https://cloud.tencent.com/document/product/460/76911#jobsDetail" target="_blank">音视频流分离</a>
- <a href="https://cloud.tencent.com/document/product/460/76906#jobsDetail" target="_blank">视频质量分析</a>
- <a href="https://cloud.tencent.com/document/product/460/76914#jobsDetail" target="_blank">语音合成</a>
- <a href="https://cloud.tencent.com/document/product/460/76905#jobsDetail" target="_blank">音频降噪</a>


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 使用多个模板 ID

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: test-1234567890.ci.ap-chongqing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <Input>
        <Object>input/demo.mp4</Object>
    </Input>
    <Operation>
        <Tag>Animation</Tag>
        <TemplateId>t1f16e1dfbdc994105b31292d45710642a</TemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/animation.gif</Object>
        </Output>
        <UserData>This is my Animation job.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <Operation>
        <Tag>Transcode</Tag>
        <TemplateId>t1995d523e42df4c5e858f244b4174360c</TemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/transcode.mp4</Object>
        </Output>
        <UserData>This is my Trancode job.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <Operation>
        <Tag>SmartCover</Tag>
        <SmartCover>
            <Format>jpg</Format>
            <Width>1280</Width>
            <Height>960</Height>
            <Count>5</Count>
            <DeleteDuplicates>true</DeleteDuplicates>
        </SmartCover>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/smartcover-${Number}.jpg</Object>
        </Output>   
        <UserData>This is my SmartCover job.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Mon, 28 Jun 2022 15:23:12 GMT
Server: tencent-ci
x-ci-request-id: NjMxMDJhYTNfMThhYTk0MGFfYmU1OV8zZjc=

<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j682b9662f84611ecb8546d80f2baf56f</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Tag>Animation</Tag>
            <TemplateId>t1f16e1dfbdc994105b31292d45710642a</TemplateId>
            <TemplateName>animation_demo</TemplateName>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/animation.gif</Object>
            </Output>
            <UserData>This is my Animation job.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j68427030f84611ecb8546d80f2baf56f</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Tag>Transcode</Tag>
            <TemplateId>t1995d523e42df4c5e858f244b4174360c</TemplateId>
            <TemplateName>trancode_demo</TemplateName>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/transcode.mp4</Object>
            </Output>
            <UserData>This is my Trancode job.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>j6842765cf84611ecb8546d80f2baf56f</JobId>
        <State>Submitted</State>
        <CreationTime>2022-06-27T15:23:10+0800</CreationTime>
        <StartTime>-</StartTime>
        <EndTime>-</EndTime>
        <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>
        <Input>
            <BucketId>test-123456789</BucketId>
            <Object>input/demo.mp4</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Tag>SmartCover</Tag>
            <SmartCover>
                <Format>jpg</Format>
                <Width>1280</Width>
                <Height>960</Height>
                <Count>5</Count>
                <DeleteDuplicates>true</DeleteDuplicates>
            </SmartCover>
            <Output>
                <Region>ap-chongqing</Region>
                <Bucket>test-123456789</Bucket>
                <Object>output/smartcover-${Number}.jpg</Object>
            </Output>   
            <UserData>This is my SmartCover job.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```
