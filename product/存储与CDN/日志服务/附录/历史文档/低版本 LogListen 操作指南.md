
>! 本文档提供2.2.4以下版本的 LogListener 操作指南，后续可能不再维护，建议您更新到最新版本，最新版本安装操作详见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。

#### 启动 LogListener

进入`loglistener`安装目录，通过以下脚本启动 LogListener：

```plaintext
cd loglistener/tools; ./start.sh
```

#### 停止 LogListener

进入`loglistener`安装目录，通过以下脚本停止 LogListener：

```shell
cd loglistener/tools; ./stop.sh
```

#### 查看 LogListener 进程状态

进入`loglistener`安装目录，通过以下命令查看 LogListener 进程：

```shell
cd loglistener/tools; ./p.sh
```

![](https://main.qcloudimg.com/raw/fea48cecfb8869bfecb58563c40e1bc3.png)
正常情况下，将存在以下三个进程：

```shell
bin/loglistenerm -d                                #守护进程
bin/loglistener --conf=etc/loglistener.conf        #主进程    
bin/loglisteneru -u --conf=etc/loglistener.conf    #更新进程
```

#### 卸载 LogListener

进入`loglistener`安装目录，通过以下命令卸载 LogListener：

```shell
cd loglistener/tools; ./uninstall.sh
```

#### 检查 LogListener 心跳及配置

进入`loglistener`安装目录，通过以下命令卸载 LogListener：

```shell
cd loglistener/tools; ./check.sh
```
