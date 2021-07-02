
本文将为您介绍如何使用 Jaeger 原始SDK上报 Go 应用数据。
## 操作步骤
### 步骤一：获取接入点和Token

在 [应用性能观测控制台](https://console.cloud.tencent.com/apm)>【应用监控】>【应用列表】，单击【添加应用】，在添加应用列 GO 语言与 Jaeger 原始 SDK 的数据采集方式。
在探针部署步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/59b54bc48f1c114fd5b39057a3b8e1cb.png)

### 步骤二：安装 Jaeger Agent

1.下载 [Jaeger Agent](https://github.com/jaegertracing/jaeger/releases/tag/v1.22.0)。
2. 执行下列命令启动 Agent 。

```
 shell nohup ./jaeger-agent --reporter.grpc.host-port={{collectorRPCHostPort}} --jaeger.tags=token={{token}}
```

### 步骤三：通过 Jaeger 原始 SDK 上报数据

1.客户端侧由于需要模拟HTTP请求，引入opentracing-contrib/go-stdlib/nethttp依赖

- 依赖路径：github.com/opentracing-contrib/go-stdlib/nethttp
- 版本要求： >= v1.0.0

2.配置 jaeger，创建Trace对象。示例如下：

```
tracer, _ := trace.NewJaegerTracer(clientServerName)
```

3.构建 span 并把 span 放入 conext 中，示例如下：

```
span := tracer.StartSpan("CallDemoServer") //构建span
ctx := opentracing.ContextWithSpan(context.Background(), span) //将span的引用放入conext中
```

4.构建带 tracer 的 Request 请求，示例如下：

```
//构建http的请求
req, err := http.NewRequest(
		http.MethodGet,
		fmt.Sprintf("http://localhost%s/ping", ginPort),
		nil,
	)
req = req.WithContext(ctx)
//构建带tracer的请求
req, ht := nethttp.TraceRequest(tracer, req)
```


5.发起HTTP请求，并获得返回结果。

```
httpClient := &http.Client{Transport: &nethttp.Transport{}} //初始化http客户端
res, err := httpClient.Do(req)
//..省略err判断
body, err := ioutil.ReadAll(res.Body)
//..省略err判断
log.Printf(" %s recevice: %s\n", clientServerName, string(body))
```

完整代码如下：

```
package gindemo

import (
	"context"
	"fmt"
	"git.code.oa.com/taw/taw-simple-demo/examples/go-jaeger-demo/trace"
	"github.com/opentracing/opentracing-go"
	"io/ioutil"
	"log"
	"net/http"
	"github.com/opentracing-contrib/go-stdlib/nethttp"
)

const (
	// 服务名 服务唯一标示，服务指标聚合过滤依据。
	clientServerName = "demo-gin-client"
	ginPort          = ":8080"
)

// StartClient gin client 也是标准的 http client.
func StartClient() {
	tracer, _ := trace.NewJaegerTracer(clientServerName)
	span := tracer.StartSpan("CallDemoServer")
	ctx := opentracing.ContextWithSpan(context.Background(), span)
	defer span.Finish()

	// 构建http请求
	req, err := http.NewRequest(
		http.MethodGet,
		fmt.Sprintf("http://localhost%s/ping", ginPort),
		nil,
	)
	if err != nil {
		trace.HandlerError(span, err)
		return
	}
	// 构建带tracer的请求
	req = req.WithContext(ctx)
	req, ht := nethttp.TraceRequest(tracer, req)
	defer ht.Finish()

	// 初始化http客户端
	httpClient := &http.Client{Transport: &nethttp.Transport{}}
	// 发起请求
	res, err := httpClient.Do(req)
	if err != nil {
		trace.HandlerError(span, err)
		return
	}
	defer res.Body.Close()
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		trace.HandlerError(span, err)
		return
	}
	log.Printf(" %s recevice: %s\n", clientServerName, string(body))
}


```
