## 简介

基于 COS 的 PHP SDK 和云 API 的 SDK，VOD 提供了一个 PHP语言的 SDK，通过该 SDK，用户可以将服务端的视频和封面文件直接上传到腾讯云点播系统。

## 下载地址

* [从 Github 访问 >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [单击下载 PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

## 使用方式

1. 下载本 SDK 后，编辑 conf.php，将SECRET_ID 设置为 API 密钥中的 secret id，将 SECRET_KEY 设置为 API 密钥中的 secret key。
2. 执行 php upload_demo.php，即可发起文件上传，上传成功后将获取文件的播放地址和 fileid。