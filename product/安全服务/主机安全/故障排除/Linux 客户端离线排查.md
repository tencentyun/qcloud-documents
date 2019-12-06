## 客户端进程未启动排查
1. 请查询主机安全（云镜）进程是否存在。输入：`ps -ef|grep YD`。
2. 正常状态下，主机安全（云镜）存在两个进程，如下图所示：
  ![1](https://main.qcloudimg.com/raw/f999a58033d7ddca296e4eb74f2758a9.png)
3. 如果进程不存在，可能存在以下情况：
 - 服务器未安装主机安全（云镜）或者客户端已被卸载，请根据 [快速入门](https://cloud.tencent.com/document/product/296/12236) 安装指引，进行客户端安装。
 - 客户端可能出现异常冲突或者崩溃，导致进程没有启动。
2. 排查方法：
 - 可查看客户端日志，存放路径：`/usr/local/qcloud/YunJing/log`。
 - 可执行命令：`/usr/local/qcloud/YunJing/YDEyes/YDService` 手动运行客户端。

## 网络故障排查
如果进程存在，但主机安全（云镜）不在线，大部分原因是网络不通，请按照以下操作进行排查：
1. 检查 DNS 是否被修改，可以通过执行如下命令行进行排查： 
	- 基础网络环境（非 VPC 服务器）：telnet s.yd.qcloud.com 5574。
	- VPC 网络和黑石服务器环境：telnet s.yd.tencentyun.com 5574。
 
 正常情况下返回如下图所示结果：
	![](https://main.qcloudimg.com/raw/50e39ceadcb275a72738b235e9637b4c.png)

2. 防火墙策略限制，需要开放 TCP 端口：5574、8080、80、9080。
