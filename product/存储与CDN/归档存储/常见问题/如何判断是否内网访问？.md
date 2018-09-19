在相同地域内，腾讯云产品相互访问，将会自动使用内网连接。因此选购云产品或进行 API 操作时，建议尽量选择相同地域，以减少您的外网流量费用。

下面以云服务器 CVM 访问 CAS 为例，判断是否使用内网访问归档存储 CAS，可以在 CVM 上 使用 `nslookup` 命令解析在归档存储上创建的文件库请求地址，若返回内网 IP，则表明 CVM 和 CAS 之间是内网访问，否则为外网访问。
内网 IP 地址一般形如 `10.*.*.*`、`100.*.*.*` 。VPC 网络一般为 `169.*.*.*` 等。
假设 `cas.ap-chengdu.myqcloud.com` 为文件库的请求地址，其下方的 `Address: 10.148.214.13` 表示从内网访问。

```
nslookup cas.ap-chengdu.myqcloud.com

Server:         10.138.224.65
Address:        10.138.224.65#53

Name:   cas.ap-chengdu.myqcloud.com
Address: 10.148.214.13
Name:   cas.ap-chengdu.myqcloud.com
Address: 10.148.214.14
```
