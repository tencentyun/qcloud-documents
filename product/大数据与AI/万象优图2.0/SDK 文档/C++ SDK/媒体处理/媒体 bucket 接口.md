## 简介

本文档提供关于媒体 bucket 的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
|  [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988)  |  查询媒体处理开通情况    |    用于查询已经开通媒体处理功能的存储桶         |


## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

#### 方法原型

```cpp
CosResult DescribeMediaBuckets(const DescribeMediaBucketsReq& request, DescribeMediaBucketsResp* response);
```

#### 示例代码

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
DescribeMediaBucketsReq req;
DescribeMediaBucketsResp resp;
req.SetRegions("ap-guangzhou");
// 设置存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
// req.SetBucketNames("xxx");
// 设置存储桶名称前缀，前缀搜索
// req.SetBucketName("xxx");
// 设置第几页
// req.SetPageNumber();
// 设置每页个数
// req.SetPageSize();
CosResult result = cos.DescribeMediaBuckets(req, &resp);
qcloud_cos::CosResult result = cos.GetObject(req, &resp);
if (result.IsSucc()) {
   // 调用成功，调用 resp 的成员函数获取返回内容
   std::cout << "Result: " << resp.GetResult().to_string() << std::endl;
} else {
   // 调用失败，调用 result 的成员函数获取错误信息
} 
```

#### 参数说明

| 参数名称           | 参数描述                                                     | 类型    | 是否必填 |
| ------------------ | ------------------------------------------------------------ | ------- | ------------------ |
| request     | 操作的请求                                              | DescribeMediaBucketsReq | 是 |
| response | 操作的响应                                    | DescribeMediaBucketsResp | 是 |

