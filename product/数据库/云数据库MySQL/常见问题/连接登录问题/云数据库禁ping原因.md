## 问题描述
为防止云数据库被 DDoS 攻击，MySQL 默认禁止使用 ping 命令来检查网络的连通性。

## 解决方案
建议您使用 telnet 命令来快速排查和定位网络连通性问题。

- **命令格式如下：**
```
telnet 内网/外网IP地址 内/外网端口
```

- **执行命令后网络访问情况如下**：
 - 网络访问正常的情况
![](https://main.qcloudimg.com/raw/b8f843fb18ca7091769a19962842ad0c.png)
 - 网络访问异常的情况
![](https://main.qcloudimg.com/raw/3d0fcb7f8e5f170e06b3c58077bf6531.png)

>?若使用 telnet 命令也无法连接，您可以通过 [连接检查工具](https://cloud.tencent.com/document/product/236/33206) 来协助您轻松排查内、外网的连接问题。



