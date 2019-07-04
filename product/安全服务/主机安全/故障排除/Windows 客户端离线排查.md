## 客户端进程未启动排查
1. 请查询主机安全（云镜）进程是否存在。
打开 Windows 任务管理器，查找名为`YDService.exe`的进程是否存在。
 ![](https://main.qcloudimg.com/raw/27dbe87687c917e2cd2426cbc71a45c4.png)
2. 如果进程不存在，可能存在以下情况：
 - 服务器未安装主机安全（云镜）或者客户端已被卸载，请根据 [快速入门](https://cloud.tencent.com/document/product/296/12236) 安装指引，进行客户端安装。
 - 客户端可能出现异常冲突或者崩溃，导致进程没有启动。
3. 排查方法：
 - 可查看客户端日志，存放路径：`C:\Program Files\QCloud\YunJing\log`。
 - 可执行命令：`sc start ydservice`手动运行客户端。

## 网络故障排查
如果进程存在，但 CVM 不在线，大部分原因是网络不通，请按照以下操作进行排查：
1. 检查 DNS 是否被修改，可以通过执行如下命令行进行排查，只要其中一个返回正常结果，则表示 DNS 无问题：
 - 基础网络下载地址（非 VPC 服务器）：`telnet s.yd.qcloud.com 5574`。
 - VPC 和黑石服务器下载：`telnet s.yd.tencentyun.com 5574`。
2. 防火墙阻拦导致故障，需要开放5574、8080、80、9080端口。
