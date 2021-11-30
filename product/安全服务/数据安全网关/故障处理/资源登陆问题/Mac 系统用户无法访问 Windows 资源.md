## 现象描述
Mac 系统用户安装完 BHLoader 插件后访问 Windows 资源，提示未找到 Microsoft Remote Desktop，无法访问资源。如下图所示：

![](https://main.qcloudimg.com/raw/c181cde5a2b3e1d6c51f7c0fbf1044a4.png)

## 可能原因
Mac 系统未内置 RDP 的远程工具，需要用户自己安装工具并进行设置。


## 解决思路
在 Mac 系统中安装 RDP 的远程工具。

## 处理步骤
1.下载并安装：[Microsoft Remote Desktop](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac)，推荐版本 10.5.1(1852)，使用默认安装即可。
2. 访问 Windows 资源，根据提示设置工具调取路径。
![](https://main.qcloudimg.com/raw/169af49492251f7fc205ba1272766a0e.png)
3. 设置完成后，单击【访问】，触发拉起 BHLoader 插件。。
![](https://main.qcloudimg.com/raw/fb91431095b8536ac6c57ff1cd255a99.png)
4. 单击【确认】，调用 MRD 客户端。
![](https://main.qcloudimg.com/raw/044e23057440f80a7ac25e3750957e21.png)
5. 单击【continue】，完成访问资源调用工具验证，开始资源访问。
![](https://main.qcloudimg.com/raw/d18cc7c9b505011c7d7cc40d8a0dd68b.png)
