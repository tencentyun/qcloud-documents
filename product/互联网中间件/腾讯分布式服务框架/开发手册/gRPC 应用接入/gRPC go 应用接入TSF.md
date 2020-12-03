# gRPC go 接入 TSF
TSF 为用户现存的的 gRPC 应用提供了go语言sdk插件，gRPC 应用可通过依赖go package的方式接入该项服务。本文档介绍 gRPC 应用从接入TSF 到部署应用的操作方法及相关注意事项。

## 特性
- 自动集成TSF平台治理能力：分布式远程配置、远程日志、分布式调用链追踪、监控、服务鉴权、服务路由、全链路灰度发布、API自动上报（全局限流、熔断暂不支持）
- Server同时支持gRPC&HTTP双协议,可以被Spring Cloud服务调用
- 改动小，集成SDK成本低

## 说明
暂时只支持go语言 

gRPC接入TSF最新文档地址也可以点击此处查看:[TSF gRPC go](https://github.com/tencentyun/tsf-go/blob/master/doc/GRPC.md)

## Server端接入

#### 1. 生成*.pb.go文件
protoc --go_out=plugins=grpc:. *.proto

#### 2. 引入TSF的package
`import "github.com/tencentyun/tsf-go/pkg/grpc/server"`	

#### 3. 修改启动入口代码
```
server := server.NewServer(&server.Config{ServerName: "provider-demo"})
pb.RegisterGreeterServer(server.GrpcServer(), &Service{})
err := server.Start()
if err != nil {
	panic(err)
}
````
需将代码中`provider-demo`替换成实际的gRPC serviceName
如果配置文件中不指定端口则默认为8080，也可以通过tsf_service_port环境或者启动参数来指定，其他的可指定的配置参考`pkg/sys/env/env.go`中定义的Key

> 通过TSF启动的gRPC server除了gRPC协议同时还支持http1.1+json（可以被Spring Cloud服务调用），此时http的path为：/<package_name.service_name>/<method\>
比如：curl -v -X POST --data '{"name":"grpc world"}' 127.0.0.1:8080/tsf.test.helloworld.Greeter/SayHello
想要禁用这个feature可以注入环境变量或启动参数：tsf_disable_grpc_http=true

## Client端接入

#### 1. 生成*.pb.go文件
protoc --go_out=plugins=grpc:. *.proto

#### 2. 引入TSF的package
`import "github.com/tencentyun/tsf-go/pkg/grpc/client"`	

#### 3. 生成gRPC client stub：
```
ctx, cancel := context.WithTimeout(context.Background(), time.Second*3)
defer cancel()
cc, err := client.DialWithBlock(ctx, "consul://local/provider-demo")
if err != nil {
	panic(err)
}
greeter := pb.NewGreeterClient(cc.GrpcConn())
```
需将`tsf.provider-demo`需要替换成实际被访问的服务提供者的serviceName
`local`的含义是访问本地命名空间的服务,如果需要发现全局命名空间服务需要替换成`global`

## 标签Tags传递
```
ctx = meta.WithUser(ctx, meta.UserPair{Key: "user", Value: "test2233"})
s.client.SayHello(ctx, req)
```

## TSF日志
#### 1.引入package
`import 	"github.com/tencentyun/tsf-go/pkg/log"`
#### 2.打印日志
```
log.Infof(ctx, "got resp: %v", resp)
log.Info(context.Background(), "got message", zap.String("resp",resp))
```
> 可以通过注入环境变量tsf_log_path或者启动参数tsf_log_path来指定日志输出路径
注意如果不传递go的ctx，会导致日志中不打印traceID
同时需要在tsf日志配置中配置日志类型为:自定义Logback,日志格式为:%d{yyyy-MM-dd HH:mm:ss.SSS} %level %msg%n



## 分布式配置
#### 1.import配置模块
`"github.com/tencentyun/tsf-go/pkg/config/tsf"`
#### 2.初始化配置模块
`if err := tsf.Init(context.Background());err != nil {
		panic(err)
	}`
#### 3.初始化完毕后直接非阻塞get某一个配置值：
```
if temp, ok := tsf.GetApp("prefix");ok {
	prefix, _ = temp.(string)
}
```
#### 4.订阅某一个配置文件的变化:
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

## 容器部署
#### 1. 编写Dockerfile:
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

# JAVA_OPTS 环境变量的值为部署组的 JVM 启动参数，在运行时 bash 替换。使用 exec 以使 Java 程序可以接收 SIGTERM 信号。
CMD ["sh", "-ec", "exec ${workdir}provider ${JAVA_OPTS}"]
```
替换其中的provider为实际的可执行二进制文件名

#### 2. 打包镜像
将`GOOS=linux go build`编译出的二进制文件放在Dockfile同一目录下
docker build . -t ccr.ccs.tencentyun.com/tsf_xxx/provider:1.0

#### 3. 推送镜像
docker push ccr.ccs.tencentyun.com/tsf_xxx/provider:1.0

#### 4. 在tsf上部署镜像

## 虚拟机部署
#### 1. 编写start.sh：
```
#!/bin/bash

already_run=`ps -ef|grep "./provider"|grep -v grep|wc -l`
if [ ${already_run} -ne 0 ];then
	echo "provider already Running!!!! Stop it first"
	exit -1
fi

nohup ./provider >stdout.log 2>&1 &
```
替换其中的provider为实际的可执行二进制文件名

#### 2. 编写stop.sh:
```
#!/bin/bash

pid=`ps -ef|grep "./provider"|grep -v grep|awk '{print $2}'`
kill -SIGTERM $pid
echo "process ${pid} killed"
```
替换其中的provider为实际的可执行二进制文件名

#### 3. 编写cmdline:
`./provider`
替换其中的provider为实际的可执行二进制文件名

#### 4. 将可执行二进制文件拷贝进当前目录
   
#### 5. 将当前目录打包成tar.gz: tar –czf provider.tar.gz *
   
#### 6. 上传provider.tar.gz并部署
