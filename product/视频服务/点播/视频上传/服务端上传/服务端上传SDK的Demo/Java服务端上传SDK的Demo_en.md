## Overview

VOD provides a Java-based Demo which is based on COS Java SDK and Cloud API SDK. Users can refer to this demo to upload videos and cover image files stored in their servers directly to Tencent Cloud VOD system.

## Download Links

* [VOD Java DEMO](https://github.com/tencentyun/vod-java-sdk-based-demo)
* [COS Java SDK](https://www.qcloud.com/document/product/436/6273)
* [Cloud API Java SDK](https://www.qcloud.com/document/developer-resource/494/7245)

## How to Use

1. If you haven't installed Maven, install [mvn](https://maven.apache.org/download.cgi).
2. Download VOD JAVA DEMO and decompress the files to vod-java-sdk-based-demo directory.
3. Modify vod-java-sdk-based-demo/UploadDemo.java, change the SecretId and Secret Key into your own secret keys.
4. Decompress cos-java-sdk-v4-master.zip and place the files to vod-java-sdk-based-demo directory.
5. Decompress qcloudapi-sdk-java-master.zip and place the files to vod-java-sdk-based-demo directory.
6. Execute copy command: cp -R vod-java-sdk-based-demo/qcloudapi-sdk-java-master/src/com/qcloud/* vod-java-sdk-based-demo/cos-java-sdk-v4-master/src/main/java/com/qcloud.
7. Execute copy command: cp vod-java-sdk-based-demo/UploadDemo.java  vod-java-sdk-based-demo/VodApi.java vod-java-sdk-based-demo/cos-java-sdk-v4-master/src/main/java/com/qcloud.
8. Execute copy and overwrite command: cp vod-java-sdk-based-demo/Wildlife-cover.png  vod-java-sdk-based-demo/Wildlife.wmv  vod-java-sdk-based-demo/pom.xml vod-java-sdk-based-demo/cos-java-sdk-v4-master.
9. Execute cd vod-java-sdk-based-demo/cos-java-sdk-v4-master.
10. Execute mvn clean compile assembly:single to complete the compiling process.
11. Execute java -cp target/cos_api-4.4-jar-with-dependencies.jar com.qcloud.UploadDemo to initiate the upload process. You'll acquire file playback address and fileid once the upload process is successfully completed.

