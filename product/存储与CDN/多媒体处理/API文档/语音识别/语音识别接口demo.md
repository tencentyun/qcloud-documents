## 开通语音识别任务接口 

#### 请求

```
POST /asrbucket HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: markjrzhang-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 91
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597911213;1597921273&q-key-time=1597911213;1597921273&q-header-list=content-type;host&q-url-param-list=&q-signature=4f848c055b457fdc67155fe1275f2b31d893a4f2

<?xml version="1.0" encoding="UTF-8" ?>

<Request>
  <Bucket>markjrzhangtest</Bucket>
</Request>
```

#### 响应

```
HTTP/1.1 200 OK
Date: Thu, 20 Aug 2020 08:14:34 GMT
Content-Type: application/xml
Content-Length: 334
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYzZTMwZTlfOTBmYTUwNjRfMjJhNl8x

<?xml version="1.0" encoding="utf-8"?>
<Response>
	<RequestId>NWYzZTMwZTlfOTBmYTUwNjRfMjJhNl8x</RequestId>
	<AsrBucket>
		<Name>markjrzhang-1251704708</Name>
		<CreateTime>2020-08-20T16:14:34+0800</CreateTime>
		<Region>ap-chongqing</Region>
		<AliasBucketId/>
		<BucketId>markjrzhang-1251704708</BucketId>
	</AsrBucket>
</Response>

```



## 提交语音识别任务 

#### 请求

```
POST /asr_jobs HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: markjrzhang-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 411
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597915249;1597925309&q-key-time=1597915249;1597925309&q-header-list=content-type;host&q-url-param-list=&q-signature=cb18718939be449e84d22358e8f0e7c8f

<?xml version="1.0" encoding="utf-8"?>

<Request>
  <Input>
    <Object>1.mp3</Object>
  </Input>
  <Operation>
    <Output>
      <Region>ap-chongqing</Region>
      <Object>1.mp3</Object>
      <Bucket>markjrzhang-1251704708</Bucket>
    </Output>
    <SpeechRecognition>
      <ChannelNum>1</ChannelNum>
      <EngineModelType>16k_zh</EngineModelType>
    </SpeechRecognition>
  </Operation>
  <Tag>SpeechRecognition</Tag>
  <QueueId>p2e11b0a26d404d029c15f06c48803dde</QueueId>
</Request>
```

#### 响应

```
HTTP/1.1 200 OK
Date: Date
Content-Type: application/xml
Content-Length: 863
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: request-id

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-08-20T17:35:11+0800</CreationTime>
                <EndTime>-</EndTime>
                <Input>
                        <Object>16k.mp3</Object>
                </Input>
                <JobId>s716d8c8ee2c811ea94a0b170ddb38f60</JobId>
                <Message/>
                <Operation>
                        <Output>
                                <Bucket>test005-1251704708</Bucket>
                                <Object>1.txt</Object>
                                <Region>ap-chongqing</Region>
                        </Output>
                        <SpeechRecognition>
                                <ChannelNum>1</ChannelNum>
                                <ConvertNumMode>1</ConvertNumMode>
                                <EngineModelType>16k_zh</EngineModelType>
                                <FilterDirty>0</FilterDirty>
                                <FilterModal>0</FilterModal>
                                <ResTextFormat>0</ResTextFormat>
                        </SpeechRecognition>
                </Operation>
                <QueueId>p5275b560c7fd498db9a36e5e202827b6</QueueId>
                <State>Submitted</State>
                <Tag>SpeechRecognition</Tag>
        </JobsDetail>
</Response>
```

## 语音识别任务队列

#### 请求

```
GET /asr_jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: chongqingtest-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 413
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597916272;1597926332&q-key-time=1597916272;1597926332&q-header-list=content-type;host&q-url-param-list=&q-signature=f267d01af850ee168d0058ea8e6b923ff9837c2d

<?xml version="1.0" encoding="utf-8"?>

<Request>
  <Input>
    <Object>1.mp3</Object>
  </Input>
  <Operation>
    <Output>
      <Region>ap-chongqing</Region>
      <Object>1.mp3</Object>
      <Bucket>chongqingtest-1251704708</Bucket>
    </Output>
    <SpeechRecognition>
      <ChannelNum>1</ChannelNum>
      <EngineModelType>16k_zh</EngineModelType>
    </SpeechRecognition>
  </Operation>
  <Tag>SpeechRecognition</Tag>
  <QueueId>p2e11b0a26d404d029c15f06c48803dde</QueueId>
</Request>
```

#### 响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 08:22:41 GMT
Content-Type: application/xml
Content-Length: 677
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: request-id

<?xml version="1.0" encoding="utf-8"?>

<Response> 
  <JobsDetail> 
    <Code>Success</Code>  
    <CreationTime>2020-08-20T17:43:01+0800</CreationTime>  
    <EndTime>2020-08-20T17:43:25+0800</EndTime>  
    <Input> 
      <Object>16k.mp3</Object> 
    </Input>  
    <JobId>s8988119ee2c911eab2cdd3817d4d5e64</JobId>  
    <Message/>  
    <Operation> 
      <Output> 
        <Bucket>test005-1251704708</Bucket>  
        <Object>1.txt</Object>  
        <Region>ap-chongqing</Region> 
      </Output>  
      <SpeechRecognition> 
        <ChannelNum>1</ChannelNum>  
        <ConvertNumMode>1</ConvertNumMode>  
        <EngineModelType>16k_zh</EngineModelType>  
        <FilterDirty>0</FilterDirty>  
        <FilterModal>0</FilterModal>  
        <ResTextFormat>0</ResTextFormat> 
      </SpeechRecognition>  
      <SpeechRecognitionResult> 
        <AudioTime>30.12</AudioTime>  
        <Result>[0:0.000,0:30.080] 这是一条语音测试信息，展示的是识别后的文本内容</Result>  
        <ResultDetail/> 
      </SpeechRecognitionResult> 
    </Operation>  
    <QueueId>p5275b560c7fd498db9a36e5e202827b6</QueueId>  
    <State>Success</State>  
    <Tag>SpeechRecognition</Tag> 
  </JobsDetail>  
  <NextToken>21</NextToken> 
</Response>

```

## 根据任务 ID 查询任务详情

#### 请求

```
GET /asr_jobs/s8988119ee2c911eab2cdd3817d4d5e64 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: application/xml
User-Agent: cos-python-sdk-v5.3.2
Host: chongqingtest-1251704708.ci.ap-chongqing.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597916951;1597927011&q-key-time=1597916951;1597927011&q-header-list=host&q-url-param-list=&q-signature=85ec7fbafd8ed9354fd37ae8667c2d3054ccdec9
```


#### 响应

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 08:22:41 GMT
Content-Type: application/xml
Content-Length: 641
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: request-id

<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-08-20T17:43:01+0800</CreationTime>
                <EndTime>2020-08-20T17:43:25+0800</EndTime>
                <Input>
                        <Object>16k.mp3</Object>
                </Input>
                <JobId>s8988119ee2c911eab2cdd3817d4d5e64</JobId>
                <Message/>
                <Operation>
                        <Output>
                                <Bucket>test005-1251704708</Bucket>
                                <Object>1.txt</Object>
                                <Region>ap-chongqing</Region>
                        </Output>
                        <SpeechRecognition>
                                <ChannelNum>1</ChannelNum>
                                <ConvertNumMode>1</ConvertNumMode>
                                <EngineModelType>16k_zh</EngineModelType>
                                <FilterDirty>0</FilterDirty>
                                <FilterModal>0</FilterModal>
                                <ResTextFormat>0</ResTextFormat>
                        </SpeechRecognition>
                        <SpeechRecognitionResult>
                                <AudioTime>30.12</AudioTime>
                                <Result>[0:0.000,0:30.080]  这是一条语音测试信息，展示的是识别后的文本内容</Result>
                                <ResultDetail/>
                        </SpeechRecognitionResult>
                </Operation>
                <QueueId>p5275b560c7fd498db9a36e5e202827b6</QueueId>
                <State>Success</State>
                <Tag>SpeechRecognition</Tag>
        </JobsDetail>
</Response>
```

## 查询 bucket 队列

#### 请求
```
GET /asrqueue?pageNumber=1&pageSize=5 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: chongqingtest-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597917121;1597927181&q-key-time=1597917121;1597927181&q-header-list=content-type;host&q-url-param-list=&q-signature=96322cc56f78ca161aaa6908f3d8af9105d21532
```

#### 响应

```
HTTP/1.1 200 OK
Date: Thu, 20 Aug 2020 09:53:02 GMT
Content-Type: application/xml
Content-Length: 674
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYzZTQ3ZmRfOTBmYTUwNjRfMjJhNl8z

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>1</TotalCount>
        <RequestId>NWYzZTQ3ZmRfOTBmYTUwNjRfMjJhNl8z</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>5</PageSize>
        <QueueList>
                <QueueId>pd0a7e02988c24db88b61551cf540444c</QueueId>
                <Name>queue-speech-1</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url/>
                        <Event/>
                        <Type/>
                        <State>Off</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>2020-08-20T17:52:33+0800</CreateTime>
                <UpdateTime>2020-08-20T17:52:33+0800</UpdateTime>
                <BucketId>chongqingtest-1251704708</BucketId>
                <Category>Speeching</Category>
        </QueueList>
</Response>
```

## 修改队列

#### 请求

```
PUT /asrqueue/pd0a7e02988c24db88b61551cf540444c HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: chongqingtest-1251704708.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 271
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597917374;1597927434&q-key-time=1597917374;1597927434&q-header-list=content-type;host&q-url-param-list=&q-signature=670ce7355f265cb0792c00e490a20597585602df

<?xml version="1.0" encoding="utf-8"?>

<Request>
  <QueueId>p5275b560c7fd498db9a36e5e202827b6</QueueId>
  <State>Active</State>
  <Name>test</Name>
  <NotifyConfig>
    <Url>http://google.com/</Url>
    <State>On</State>
    <Type>Url</Type>
    <Event>TransCodingFinish</Event>
  </NotifyConfig>
</Request>
```

#### 响应

```
HTTP/1.1 200 OK
Date: Thu, 20 Aug 2020 09:53:02 GMT
Content-Type: application/xml
Content-Length: 674
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYzZTQ3ZmRfOTBmYTUwNjRfMjJhNl8z

<Response>
        <RequestId>NWYzZTQ5NTdfZWM0YTYyNjRfNWE4ZF9lZjk=</RequestId>
        <Queue>
                <QueueId>p5275b560c7fd498db9a36e5e202827b6</QueueId>
                <Name>test</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url>http://google.com/</Url>
                        <Event>TransCodingFinish</Event>
                        <Type>Url</Type>
                        <State>On</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>2020-06-29T16:55:04+0800</CreateTime>
                <UpdateTime>2020-08-20T17:58:47+0800</UpdateTime>
                <BucketId>chongqingtest-1251704708</BucketId>
                <Category>Speeching</Category>
        </Queue>
</Response>
```

## 查询 bucketList

#### 请求
```
GET /asrbucket HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1597999958;1598010018&q-key-time=1597999958;1598010018&q-header-list=content-type;host&q-url-param-list=&q-signature=a3ae564aa6f9798a4a7389badf3cb54a59f7686e
```

#### 响应
```
HTTP/1.1 200 OK
Date: Fri, 21 Aug 2020 08:53:38 GMT
Content-Type: application/xml
Content-Length: 1309
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYzZjhiOTJfOTBmYTUwNjRfMjJiZF9l

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>5</TotalCount>
        <RequestId>NWYzZjhiOTJfOTBmYTUwNjRfMjJiZF9l</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <AsrBucketList>
                <Name>markjrzhang-1251704708</Name>
                <CreateTime>2020-05-26T13:31:41+0800</CreateTime>
                <Region>ap-chongqing</Region>
                <AliasBucketId/>
                <BucketId>markjrzhang-1251704708</BucketId>
        </AsrBucketList>
</Response>
```
