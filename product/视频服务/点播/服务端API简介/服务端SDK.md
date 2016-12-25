服务端API的调用较为复杂。对于一般的API，需要对调用参数进行排序、计算鉴权签名；对于视频上传的三个服务端API，更是要处理复杂的分片上传逻辑。为了方便开发者，点播提供了服务端API来简化开发。

所有API均包含一般服务端API调用、服务端视频上传两大类功能。

- [vod-php-server-sdk-v4](https://github.com/tencentyun/vod-php-server-sdk-v4)
- vod-nodejs-server-sdk-v4(即将推出)
- vod-python-server-sdk-v4(即将推出)
- vod-java-server-sdk-v4(即将推出)
- vod-golang-server-sdk-v4(即将推出)
- vod-csharp-server-sdk-v4(即将推出)