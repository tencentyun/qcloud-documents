## 操作场景
TSF 为用户现存的的 gRPC 应用提供了 Go 语言 SDK 插件，gRPC 应用可通过依赖 Go package 的方式接入该项服务。
本文档介绍 gRPC 应用从接入TSF 到部署应用的操作方法及相关注意事项。


## 功能特性
- 自动集成 TSF 平台治理能力：分布式远程配置、远程日志、分布式调用链追踪、监控、服务鉴权、服务路由、全链路灰度发布、API 自动上报（全局限流、熔断暂不支持）。
- Server 同时支持 gRPC 和 HTTP 双协议，可以被 Spring Cloud 服务调用。
- 改动小，集成 SDK 成本低。

>?目前只支持 Go 语言。您也可以通过 GitHub 查看 [gRPC 接入 TSF](https://github.com/tencentyun/tsf-go/blob/master/doc/GRPC.md) 的最新文档。

## 快速上手
### Server 端

#### 1. 生成 *.pb.go 文件
`protoc --go_out=plugins=grpc:. *.proto`
>?详细说明请参考 [gRPC Go 教程](https://cloud.tencent.com/document/product/1165/46154)。 

#### 2. 引入 TSF 的 package
`import "github.com/tencentyun/tsf-go/pkg/grpc/server"`	

#### 3. 修改启动入口代码
```
server := server.NewServer(&server.Config{ServerName: "provider-demo"})
pb.RegisterGreeterServer(server.GrpcServer(), &Service{})
err := server.Start()
if err != nil {
	panic(err)
}
```
- 您需将代码中的 `provider-demo` 替换成实际的 gRPC serviceName。
- 如果配置文件中不指定端口则默认为8080，也可以通过 tsf_service_port 环境或者启动参数来指定，其他的可指定的配置参考`pkg/sys/env/env.go`中定义的 Key。

>?通过 TSF 启动的 gRPC server 除了 gRPC 协议同时还支持 HTTP1.1+JSON（可以被 Spring Cloud 服务调用），此时 HTTP 的 path 为`/<package_name.service_name>/<method>`，例如 `curl -v -X POST --data '{"name":"grpc world"}' 127.0.0.1:8080/tsf.test.helloworld.Greeter/SayHello`。
如需禁用该功能可以注入环境变量或启动参数：tsf_disable_grpc_http=true。

### Client 端

#### 1. 生成 *.pb.go 文件
`protoc --go_out=plugins=grpc:. *.proto`

#### 2. 引入 TSF 的 package
`import "github.com/tencentyun/tsf-go/pkg/grpc/client"`	

#### 3. 生成 gRPC client stub
```
ctx, cancel := context.WithTimeout(context.Background(), time.Second*3)
defer cancel()
cc, err := client.DialWithBlock(ctx, "consul://local/provider-demo")
if err != nil {
	panic(err)
}
greeter := pb.NewGreeterClient(cc.GrpcConn())
```
- 您需将 `tsf.provider-demo` 需要替换成实际被访问的服务提供者的 serviceName。
- `local` 是访问本地命名空间的服务，如果需要发现全局命名空间服务则要替换成 `global`。

## 集成 TSF 中其他能力

### TSF 标签 Tags 传递
```
ctx = meta.WithUser(ctx, meta.UserPair{Key: "user", Value: "test2233"})
s.client.SayHello(ctx, req)
```

### 远程日志
#### 1. 引入 package
`import 	"github.com/tencentyun/tsf-go/pkg/log"`
#### 2. 打印日志
```
log.Infof(ctx, "got resp: %v", resp)
log.Info(context.Background(), "got message", zap.String("resp",resp))
```
- 您可以通过注入环境变量 tsf_log_path 或者启动参数 tsf_log_path 来指定日志输出路径。
- 如果不传递 Go 的 context，会导致日志中不打印 traceID。
- 需要在 TSF 日志配置中配置日志类型为自定义 Logback，日志格式为 `%d{yyyy-MM-dd HH:mm:ss.SSS} %level %msg%n`。

>?更多 TSF 日志配置可参考 [日志服务说明](https://cloud.tencent.com/document/product/649/18196)。 

### 分布式配置
#### 1. 引入配置模块
`"github.com/tencentyun/tsf-go/pkg/config/tsf"`
#### 2. 初始化配置模块
`if err := tsf.Init(context.Background());err != nil {
		panic(err)
	}`
#### 3. 非阻塞获取某一个配置值
```
if temp, ok := tsf.GetApp("prefix");ok {
	prefix, _ = temp.(string)
}
```
#### 4. 订阅某一个配置文件的变化
```
type AppConfig struct {
	Prefix string `yaml:"prefix"`
}
tsf.AppConfig(func(cfg *tsf.Config) {
		if cfg == nil {
			// 配置文件不存在（被删除）
			return
		}
		var appCfg AppConfig
		err := cfg.Unmarshal(&appCfg)
		if err != nil {
			log.L().Info(context.Background(), "reload remote config failed!", zap.String("raw", string(cfg.Raw())))
			return
		}
		service.prefix.Store(appCfg.Prefix)
})
```
>?更多 TSF 分布式配置的说明请参考 [配置管理概述](https://cloud.tencent.com/document/product/649/17956)。 

## 部署应用
### 容器部署
#### 1. 编写 Dockerfile
```
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

#### 2. 打包镜像
将 `GOOS=linux go build` 编译出的二进制文件放在 Dockfile 同一目录下：
`docker build . -t ccr.ccs.tencentyun.com/tsf_xxx/provider:1.0`

#### 3. 推送镜像
`docker push ccr.ccs.tencentyun.com/tsf_xxx/provider:1.0`

#### 4. 在 TSF 上部署镜像

### 虚拟机部署
#### 1. 编写 start.sh
```
#!/bin/bash

already_run=`ps -ef|grep "./provider"|grep -v grep|wc -l`
if [ ${already_run} -ne 0 ];then
	echo "provider already Running!!!! Stop it first"
	exit -1
fi

nohup ./provider >stdout.log 2>&1 &
```
您需要将上述的 provider 替换为实际的可执行二进制文件名。

#### 2. 编写 stop.sh
```
#!/bin/bash

pid=`ps -ef|grep "./provider"|grep -v grep|awk '{print $2}'`
kill -SIGTERM $pid
echo "process ${pid} killed"
```
您需要将上述的 provider 替换为实际的可执行二进制文件名。

#### 3. 编写 cmdline
`./provider`
您需要将上述的 provider 替换为实际的可执行二进制文件名。

#### 4. 将可执行二进制文件复制进当前目录
   
#### 5. 将当前目录打包成 tar.gz: tar –czf provider.tar.gz *
   
#### 6. 上传 provider.tar.gz 并部署
