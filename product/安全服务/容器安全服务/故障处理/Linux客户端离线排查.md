本文档将指导您进行 Linux 客户端离线排查，包括客户端进程未启动排查及网络故障排查。
>?镜像安全扫描报离线提示时，需根据镜像名称/ID 定位关联主机后再进行客户端离线排查。
## 客户端进程未启动排查
1. 请查询容器安全服务进程是否存在。输入：`ps -ef|grep YD`。
	- 正常状态下，容器安全服务存在两个进程，如下图所示：
  ![1](https://main.qcloudimg.com/raw/f999a58033d7ddca296e4eb74f2758a9.png)
	- 如果进程不存在，可能存在以下情况：
	 - 服务器未安装容器安全服务或者客户端已被卸载，请根据 [快速入门](https://cloud.tencent.com/document/product/1285/52087) 安装指引，进行客户端安装。
	 - 客户端可能出现异常冲突或者崩溃，导致进程没有启动。
2. 若服务器已安装容器安全服务或者客户端，可采用以下方法排查客户端进程未启动原因：
 - 可查看客户端日志，存放路径：`/usr/local/qcloud/YunJing/log`。
 - 可执行命令：`sh /usr/local/qcloud/YunJing/startYD.sh` 启动容器安全服务服务。

## 网络故障排查
如果进程存在，但容器安全服务不在线，大部分原因是网络不通，请按照以下操作进行排查：    
1. 如果无法访问容器安全服务域名，可以尝试修改 DNS。可以通过执行如下命令行，排查容器安全服务域名是否可以访问： 
	- VPC 网络和黑石服务器环境：`telnet s.yd.tencentyun.com 5574`。
	**正常情况下**：返回如下图所示结果。
![](https://main.qcloudimg.com/raw/50e39ceadcb275a72738b235e9637b4c.png)
**如果无法访问**：
		1. 可以尝试修改`dns nameserver`字段：`vim /etc/resolv.conf`
		`nameserver 183.60.83.19`
		`nameserver 183.60.82.98`
		2. 修改完成后，重新执行`telnet s.yd.tencentyun.com 5574`检测能否连通。
		![](https://main.qcloudimg.com/raw/1ca906db209a6ddacaad46146a7355b8.png)
		3. 如果可以连通，等待几分钟后（时间长短根据网络情况而定），控制台将能看到对应服务器重新上线。
	- 基础网络环境（非 VPC 上的服务器）：`telnet s.yd.qcloud.com 5574`。
	**正常情况下**：返回如下图所示结果。
	![](https://main.qcloudimg.com/raw/93a2f6f05867b88aa41e753e4c4e83c0.png)
		**如果无法访问**：
		1. 可以尝试修改`dns nameserver`字段：`vim /etc/resolv.conf`，先把原有的`nameserver`字段注释，再新增`nameserver`字段，具体的 nameserver ip 相关内容，请参见 [内网服务](https://cloud.tencent.com/document/product/213/5225)。
		2. 修改完成后，重新执行`telnet s.yd.qcloud.com 5574`检测能否连通。
		3. 如果可以连通，等待几分钟后（时间长短根据网络情况而定），控制台将能看到对应服务器重新上线。
2. 防火墙策略限制，需要在 Linux 客户端开放 TCP 端口：5574、8080、80、9080。
3. 如果容器安全服务进程存在，且不是由于网络原因导致的客户端离线，请打包客户端日志（日志路径：`/usr/local/qcloud/YunJing/log`）并 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=141&level2_id=635&source=0&data_title=T-Sec-%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8&level3_id=640&radio_title=%E4%B8%BB%E5%8A%A8%E6%9C%8D%E5%8A%A1&queue=3233&scene_code=30899&step=2) 进行反馈。
