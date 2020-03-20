公网 IP 地址是 Internet 上的非保留地址，有公网 IP 地址的云服务器可以和 Internet 上的其他计算机互相访问。
腾讯云公网 IP 地址有两类，普通公网 IP 和弹性公网 IP（EIP），二者都可以为云服务器提供访问公网和被公网访问的能力。
- 普通公网 IP：仅能在云服务器购买时分配且无法与云服务器解绑，如购买时未分配，则无法获得。
- 弹性公网 IP（EIP）：可以独立购买和持有的公网 IP 地址资源，可随时与云服务器、NAT 网关等云资源绑定、解绑。

您可以将云服务器的普通公网 IP 转成 EIP，使其具备解绑和绑定的能力，实现公网 IP 的灵活使用。

## 操作说明
- 普通公网 IP 转成 EIP 前，请确保 EIP 总数未超过产品总配额，详情请参见 [配额限制](https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6)。
- 普通公网 IP 转成 EIP 过程中，不影响云服务器的访问公网和被公网访问的能力。
- 普通公网 IP 转成 EIP 后，并不会改变原有地址。	
- 普通公网 IP 转成 EIP 后，无法转换回普通公网 IP。
- 普通公网 IP 转成 EIP 后，保留原有公网网络计费模式。


## 操作步骤
您可根据如下操作步骤，将普通公网 IP 转成 EIP：
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。
2. 在实例管理页面，找到选择需转换的实例，单击对应的普通公网 IP 右侧的 <img src="https://main.qcloudimg.com/raw/25e8c0e37b73c12da900301f03e57dbc.png" style="margin: -3px;"></img>。
![](https://main.qcloudimg.com/raw/aee823ae6b8f5f977cb3c42549eaf090.png)
3. 在弹出的窗口中，单击【确定】即可。
![](https://main.qcloudimg.com/raw/29b368e16bcf388067be3f869ee3935a.png)
