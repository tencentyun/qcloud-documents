## 现象描述
使用 VNC 登录云服务器时，输入正确的密码无法登录，会卡在如下图所示界面，稍后会再次提示需要输入账号。
![](https://main.qcloudimg.com/raw/13b30f4ccfc97afd0e704e2e5c600047.png)
且使用 SSH 远程登录时，会出现报错信息 “Permission denied,please try again.”。如下图所示：
![](https://main.qcloudimg.com/raw/db09e73d2a057fb8b297ffd31bf67b62.png)

## 可能原因
可能是由于频繁暴力破解导致 `/var/log/btmp` 日志容量过大。该文件用于记录错误登录的日志，容量过大会导致登录时写入日志异常，造成无法正常登录。如下图所示：
![](https://main.qcloudimg.com/raw/c19f9e57a67ce6b1ed30cee22af9964c.png)

## 解决思路
1. 参考 [处理步骤](#ProcessingSteps) 查看日志文件 `/var/log/btmp` 容量是否过大。
2. 核实是否为暴力破解导致，并加固安全策略。

## 处理步骤[](id:ProcessingSteps)
1. 尝试使用 SSH 登录云服务器，详情请参见 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。
	- 登录成功，则执行下一步。
	- 登录失败，则需使用单用户模式，详情请参见 [通过控制台进入 Linux 实例单用户模式](https://cloud.tencent.com/document/product/213/33321)。
2. 进入 `/var/log` 查看日志文件 `/var/log/btmp` 容量。
3. 若日志文件 `/var/log/btmp` 容量过大，则执行以下命令，对 btmp 日志内容进行清空。清空日志文件后，即可恢复登录。
```
cat /dev/null > /var/log/btmp
```
5. 核实帐户锁定是由人为误操作还是暴力破解引起。若是由暴力破解引起，建议选择以下方案加固安全策略：
	- 修改云服务器密码，密码设置为由大写、小写、特殊字符、数字组成的12 - 16位的复杂随机密码。详情请参见 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
	- 删除云服务器中已不再使用的用户。
	- 将 sshd 的默认22端口改为1024 - 65525间的其他非常用端口。详情请参见 [修改云服务器远程默认端口](https://cloud.tencent.com/document/product/213/42838)。
	- 管理云服务器已关联安全组中的规则，只需放通业务和协议所需端口，不建议放通所有协议及端口。详情请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。
	- 不建议向公网开放核心应用服务端口访问。例如，mysql 及 redis 等。您可将相关端口修改为本地访问或禁止外网访问。
	- 安装云镜、云锁等防护软件，并添加实时告警，以便及时获取异常登录信息。
