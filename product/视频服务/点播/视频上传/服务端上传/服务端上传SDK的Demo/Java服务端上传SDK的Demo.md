## 简介

基于 COS 的 Java SDK 和云 API 的 SDK，VOD 提供了一个 Java 语言的 Demo，通过该 Demo，用户可以将服务端的视频和封面文件直接上传到腾讯云点播系统。

## 下载地址

* [VOD Java DEMO](https://github.com/tencentyun/vod-java-sdk-based-demo)
* [COS Java SDK](https://www.qcloud.com/document/product/436/6273)
* [云API Java SDK](https://www.qcloud.com/document/developer-resource/494/7245)

## 使用方式

1. 如果未安装Maven，先安装 [mvn](https://maven.apache.org/download.cgi)。
1. 下载 VOD JAVA DEMO 并解压到 vod-java-sdk-based-demo 目录下。
1. 修改 vod-java-sdk-based-demo/UploadDemo.java，将 SecretId 和 Secret Key 替换为自己的密钥。
1. 将 cos-java-sdk-v4-master.zip 解压到 vod-java-sdk-based-demo 目录下。
1. 将 qcloudapi-sdk-java-master.zip 解压到 vod-java-sdk-based-demo 目录下。
1. 执行 cp -R vod-java-sdk-based-demo/qcloudapi-sdk-java-master/src/com/qcloud/* vod-java-sdk-based-demo/cos-java-sdk-v4-master/src/main/java/com/qcloud 的拷贝。
1. 执行 cp vod-java-sdk-based-demo/UploadDemo.java  vod-java-sdk-based-demo/VodApi.java vod-java-sdk-based-demo/cos-java-sdk-v4-master/src/main/java/com/qcloud 的拷贝。
1. 执行 cp vod-java-sdk-based-demo/Wildlife-cover.png  vod-java-sdk-based-demo/Wildlife.wmv  vod-java-sdk-based-demo/pom.xml vod-java-sdk-based-demo/cos-java-sdk-v4-master 的拷贝和覆盖。
1. 执行 cd vod-java-sdk-based-demo/cos-java-sdk-v4-master。
1. 执行 mvn clean compile assembly:single 完成编译。
1. 执行 java -cp target/cos_api-4.4-jar-with-dependencies.jar com.qcloud.UploadDemo 发起上传，上传成功后将获取文件的播放地址和 fileid。
