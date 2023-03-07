本文将为您介绍如何通过 opentelemetry - grpc-go 上报 Go 应用数据。

## 操作步骤

### 步骤1：获取接入点和 Token
进入**应用监控** > **应用列表**，单击**接入应用**页面，在接入应用时选择 GO 语言与  opentelemetry - grpc-go 的数据采集方式。 
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)



### 步骤2：修改接入点信息
> ? 我们采用 grpc-go 拦截器方式上报数据，需要修改接入点信息为：ap-guangzhou.apm.tencentcs.com:14268/api/traces，可以直接将数据上报到 collector，无需使用 agent。

### 步骤3：引入依赖
需要引入 opentelemetry 的 SDK 埋点依赖。
- 依赖路径： "[go.opentelemetry.io/otel/sdk/trace](http://go.opentelemetry.io/otel/sdk/trace)"

### 步骤4：trace 初始化
```
// Init配置OpenTelemetry
func Init() *sdktrace.TracerProvider {
    if ctx == nil {
        ctx = context.Background()
    }
    //创建新的exporter，设置基本的endpoint
    opts := []otlptracegrpc.Option{
        otlptracegrpc.WithEndpoint("<接入点>"),
        otlptracegrpc.WithInsecure(),
    }
    exporter, err := otlptracegrpc.New(ctx, opts...)
    if err != nil {
        log.Fatal(err)
    }

    //设置Token，也可以设置环境变量：OTEL_RESOURCE_ATTRIBUTES=token=xxxxxxxxx
    r, err := resource.New(ctx, []resource.Option{
        //设置Token值
        resource.WithAttributes(attribute.KeyValue{
            Key: "token", Value: attribute.StringValue("<Token>"),
        }),
        //设置服务名
        resource.WithAttributes(attribute.KeyValue{
            Key: "service.name", Value: attribute.StringValue("audotanggrpcdemo"),
        }),
    }...)
    if err != nil {
        log.Fatal(err)
    }

    //创建新的TracerProvider
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

### 步骤5：选择上报端类型上报应用数据
#### 服务端
1. 初始化 TracerProvider。
```
    //初始化trace
    tp := trace.Init()
    defer func() {
        if err := tp.Shutdown(context.Background()); err != nil {
            log.Printf("Error shutting down tracer provider: %v", err)
        }
    }()
    //指定host
    host := os.Getenv("grpc1")

    lis, err := net.Listen("tcp", host+":7778")
    if err != nil {
        log.Fatalf("failed to listen: %v", err)
    }
```
2. 配置拦截器
```
    s := grpc.NewServer(
        grpc.UnaryInterceptor(otelgrpc.UnaryServerInterceptor()),
        grpc.StreamInterceptor(otelgrpc.StreamServerInterceptor()),
    )
```
3. 启动 server 服务
```
    //在gRPC服务器处注册我们的服务
    api.RegisterHelloServiceServer(s, &server{})
    reflection.Register(s)
    if err := s.Serve(lis); err != nil {
        log.Fatalf("failed to serve: %v", err)
    }
```

#### 客户端配置
1. 初始化 TracerProvider。
```
    //初始化trace
    tp := trace.Init()
    defer func() {
        if err := tp.Shutdown(context.Background()); err != nil {
            log.Printf("Error shutting down tracer provider: %v", err)
        }
    }()
```
2. 建立连接，配置拦截器。
```
    //向服务端建立连接，配置拦截器
    conn, err := grpc.DialContext(context.Background(), "localhost:7778", grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithBlock())
```
3. 进行 GRPC 调用。
```
    c := api.NewHelloServiceClient(conn)
    for {
        callSayHelloClientStream(c)
        time.Sleep(100 * time.Millisecond)
    }
```

