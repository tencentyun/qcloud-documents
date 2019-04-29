## 获取实例的内网 IP 地址
### 使用控制台获取
1. 登录 [云服务器控制台]( https://console.cloud.tencent.com/cvm/) 。
2. 云服务器列表中列出了您名下的实例，鼠标移动到云服务器的内网 IP 后，出现复制按钮，单击即可复制内网 IP 。
![](//mc.qcloudimg.com/static/img/2663aabcbe44c2ad372b5b8ba2bb6a1f/image.png)

### 使用 API 获取
请参考 [DescribeInstances 接口](/document/product/213/15728) 。

### 使用实例元数据获取
1. 登录云服务器实例。具体登录方法参考 [登录 Linux 实例](/doc/product/213/5436) 和 [登录 Windows 实例](/doc/product/213/5435)。
2. 输入命令：
```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
```
返回值有类似如下结构，即可查看到内网 IP 地址：
![](//mc.qcloudimg.com/static/img/14a13eccebc7eee6f83bc026adb30902/image.png)
有关更多信息，请参阅 [查看实例元数据](/doc/product/213/4934)。

## 设置内网 DNS 
当网络解析出现错误时，用户可以手动进行内网 DNS 设置。设置方法如下：
### Linux 系统
在云服务器上，通过编辑 `/etc/resolv.conf` 文件，修改云服务器 DNS 。
运行命令 ，根据 [内网 DNS ](https://cloud.tencent.com/document/product/213/5225#.E5.86.85.E7.BD.91-dns) 列表中对应的不同地域编辑修改 DNS IP。
```
vi /etc/resolv.conf
```
![](//mc.qcloudimg.com/static/img/9c46100760f1049454b076a3c83c7f8a/image.png)

### Windows 系统
在云服务器上，打开【控制面板】>【网络和共享中心】>【更改适配器设备】，右键单击以太网【属性】，双击【Internet 协议版本4】，修改 DNS 服务器 IP 。
![](//mc.qcloudimg.com/static/img/93b7bda1075530ff6e7ba5ece4ab71f4/image.png)
