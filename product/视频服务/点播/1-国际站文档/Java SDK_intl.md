## Overview

VOD provides a Java-based SDK which is based on COS Java SDK and Cloud API SDK. Users can refer to this SDK to upload videos and cover image files stored in their servers directly to Tencent Cloud VOD system.

## SDK Download and Install

JAVA SDK can be obtained in the following ways, developers can combine their own situation, select the SDK source, add maven dependencies.

1. download source
* [visit Github >>](https://github.com/tencentyun/vod-java-sdk)
* [click to download Java SDK >>](https://github.com/tencentyun/vod-java-sdk/archive/master.zip)

2. maven
```
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>vod_api</artifactId>
    <version>1.0.0</version>
</dependency>
```

## Example
**Upload API**
```
public static void main(String[] args) {
        try {
            VodApi vodApi = new VodApi("your secretId", "your secretKey");
            //set sign expire time
            //VodApi vodApi = new VodApi("your secretId", "your secretKey", 24 * 3600);
            vodApi.upload("videos/Wildlife.wmv", "videos/Wildlife-cover.png");
        } catch(Exception e) {
            //log
            log.error("upload video fail", e)
        }
}
```