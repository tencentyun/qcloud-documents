## COSFS 工具相关
#### 1. 如何挂载目录？
在挂载命令的时候，可以指定目录，如：
```
 cosfs appid:my-bucket:/my-dir /tmp/cosfs -ourl=http://cn-south.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```
>  <font color="#0000cc">**注意：** </font>
my-dir 必须以“ / ”开头。

####  2. 为什么之前可用写文件，突然不能写了？
由于 COS 鉴权产品策略调整，所以老版本的 COSFS 工具会导致策略校验不过，因此需要拉取最新的 COSFS 工具重新 mount。

#### 3. 使用 COSFS 工具过程中，遇到 Input/Output ERROR 等错误，该如何调试？
请先按照以下步骤依次检查，确认问题。
1. 请检查机器是否能正常访问 COS 的域名；
2. 检查账号是否配置正确。

确认以上配置正确，请打开机器 `/var/log/messages`日志文件，找到 s3fs 相关的日志，日志可以帮助您定位问题原因。如果无法解决，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云技术支持，协助您解决问题。

#### 4. 挂载后，如何能让机器上其他账户来访问我挂载的目录？
如果要开放权限，需要在挂载的时候，指定 -oallow_other。

#### 5. Ubuntu 如何打开 syslog 查看 COSFS 工具的日志？
以 **root** 身份打开`/etc/rsyslog.d/50-default.conf`文件，将以下代码的行首 # 注释符号删除：
```
     #.=info;.=notice;*.=warn;
     # auth,authpriv.none;
     # cron,daemon.none;
     # mail,news.none -/var/log/messages
```
重启 rsyslog 服务： 
```
service rsyslog restart
```  
查看 `cat /var/log/messages`文件中 COSFS 的异常日志。
