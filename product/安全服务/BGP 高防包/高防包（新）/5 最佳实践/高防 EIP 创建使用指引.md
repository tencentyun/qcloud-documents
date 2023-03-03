
>?仅标准账号类型支持创建**高防 EIP**，若您无法确定账户类型，请参见 [弹性公网 IP-账户类型说明](https://cloud.tencent.com/document/product/1199/49090#judge)。


## 步骤一：购买企业版高防包
登录腾讯云官网，进入 [DDoS 高防包购买页](https://buy.cloud.tencent.com/antiddos#/native) 进行选购。更多详情请参见 [购买指引](https://cloud.tencent.com/document/product/1021/43894)。


## 步骤二：创建 BGP 带宽包
参考 [创建 IP 带宽包](https://cloud.tencent.com/document/product/684/39942) 文档，创建 BGP 带宽包。
>?如您在需要使用的地域已创建常规 BGP 带宽包 可跳过此步骤至 [步骤三](#S3)。

## 步骤三：创建高防 EIP[](id:S3)
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/ip?rid=1)，在左侧操作栏中，单击**公网 IP**。
2. 在公网  IP 页面，选择地域，单击**申请**。
![](https://qcloudimg.tencent-cloud.cn/raw/fb4b6d38cb0c3d1ce2f5b3988d3e6255.png)
3. 在申请 EIP 窗口中，配置相关参数，单击**确定**，完成 EIP 的申请。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/35a6b94661a18b31d2a92b7eb2eea57d.png" width=600px>
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>IP 地址类型</td>
<td>选择<strong>高防 EIP</strong></td>
</tr>
<tr>
<td>计费模式</td>
<td>无需选择，高防 EIP 仅支持共享带宽包计费模式</td>
</tr>
<tr>
<td>共享带宽包</td>
<td>选择需要加入的<strong>常规 BGP 共享带宽包</strong></td>
</tr>
<tr>
<td>带宽上限</td>
<td>请按需设置带宽上限，合理分配带宽资源</td>
</tr>
<tr>
<td>企业版高防包</td>
<td>选择需要绑定的<strong>企业版高防包</strong></td>
</tr>
<tr>
<td>数量</td>
<td>请按需选择申请的数量且确保 EIP 总数未超过产品总配额，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">限额配置-使用限制</a></td>
</tr>
<tr>
<td>名称</td>
<td>EIP 实例名称，非必填</td>
</tr>
<tr>
<td>标签</td>
<td>如需添加标签可在此进行添加，可通过标签进行权限管理</td>
</tr>
</tbody></table>

## 后续操作
若需要为 EIP 绑定云资源，请参见 [弹性公网 IP-EIP 绑定云资源](https://cloud.tencent.com/document/product/1199/41702)。
