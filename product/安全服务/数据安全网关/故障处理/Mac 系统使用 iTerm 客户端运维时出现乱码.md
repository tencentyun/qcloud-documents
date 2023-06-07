## 现象描述
Mac 系统使用 iTerm 客户端访问 Linux 服务器时，中文出现乱码。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5877997ada02fa3e76bd762e94ead897.png)

## 可能原因
Mac 系统内 SSH 配置文件问题。

## 解决思路
修改 Mac 系统中的 ssh_config 文件。

## 处理步骤
1.	打开 Mac 系统的终端，输入命令：vi /etc/ssh/ssh_config。
2.	将 SendEnv LANG 处的配置修改为 SendEnv LANG LC_*。
![](https://qcloudimg.tencent-cloud.cn/raw/316b8404d056555c1e5476acfe54de92.jpg)
3.	关闭 iTerm 客户端，重新使用堡垒机访问目标设备，确认乱码问题是否解决。
