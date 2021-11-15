## 操作场景
Dubbo 作为一款传统基于 SDK 的 Java RPC 框架，通过引入 jar 包的方式实现服务间远程方法调用、服务注册发现及服务治理。Dubbo 开发的应用在不修改任何业务代码的前提下，通过简单的 Mesh 封包部署到 TSF 平台，可透明实现服务注册发现和无侵入的服务治理能力。

本文档以 Dubbo Mesh Demo 为例介绍 Dubbo 应用在 TSF 平台接入 Mesh 的操作方案及相关注意事项。

<span id="demo"></span>
## 前提条件
已下载 [Dubbo Mesh Demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/mesh-demo/tsf-mesh-dubbo-demo.tar.gz)

## 操作步骤
#### 1. Maven 环境安装
详细操作请参考 [Maven 安装](https://cloud.tencent.com/document/product/649/20231#2.-.E5.AE.89.E8.A3.85-maven)。

#### 2. 配置 spec.yaml 服务注册文件
Dubbo Mesh Demo 中提供了三个 Dubbo 应用，以 greet 应用为例，其 spec.yaml 配置为：
```yaml
apiVersion: v1
kind: Application
spec:
  services:
    - name: org.apache.dubbo.samples.api.GreetingService # 需要注册的 Dubbo 服务名，必须跟提供的 interface 名保持一致
      ports:
        - targetPort: 20881 # 该 Dubbo 服务监听的端口
          protocol: dubbo # 协议指定为 Dubbo
      healthCheck:
        path:

```

>?部署到 TSF 平台后，Mesh 的 sidecar 解析 Dubbo 应用的 spec.yaml，根据服务名、监听端口、协议等信息自动注册服务到注册中心。

屏蔽 greet 应用原注册中心（可选）：
```xml
<dubbo:registry address="N/A" subscribe="false" register="false"/>
```

>?此处也可保留原注册中心，实现 Dubbo 服务双注册。

#### 3. 编译打包
Dubbo Mesh Demo 中每个应用都提供了`build.sh`脚本用于构建部署在 TSF 上的 Mesh 程序包，执行`./build.sh`将在当前目录下生成对应的`tar.gz`包，该包可直接部署在 TSF 上，以 greet 应用为例，生成的程序包为`dubbo-greet.tar.gz`，文件目录包括：
- dubbo-samples-greetservice-1.0.jar: Maven 构建的 FATJAR 包
- start.sh
- stop.sh
- cmdline
- spec.yaml

`build.sh`脚本及程序包中文件详细内容请 [下载 Dubbo Mesh Demo](#demo) 查看。

## Dubbo 兼容说明
- TSF Mesh 为 Dubbo 应用提供服务间通信、服务注册发现、负载均衡、服务路由、服务熔断、服务鉴权和服务限流等治理能力。
- Dubbo 应用可以保留原有的注册方式。
- Dubbo 应用可以继续使用原有的 filter 机制。


