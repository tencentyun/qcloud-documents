## 简介

Discuz! 论坛可以通过配置远程附件功能将论坛的附件保存在腾讯云 COS 上，将论坛附件保存在 COS 上有以下好处：

- 附件将拥有更高的可靠性。
- 您的服务器无需为论坛附件准备额外的存储空间。
- 论坛用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。
- 可配合腾讯云 CDN 进一步提升论坛用户查看图片附件的速度。

## 准备工作

1. 搭建 Discuz! 论坛。
	- 您可在 [Discuz! 官方发布](https://www.discuz.net/forum-10-1.html) 页面下载 Discuz! 论坛的最新版并查看安装说明。
	- 您也可以在 [腾讯云市场](https://market.cloud.tencent.com/) 中搜索购买已经预装 Discuz! 论坛程序的 CVM 镜像。
2. 创建一个**公有读私有写**的存储桶，存储桶的地域建议与运行 Discuz! 论坛的 CVM 的地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
3. 在存储桶列表中找到刚刚创建的存储桶，并单击【配置管理】。
![](https://main.qcloudimg.com/raw/6e011a00b4646f7d465056e9c88aa78c.png)
4. 在左侧导航栏中，选择【概览】页签，查看**访问域名**并记录。
![](https://main.qcloudimg.com/raw/e84d246bb9c44ac9647d4d0abae565b6.png)
5. 在运行 Discuz! 论坛的 CVM 上，部署 COS FTP Server 工具，部署步骤可参见 [FTP Server 工具](https://cloud.tencent.com/document/product/436/7214)。
	- 在配置 FTP Server 时，FTP Server 配置中的 masquerade_address 设置为 127.0.0.1 以保证该 FTP 服务仅能被本机访问。
	- 您也可以使用独立的 CVM 单独部署 FTP Server，此时配置中的 masquerade_address 参数，您可依据实际情况配置为内网 IP 或外网 IP。

## 配置远程附件

1. 使用管理员账号登录 Discuz! 论坛并进入**管理中心**页面。
2. 依次进入【全局】 > 【上传设置】 > 【远程附件】。
3. 设置远程附件选项，配置说明见下表。

| 配置项             | 配置值                                                       |
| ------------------ | ------------------------------------------------------------ |
| 启用远程附件       | 是                                                           |
| 启用 SSL 连接      | 否                                                           |
| FTP 服务器地址     | COS FTP Server 工具的地址，通常为 127.0.0.1，如果您使用独立的 CVM 单独部署 FTP Server，此处配置为实际的内网 IP 或外网 IP |
| FTP 服务器端口     | 默认为 2121                                                  |
| FTP 账号           | COS FTP Server 工具中配置的 FTP 账号                         |
| FTP 密码           | COS FTP Server 工具中配置的 FTP 密码                         |
| 被动模式(pasv)连接 | 是                                                           |
| 远程附件目录       | 保持默认的半角句号(.)                                        |
| 远程访问 URL       | 存储桶的**访问域名**，例如`https://examplebucket-1250000000.cos.ap-beijing.myqcloud.com` |
| FTP 传输超时时间   | 保持默认的0                                                  |

<img src="https://main.qcloudimg.com/raw/0c49e755be38e71393f71d51974e06be.jpg" width="90%"></img>
<img src="https://main.qcloudimg.com/raw/e8deab38f87844e947a2cc8fd0a74986.jpg" width="90%"></img>
4. 单击【测试远程附件】，如果提示“远程附件设置一切正常”，说明设置成功。
<img src="https://main.qcloudimg.com/raw/38c8232f60577691da78d93925e9b0fa.png" width="90%"></img>
5. 保存配置。
6. 发帖测试。
<img src="https://main.qcloudimg.com/raw/5d984846af7d99780b21d4f1b6ca4045.png" width="90%" ></img>
7. 单击附件图片，单击右上角的**在新窗口打开**图标。
<img src="https://main.qcloudimg.com/raw/25175e71eac8738097f5c66c26489d7e.png" width="90%"></img>
8. 查看附件图片的 URL，确认附件图片的 URL 指向腾讯云 COS。
<img src="https://main.qcloudimg.com/raw/28803b68fd3cc513c5a26d8a160579fe.png" width="90%" ></img>


## 使用 CDN 加速访问

1. 您如需为已保存了 Discuz! 论坛附件的存储桶配置 CDN 加速，可参见 [CDN 加速配置](https://cloud.tencent.com/document/product/436/18670) 文档。
2. 在 Discuz! 论坛的**远程附件**设置中将**远程访问 URL**修改为默认 CDN 加速域名或自定义加速域名即可。

