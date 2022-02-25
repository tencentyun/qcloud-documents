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
nohup ./jaeger-agent --reporter.grpc.host-port={{collectorRPCHostPort}} --agent.tags=token={{token}}
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
cfg := &jaegerConfig.Configuration{
  ServiceName: grpcServerName, //对其发起请求的的调用链，叫什么服务
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
3. 配置中间件
<dx-codeblock>
:::  go
r := gin.Default()
//传入tracer
r.Use(ginhttp.Middleware(tracer))
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
官方默认 OperationName 是 HTTP + HttpMethod，建议使用 `HTTP + HttpMethod + URL` 可以分析到具体接口，接口主要 URL 应是参数名，不是具体参数值。 具体用法如下：
正确：`/user/{id}`， 错误：`/user/1`
</dx-alert>
<dx-codeblock>
:::  go
r.Use(ginhttp.Middleware(tracer, ginhttp.OperationNameFunc(func(r *http.Request) string {
		return fmt.Sprintf("testtestheling  HTTP %s %s", r.Method, r.URL.String())
	})))
:::
</dx-codeblock>
完整代码如下：
<dx-codeblock>
:::  go
// Copyright © 2019-2020 Tencent Co., Ltd.

// This file is part of tencent project.
// Do not copy, cite, or distribute without the express
// permission from Cloud Monitor group.

package grpcdemo

import (
	"context"
	"fmt"
	"github.com/opentracing/opentracing-go"
	"github.com/uber/jaeger-client-go"
	jaegerConfig "github.com/uber/jaeger-client-go/config"
	"log"
	"net"

	"github.com/opentracing-contrib/go-grpc"
	"google.golang.org/grpc"
)

const (
	// 服务名 服务唯一标示，服务指标聚合过滤依据。
	grpcServerName = "demo-grpc-server"
	serverPort     = ":9090"
)

// server is used to implement proto.HelloTraceServer.
type server struct {
	UnimplementedHelloTraceServer
}

// SayHello implements proto.HelloTraceServer
func (s *server) SayHello(ctx context.Context, in *TraceRequest) (*TraceResponse, error) {
	log.Printf("Received: %v", in.GetName())
	return &TraceResponse{Message: "Hello " + in.GetName()}, nil
}

// StartServer
func StartServer() {
	cfg := &jaegerConfig.Configuration{
		ServiceName: grpcServerName, //对其发起请求的的调用链，叫什么服务
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
	lis, err := net.Listen("tcp", serverPort)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer(grpc.UnaryInterceptor(otgrpc.OpenTracingServerInterceptor(tracer)))

	// 在gRPC服务器处注册我们的服务
	RegisterHelloTraceServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
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
cfg := &jaegerConfig.Configuration{
  ServiceName: grpcClientName, //对其发起请求的的调用链，叫什么服务
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
// Copyright © 2019-2020 Tencent Co., Ltd.

// This file is part of tencent project.
// Do not copy, cite, or distribute without the express
// permission from Cloud Monitor group.

package grpcdemo

import (
	"context"
	"fmt"
	"github.com/opentracing-contrib/go-grpc"
	"github.com/opentracing/opentracing-go"
	"github.com/uber/jaeger-client-go"
	jaegerConfig "github.com/uber/jaeger-client-go/config"
	"google.golang.org/grpc"
	"log"
	"time"
)

const (
	// 服务名 服务唯一标示，服务指标聚合过滤依据。
	grpcClientName = "demo-grpc-client"
	defaultName    = "TAW Tracing"
	serverAddress  = "localhost:9090"
	endPoint       = "xxxxx:6831" // 本地agent地址
	token          = "abc"
)

// StartClient
func StartClient() {
	cfg := &jaegerConfig.Configuration{
		ServiceName: grpcClientName, //对其发起请求的的调用链，叫什么服务
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
	// 向服务端建立链接，配置拦截器
	conn, err := grpc.Dial(serverAddress, grpc.WithInsecure(), grpc.WithBlock(),
		grpc.WithUnaryInterceptor(otgrpc.OpenTracingClientInterceptor(tracer)))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	//
	c := NewHelloTraceClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	// 发起RPC调用
	r, err := c.SayHello(ctx, &TraceRequest{Name: defaultName})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("RPC Client receive: %s", r.GetMessage())
}
:::
</dx-codeblock>
