##使用场景
通过EIP访问外网时可选NAT模式或EIP直通模式（当前默认NAT模式），NAT模式下EIP对本地不可见。EIP直通后EIP在本地可见，在做配置时无须每次手动加入EIP地址，降低开发成本。目前EIP直通通过白名单控制仅支持VPC内的设备。
##操作步骤
###下载EIP配置脚本
由于EIP直通过程会导致网络中断，需先下载EIP直通脚本并上传至CVM
1）打开云服务器CVM控制台。
2）在左侧导航窗格中，点击【弹性公网IP】。
3）点击EIP直通后，下载EIP直通配置脚本。（linux脚本下载  windows脚本下载）
4）下载到本地后，上传至需要做EIP直通的机器中。
###运行EIP直通
1）打开云服务器CVM控制台。
2）在左侧导航窗格中，点击【弹性公网IP】。
3）在选择列表【操作】一列中，点击EIP直通按钮。
###运行EIP直通脚本
1）登录到需要EIP直通的CVM。
2）运行EIP直通脚本
CentOS操作系统下：eip_direct.sh install XX.XX.XX.XX( EIP地址可选）
Windows操作系统下：eip.bat XX.XX.XX.XX( EIP地址）



> 注意：
脚本仅支持eth0, 暂不支持辅助网卡。
NAT网关可绑定开通直通模式的EIP，但无直通效果。