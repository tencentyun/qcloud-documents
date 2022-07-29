## 操作场景

TSF SDK 对一些常用的消息队列组件、数据库组件等有埋点操作以支持全链路跟踪，但在客户实际场景下可能存在 直接使用 ApacheHttpClient 的场景。

本文将介绍如何使用ApacheHttpClient 注入调用链。




>?当前仅以下 SDK 版本及其之后的 SDK 版本支持：1.29.5-Hoxton、1.29.12-Finchley、1.29.2-Greenwich。


## 前提条件

在开始本文的实践前，您需要先了解 TSF 的以下功能。

- [调用链快速入门](https://cloud.tencent.com/document/product/649/16622)
- [服务依赖拓扑](https://cloud.tencent.com/document/product/649/15544)
- [调用链查询](https://cloud.tencent.com/document/product/649/13688)



## 操作步骤

#### 有两种使用方式

直接使用 @Autowired 注入的 HttpClientBuilder 创建 client。
```java
@Autowired 
private HttpClientBuilder httpClientBuilder;

public void call(String str) {

    CloseableHttpClient client = httpClientBuilder.build();
    HttpGet get = new HttpGet("http://localhost:18081/echo/" + str);
    HttpResponse response = client.execute(get);
}

```

创建 HttpClientBuilder 的时候传入 httpTracing。

```java

@Autowired
private HttpTracing httpTracing;

public void call(String str) {
    
    HttpClientBuilder httpClientBuilder = TracingHttpClientBuilder.create(httpTracing);

    CloseableHttpClient client = httpClientBuilder.build();
    HttpGet get = new HttpGet("http://localhost:18081/echo/" + str);
    HttpResponse response = client.execute(get);
}
```


## 说明与注意

- 注入失败不会影响业务的正常运行
