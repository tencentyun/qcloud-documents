## Cloud-Init 介绍

在2018年3月1号之后，腾讯云官网提供的 Linux 公有镜像预安装了纯开源的工具 Cloud-Init，并通过 Cloud-Init 实现了实例的所有初始化操作，使得整个实例内部的操作更加的透明。详情请参见 [Cloud-Init](https://cloud.tencent.com/document/product/213/19670)。

## 问题背景

Cloud-Init 在**每次启动**时会根据 `/etc/cloud/templates/hosts.${os_type}.tmpl` 模板生成一份新的 `/etc/hosts` 文件覆盖实例原有的 `/etc/hosts` 文件，导致用户在实例内部手动修改 `/etc/hosts` 配置并重启实例后， `/etc/hosts` 配置又变为原始默认配置。

>? 腾讯云针对 Cloud-Init 的覆盖操作已经做了优化，2018年9月后创建的实例不会出现 `/etc/hosts` 配置在重启后被覆盖的问题。
> 若您的实例创建于2018年9月前，请通过下面的解决方案进行修改。

## 解决方案

1. 登录 Linux 服务器。
2. 执行以下命令，将 `/etc/cloud/cloud.cfg` 配置文件中的 `- update_etc_hosts` 修改为 `- ['update-etc-hosts', 'once-per-instance']`，并在 `/var/lib/cloud/instance/sem/` 路径下创建 `config_update_etc_hosts` 文件。
```
sed -i "/update_etc_hosts/c \ - ['update_etc_hosts', 'once-per-instance']" /etc/cloud/cloud.cfg
touch /var/lib/cloud/instance/sem/config_update_etc_hosts
```
