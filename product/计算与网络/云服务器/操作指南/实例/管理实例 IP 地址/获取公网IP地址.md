## 使用控制台获取
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/) 。
2. 云服务器列表中列出了您名下的实例，鼠标移动到云服务器的公网 IP 后，出现复制按钮，单击即可复制该 IP 地址。
  ![](//mc.qcloudimg.com/static/img/be0c50402332ca78c347f372f7c54eef/image.png)
> **注意：**
> 公网 IP 地址通过 NAT 映射到内网 IP 地址。因此，如果在实例内部查看网络接口的属性（例如，通过 `ifconfig (Linux)` 或 `ipconfig (Windows)` 命令），则不会显示公网 IP 地址。要从实例内部确定实例的公网 IP 地址，可以参考 [使用实例元数据获取公网 IP 地址](#jump) 。

## 使用 API 获取
请参考 [查看实例列表](/document/product/213/15728) 相关接口。

<span id = "jump">  </span>
## 使用实例元数据获取
1. 登录云服务器实例。具体登录方法参考 [登录 Linux 实例](/doc/product/213/5436) 和 [登录 Windows 实例](/doc/product/213/5435) 。
2. 输入命令：
```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```
返回值有类似如下结构，即可查看到公网 IP 地址：
![](//mccdn.qcloud.com/img56a1f015c48e5.png)
有关更多信息，请参阅 [查看实例元数据](/doc/product/213/4934) 。