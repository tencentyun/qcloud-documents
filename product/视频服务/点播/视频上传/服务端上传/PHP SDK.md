对于在服务端上传视频的场景，腾讯云点播提供了 PHP SDK 来实现。上传的流程可以参见 [服务端上传指引](/document/product/266/9759)。

## 集成方式

### 使用 composer 引入
```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v1.2.1"
    }
}
```

### 源文件导入
如果项目当中没有使用 composer 工具进行依赖管理的，可以直接下载源码导入项目中使用：

* [从 Github 访问 >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [点击下载 PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

复制 src 文件下的源码和 test/non-composer 文件的 cos-sdk-v5、qcloudapi-sdk-php 到项目同级目录即可

##  简单视频上传
### 初始化上传对象
使用云API密钥初始化VodApi
**对于使用 composer 导入的**
```
<?php
require 'vendor/autoload.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");
```

**对于使用源码导入的**
```php
<?php
require './cos-sdk-v5/cos-autoloader.php';
require './qcloudapi-sdk-php/src/QcloudApi/QcloudApi.php';
require './src/Vod/VodApi.php';
require './src/Vod/Conf.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");
```

### 调用上传
传入视频地址进行上传
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

## 高级功能
### 携带封面
同时传入视频地址和封面地址
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

### 指定任务流
传入任务流参数，具体的任务流介绍参考[任务流综述](/document/product/266/11700)，视频上传成功后会自动执行任务流
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    ),
    array (
        'procedure' => 'QCVB_SimpleProcessFile(1, 1)'
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

###  指定上传区域
传入指定的地域标识，即可将视频上传指定的区域，详见[服务端上传指引](/document/product/266/9759)。
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    ),
    array (
        'storageRegion' => 'tj'
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

## 接口描述
初始化上传对象 `VodApi::initConf(secretId, secretKey)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| secretId   | 云API密钥ID        | String | 是    |
| secretKey | 云API密钥Key | String  | 是    |

上传方法 `VodApi.upload(src, parameter)`

**src 参数**

| 参数名称         | 参数描述    | 类型 | 必填 |
| ------------ | ------------ |  ------------ | ------------  |
| videoPath | 视频路径 |  String |  是 |
| coverPath | 封面路径 |  String | 否 |

**parameter 参数**

| 参数名称         | 参数描述    | 类型 | 必填 |
| ------------ | ------------ |  ------------ |   ------------  |
| videoName | 视频名称 |  String | 否 |
| sourceContext | 用户自定义上下文 |  String | 否 |
| storageRegion | 指定存储地区 |  String | 否 |
| procedure | 任务流 |  String | 否 |

上传结果 

| 成员变量名称   | 变量说明      | 类型     |
| -------- | --------- | ------ |
| code |结果码 |  int | 
| message | 提示信息 |  String | 
| data | 返回数据 |  Object |
| data.fileId | 点播视频文件Id |  String |
| data.video.url | 视频存储地址 |  String |
| data.cover.url | 封面存储地址 |  String |

## 错误码列表
调用SDK上传后， 可以根据结果中的 code 来确认视频上传的情况

| 状态码         | 含义               |
| ----------- | ----------------- |
| 0       | 上传成功 |
| 31001       | 用户请求session_key错误 |
| 31002       | 用户请求中的VOD签名重复     |
| 31003       | 上传文件不存在           |
| 32001       | 服务错误              |
