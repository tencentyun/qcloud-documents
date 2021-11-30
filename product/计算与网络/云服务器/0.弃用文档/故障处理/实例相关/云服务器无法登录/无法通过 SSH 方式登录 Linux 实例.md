本文档以 CentOS 7.5 操作系统的云服务器为例，介绍无法通过 SSH 登录 Linux 实例的问题排查和解决方案。

## 故障现象

[使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 时，提示无法连接或者连接失败。

## 故障定位及处理
### 步骤1：查看安全组规则配置

通过 [安全组（端口）验通工具](https://console.cloud.tencent.com/vpc/helper) 进行检查安全组规则设置是否正确。
- 如果确定为安全组端口设置问题，可通过工具中的【一键放通】功能放通端口。您也可以根据实际需要，自定义设置安全组规则，请参考 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740) 重新配置安全组规则。
- 如果安全组端口设置没有问题，请执行 [下一步](#step07)。
 
###  步骤2：查看 sshd 服务端口
1. <span id="step07">[使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。</span>
>?当您在无法使用远程登录客户端及其他方式均无法登录实例的情况下，可通过 VNC 方式登录连接实例，观察实例状态并进行问题排查。
>
2. 在操作系统界面，执行以下命令，查看是否含有 sshd 服务监听的端口。
```
netstat -tnlp | grep sshd
```
 - 若返回如下结果，即表示 sshd 进程已监听22端口，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进行反馈。
```
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1015/sshd  
```
 - 若无输出，则可能是 sshd 服务未启动，请执行 [下一步](#step09)。
 
###  步骤3：查看 sshd 服务是否启动
<span id="step09">执行以下命令，查看 sshd 服务是否启动。</span>
```
systemctl status sshd.service
```
 - 如果已启动，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进行反馈。
 - 如果未启动，请执行以下命令，启动 sshd 服务，再重新使用 SSH 登录 Linux 实例。
```
systemctl start sshd
```

如果进行以上操作后，您的实例仍无法连接，建议您通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进行反馈。

