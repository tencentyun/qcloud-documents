## 简介

本文档提供关于媒体 bucket 接口的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
| [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通情况 |用于查询已经开通媒体处理功能的存储桶      |

## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

>! COS Go SDK 版本需要大于等于 v0.7.32。

#### 方法原型

```go
func (s *CIService) DescribeMediaProcessBuckets(ctx context.Context, opt *DescribeMediaProcessBucketsOptions) (*DescribeMediaProcessBucketsResult, *Response, error)
```

#### 请求示例
```go
// 需要设置 请求 URL 为 ci.<Region>.myqcloud.com
cu, _ := url.Parse("https://ci.ap-guangzhou.myqcloud.com")
b := &cos.BaseURL{CIURL: cu}
c := cos.NewClient(b, &http.Client{
    Transport: &cos.AuthorizationTransport{
        SecretID:  "SECRETID",
        SecretKey: "SECRETKEY",
    })

opt := &cos.DescribeMediaProcessBucketsOptions{
    Regions: "ap-guangzhou",
}
res, _, err := c.CI.DescribeMediaProcessBuckets(context.Background(), opt)
if err != nil {
    // ERROR       
}
fmt.Printf("res: %+v\n", res)
```

#### 参数说明

```go
type DescribeMediaProcessBucketsOptions struct {
        Regions     string
        BucketNames string
        BucketName  string
        PageNumber  int
        PageSize    int
}
```

| 参数名称 | 参数描述                                                     | 类型   | 是否必填 |
| :------- | :----------------------------------------------------------- | :----- | :------- |
| Regions  | 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066) | string | 否 |
| BucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索 | string | 否 |
| BucketName | 存储桶名称前缀，前缀搜索                        | string | 否   |
| PageNumber | 第几页                                          | string | 否   |
| PageSize   | 每页个数                                        | string | 否   |

#### 返回结果说明

```go
type DescribeMediaProcessBucketsResult struct {
        RequestId       string
        TotalCount      int
        PageNumber      int
        PageSize        int
        MediaBucketList []MediaProcessBucket
}
type MediaProcessBucket struct {
        BucketId   string
        Region     string
        CreateTime string
}
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点   | 描述                            | 类型      |
| :----------------- | :------- | :------------------------------ | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 媒体 Bucket 总数                | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| MediaBucketList    | Response | 媒体 Bucket 列表                | Container |

Container 节点 MediaBucketList 的内容：

| 节点名称（关键字） | 父节点                   | 描述                    | 类型   |
| :----------------- | :----------------------- | :---------------------- | :----- |
| BucketId           | Response.MediaBucketList | 存储桶 ID               | String |
| Name               | Response.MediaBucketList | 存储桶名称，同 BucketId | String |
| Region             | Response.MediaBucketList | 所在的地域              | String |
| CreateTime         | Response.MediaBucketList | 创建时间                | String |


