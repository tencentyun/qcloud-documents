## 支持环境
- PHP 5.6.33 版本及以上。
- 调用地址：`ims.tencentcloudapi.com`。
>!API 支持就近地域接入，本产品就近地域接入的域名为 ims.tencentcloudapi.com ，也支持指定地域域名访问，例如：广州地域的域名为 ims.ap-guangzhou.tencentcloudapi.com 。详细请参考 [图片内容安全-请求结构](https://cloud.tencent.com/document/product/1125/53276)。
>

## 安装 PHP SDK 3.0
通过 Composer 获取安装是使用 PHP SDK 推荐方法，Composer 是 PHP 的依赖管理工具。关于 Composer 详细可参见 [Composer 官网](https://getcomposer.org/download/)。 
>?Composer 需要 PHP 5.3.2+ 以上版本，且需要开启 openssl。
>
### 步骤1：安装 Composer
- Windows 环境请访问 [Composer 官网](https://getcomposer.org/download/)下载安装包安装。
- Unix 环境在命令行中执行以下命令安装：
```
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
```

### 步骤2：添加镜像源
中国大陆地区的用户可以使用腾讯云镜像源提高下载速度，在打开的命令窗口执行以下命令：
```
composer config -g repos.packagist composer
https://mirrors.tencent.com/composer/
```

### 步骤3：添加依赖
在打开的命令窗口执行命令安装 SDK（安装到指定位置），例如安装到 `C:\Users\···>`目录下，则在指定的位置打开命令窗口，并执行以下命令：
```
composer require tencentcloud/tencentcloud-sdk-php
```
### 步骤4：添加引用
在代码中添加以下引用代码。
>!如下仅为示例，Composer 会在项目根目录下生成 vendor 目录，/path/to/ 为项目根目录的实际绝对路径（如果是在当前目录执行，可以省略绝对路径）。
>
```
require '/path/to/vendor/autoload.php';
```

## 使用 SDK
以下为 ImageModeration 接口的 demo 示例，其中 region 配置为广州，实际请按需配置。
```
< ? php require_once 'vendor/autoload.php';
use TencentCloud\ Common\ Credential;
use TencentCloud\ Common\ Profile\ ClientProfile;
use TencentCloud\ Common\ Profile\ HttpProfile;
use TencentCloud\ Common\ Exception\ TencentCloudSDKException;
use TencentCloud\ Ims\ V20201229\ ImsClient;
use TencentCloud\ Ims\ V20201229\ Models\ ImageModerationRequest;
try {
	$cred = new Credential("SecretId", "SecretKey");
	$httpProfile = new HttpProfile();
	$httpProfile - > setEndpoint("ims.tencentcloudapi.com");
	$clientProfile = new ClientProfile();
	$clientProfile - > setHttpProfile($httpProfile);
	$client = new ImsClient($cred, "ap-guangzhou", $clientProfile);
	$req = new ImageModerationRequest();
	$params = array();
	$req - > fromJsonString(json_encode($params));
	$resp = $client - > ImageModeration($req);
	print_r($resp - > toJsonString());
} catch (TencentCloudSDKException $e) {
	echo $e;
}
```
