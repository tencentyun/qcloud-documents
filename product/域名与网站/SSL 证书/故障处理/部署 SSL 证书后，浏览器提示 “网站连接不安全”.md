## 现象描述
部署 SSL 证书后，使用 HTTPS 协议访问网站，浏览器地址栏中域名前显示<span ><img src="https://main.qcloudimg.com/raw/fd19301d82877dddfb19dbba29366b17.png" style="margin-bottom:-5px;"/></span>图标和 “不安全” 字样。单击<span ><img src="https://main.qcloudimg.com/raw/fd19301d82877dddfb19dbba29366b17.png" style="margin-bottom:-5px;"/></span>，将提示红字警告 “你与此网站之间建立的连接不安全”。如下图所示：
![](https://main.qcloudimg.com/raw/d0e139c4326a84444ab6fd2a68170440.png)

## 可能原因
- **SSL 证书过期**：为了确保私钥安全，SSL 证书均存在有效期限，最新的国际标准 SSL 证书最长有效期为1年。如 SSL 证书过了有效期，没有及时替换新证书，网站会出现红色 “不安全” 警告。
- **网页存在不安全因素**：网站已经部署 SSL 证书，但是网页中调用了非 HTTPS 的外部资源（图片或 js）时，网站会存在不安全因素，对这类情况，网站浏览器也会标记 “你与此网站之间建立的连接不安全”，如果用户选择加载不安全内容，浏览器就会升级为红色 “不安全” 警告。


## 解决办法
### SSL 证书过期
请尽快替换已过期 SSL 证书，重新申请新证书并安装部署至网站服务器上，您可以参考以下文档进行操作：
1. [SSL 证书申请流程](https://cloud.tencent.com/document/product/400/43473)
2. [如何选择 SSL 证书安装部署类型？](https://cloud.tencent.com/document/product/400/4143)
 

### 网页存在不安全因素
可以将外链复制到 URL 中，并通过在 http 后添加 “s” 进行访问，测试此外链是否支持 https 协议的链接。
- 若可以访问，请直接在代码中修改 http 为 https 的链接。
- 若不可以访问，则可以下载该资源到本地服务器上，并修改资源路径指向到服务器上，并使用相对路径如 `image/button.gif` 或者完整的 https 路径如 `https://***/image/button.gif`。


