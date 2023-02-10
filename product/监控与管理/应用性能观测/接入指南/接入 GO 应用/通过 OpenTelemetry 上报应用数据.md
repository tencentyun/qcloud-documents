OpenTelemetry 是工具、API 和 SDK 的集合。使用它来检测、生成、收集和导出遥测数据（指标、日志和跟踪），以帮助您分析软件的性能和行为。本文将介绍如何使用 OpenTelemetry 上报 Go 应用数据。




### 步骤一：获取接入点和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 Go 语言与 OpenTelemetry 的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

<dx-alert infotype="explain" title="上报方式说明">
- 内网上报：使用此上报方式，您的服务需运行在腾讯云 VPC 。通过 VPC 直接联通，在避免外网通信的安全风险同时，可以节省上报流量开销。
- 外网上报：当您的服务部署在本地或非腾讯云 VPC 内，可以通过此方式上报数据。请注意外网通信存在安全风险，同时也会造成一定上报流量费用。
</dx-alert>


### 步骤二：上报 Go 应用数据

1. 引入 opentelemtry-sdk 依赖，进行 sdk 埋点上报，首先对 trace 进行构造：
```
import (
	"context"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	"log"
	_ "os"
)
// Init configures an OpenTelemetry exporter and trace provider
func Init(ctx context.Context) *sdktrace.TracerProvider {
	//New otlp exporter
	opts := []otlptracegrpc.Option{
		// 配置上报地址，如 config.yaml 里已配置，此处可忽略
		otlptracegrpc.WithEndpoint("{接入点信息}"), otlptracegrpc.WithInsecure(),
	}
	exporter, err := otlptracegrpc.New(ctx,opts...)
	if err != nil {
		log.Fatal(err)
	}
	//在 Resource 下设置上报 Token，也可以直接配置环境变量来设置 token: OTEL_RESOURCE_ATTRIBUTES=token=xxxxxxxxx 如 config.yaml 里已配置，此处可忽略
	r,err := resource.New(ctx,[]resource.Option{
		resource.WithAttributes(attribute.KeyValue{Key: "token",Value: attribute.StringValue("{上报token}"),}),
	}...)

	if err != nil{
		log.Fatal(err)
	}
	//创建一个新的TracerProvider
	tp := sdktrace.NewTracerProvider(
		sdktrace.WithSampler(sdktrace.AlwaysSample()),
		sdktrace.WithBatcher(exporter),
		sdktrace.WithResource(r),
	)
	otel.SetTracerProvider(tp)
	otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(propagation.TraceContext{}, propagation.Baggage{}))
	return tp
}
```
2. 以 grpc 为例，服务端代码中，首先进行 trace 的初始化，并在创建服务时设置拦截器，再根据自身的服务编写服务代码即可。
```
func main() {

	tp := trace.Init() //初始化工作，Init方法即为上述的构造方法
	defer func() {
		if err := tp.Shutdown(context.Background()); err != nil {
			log.Printf("Error shutting down tracer provider: %v", err)
		}
	}()

	host := os.Getenv("grpc1")

	lis, err := net.Listen("tcp", host+":7778")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer(
		grpc.UnaryInterceptor(otelgrpc.UnaryServerInterceptor()),     //设置拦截器进行埋点
		grpc.StreamInterceptor(otelgrpc.StreamServerInterceptor()),
	)

	api.RegisterHelloServiceServer(s, &server{})   //注册服务，具体服务代码可自行更改
	reflection.Register(s)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
```
3. 以 grpc 为例，客户端代码中，依然首先进行 trace 的初始化，并建立链接。
```
func main() {
	tp := trace.Init()    //初始化
	fmt.Println("tp create success")
	defer func() {
		if err := tp.Shutdown(context.Background()); err != nil {
			log.Printf("Error shutting down tracer provider: %v", err)
		}
	}()
	fmt.Println("aaa")
	conn, err := grpc.DialContext(context.Background(), "localhost:7778", grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithBlock()) //建立连接
	fmt.Println("pro")
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	fmt.Println("conn")

	c := api.NewHelloServiceClient(conn)  //客户端代码

	for {
		callSayHelloClientStream(c)
		time.Sleep(100 * time.Millisecond)
	}
```

>?若需要上报服务端数据，则需要指明字段 span.kind = server 
><img src="https://qcloudimg.tencent-cloud.cn/raw/83246ec0c0c55a492c49401105e2bd58.png" width=55%"">

### 步骤三：启动您的应用



### 查看应用数据
登录 [应用性能观测控制台](https://console.cloud.tencent.com/apm) ，在应用列表中即可查看性能数据。

