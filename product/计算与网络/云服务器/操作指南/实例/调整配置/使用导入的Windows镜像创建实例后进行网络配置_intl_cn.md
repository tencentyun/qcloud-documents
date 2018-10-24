导入Windows类型镜像并创建云服务器后，用户请通过[控制台云服务器列表](https://console.cloud.tencent.com/cvm)后的【登录】按钮登录刚创建的云服务器并进行网络配置。

Windows机器网络配置信息保存在文件`C:\qcloud-network-config.ini`中，打开该配置文件，结构如下：

```
[ip]
ip= x.x.x.x
mask = x.x.x.x
gateway = x.x.x.x
 
[dns]
dns = x.x.x.x
```

请根据此配置文件信息修改网络
