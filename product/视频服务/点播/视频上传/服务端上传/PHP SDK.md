## 简介

用于服务端上传的PHP SDK，可向腾讯云点播系统上传视频和封面文件。

## 集成方式

### 使用composer引入
```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v1.2.1"
    }
}
```

### 源文件导入
如果项目当中没有使用composer工具进行依赖管理的，可以直接下载源码导入项目中使用：

* [从 Github 访问 >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [点击下载 PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

复制src文件下的源码和test/non-composer文件的cos-sdk-v5、qcloudapi-sdk-php到项目同级目录即可

## 上传步骤
###  第一步：初始化配置
使用云API密钥初始化配置

**对于使用composer导入的**

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

### 第二步：调用upload方法进行上传

方法签名
```
public static function upload(array $src, $parameter = null)
```

方法参数
**src参数**

| 参数名称         | 参数描述    | 类型 | 是否必填 |
| ------------ | ------------ |  ------------ | ------------  |
| videoPath | 视频路径 |  String |  是 |
| coverPath | 封面路径 |  String | 否 |

**parameter参数**

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| videoName | 视频名称 |  String | 
| sourceContext | 用户自定义上下文 |  String | 
| storageRegion | 指定存储地区 |  String | 
| procedure | 任务流 |  String | 

方法返回值

|  名称         | 描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| code | 状态码，0为成功，非0为失败 |  Integer | 
| message | 提示信息 |  String | 
| data | 返回数据 |  Object |
| data.fileId | 视频文件ID |  String |
| data.video.url | 视频Url |  String |
| data.cover.url | 封面Url |  String |

#### 上传视频
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

#### 上传视频附带封面
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

#### 上传视频指定任务流
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

#### 上传视频到指定地域
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
## 错误码列表

| 错误码         | 说明                |
| ----------- | ----------------- |
| 31001       | 用户请求session_key错误 |
| 31002       | 用户请求中的VOD签名重复     |
| 31003       | 上传文件不存在           |
| 32001       | 服务错误              |