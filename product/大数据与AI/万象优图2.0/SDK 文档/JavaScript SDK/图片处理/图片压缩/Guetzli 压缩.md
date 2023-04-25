## 简介

本文档提供关于 Guetzli 压缩接口的 API 概览以及 SDK 示例代码。

| API                                                            | 操作描述     |
|----------------------------------------------------------------|----------|
| [开通 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30112) | 开通 Guetzli 压缩功能 |
| [查询 Guetzli 状态](https://cloud.tencent.com/document/product/460/30111) | 查询 Guetzli 压缩功能是否开启 |
| [关闭 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30113) | 关闭 Guetzli 压缩功能 |


## 开通 Guetzli 压缩

#### 功能说明

对 Bucket 开通 Guetzli 压缩功能。

#### 示例代码

```javascript
function openImageGuetzli() {
    var config = {
        // 需要替换成您自己的存储桶信息
        Bucket: 'examplebucket-1250000000', /* 存储桶，必须 */
        Region: 'COS_REGION', /* 存储桶所在地域，必须字段 */
    };
    var host = config.Bucket + '.pic.' + config.Region + '.myqcloud.com/?guetzli';
    var url = 'https://' + host;
    cos.request({
            Method: 'PUT',
            Url: url,
        },
        function(err, data){
            logger.log(err || data);
        });
}
openImageGuetzli();
```

#### 参数说明
无

#### 返回结果说明

详情请参见 [开通 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30112#.E5.93.8D.E5.BA.94) 。

## 查询 Guetzli 状态

#### 功能说明

用于查询 Guetzli 压缩功能是否开启。

#### 示例代码

```javascript
function describeImageGuetzli() {
    var config = {
        // 需要替换成您自己的存储桶信息
        Bucket: 'examplebucket-1250000000', /* 存储桶，必须 */
        Region: 'COS_REGION', /* 存储桶所在地域，必须字段 */
    };
    var host = config.Bucket + '.pic.' + config.Region + '.myqcloud.com/?guetzli';
    var url = 'https://' + host;
    cos.request({
            Method: 'GET',
            Url: url,
        },
        function(err, data){
            logger.log(err || data);
        });
}
describeImageGuetzli();
```

#### 参数说明
无

#### 返回结果说明

详情请参见 [查询 Guetzli 状态](https://cloud.tencent.com/document/product/460/30111#.E5.93.8D.E5.BA.94) 。


## 关闭 Guetzli 压缩

#### 功能说明

用于删除某一特定样式。

#### 示例代码

```javascript
function closeImageGuetzli() {
    var config = {
        // 需要替换成您自己的存储桶信息
        Bucket: 'examplebucket-1250000000', /* 存储桶，必须 */
        Region: 'COS_REGION', /* 存储桶所在地域，必须字段 */
    };
    var host = config.Bucket + '.pic.' + config.Region + '.myqcloud.com/?guetzli';
    var url = 'https://' + host;
    cos.request({
            Method: 'DELETE',
            Url: url,
        },
        function(err, data){
            logger.log(err || data);
        });
}
closeImageGuetzli();
```

#### 参数说明
无

#### 返回结果说明

详情请参见 [关闭 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30113#.E5.93.8D.E5.BA.94) 。

