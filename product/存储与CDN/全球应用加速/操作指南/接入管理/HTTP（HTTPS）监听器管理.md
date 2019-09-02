## 新增HTTP/HTTPS 监听器
1. 登录 [全球应用加速控制台](https://console.cloud.tencent.com/gaap)，进入“接入管理”页面，单击指定通道的【ID/通道名】。
2. 进入到下一级页面，选择【HTTP 监听器管理】/【HTTPS 监听器管理】>【新增】，可选的协议有 HTTP 和 HTTPS，具体配置如下：
 - 当选中 HTTP 时，仅需要输入端口即可，监听器会默认按照 HTTP 协议进行转发。
 ![](https://main.qcloudimg.com/raw/df272654d597b8d63358d0fc075f6864.png)
 - 当选中 HTTPS 时，则需要额外配置证书和其他信息，如下图：
![](https://main.qcloudimg.com/raw/a31070a0115e979ad3397f400b2d875b.png)
 - “监听器与源站之间使用 HTTP 协议”，指客户端到加速通道 VIP 之间使用 HTTPS 协议，而 VIP 到源站之间使用 HTTP 协议，需要源站开通HTTP协议端口；“监听器与源站之间使用 HTTPS 协议”，指客户端到源站之间全程使用 HTTPS 协议，需要源站开通 HTTPS 协议端口。二者的主要区别在于，前者的链路延迟会更低。
 - **SSL 解析方式**：目前只支持单向认证，即客户端认证服务器。
 - **服务器证书**：需要在腾讯云的【SSL证书管理】产品中购买或上传，然后从下拉列表中选择对应的证书。

## 设置HTTP/HTTPS 监听器
单击【HTTP/HTTPS 监听器管理】标签页，在操作栏单击【设置】，可以进入下一级页面，进行域名和 URL 管理。
<span id ="添加规则">
### 添加规则</span>
在“HTTP/HTTPS 监听器管理”，单击【添加规则】，可以添加域名和对应的 URL，同一个域名下可以添加最多20条 URL 规则，具体如下：
1. 基本配置
![](https://main.qcloudimg.com/raw/b3cb374125b39dfb3584b241f4e96af4.png)
**域名**：需要精确匹配，支持的字符集有：`a-z`、`0-9`、` _`、` .`、` –`，长度3 - 80。
**URL**：支持字符集如下，`a-z`、` A-Z`、`0-9`、`_` 、`.`、`-` 、`/`，长度1 - 80。
**源站类型**：支持 IP 和域名两种类型的源站，两种类型的区别同 TCP/UDP 监听器说明。

2. 源站处理策略
设置源站的转发处理规则，支持轮询、轮询加权和最小连接数，具体策略的说明同 TCP/UDP 监听器说明。
![](https://main.qcloudimg.com/raw/292d45db29f3ee3c991dacf5860e3868.png)
3. 源站健康检查机制
可以启用监控检查机制，针对当前域名，可以设置独立的 检查 URL，请求方式可以支持 HEAD 和 GET，检查状态码可以支持 http_1xx，http_2xx，http_3xx，http_4xx，http_5xx，可单选也可多选，即当检测到指定的状态码时，监听器认为后端源站属于正常状态，如果未检测到任何状态码时，监听器认为后端源站异常。
![](https://main.qcloudimg.com/raw/576a01ceb4a8eb66a31ca5c9506c6218.png)

### 修改域名
在“HTTP/HTTPS 监听器管理”页面的操作栏，单击【修改域名】，可以对域名进行修改，如下图：
![](https://main.qcloudimg.com/raw/4a87419818656d855b2d431933cbff9e.png)

### 删除域名
删除域名时，如果域名下有规则已经绑定源站，则需要勾选“强制删除绑定有源站的规则”。
![](https://main.qcloudimg.com/raw/50987ba13431db15c467acfed88a3319.png)

### 修改规则
参考上文 [添加规则](#添加规则)，主要差别在于域名和源站类型无法修改。

### 绑定源站
详情请参见 [绑定源站](https://cloud.tencent.com/document/product/608/17849#.E7.AC.AC.E5.9B.9B.E6.AD.A5.EF.BC.9A.E7.BB.91.E5.AE.9A.E6.BA.90.E7.AB.99)，可以对不同源站绑定不同的端口。

### 删除规则
如果规则下有绑定的源站，需要先勾选“强制删除绑定有源站的规则”。
![](https://main.qcloudimg.com/raw/f0db28068f2f1d231af4f47db9ce124d.png)

## 删除HTTP/HTTPS 监听器
单击【HTTP/HTTPS 监听器管理】标签页，单击【删除】，可以删除指定的监听器，若监听器已绑定源站，则需要选中“允许强制删除绑定有源站的监听器”后，才能删除。删除后，该监听器的端口将停止加速。
![](https://main.qcloudimg.com/raw/2bd55dcafc2ffeb68dc70b937eb5e72a.png)

## 修改HTTP/HTTPS 监听器
单击【HTTP/HTTPS 监听器管理】标签页，单击【修改】，可修改监听器信息。
- HTTP 监听器：支持修改监听器的名称，如下图：
![](https://main.qcloudimg.com/raw/1ac967c0a3058762589de1dbdad81286.png)
- HTTPS 监听器：支持修改名称，监听器与源站之间协议，以及更新证书，如下图：
![](https://main.qcloudimg.com/raw/27471026ad23fcd3c86b1417ac0ecd66.png)
