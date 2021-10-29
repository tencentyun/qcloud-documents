Go2sky 是 Golang 提供给开发者实现 SkyWalking agent 探针的包，可以通过它来实现向 SkyWalking Collector上报数据。本文将为您介绍如何使用 Skywalking 协议上报 Go 应用数据。


## 操作流程

### 步骤1：获取接入点和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 Go 语言与 Skywalking 的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token。
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：上报应用数据
通过 Skywalking 协议上报 Go 应用数据：
1. 接入埋点。
参见 [Go2Sky 文档](https://github.com/SkyAPM/go2sky)，自行对 Go 的跨服务调用埋点。 Go 语言应用在使用 Skywalking 上报数据时有一定改造成本，您需要改造少量业务代码以完成接入埋点。
2. 修改上报配置。
将 reporter 的 serverAddr 修改为 APM 的接入点，将 reporter 的 auth 修改为 Token。
3. 重启服务，开始上报数据。
4. 接入验证。

向应用发送请求，在收到响应后，在应用性能监控控制台查看调用数据。 您可以在1分钟内通过**链路追踪** > **[调用查询](https://console.cloud.tencent.com/apm/monitor/span)** 查找调用详情。监控曲线与统计数据将在1分钟后开始正常显示。

## Go2Sky 改造示例

以下是基于 Go2Sky 的 Demo 改造示例，您可根据实际情况进行修改。

1. 在 NewGRPCReporter 的时设置上报地址和 Authentication（上报地址与 Token 的获取方式参见 [步骤1](https://git.woa.com/taw/go-skywalking-taw-simple-demo/blob/master/README.md#step1)）。
<dx-codeblock>
:::  go
report, err = reporter.NewGRPCReporter(
"ap-guangzhou.tencentservicewatcher.com:11800",
reporter.WithAuthentication("tsw_site@xxxxxxxxxx"))
:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
请根据控制台给出的私网接入点和 Token 进行改造。
</dx-alert>
2. 进行 Server 端配置，Demo 如下：
<dx-codeblock>
:::  go
package main
import (
"flag"
"github.com/SkyAPM/go2sky"
v3 "github.com/SkyAPM/go2sky-plugins/gin/v3"
"github.com/SkyAPM/go2sky/reporter"
"github.com/gin-gonic/gin"
"log"
"net/http"
)

var (
grpc bool
oapServer string
listenAddr string
serviceName string
client *http.Client
)

func init() {
flag.BoolVar(&grpc, "grpc", false, "use grpc reporter")
//9.223.77.222:11800 需替换为 TAW 的私网接入点
flag.StringVar(&oapServer, "oap-server", "9.223.77.222:11800", "oap server address")
flag.StringVar(&listenAddr, "listen-addr", "0.0.0.0:8809", "listen address")
flag.StringVar(&serviceName, "service-name", "go2sky-server", "service name")
}

func main() {
flag.Parse()
log.Println("reporter.NewGRPCReporter start")
var report go2sky.Reporter
var err error
/*
参数说明：
@oapServer:SkyWalking 后端收集器地址
*/
report, err = reporter.NewGRPCReporter(
oapServer,
reporter.WithAuthentication("c944279f910baee6d2e1028172xxxxxx"))
//c944279f910baee6d2e1028172xxxxxx 需替换成您的 Token
//report, err = reporter.NewLogReporter()
if err != nil {
log.Fatalf("crate grpc reporter error: %v \n", err)
}
/*
参数说明：
@service 服务名字, 以 @结尾代表该服务所在 DMP 租户。
@opts 固定格式，一个Reporter的实例
*/
log.Println("go2sky.NewTracer")
tracer, err := go2sky.NewTracer(serviceName, go2sky.WithReporter(report))
if err != nil {
log.Fatalf("crate tracer error: %v \n", err)
}

gin.SetMode(gin.ReleaseMode)
r := gin.New()
:::
</dx-codeblock>
