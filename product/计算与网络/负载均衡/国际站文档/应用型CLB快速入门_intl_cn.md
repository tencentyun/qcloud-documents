腾讯云应用型负载均衡是增强型负载均衡，相比于传统型负载均衡，应用型负载均衡支持更多的功能和更强的性能。除去传统型的基本功能外，应用型负载均衡覆支持用户配置基于域名和 URL 的转发规则，支持重定向（如将 HTTP 请求重定向为 HTTPS 请求），支持 SNI 绑定多个证书等等。本文档将指引您如何初步使用腾讯云应用型负载均衡。

## 1. 购买云服务器，搭建后端服务
负载均衡只负责转发流量，不具备处理请求的能力。因此，您需要有处理用户请求的云服务器实例，请先购买云服务器，并搭建后端服务。
### 1.1 购买云服务器
在云服务器的 [选购页面](https://buy.cloud.tencent.com/cvm) 选择适合自己的机型和镜像等，设置主机的初始密码，配置安全组（此处为了测试方便，可以先选择放通全部端口，后续再做限制）。另外，在购买云服务器时注意开通公网流量，否则会导致后续关联 CLB 后访问不通。
![](https://main.qcloudimg.com/raw/8edc105a8037a0bedcb2538828430d81.png)

本例中已经在广州地域下创建了云服务器实例 `rs-1` 和 `rs-2`，详情请参考 [购买并启动云服务器实例](https://cloud.tencent.com/document/product/213/4855)。
- **主机信息**
 - 地域：广州
 - 可用区：广州三区一台，广州四区一台
 - 主机计费模式：按量计费
 - 网络计费模式：按带宽计费
 - 所属网络：私有网络（默认的 Default-VPC）
- **机器配置**
 - 实例类型：S4.SMALL2（标准型S4）
 - 操作系统	CentOS 7.5 64位
 - CPU：1核
 - 内存：2GB
 - 系统盘：50GB(普通云硬盘)
 - 数据盘：500GB(高性能云硬盘)
 - 公网带宽：1Mbps（必选）

 > 注：云服务器上必须购买公网带宽，因为当前的带宽属性在 CVM 上，而非 CLB 上。

### 1.2 搭建后端服务
本文以 HTTP 转发为例，云服务器上必须部署相应的 Web 服务器，如 Apache、Nginx、IIS等。为了验证结果，示例在 `rs-1` 上部署了 Nginx 并返回一个带有 “This is rs-1! URL is index.html” 的 HTML，在 `rs-2` 上部署了 Nginx 并返回一个带有 “This is rs-2! URL is image/index.html” 的 HTML。部署 Nginx 请参考[Linux(CentOS) 下部署 nginx](待发布)。有关如何在云服务器上部署服务的更多内容，请参考[Linux(CentOS) 下部署 Java Web](待发布)及[Windows 下安装配置 PHP](https://cloud.tencent.com/document/product/213/10182)。

### 1.3 验证服务
访问云服务器的公网 IP + 路径，如果可以显示出您部署好的页面的话，则证明服务部署成功。

## 2. 购买负载均衡实例
1. 登录腾讯云 [负载均衡服务购买页](https://buy.cloud.tencent.com/lb)。
2. 本例地域选择与云服务器相同的【广州】，实例类型选择【应用型】，网络属性选择【公网】，网络选择【Default-VPC(默认)】，实例名称填写【clb-test】。
3. 单击【立即购买】按钮，完成付款。
有关负载均衡实例的更多内容，请参考 [购买属性指引](待发布) 。
![](https://main.qcloudimg.com/raw/ce5c1f23b671760a8e14f06f28040da4.png)
4. 在【LB 实例列表】页，选择对应的地域即可看到新建的实例。
![](https://main.qcloudimg.com/raw/36e75ded1d8a0e93bd25b9c24ee850c5.png)

## 3. 创建负载均衡监听器
负载均衡监听器通过指定协议及端口来负责实际转发。本文以负载均衡转发客户端的 HTTP 请求配置为例。
### 3.1 配置 HTTP 监听协议和端口
1. 登录[腾讯云控制台](https://console.cloud.tencent.com/)，单击【云产品】-【网络】-【负载均衡】进入负载均衡控制台。
2. 在【LB 实例列表】中找到已创建的应用型的负载均衡实例 `clb-test`，单击实例 ID 进入负载均衡详情页。
3. 在【基本信息】部分，您可以单击名称后的小图标修改实例名称。
4. 在【监听器管理】中的【HTTP/HTTPS监听器】下，单击【新建】按钮新建负载均衡监听器。
![](https://main.qcloudimg.com/raw/08476cf9f61eec6dc1baba400821e6ec.png)
5. 在弹出框中配置以下内容：
  - 名称自定义为“Listener1”；
  - 监听协议端口为 `HTTP：80`；
  - 单击【提交】按钮创建负载均衡监听器。

### 3.2 配置监听器的转发规则
1. 在【监听器管理】中，选中刚才新建的监听器 Listener1，点击“＋”号，开始添加规则。
![](https://main.qcloudimg.com/raw/ff0a2b40bf4fcd7e361966ee6d4a21d9.png)
2. 在弹出框中配置域名、URL路径和均衡方式
  - 域名：您的后端服务所使用的域名，本例使用 `www.qcloudtest.com`。域名支持通配符，详见[配置说明](https://cloud.tencent.com/document/product/214/9032)；
  - URL 路径：您的后端服务的访问路径，本例使用 `/image/`;
  - 均衡方式选择 `按权重轮询`；
![](https://main.qcloudimg.com/raw/1dc1ab66d04f361dd138e24eb7509d50.png)
3. 配置健康检查：开启健康检查，检查域名使用默认的转发域名和转发路径；
![](https://main.qcloudimg.com/raw/305f3f9de7e4641f0cd8f5944ff57ac8.png)
4. 会话保持：不勾选会话保持。
5. 点击【完成】，完成监听器转发规则的配置。
![](https://main.qcloudimg.com/raw/5de81a61e3a83eb760339ed0124f7d66.png)

有关负载均衡监听器的更多内容，请参考 [负载均衡监听器概述](https://cloud.tencent.com/document/product/214/6151)。
> 注：一个监听器（即监听协议：端口）可以配置多个域名，一个域名下可以配置多条 URL 路径，选中监听器或域名，点击“＋”号即可创建新的规则。
> 会话保持：如果用户关闭会话保持功能，选择轮询的方式进行调度，则请求依次分配到不同后端服务器上；如果用户开启会话保持功能，或关闭会话保持功能但选择 ip_hash 的调度方式，则请求持续分配到同一台后端服务器上去。

### 3.3 绑定云服务器
1. 在【监听器管理】页面，选中并展开刚才创建的监听器 Listener1，选中域名、选中 URL 路径，在屏幕右侧即可看到该 URL 路径绑定的云服务器信息，单击【绑定】按钮。
![](https://main.qcloudimg.com/raw/fa041a80ebf420e75f77f4ab5fbddf24.png)
2. 在弹出框中选择与 CLB 同地域下的云服务器实例 `rs-1` 和 `rs-2`，设置云服务器端口均为 `80`，云服务器权重均为默认值 `10`。
![](https://main.qcloudimg.com/raw/8729820affbf015a4256f8716ae888de.png)
3. 单击【确定】按钮完成绑定。
4. 展开监听器到 URL 路径维度，可以查看绑定的云服务器和其健康检查状态，当状态为“健康”时表示云服务器可以正常处理负载均衡转发的请求。
![](https://main.qcloudimg.com/raw/b66d71a83253dd0729092a0489c33d1e.png)
> 注：一条转发规则（监听协议 + 端口 + 域名 + URL 路径）可以绑定同一台云服务器的多个端口。如用户在 `rs-1` 的 `80` 和 `81` 端口部署了一样的服务，则 CLB 支持示例中的转发规则同时绑定 `rs-1` 的 `80` 和 `81` 端口，两个端口都会接收到 CLB 转发的请求。

## 4. 验证负载均衡服务
配置完成负载均衡后，我们可以验证一下该架构是否生效，即验证通过一个 CLB 实例下不同的 **域名+URL** 访问不同的后端云服务器，也即验证**“内容路由（content-based routing）”** 的功能。
### 4.1 方法一：配置 hosts 将域名指向 CLB
在 Windows 系统中，进入 `C:\Windows\System32\drivers\etc` 目录，修改 hosts 文件，把域名映射到 CLB 实例的 VIP 上。
![](https://main.qcloudimg.com/raw/2a5cd0cc116ce53fed3ac98d4017a59f.png)

为了验证 hosts 是否配置成功，可以在本机开 cmd 用 ping 命令探测一下该域名是否成功绑定了 VIP，如果发现有数据包，则证明绑定成功。
![](https://main.qcloudimg.com/raw/cbf250997c885695d3ff8525de816be5.png)

接下来在浏览器中输入访问路径 `http://www.qcloudtest.com/image/`，测试负载均衡服务。如下表示本次请求被 CLB 转发到了 rs-1 这台 CVM 上，CVM 正常处理请求并返回。
![](https://main.qcloudimg.com/raw/97b1f947d2b9dd90e99efb82a95722b9.png)

此监听器的轮询算法是“按权重轮询”且两台 CVM 的权重都是 10，刷新浏览器，再次发送请求，可以看到本次请求被 CLB 转发到了 rs-2 这台 CVM 上。
![](https://main.qcloudimg.com/raw/7c467013c2635338527dc0eb70fc4635.png)
> 注：`image/` 后面的 `/` 很重要，因为这个代表了 image 是以个默认的目录，而不是名为 image 的文件。

### 4.2 方法二：配置云解析将域名指向 CLB
1. 打开 [腾讯云域名注册页面](https://dnspod.cloud.tencent.com) 进行域名查询和注册。本例以 qcloudtest.com 为例，详情请参考[域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 登录[腾讯云控制台](https://console.cloud.tencent.com/)，单击【云产品】-【域名与网站】-【云解析】。
3. 单击您所购买的【域名】，在【域名解析管理】页面单击【添加记录】按钮，为域名添加 A 记录，输入以下内容：
  - 记录类型：`A记录`；
  - 主机记录：即域名前缀。本例以解析所有前缀为例，设为 `*.qcloudtest.com`；
  - 线路类型：默认；
  - 记录值：点击【关联云资源】，在弹出框勾选刚刚创建的 `clb-test`；
  - TTL：设置为默认值 `600s`；
  - 添加完毕后，单击【保存】。

云解析需要一段时间将该记录在 Internet 上传播。为测试域名是否解析正常，可以在添加完解析记录一段时间后，直接访问绑定后的CNAME域名（如本例中的www.qcloudtest.com ）来验证负载均衡。

## 5. 配置重定向功能（可选）
重定向配置分为手动重定向和自动重定向两种。
- 自动重定向（强制 HTTPS）：PC、手机浏览器等以 HTTP 请求访问 Web服务，希望 CLB 代理后，返回 HTTPS 的 respond。默认强制浏览器以 HTTPS 访问网页。
- 自定义重定向：当出现 Web 业务需要临时下线（如电商售罄、页面维护，更新升级时）会需要重定向能力。如果不做重定向，用户的收藏和搜索引擎数据库中的旧地址只能让访客得到一个404/503错误信息页面降低了用户体验度，导致访问流量白白丧失。不仅如此，之前该页面积累的搜索引擎评分也浪费了。
详情参见 [重定向配置](https://cloud.tencent.com/document/product/214/8839)。
