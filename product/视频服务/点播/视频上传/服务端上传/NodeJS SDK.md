对于在服务端上传视频的场景，云点播提供 NodeJS SDK 来实现。上传流程请参见 [服务端上传指引](https://cloud.tencent.com/document/product/266/9759)。

## 集成方式

### 使用 npm 安装
```
npm i vod-node-sdk --save
```

### 通过源码包安装
如果项目中没有使用 npm 工具进行依赖管理，可以直接下载源码导入项目中使用：

* [从 Github 访问](https://github.com/tencentyun/vod-node-sdk)
* [单击下载 NodeJS SDK](https://github.com/tencentyun/vod-node-sdk/archive/master.zip)

##  简单视频上传
### 初始化上传对象
使用云 API 密钥初始化 VodUploadClient 实例。

```
const { VodUploadClient, VodUploadRequest } = require('vod-node-sdk');

client = new VodUploadClient("your secretId", "your secretKey");
```

### 构造上传请求对象
```
let req = new VodUploadRequest();
req.MediaFilePath = "/data/file/Wildlife.mp4";
```

### 调用上传
调用上传方法，传入上传地域及上传请求，通过回调方法获取返回的信息。
```
client.upload("ap-guangzhou", req, function (err, data) {
    if (err) {
        // 处理业务异常
        console.log(err)
    } else {
        // 获取上传成功后的信息
        console.log(data.FileId);
        console.log(data.MediaUrl);
    }
});
```

>?上传方法根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。

## 高级功能
### 携带封面
```
const { VodUploadClient, VodUploadRequest } = require('vod-node-sdk');

client = new VodUploadClient("your secretId", "your secretKey");
let req = new VodUploadRequest();
req.MediaFilePath = "/data/file/Wildlife.mp4";
req.CoverFilePath = "/data/file/Wildlife-cover.png";
client.upload("ap-guangzhou", req, function (err, data) {
    if (err) {
        // 处理业务异常
        console.log(err)
    } else {
        // 获取上传成功后的信息
        console.log(data.FileId);
        console.log(data.MediaUrl);
        console.log(data.CoverUrl);
    }
});
```

### 指定任务流
首先 [创建任务流模板](https://cloud.tencent.com/document/product/266/33819) 并为模板命名，发起任务流时，可以用任务流模板名设置`Procedure`参数，上传成功后会自动执行任务流。
```
const { VodUploadClient, VodUploadRequest } = require('vod-node-sdk');

client = new VodUploadClient("your secretId", "your secretKey");
let req = new VodUploadRequest();
req.MediaFilePath = "/data/file/Wildlife.mp4";
req.Procedure = "Your Procedure Name";
client.upload("ap-guangzhou", req, function (err, data) {
    if (err) {
        // 处理业务异常
        console.log(err)
    } else {
        // 获取上传成功后的信息
        console.log(data.FileId);
        console.log(data.MediaUrl);
    }
});
```

### 子应用上传
传入 [子应用](https://cloud.tencent.com/document/product/266/14574) ID，上传成功后资源只属于具体的子应用。
```
const { VodUploadClient, VodUploadRequest } = require('vod-node-sdk');

client = new VodUploadClient("your secretId", "your secretKey");
let req = new VodUploadRequest();
req.MediaFilePath = "/data/file/Wildlife.mp4";
req.SubAppId = 101;
client.upload("ap-guangzhou", req, function (err, data) {
    if (err) {
        // 处理业务异常
        console.log(err)
    } else {
        // 获取上传成功后的信息
        console.log(data.FileId);
        console.log(data.MediaUrl);
    }
});
```

## 接口描述
上传客户端类`VodUploadClient`

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| secretId   | 云 API 密钥 ID。        | String | 是    |
| secretKey | 云 API 密钥 Key。 | String  | 是    |

上传请求类`VodUploadRequest`

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| MediaFilePath   | 媒体文件路径，路径为本地路径，不支持 URL 路径。         | String | 是    |
| MediaType   | 媒体文件类型，可选类型请参见 [视频上传综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)，若 MediaFilePath 路径带后缀可不填。       | String | 否    |
| MediaName   | 媒体名称，若不填默认采用 MediaFilePath 的文件名。      | String | 否    |
| CoverFilePath   | 封面文件路径。        | String | 否    |
| CoverType   | 媒体文件类型，可选类型请参见 [视频上传综述](/document/product/266/9760#.E5.B0.81.E9.9D.A2.E7.B1.BB.E5.9E.8B)，若 CoverFilePath 路径带后缀可不填。        | String | 否    |
| Procedure   | 任务流，具体的任务流介绍请参见 [参数模版与任务流](https://cloud.tencent.com/document/product/266/33475#.E5.8F.82.E6.95.B0.E6.A8.A1.E6.9D.BF)。        | String | 否    |
| ExpireTime   | 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。        | String | 否    |
| ClassId   | 分类 ID，用于对媒体进行分类管理，可通过 [创建分类](https://cloud.tencent.com/document/product/266/31772) 接口，创建分类，获得分类 ID。        | Integer | 否    |
| SourceContext   | 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长250个字符。        | String | 否    |
| SubAppId   | 云点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID，否则无需填写该字段。        | Integer | 否    |

上传响应类`VodUploadResponse`

| 属性名称      | 属性描述                   | 类型      |
| --------- | ---------------------- | ------- |
| FileId   | 媒体文件的唯一标识。         | String |
| MediaUrl | 媒体播放地址。  | String  |
| CoverUrl | 媒体封面地址。  | String  |
| RequestId | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。  | String  |

上传方法`VodUploadClient.upload(String region, VodUploadRequest request, function callback)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| region   | 上传地域，具体参考支持的 [地域列表](https://cloud.tencent.com/document/product/266/31756#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。       | String | 是    |
| request   | 上传请求。       | VodUploadRequest | 是    |
| callback   | 上传完成回调函数。        | function | 是    |

上传完成回调函数`function(err, data)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| err   | 错误信息。       | Exception | 是    |
| data   | 上传响应结果。       | VodUploadResponse | 是    |

## 错误码表

| 状态码         | 含义               |
| ----------- | ----------------- |
| InternalError       | 内部错误。  |
| InvalidParameter.ExpireTime       | 参数值错误：过期时间。  |
| InvalidParameterValue.CoverType       | 参数值错误：封面类型。      |
| InvalidParameterValue.MediaType       | 参数值错误：媒体类型。            |
| InvalidParameterValue.SubAppId       | 参数值错误：子应用 ID。               |
| InvalidParameterValue.VodSessionKey       | 参数值错误：点播会话。               |
| ResourceNotFound       | 资源不存在。               |
