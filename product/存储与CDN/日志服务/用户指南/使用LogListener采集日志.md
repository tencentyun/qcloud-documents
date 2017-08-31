LogListener是腾讯云日志服务提供的日志采集Agent，您可以在您的安装LogListener实时采集日志

##LogListener的系统支持

目前LogListener支持如下版本的Linux 64位操作系统

centos6.0

centos7.2

## LogListener使用指南

###安装LogListener

[点击此处下载安装包](https://mc.qcloudimg.com/static/archive/e781c7e7651764dda458ff6d202aebb4/loglistener.0.1.0.tar.gz)，将安装包解压至指定的目标目录中，在root下执行

```
cd loglistener/tools/op;
./install ($uin)($region)
```

注：uin为您的腾讯云帐号ID，而非APPID，您可登录腾讯云控制台，在帐号中查看您的帐号ID。region为您所使用的日志服务区域。服务区域编码如下

```
sh - 上海
```

安装脚本会注册`crontab`，以保证机器重起后，客户端正常拉起

```
*/1 * * * *  cd /…/loglistener/tools/cron; ./check_all.sh  > /dev/null 2>&1
```

###查看进程

您可以通过以下命令查看进程

```
cd loglistener/tools/op; ./p.sh
```

正常情况下，将存才以下三个进程

```
./loglistener_watchdog                                   --守护进程
./loglistener_dcc ../etc/loglistener_dcc.conf nofork     --负责网络收发
./loglistener_mcd ../etc/loglistener_mcd.conf nofork     --负责日志监听
```

###起停客户端

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

卸载操作将掉客户端，注销`crontab`，并清理整个模块及其共享内存、中间文件及日志

## LogListener工作原理

LogListener是通过文件系统的修改事件（Inotify）来感知文件的变化，采集日志。

## LogListener相关指标与使用限制

采集延时，2秒

采集配置变更生效延时，1分钟内

日志量限制，16MB/s

最大连接数限制，1024

内存使用，正常情况最多50MB，后台服务故障时150MB

CPU使用，5MB/s日志量下，3进程合计不超过单核20%