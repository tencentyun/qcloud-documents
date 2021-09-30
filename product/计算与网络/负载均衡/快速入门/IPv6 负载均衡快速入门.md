腾讯云负载均衡支持 IPv4、IPv6 和 IPv6 NAT64 三个 IP 版本，IPv6 负载均衡支持 TCP/UDP/TCP SSL/HTTP/HTTPS 协议，提供基于域名和 URL 路径的灵活转发能力。本文将引导您如何快速使用 IPv6 负载均衡。
>?IPv6 负载均衡处于内测阶段，如需使用，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)。

## 前提条件
1. 负载均衡只负责转发流量，不具备处理请求的能力。因此，您需要首先搭建处理用户请求的云服务器实例，并完成云服务器的 IPv6 配置。有关如何创建云服务器实例并启用 IPv6，请参见 [快速搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/37946)。
2. 本文以 HTTP 转发为例，云服务器上必须部署相应的 Web 服务器（如 Apache、Nginx、IIS 等），同时 Web 服务使用的端口需要监听 IPv6。

## 使用说明
- 目前仅支持如下地域开通 IPv6 负载均衡：广州、深圳金融、上海、上海金融、南京、北京、成都、香港、新加坡、弗吉尼亚。其中，针对地域为**深圳金融**、**上海金融**的金融行业监管要求定制的合规专区，需提交 [工单申请](https://console.cloud.tencent.com/workorder/category) 使用专区。
- IPv6 负载均衡不支持传统型负载均衡。
- IPv6 负载均衡支持获取客户端 IPv6 源地址。四层 IPv6 负载均衡支持直接获取客户端 IPv6 源地址，七层 IPv6 负载均衡支持通过 HTTP 的 X-Forwarded-For 头域获取客户端 IPv6 源地址。
- 当前 IPv6 负载均衡是纯公网负载均衡，相同 VPC 的客户端无法通过内网访问该 IPv6 负载均衡。
- 互联网 IPv6 网络大环境还处于建设初期，如出现线路访问不通的情况，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 反馈，另外在内测期间，不提供 SLA 保障。

## 步骤1：搭建云服务器并配置 IPv6
1. 进入 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)，登录云服务器完成 IPv6 的基础配置，详细操作请参见 [快速搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/37946)。
2. 在云服务器中，依次执行如下命令，部署并重启 Nginx 服务。
```
yum install nginx
service nginx restart
```
3. <span id="check" />查看部署在云服务器上的 Nginx 服务是否已经监听 IPv6。
 1. 执行如下命令进行查看。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/5bbe14c9e654b5a451828fa1e4157ac8.png)
 2. 执行如下命令，打开 Nginx 配置文件进行查看。
```
vim  /etc/nginx/nginx.conf
```
![](https://main.qcloudimg.com/raw/ff7718571c02a45f02646ab330c21ee2.png)

## 步骤2：创建 IPv6 负载均衡实例
1. 登录腾讯云官网，进入 [负载均衡购买页](https://buy.cloud.tencent.com/lb)。
2. 请正确选择如下参数：
 - 计费模式：仅支持按量计费。
 - 地域：选择目标地域。
 - IP 版本：IPv6。
 - 运营商类型：BGP。
 - 网络：请务必选择已获取 IPv6 CIDR 的私有网络和子网。
3. 在购买页选择各项配置后，单击**立即购买**。
4. 在“CLB 实例列表”页，选择对应的地域即可看到新建的实例。
![](https://main.qcloudimg.com/raw/c3c1422a41460f7a0badb6eef9e751f2.png)

## 步骤3：创建 IPv6 负载均衡监听器
### 配置 HTTP 监听协议和端口
1. 登录[ 负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)。
2. 在“CLB 实例列表”中，找到已创建的负载均衡实例 ，单击实例 ID，进入负载均衡详情页。
3. 在“基本信息”模块，可以单击名称后的修改图标修改实例名称。
4. 在“监听器管理”中的**HTTP/HTTPS 监听器**下，单击**新建**，新建负载均衡监听器。
![](https://main.qcloudimg.com/raw/aa359844bac2ad9b75c99b38e796dc39.png)
5. 在弹出框中，配置以下内容：
 - 名称自定义为“IPv6test”。
 - 监听协议端口为 `HTTP：80`。
6. 单击**提交**，创建负载均衡监听器。

### 配置监听器的转发规则
1. 在“监听器管理”中，选中刚才新建的监听器 IPv6test，单击**＋**，开始添加规则。
2. 在弹出框中，配置域名、URL 路径和均衡方式，单击**下一步**。
  - 域名：您的后端服务所使用的域名，本例使用 ` www.qcloudipv6test.com`。域名支持通配符，详情请参见 [七层转发域名和 URL 规则说明](https://cloud.tencent.com/document/product/214/9032)。
  - URL 路径：您的后端服务的访问路径，本例使用 `/`。
  - 均衡方式选择“加权轮询”。
![](https://main.qcloudimg.com/raw/b3bfa52c7fbc8a7222c372329c004132.png)
3. 配置健康检查：开启健康检查，检查域名使用默认的转发域名和转发路径，单击**下一步**。
![](https://main.qcloudimg.com/raw/37665ef7950ceacf4f2bd0efd91d38d4.png)
4. 会话保持：开启会话保持并配置保持时间，单击**提交**。
![](https://main.qcloudimg.com/raw/9be4156f8d3d7cda26c95f7c97a42191.png)

有关负载均衡监听器的更多内容，请参见 [负载均衡监听器概述](https://cloud.tencent.com/document/product/214/6151)。
>?
>- 一个监听器（即监听协议：端口）可以配置多个域名，一个域名下可以配置多条 URL 路径，选中监听器或域名，单击**＋**即可创建新的规则。
- 会话保持：如果用户关闭会话保持功能，选择轮询的方式进行调度，则请求依次分配到不同后端服务器上；如果用户开启会话保持功能，或关闭会话保持功能但选择 ip_hash 的调度方式，则请求持续分配到同一台后端服务器上去。

### 绑定云服务器
>?绑定云服务器前，请确定该云服务器已获取 IPv6 地址。
>
1. 在“监听器管理”页面，选中并展开刚才创建的监听器，选中域名、选中 URL 路径，在右侧即可看到该 URL 路径绑定的云服务器 IPv6 信息，单击**绑定**。
2. 在弹框中，选择云服务器，并设置云服务器的 Nginx 服务默认端口为80，设置权重（默认值10），单击**确定**。
![](https://main.qcloudimg.com/raw/475b9360540372bda5ad1987bf7aa6f5.png)
3. 成功绑定云服务器后：
 - 请确认端口状态是否为“健康”，如果为“健康”，请进行 [步骤4：测试 IPv6 负载均衡](#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E6.B5.8B.E8.AF.95-ipv6-.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1)。
 ![](https://main.qcloudimg.com/raw/3903080da94505b1f2cff562d0ccc503.png)
 - 如果端口状态为“异常”，请确定监听器是否绑定了正确的云服务器的 Nginx 服务端口，同时登录云服务器检查端口已经正常监听 IPv6，可参见 [步骤1中的第3步](#check) 进行查看。 
![](https://main.qcloudimg.com/raw/df6d8776624118f278db0b1b05eb6022.png)

## 步骤4：测试 IPv6 负载均衡
配置完成 IPv6 负载均衡后，可以验证该架构是否生效，即验证通过一个 CLB 实例下不同的域名 + URL 访问不同的后端云服务器，也即验证内容路由（content-based routing） 的功能是否可用。

使用具有 IPv6 公网能力的客户端，访问域名或者负载均衡的 IPv6 地址，如果能够正常访问云服务器的 Web 服务，则表明 IPv6 负载均衡工作正常，示例步骤如下：
1. 打开 [腾讯云域名注册页面](https://dnspod.cloud.tencent.com/) 进行域名查询和注册。本例以`qcloudipv6test.com` 为例，详情请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 登录 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns)，单击您所购买的**域名**，在“记录管理”页面单击**添加记录**，为域名添加 AAAA 记录，输入如下内容并保存：
   - 主机记录：即域名前缀，本例设为`www`。
   - 记录类型：`AAAA记录`。
   - 线路类型：默认。
   - 记录值：填写负载均衡的 IPv6 地址。
   - TTL：设置为默认值“600s”。
3. 添加域名解析后，通过 Ping 域名进行验证，如下图：
![](https://main.qcloudimg.com/raw/9b0fdfd7b14fa59b8bd6447a9a953d0f.png)
4. 再通过浏览器访问域名来验证，如下图：
![](https://main.qcloudimg.com/raw/77a28d46b830e44db2856b029f5f8697.png)
