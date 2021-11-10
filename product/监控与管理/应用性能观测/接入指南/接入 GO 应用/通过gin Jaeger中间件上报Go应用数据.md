本文将为您介绍如何使用 gin Jaeger 中间件上报 Go 应用数据。

## 操作步骤

### 步骤1：获取接入点和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**，单击**接入应用**页面，在接入应用时选择 GO 语言与 gin Jaeger 中间组件的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：安装 Jaeger Agent

1. 下载 [Jaeger Agent](https://github.com/jaegertracing/jaeger/releases/tag/v1.22.0)。
2. 执行下列命令启动 Agent 。
<dx-codeblock>
:::  shell
 shell nohup ./jaeger-agent --reporter.grpc.host-port={{collectorRPCHostPort}} --agent.tags=token={{token}}
:::
</dx-codeblock>

### 步骤3：选择上报端类型上报应用数据
选择上报端类型，通过 gin Jaeger 中间件上报 Go 应用数据：
#### 服务端
1. 在服务端侧引入 `opentracing-contrib/go-gin` 依赖
 - 依赖路径： `github.com/opentracing-contrib/go-gin`
 - 版本要求： ≥ `v0.0.0-20201220185307-1dd2273433a4`

2. 配置  Jaeger，创建 Trace 对象。示例如下：
<dx-codeblock>
:::  go
tracer, closer := trace.NewJaegerTracer("demo-service")
	cfg := &jaegerConfig.Configuration{
		ServiceName: clientServiceName,    //对其发起请求的的调用链，服务名称
		Sampler: &jaegerConfig.SamplerConfig{  
			Type:  "const",
			Param: 1,
		},
		Reporter: &jaegerConfig.ReporterConfig{ //配置客户端如何上报trace信息，所有字段都是可选的
			LogSpans:           true,
			CollectorEndpoint: httpEndPoint,
		},
		Tags:        tags,   //设置tag，token等信息可存于此
	}

tracer, closer, err := cfg.NewTracer(jaegerConfig.Logger(jaeger.StdLogger)) //根据配置得到tracer
:::
</dx-codeblock>
3. 配置中间件
<dx-codeblock>
:::  go
r := gin.Default()
//传入tracer
r.Use(ginhttp.Middleware(tracer))
r.Use(ginhttp.Middleware(tracer, ginhttp.OperationNameFunc(func(r *http.Request) string {
		return fmt.Sprintf("testtestheling  HTTP %s %s", r.Method, r.URL.String())
	})))
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
官方默认 OperationName 是 HTTP + HttpMethod，建议使用 `HTTP + HttpMethod + URL` 可以分析到具体接口，接口主要 URL 应是参数名，不是具体参数值。 具体用法如下：
正确：`/user/{id}`， 错误：`/user/1`
</dx-alert>
完整代码如下：
<dx-codeblock>
:::  go
package gindemo

import (
	"fmt"
	"git.code.oa.com/taw/taw-simple-demo/examples/go-jaeger-demo/trace"
	"github.com/gin-gonic/gin"
	"github.com/opentracing-contrib/go-gin/ginhttp"
	"net/http"
)

// 服务名服务唯一标示，服务指标聚合过滤依据。
const ginServerName = "demo-gin-server"

func StartServer() {
	tracer, closer := trace.NewJaegerTracer(ginServerName)
	defer closer.Close()
	r := gin.Default()
	r.Use(ginhttp.Middleware(tracer, ginhttp.OperationNameFunc(func(r *http.Request) string {
		return fmt.Sprintf("HTTP %s %s", r.Method, r.URL.String())
	})))
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run() // 监听 0.0.0.0:8080
}
:::
</dx-codeblock>

#### 客户端

1. 客户端侧由于需要模拟 HTTP 请求，引入 `opentracing-contrib/go-stdlib/nethttp` 依赖
 - 依赖路径：`github.com/opentracing-contrib/go-stdlib/nethttp`
 - 版本要求： ≥ `v1.0.0`
2. 配置 Jaeger，创建 Trace 对象。示例如下：
<dx-codeblock>
:::  go
tracer, _ := trace.NewJaegerTracer(clientServerName)
:::
</dx-codeblock>
3. 构建 span 并把 span 放入 conext 中，示例如下：
<dx-codeblock>
:::  go
span := tracer.StartSpan("CallDemoServer") //构建span
ctx := opentracing.ContextWithSpan(context.Background(), span) //将span的引用放入conext中
:::
</dx-codeblock>
4. 构建带 tracer 的 Request 请求，示例如下：
<dx-codeblock>
:::  go
//构建http的请求
req, err := http.NewRequest(
		http.MethodGet,
		fmt.Sprintf("http://localhost%s/ping", ginPort),
		nil,
	)
req = req.WithContext(ctx)
//构建带tracer的请求
req, ht := nethttp.TraceRequest(tracer, req)
:::
</dx-codeblock>
5. 发起 HTTP 请求，并获得返回结果。
<dx-codeblock>
:::  go
httpClient := &http.Client{Transport: &nethttp.Transport{}} //初始化http客户端
res, err := httpClient.Do(req)
//..省略err判断
body, err := ioutil.ReadAll(res.Body)
//..省略err判断
log.Printf(" %s recevice: %s\n", clientServerName, string(body))
:::
</dx-codeblock>
完整代码如下：
<dx-codeblock>
:::  go
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
:::
</dx-codeblock>
