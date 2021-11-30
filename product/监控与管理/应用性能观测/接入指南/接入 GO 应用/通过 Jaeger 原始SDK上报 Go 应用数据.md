本文将为您介绍如何使用 Jaeger 原始 SDK 上报 Go 应用数据。

## 操作步骤
### 步骤1：获取接入点和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 GO 语言与 Jaeger 原始 SDK 的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：安装 Jaeger Agent

1. 下载 [Jaeger Agent](https://github.com/jaegertracing/jaeger/releases/tag/v1.22.0)。
2. 执行下列命令启动 Agent 。
<dx-codeblock>
:::  shell
nohup ./jaeger-agent --reporter.grpc.host-port={{接入点}} --agent.tags=token={{token}}
:::
</dx-codeblock>

>?对于 Jaeger Agent v1.15.0及以下版本，请将启动命令中 `--agent.tags` 替换为 `--jaeger.tags`。

### 步骤3：上报数据
通过 Jaeger 原始 SDK 上报数据：
1. 客户端侧由于需要模拟 HTTP 请求，引入 `opentracing-contrib/go-stdlib/nethttp` 依赖
 - 依赖路径：`github.com/opentracing-contrib/go-stdlib/nethttp`
 - 版本要求： ≥ `dv1.0.0`
2. 配置 Jaeger，创建 Trace 对象。示例如下：
<dx-codeblock>
:::  GO
tracer, _ := trace.NewJaegerTracer(clientServerName)
:::
</dx-codeblock>
3. 构建 span 并把 span 放入 conext 中，示例如下：
<dx-codeblock>
:::  GO
span := tracer.StartSpan("CallDemoServer") //构建span
ctx := opentracing.ContextWithSpan(context.Background(), span) //将span的引用放入conext中
:::
</dx-codeblock>
4. 构建带 tracer 的 Request 请求，示例如下：
<dx-codeblock>
:::  GO
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
:::  GO
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
:::  GO
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
