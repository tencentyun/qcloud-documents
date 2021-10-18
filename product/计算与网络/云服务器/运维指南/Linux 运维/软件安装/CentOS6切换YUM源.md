## 操作背景
CentOS 6操作系统版本生命周期（EOL）于2020年11月30日结束，Linux 社区不再维护该操作系统版本。按照社区规则，CentOS 6的源地址 `http://mirror.centos.org/centos-6/` 内容已移除，且目前第三方的镜像站中均已移除 CentOS 6的源。腾讯云的源 `http://mirrors.cloud.tencent.com/和http://mirrors.tencentyun.com/` 也无法同步到 CentOS 6的源，当您在腾讯云上继续使用默认配置的 CentOS 6的源会发生报错。

<dx-alert infotype="explain" title="">
建议您升级操作系统至 CentOS 7及以上，如果您的业务过渡期仍需要使用 CentOS 6操作系统中的一些安装包，请根据本文提供的信息切换 CentOS 6的源。
</dx-alert>


## 操作步骤
1. [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
	- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
	- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)
2. 执行以下命令，查看当前操作系统 CentOS 版本。
```
cat /etc/centos-release
```
返回结果如下图所示，则说明当前操作系统版本为 CentOS 6.9。
![](https://main.qcloudimg.com/raw/de65529a43dc5bfee695c08d5f7bff80.png)
3. 执行以下命令，编辑 `CentOS-Base.repo` 文件。
```
vim /etc/yum.repos.d/CentOS-Base.repo 
```
4. 按 **i** 进入编辑模式，根据 CentOS 版本及网络环境修改 baseurl。
<dx-alert infotype="explain" title="">
您可参考 [内网服务[]()](https://cloud.tencent.com/document/product/213/5225) 及 [公网服务](https://cloud.tencent.com/document/product/213/5224) 判断实例需使用的源：
- 内网访问需切换为：`http://mirrors.tencentyun.com/centos-vault/6.x/` 源。
- 公网访问需切换为：`https://mirrors.cloud.tencent.com/centos-vault/6.x/` 源。
</dx-alert>
本文以实例操作系统为 CentOS 6.9，使用内网访问为例。修改完成后 <code>CentOS-Base.repo</code> 文件如下图所示：
<img src="https://main.qcloudimg.com/raw/1d2485a9be0df6d5f7c46151fc50d73b.png"/>
5. 按 **ESC** 输入 **:wq** 后，按 **Enter** 保存修改。
6. 执行以下命令，修改 `CentOS-Epel.repo` 文件。
```
vim /etc/yum.repos.d/CentOS-Epel.repo 
```
6. 按 **i** 进入编辑模式，根据实例网络环境修改 baseurl。
本文以使用内网访问为例，则将 `baseurl=http://mirrors.tencentyun.com/epel/$releasever/$basearch/` 修改为 `baseurl=http://mirrors.tencentyun.com/epel-archive/6/$basearch/` 即可。修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/9c4b3eaf65d005b3d6819f013037443d.png)
7. 按 **ESC** 输入 **:wq** 后，按 **Enter** 保存修改。
8. 至此已完成 YUM 源切换，您可使用 `yum install` 命令安装所需软件。


