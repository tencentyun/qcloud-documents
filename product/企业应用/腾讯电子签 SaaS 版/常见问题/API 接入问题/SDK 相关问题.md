### 如何获取 SDK 调用样例？  
电子签集成版目前提供了 [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php/tree/master/examples/ess) 、[Python](https://github.com/TencentCloud/tencentcloud-sdk-python/tree/master/examples/ess) 、[Java](https://github.com/TencentCloud/tencentcloud-sdk-java/tree/master/examples/ess) 、[Go](https://github.com/TencentCloud/tencentcloud-sdk-go/tree/master/examples/ess)  等语言的调用 Demo 供您在接入时参考，已上传至 GitHub 腾讯云官方 SDK 项目。

### 如何导入 SDK ？  
目前官方提供了 PHP、Python、Java、Go、.NET、Node.js、C++、Ruby 等语言的 SDK 支持，请根据您的实际需要进行导入，请参见  [SDK 导入指引](https://cloud.tencent.com/document/sdk) 。

### JDK1.7 使用 SDK 调用上传文件接口报 javax.net.ssl.SSLException-Received fatal alert: protocol_version？
JDK1.7 默认使用 TLSv1.0，需要强制设置成 TLSv1.2，官方使用的 HTTP 客户端是 okhttp，需要自行修改官网 SDK 源码。
在 com.tencentcloudapi.common.http.HttpConnection 类中修改构造函数如下：
```
 public HttpConnection(Integer connTimeout, Integer readTimeout, Integer writeTimeout) {
    this.client = new OkHttpClient();
    SSLContext sslContext = null; //这边指定tls版本
    try {
        sslContext = SSLContext.getInstance("TLSv1.2");
        sslContext.init(null, null,null);
    } catch (Exception e) {
        e.printStackTrace();
        throw new RuntimeException(e.getMessage());
    }
    SSLSocketFactory factory = sslContext.getSocketFactory();
    this.client.setSslSocketFactory(factory);
    this.client.setConnectTimeout(connTimeout, TimeUnit.SECONDS);
    this.client.setReadTimeout(readTimeout, TimeUnit.SECONDS);
    this.client.setWriteTimeout(writeTimeout, TimeUnit.SECONDS);
  }
```
