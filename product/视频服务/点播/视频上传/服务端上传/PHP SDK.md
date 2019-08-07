对于在服务端上传视频的场景，云点播提供 PHP SDK 来实现。上传流程请参见 [服务端上传指引](/document/product/266/9759)。

## 集成方式

### 使用 composer 引入
```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v2.2.0"
    }
}
```

### 通过源码包安装
如果项目中没有使用 composer 工具进行依赖管理，可以直接下载源码，导入项目中使用：

* [从 Github 访问](https://github.com/tencentyun/vod-php-sdk-v5)
* [单击下载 PHP SDK](https://github.com/tencentyun/vod-php-sdk-v5/raw/master/packages/vod-sdk.zip)

解压 vod-sdk.zip 文件到项目中，引入 autoload.php 文件即可使用。

##  简单视频上传
### 初始化上传对象
使用云 API 密钥初始化 VodUploadClient 实例。

**使用 composer 导入**
```
<?php
require 'vendor/autoload.php';

use Vod\VodUploadClient;

$client = new VodUploadClient("your secretId", "your secretKey");
```

**使用源码导入**
```php
<?php
require 'vod-sdk-v5/autoload.php';

use Vod\VodUploadClient;

$client = new VodUploadClient("your secretId", "your secretKey");
```

### 构造上传请求对象
```
use Vod\Model\VodUploadRequest;

$req = new VodUploadRequest();
$req->MediaFilePath = "/data/videos/Wildlife.wmv";
```

### 调用上传
调用上传方法，传入上传地域及上传请求。
```
try {
    $rsp = $client->upload("ap-guangzhou", $req);
    echo "FileId -> ". $rsp->FileId . "\n";
    echo "MediaUrl -> ". $rsp->MediaUrl . "\n";
} catch (Exception $e) {
    // 处理上传异常
    echo $e;
}
```

## 高级功能
### 携带封面
```
<?php
require 'vendor/autoload.php';

use Vod\VodUploadClient;
use Vod\Model\VodUploadRequest;

$client = new VodUploadClient("your secretId", "your secretKey");
$req = new VodUploadRequest();
$req->MediaFilePath = "/data/videos/Wildlife.wmv";
$req->CoverFilePath = "/data/videos/Wildlife-Cover.png";
try {
    $rsp = $client->upload("ap-guangzhou", $req);
    echo "FileId -> ". $rsp->FileId . "\n";
    echo "MediaUrl -> ". $rsp->MediaUrl . "\n";
    echo "CoverUrl -> ". $rsp->CoverUrl . "\n";
} catch (Exception $e) {
    // 处理上传异常
    echo $e;
}
```

### 指定任务流
首先 [创建任务流模板](https://cloud.tencent.com/document/product/266/33819) 并为模板命名，发起任务流时，可以用任务流模板名设置`Procedure`参数，上传成功后会自动执行任务流。
```
<?php
require 'vendor/autoload.php';

use Vod\VodUploadClient;
use Vod\Model\VodUploadRequest;

$client = new VodUploadClient("your secretId", "your secretKey");
$req = new VodUploadRequest();
$req->MediaFilePath = "/data/videos/Wildlife.wmv";
$req->Procedure = "Your Procedure Name";
try {
    $rsp = $client->upload("ap-guangzhou", $req);
    echo "FileId -> ". $rsp->FileId . "\n";
    echo "MediaUrl -> ". $rsp->MediaUrl . "\n";
} catch (Exception $e) {
    // 处理上传异常
    echo $e;
}
```

### 子应用上传
传入 [子应用](/document/product/266/14574) ID，上传成功后资源只属于具体的子应用。
```
<?php
require 'vendor/autoload.php';

use Vod\VodUploadClient;
use Vod\Model\VodUploadRequest;

$client = new VodUploadClient("your secretId", "your secretKey");
$req = new VodUploadRequest();
$req->MediaFilePath = "/data/videos/Wildlife.wmv";
$req->SubAppId = 101;
try {
    $rsp = $client->upload("ap-guangzhou", $req);
    echo "FileId -> ". $rsp->FileId . "\n";
    echo "MediaUrl -> ". $rsp->MediaUrl . "\n";
} catch (Exception $e) {
    // 处理上传异常
    echo $e;
}
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
| MediaFilePath   | 媒体文件路径。        | String | 是    |
| MediaType   | 媒体文件类型，可选类型请参见 [视频上传综述](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)，若 MediaFilePath 路径带后缀可不填。        | String | 否    |
| MediaName   | 媒体名称，若不填默认采用 MediaFilePath 的文件名。      | String | 否    |
| CoverFilePath   | 封面文件路径。        | String | 否    |
| CoverType   | 媒体文件类型，可选类型请参见 [视频上传综述](/document/product/266/9760#.E5.B0.81.E9.9D.A2.E7.B1.BB.E5.9E.8B)，若 CoverFilePath 路径带后缀可不填。        | String | 否    |
| Procedure   | 任务流，具体的任务流介绍请参见 [任务流综述](https://cloud.tencent.com/document/product/266/33475#.E4.BB.BB.E5.8A.A1.E6.B5.81)。        | String | 否    |
| ExpireTime   | 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。        | String | 否    |
| ClassId   | 分类 ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/31772) 接口，创建分类，获得分类 ID。        | Integer | 否    |
| SourceContext   | 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长250个字符。        | String | 否    |
| SubAppId   | 云点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID，否则无需填写该字段。        | Integer | 否    |

上传响应类`VodUploadResponse`

| 属性名称      | 属性描述                   | 类型      |
| --------- | ---------------------- | ------- |
| FileId   | 媒体文件的唯一标识。        | String |
| MediaUrl | 媒体播放地址。 | String  |
| CoverUrl | 媒体封面地址。 | String  |
| RequestId | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 | String  |

上传方法`VodUploadClient.upload(String region, VodUploadRequest request)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| region   | 上传地域，具体参考支持的 [地域列表](/document/api/266/31756#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。        | String | 是    |
| request   | 上传请求。        | VodUploadRequest | 是    |

## 错误码表
| 状态码         | 含义               |
| ----------- | ----------------- |
| InternalError       | 内部错误。 |
| InvalidParameter.ExpireTime       | 参数值错误：过期时间。 |
| InvalidParameterValue.CoverType       | 参数值错误：封面类型。     |
| InvalidParameterValue.MediaType       | 参数值错误：媒体类型。           |
| InvalidParameterValue.SubAppId       | 参数值错误：子应用 ID。              |
| InvalidParameterValue.VodSessionKey       | 参数值错误：点播会话。              |
| ResourceNotFound       | 资源不存在。              |
