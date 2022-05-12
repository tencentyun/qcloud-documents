## 简介

本文档提供关于媒体 bucket 接口的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
| [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通情况 |用于查询已经开通媒体处理功能的存储桶      |

## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

>! COS Javascript SDK 版本需要大于等于 v1.3.1。


#### 使用示例
```js
var config = {
  // 需要替换成您自己的存储桶信息
  Bucket: 'examplebucket-1250000000', /* 存储桶，必须 */
  Region: 'COS_REGION', /* 存储桶所在地域，必须字段 */
};
var host = 'ci.' + config.Region + '.myqcloud.com';
var url = 'https://' + host + '/mediabucket';
cos.request({
    Bucket: config.Bucket,
    Region: config.Region,
    Method: 'GET',
    Key: 'mediabucket', /** 固定值，必须 */
    Url: url,
    Query: {
        pageNumber: '1', /** 第几页，非必须 */
        pageSize: '10', /** 每页个数，非必须 */
        // regions: 'ap-chengdu', /** 地域信息，例如'ap-beijing'，支持多个值用逗号分隔如'ap-shanghai,ap-beijing'，非必须 */
        // bucketNames: 'test-1250000000', /** 存储桶名称，精确搜索，例如'test-1250000000'，支持多个值用逗号分隔如'test1-1250000000,test2-1250000000'，非必须 */
        // bucketName: 'test', /** 存储桶名称前缀，前缀搜索，例如'test'，支持多个值用逗号分隔如'test1,test2'，非必须 */
    }
}, function (err, data) {
    console.log(err || data);
});
```

#### 参数说明

| 参数名称 | 参数描述                                                     | 类型   | 是否必填 |
| :------- | :----------------------------------------------------------- | :----- | :------- |
| Bucket                     | 存储桶的名称，命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String   | 是   |
| Region                     | 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) | String   | 是   |
| Key                        | 固定值: mediabucket | String   | 是   |
| PageNumber | 第几页                                          | String | 否   |
| PageSize   | 每页个数                                        | String | 否   |
| Regions  | 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066) | String | 否 |
| BucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索 | String | 否 |
| BucketName | 存储桶名称前缀，前缀搜索                        | String | 否   |


#### 回调函数说明

```
function(err, data) { ... }
```

| 参数名       | 参数描述                                                     | 类型   |
| ------------ | ------------------------------------------------------------ | ------ |
| err          | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) | Object |
| - statusCode | 请求返回的 HTTP 状态码，例如200、403、404等                  | Number |
| - headers    | 请求返回的头部信息                                           | Object |
| data         | 请求成功时返回的对象，如果请求发生错误，则为空               | Object |
| - statusCode | 请求返回的 HTTP 状态码，例如200、403、404等                  | Number |
| - headers    | 请求返回的头部信息                                           | Object |
| - Response       | 响应结果 | Object |
| - - RequestId          | 请求的唯一 ID                   | String    |
| - - TotalCount         | 媒体 Bucket 总数                | String       |
| - - PageNumber         | 当前页数，同请求中的 pageNumber | String       |
| - - PageSize           | 每页个数，同请求中的 pageSize   | String       |
| - - MediaBucketList    | 媒体 Bucket 列表                | Object |
| - - - BucketId           | 存储桶 ID               | String |
| - - - Name               | 存储桶名称，同 BucketId | String |
| - - - Region             | 所在的地域              | String |
| - - - CreateTime         | 创建时间                | String |





