### 使用Ingress前置条件
使用Ingress的服务需要是以下三种类型的服务

- 公网访问
- 仅在集群内访问
- VPC内网访问

Ingress类型目前支持应用型LB, 应用型LB后端容器节点需打开对应的端口，公网访问和VPC内访问默认已开启主机端口， 仅在集群内访问的服务默认不开启主机端口，但如果设置为ingress后端服务将会自动开启主机端口，不启用访问方式的服务不支持设置Ingress,

您可以灵活的使用Ingress来设置您的服务的访问方式。服务的访问方式与Ingress不冲突，您可以通过使用两种方式，如下图：
![Alt text][roledemo]

### 域名通配符说明
域名配置规则, 需同时满足公网应用型负载均衡域名规则和kubernetes的ingress域名规则：
1. 支持正则表达式，长度限制为1-80。
2. 非正则的域名支持的字符集：a-z 0-9 . -

通配的域名，目前只支持`\*.example.com` 的形式，且单个域名中只支持* 出现一次。

### 配置Ingress 示例

提前创建需要使用Ingress的后端服务:

- hello 服务：监听80端口，入口文件位于/path_hello/index.html
- bye 服务：监听80端口，入口文件位于/path_bye/index.html

在Ingress页面创建Ingress(已有Ingress可跳过该步骤)
![Alt text][create]

将自有域名解析到该负载均衡器的VIP，详细见[域名解析帮助文档](https://cloud.tencent.com/document/product/302/3446)。
本示例www.qcloudccs.com解析到示例负载均衡。

设置Ingress转发规则:

![Alt text][set]

测试访问：

![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)




[roledemo]:https://mc.qcloudimg.com/static/img/fa7048f3ab7dc6aad9aa554b39b158a6/%7B7487A7E3-8BDD-44CB-81F9-38631784E0F0%7D.png
[create]:https://mc.qcloudimg.com/static/img/6dc5400d69b00794787bcfda3dd231bf/%7BE8312885-54E0-4D25-AFCA-59B6E2CA74C2%7D.png
[set]:https://mc.qcloudimg.com/static/img/b5cec3c1703b0a69bad15b7477d10017/%7B4833E8A7-E8E7-4FA9-81D3-50A2291F4E42%7D.png
