## 简介

本文将介绍如何使用 APICloud 快速集成 cos 功能模块并开发跨平台应用。

## APICloud 相关资源

- [官网以及文档](https://www.apicloud.com/mod_detail/147670)
- [视频教程](https://ke.qq.com/course/5911100/14831329532850748#term_id=106129926)

## 准备
按照 APICloud 教程创建 App，并在模块库中搜索 cosClient 模块并点击添加。

## cosClient 简单使用

### 1. 获取模块实例

```
var demo = api.require('cosClient');
```

### 2. 配置密钥

COS SDK 模块提供两种密钥配置方法：

- #### 临时密钥（推荐使用）
  在 script 标签中实现如下：
```
function refreshCredentail() {
    // 通过请求接口获取临时密钥 secretID 、secretKey、token、startDate、expirationDate；
    // 拼接成如下格式 返回即可；
    return  "secretID=***&secretKey=***&token=***&startDate=***&expirationDate=***";
}
```
- #### 永久密钥
  在注册服务之前设置永久密钥：
```
var demo = api.require('cosClient');
demo.setupPermanentCredentail({"secretID":secretID,"secretKey":secretKey});
```

### 3. 注册 cos 服务实例
```
demo.registerTransferManger({"serviceKey":"test","useHttps":true})
```


## cosClient 接口文档

### 1. 注册基础服务

#### 实例代码
```
var demo = api.require('cosClient');
demo.registerServiceForKey({"serviceKey":"test","useHttps":true})
```

#### 参数说明
- 请求参数

| 参数名      | 类型   | 说明                                                         | 是否必传 |
| ----------- | ------ | ------------------------------------------------------------ | -------- |
| serviceKey  | 字符串 | cos 服务实例唯一标识，不传则注册默认服务                      | 否       |
| appId       | 字符串 | 您的 AppID                                                    | 否       |
| region      | 字符串 | 服务地域名称,可用的服务地域名称请查看官网 ` https://www.qcloud.com/document/product/436/6224 ` 中提供的地域，这里填入官网里提供的地域简称，例如 ap-beijing 等。 | 否       |
| isPrefixURL | 布尔值 |             -                                                 | 否       |
| timeOut     | 整型   | 超时时间                                                     | 否       |
| serviceName | 字符串 | 服务的基础名称, 默认值为:  myqcloud.com                      | 否       |
| suffix      | 字符串 | 自定义域名：`http://bucketname.suffix` 未指定该参数，该存储桶 host 为 http://bucketname.**** 。 指定该参数为 testsuffix，该存储桶 host 为 http://bucketname.testsuffix.**** 。 在 IOS 端生效。 | 否       |
| useHttps    | 布尔值 | 是否使用 https                                                | 否       |
| userAgent   | 字符串 | 设置自定义 ua                                                 | 否       |
| host        | 字符串 | 自定义域名，不包含“http://”， 在 Android 端生效                   | 否       |
| port        | 整型   | 自定义端口， 在 Android 端生效                                    | 否       |

- 返回参数
无

### 2. 注册传输服务

#### 实例代码

```
var demo = api.require('cosClient');
demo.registerTransferManger({"serviceKey":"test","useHttps":true})
```

#### 参数说明

- 请求参数

| 参数名      | 类型   | 说明                                                         | 是否必传 |
| ----------- | ------ | ------------------------------------------------------------ | -------- |
| serviceKey  | 字符串 | cos 服务实例唯一标识，不传则注册默认服务                      | 否       |
| appId       | 字符串 | 您的 AppID                                                    | 否       |
| region      | 字符串 | 服务地域名称,可用的服务地域名称请查看官网 ` https://www.qcloud.com/document/product/436/6224` 中提供的地域，这里填入官网里提供的地域简称，例如 ap-beijing 等。 | 否       |
| isPrefixURL | 布尔值 |          -                                                    | 否       |
| timeOut     | 整型   | 超时时间                                                     | 否       |
| serviceName | 字符串 | 服务的基础名称, 默认值为:  myqcloud.com                      | 否       |
| suffix      | 字符串 | 自定义域名：`http://bucketname.suffix ` 未指定该参数，该存储桶 host 为 http://bucketname.**** 。 指定该参数为 testsuffix，该存储桶 host 为 http://bucketname.testsuffix.**** 。在 IOS端生效。 | 否       |
| useHttps    | 布尔值 | 是否使用 https                                                | 否       |
| userAgent   | 字符串 | 设置自定义 ua                                                 | 否       |
| host        | 字符串 | 自定义域名，不包含“http://”， 在 Android 端生效                   | 否       |
| port        | 整型   | 自定义端口， 在 Android 端生效                                    | 否       |

- 返回参数
无


### 3. 获取桶列表

#### 实例代码

```
/// 模块名称 cosClient，用过模块名拿到模块实例。
var demo = api.require('cosClient');
demo.getBucketList(
    {"serviceKey":"test"}
    ,function(ret,err){
        /// err 为空时,返回""
        if(err != ""){
            alert(err.data);
        }else{
            alert(ret.data);
        }
});
```

#### 参数说明

- 请求参数

| 参数名     | 类型   | 说明                                                    | 是否必传 |
| ---------- | ------ | ------------------------------------------------------- | -------- |
| serviceKey | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求 | 否       |

- 返回参数
```
{
    "result":"success",
    "data":{
    buckets =     [ /// 桶列表
                {
            createDate = "2021-06-02T07:33:33Z"; /// 创建时间
            location = "ap-chengdu"; /// 地域
            name = "0-1253960454";  /// 桶名称
            type = ""; 存储桶类型
        }];
    owner =     {
        displayName = 2832742109; /// 持有者的名称
        id = "qcs::cam::uin/2832742109:uin/2832742109"; /// 持有者 ID，
    };
}
}

```

### 4. 删除存储桶

#### 实例代码

```
/// 模块名称 cosClient，用过模块名拿到模块实例。
var demo = api.require('cosClient');
demo.deleteBucket({
    "serviceKey":"test",
    "region":"ap-chengdu",
    "bucket":"0-appid",},
    function(ret,err){
    /// err 为空时,返回""
    if(err != ""){
        alert(err.data);
    }else{
        alert(ret.data);
    }
});
```

#### 参数说明

- 请求参数

| 参数名     | 类型   | 说明                                                    | 是否必传 |
| ---------- | ------ | ------------------------------------------------------- | -------- |
| serviceKey | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求 | 否       |
| region     | 字符串 | 桶地域                                                  | 是       |
| bucket     | 字符串 | 存储桶名称，格式为 BucketName-APPID                     | 是       |

- 返回参数
 - 删除成功
```
{
    "result":"success"
}
```
 - 删除失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```

### 5. 创建存储桶

#### 实例代码

```
/// 模块名称 cosClient，用过模块名拿到模块实例。
var demo = api.require('cosClient');
demo.createBucket({
"serviceKey":"test",
"name":"apicloudtest",
"appId":"appId",
"region":"ap-chengdu"},function(ret,err){
    /// err 为空时,返回""
    if(err != ""){
        alert(err.data);
    }else{
        alert(ret.data);
    }
});
```

#### 参数说明

- 请求参数

| 参数名            | 类型   | 说明                                                         | 是否必传 |
| ----------------- | ------ | ------------------------------------------------------------ | -------- |
| serviceKey        | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求      | 否       |
| name              | 字符串 | 桶名称不包含 appid                                            | 是       |
| appId             | 字符串 | 用户 appid                                                    | 是       |
| region            | 字符串 | 桶地域                                                       | 是       |
| accessControlList | 字符串 | 定义 bucket 的 acl 属性。有效值：private，public-read-write，public-read；默认值：private | 否       |
| readAccount       | 字符串 | 赋予被授权者读的权限,id="OwnerUin"；                         | 否       |
| writeAccount      | 字符串 | 赋予被授权者写的权限。格式: id="OwnerUin"；                  | 否       |
| readWriteAccount  | 字符串 | 赋予被授权者读写权限。格式: id="OwnerUin"；                  | 否       |
| enableMAZ         | 布尔值 | 是否使用多 AZ，默认否                                         | 否       |

- 返回参数
 - 创建成功
```
{
    "result":"success"
}
```
 - 创建失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```


### 6. 获取存储桶内容

#### 实例代码

```
var demo = api.require('cosClient');
demo.listBucketContent({"serviceKey":"test","bucket":"0-appid","region":"ap-chengdu"},function(ret,err){
    /// err 为空时,返回""
    if(err != ""){
        alert(err.data);
    }else{
        alert(ret.data);
    }
});
```

#### 参数说明

- 请求参数

| 参数名     | 类型   | 说明                                                         | 是否必传 |
| ---------- | ------ | ------------------------------------------------------------ | -------- |
| serviceKey | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求      | 否       |
| region     | 字符串 | 桶地域                                                       | 是       |
| bucket     | 字符串 | 存储桶名称，格式为 BucketName-APPID                          | 是       |
| prefix     | 字符串 | 前缀匹配，用来规定返回的文件前缀地址                         | 否       |
| delimiter  | 字符串 | 定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 | 否       |
| marker     | 字符串 | 默认以 UTF-8二进制顺序列出条目，所有列出条目从 marker 开始      | 否       |
| maxKeys    | 字符串 | 单次返回的最大条目数量，默认1000                             | 否       |


- 返回参数

 - 获取成功
```
{
    "result":"success",
    "data":{
        "Contents":[
            {
                "ETag":"\"c57b7cd3647561480b355a92dc2e971a\"", // 根据对象内容计算出的 MD5 算法校验值，
例如"22ca88419e2ed4721c23807c678adbe4c08a7880"，注意前后携带双引号
                "Owner":{
                    "ID":"1253960454", // 对象持有者的完整 ID，格式为qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]，
例如 qcs::cam::uin/100000000001:uin/100000000001，其中100000000001为 uin
                    "DisplayName":"1253960454" // 对象持有者的名称
                },
                "StorageClass":"STANDARD", // 类型标准
                "Key":"02_常用语法.pdf", // 文件名
                "LastModified":"2023-01-09T11:15:25.000Z", // 最后修改时间
                "Size":816838 // 文件大小
            }
        ],
        "MaxKeys":1000, 
        "IsTruncated":"False",// 响应请求条目是否被截断，值为 'true' 或者 'false'
        "CommonPrefixes":[  // 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix
            {
                "Prefix":"1\/" // 单条 Common Prefix 的前缀
            }
        ],
        "Delimiter":"\/", // 定界符
        "Name":"0-1253960454" // 存储桶的名称，格式为 BucketName-APPID，例如 examplebucket-1250000000
}
}
```
 - 获取失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```

### 7. 上传文件

#### 实例代码

```
var uploadTaskId;
var demo = api.require('cosClient');
demo.uploadObject({
    "serviceKey":"test",
    "region":"ap-chengdu",
    "bucket":"0-appid",
    "filePath":"file://test.jpg",
    "object":"test.gif"},function(ret,err){
        if(err != ""){
            alert(err.data);
        }else{
            if(ret.result == "begin"){
                // 在 begin 时，拿到 taskId，用于取消任务。
                uploadTaskId = JSON.parse(ret.data).taskId;
                alert(uploadTaskId);
            }
        }
});
```

#### 参数说明

- 请求参数

| 参数名             | 类型   | 说明                                                         | 是否必传 |
| ---------------- | ----------- | ------------------------------------------------------------ | -------- |
| serviceKey         | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求      | 否       |
| region             | 字符串 | 桶地域                                                       | 是       |
| bucket             | 字符串 | 存储桶名称，格式为 BucketName-APPID                          | 是       |
| object             | 字符串 | 上传到服务端的文件名                                         | 是       |
| filePath           | 字符串 | 本地文件路径                                                 | 是       |
| uploadId           | 字符串 | 在第一次上传文件时无需设置，再次续传时需要设置               | 否       |
| stroageClass       | 字符串 | 对象的存储级别                                               | 否       |
| trafficLimit       | 字符串 | 针对本次下载行流量控制的限速值，必须为数字，单位默认为 bit/s。限速值设置范围为819200 - 838860800,即100KB/s - 100MB/s，如果超出该范围将返回400错误 | 否       |
| enableVerification | 字符串 | 是否在上传完成以后，将 COS 返回的文件 MD5与本地文件算出来的 md5进行校验。默认开启，如果校验出错，文件仍然会被上传到 COS, 不过我们会在本地抛出校验失败的 error。 | 否       |


- 返回参数

 - 上传初始化阶段
```
{
    "result":"begin",
    "data":{
       "taskId":taskId, // 当前任务 ID，用户取消任务。
       "uploadId":uploadId // 当前上传 ID，用于续传。
    }
}
```

 - 上传阶段
```
{
    "result":"processing",
    "data":{
       "totalBytesSent":totalBytesSent, // 当前传输进度。
       "totalBytesExpectedToSend":totalBytesExpectedToSend // 文件总大小。
    }
}
```

 - 完成

 - 上传成功
```
{
    "result":"success",
    "data":{} // 文件信息
}
```

 - 上传失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```

### 8.  暂停上传
#### 实例代码

```
var demo = api.require('cosClient');
// uploadTaskId 为从上传接口中获取 由业务保存。
demo.pauseUploadObject({"taskId":uploadTaskId});
```

#### 请求参数

| 参数名 | 类型   | 说明                                        | 是否必传 |
| ------ | ------ | ------------------------------------------- | -------- |
| taskId | 字符串 | 上传接口中获取 由业务保存，用于取消当前任务 | 否       |


### 9. 下载文件

#### 实例代码

```
var downloadTaskId;
var demo = api.require('cosClient');
demo.registerTransferManger({"serviceKey":"test","useHttps":true})
demo.uploadObject({
    "serviceKey":"test",
    "region":"ap-chengdu",
    "bucket":"0-appid",
    "filePath":"0-1253960454",
    "object":"test.gif"},function(ret,err){
        if(err != ""){
            alert(err.data);
        }else{
            if(ret.result == "begin"){
                // 在 begin 时，拿到 taskId，用于取消任务。
                downloadTaskId = JSON.parse(ret.data).taskId;
                alert(downloadTaskId);
            }
        }
});
```

#### 参数说明

- 请求参数

| 参数名             | 类型   | 说明                                                         | 是否必传 |
| ------------------ | ------ | ------------------------------------------------------------ | -------- |
| serviceKey         | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求      | 否       |
| region             | 字符串 | 桶地域                                                       | 是       |
| bucket             | 字符串 | 存储桶名称，格式为 BucketName-APPID                          | 是       |
| object             | 字符串 | 服务端的文件名                                               | 是       |
| versionId          | 字符串 | 文件版本号                                                   | 否       |
| localPath          | 字符串 | 本地文件路径                                                 | 是       |
| trafficLimit       | 字符串 | 针对本次下载行流量控制的限速值，必须为数字，单位默认为 bit/s。限速值设置范围为819200 - 838860800,即100KB/s - 100MB/s，如果超出该范围将返回400错误 | 否       |
| enableVerification | 字符串 | 是否在上传完成以后，将 COS 返回的文件 MD5与本地文件算出来的 MD5进行校验。默认开启，如果校验出错，文件仍然会被上传到 COS, 不过我们会在本地抛出校验失败的 error。默认校验。 | 否       |


- 返回参数

 - 下载初始化阶段
```
{
    "result":"begin",
    "data":{
       "taskId":taskId, // 当前任务 ID，用户取消任务。
    }
}
```

 - 下载阶段
```
{
    "result":"processing",
    "data":{
       "totalBytesDownload":totalBytesDownload, // 当前传输进度。
       "totalBytesExpectedToDownload":totalBytesExpectedToDownload // 文件总大小。
    }
}
```

 - 完成

 -  下载成功
```
{
    "result":"success",
    "data":{} // 文件信息
}
```

 -  下载失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```

### 10. 暂停下载

#### 实例代码
```
var demo = api.require('cosClient');
// uploadTaskId 为从下载接口中获取 由业务保存。
demo.pauseDownloadObject({"taskId":downloadTaskId});
```

#### 请求参数

| 参数名 | 类型   | 说明                                        | 是否必传 |
| ------ | ------ | ------------------------------------------- | -------- |
| taskId | 字符串 | 下载接口中获取 由业务保存，用于取消当前任务 | 否       |


### 11. 获取文件信息

#### 实例代码

```
var demo = api.require('cosClient');
demo.headObject({
    "serviceKey":"test",
    "region":"ap-chengdu",
    "bucket":"0-appid",
    "object":"test.jpg"},function(ret,err){
        if(err != ""){
            alert(err.data);
        }else{
            alert(ret.data);
        }
});
```

#### 参数说明

- 请求参数

| 参数名     | 类型   | 说明                                                    | 是否必传 |
| ---------- | ------ | ------------------------------------------------------- | -------- |
| serviceKey | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求 | 否       |
| region     | 字符串 | 桶地域                                                  | 是       |
| bucket     | 字符串 | 存储桶名称，格式为 BucketName-APPID                     | 是       |
| object     | 字符串 | 服务端的文件名                                          | 是       |
| versionId  | 字符串 | 文件版本号                                              | 否       |


- 返回参数

 - 获取成功
```
{
    "result":"success",
    "data":{} // 文件对象信息
}
```

 - 获取失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```


### 12. 暂停下载

#### 实例代码

```
var demo = api.require('cosClient');
// uploadTaskId 为从下载接口中获取 由业务保存。
demo.pauseDownloadObject({"taskId":uploadTaskId});
```

#### 请求参数

| 参数名 | 类型   | 说明                                        | 是否必传 |
| ------ | ------ | ------------------------------------------- | -------- |
| taskId | 字符串 | 下载接口中获取 由业务保存，用于取消当前任务 | 否       |


### 13. 删除文件

#### 实例代码

```
var demo = api.require('cosClient');
demo.deleteObject({
    "serviceKey":"test",
    "region":"ap-chengdu",
    "bucket":"0-1253960454",
    "object":"test.jpg"},function(ret,err){
        if(err != ""){
            alert(err.data);
        }else{
            alert(ret.result);
            
        }
});
```

#### 参数说明

- 请求参数

| 参数名     | 类型   | 说明                                                    | 是否必传 |
| ---------- | ------ | ------------------------------------------------------- | -------- |
| serviceKey | 字符串 | cos 服务实例唯一标识，不传则使用默认服务实例进行网络请求 | 否       |
| region     | 字符串 | 桶地域                                                  | 是       |
| bucket     | 字符串 | 桶名称-AppId                                            | 是       |
| object     | 字符串 | 服务端的文件名                                          | 是       |
| versionId  | 字符串 | 文件版本号                                              | 否       |


- 返回参数

 - 删除成功
```
{
    "result":"success",
}
```

 - 删除失败并返回错误信息
```
{
    "result":"error",
    "error":{} /// 错误信息
}
```

### 14. 取消所有请求任务

#### 实例代码

```
var demo = api.require('cosClient');
demo.cancelAll({
    "serviceKey":"test"
    },function(ret,err){
        if(err != ""){
            alert(err.data);
        }else{
            alert(ret.result);
            
        }
});
```

#### 参数说明

- 请求参数

|  参数名   | 类型  | 说明 | 是否必传 |
|  ----  | ----  | --- | --- |
| serviceKey  | 字符串 | cos服务实例唯一标识，取消对应服务实例发起的网络请求 | 否 |

- 返回参数
无


