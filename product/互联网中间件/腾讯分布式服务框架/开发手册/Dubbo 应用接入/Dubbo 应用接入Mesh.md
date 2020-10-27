## 操作场景
Dubbo作为一款传统基于SDK的Java RPC框架，通过引入jar包的方式实现服务间远程方法调用、服务注册发现及服务治理；Dubbo开发的应用在不修改任何业务代码的前提下，通过简单的Mesh封包部署到TSF平台，可透明实现服务注册发现和无侵入的服务治理能力。本文档以Dubbo Mesh Demo为例介绍Dubbo应用在TSF平台接入Mesh的操作方案及相关注意事项。

[Dubbo Mesh Demo下载](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/mesh-demo/tsf-mesh-dubbo-demo.tar.gz)

## 操作步骤
#### 1. Maven 环境安装
详细操作请参考 [Maven 安装](https://cloud.tencent.com/document/product/649/20231#2.-.E5.AE.89.E8.A3.85-maven)。

#### 2. 配置spec.yaml服务注册文件
Dubbo Mesh Demo中提供了三个dubbo应用，以greet应用为例，其spec.yaml配置为：
```yaml
apiVersion: v1
kind: Application
spec:
  services:
    - name: org.apache.dubbo.samples.api.GreetingService # 需要注册的dubbo服务名，必须跟提供的interface名保持一致
      ports:
        - targetPort: 20881 # 该dubbo服务监听的端口
          protocol: dubbo # 协议指定为dubbo
      healthCheck:
        path:

```

>?部署到TSF平台后，mesh的sidecar解析dubbo应用的spec.yaml，根据服务名、监听端口、协议等信息自动注册服务到注册中心。

屏蔽greet应用原注册中心（可选）：
```xml
<dubbo:registry address="N/A" subscribe="false" register="false"/>
```

>?此处也可保留原注册中心，实现dubbo服务双注册。

#### 3. 编译打包
Dubbo Mesh Demo中每个应用都提供了`build.sh`脚本用于构建部署在TSF上的Mesh程序包，执行`./build.sh`将在当前目录下生成对应的`tar.gz`包，该包可直接部署在TSF上，以greet应用为例，生成的程序包为`dubbo-greet.tar.gz`，文件目录包括：
- dubbo-samples-greetservice-1.0.jar: Maven构建的FATJAR包
- start.sh
- stop.sh
- cmdline
- spec.yaml

`build.sh`脚本及程序包中文件详细内容请下载Dubbo Mesh Demo查看。

## Dubbo 兼容说明
- TSF Mesh为Dubbo应用提供服务间通信、服务注册发现、负载均衡、服务路由等治理能力
- Dubbo应用可以保留原有的注册方式
- Dubbo应用可以继续使用原有的filter机制
