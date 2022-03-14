## 功能描述

DescribeDocProcessJob 用于查询指定的文档转码任务。

## 请求

#### 请求示例

```shell
GET /doc_jobs/<jobId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。

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
                <Message> </Message>
                <Operation>
                        <DocProcess>
                                <EndPage></EndPage>
                                <ImageParams></ImageParams>
                                <SrcType></SrcType>
                                <StartPage></StartPage>
                                <TgtType></TgtType>
                        </DocProcess>
                        <DocProcessResult>
                                <FailPageCount></FailPageCount>
                                <PageInfo>
                                        <PageNo></PageNo>
                                        <TgtUri></TgtUri>
                                </PageInfo>
                                <SuccPageCount></SuccPageCount>
                                <TaskId></TaskId>
                                <TgtType></TgtType/>
                                <TotalPageCount></TotalPageCount>
                        </DocProcessResult>
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

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息，同 [CreateDocProcessJobs](https://cloud.tencent.com/document/product/460/46942#.E5.93.8D.E5.BA.94) 接口的 Response.JobsDetail 节点 | Container |
| NonExistJobIds     | Response | 查询的 ID 中不存在的任务，所有任务都存在时不返回             | String    |


Container 节点 Operation 的内容：

| 节点名称（关键字） | 父节点                        | 描述                                                         | 类型      |
| :----------------- | :---------------------------- | :----------------------------------------------------------- | :-------- |
| DocProcess         | Response.JobsDetail.Operation | 文档预览任务参数，同 [CreateDocProcessJobs](https://cloud.tencent.com/document/product/460/46942#.E8.AF.B7.E6.B1.82) 接口的 Request.Operation.DocProcess 节点 | Container |
| DocProcessResult   | Response.JobsDetail.Operation | 在 job 的类型为 DocProcess 且 job 状态为 success 时，返回文档预览任务结果详情 | Container |
| Output             | Response.JobsDetail.Operation | 结果输出地址，同 [CreateDocProcessJobs](https://cloud.tencent.com/document/product/460/46942#.E8.AF.B7.E6.B1.82) 接口的 Request.Operation.Output 节点 | Container |

Container 节点 DocProcessResult 节点的内容

| 节点名称（关键字） | 父节点                        | 描述                                                         | 类型      |
| :----------------- | :---------------------------- | :----------------------------------------------------------- | :-------- |
| PageInfo           | Response.JobsDetail.Operation.DocProcessResult | 预览任务产物详情 | Container |
| TgtType           | Response.JobsDetail.Operation.DocProcessResult | 预览产物目标格式 | String |
| TotalPageCount     | Response.JobsDetail.Operation.DocProcessResult | 预览任务产物的总数 | Int |
| SuccPageCount      | Response.JobsDetail.Operation.DocProcessResult | 预览任务产物的成功数 | Int |
| FailPageCount      | Response.JobsDetail.Operation.DocProcessResult | 预览任务产物的失败数 | Int |
| TotalSheetCount     | Response.JobsDetail.Operation.DocProcessResult | 预览任务的 Sheet 总数（源文件为 Excel 特有参数） | Int |

Container 节点 PageInfo 节点的内容

| 节点名称（关键字） | 父节点                        | 描述                                                         | 类型      |
| :----------------- | :---------------------------- | :----------------------------------------------------------- | :-------- |
| PageNo           | Response.JobsDetail.Operation.DocProcessResult.PageInfo | 预览产物页码,源文件为 Excel 格式时表示 SheetId | Container |
| TgtUri     | Response.JobsDetail.Operation.DocProcessResult.PageInfo | 预览产物生成的 cos 桶路径 | Int |
| X-SheetPics      | Response.JobsDetail.Operation.DocProcessResult.PageInfo | 当前 Sheet 生成的图片总数（源文件为 Excel 特有参数） | Int |
| PicIndex      | Response.JobsDetail.Operation.DocProcessResult.PageInfo | 当前预览产物在整个源文件中的序号（源文件为 Excel 特有参数） | Int |
| PicNum      | Response.JobsDetail.Operation.DocProcessResult.PageInfo | 当前预览产物在 Sheet 中的序号（源文件为 Excel 特有参数） | Int |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

### 请求

```shell
GET /doc_jobs/d13cfd584cd9011ea820b597ad1785a2f HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
```

#### 1.非 Excel 文档请求响应

```shell
<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-07-24T17:28:47+0800</CreationTime>
                <EndTime>2020-07-24T17:28:49+0800</EndTime>
                <Input>
                        <Object>1.doc</Object>
                </Input>
                <JobId>d13cfd584cd9011ea820b597ad1785a2f</JobId>
                <Message/>
                <Operation>
                        <DocProcess>
                                <EndPage>0</EndPage>
                                <ImageParams/>
                                <SrcType/>
                                <StartPage>2</StartPage>
                                <TgtType>png</TgtType>
                        </DocProcess>
                        <DocProcessResult>
                                <FailPageCount>0</FailPageCount>
                                <PageInfo>
                                        <PageNo>2</PageNo>
                                        <TgtUri>big/test-1</TgtUri>
                                </PageInfo>
                                <SuccPageCount>1</SuccPageCount>
                                <TaskId/>
                                <TgtType/>
                                <TotalPageCount>2</TotalPageCount>
                        </DocProcessResult>
                        <Output>
                                <Bucket>examplebucket-1250000000</Bucket>
                                <Object>big/test-${Number}</Object>
                                <Region>ap-chongqing</Region>
                        </Output>
                </Operation>
                <QueueId>p50882922b848464fadd222d771438328</QueueId>
                <State>Success</State>
                <Tag>DocProcess</Tag>
        </JobsDetail>
</Response>
```

#### 2. Excel 格式响应
```plaintext
<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-12-03T19:54:10+0800</CreationTime>
                <EndTime>2020-12-03T19:54:13+0800</EndTime>
                <Input>
                        <Object>1.xlsx</Object>
                </Input>
                <JobId>d13cfd584cd9011ea820b597ad1785a2f</JobId>
                <Message/>
                <Operation>
                        <DocProcess>
                                <Comments>0</Comments>
                                <DocPassword/>
                                <EndPage>2</EndPage>
                                <ImageParams/>
                                <PaperDirection>0</PaperDirection>
                                <PaperSize>0</PaperSize>
                                <Quality>100</Quality>
                                <SheetId>0</SheetId>
                                <SrcType/>
                                <StartPage>1</StartPage>
                                <TgtType/>
                                <Zoom>100</Zoom>
                        </DocProcess>
                        <DocProcessResult>
                                <FailPageCount>0</FailPageCount>
                                <PageInfo>
                                        <PageNo>1</PageNo>
                                        <PicIndex>1</PicIndex>
                                        <PicNum>1</PicNum>
                                        <TgtUri>mark2/1/test-1.jpg</TgtUri>
                                        <X-SheetPics>2</X-SheetPics>
                                </PageInfo>
                                <PageInfo>
                                        <PageNo>1</PageNo>
                                        <PicIndex>2</PicIndex>
                                        <PicNum>2</PicNum>
                                        <TgtUri>mark2/1/test-2.jpg</TgtUri>
                                        <X-SheetPics>2</X-SheetPics>
                                </PageInfo>
                                <SuccPageCount>6</SuccPageCount>
                                <TaskId/>
                                <TgtType/>
                                <TotalPageCount>6</TotalPageCount>
                                <TotalSheetCount>3</TotalSheetCount>
                        </DocProcessResult>
                        <Output>
                                <Bucket>markjrzhang-1251704708</Bucket>
                                <Object>mark/${SheetID}/pic-${Page}.jpg</Object>
                                <Region>ap-chongqing</Region>
                        </Output>
                </Operation>
                <QueueId>p5fdbba9a9b83479f84538d5beb*****</QueueId>
                <State>Success</State>
                <Tag>DocProcess</Tag>
        </JobsDetail>
</Response>
```
