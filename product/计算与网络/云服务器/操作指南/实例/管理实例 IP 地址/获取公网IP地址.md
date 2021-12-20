## 操作场景
本文档指导您通过控制台、API，以及实例元数据获取公网 IP。

## 操作步骤
<dx-tabs>
::: 使用控制台获取
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/)。
2. 在实例的管理页面，鼠标移动至主 IP 地址列，出现 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin: -3px 0px;"></img>。如下图所示：
![](https://main.qcloudimg.com/raw/7f184b52a3311b4d3cc45b810bbda04f.png)
3. 单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin: 0;"/>，即可复制该 IP 地址。	
<dx-alert infotype="notice" title="">
由于公网 IP 地址通过 NAT 映射到内网 IP 地址，因此，您如果在实例内部查看网络接口的属性（例如通过 `ifconfig (Linux)` 或 `ipconfig (Windows)` 命令），将不会显示公网 IP 地址。如需从实例内部确定实例的公网 IP 地址，可参考 [使用实例元数据获取](#jump)。
</dx-alert>


:::
::: 使用\sAPI\s获取
请参考 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 相关接口。
:::
::: 使用实例元数据获取[](id:jump)
1. 登录云服务器实例。
具体登录方法参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/16515) 和 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/35697)。
2. 通过 cURL 工具或是 HTTP 的 GET 请求访问 metadata，获取公网 IP 地址。
```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
``` 返回值有类似如下结构，即可查看到公网 IP 地址：
![](https://main.qcloudimg.com/raw/03f603e433b7a5da09e33a8b09d731b4.png)
有关更多信息，请参阅 [查看实例元数据](https://cloud.tencent.com/document/product/213/4934)。
:::
</dx-tabs>
