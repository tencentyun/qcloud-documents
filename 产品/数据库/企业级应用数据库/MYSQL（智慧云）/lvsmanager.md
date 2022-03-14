## 新增功能
- 新增自动化路由备份，每次路由下发前后，都会对路由进行备份。
- 新增备份路由恢复工具resumeRouter.sh
- 新增关闭lvs机器lro功能。
- keepalived调整拨测方式，默认采用misc_check方式对网关进行拨测。
- keepalived探活方式可以通过zk配置下发。


## 功能优化
- 上报lvsmanager版本号到zk
- 采用zk_acl编译
- 调整lvs设备timeout设置，将默认设置从[Timeout (tcp tcpfin udp) 900 5 300]，调整为[Timeout (tcp tcpfin udp) 120 5 300] 


## BUG修复
- 修复卸载脚本卸载lvs失败的遗留bug。



