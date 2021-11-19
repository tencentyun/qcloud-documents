## 操作场景

在2018年3月1号之后，腾讯云官网提供的 Linux 公有镜像预安装了纯开源的工具 Cloud-Init，并通过 Cloud-Init 实现了实例的所有初始化操作，使得整个实例内部的操作更加的透明，详情请参见 [Cloud-Init](https://cloud.tencent.com/document/product/213/19670#cloud-init)。
Cloud-Init 在**每次启动**时会根据 `/etc/cloud/templates/hosts.${os_type}.tmpl` 模板生成一份新的 `/etc/hosts` 文件覆盖实例原有的 `/etc/hosts` 文件，导致用户在实例内部手动修改 `/etc/hosts` 配置并重启实例后， `/etc/hosts` 配置又变为原始默认配置。

## 前提条件
腾讯云针对 Cloud-Init 的覆盖操作已经做了优化，**2018年9月后使用公共镜像**创建的实例不会出现 `/etc/hosts` 配置在重启后被覆盖的问题。
若您的实例创建于**2018年9月前**，请通过下面的解决方案进行修改。

## 操作步骤

### 方案一 
1. 登录 Linux 服务器。
2. 执行以下命令，将 `/etc/cloud/cloud.cfg` 配置文件中的 `- update_etc_hosts` 修改为 `- ['update-etc-hosts', 'once-per-instance']`。
```
sed -i "/update_etc_hosts/c \ - ['update_etc_hosts', 'once-per-instance']" /etc/cloud/cloud.cfg
```
3. 执行以下命令，在 `/var/lib/cloud/instance/sem/` 路径下创建 `config_update_etc_hosts` 文件。
```
touch /var/lib/cloud/instance/sem/config_update_etc_hosts
```

### 方案二
>?此方案以 CentOS7.2 操作系统为例。
>
#### 获取 hosts 模版文件路径
1. 登录 Linux 服务器。
2. 执行以下命令，查看系统 hosts 模版文件。
```
cat /etc/hosts
```
hosts 模版文件如下图所示：
![](https://main.qcloudimg.com/raw/f51f9c53004574f72d32f5ed790c8563.png)


#### 修改 hosts 模版文件
>?以添加 127.0.0.1 test test 为例，您可按需修改 hosts 模版文件与 /etc/hosts 文件。
>
1. 执行以下命令，修改 hosts 模版文件。
```
vim /etc/cloud/templates/hosts.redhat.tmpl
```
2. 按 **i** 切换至编辑模式。
3. 在文件末尾输入以下内容。
```
127.0.0.1 test test
```
4. 输入完成后，按 **Esc**，输入 **:wq**，保存文件并返回。

#### 修改 /etc/hosts 文件
1. 执行以下命令，修改 `/etc/hosts` 文件。
```
vim /etc/hosts
```
2. 按 **i** 切换至编辑模式。
3. 在文件末尾输入以下内容。
```
127.0.0.1 test test
```
4. 输入完成后，按 **Esc**，输入 **:wq**，保存文件并返回。



