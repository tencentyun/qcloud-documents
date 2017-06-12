## 简介

基于 COS 的 PHP SDK 和云 API 的 SDK，VOD 提供了一个 PHP语言的 Demo，通过该 Demo，用户可以将服务端的视频和封面文件直接上传到腾讯云点播系统。

## 下载地址

* [VOD 服务端上传 PHP DEMO](https://github.com/tencentyun/vod-php-sdk-based-demo)
* [COS PHP SDK](https://www.qcloud.com/document/product/436/6274)
* [云API PHP SDK](https://www.qcloud.com/document/developer-resource/494/7243)

## 使用方式

1. 下载 VOD 服务端上传 PHP DEMO 并解压，将工作目录切换到 upload_demo.php 所在的目录下。
1. 将 cos-php-sdk-v4-master.zip 解压到工作目录。
1. 将 qcloudapi-sdk-php-master.zip 解压到工作目录。
1. 编辑 cos-php-sdk-v4-master/qcloudcos/conf.php，将 APP_ID 设置为  SECRET_ID 设置为 API 密钥中的 secret id，将 SECRET_KEY 设置为 API 密钥中的 secret key。
1. 执行 php upload_demo.php，即可发起文件上传，上传成功后将获取文件的播放地址和 fileid。