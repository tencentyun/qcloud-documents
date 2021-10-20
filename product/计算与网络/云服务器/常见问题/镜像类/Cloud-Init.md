## Cloud-Init

### 什么是 Cloud-Init？
Cloud-Init 是一个开源工具，运行在云服务器实例内部的一个非常驻服务，在开机启动时执行，执行完成立即退出，不会监听任何端口。
腾讯云的 Linux 公有镜像都预安装了 Cloud-Init 服务。由于 Cloud-Init 服务主要用于实现对 CVM 实例的初始化操作（例如，对 DNS，Hostname，IP 等信息的配置），以及执行一些用户在创建 CVM 实例时指定首次开机启动要执行的自定义脚本，因此需要以 root 用户运行 Cloud-Init 服务。

### 如何确认 Linux 实例内部的 Cloud-Init 服务是否正常运行？


#### Cloud-Init 服务运行排查方案[](id:checkcloud-init)
首先请登录实例，依次执行以下命令，观察是否报错。显示执行结果则服务正常运行，否则会提示错误原因，请根据提示进行问题排查。
1. 删除 cloud-init 缓存目录。
```
rm -rf /var/lib/cloud
```
2. 执行完整的 cloud-init 初始化。
```
cloud-init init --local
```
3. 根据配置的数据源拉取数据。
```
cloud-init init
```
4. Cloud-Init 初始化分为多个 stage，为保证各个 stage 的依赖充分，cloud-init modules 指定运行 config stage。
```
cloud-init modules --mode=config
```
5. cloud-init modules 指定运行 final stage。
```
cloud-init modules --mode=final
```

### Cloud-Init 执行了哪些实例初始化的操作？

腾讯云通过 Cloud-Init 实现了实例的所有初始化操作，使得整个实例内部的操作更加的透明。以下内容简单介绍了相关操作情况，更多详情可见 [Cloud-init 官方文档](http://cloudinit.readthedocs.io/en/latest/)。

<table>
<tr><th style="width: 25%;">初始化类型</th><th style="width: 25%;">默认行为</th><th style="width: 25%;">禁用方式</th><th style="width: 25%;">注意事项</th></tr>
<tr>
	<td>hostname 的初始化</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会根据 <code>vendor_data.json</code> 中的 hostname 信息来设置实例的 hostname。</td>
	<td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的 hostname 设置，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- scripts-user</code> 这行配置。</td>
	<td>如果您禁用了 <code>- scripts-user</code> 这行配置，实例内部的 <code>/var/lib/cloud/instance/scripts/runcmd</code> 初始化脚本将不会被执行，并会同时影响其他子项的初始化（主要涉及：云监控、云安全的安装、软件源的设置）。 同时，在您创建子机时，自定义脚本也不会被执行。</td>
</tr>

<tr>
	<td>/etc/hosts 的初始化</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会默认将 <code>/etc/hosts</code> 初始化为 <code>127.0.0.1 $hostname</code>。</td>
	<td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的 /etc/hosts 设置，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- scripts-user</code> 与 <code>- ['update_etc_hosts', 'once-per-instance']</code> 这两行配置。</td>
	<td>
		<ul style="margin: 0px;">
			<li>如果您禁用了 <code>- scripts-user</code> 这行配置，实例内部的 <code>/var/lib/cloud/instance/scripts/runcmd</code> 初始化脚本将不会被执行，并会同时影响其他子项的初始化（主要涉及：云监控、云安全的安装、软件源的设置）。同时，在您创建子机时，自定义脚本也不会被执行。</li>
			<li>每当子机重启时，部分存量机器 <code>/etc/hosts</code> 的设置都会被覆盖。解决方案请参见 <a href="https://cloud.tencent.com/document/product/213/34698">如何有效的修改 Linux 实例的 etc hosts 配置</a>。</li>
		</ul>
	</td>
</tr>

<tr>
	<td>DNS 的初始化（非 DHCP 场景）</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会根据 <code>vendor_data.json</code> 中的 nameservers 信息来设置实例的 DNS。</td>
	<td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的 DNS 设置，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- resolv_conf</code> 与 <code>unverified_modules: ['resolv_conf']</code> 两行配置。</td>
	<td>无。</td>
</tr>

<tr>
	<td>软件源的初始化</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会根据 <code>vendor_data.json</code> 中的 write_files 信息来设置实例的软件源。</td><td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的软件源设置，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- write-files</code> 这行配置。</td>
	<td>无。</td>
</tr>

<tr>
	<td>NTP 的初始化</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会根据 <code>vendor_data.json</code> 中的 NTP Server 信息来设置实例的 NTP 服务器配置，并拉起 NTP Service。</td>
	<td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的 NTP 设置，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- ntp<code/> 这行配置。</td>
	<td>无。</td>
</tr>

<tr>
	<td>密码的初始化</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会根据 <code>vendor_data.json</code> 中的 chpasswd 信息来设置实例的默认账号密码。</td>
	<td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的默认账号密码，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- set-passwords</code> 这行配置。</td>
	<td>无。</td>
</tr>

<tr>
	<td>密钥绑定</td>
	<td> 实例<b>首次启动</b>时，Cloud-Init 会根据 <code>vendor_data.json</code> 中的 ssh_authorized_keys 信息来设置实例的默认账号密钥。</td>
	<td>当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的密钥，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面删除 <code>- users-groups</code> 这行配置。</td>
	<td>如果您通过手工的方式在实例内部自行绑定密钥，在通过控制台下发密钥绑定的操作时，系统会将此密钥覆盖。</td>
</tr>

<tr>
	<td>网络初始化（非 DHCP 场景）</td>
	<td>实例<b>首次启动</b>时，Cloud-Init 会根据 <code>network_data.json</code> 中的信息来设置实例的 IP、GATEWAY、MASK 等。</td>
	<td> 当您使用自定义镜像创建或重装实例时，您想保持自定义镜像内部自定义的网络信息，可以在制作自定义镜像之前在 <code>/etc/cloud/cloud.cfg</code> 里面增加 <code>network: {config: disabled}</code> 这行配置。</td>
	<td>无。</td>
</tr>
</table>

### 如何排查 Cloud-Init 常见问题？ 

#### 1. 因卸载 Cloud-Init 的依赖包导致报错
- 问题现象：
在使用命令确认 Cloud-Init 服务是否正常运行时，收到如下的错误：
```
Traceback (most recent call last):
  File "/usr/bin/cloud-init", line 5, in 
    ********
    raise DistributionNotFound(req)
pkg_resources.DistributionNotFound: pyyaml
```
- 问题分析 ：
“pkg_resources.DistributionNotFound: xxxxx ” 表示 Cloud-Init 的安装依赖包被卸载。
- 解决方案：
 1. 重新安装该依赖包。
 2. 根据 [Cloud-Init 服务运行排查方案](#checkcloud-init) 执行操作，直至全部执行完无错误为止。

#### 2. 修改了默认 Python 解释器导致报错
- 问题现象：
在开机启动执行 Cloud-Init 时报错。
- 问题分析：
安装 Cloud-Init 时，Python 解释默认使用 Python2（即 `/usr/bin/python` 与 `/bin/python` 这两个软连链向 Python2）。当用户业务有需要时，可能会在实例内部把 Python 的默认解释器改为 Python3（即修改 `/usr/bin/python` 与 `/bin/python` 这两个软连，使其指向 Python3）。由于兼容性问题，导致在开机启动执行 Cloud-Init 时报错。
- 解决方案：
 1. 修改 `/usr/bin/cloud-init` 文件中指定的 Python 解释器，将 `#/usr/bin/python`或`#/bin/python` 修改为 `#! user/bin/python`。
<dx-alert infotype="notice" title="">
不要使用软连接，直接指向具体的解释器。
</dx-alert>
 2. 根据 [Cloud-Init 服务运行排查方案](#checkcloud-init) 执行操作，直至全部执行完无错误为止。

## Cloudbase-Init

### 什么是 Cloudbase-Init？
与 Cloud-Init 相似，Cloudbase-Init 是与 Windows 云服务器实例通信的桥梁。 在实例首次启动的时候会执行 Cloudbase-Init 服务，该服务会读取出实例的初始化配置信息，并对实例进行初始化操作。同时包括后续的重置密码、修改 IP 等功能也都是通过 Cloudbase-Init 来实现的。

### 如何确认 Windows 实例内部的 Cloudbase-Init 服务是否正常运行？


#### Cloudbase-Init 服务运行排查方案：[](id:checkcloudbase-init)
1. 登录实例。
<dx-alert infotype="explain" title="">
若您忘记密码或因为 Cloudbase-Init 服务异常重置密码失败，可通过 [步骤 2](#step02) 进行密码重置。 
</dx-alert>
2. [](id:step02)打开**控制面板** > **管理工具** > **服务**。
3. 找到 cloudbase-init 服务，并右键单击**属性**，打开 cloudbase-init 的属性窗口。
 - 查看“启动类型”，确保“启动类型”为“自动”。如下图所示：
![](https://main.qcloudimg.com/raw/43f39931ec8932f88ee491f2bdbd7ada.png)
 - 查看“登录身份”，确保“登录身份”为“本地系统帐户”。如下图所示：
![](https://main.qcloudimg.com/raw/5a69afcde36c5bb3259ac1f136f59118.png)
 - 手动启动 cloudbase-init 服务并观察是否有相关报错。
如果有报错需要优先解决，并请确认是否安装相关安全软件拦截 cloudbase-init 执行的相关操作。 
![](https://main.qcloudimg.com/raw/97684bd42d3b0d05eee996d0106825e3.png)
 - 打开“注册表”搜索并找到全部的“LocalScriptsPlugin”，确保其值为2。如下图所示：
![](https://main.qcloudimg.com/raw/4f98965fa228c7f948fc8d720424a7ea.png)
 - 确认 CD-ROM 的加载是否被禁用。如下图所示，可以看到一个光驱设备，则表示正常加载；否则是被禁用了，需要取消禁用。
![](https://main.qcloudimg.com/raw/0e8c68537e238fe7a1e4b718848b9e98.png)

### 如何排查 Cloudbase-Init 常见问题？
#### 初始化重置密码失败
- 可能原因：
 - 手动修改 cloudbase-init 账号密码导致 cloudbase-init 服务启动失败，从而使得初始化重置密码等操作失败。
 - 禁用了 cloudbase-init 服务，从而使得初始化重置密码等操作失败。
 - 安装安全软件拦截了 cloudbase-init 服务重置密码的操作，从而使得重置密码流程返回成功但实际重置失败。
- 解决方案：
请针对可能原因，分别参考以下三点进行操作。
 1. 将 cloudbase-init 服务改为 LocalSystem 服务，具体操作方式请参见 [Cloudbase-Init 服务运行排查方案](#checkcloudbase-init) 的 [步骤 2](#step02)。 
 2. 将 cloudbase-init 服务启动类型改为自动。 具体操作方式请参见 [Cloudbase-Init 服务运行排查方案](#checkcloudbase-init) 的 [步骤 2](#step02)。
 3. 卸载对应的安全软件， 或在安全软件里面对 cloudbase-init 服务的相关操作加白名单。


