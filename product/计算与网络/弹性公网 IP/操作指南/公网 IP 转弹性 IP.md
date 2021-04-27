您可以将云服务器的普通公网 IP 转换为弹性公网 IP（EIP），转换后，弹性公网 IP 具备随时与云服务器解绑和绑定的能力，更易于实现公网 IP 的灵活管理。
>?
>- 当前普通公网 IP 仅支持常规 BGP IP 线路类型。
>- 按带宽包年包月计费的公网 IP 暂不支持转换为 EIP，请先切换网络计费模式为按流量计费或带宽按小时后付费。
>

## 背景信息
公网 IP 地址是 Internet 上的非保留地址，有公网 IP 地址的云服务器可以和 Internet 上的其他计算机互相访问。
腾讯云公网 IP 地址有两类，普通公网 IP 和 EIP，二者都可以为云服务器提供访问公网和被公网访问的能力。
- 普通公网 IP：仅能在云服务器购买时分配且无法与云服务器解绑，如购买时未分配，则无法获得。
- EIP：可以独立购买和持有的公网 IP 地址资源，可随时与云服务器、NAT 网关等云资源绑定、解绑。

与云服务器的普通公网 IP 相比，EIP 提供更灵活的管理方式，如下表所示，详情请参见 <a href="https://cloud.tencent.com/document/product/215/38109#.E5.85.AC.E7.BD.91-ipv4-.E5.9C.B0.E5.9D.80">公网 IPv4 地址</a>。
<table>
<thead>
<tr>
<th>对比项</th>
<th>普通公网 IP</th>
<th>EIP</th>
</tr>
</thead>
<tbody><tr>
<td>访问公网/被公网访问</td>
<td>&#10003; </td>
<td>&#10003; </td>
</tr>
<tr>
<td>独立购买与持有</td>
<td>×</td>
<td>&#10003; </td>
</tr>
<tr>
<td>自由绑定与解绑</td>
<td>×</td>
<td>&#10003; </td>
</tr>
<tr>
<td>实时调整带宽</td>
<td>&#10003; </td>
<td>&#10003; </td>
</tr>
<tr>
<td>IP 资源占用费</td>
<td>×</td>
<td>&#10003; </td>
</tr>
</tbody></table>

## 操作说明
- 普通公网 IP 转成 EIP 前，请确保 EIP 总数未超过产品总配额，详情请参见 [配额限制](https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6)。
- 普通公网 IP 转成 EIP 过程中，不影响云服务器的访问公网和被公网访问的能力。
- 普通公网 IP 转成 EIP 后，并不会改变原有地址。	
- 普通公网 IP 转成 EIP 后，无法转换回普通公网 IP。
- 普通公网 IP 转成 EIP 后，保留原有公网网络计费模式，如转换前公网网络计费模式为按流量计费，转换后仍为按流量计费。


## 操作步骤
您可根据如下操作步骤，将普通公网 IP 转成 EIP：
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。
2. 在实例管理页面，选择需转换的实例所在地域，单击对应实例的普通公网 IP 右侧的 <img src="https://main.qcloudimg.com/raw/25e8c0e37b73c12da900301f03e57dbc.png" style="margin: -3px;"></img>。
![](https://main.qcloudimg.com/raw/aee823ae6b8f5f977cb3c42549eaf090.png)
3. 在弹出的“转换为弹性公网IP”窗口中，单击【确定】即可。
![](https://main.qcloudimg.com/raw/29b368e16bcf388067be3f869ee3935a.png)

## 后续步骤
- 若需要调整 EIP 的带宽峰值，请参见 [调整带宽](https://cloud.tencent.com/document/product/1199/41705)。
- 若需要监控 EIP 的流量波动情况，请参见 [查看监控数据](https://cloud.tencent.com/document/product/1199/42105)。
