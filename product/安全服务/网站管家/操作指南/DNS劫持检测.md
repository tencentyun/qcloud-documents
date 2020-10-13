## 功能简介 
DNS 劫持检测功能可用于检测域名是否被劫持，并且能实时监测劫持区域分布、劫持用户数量和劫持后的 IP 地址。

## 配置示例
#### 保护网站主页不被篡改
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia
)，在左侧导航栏中，选择【Web 安全检测】>【DNS 劫持检测】，进入 DNS 劫持检测页面，单击【基础设置】。
 ![](https://main.qcloudimg.com/raw/29057745ae5684c02c1f09f23ab9955e.png)
2. 单击【添加域名】，弹出域名信息填写窗口。 输入待检测的域名及域名对应的权威 IP 地址，单击【添加】即可。若有多个权威 IP 地址，请单击【+添加一行】进行添加。
>?权威 IP 地址一般指 VIP 地址，您可在 Web 应用防火墙控制台的 [防护配置](https://console.cloud.tencent.com/guanjia/waf/config) 中查看 VIP 地址 。
>
 ![](https://main.qcloudimg.com/raw/cb85a0fd66a915c6aa1a55be53566501.png)
3. DNS 劫持检测配置成功，基础配置页面显示域名相关记录。
![](https://main.qcloudimg.com/raw/1803a7822cc6d285b77b2152044ba883.png)   

<a href="https://cloud.tencent.com/document/product/627/11709">下一步：CC 防护设置</a>
