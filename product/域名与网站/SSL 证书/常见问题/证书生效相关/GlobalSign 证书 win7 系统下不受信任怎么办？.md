## 背景
2019年5月27日，GlobalSign 正式使用新的中级 CA 为 SSL 证书产品签名。因 Windows 7 系统中没有新根支持，致使 Windows 7 系统访问2019年5月27日之后签发（包括更新或者重颁发的证书）的 GlobalSign 证书时，网站不受信任。详情可查看：[关于 GlobalSign 迁移签发 SSL 证书的中级 CA 的通知](https://www.globalsign.cn/news/1081.shtml)。

## 解决办法
请使用文本编辑器，打开已下载证书中 Nginx 目录下的 .crt 文件，将以下交叉证书复制粘贴放置于证书链最后位置。重启 Nginx 服务，证书即可正常使用。
**交叉证书下载请** [单击此处](https://da.do/t6za)。
