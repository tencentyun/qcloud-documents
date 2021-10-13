弹性公网 IP 支持针对 FTP 和 SIP 协议设置 ALG 功能。开启 ALG 功能后，则可对指定协议的应用层数据载荷进行 NAT 穿透。

>? 该功能目前处于内测中，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/7a8h6lgesmg)。


## 背景信息
通常情况下 NAT 只对报头中的 IP、PORT 信息进行转换，不对应用层数据载荷中的字段进行分析。一些应用层协议像 FTP、H323 等多通道协议及流媒体 RTSP、MMS，还有 DNS、SMTP，和一些 IM 和 P2P，一般情况下在应用载荷信息之中会包括一些地址、端口信息，如果这些信息不被转换就会造成通信的失败。

ALG（Application Layer Gateway，应用层网关）是由一个扩增防火墙或计算机网络应用或 NAT 平安部件组成的一类防火墙。ALG 主要完成了对应用层报文的处理，如果开启了 ALG，则在识别了相应报文之后便会对 IP 报头以外的载荷信息进行解析，然后进行地址转换，重新计算校验和。

## 限制说明
- 目前仅支持 FTP 和 SIP 协议设置 ALG 功能。
- 目前仅弹性公网 IP 支持设置 ALG 功能，弹性公网 IPv6 不支持。
- 有部分集群机型不支持设置 ALG 功能，如需使用，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=660&source=0&data_title=%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91%20EIP&level3_id=662&queue=96&scene_code=16400&step=2)。


## 操作步骤
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在“弹性公网 IP”页面左上角选择**地域**。
3. 在弹性公网 IP 列表中选中目标实例，在右侧“操作”列选择**更多 > 设置 ALG**。
4. 在弹出的“设置 ALG”对话框中，设置针对 FTP、SIP 协议开启或关闭 ALG 功能。
>? 默认情况下，ALG 处于开启状态。
5. 设置完成后，单击**确认**。
