## Nginx HTTPS 双向认证配置流程

以第三方开发者域名 `http://www.example.com` 为例，有如下两种情况：

- **第三方开发者已有权威第三方签发的证书**
 - 开发者准备权威第三方为 `www.example.com` 签发的证书 `www.example.com.crt` 和派发的私钥 `www.example.com.key`，注意必须是权威的第三方机构（如天威、globalsign 等）签发的证书。
 - 即时通信 IM 给开发者后台提供用于验证请求方（即时通信 IM）证书的 CA 证书 [TencentQQAuthCA.crt](http://share.weiyun.com/7d86303625fda66998bcc46f79320503)。
 - 参照下文 Nginx HTTPS 双向认证配置参考进行配置。

- **第三方开发者向即时通信 IM 申请为域名签发证书**
 - 开发者向即时通信 IM 提供开发者后台域名，例如`www.example.com`。
 - 即时通信 IM 给开发者后台域名`www.example.com`签发证书和私钥，`www.example.com.crt`和 `www.example.com.key`。
 - 即时通信 IM 给开发者后台提供用于验证请求方（即时通信 IM）证书的 CA 证书 [TencentQQAuthCA.crt](http://share.weiyun.com/7d86303625fda66998bcc46f79320503)。
 - 参照下文 Nginx HTTPS 双向认证配置参考进行配置。

## Nginx HTTPS 双向认证配置参考

1. 将 `www.example.com.crt`、`www.example.com.key` 和 `TencentQQAuthCA.crt` 拷贝到 Nginx 的安装目录的 conf 文件夹下。
2. 修改 **nginx.conf** 配置文件，参考配置如下。
```
server {
    listen 443 ssl;
    ssl_protocols TLSv1 TLSv1.1;
    server_name            www.example.com; # 域名
    ssl_certificate        www.example.com.crt; # 腾讯给第三方签发的证书
    ssl_certificate_key    www.example.com.key; # 和证书配对的私钥
    ssl_verify_client on; # 验证请求来源
    ssl_client_certificate TencentQQAuthCA.crt; # 腾讯认证的 CA 证书
    location / {
        root   html;
        index  index.html index.htm;
    }
}
```
