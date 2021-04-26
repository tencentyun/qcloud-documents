## 简介

基于 COS 的 Java SDK 和云 API 的 SDK，VOD 提供了一个 Java 语言的 SDK，通过该 SDK，用户可以将服务端的视频和封面文件直接上传到腾讯云点播系统。

## SDK获取与安装

可以通过以下方式获取JAVA SDK，开发者可以结合自身的情况，选择SDK源码、添加maven依赖项。

1. 获取源码
[从 Github 访问 >>](https://github.com/tencentyun/vod-java-sdk)
[单击下载 Java SDK >>](https://github.com/tencentyun/vod-java-sdk/archive/master.zip)

2. maven
```
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>vod_api</artifactId>
    <version>1.0.0</version>
</dependency>
```

## 示例
**upload 接口**
```
public static void main(String[] args) {
        try {
            VodApi vodApi = new VodApi("your secretId", "your secretKey");
            //设置签名过期时长
            //VodApi vodApi = new VodApi("your secretId", "your secretKey", 24 * 3600);
            vodApi.upload("videos/Wildlife.wmv", "videos/Wildlife-cover.png");
        } catch(Exception e) {
            //打日志
            log.error("上传视频失败", e)
        }
}
```
