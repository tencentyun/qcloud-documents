## 操作场景
创建边缘计算机器实例时，默认已配置 EIP 直通。如您的边缘计算机器实例未配置 EIP 直通，可通过执行 EIP 直通脚本进行配置。本文指导您如何在边缘计算机器实例上配置 EIP 直通脚本，并指导您在误操作删除脚本时，该如何恢复 EIP 直通脚本。 

## 注意事项

- 目前仅支持在 Linux 实例上配置 EIP 直通。
- EIP 直通脚本需在 CentOS 6 及以上版本和 Ubuntu 系统上运行。

## 前提条件

- 已创建边缘计算实例，及获取公网 IP。
- 已获取实例的管理员帐号和对应的密码。
- Linux 实例的内网 IP 和弹性公网 IP 需均在主网卡（eth0）上。
如果主网卡绑定的公网 IP 不是弹性 IP，则需要先转换为弹性 IP，详情请参见 [普通公网 IP 转 EIP](https://cloud.tencent.com/document/product/1199/41706)。

## 操作步骤

<span id="downloadEIPscript"></span>
### 下载 EIP 直通脚本

由于 EIP 直通过程会导致网络中断，请先选择如下任意一种方式将 EIP 直通脚本保存至边缘云服务器中。
- **方式一：上传 EIP 直通脚本**
 1. 在本地计算机中，下载 EIP 直通脚本。
 请 [点此下载](https://eip-direct-1254277469.cos.ap-guangzhou.myqcloud.com/eip_direct.sh)。
 2. 将已下载的 EIP 直通脚本上传至需要进行 EIP 直通的边缘计算机器实例中。
- **方法二：直接使用命令** 
登录边缘计算机器实例，并在实例中执行如下命令，下载 EIP 直通脚本。
```
wget https://eip-direct-1254277469.cos.ap-guangzhou.myqcloud.com/eip_direct.sh
```

### 运行 EIP 直通脚本

1. [登录 Linux 实例](https://cloud.tencent.com/document/product/1108/44895)。
2. 执行如下命令，添加执行权限。
```
chmod +x eip_direct.sh
```
3. 执行如下命令，执行脚本。
```
./eip_direct.sh install XX.XX.XX.XX
```
其中，`XX.XX.XX.XX`为 EIP 地址，可选填。如不填写，直接执行 `./eip_direct.sh install` 即可。


## 附录
如果您误操作删除了 EIP 直通脚本，可通过如下操作进行恢复。
1. 将 EIP 直通脚本上传/下载到边缘计算机器实例中。
详情请参考 [下载 EIP 直通脚本](#downloadEIPscript)。
2. 登录实例，并在该实例中执行如下命令，重启实例。
```
reboot
```

