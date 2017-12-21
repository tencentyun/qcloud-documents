LogListener是腾讯云日志服务提供的日志采集Agent，您可以安装LogListener实时采集日志文件。

**此文档为较低版本 LogListener 的使用指南，若还未安装过 LogListener 我们建议您安装最新版本的LogListener。[获取最新版本 LogListener](https://cloud.tencent.com/document/product/614/11257)** 

## LogListener的系统支持

目前LogListener支持如下版本的Linux 64位操作系统

CentOS

Debian

SUSE

OpenSUSE

Ubuntu

## LogListener使用指南

### 安装LogListener

[点击下载 LogListener 1.1.2](https://mc.qcloudimg.com/static/archive/64065f325335ce4fb1ed96433eb691fd/loglistener.1.1.2.tar.gz)，将安装包解压至指定的目标目录中，在root下执行

```
cd loglistener/tools/op;
./install.sh ($SecretId)($SecretKey)($region)
```

注：这里的SecretId与SecretKey为您云api秘钥中的SecretId与SecretKey。region为您所使用的**日志服务区域而非您的机器所处的区域**。服务区域编码如下：

```
shanghai - 上海
guangzhou - 广州
chengdu - 成都
```

安装脚本会注册`crontab`，以保证机器重起后，客户端正常拉起

```
*/1 * * * *  cd /…/loglistener/tools/cron; ./check_all.sh  > /dev/null 2>&1
```

### 查看进程

您可以通过以下命令查看进程

```
cd loglistener/tools/op; ./p.sh
```

正常情况下，将存在以下三个进程

```
./loglistener_watchdog                                   --守护进程
./loglistener_dcc ../etc/loglistener_dcc.conf nofork     --负责网络收发
./loglistener_mcd ../etc/loglistener_mcd.conf nofork     --负责日志监听
```

### 启停客户端

您可以通过一下脚本启停客户端

```
cd loglistener/tools/op; ./start.sh
cd loglistener/tools/op; ./stop.sh
```

### 卸载LogListener

```
cd loglistener/tools/op;
./uninstall
```

卸载操作将删除客户端，注销`crontab`，并清理整个模块及其共享内存、中间文件及日志

## LogListener工作原理

LogListener是通过文件系统的修改事件（Inotify）来感知文件的变化，采集日志。

## LogListener相关指标与使用限制

采集延时，2秒

采集配置变更生效延时，1分钟内

日志量限制，16MB/s

日志长度限制，单条512k，如超过会跳过此512k继续采集（即本条日志会被截断入库）

最大连接数限制，1024

内存使用，正常情况最多50MB，后台服务故障时150MB

CPU使用，5MB/s日志量下，3进程合计不超过单核20%