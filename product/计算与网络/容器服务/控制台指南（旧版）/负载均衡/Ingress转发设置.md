>?此文档为原 容器服务控制台 Ingress 使用介绍，TKE 已于2019年6月17日起默认采用兼容原生 kubernetes 特性的新版控制台，请结合 [Ingress 管理](https://cloud.tencent.com/document/product/457/31711) 前往 [新版控制台](https://console.cloud.tencent.com/tke2) 进行使用。

### 使用限制
在集群中不启用访问方式的服务无法使用 Ingress，可使用 Ingress 的服务类型为：
- 公网访问
- VPC 内网访问

Ingress 类型同时还支持负载均衡，负载均衡后端容器节点需打开对应的端口，公网访问和 VPC 内访问的服务默认已开启主机端口。转发配置为后端服务时，无法添加访问方式为集群内访问的服务，如有需要您可更新服务的访问方式。


您可以灵活地使用 Ingress 来设置您的服务的访问方式。服务的访问方式与 Ingress 不冲突，您可以通过 `internet --> Services`，`internet --> Ingress --> Services` 两种方式开始使用，如下图所示：
![Alt text](https://main.qcloudimg.com/raw/67ffea725ff35dbcc218ad123bf73d69.png)

### 域名通配符说明
域名配置规则，需同时满足公网负载均衡域名规则和 kubernetes 的 Ingress 域名规则：
 - 支持正则表达式，长度限制为1 - 80。
 - 非正则的域名支持的字符集：`a - z 0 - 9 . -`。
 - 通配的域名，目前只支持 `*.example.com` 的形式，且单个域名中只支持 `*` 出现一次。

### 配置 Ingress 示例

提前创建需要使用 Ingress 的后端服务：
- hello 服务：监听80端口，入口文件位于 `/path_hello/index.html`。
- bye 服务：监听80端口，入口文件位于 `/path_bye/index.html`。

请按照以下步骤新建 Ingress 并进行配置：
1. 登录容器服务控制台，选择左侧导航栏中的 [Ingress](https://console.cloud.tencent.com/tke/lb)。
2. 在 “Ingress” 管理页面上方，选择地域及需配置 Ingress 的集群，并单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/f99c3bf3c70ef6e7b7737e9572b7a9ae.png)
3. [](id:step3)Ingress 创建成功后，请将自有域名解析到该 Ingress 负载均衡器的 VIP，详情请参见 [快速添加域名解析](https://cloud.tencent.com/document/product/302/3446)。
本示例使用 `www.qcloudccs.com` 解析到示例负载均衡。
4. 在 Ingress 详情页，参考以下信息设置 Ingress 转发规则。如下图所示：
![](https://main.qcloudimg.com/raw/20fe676987e2a6516a896d63d135f2b1.png)
主要参数信息如下：
	- **协议**：支持 HTTP 及 HTTPS 协议，本文以 HTTP 协议为例。
	- **域名**：输入 [步骤3](#step3) 中已解析的域名。
	- **URL路径**：请按需输入，本文以 `/path_hello/index.html` 及 `/path_bye/index.html` 为例。
	- **后端服务**：选择已创建的服务。
	- **服务端口**：输入创建该后端服务时设置的服务端口，可前往服务详情页查看。
5. 设置完成后单击**保存**即可生效。
测试访问结果如下：
![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)
