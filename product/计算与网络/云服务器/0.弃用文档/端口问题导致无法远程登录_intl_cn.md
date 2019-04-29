
本文档介绍云服务器因端口问题导致无法远程登录的排查方法和解决方案。

## 步骤一：检查网络连通性

通过本地 Ping 命令，测试网络的连通性。
同时采用不同网络环境中（不同网段或不同运营商）的电脑测试，判断是本地网络问题还是服务器端问题。

> **注意：**
> 请确保控制台安全组已开放 ICMP 协议。

 1. 开启“运行”对话框。本地电脑，快捷键【 Windows + R 】，输入【 cmd 】，回车打开命令提示符。
 
 2. 输入【Ping + 服务器公网 IP 地址】，回车。如：ping 139.199.XXX.XXX
 正常情况：
![](//mc.qcloudimg.com/static/img/9596963f31d642deb9417e0a7c0a4085/image.png)
 异常情况：（网络连接问题）
![](//mc.qcloudimg.com/static/img/d2f8d5dba402be0bab945cb01f9194a4/image.png)

 3. 测试远程端口开启情况。输入【telnet + 服务器公网 IP 地址 + 端口号】，回车。如：telnet 139.199.XXX.XXX 。
![](//mc.qcloudimg.com/static/img/e18be3704977545d5c952d3a583f2ccc/image.png)
 正常情况：黑屏，仅显示光标。
 异常情况：连接失败，如下图：
![](//mc.qcloudimg.com/static/img/4b3d0e492b8c005fb1a43bc0cbd1496c/image.png)

 4. 若网络出现问题则检查问题网络相应部分，若网络正常则进入 [步骤二](#F2) 筛查。


<span id = "F2"></span>
## 步骤二：检查远程桌面服务配置

>**注意：**
> - 请关闭防火墙或安全软件，再进行检查测试。
> - 请勿在 Windows 云服务器上安装个人 PC 类的杀毒软件，此类软件可能会封云服务器的远程登录端口，导致云服务器无法登录。

 1. 通过 [控制台](https://console.cloud.tencent.com/cvm) 登录云服务器。

 2. 在云服务器中，右键单击【我的电脑】- 单击【属性】-【高级系统设置】-【远程】，在 “远程桌面”功能块中点选【允许远程连接带此计算机】，单击【确定】。
![](//mc.qcloudimg.com/static/img/9d9e587e02ee10fbdffe861efd9bf3fd/image.png)

## 步骤三：检查远程桌面运行情况

 1. 登录云服务器，单击【开始】，单击【搜索(图标)】，输入【 cmd 】，回车打开管理员命令框。
![](//mc.qcloudimg.com/static/img/a4d38adde06ab471abf845e906c9bb06/image.png)

 2. 执行命令``` netstat -ant | findstr 3389 ```（默认情况下远程桌面服务端口号为 3389 ）：
正常情况：
![](//mc.qcloudimg.com/static/img/45484df01fb678058a23c2f2e122eee1/image.png)
异常情况：不显示任何连接。

有以下两种问题均会导致无法正常远程连接：
 -  远程桌面服务异常，请参照 [步骤四](#F4) 排查与解决。
 -  远程桌面端口异常，请参照 [步骤五](#F5) 排查与解决。

<span id = "F4"></span>
## 步骤四：检查远程桌面服务

 1. 在云服务器中，单击【开始】，单击【搜索(图标)】，输入【 services.msc 】，回车。
 > **注意：**
 > 若提示分辨率过低，请在桌面单击右键，单击【屏幕分辨率】，提高分辨率后再执行本操作。

 2. 找到 Remote Desktop Services ，右键单击，选择【重新启动】。
![](//mc.qcloudimg.com/static/img/973afc9859e44bb4ff6628abcb6f0ca1/image.png)

<span id = "F5"></span>
## 步骤五：检查远程端口

该步骤指导检查两处端口号，两处端口号必须一致。

 1. 在云服务器中，单击【开始】，单击【搜索(图标)】，输入【 regedit 】，回车。

 2. 依据左侧目录导航，依次打开目的地址：
【HKEY_LOCAL_MACHINE】-【SYSTEM】-【CurrentControlSet】-【Control】-【Terminal Server】-【Wds】-【rdpwd】-【Tds】-【tcp】
![](//mc.qcloudimg.com/static/img/089a6200b7c8b75260320d4ac71a4a3a/image.png)

 3. 查看并记录该处 PortNumber (端口号)，默认为 3389 。
 
 4. 再依据左侧目录导航，依次打开目的地址：
【HKEY_LOCAL_MACHINE】-【SYSTEM】-【CurrentControlSet】-【Control】-【Tenninal Server】-【WinStations】-【RDP-Tcp PortNumer】
![](//mc.qcloudimg.com/static/img/6269a1f4c7ff9eacf93f82a5ce21f4bd/image.png)

 5. 查看第二处 PortNumber (端口号)是否与上一目录查询结果一致。若出现不一致，需要根据 [步骤六](#F6) 修改远程端口。


<span id = "F6"></span>
## 步骤六：修改远程端口

>两种情况下需要修改远程端口：
>- 出现步骤五中端口号不一致的情况。
>- 出于安全考虑，需更换远程端口。


 1. 继续步骤五中操作，在左侧目录导航找到需要修改的端口，双击【 PortNumber 】。
![](//mc.qcloudimg.com/static/img/441fd60bbe057f0de4c1382ecfbe6d04/image.png)

 2. 点选 “十进制” ，将端口修改成 0~65535 之间未被占用端口即可。
![](//mc.qcloudimg.com/static/img/9902bc90e999f8d86f6733157258ba40/image.png)

 3. 重复以上操作修改第二处端口号，修改端口**两处需保持一致**。

 4. 修改完成，重启云服务器，即可正常远程登录。
 
