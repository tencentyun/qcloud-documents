TSF-Go 基于轻量级 Go 微服务框架 [Kratos](https://github.com/go-kratos/kratos) 为用户现存的 Go 应用提供了接入TSF 治理平台的能力。本文档介绍 Go 应用从接入TSF 到部署应用的操作方法及相关注意事项。
>?您也可以通过 [SDK 文档](https://github.com/tencentyun/tsf-go) 查看 TSF Go 最新使用说明。

## 功能特性

- 自动集成 TSF 平台治理能力：分布式远程配置、远程日志、分布式调用链追踪、监控、服务鉴权、服务路由、全链路灰度发布、API 自动上报。
- 同时支持 gRPC 和 HTTP 协议，并可以和 Java Spring Cloud 服务互相调用。
- 开放性高，丰富的 Middlewares、Options 可以自定义组件。
- 一切围绕 Protobuf 定义 Service、Interface、Error、Validating、Swagger json 等。
- 拥抱开源规范、Trace、Validate、API Definition 等都直接使用开源规范和协议。
- 支持私有化部署。

## 安装依赖

#### 1. 安装 protoc v3.15.0+

请根据自己使用的操作系统，优先选择对应的包管理工具安装，如：

- Linux 下用 yum或 apt 等安装
- macOS 通过 brew 安装
- Windows 通过下载可执行程序或者其他安装程序来安装

#### 2. 安装 protoc-gen-xxx

```bash
go get -u github.com/golang/protobuf/protoc-gen-go
go get -u google.golang.org/grpc/cmd/protoc-gen-go-grpc
go get -u github.com/go-kratos/kratos/cmd/protoc-gen-go-http
```

## 服务端开发

#### 1. 通过 protobuf 定义服务接口

```protobuf
syntax = "proto3";

// 定义protobuf包名pacakage_name
package helloworld;

// 如果不使用restful http协议，可以不引入此proto
import "google/api/annotations.proto";

// 这里go_package指定的是protofbu生成文件xxx.pb.go在git上的地址
option go_package = "github.com/tencentyun/tsf-go/examples/helloworld/proto";

// 定义服务名service_name
service Greeter {
  // 方法接口名,rpc_method
  rpc SayHello (HelloRequest) returns (HelloReply)  {    
  }
}

//  请求参数
message HelloRequest {
  string name = 1;
}

// 响应参数
message HelloReply {
  string message = 1;
}
```

如上，这里我们定义了一个Greeter服务，这个服务里面有个 SayHello 方法，接收一个包含 msg 字符串的 HelloRequest 参数，返回 HelloReply 数据。
这里需要注意以下几点：

- syntax 必须是 proto3，tsf go 都是基于 proto3 通信的。
- package 后面必须有 option go_package="github.com/tencentyun/tsf-go/examples/helloworld/proto";指明您的pb.go生成文件的git存放地址，协议与服务分离，方便其他人直接引用
- 编写 protobuf 时必须遵循 [谷歌官方规范](https://developers.google.com/protocol-buffers/docs/style)。

#### 2. 生成服务端桩代码 xxx.pb.go 代码

通过protoc命令生成服务代码(grpc协议)
`protoc --proto_path=. --proto_path=./third_party
--go_out=paths=source_relative:. --go-grpc_out=paths=source_relative:. *.proto`

#### 3. 编写 service 实现层代码

```go
import	pb "github.com/tencentyun/tsf-go/examples/helloworld/proto"

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnimplementedGreeterServer
}

// SayHello implements helloworld.GreeterServer
func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	return &pb.HelloReply{Message: fmt.Sprintf("Welcome %+v!", in.Name)}, nil
}
```

#### 4. 编写 server(grpc 协议) 启动入口 main.go

```go
import  pb "github.com/tencentyun/tsf-go/examples/helloworld/proto"
import 	tsf "github.com/tencentyun/tsf-go"
import  "github.com/go-kratos/kratos/v2"
import  "github.com/go-kratos/kratos/v2/transport/grpc"

func main() {
    flag.Parse()
    // grpc协议
    grpcSrv := grpc.NewServer(
        // 定义grpc协议监听地址
        grpc.Address(":9000"),
        grpc.Middleware(
            // 使用tsf默认的middleware
            tsf.ServerMiddleware(),
        ),
    )
    // 将第三步骤中的service实现结构体注入进grpc server中
    s := &server{}
    pb.RegisterGreeterServer(grpcSrv, s)
  
    // 应用配置
    opts := []kratos.Option{
        // 定义注册到服务发现中的服务名
        kratos.Name("provider-grpc"),
        // 添加grpc server至应用运行时
        kratos.Server(grpcSrv),
    }
    // 添加tsf应用默认启动配置
    // 如果不想启用服务注册，可以加入tsf.EnableReigstry(false)该Option
    opts = append(opts, tsf.AppOptions()...)
    app := kratos.New(opts...)
    // 应用阻塞式启动
    if err := app.Run(); err != nil {
        panic(err) 
    }
}
```

#### 5. 服务启动

- 参考 [轻量级服务注册中心](https://cloud.tencent.com/document/product/649/16618) 搭建并启动一个本地轻量级 consul 注册中心；如果暂时不想启动服务注册直接调试，则可以在第4步骤中传入 `tsf.EnableReigstry(false)` 即：`opts = append(opts, tsf.AppOptions(tsf.EnableReigstry(false))...)`
- 执行 `go run main.go` 即可启动 server。

## 客户端开发（gRPC 协议）

#### 1. 编写客户端代码

```go
import  pb "github.com/tencentyun/tsf-go/examples/helloworld/proto"
import  tsf "github.com/tencentyun/tsf-go"
import 	"github.com/go-kratos/kratos/v2/transport/grpc"
import  "import  "github.com/go-kratos/kratos/v2"

func main() {
    flag.Parse()
    // 指定被调方服务连接地址:<scheme>://<authority>/<service_name>
    // 如果使用服务发现，此处scheme固定为discovery，authority留空，service_name为定义注册到服务发现中的服务名
    // 如果不使用服务发现，直接填写"<ip>:<port>"即可
    clientOpts := []grpc.ClientOption{grpc.WithEndpoint("discovery:///provider-grpc")}
    // 如果不使用服务发现，此行可以删除
    clientOpts = append(clientOpts, tsf.ClientGrpcOptions()...)
    conn, err := grpc.DialInsecure(context.Background(), clientOpts...)
    if err != nil {
        panic(err)
    }
    client := pb.NewGreeterClient(conn)
    reply, err := client.SayHello(context.Background(), &pb.HelloRequest{Name: "tsf_grpc"})
    if err != nil {
        panic(err)
    }
}
```

#### 2.启动客户端

执行 `go run main.go` 即可启动客户端。

## 部署至腾讯云 TSF 治理平台

#### 1. 在 TSF 上创建应用和镜像仓库

参考文档 [应用管理](https://cloud.tencent.com/document/product/649/56145) 创建应用并开通镜像仓库。

#### 2. 编写 Dockerfile

```dockerfile
FROM centos:7

RUN echo "ip_resolve=4" >> /etc/yum.conf
#RUN yum update -y && yum install -y ca-certificates

# 设置时区。这对于日志、调用链等功能能否在 TSF 控制台被检索到非常重要。
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
ENV workdir /app/

COPY provider ${workdir}
WORKDIR ${workdir}

# tsf-consul-template-docker 用于文件配置功能，如不需要可注释掉该行
#ADD tsf-consul-template-docker.tar.gz /root/

# JAVA_OPTS 环境变量的值为部署组的 JVM 启动参数，在运行时 bash 替换。如果加了${JAVA_OPTS},需要在TSF的容器部署组启动参数中删除默认的"-Xms128m xxx"参数,否则会启动失败
#使用 exec 以使 Java 程序可以接收 SIGTERM 信号。
CMD ["sh", "-ec", "exec ${workdir}provider ${JAVA_OPTS}"]
```

您需要将上述的 provider 替换为实际的可执行二进制文件名。

#### 3. 打包镜像

将 `GOOS=linux go build` 编译出的二进制文件放在 Dockfile 同一目录下，执行如下命令。

```
docker build . -t ccr.ccs.tencentyun.com/tsf_xxx/provider:1.0
```

镜像地址改成应用上传镜像页面中实际的地址

#### 4. 推送镜像

执行如下命令推送镜像到镜像仓库。

```
docker push ccr.ccs.tencentyun.com/tsf_xxx/provider:1.0
镜像地址改成应用上传镜像页面中实际的地址
```

#### 5. 部署应用

参考文档 [部署组管理](https://cloud.tencent.com/document/product/649/15525)。

## 更多文档

- [HTTP Restful 开发](https://github.com/tencentyun/tsf-go/blob/master/docs/HTTP.md)
- [TSF 远程配置](https://github.com/tencentyun/tsf-go/blob/master/docs/Config.md)
- [Swagger API 上报](https://github.com/tencentyun/tsf-go/blob/master/docs/Swagger.md)
- [错误定义](https://github.com/tencentyun/tsf-go/blob/master/docs/Error.md)
- [分布式调用链追踪](https://github.com/tencentyun/tsf-go/blob/master/docs/Trace.md)
- [自定义标签](https://github.com/tencentyun/tsf-go/blob/master/docs/Metadata.md)
- [负载均衡](https://github.com/tencentyun/tsf-go/blob/master/docs/Balancer.md)
- [自适应熔断](https://github.com/tencentyun/tsf-go/blob/master/docs/Breaker.md)

## Examples

- [gRPC](https://github.com/tencentyun/tsf-go/blob/master/examples/helloworld/grpc)
- [HTTP](https://github.com/tencentyun/tsf-go/blob/master/examples/helloworld/http)
- [gin-go](https://github.com/tencentyun/tsf-go/blob/master/examples/helloworld/gin)
- [log](https://github.com/tencentyun/tsf-go/blob/master/examples/log)
- [error](https://github.com/tencentyun/tsf-go/blob/master/examples/error)
- [tracing](https://github.com/tencentyun/tsf-go/blob/master/examples/tracing)
- [breaker](https://github.com/tencentyun/tsf-go/tree/master/examples/breaker)
