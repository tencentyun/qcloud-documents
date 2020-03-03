自定义消息功能提供了命令行发送工具（cagent_tools），开发者可以调用相应命令设置自定义消息内容，并在告警时发送相关内容。

- 目前仅支持命令行工具的方式进行上报，后续会提供 API 接口，更便于用户在代码中进行自定义消息的上报。
- cagent_tools 适用于腾讯云中使用<font color="red">系统镜像</font>创建的云服务器。

## Linux 系统下配置自定义消息
1) 安装 Linux 监控组件，安装方法见[安装监控控件](/doc/product/248/6211)。

2) 查看工具帮助

直接执行以下命令，查看帮助信息：

```
cagent_tools
```
结果如下图：
![](//mccdn.qcloud.com/img56cacd38f3fb9.png)

3) 使用示例

按以下命令行执行：

```
cagent_tools alarm ‘告警内容’
```

PHP示例：

```
$link = mysql_connect('192.168.0.2', 'mysql_user', 'mysql_password');
if (!$link) {
 //alarm content
  $alarmContent = " Connection failed ";
  $cmd = “cagent_tools alarm $alarmContent”; 
  system($cmd);
  die('Could not connect: ' . mysql_error());
}
```
Shell示例：

```
#!/bin/sh
PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:$PATH
CAGENT_CMD = /usr/bin/cagent_tools
cnt=$(ps -ef | grep mysqld | grep -v grep | wc -l)
if [ $cnt -eq 0 ] ; then
    # alarm content 
    cagent_tools alarm "the process mysqld died."
fi
```

开发者自己对收集来的数据进行分析的时如流量掉底、在线人数下降、收入异常等情况，也可以通过调用 cagent_tools 发送告警。

5) 配置完成

成功调用 cagent_tools 后，当检测到目标异常时腾讯云监控会自动将自定义消息发送至相关告警接受人。您可在腾讯云控制台【云监控】-【我的告警】-【自定义消息】查看历史告警数据。

> 注：
> 
- 中文告警内容目前仅支持 utf-8 编码格式。
- 告警内容最大长度为 256 字节， 超出部分会截断。
- 成功发送告警信息，命令行提示"send alarm OK!"，进程执行返回码为 0；若发送告警信息失败，命令行提示相应错误，进程执行返回码为非 0。

## Windows 系统下配置自定义消息
1) 安装 Windows 监控组件，安装方法见[安装监控控件](/doc/product/248/6211)。

2) 查看工具帮助

在命令行界面下直接执行以下命令，查看帮助信息：

```
cagent_tools
```
结果如下：
![](//mccdn.qcloud.com/img56cacf193430e.png)

3) 使用示例

命令行执行方式如下：

```
cagent_tools alarm ‘告警内容’
```

DOS示例：

```
@echo off
set service_name=StargateSvc
sc query %service_name% > nul
if not %errorlevel% == 0 (
    cagent_tools alarm "service %service_name% didn't exist"
)
```

开发者自己对收集来的数据进行分析的时如流量掉底、在线人数下降、收入异常等情况，也可以通过调用 cagent_tools 发送告警。

5) 配置完成
成功调用 cagent_tools 后，当检测到目标异常时，腾讯云监控会自动将自定义消息发送至相关告警接受人。您可在腾讯云控制台【云监控】-【我的告警】-【自定义消息】查看历史告警数据。

> 注：
> 
- 中文告警内容目前支持 utf-8 和 GBK 编码格式。
- 告警内容显示最大长度为 256 字节， 超出部分会截断。
- 成功发送告警信息，命令行提示"send alarm OK!"，进程执行返回码为 0；若发送告警信息失败，命令行提示相应错误，进程执行返回码为非 0。