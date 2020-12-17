## 问题描述
为防止云数据库被 DDoS 攻击，默认禁止使用 ping 命令来检查 MySQL 内网地址的网络连通性。
>?外网地址可使用 ping 命令检查网络连通性。


## 解决方案
建议您使用 telnet 命令来快速排查和定位网络连通性问题。

- **命令格式如下：**
```
telnet 内网/外网IP地址 内/外网端口
```

- **执行命令后网络访问情况如下**：
 - 网络访问正常的情况
![](https://main.qcloudimg.com/raw/576f29ab50c2b8c347514a59242a7ae9.png)
 - 网络访问异常的情况
![](https://main.qcloudimg.com/raw/76ce15542eb5278ad2c4e1f58c80f4db.png)

>?若使用 telnet 命令也无法连接，您可以通过 [连接检查工具](https://cloud.tencent.com/document/product/236/33206) 来协助您轻松排查内、外网的连接问题。


