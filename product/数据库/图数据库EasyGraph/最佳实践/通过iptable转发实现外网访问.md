## 操作场景
图数据库 KonisGraph 暂时不支持直接通过外网访问，您可以通过具备外网 IP 的云服务器 CVM 进行端口转发，来实现外网访问 KonisGraph 实例。

>?iptable 转发的方式存在稳定性风险，不建议在生产环境使用外网接入。

![](https://qcloudimg.tencent-cloud.cn/raw/248e7cda24ed6116170acc962304c6de.png)

## 操作步骤
1. 登录 [云服务器](https://cloud.tencent.com/document/product/213/5436)，开通云服务器 IP 转发功能。
>?云服务器和数据库须是同一腾讯云账号，且同一个 VPC 内（保障同一个地域）。
>
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```
2. 配置转发规则，如下示例是将26.xx.x.2:10001（云服务器外网地址，端口可自行选择）的访问转发至内网为10.x.x.5:8186的 KonisGraph 实例。
```
iptables -t nat -A PREROUTING -p tcp --dport 10001 -j DNAT --to-destination 10.x.x.5:8186
iptables -t nat -A POSTROUTING -d 10.x.x.5 -p tcp --dport 8186 -j MASQUERADE
```
3. 配置 [云服务器安全组](https://cloud.tencent.com/document/product/213/39740)，放开云服务器外网端口的访问权限，安全组规则建议仅放开需要访问的源地址。
4. 在访问端，通过外网地址（本示例即26.xx.xx.2:10001）连接内网 KonisGraph 实例，连接方式与内网连接一致，请参见 [连接 KonisGraph 实例](https://cloud.tencent.com/document/product/1366/61174)。
