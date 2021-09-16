## 功能描述

CreateDocProcessJobs 接口用于提交一个文档转码任务。

>!
>- 目前支持的输入文件类型包含如下格式：
>  - 演示文件：pptx、ppt、pot、potx、pps、ppsx、dps、dpt、pptm、potm、ppsm。
>  - 文字文件：doc、dot、wps、wpt、docx、dotx、docm、dotm。
>  - 表格文件：xls、xlt、et、ett、xlsx、xltx、csv、xlsb、xlsm、xltm、ets。
    表格文件，一张表可能分割为多页转换，生成多张图片。
>  - 其他格式文件： pdf、 lrc、 c、 cpp、 h、 asm、 s、 java、 asp、 bat、 bas、 prg、 cmd、 rtf、 txt、 log、 xml、 htm、 html。
>- 输入文件大小限制在200M之内。
>- 输入文件页数限制在5000页之内。


## 请求

#### 请求示例

```shell
POST /doc_jobs HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```shell
<Request>
  <Tag></Tag>
  <Input>
    <Object></Object>
  </Input>
  <Operation>
    <Output>
      <Region></Region>
      <Bucket></Bucket>
      <Object></Object>
    </Output>
    <DocProcess>
       <StartPage></StartPage>
       <EndPage></EndPage>
       <TgtType></TgtType>
    </DocProcess>
  </Operation>
  <QueueId></QueueId>
</Request>
```

具体的数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Request</td>
      <td>无</td>
      <td>保存请求的容器</td>
      <td>Container</td>
      <td>是</td>
   </tr>
</table>


Container 类型 Request 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Tag</td>
      <td>Request</td>
      <td>创建任务的 Tag，目前仅支持：DocProcess</td>
      <td>String</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Input</td>
      <td>Request</td>
      <td>待操作的文件对象</td>
      <td>Container</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Operation</td>
      <td>Request</td>
      <td>操作规则</td>
      <td>Container</td>
      <td>是</td>
   </tr>
   <tr>
      <td>QueueId</td>
      <td>Request</td>
      <td>任务所在的队列 ID</td>
      <td>String</td>
      <td>是</td>
   </tr>
</table>


Container 类型 Input 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Object</td>
      <td>Request.Input</td>
      <td>文件在 COS 上的文件路径，Bucket 由 Host 指定</td>
      <td>String</td>
      <td>是</td>
   </tr>
</table>




Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                          | 类型      | 是否必选 |
| ------------------ | ----------------- | --------------------------------------------- | --------- | -------- |
| DocProcess         | Request.Operation | 当 Tag 为 DocProcess 时有效，指定该任务的参数 | Container | 是       |
| Output             | Request.Operation | 结果输出地址                                  | Container | 是       |


Container 类型 DocProcess 的具体数据描述如下：

| 节点名称（关键字） | 父节点                       | 描述                                                         | 类型   | 是否必选 |
| ------------------ | :--------------------------- | ------------------------------------------------------------ | ------ | -------- |
| SrcType            | Request.Operation.DocProcess | 源数据的后缀类型，当前文档转换根据 cos 对象的后缀名来确定源数据类型，当 cos 对象没有后缀名时，可以设置该值 | String | 否       |
| TgtType            | Request.Operation.DocProcess | 转换输出目标文件类型：<br><li>jpg，转成 jpg 格式的图片文件；如果传入的格式未能识别，默认使用 jpg 格式<li>png，转成 png 格式的图片文件<br><li>pdf，转成 pdf 格式文件（暂不支持指定页数）<br> | String | 否       |
| SheetId          | Request.Operation.DocProcess | 表格文件参数，转换第 X 个表，默认为0；设置 SheetId 为0，即转换文档中全部表                                   | Int    | 否       |
| StartPage          | Request.Operation.DocProcess | 从第 X 页开始转换；在表格文件中，一张表可能分割为多页转换，生成多张图片。StartPage 表示从指定 SheetId 的第 X 页开始转换。默认为1                                   | Int   | 否       |
| EndPage            | Request.Operation.DocProcess | 转换至第 X 页；在表格文件中，一张表可能分割为多页转换，生成多张图片。EndPage 表示转换至指定 SheetId 的第 X 页。默认为-1，即转换全部页 | Int    | 否       |
| ImageParams        | Request.Operation.DocProcess | 转换后的图片处理参数，支持 [基础图片处理](https://cloud.tencent.com/document/product/460/6924) 所有处理参数，多个处理参数可通过 [管道操作符](https://cloud.tencent.com/document/product/460/15293) 分隔，从而实现在一次访问中按顺序对图片进行不同处理 | String | 否       |
| DocPassword       | Request.Operation.DocProcess | Office 文档的打开密码，如果需要转换有密码的文档，请设置该字段  | String | 否     |
| Comments       | Request.Operation.DocProcess | 是否隐藏批注和应用修订，默认为 0。<br><li>0：隐藏批注，应用修订<br><li>1：显示批注和修订  | Int | 否     |
| PaperDirection       | Request.Operation.DocProcess | 表格文件转换纸张方向，0代表垂直方向，非0代表水平方向，默认为0   | Int | 否     |
| Quality           | Request.Operation.DocProces|  生成预览图的图片质量，取值范围 [1-100]，默认值100。 例：值为100，代表生成图片质量为100%   | Int | 否      |
| Zoom             | Request.Operation.DocProces|预览图片的缩放参数，取值范围[10-200]， 默认值100。 例：值为200，代表图片缩放比例为200% 即放大两倍   | Int | 否      |



Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | -------- |
| Region             | Request.Operation.Output | 存储桶的地域                                                 | String | 是       |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                             | String | 是       |
| Object             | Request.Operation.Output | 输出文件路径。<br/>**非表格文件输出文件名需包含 ${Number} 或 ${Page} 参数。**多个输出文件，${Number} 表示序号从1开始，${Page} 表示序号与预览页码一致。<li>${Number} 表示多个输出文件，序号从1开始，例如输入 abc_${Number}.jpg，预览某文件5 - 6页，则输出文件名为 abc_1.jpg，abc_2.jpg<li>${Page} 表示多个输出文件，序号与预览页码一致，例如输入 abc_${Page}.jpg，预览某文件5-6页，则输出文件名为 abc_5.jpg，abc_6.jpg<br/>**表格文件输出路径需包含 ${SheetID} 占位符，输出文件名必须包含 ${Number} 参数。**<li>例如 `/${SheetID}/abc_${Number}.jpg`，先根据 excel 转换的表格数，生成对应数量的文件夹，再在对应的文件夹下，生成对应数量的图片文件</li> | String | 是       |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
        <JobsDetail>
                <Code></Code>
                <CreationTime></CreationTime>
                <EndTime></EndTime>
                <Input>
                    <Object></Object>
                </Input>
                <JobId></JobId>
                <Message/>
                <Operation>
                    <DocProcess>
                        <SrcType></SrcType>
                        <TgtType></TgtType>
                        <StartPage></StartPage>
                        <EndPage></EndPage>
                        <ImageParams></ImageParams>
                    </DocProcess>
                    <Output>
                        <Bucket></Bucket>
                        <Object></Object>
                        <Region></Region>
                    </Output>
                </Operation>
                <QueueId></QueueId>
                <State></State>
                <Tag></Tag>
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
| JobsDetail         | Response | 任务的详细信息 | Container |

Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                                         | 类型      |
| :----------------- | :------------------ | :----------------------------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义                        | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义                      | String    |
| JobId              | Response.JobsDetail | 新创建任务的 ID                                              | String    |
| Tag                | Response.JobsDetail | 新创建任务的 Tag：DocProcess                                 | String    |
| State              | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                                               | String    |
| QueueId            | Response.JobsDetail | 任务所属的队列 ID                                            | String    |
| Input              | Response.JobsDetail | 该任务的输入文件路径                                         | Container |
| Operation          | Response.JobsDetail | 该任务的规则                                                 | Container |

Container 节点 Input 的内容：
同上面请求中的 Request.Input 节点。

Container 节点 Operation 的内容：

| 节点名称（关键字） | 父节点                        | 描述             | 类型      |
| :----------------- | :---------------------------- | :--------------- | :-------- |
| DocProcess         | Response.JobsDetail.Operation | 文档预览任务参数 | Container |
| Output             | Response.JobsDetail.Operation | 文件的输出地址   | Container |

Container 节点 DocProcess 的内容：
同上面请求中的 Request.Operation.DocProcess 节点。

Container 节点 Output 的内容：
同上面请求中的 Request.Operation.Output 节点。


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```plaintext
POST /doc_jobs HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: examplebucket-1250000000.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 546
Authorization: Authorization

<?xml version="1.0" encoding="UTF-8" ?>

<Request>
    <Input>
        <Object>1.doc</Object>
    </Input>
    <Operation>
      <Output>
          <Region>ap-chongqing</Region>
          <Object>big/test-${Number}</Object>
          <Bucket>examplebucket-1250000000</Bucket>
      </Output>
      <DocProcess>
          <TgtType>png</TgtType>
          <StartPage>1</StartPage>
          <EndPage>-1</EndPage>
	      <ImageParams>watermark/1/image/aHR0cDovL3Rlc3QwMDUtMTI1MTcwNDcwOC5jb3MuYXAtY2hvbmdxaW5nLm15cWNsb3VkLmNvbS8xLmpwZw==/gravity/southeast</ImageParams>
      </DocProcess>
    </Operation>
    <Tag>DocProcess</Tag>
    <QueueId>p532fdead78444e649e1a4467c1cd19d3</QueueId>
</Request>[!http]
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 07:20:08 GMT
Content-Type: application/xml
Content-Length: 863
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZTgwMjhfYzc2OTQzNjRfMzUx****

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-07-27T15:20:08+0800</CreationTime>
                <EndTime>-</EndTime>
                <Input>
                        <Object>1.doc</Object>
                </Input>
                <JobId>d99b3127ecfd911eab5e60dedb7c395dd</JobId>
                <Message/>
                <Operation>
                        <DocProcess>
                                <EndPage>5001</EndPage>
                                <ImageParams>watermark/1/image/aHR0cDovL3Rlc3QwMDUtMTI1MTcwNDcwOC5jb3MuYXAtY2hvbmdxaW5nLm15cWNsb3VkLmNvbS8xLmpwZw==/gravity/southeast</ImageParams>
                                <SrcType/>
                                <StartPage>1</StartPage>
                                <TgtType>png</TgtType>
                        </DocProcess>
                        <Output>
                                <Bucket>examplebucket-1250000000</Bucket>
                                <Object>big/test-${Number}</Object>
                                <Region>ap-chongqing</Region>
                        </Output>
                </Operation>
                <QueueId>p532fdead78444e649e1a4467c1cd19d3</QueueId>
                <State>Submitted</State>
                <Tag>DocProcess</Tag>
        </JobsDetail>
</Response>
```

