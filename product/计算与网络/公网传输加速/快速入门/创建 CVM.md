下例中我们以快速配置为例来演示如何快速配置相关选项，实际购买时用户也可以选择自定义配置来选择更多的配置项。
### 第 1 步：登录控制台
登录 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)。如果没有帐号，请参考 [帐号注册教程](https://cloud.tencent.com/document/product/378/8415)。
![登录](//mc.qcloudimg.com/static/img/ff6e234a3c1b419cc8ea2ba272c59101/image.png)

### 第 2 步：新建云主机（CVM）
进入云主机的界面，单击【新建】创建和配置云主机。
![新建云主机](//mc.qcloudimg.com/static/img/f51676036b7681c3c938014c36f7d40a/image.png)

### 第 3 步：配置云主机的相关选项
选择地域和机型：
- [计费模式](https://cloud.tencent.com/document/product/213/2180?_ga=1.33985321.903886351.1504603839)：包年包月和按量计费。
- 地域：选择靠近您的客户的地域可以降低访问延迟，此处以广州为例。
- 可用区：同一地域下，电力和网络互相独立的物理区域（一般是一个物理机房）。单可用区故障不会影响其他可用区云服务的正常运行。
- 系列：系列 2 较系列 1 进行了硬件升级，采用 Intel Broadwell CPU、DDR4 内存，全面搭配网络增强，包转发能力最高可达 30 w，整数和浮点运算的性能翻倍，整体计算能力更强。系列 1 与系列 2 之间不能互相升降配。
- 机型：提供从基础到专业的四种“CPU+内存”的搭配供您选择。
![选择地域和机型](//mc.qcloudimg.com/static/img/04d83499835277ae5c0c956cb888819b/image.png)
选择镜像：
提供四种常见的操作系统和集成了特定软件的操作系统供您选择。
![选择镜像](//mc.qcloudimg.com/static/img/4d0ede17f103700962a68fbf558735c0/image.png)
选择存储与网络：
- [系统盘](https://cloud.tencent.com/document/product/213/4952?_ga=1.26270517.903886351.1504603839)：有本地硬盘和云硬盘供选择。
- 数据盘：根据需要分配合适的容量。
- 网络类型：基础网络 IP 地址由腾讯云默认分配，配置简便，使用方便，适合对操作易用性要求比较高，需要快速使用 CVM 的场景。私有网络是指逻辑隔离的网络空间，您可以自定义网段划分和 IP 地址、路由，支持 VPN 连接/专线接入等。适合于有一定网络自定义配置需求的场景。基础网络与私有网络不能互通，购买后不能更换网络类型。
- [带宽计费模式：](https://cloud.tencent.com/document/product/213/10578)包括按带宽计费和按使用流量计费。
- 带宽：根据业务需求分配合适的带宽。默认勾选分配免费公网 IP。
- 服务器数量：默认 1 台。
- 购买时长：默认 1 个月。
- 自动续费：用户根据需求选择。
![选择存储与网络](//mc.qcloudimg.com/static/img/d76e5cb52eb26e9c80be548615253ef5/image.png)
设置信息：
设置云主机所属项目、主机名、登录方式和 [安全组](https://cloud.tencent.com/document/product/213/2502?_ga=1.155629235.903886351.1504603839#1.-.E4.B8.BA.E4.BB.80.E4.B9.88.E5.9C.A8.E8.B4.AD.E4.B9.B0-.E4.BA.91.E4.B8.BB.E6.9C.BA-.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.97.B6.E5.80.99.E9.9C.80.E8.A6.81.E9.80.89.E6.8B.A9.E5.AE.89.E5.85.A8.E7.BB.84.EF.BC.9F2) 等信息。
![设置信息](//mc.qcloudimg.com/static/img/1a99945636e40c391491e08f9bdf4866/image.png)
### 第 4 步：确认配置详情并支付
确认配置详情后，选择【立即购买】，支付完成后，系统大概需要几分钟时间来为您创建 CVM 服务器。
![支付完成](//mc.qcloudimg.com/static/img/296c50a25f3eed1f8dea7f5b997ab444/image.png)
