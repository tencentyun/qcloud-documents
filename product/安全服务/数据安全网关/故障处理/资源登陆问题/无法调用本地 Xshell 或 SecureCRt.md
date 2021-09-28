## 现象描述
已经安装了 Xshell/SecureCRT，但是点击访问 Linux 资源时 BHLoader 插件没有拉起对应工具，而是弹出了如下文件选择框。
![](https://main.qcloudimg.com/raw/5f36b0d557302f0b70691f8501816f28.png)
## 可能原因
工具未安装在程序的默认目录C:\Program Files 或者 C:\Program Files (x86)，导致 BHLoader 无法直接拉起工具。


## 解决思路
重新安装 Xshell 或 SecureCRT，使用默认路径安装，或手动选择工具路径。

## 处理步骤
1. 重新安装 Xshell 或 SecureCRT，安装路径选择默认目录：C:\Program Files 或者 C:\Program Files (x86)。
2. 当运维用户第一次使用工具访问资源时，BHLoader 会弹窗提示，提示是否已安装工具，选择“是”。
![](https://main.qcloudimg.com/raw/e2035b2e7449bbe54d429eaa50a47ed2.png)
3. 在选择客户端工具弹窗中，选择 Xshell/SecureCRT 的安装目录与应用程序，BHLoader 会把本次选择的结果保存在配置中，后续不用再选择。
 - Xshell 选择程序
![](https://main.qcloudimg.com/raw/fab2eb5f185cc15b67983a926f7752e3.png)
 - SecureCRT 选择程序
![](https://main.qcloudimg.com/raw/973841d5e97b054d92c3246986a63b3e.png)
