### PHP SDK 运行时抛出 `Call to undefined method GuzzleHttp\Utils::chooseHandler()` 异常，该如何处理？


PHP SDK 依赖 Guzzle，推荐用户使用 Composer 方式安装 SDK。
- 在使用 Composer 方式安装时，需要执行 `php composer.phar install` 命令安装 SDK 和依赖。
- 在使用源码方式安装时，需要执行 `composer install` 命令安装 SDK 和依赖，详情请参阅 [PHP SDK - 下载与安装](https://cloud.tencent.com/document/product/436/12266#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85)。


### COS 接入 PHP SDK 上传文件报错：`cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html`，该如何处理？

如果您的 PHP 环境证书有问题，可能会遇到报错，类似于 `cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html`，请尝试按以下步骤解决：

1. 访问地址 `https://curl.haxx.se/ca/cacert.pem` 下载证书文件 cacert.pem，将其保存到 PHP 安装路径下。
2. 编辑 php.ini 文件，删除 curl.cainfo 配置项前的分号注释符（;），值设置为保存的证书文件 cacert.pem 的绝对路径。
3. 重启依赖 PHP 的服务。

