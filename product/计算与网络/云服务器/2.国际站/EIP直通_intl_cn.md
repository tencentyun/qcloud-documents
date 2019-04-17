## 使用场景
用户通过 EIP 访问外网时可选 NAT 模式或 EIP 直通模式，当前默认 NAT 模式。
- NAT 模式下 EIP 在本地不可见。
- EIP 直通后 EIP 在本地可见，在做配置时无须每次手动加入 EIP 地址，可降低开发成本。

> **注意：**
> 目前 EIP 直通通过白名单控制，仅支持 VPC 内的设备。

## 操作步骤
### 一、下载 EIP 配置脚本
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通脚本并上传至 CVM。步骤如下：
1. 下载 EIP 直通配置脚本，该步骤可选。下载路径：
 -  [Linux 脚本下载](https://mc.qcloudimg.com/static/archive/e66c8253642e37c62c8e581d6f0299de/eip_linux.zip)
 -  [Windows 脚本下载](https://mc.qcloudimg.com/static/archive/af1eee0dbe7d9407cddb3e1bd510cb3a/eip_windows.zip)
> 注意：
> Linux 脚本支持系统版本 CentOS 6.x、CentOS 7 和 Ubuntu。

2. 脚本下载到本地后，上传至需要进行 EIP 直通的云主机中。

### 二、开启 EIP 直通
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)。

2. 在左侧导航窗格中，点击【弹性公网IP】。

3. 在选择列表【操作】一列中，单击【EIP 直通】按钮开通即可。

### 三、运行 EIP 直通脚本
1. 登录到需要 EIP 直通的 CVM 云主机。

2. 运行 EIP 直通脚本。具体方法：

 - Linux 操作系统 CentOS 下：
```
eip_direct.sh install XX.XX.XX.XX 
```
其中，`XX.XX.XX.XX`为 EIP 地址，可选填。

 - Windows 操作系统下：
```
eip.bat XX.XX.XX.XX
```
其中，`XX.XX.XX.XX`为 EIP 地址。

> **注意：**
- 脚本仅支持 eth0，暂不支持辅助网卡。
- NAT 网关可绑定开通直通模式的 EIP，但无直通效果。
