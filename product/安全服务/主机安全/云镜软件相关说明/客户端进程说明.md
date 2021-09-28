
|名称 | Windows 系统 | Linux 系统 |
|---------|---------|---------|
| 程序安装目录  | C:\program files\qcloud\yunjing\ydeyes <br>C:\program files\qcloud\yunjing\ydlive  | /usr/local/qcloud/YunJing/  |
| 进程名称   | YDService.exe <br>YDLive.exe <br>YDEdr.exe  | YDService <br>YDLive<br>YDEdr |
| 注册服务名称   | YDService <br>YDLive<br>YDEdr   |       -   |

客户端程序所占用端口是系统随机返回的，无固定端口范围，若占用端口与用户业务端口冲突，重启客户端程序即可。
- 客户端重启命令（Linux系统）
 1. 暂停客户端程序服务
```
/usr/local/qcloud/YunJing/stopYDCore.sh 
```
 2. 重新启动客户端
```
/usr/local/qcloud/YunJing/startYD.sh
```
- 客户端重启命令（Windows系统）
输入以下命令，或打开任务管理器的服务，找到 YDService 服务，右键重启。
 1. 暂停客户端程序服务
```
net stop YDService
```
 2. 重新启动客户端
```
net  start YDService
```

