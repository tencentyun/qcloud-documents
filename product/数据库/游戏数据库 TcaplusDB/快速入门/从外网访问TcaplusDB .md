## 操作场景
游戏数据库 TcaplusDB 暂时不支持外网访问，您可以通过具备外网 IP 的云服务器 CVM 进行端口转发，来实现外网访问 TcaplusDB。
>?iptable 转发的方式存在稳定性风险，不建议在生产环境使用外网接入。
>
![](https://main.qcloudimg.com/raw/8a5ed2e2527a5d50ca2b0deda2ce0908.png)
![](https://main.qcloudimg.com/raw/45192ccfd85eaebbe35223258191ed73.png)

## 操作步骤
1. 登录 [云服务器](https://cloud.tencent.com/document/product/213/5436)，开通云服务器 IP 转发功能。
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```
2. 配置转发规则，如下示例是将26.xx.x.2:6379的访问转发至内网为10.0.0.5:6379的 TcaplusDB。
>?本示例中，云服务器外网地址为26.xx.x.2:6379，TcaplusDB 内网地址为10.0.0.5:6379。
>
```
iptables -t nat -A PREROUTING -p tcp --dport 6379 -j DNAT --to-destination 10.0.0.5:6379
iptables -t nat -A POSTROUTING -d 10.0.0.5 -p tcp --dport 6379 -j MASQUERADE
```
3. 配置 [云服务器安全组](https://cloud.tencent.com/document/product/213/18197)，放开云服务器外网端口的访问权限，安全组规则建议仅放开需要访问的源地址。
4. 通过26.xx.xx.2:6379即可连接访问内网 TcaplusDB。

