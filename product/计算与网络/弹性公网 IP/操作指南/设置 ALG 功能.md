弹性公网 IP 支持针对 FTP 和 SIP 协议设置 ALG 功能。开启 ALG 功能后，则可对指定协议的应用层数据载荷进行 NAT 穿透。
>?该功能目前处于内测中，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/7a8h6lgesmg)。
>


## 背景信息
通常情况下 NAT 只对报头中的 IP、PORT 信息进行转换，不对应用层数据载荷中的字段进行分析。一些应用层协议像 FTP、H323 等多通道协议及流媒体 RTSP、MMS，还有 DNS、SMTP，和一些 IM 和 P2P，一般情况下在应用载荷信息之中会包括一些地址、端口信息，如果这些信息不被转换就会造成通信的失败。

ALG（Application Layer Gateway，应用层网关）是由一个扩增防火墙或计算机网络应用或 NAT 平安部件组成的一类防火墙。ALG 主要完成了对应用层报文的处理，如果开启了 ALG，则在识别了相应报文之后便会对 IP 报头以外的载荷信息进行解析，然后进行地址转换，重新计算校验和。

## 限制说明
- 目前仅支持 FTP 和 SIP 协议设置 ALG 功能。
- 目前仅 EIP 和普通公网 IP 支持设置 ALG 功能，弹性公网 IPv6 不支持。
- 以下部分集群机型不支持设置 ALG 功能，如需使用，请 [联系我们](https://cloud.tencent.com/document/product/1199/59721)。
<table>
<tbody>
<tr>
<th>云服务器实例类型</th>
<th>机型</th>
</tr>
<tr>
<td>标准型</td>
<td>标准型 S5</td>
</tr>
<tr>
<td rowspan="6">黑石物理服务器2.0</td>
<td>标准型 BMS4</td>
</tr>
<tr>
<td>高 IO 型 BMI5</td>
</tr>
<tr>
<td>大数据型 BMD3</td>
</tr>
<tr>
<td>大数据型 BMD2</td>
</tr>
<tr>		<td>GPU 型 BMG5t</td>
</tr>
<tr>
<td>GPU 型 BMG5v</td>
</tr>
<tr>
<td>高性能计算集群</td>
<td>GPU 型 HCCG5v</td>
</tr>
</tbody>
</table>


## 操作步骤
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在“公网 IP”页面顶部选择**地域**。
3. 在公网 IP 列表中选中目标实例，在右侧“操作”列选择**更多** > **设置 ALG**。
4. 在弹出的“设置 ALG”对话框中，设置针对 FTP、SIP 协议开启或关闭 ALG 功能。
>? 默认情况下，ALG 处于开启状态。
>
<img src="https://main.qcloudimg.com/raw/a1744b563b8086c71d11e3a89779e3e0.png" width="70%">
5. 设置完成后，单击**确认**。
