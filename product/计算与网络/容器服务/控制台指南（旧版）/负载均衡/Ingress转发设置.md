### 使用限制
在集群中不启用访问方式的服务无法使用 Ingress，可使用 Ingress 的服务类型为：
- 公网访问
- VPC 内网访问

Ingress 类型同时还支持负载均衡，负载均衡后端容器节点需打开对应的端口，公网访问和 VPC 内访问的服务默认已开启主机端口。转发配置为后端服务时，无法添加访问方式为集群内访问的服务，如有需要您可更新服务的访问方式。


您可以灵活地使用 Ingress 来设置您的服务的访问方式。服务的访问方式与 Ingress 不冲突，您可以通过 `internet --> Services`，`internet --> Ingress --> Services` 两种方式开始使用，如下图所示：
![Alt text](https://main.qcloudimg.com/raw/67ffea725ff35dbcc218ad123bf73d69.png)

### 域名通配符说明
域名配置规则，需同时满足公网负载均衡域名规则和 kubernetes 的 Ingress 域名规则：
1. 支持正则表达式，长度限制为1 - 80。
2. 非正则的域名支持的字符集：`a - z 0 - 9 . -`。

通配的域名，目前只支持 `*.example.com` 的形式，且单个域名中只支持 `*` 出现一次。

### 配置 Ingress 示例

提前创建需要使用 Ingress 的后端服务：
- hello 服务：监听80端口，入口文件位于 `/path_hello/index.html`。
- bye 服务：监听80端口，入口文件位于 `/path_bye/index.html`。

请按照以下步骤新建 Ingress 并进行配置：
1. 登录容器服务控制台，选择左侧导航栏中的 [Ingress](https://console.cloud.tencent.com/tke/lb)。
2. 在 “Ingress” 管理页面上方，选择地域及需配置 Ingress 的集群，并单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/d8bee786541a87e18dcc594e2c1b4116.png)
3. 将自有域名解析到该负载均衡器的 VIP，详情请参见 [快速添加域名解析](https://cloud.tencent.com/document/product/302/3446)。
本示例使用 `www.qcloudccs.com` 解析到示例负载均衡。
4. 在 Ingress 详情页，设置 Ingress 转发规则。如下图所示：
![](https://main.qcloudimg.com/raw/3aaaa2dc5bc361387af8f5e17ebe4f96.png)
测试访问结果如下：
![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)
