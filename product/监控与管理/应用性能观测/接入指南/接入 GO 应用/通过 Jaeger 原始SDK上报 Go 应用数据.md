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
::: shell
nohup ./jaeger-agent --reporter.grpc.host-port={{接入点}} --agent.tags=token={{token}}
:::
</dx-codeblock>

>?对于 Jaeger Agent v1.15.0及以下版本，请将启动命令中 `--agent.tags` 替换为 `--jaeger.tags`。

### 步骤3：上报数据
通过 Jaeger 原始 SDK 上报数据：
1. 客户端侧由于需要模拟 HTTP 请求，引入 `opentracing-contrib/go-stdlib/nethttp` 依赖
 - 依赖路径：`github.com/opentracing-contrib/go-stdlib/nethttp`
 - 版本要求： ≥ `v1.0.0`
2. 配置 Jaeger，创建 Trace 对象。示例如下：
<dx-codeblock>
:::  GO
cfg := &jaegerConfig.Configuration{
  ServiceName: ginClientName, //对其发起请求的的调用链，叫什么服务
  Sampler: &jaegerConfig.SamplerConfig{ //采样策略的配置，详情见4.1.1
    Type:  "const",
    Param: 1,
  },
  Reporter: &jaegerConfig.ReporterConfig{ //配置客户端如何上报trace信息，所有字段都是可选的
    LogSpans:          true,
    LocalAgentHostPort: endPoint,
  },
  //Token配置
  Tags:        []opentracing.Tag{ //设置tag，token等信息可存于此
    opentracing.Tag{Key: "token", Value: token}, //设置token
  },
}

tracer, closer, err := cfg.NewTracer(jaegerConfig.Logger(jaeger.StdLogger)) //根据配置得到tracer
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
// Copyright © 2019-2020 Tencent Co., Ltd.

// This file is part of tencent project.
// Do not copy, cite, or distribute without the express
// permission from Cloud Monitor group.

package gindemo

import (
	"context"
	"fmt"
	"github.com/opentracing-contrib/go-stdlib/nethttp"
	"github.com/opentracing/opentracing-go"
	"github.com/opentracing/opentracing-go/ext"
	opentracingLog "github.com/opentracing/opentracing-go/log"
	"github.com/uber/jaeger-client-go"
	jaegerConfig "github.com/uber/jaeger-client-go/config"
	"io/ioutil"
	"log"
	"net/http"
)

const (
	// 服务名 服务唯一标示，服务指标聚合过滤依据。
	ginClientName = "demo-gin-client"
	ginPort       = ":8080"
	endPoint      = "xxxxx:6831" // 本地agent地址
	token         = "abc"
)

// StartClient gin client 也是标准的 http client.
func StartClient() {
	cfg := &jaegerConfig.Configuration{
		ServiceName: ginClientName, //对其发起请求的的调用链，叫什么服务
		Sampler: &jaegerConfig.SamplerConfig{ //采样策略的配置，详情见4.1.1
			Type:  "const",
			Param: 1,
		},
		Reporter: &jaegerConfig.ReporterConfig{ //配置客户端如何上报trace信息，所有字段都是可选的
			LogSpans:           true,
			LocalAgentHostPort: endPoint,
		},
		//Token配置
		Tags: []opentracing.Tag{ //设置tag，token等信息可存于此
			opentracing.Tag{Key: "token", Value: token}, //设置token
		},
	}

	tracer, closer, err := cfg.NewTracer(jaegerConfig.Logger(jaeger.StdLogger)) //根据配置得到tracer
	defer closer.Close()
	if err != nil {
		panic(fmt.Sprintf("ERROR: fail init Jaeger: %v\n", err))
	}
	//构建span，并将span放入context中
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
		HandlerError(span, err)
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
		HandlerError(span, err)
		return
	}
	defer res.Body.Close()
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		HandlerError(span, err)
		return
	}
	log.Printf(" %s recevice: %s\n", ginClientName, string(body))
}

// HandlerError handle error to span.
func HandlerError(span opentracing.Span, err error) {
	span.SetTag(string(ext.Error), true)
	span.LogKV(opentracingLog.Error(err))
}
:::
</dx-codeblock>
