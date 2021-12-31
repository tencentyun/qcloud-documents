## 现象描述
使用 VNC 无法正常登录云服务器，在输入登录密码前就出现报错信息 “Account locked due to XXX failed logins”。如下图所示：
![](https://main.qcloudimg.com/raw/0dcc0c3b62a36ba0f269e629a3365564.png)

## 可能原因
使用 VNC 登录会调用 `/etc/pam.d/login` 这个 pam 模块进行校验，而在 login 配置文件中具备 `pam_tally2.so` 模块的认证。`pam_tally2.so` 模块的功能是设置 Linux 用户连续 N 次输入错误密码进行登录时，自动锁定 X 分钟或永久锁定。其中，永久锁定需进行手工解锁，否则将一直锁定。

如果登录失败超过配置的尝试次数，登录帐户就会被锁定一段时间，且暴力破解也有可能导致帐户被锁定从而无法登录。下图为已配置的登录可尝试次数：
![](https://main.qcloudimg.com/raw/806c1d8ccded0746f5457320df479177.png)
`pam_tally2` 模块参数说明见下表：
<table>
<tr>
<th>参数</th><th>说明</th>
</tr>
<tr>
<td><code>deny=n</code></td>
<td> 登录失败次数超过 n 次后拒绝访问。</td>
</tr>
<tr>
<td><code>lock_time=n </code></td>
<td>登录失败后锁定的时间（秒）。</td>
</tr>
<tr>
<td><code>un lock_time=n</code></td>
<td>超出登录失败次数限制后，解锁所需的时间。</td>
</tr>
<tr>
<td><code>no_lock_time </code></td>
<td>不在日志文件 <code>/var/log/faillog</code> 中记录 <code>.fail_locktime</code> 字段。</td>
</tr>
<tr>
<td><code>magic_root   </code></td>
<td>root 用户（uid=0）调用该模块时，计数器不会递增。</td>
</tr>
<tr>
<td><code>even_deny_root </code></td>
<td>root 用户登录失败次数超过 deny=n 次后拒绝访问。</td>
</tr>
<tr>
<td><code>root_unlock_time=n  </code></td>
<td>与 <code>even_deny_root</code> 相对应的选项。如果配置该选项，root 用户在登录失败次数超出限制后被锁定的时间。</td>
</tr>
</table>

## 解决思路
1. 参考 [处理步骤](#ProcessingSteps)，进入 login 配置文件，临时注释 `pam_limits.so` 模块配置。
2. 核实帐户锁定的原因，并加固安全策略。

## 处理步骤[](id:ProcessingSteps)
1. 尝试使用 SSH 登录云服务器，详情请参见 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。
	- 登录成功，则执行下一步。
	- 登录失败，则需使用单用户模式，详情请参见 [通过控制台进入 Linux 实例单用户模式](https://cloud.tencent.com/document/product/213/33321)。
2. 登录成功后，执行以下命令查看日志信息。
```
vim /var/log/secure
```
此文件一般用来记录安全相关的信息，其中大部分记录为用户登录云服务器的相关日志。如下图所示，可从信息中获取有 `pam_tally2` 的报错信息。
![](https://main.qcloudimg.com/raw/f45fb4564cfea44f0210a6e9b7124b73.png)
3. 依次执行以下命令，进入 `/etc/pam.d` 后，搜索日志中报错 pam 模块的关键字 `pam_tally2`。
```
cd /etc/pam.d
```
```
find . | xargs grep -ri "pam_tally2" -l
```
返回类似如下图所示信息，则表示 `login` 文件中配置了该参数。
![](https://main.qcloudimg.com/raw/a5d272e11a88d4f9cee347244fb98441.png)
4. 执行以下命令，临时注释 `pam_tally2.so` 模块配置。配置完成后，即可恢复登录。
```
sed -i "s/.*pam_tally.*/#&/" /etc/pam.d/login
```
4. 核实帐户锁定是由人为误操作还是暴力破解引起。若是由暴力破解引起，建议选择以下方案加固安全策略：
 - 修改云服务器密码，密码设置为由大写、小写、特殊字符、数字组成的12 - 16位的复杂随机密码。详情请参见 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
 - 删除云服务器中已不再使用的用户。
 - 将 sshd 的默认22端口改为1024 - 65525间的其他非常用端口。详情请参见 [修改云服务器远程默认端口](https://cloud.tencent.com/document/product/213/42838)。
 - 管理云服务器已关联安全组中的规则，只需放通业务和协议所需端口，不建议放通所有协议及端口。详情请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。
 - 不建议向公网开放核心应用服务端口访问。例如，mysql 及 redis 等。您可将相关端口修改为本地访问或禁止外网访问。
 - 安装云镜等防护软件，并添加实时告警，以便及时获取异常登录信息。
 



