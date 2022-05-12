## bucket 列表示例 

#### 请求

```
GET /docbucket?regions=ap-chongqing HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: Authorization
```

#### 响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 07:00:43 GMT
Content-Type: application/xml
Content-Length: 843
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZTdiOWJfYzc2OTQzNjRfM2QzOF8x

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>3</TotalCount>
        <RequestId>NWYxZTdiOWJfYzc2OTQzNjRfM2QzOF8x</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <DocBucketList>
                <Name>test008-1251704708</Name>
                <CreateTime>2020-07-27T10:54:42+0800</CreateTime>
                <Region>ap-chongqing</Region>
                <AliasBucketId/>
                <BucketId>test008-1251704708</BucketId>
        </DocBucketList>
        <DocBucketList>
                <Name>test007-1251704708</Name>
                <CreateTime>2020-07-24T22:42:26+0800</CreateTime>
                <Region>ap-chongqing</Region>
                <AliasBucketId/>
                <BucketId>test007-1251704708</BucketId>
        </DocBucketList>
</Response>
```

## 提交任务 

#### 请求

```
POST /doc_jobs HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: test008-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 546
Authorization: Authorization

<?xml version="1.0" encoding="UTF-8" ?><Request><Input><Object>1.doc</Object></Input><Operation><Output><Region>ap-chongqing</Region><Object>big/test-${Number}</Object><Bucket>test008-1251704708</Bucket></Output><DocProcess><TgtType>png</TgtType><StartPage>1</StartPage><EndPage>-1</EndPage><ImageParams>watermark/1/image/aHR0cDovL3Rlc3QwMDUtMTI1MTcwNDcwOC5jb3MuYXAtY2hvbmdxaW5nLm15cWNsb3VkLmNvbS8xLmpwZw==/gravity/southeast</ImageParams></DocProcess></Operation><Tag>DocProcess</Tag><QueueId>p532fdead78444e649e1a4467c1cd19d3</QueueId></Request>[!http]
```

#### 响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 07:20:08 GMT
Content-Type: application/xml
Content-Length: 863
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZTgwMjhfYzc2OTQzNjRfMzUxZl84

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
                                <Bucket>test008-1251704708</Bucket>
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

excel 任务返回

```
<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-09-28T14:47:06+0800</CreationTime>
                <EndTime>2020-09-28T14:47:08+0800</EndTime>
                <Input>
                        <Object>1.xlsx</Object>
                </Input>
                <JobId>d6ca2a6ec015611eb95c41789273ab63d</JobId>
                <Message/>
                <Operation>
                        <DocProcess>
                                <EndPage>2</EndPage>
                                <ImageParams/>
                                <PaperDirection>0</PaperDirection>
                                <PaperSize>0</PaperSize>
                                <SheetId>2</SheetId>
                                <SrcType/>
                                <StartPage>1</StartPage>
                                <TgtType/>
                        </DocProcess>
                        <DocProcessResult>
                                <FailPageCount>0</FailPageCount>
                                <PageInfo>
                                        <PageNo>2</PageNo>
                                        <TgtUri>mark1/2/test-1.jpg</TgtUri>
                                        <X-SheetPics>2</X-SheetPics>
                                </PageInfo>
                                <PageInfo>
                                        <PageNo>2</PageNo>
                                        <TgtUri>mark1/2/test-2.jpg</TgtUri>
                                        <X-SheetPics>2</X-SheetPics>
                                </PageInfo>
                                <SuccPageCount>2</SuccPageCount>
                                <TaskId/>
                                <TgtType/>
                                <TotalPageCount>2</TotalPageCount>
                                <TotalSheetCount>3</TotalSheetCount>
                        </DocProcessResult>
                        <Output>
                                <Bucket>chengdutest-1251704708</Bucket>
                                <Object>mark1/${SheetID}/test-${Number}.jpg</Object>
                                <Region>ap-chengdu</Region>
                        </Output>
                </Operation>
                <QueueId>p5ca4e360fd86411db7a080af40e4e579</QueueId>
                <State>Success</State>
                <Tag>DocProcess</Tag>
        </JobsDetail>
</Response>
```

## 文档预览队列

#### 请求

```
GET /docqueue?pageNumber=1&pageSize=2 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: test007-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: Authorization
```

#### 响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 07:29:28 GMT
Content-Type: application/xml
Content-Length: 677
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZTgyNTdfYzc2OTQzNjRfMzUxZF9h

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>1</TotalCount>
        <RequestId>NWYxZTgyNTdfYzc2OTQzNjRfMzUxZF9h</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>2</PageSize>
        <QueueList>
                <QueueId>p2505d57bdf4c4329804b58a6a5fb1572</QueueId>
                <Name>queue-doc-process-1</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url/>
                        <Event/>
                        <Type/>
                        <State>Off</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>2020-07-24T22:42:27+0800</CreateTime>
                <UpdateTime>2020-07-24T22:42:27+0800</UpdateTime>
                <BucketId>test007-1251704708</BucketId>
                <Category>DocProcessing</Category>
        </QueueList>
</Response>
```

## 修改队列参数

#### 请求

```
PUT /docqueue/p2505d57bdf4c4329804b58a6a5fb1572 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: test007-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 279
Authorization: Authorization

<?xml version="1.0" encoding="UTF-8" ?><Request><QueueId>p2505d57bdf4c4329804b58a6a5fb1572</QueueId><State>Active</State><Name>markjrzhang4</Name><NotifyConfig><Url>http://google.com/</Url><State>On</State><Type>Url</Type><Event>TransCodingFinish</Event></NotifyConfig></Request>[!http]
```


#### 响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 08:22:41 GMT
Content-Type: application/xml
Content-Length: 641
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZThlZDBfYzc2OTQzNjRfMzUxYV8xNQ==

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <RequestId>NWYxZThlZDBfYzc2OTQzNjRfMzUxYV8xNQ==</RequestId>
        <Queue>
                <QueueId>p2505d57bdf4c4329804b58a6a5fb1572</QueueId>
                <Name>markjrzhang4</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url>http://google.com/</Url>
                        <Event>TransCodingFinish</Event>
                        <Type>Url</Type>
                        <State>On</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>2020-07-24T22:42:27+0800</CreateTime>
                <UpdateTime>2020-07-27T16:22:40+0800</UpdateTime>
                <BucketId>test007-1251704708</BucketId>
                <Category>DocProcessing</Category>
        </Queue>
</Response>
```
