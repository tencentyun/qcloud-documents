## 操作场景
本文档以 WooCommerce 6.8.2 应用镜像为例，由于镜像间的差异，设置 HTTPS 的路径可能有所不同。

## 操作步骤
1. 登录轻量应用服务器控制台，选择左侧导航栏中的服务器。
2. 在实例列表中，选择目标实例并进入实例详情页。
3. 选择应用管理页签，在应用软件安装地址卡片中找到当前实例中 Web Server 的安装路径。

 <img style="width:700px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/9c42b61cc8b560051500335aaff8167b.png" />

4. 登录服务器，进入步骤3中获取到的路径，并找到 Web Server 应用安装的目录。
5. 在应用安装目录下找到 `主机名.conf` 的文件。

<dx-alert infotype="notice" title="">
也可以用“`cd /`”命令进入根目录进行搜索 `find . -name "您的主机名.conf"`。
</dx-alert>


6. 删除该文件。
```plaintext
rm -f 搜索到的文件路径
 ```
 
7. 重启 Nginx。
```plaintext
sudo systemctl reload nginx
```


