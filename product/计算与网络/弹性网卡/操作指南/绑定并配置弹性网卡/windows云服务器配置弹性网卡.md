>? 如下步骤以 Windows 2012 为例。
>

## 操作步骤
### Windows 操作系统设置了 DHCP
如果 Windows 操作系统设置了 DHCP，则无需配置，即能支持自动识别辅助网卡以及网卡上的 IP。查看操作如下：
1. 登录云服务器，进入操作系统的**控制面板** > **网络和 Internet** > **网络和共享中心**，可查看到已自动识别辅助网卡。
2. 单击命名为“以太网 2”的辅助网卡，查看信息。
![](https://main.qcloudimg.com/raw/b8498adcc2896f436a1bfdc96d11090d.png)
3. 在“以太网 2 状态”弹窗中，单击**属性**。
4. 在“以太网 2 属性”弹窗中，双击**Internet 协议版本4（TCP/IPv4）**。
5. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，可查看到已选择**自动获取 IP 地址**，无需手动填写。
![](https://main.qcloudimg.com/raw/93256b91fa4124b39c9e67a7ca06ead4.png)
6. 返回“以太网 2 状态”弹窗中，单击**详细信息**，即可查看已启用 DHCP，自动识别 IP。
![](https://main.qcloudimg.com/raw/2b8c5273070b0880a2e0b8482a572ce6.png)


### Windows 操作系统未设置 DHCP
如果 Windows 操作系统没有设置 DHCP，则需要在操作系统内，把内网 IP 配上。操作步骤如下：
1. 登录 [弹性网卡控制台](https://console.cloud.tencent.com/vpc/eni?rid=1)，把弹性网卡 [绑定云服务器](https://cloud.tencent.com/document/product/576/18535#.E7.BB.91.E5.AE.9A.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8)。
2. 登录云服务器，进入操作系统的**控制面板** > **网络和 Internet** > **网络和共享中心**。
3. 单击命名为“以太网 2”的辅助网卡，进行编辑。
![](https://main.qcloudimg.com/raw/b8498adcc2896f436a1bfdc96d11090d.png)
4. 在“以太网 2 状态”弹窗中，单击**属性**。
5. 在“以太网 2 属性”弹窗中，双击 **Internet 协议版本4（TCP/IPv4）**。
6. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，手动填写 IP 信息（按实际填写），完成后单击**确定**。
![](https://main.qcloudimg.com/raw/71eefd1aa5299036a4789792b3bb9602.png)
7. 在“以太网 2 属性”弹窗中，单击**确定**即可完成配置。
8. 在“以太网 2 状态”弹窗中，单击**详细信息**，可查看未启用 DHCP，手动填写的 IP 信息。
![](https://main.qcloudimg.com/raw/3fe09a17eca280416d8ad64fb52a1675.png)
9. 用同一个子网下的 CVM，来 Ping 内网地址，能 Ping 通即说明成功。如无其他 CVM，可以给辅助网卡的内网 IP 绑定公网 IP，Ping 该公网 IP 来验证。
