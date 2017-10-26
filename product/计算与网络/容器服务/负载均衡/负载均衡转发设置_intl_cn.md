## Ingress转发设置

### Ingress说明
容器服务支持4层负载均衡器来转发流量到容器上，4层支持公网型和内网型负载均衡器，更多负载均衡器介绍可查看[负载均衡简介](https://cloud.tencent.com/document/product/214/524)。本文主要讲解容器服务如何使用Ingress实现7层的HTTP和HTTPS的转发。

### 使用Ingress前置条件
创建服务提供以下4种访问方式选择：

- 使用负载均衡(公网4层，TCP/UDP) —— 可使用
- 使用负载均衡(内网4层，TCP/UDP) —— 可使用
- 使用主机端口 —— 可使用
- 仅集群内访问 —— 可使用，会自动打开主机端口用于路由转发。

使用Ingress目前支持应用型LB类型,流量先转发到主机再转发到容器上，负载均衡后端RS(即容器节点)需打开对应的端口，故仅在集群内访问的服务若需要使用Ingress也会自动打开主机端口。。
您可以灵活的使用4层LB和Ingress来设置您的服务的访问方式。如即使用内网的负载均衡又使用应用型负载均衡器，同一个服务即有内网入口又有外网入口以适配您的不同的业务要求。

![Alt text](https://mc.qcloudimg.com/static/img/a87562b86939fb9375b49fcc7a045cac/%7BE6F16A25-D6CD-44B2-B6F8-FFF5E3A92BA3%7D.png)

### 配置Ingress
服务若想配置应用型负载均衡，该服务的访问方式必须是使用4层负载均衡或使用主机端口通信。应用性负载均衡与内网、公网型负载均衡不互斥。
首先创建需要使用的应用型负载均衡的后端服务，举个例子
后端服务：

- hello 服务：监听80端口，入口文件位于/path_hello/index.html 
- bye 服务：监听80端口，入口文件位于/path_bye/index.html

在Ingress页面创建应用型负载均衡，(已有Ingress可跳过该步骤)
![Alt text](https://mc.qcloudimg.com/static/img/a3b194503971f8bdd1147852496abeba/%7B946ED9B7-80DA-4FCC-80B9-AF02897B1BD1%7D.png)

将自有域名解析到该负载均衡器的VIP，详细见[域名解析帮助文档](https://cloud.tencent.com/document/product/302/3446)。
本示例www.qcloudccs.com解析到示例负载均衡。

设置Ingress转发规则:

![Alt text](https://mc.qcloudimg.com/static/img/cb9e6912f2dccd99e86833dea18d3965/%7B537EFD34-F43E-439E-8D22-BB77BFCB29E5%7D.png)

测试访问：

![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)
