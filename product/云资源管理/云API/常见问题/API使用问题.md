### C++ 运行单个签名文件报错
- 问题现象：
在命令行运行 `g++ -o main sign.cpp` 导致报错。如下图所示：
![](https://main.qcloudimg.com/raw/499379efd848870eb0e0b3fb97171968.png) 
- 解决方案：
```bash
g++ -o main sign.cpp -lssl -lcrypto
```


### 提示错误码 10060，如何处理？
```
Socket error 10060 - Connection timed out
```
10060 是 Socket 编程接口给出的错误，表示网络连接超时。您的机器将无法和腾讯云云 API 服务器进行连通，请排查以下问题：
- 本地访问外网是否需要设置代理。
- 本地机器防火墙是否有限制外访的规则。
- 路由器是否有限制外访的规则。

### 腾讯云 API 的错误码有哪些？

腾讯云 API 的错误码通常分为公共错误码和非公共错误码。
- 公共错误码一般可以单击每个产品下的调用方式，返回结果查看。
- 非公共错误码可以在具体的接口描述页面查看。单击这里可以查看 [错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)（以 CVM 为例）。
