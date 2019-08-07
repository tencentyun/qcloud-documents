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
如果进程存在，但 CVM 不在线，大部分原因是网络不通，请按照以下操作进行排查：
1. 假设后台的地址是 a.b.c.d，执行命令：`telnet a.b.c.d 5574` ，测试网络连通性。
 - 正常情况下，将成功返回如下图所示结果：
  ![](https://main.qcloudimg.com/raw/261893e2591f763ac8e55bbe48072dec.png)
 - 异常情况下，将返回超时，由此判断是网络故障。
2. 可能的故障原因：
 - 修改 DNS 导致故障，通过`cat /etc/resolv.conf`查看是否修改了 DNS。
 - 防火墙阻拦导致故障，需要开放5574、8080、80、9080端口。
