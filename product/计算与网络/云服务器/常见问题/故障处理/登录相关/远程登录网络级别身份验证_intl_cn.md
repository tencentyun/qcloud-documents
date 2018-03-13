使用 Windows 系统自带远程桌面连接，有时出现无法连接到远程计算机的问题。本文档介绍该情况的解决方案。

 1. 打开注册表编辑器。在远程登录计算机，单击【开始】，运行里输入【regedit】回车。

 2. 进入 Security Packages 编辑框。依据路径进入 `HKEY_LOCAL_MACHINE＼SYSTEM＼CurrentControlSet＼Control＼Lsa`，双击右边栏中的【Security Packages】，打开【编辑多字符串】对话框，在列表框光标处增加【tspkg】字符。
![](//mc.qcloudimg.com/static/img/418c09b8bd7017fb16d55c30c712baac/image.png)
![](//mc.qcloudimg.com/static/img/5816749e6cdf88573f409e032443d613/image.png)

 3. 进入 SecurityProviders 编辑框。再依据路径进入到 `HKEY_LOCAL_MACHINE＼SYSTEM＼CurrentControlSet＼Control＼SecurityProviders`，双击右侧的【SecurityProviders】字符串，打开【编辑字符串】对话框，在数值末端中添加【, credssp.dll】（逗号后有一个英文空格）。
![](//mc.qcloudimg.com/static/img/edd5196a4232c0677dc9865931f8ec91/image.png)

 4. 退出注册表程序，重启计算机后故障排除，可进行远程登录。



