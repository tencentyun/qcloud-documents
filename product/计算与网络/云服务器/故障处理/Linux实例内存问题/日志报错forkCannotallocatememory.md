## 现象描述
日志中出现报错信息 “fork：Cannot allocate memory”。如下图所示：
![](https://main.qcloudimg.com/raw/db85a43e7495f1655a2b59063ffc33e3.png)

## 可能原因
可能是线程数超限导致。系统内部的总线程数达到了 `pid_max` 时，再创建新线程时会报 “fork：Cannot allocate memory” 错。

## 解决思路
1. 参考 [处理步骤](#ProcessingSteps)，查看实例内存使用率是否过高。
2. 核实线程数是否不足，并修改总线程数 `pid_max` 配置。 



## 处理步骤[](id:ProcessingSteps)
1. 参考 [内存使用率过高问题处理](https://cloud.tencent.com/document/product/213/54644#ProcessingSteps) ，查看实例是否内存使用率过高。若实例内存使用率正常，则执行下一步。
2. 执行以下命令，查看系统 `pid_max` 值。
```
sysctl  -a | grep pid_max
```
`pid_max` 默认值为32768，返回结果如下图所示：
![](https://main.qcloudimg.com/raw/816a0bd183244aadf14e04c6ed200d68.png)
3. 执行以下命令，查看系统内部总线程数。
```
pstree -p | wc -l
```
若总线程数达到了 `pid_max`，则系统在创建新线程时会报 “fork Cannot allocate memory” 错。
>?您可执行 `ps -efL` 命令，定位启动线程较多的程序。
>
4. 将 `/etc/sysctl.conf` 配置文件中的 `kernel.pid_max` 值修改为65535，以增加线程数。修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/a4bbf49b3236b9f50988e914298adb31.png)
5. 执行以下命令，使配置立即生效。
```
sysctl -p
```
