本教程将帮助您在 Windows 操作系统环境下配置 IPv6 地址。

>?
>- 默认云服务器的 IPv6 地址仅具有私网通信能力，若您想要通过该 IPv6 地址访问公网或被公网访问，则需通过弹性公网 IPv6 为该 IPv6 地址开通公网能力，操作详情请参见 [为云服务器的 IPv6 地址开通公网](https://cloud.tencent.com/document/product/1142/47665#step4)。
>- 若部分机型可以自动获取到地址，为避免主机重启后获取地址失败，也需要按照如下方式手动配置。
>


IPv6 配置包括 IPv6 地址和 IPv6 默认路由两个部分，Windows 操作系统镜像暂不支持通过 DHCP 动态获取 IPv6 地址，需要手工配置 IPv6 地址和 IPv6 默认路由：
<table>
<tr>
<th>镜像类型</th>
<th>配置方式</th>
</tr>
<tr>
<td>
<ul>
<li>Windows Server 2022 数据中心版 64位 中文版</li>
<li>Windows Server 2019 数据中心版 64位 中文版</li>
<li>Windows Server 2016 数据中心版 64位 中文版</li>
<li>Windows Server 2012 R2 数据中心版 64位 中文版</li>
<li>Windows Server 2016 数据中心版 64位 英文版</li>
<li>Windows Server 2019 数据中心版 64位 英文版</li>
<li>Windows Server 2022 数据中心版 64位 英文版</li>
</ul>
</td>
<td>配置 IPv6 地址和 IPv6 默认路由</td>
</tr>

</table>



### 配置 IPv6 地址和 IPv6 默认路由
如下操作以 Windows Server 2012 R2 数据中心版 64位 中文版为例：
1. 登录云服务器实例，进入操作系统的**控制面板** > **网络和 Internet** > **网络和共享中心**，单击命名为**以太网**的网卡进行编辑。
![](https://qcloudimg.tencent-cloud.cn/raw/abf6c279b38ba1f1d8e10dac3aafaa6a.png)
2. 在**以太网状态**弹窗中，单击左下角**属性**。
3. 在**以太网属性**弹窗中，选中 **Internet 协议版本6（TCP/IPv6）**并单击**属性**。
![](https://qcloudimg.tencent-cloud.cn/raw/41deba067d59bc616bdab50f3c38afff.png)
4. 在 **Internet 协议版本6（TCP/IPv6）属性**弹窗中，手工输入云服务器获取到的 IPv6 地址（请参见 [搭建 IPv6 私有网络：步骤三](https://cloud.tencent.com/document/product/215/47557#step3)）并设置 DNS（推荐使用240c::6666），单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/c6faac59d816c26654daa8f8200cea95.png)
5. 在操作系统界面，选择左下角的<img src="https://qcloudimg.tencent-cloud.cn/raw/c88d57abf262f95563ba3d007f809200.png" width="3%">，单击<img src="https://qcloudimg.tencent-cloud.cn/raw/d1cf2d7e2fb1c37d0327a016c5bee66e.png" width="4%">，打开 “Windows PowerShell” 窗口，依次执行如下命令配置默认路由以及查看 IPv6 地址。
```
netsh interface ipv6 add route ::/0 "以太网"     #如果无法输入中文，建议修改为 “Ethernet”
ipconfig
```
![](https://qcloudimg.tencent-cloud.cn/raw/63e8fa5b878c569ff8a536121d6ce716.png)
