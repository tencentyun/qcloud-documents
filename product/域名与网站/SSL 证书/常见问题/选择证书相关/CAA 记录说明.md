## 什么是 CAA？

CAA（Certification Authority Authorization，证书颁发机构授权）是一项降低 SSL 证书错误颁发的控制措施，由互联网工程任务组（IETF）批准列为 [IETF RFC6844](https://datatracker.ietf.org/doc/html/rfc6844) 规范。2017年3月，CA 浏览器（CA/Browser Forum）论坛投票通过187号提案，要求 CA 机构从2017年9月8日起执行 CAA 强制性检查。

## CAA 如何执行？
域名所有者通过设置 CAA 解析记录来授权指定的 CA 机构为其颁发 SSL 证书，同时 CA 机构根据规范要求，在颁发 SSL 证书时会强制性检查域名 CAA 记录，如果检查发现未获得授权，将拒绝为该域名颁发 SSL 证书，从而防止未授权的 SSL 证书错误颁发，规避安全风险。

>?
>- 若域名所有者未为该域名设置 CAA 记录，那么任何 CA 机构都可以为该域名颁发 SSL 证书。
>- 若您的域名在 DNSPod 进行托管，具体操作请参见 [CAA 记录](https://docs.dnspod.cn/dns/5f3b337aab35dc34f57913e4/)。
>- 若申请域名添加了非腾讯云 CA 机构的 CAA 记录，将无法正常颁发，进行域名验证前，请先检查是否添加了 CAA 记录。若已添加，请删除后再进行域名验证。


