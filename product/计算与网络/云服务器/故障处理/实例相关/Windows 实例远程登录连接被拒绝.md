## 现象描述

[](id:FaultPhenomenon1)
**现象1**：Windows 使用远程桌面连接 Windows 实例时，提示 “连接被拒绝，因为没有授权此用户帐户进行远程登录。”。如下图所示：
![连接被拒绝](https://main.qcloudimg.com/raw/9ce749a2481cabf30cccdefeb00ae770.png)

[](id:FaultPhenomenon2)
**现象2**：Windows 使用远程桌面连接 Windows 实例时，提示 “要远程登录，您需要具有通过远程桌面服务进行登录的权限。默认情况下，远程桌面用户组的成员有这项权限。如果您所属的组没有这项权限，或者远程桌面用户组中已经删除了这项权限，那么需要手动为您授予这一权限。”。如下图所示：
![错误提示](https://main.qcloudimg.com/raw/52a79c81015d7e6b2f5299f98474348d.png)

## 可能原因

该用户未被允许通过远程桌面连接方式登录 Windows 实例。

## 解决思路
- 如果您远程桌面连接 Windows 实例时，遇到 [现象1](#FaultPhenomenon1) 的情况，则需要将用户帐户添加至 Windows 实例设置的允许通过远程桌面服务登录的列表中。具体的操作请参见 [配置允许远程登录的权限](#ConfigurationToAllowAccess)。
- 如果您远程桌面连接 Windows 实例时，遇到 [现象2](#FaultPhenomenon2) 的情况，则需要将用户帐户从 Windows 实例设置的不允许通过远程桌面服务登录的列表中删除。具体的操作请参见 [修改拒绝远程登录的权限](#ModifyLoginAuthority)。

## 处理步骤

### 通过 VNC 方式登录云服务器
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，找到目标云服务器实例，单击【登录】。如下图所示：
![云服务器列表页](https://main.qcloudimg.com/raw/038fce530c6c6827796e51d896306a93.png)
3. 在弹出的“登录Windows实例”窗口中，选择【其它方式（VNC）】，单击【立即登录】，登录云服务器。
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![](https://main.qcloudimg.com/raw/2dec43fa6ddb5e442da59c75f7a34b0f.png)


### [配置允许远程登录的权限](id:ConfigurationToAllowAccess)

>? 以下操作以 Windows Server 2016 为例。
>
1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;">，输入 **gpedit.msc**，按 **Enter**，打开 “本地组策略编辑器”。
2. 在左侧导航树中，选择【计算机配置】>【Windows 设置】>【安全设置】>【本地策略】>【用户权限分配】，双击打开【允许通过远程桌面服务登录】。如下图所示：
![](https://main.qcloudimg.com/raw/0a9f64957539a37d3c930932e24213c0.png)
3. 在打开的 “允许通过远程桌面服务登录 属性” 窗口中，检查允许通过远程桌面服务登录的用户列表是否存在需要登录的帐户。如下图所示：
![允许通过远程桌面服务登录](https://main.qcloudimg.com/raw/acd4d3cb6204a34c612b32c777308f9f.png)
 - 如果该用户不在允许通过远程桌面服务登录的列表中，请执行 [步骤4](#step04)。
 - 如果该用户已经在允许通过远程桌面服务登录的列表中，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 反馈。
4. [](id:step04)单击【添加用户或组】，打开 “选择用户或组” 窗口。
5. 输入需要进行远程登录的帐户，单击【确定】。
6. 单击【确定】，并关闭本地组策略编辑器。
7. 重启实例，重新尝试使用该帐户远程桌面连接 Windows 实例。


### [修改拒绝远程登录的权限](id:ModifyLoginAuthority)

>? 以下操作以 Windows Server 2016 为例。
>
1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;">，输入 **gpedit.msc**，按 **Enter**，打开 “本地组策略编辑器”。
2. 在左侧导航树中，选择【计算机配置】>【Windows 设置】>【安全设置】>【本地策略】>【用户权限分配】，双击打开【拒绝通过远程桌面服务登录】。如下图所示：
![拒绝通过远程桌面服务登录](https://main.qcloudimg.com/raw/aaea1d8c0dadb73676a926ed0ed56367.png)
3. 在打开的 “拒绝通过远程桌面服务登录 属性” 窗口中，检查拒绝通过远程桌面服务登录的用户列表是否存在需要登录的帐户。
 - 如果该用户在拒绝通过远程桌面服务登录的列表中，请将需要登录的帐户从列表中删除，并重启实例。
 - 如果该用户不在拒绝通过远程桌面服务登录的列表中，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 反馈。
 
 
 
