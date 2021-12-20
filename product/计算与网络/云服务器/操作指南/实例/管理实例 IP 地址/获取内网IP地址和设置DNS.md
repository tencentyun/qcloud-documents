## 操作场景
本文档介绍获取实例的内网 IP 地址和设置内网 DNS 的相关操作。

## 操作步骤
### 获取实例的内网 IP 地址
<dx-tabs>
::: 使用控制台获取
1. 登录 [云服务器控制台]( https://console.cloud.tencent.com/cvm/)。
2. 在实例的管理页面，选择您需要查看内网 IP 的实例，将鼠标移动到 “主IP地址” 列，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin: -3px 0px;"> 即可复制内网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/b25c842ea6c3e14c391a786ad0e336ac.png)
:::
::: 使用\sAPI\s获取
请参考 [DescribeInstances 接口](https://cloud.tencent.com/document/product/213/15728)。
:::
::: 使用实例元数据获取
1. 登录云服务器。
2. 使用 cURL 工具或者 HTTP 的 GET 请求访问实例元数据。
<dx-alert infotype="explain" title="">
以下操作以 cURL 工具为例。
</dx-alert>
执行以下命令，获取内网 IP。
```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
``` 返回的信息即为内网 IP 地址，如下图所示：
![](//mc.qcloudimg.com/static/img/14a13eccebc7eee6f83bc026adb30902/image.png)
更多实例元数据的信息，请参阅 [查看实例元数据](https://cloud.tencent.com/document/product/213/4934)。
:::
</dx-tabs>

### 设置内网 DNS 
当网络解析出现错误时，您可以根据云服务器操作系统的类型，进行手动设置内网 DNS。
<dx-tabs>
::: Linux\s系统
1. 登录 Linux 云服务器。
2. 执行以下命令，打开 `/etc/resolv.conf` 文件。
```
vi /etc/resolv.conf
```
3. 按 **i** 切换至编辑模式，并根据 [内网 DNS](https://cloud.tencent.com/document/product/213/5225#.E5.86.85.E7.BD.91-dns) 列表中对应的不同地域，修改 DNS IP。
例如，将内网 DNS IP 修改为北京地域的内网 DNS 服务器。
```
nameserver 10.53.216.182
nameserver 10.53.216.198
options timeout:1 rotate
```
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
:::
::: Windows\s系统
1. 登录 Windows 云服务器。
2. 在操作系统界面，打开**控制面板** > **网络和共享中心** > **更改适配器设备**。
3. 右键单击**以太网**，选择**属性**，打开 “以太网 属性” 窗口。
4. 在 “以太网 属性” 窗口，双击打开 **Internet 协议版本 4 (TCP/IPv4)**。如下图所示：
![](https://main.qcloudimg.com/raw/023e97de00a08b44a19c510798d2d1c6.png)
5. 选择**使用下面的 DNS 服务器地址**，根据 [内网 DNS](https://cloud.tencent.com/document/product/213/5225#.E5.86.85.E7.BD.91-dns) 列表中对应的不同地域，修改 DNS IP。
![](https://main.qcloudimg.com/raw/8921862c0b6ea5e407de4796f2806c8e.png)
6. 单击**确定**。
:::
</dx-tabs>
