## 操作场景
TSW 本身不提供 Go 语言客户端采集，但可兼容通过 Skywalking 的 Go2Sky 接入应用，向TSW后端上报数据。TSW 目前已支持将 Skywalking 上报的数据转换成自身兼容的 Opentracing 格式，在服务调用监控、调用链、依赖拓扑等功能上，功能可与使用 TSW 自有 Agent 保持一致。

## 操作流程
[](id:step1)
#### 1. 获取接入点和 Token
在 [TSW 控制台](https://console.cloud.tencent.com/tsw)的【服务监控】>【服务列表】中，单击【接入服务】，选择 Go 语言与 Skywalking 的数据采集方式。您可在下方的获取接入点和 Token 中找到私网接入点与您的个人 Token。

#### 2. 接入埋点
参考 [Go2Sky 文档](https://github.com/SkyAPM/go2sky)，自行对 Go 的跨服务调用埋点。
Go 语言应用在使用 Skywalking 上报数据时有一定改造成本，您需要改造少量业务代码以完成接入埋点。

#### 3. 修改上报配置
将 reporter 的 serverAddr 修改为 TSW 的接入点，将 reporter 的 auth 修改为 Token。

#### 4. 重启服务，开始上报数据

## 接入验证
向应用发送请求，在收到响应后，在 TSW 控制台查看调用数据。
您可以在1分钟内通过【链路追踪】>【调用链查询】>【[Span查询](https://console.cloud.tencent.com/tsw/trace?rid=1&tab=span)】查找调用详情。监控曲线与统计数据将在1分钟后开始正常显示。

## Go2Sky 改造示例
以下是基于 Go2Sky 的 Demo 改造示例，您可根据实际情况进行修改。
1. 在 NewGRPCReporter 的时设置上报地址和 Authentication（上报地址与 Token 的获取方式参考 [步骤1](#step1)）。
```
report, err = reporter.NewGRPCReporter(
"ap-guangzhou.tencentservicewatcher.com:11800",
reporter.WithAuthentication("tsw_site@xxxxxxxxxx"))
```
>!请根据控制台给出的私网接入点和 Token 进行改造。
2. 进行 Server 端配置，Demo 如下：
<dx-codeblock>
::: go
package main

import (
"flag"
   "github.com/SkyAPM/go2sky/reporter"
   "io/ioutil"
   "log"
   "net/http"
   "time"

   "github.com/SkyAPM/go2sky"
   httpPlugin "github.com/SkyAPM/go2sky/plugins/http"
)

var (
   grpc        bool
   oapServer   string
   upstreamURL string
   listenAddr  string
   serviceName string

   client *http.Client
)

func init() {
flag.BoolVar(&grpc, "grpc", false, "use grpc reporter")
flag.StringVar(&oapServer, "oap-server", "ap-guangzhou.tencentservicewatcher.com:11800", "oap server address")  
//ap-guangzhou.tencentservicewatcher.com:11800 需替换为 TSW 的私网接入点
flag.StringVar(&upstreamURL, "upstream-url", "upstream-service", "upstream service url")
flag.StringVar(&listenAddr, "listen-addr", ":8081", "listen address")
flag.StringVar(&serviceName, "service-name", "go2sky-server", "service name")
}

func ServerHTTP(writer http.ResponseWriter, request *http.Request) {
time.Sleep(time.Duration(500) * time.Millisecond)

   clientReq, err := http.NewRequest(http.MethodPost, upstreamURL, nil)
if err != nil {
      writer.WriteHeader(http.StatusInternalServerError)
log.Printf("unable to create http request error: %v \n", err)
return
   }
   clientReq = clientReq.WithContext(request.Context())
   res, err := client.Do(clientReq)
if err != nil {
      writer.WriteHeader(http.StatusInternalServerError)
log.Printf("unable to do http request error: %v \n", err)
return
   }
defer res.Body.Close()
   body, err := ioutil.ReadAll(res.Body)
if err != nil {
      writer.WriteHeader(http.StatusInternalServerError)
log.Printf("read http response error: %v \n", err)
return
   }
   writer.WriteHeader(res.StatusCode)
   _, _ = writer.Write(body)
}

func main() {
flag.Parse()

var report go2sky.Reporter
   var err error

   report, err = reporter.NewGRPCReporter(
						oapServer,
						reporter.WithAuthentication("tsw_site@xxxxxxxxxxxxxxxxxxxxxxxx")) 
						//tsw_site@xxxxxxxxxxxxxxxxxxxxxxxx 需替换成您的 Token
//report, err = reporter.NewLogReporter()

   if err != nil {
log.Fatalf("crate grpc reporter error: %v \n", err)
   }

   tracer, err := go2sky.NewTracer(serviceName, go2sky.WithReporter(report))
if err != nil {
log.Fatalf("crate tracer error: %v \n", err)
   }

   client, err = httpPlugin.NewClient(tracer)
if err != nil {
log.Fatalf("create client error %v \n", err)
   }

   route := http.NewServeMux()
   route.HandleFunc("/mack", ServerHTTP)

   sm, err := httpPlugin.NewServerMiddleware(tracer)
if err != nil {
log.Fatalf("create client error %v \n", err)
   }
   err = http.ListenAndServe(listenAddr, sm(route))
if err != nil {
log.Fatal(err)
   }
}
:::
</dx-codeblock>



