## 操作场景
云数据库 Redis 目前支持外网地址的地域：成都、北京、上海、广州，其他地域如需外网访问，可以通过具备外网 IP 的云服务器 CVM 进行端口转发，来实现外网访问 Redis 实例。
>?iptable 转发的方式存在稳定性风险，不建议在生产环境使用外网接入。
>
![](https://main.qcloudimg.com/raw/7bad7f6f7ca82c8655f807d2036d983b.png)

## 操作步骤
1. 登录 [云服务器](https://cloud.tencent.com/document/product/213/5436)，开通云服务器 IP 转发功能。
>?云服务器和数据库须是同一账号，且同一个 VPC 内（保障同一个地域），或同在基础网络内。
>
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```
2. 配置转发规则，如下示例是将26.xx.x.2:10001（云服务器外网地址，端口可自行选择）的访问转发至内网为10.0.0.5:6379的 Redis 实例。
```
iptables -t nat -A PREROUTING -p tcp --dport 10001 -j DNAT --to-destination 10.0.0.5:6379
iptables -t nat -A POSTROUTING -d 10.0.0.5 -p tcp --dport 6379 -j MASQUERADE
```
3. 配置 [云服务器安全组](https://cloud.tencent.com/document/product/213/39740)，放开云服务器外网端口的访问权限，安全组规则建议仅放开需要访问的源地址。
4. 在访问端通过外网地址（本示例即26.xx.xx.2:10001）连接内网 Redis 实例，连接命令与内网连接命令一致，命令请参见 [通过客户端工具连接](https://cloud.tencent.com/document/product/239/30877)。
5. 连接 Redis 后，执行`info`命令返回数据库相关信息即表示连接成功。

