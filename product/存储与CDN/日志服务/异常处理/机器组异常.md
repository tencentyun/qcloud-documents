## 现象描述
日志采集异常，检查关联的机器组，状态异常。

## 可能原因
机器组与日志服务系统之间的心跳中断，导致日志无法采集上报。导致机器组异常的可能原因有：
1. IP 地址填写错误。
2. 网络断开。
3. LogListener 进程失败。
4. LogListener 配置错误。

## 解决思路
针对以上可能原因，逐步进行排查。

## 处理步骤
1. 请检查核对机器组中所添加的 IP 地址是否正确。
2. 请使用以下命令确认当前网络环境是否连通：
```shell
telnet <region>.cls.myqcloud.com 80
```
其中，`<region>` 为日志服务所在地域简称，具体地域信息请参阅 [可用地域](https://cloud.tencent.com/document/product/614/18940) 文档。
正常连通下，将显示如下代码。否则，显示连接失败，需排查网络环境，保证正常连网。
![](https://main.qcloudimg.com/raw/2660316a4496ac356b6e7ca5cdeb9daa.png)
3. 请查看确认 LogListener 进程是否正常运行，进入安装目录查看命令如下：
```shell
cd loglistener/tools && ./p.sh
```
正常情况下，将存在以下三个进程：
```shell
bin/loglistenerm -d                                #守护进程
bin/loglistener --conf=etc/loglistener.conf        #主进程    
bin/loglisteneru -u --conf=etc/loglistener.conf    #更新进程
```
**若有失败进程**，需要重新启动，进入安装目录执行如下命令：
```shell
cd loglistener/tools && ./start.sh
```
4. 请检查确认 LogListener 中密钥及 IP 标识配置信息是否有误，配置文件路径为：`/loglistener/etc/loglistener.conf`。
![](https://main.qcloudimg.com/raw/cfa012cfb136cbbcf78667d4d1307d26.png)
 - 密钥为腾讯云账号或协作者的 API 密钥，但不支持项目密钥。
 - 配置文件中 group_ip 信息必须与控制台机器组所填写的 IP 一致，LogListener 会自动获取机器 IP，当服务器有多个网卡时需留意检查是否一致。
