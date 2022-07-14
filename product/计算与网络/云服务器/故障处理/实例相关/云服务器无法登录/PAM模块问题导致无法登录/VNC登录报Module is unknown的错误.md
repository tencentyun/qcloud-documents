## 现象描述
使用 VNC 登录云服务器时，即使输入正确密码也无法成功登录，并提示 “Module is unknown” 错误。如下图所示：
![](https://main.qcloudimg.com/raw/117961622ff73a5859a56bd890011302.png)

## 可能原因
使用 VNC 登录会调用 `/etc/pam.d/login` 这个 pam 模块进行校验，而该模块会将 `/etc/pam.d/system-auth` 模块引入进行校验。`/etc/pam.d/login` 配置文件的内容，如下图所示：
![](https://main.qcloudimg.com/raw/334e393e16d8a03eec44009be9265ea9.png)
可能导致登录失败的原因是 `system-auth` 配置文件中的 `pam_limits.so` 模块的模块路径配置错误。如下图所示：
![](https://main.qcloudimg.com/raw/36f36e0f2f5d0954f6fcebd39095d3b6.png)
<dx-alert infotype="explain" title="">
`pam_limits.so` 模块的主要功能是限制用户会话过程中对各种系统资源的使用情况。模块路径需根据操作系统实际情况进行填写，若写错路径会导致无法找到对应的认证模块，导致登录认证报错。

</dx-alert>



## 解决思路
1. 参考 [处理步骤](#ProcessingSteps)，进入 `system-auth` 文件，并找到 `pam_limits.so` 模块路径配置。
2. 修改 `pam_limits.so` 模块路径为正确配置即可。 

## 处理步骤[](id:ProcessingSteps)
1. 尝试使用 SSH 登录云服务器，详情请参见 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。
 - 登录成功，则执行下一步。
 - 登录失败，则需使用单用户模式，详情请参见 [通过控制台进入 Linux 实例单用户模式](https://cloud.tencent.com/document/product/213/33321)。
2. 登录成功后，执行以下命令查看日志信息。
```
vim /var/log/secure
```
此文件一般用来记录安全相关的信息，其中大部分记录为用户登录云服务器的相关日志。如下图所示，可从信息中获取有 `/lib/security/pam_limits.so` 的报错信息。
![](https://main.qcloudimg.com/raw/8f9f992d1835a9058020b435f1ef3c99.png)
3. 依次执行以下命令，进入 `/etc/pam.d` 后，搜索日志中报错 pam 模块的关键字 `/lib/security/pam_limits.so`。
```
cd /etc/pam.d
```
```
find . | xargs grep -ri "/lib/security/pam_limits.so" -l
```
返回类似如下图所示信息，则表示 `system-auth` 文件中配置了该参数。
![](https://main.qcloudimg.com/raw/eab27cf686eccfeb8a8b796360010bb5.png)
4. 进入 `system-auth` 文件，修复 `pam_limits.so` 模块路径配置。
例如，在64位的操作系统中，该模块路径可配置为绝对路径 `/lib64/security/pam_limits.so`，也可配置为相对路径 `pam_limits.so`。




