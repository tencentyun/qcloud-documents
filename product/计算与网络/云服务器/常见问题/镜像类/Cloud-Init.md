### 什么是 Cloud-Init？
Cloud-Init 是一个纯开源工具，运行在云服务器实例内部的一个非常驻服务，在开机启动时执行，执行完成立即退出。腾讯云的 Linux 公有镜像都预安装了 Cloud-Init 服务，主要用于实现对 CVM 实例的初始化操作，以及执行一些用户在创建 CVM 实例时指定首次开机启动要执行的自定义脚本。
### 如何确认 Linux 实例内部的 Cloud-Init 服务是否正常运行？

#### Cloud-Init 服务运行排查方案
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

### 如何排查Cloud-Init 常见问题？ 
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
“pkg_resources.DistributionNotFound: xxxxx ” 表示 Cloud-Init 的安装依赖包被卸载了。
- 解决方案：
重新安装该依赖包，然后按步骤执行 [Cloud-Init 服务运行排查方案](#check1) ，直至全部执行完无错误为止。

#### 2. 修改了默认 Python 解释器导致报错
- 问题现象：
在开机启动执行 Cloud-Init 时报错。
- 问题分析：
安装 Cloud-Init 时，Python 解释默认使用的是 Python2（即`/usr/bin/python`与`/bin/python`这两个软连是链接向 Python2 的）。当用户业务有需要时，可能会在实例内部把 Python 的默认解释器改为 Python3（即修改`/usr/bin/python`与`/bin/python`这两个软连使其指向 Python3）由于兼容性问题，导致在开机启动执行 Cloud-Init 时报错。
- 解决方案：
修改`/usr/bin/cloud-init`文件里面指定的 Python 解释器，把`#/usr/bin/python`或`#/bin/python`改为`#/usr/bin/python2.7`。 不要使用软连接，直接指向具体的解释器。然后按步骤执行 [Cloud-Init 服务运行排查方案](#checkcloud-init)，直至全部执行完无错误为止。

## Cloudbase-Init
### 什么是 Cloudbase-Init？
与 Cloud-Init 相似，Cloudbase-Init 是与 Windows 云服务器实例通信的桥梁。 在实例首次启动的时候会执行 Cloudbase-Init 服务，该服务会读取出实例的初始化配置信息，并对实例进行初始化操作。同时包括后续的重置密码、修改 IP 等功能也都是通过 Cloudbase-Init 来实现的。

### 如何确认 Windows 实例内部的 Cloudbase-Init 服务是否正常运行？

#### Cloudbase-Init 服务运行排查方案：
1. 登录实例。若忘记密码或因为 Cloudbase-Init 服务异常重置密码失败，可通过步骤 2 进行密码重置。 
2. 打开** 控制面板** > **管理工具 **> **服务**， 找到 cloudbase-init 服务，右击【属性】：
 1. 查看“启动类型”，确保“启动类型”为“自动”，如下图。
![](https://main.qcloudimg.com/raw/43f39931ec8932f88ee491f2bdbd7ada.png)
 2. 查看“登录身份”，确保“登录身份”为“本地系统帐户”，如下图。
![](https://main.qcloudimg.com/raw/5a69afcde36c5bb3259ac1f136f59118.png)
 3. 手动启动 cloudbase-init 服务并观察是否有相关报错，如果有报错需要优先解决，请特别关注是否安装相关安全软件拦截 cloudbase-init 执行的相关操作。 
![](https://main.qcloudimg.com/raw/97684bd42d3b0d05eee996d0106825e3.png)
 4. 打开“注册表”搜索并找到全部的“LocalScriptsPlugin”，确保其值为 2，如下图。
![](https://main.qcloudimg.com/raw/4f98965fa228c7f948fc8d720424a7ea.png)
 5. 确认 CD-ROM 的加载是否被禁用，可以看到一个光驱设备，则正常加载，否则是被禁用了，需要取消禁用。
![](https://main.qcloudimg.com/raw/0e8c68537e238fe7a1e4b718848b9e98.png)

### 如何排查 Cloudbase-Init 常见问题？
#### 初始化重置密码失败
- 可能原因：
 1. 手动修改 cloudbase-init 账号密码导致 cloudbase-init 服务启动失败，从而使得初始化重置密码等操作失败。
 2. 禁用了 cloudbase-init 服务，从而使得初始化重置密码等操作失败。
 3.  安装安全软件拦截了 cloudbase-init 服务重置密码的操作，从而使得重置密码流程返回成功但实际重置失败。
- 解决方案：
请针对可能原因，分别参考以下三点进行操作。
 1. 将 cloudbase-init 服务改为 LocalSystem 服务，具体操作方式详见：[Cloudbase-Init 服务运行排查方案](#checkcloudbase-init) 的步骤 2。 
 2. 将 cloudbase-init 服务启动类型改为自动。 具体操作方式详见：[Cloudbase-Init 服务运行排查方案](#checkcloudbase-init) 的步骤 2。
 3. 卸载对应的安全软件， 或在安全软件里面对 cloudbase-init 服务的相关操作加白名单。
