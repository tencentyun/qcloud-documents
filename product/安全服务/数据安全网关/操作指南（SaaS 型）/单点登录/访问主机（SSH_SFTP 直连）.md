## 操作场景
用户通过堡垒机进行对主机的访问和操作。下面将为您详细介绍如何通过 SSH/SFTP 客户端直连方式访问主机。下面以 macOS 系统下的 SecureCRT 为例，介绍如何通过 SSH 客户端直连方式访问 Linux 主机，其他客户端（例如 XShell、Xftp、Transmit 等）请参考以下方式进行访问。

## 前提条件
- 管理员已告知运维人员登录地址。
- 管理员已授予运维人员访问主机的权限。
- 运维人员已完成 [账号激活](https://cloud.tencent.com/document/product/1025/55183#step2)。
- 使用以下信息登录指定目标主机：
 - IP 地址：堡垒机的 IP 地址。
 - 端口：8322。
 - 用户：堡垒机的用户名/待访问主机的账号/待访问主机的 IP 地址。
 - 密码：堡垒机的用户密码。

>!如果您的主机是通过同步的方式添加到堡垒机，则待访问的主机 IP 地址请填写内网 IP。
>

## 操作步骤
1.	打开 SecureCRT，单击左侧的 **Session Manager**。
![](https://qcloudimg.tencent-cloud.cn/raw/9d191e9d1ace8c665073422cfda0948a.png)
2. 单击 **New Session**，打开 New Session Wizard 窗口，窗口当中 Protocol 设置为 **SSH2**，单击 **Continue**。
![](https://qcloudimg.tencent-cloud.cn/raw/086965702afe3926a9e3782e5d5ce077.png)
3. 输入登录信息，单击 **Continue**。
![](https://qcloudimg.tencent-cloud.cn/raw/2e0665bbee20a6a3cb777f7be2600ffe.png)
**参数列表**
<table>
<thead>
<tr>
<th>参数名称</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>Hostname</td>
<td>堡垒机的 IP 地址，联系管理员获取</td>
</tr>
<tr>
<td>Port</td>
<td>8322</td>
</tr>
<tr>
<td>Firewall</td>
<td>None</td>
</tr>
<tr>
<td>Username</td>
<td>堡垒机的用户名/待访问主机的账号/待访问主机的 IP 地址，例如：test/root/192.168.10.20</td>
</tr>
</tbody></table>
4. 输入自定义的 Session name 之后，单击 **Done**。
![](https://qcloudimg.tencent-cloud.cn/raw/fba5cfa1820d87b26d27d245a02a0f82.png)
5. 返回 Session Manager 后，双击“待访问的会话”。
![](https://qcloudimg.tencent-cloud.cn/raw/01adf76faecf43aaf0e775f808ea5a6f.png)
6. 在弹窗当中，输入当前堡垒机用户的密码，单击 **OK**。
![](https://qcloudimg.tencent-cloud.cn/raw/6cfb374781769d21959b8c0be75ac43e.png)
7.在弹窗当中，输入双因子验证码，单击 **OK**。
![](https://qcloudimg.tencent-cloud.cn/raw/ebc5189b9cb2d7b4d8ccdbb6f63e3176.png)
8. 如果待访问的目标主机的账号未托管密码，则在弹窗当中输入主机账号的密码，然后单击 **OK**。如果已托管密码，则跳过此步骤。
![](https://qcloudimg.tencent-cloud.cn/raw/18bc3b384142375262cd725959435367.png)
9.	登录到目标主机，可进行运维操作。
>?通过堡垒机访问主机的所有操作将会被记录。
>
![](https://qcloudimg.tencent-cloud.cn/raw/8b6136c78b5cfdaac720e11f3f740132.png)
