
## 功能介绍

内容访问控制可以通过 URL 鉴权和 Cookie 鉴权实现，腾讯云 CDN 已支持 [URL 鉴权](https://cloud.tencent.com/document/product/228/41622) ，现新增对 Cookie 鉴权的支持。客户端根据约定格式发送携带签名的 Cookie，CDN 边缘对 Cookie 进行验证，验证通过则响应请求。

>? 当前本功能仅对境外域名生效。



## 适用场景

- 不希望改变现有 URL，如基于HLS 协议的点播内容鉴权。
- 同时对多个资源进行访问控制，需要针对同个域名下的不同资源设置不同的访问策略。



## 使用流程

1. 登录 [插件中心](https://console.cloud.tencent.com/cdn/plugins) 开启 Cookie 鉴权功能，进入 [域名管理](https://console.cloud.tencent.com/cdn/domains) 设置鉴权模式和对应密钥。
2. 客户源站根据规范要求，对客户端进行 Set-Cookie ，将 Cookie 传递给客户端。
3. 终端用户(客户端)携带上述 Cookie 向 CDN 请求资源。
4. CDN 边缘服务器读取 Cookie 对应内容，鉴权通过则继续提供服务，鉴权失败则返回 403 状态码。



## Set-Cookie 格式

腾讯云 CDN 支持 Type A 和 Type B 两种格式的 Cookie 鉴权，供客户选择使用。源站服务器在传递 Cookie ，对客户端进行 Set-Cookie 操作时，需遵循以下格式规范：

### Type A

符合 Cookie 格式标准的前提下，Type A Set-Cookie 还须包含`TC-Policy`和`TC-Sign`2 个参数：

```
Set-Cookie: TC-Policy=`base64编码后的访问控制策略` ;
Set-Cookie: TC-Sign=`哈希和签名后的访问控制策略` ;
```

**访问控制策略的构成**

访问控制策略采用 JSON 格式创建，策略总字符数不超过 2048 个。支持创建多个数组（即多组策略），多组策略的优先级从上到下递减，一旦命中，则直接忽略余下的策略。

```
{
    "Policy": [
        {
            "Resource": "资源URL",       //必填参数，需包含协议、域名及 URL，如“https://www.example.com/image”
            "Condition": {
                "DateLessThan": {
                    "ExpireTime": "策略到期时间"    //UNIX时间戳，必填参数
                },
                "DateGreaterThan": {
                    "StartTime": "策略生效时间"    //UNIX时间戳，可选参数
                },
                "IpAddress": {
                    "SourceIp": "IPv4地址"    //CIDR格式，可选参数
                }
            }
        }
    ]
}
```

Set-Cookie 具体步骤：

1. 按上述格式要求创建访问控制策略
2. 删除访问控制策略中所有的空格（包含制表符和换行符）后进行 Base64 编码，用有效字符替换无效字符，再放入`TC-Policy`参数
3. 对访问控制策略进行哈希和 HMAC 签名，放入`TC-Sign`参数

>?
>- 无效字符替换成有效字符："+" 替换成 "-"，"=" 替换成 "_"，"/" 替换成  "~"。
>- Type A 签名方式具体请见 [示例](#TypeA)



### Type B

符合 Cookie 格式标准的前提下，Type B Set-Cookie 还须包含`TC-HMAC`参数，`TC-HMAC`里头的子参数（如acl/st/exp）用 "~" 进行拼接：

```
Set-Cookie: TC-HMAC=acl=`可允许的 URL`~st=`开始时间`~exp=`结束时间`~ip=`可允许的 IP`~hmac=`hmac 签名计算结果`
```

>?
>- `acl`：需必须包含需包含协议、域名及 URL，如`https://www.example.com/image`。
>- `st`：鉴权开始时间，采用 UNIX 时间戳，必填参数。
>- `exp`：鉴权结束时间，采用 UNIX 时间戳，可选参数，未设置则默认在`st` 基础上加 86400 秒。
>- `ip`： IP 白名单，采用 CIDR 格式，仅支持 IPv4，可选参数。
>- `hmac`：对上述参数进行 HMAC 签名的结果，hmac = hmac (key, acl, st, exp, ip)，Type B 签名方式具体请见 [示例](#TypeB)。



## 配置指南

首次使用需登录插件中心，打开 **Cookie 鉴权** 插件功能后，再回到域名管理进行配置。具体配置路径为：**[域名管理](https://console.cloud.tencent.com/cdn/domains)**  > **选中域名** > **访问控制** > **Cookie 鉴权**。
设置鉴权模式、首选密钥和备选密钥后，CDN 节点优先采用首选密钥进行验证，验证失败则采用备选密钥，两者都不通过则返回 403。
![](https://main.qcloudimg.com/raw/3fa5c2d1e8e01a151c3f3d130b23a923.png)

>? 备选密钥可用于密钥轮换。

设置完成后，按上述要求 Set-Cookie，用控制台设置的密钥进行签名，客户端携带已签名的 Cookie 向 CDN 节点发起访问请求即可。



## 签名示例
[](id:TypeA)
### Type A 示例

假设密钥为`TencentCDN`，创建文件`policy.json`文件，并填写如下的访问控制策略：

```
{
    "Policy": [
        {
            "Resource": "https://www.example.com/i?age/*",
            "Condition": {
                "DateLessThan": {
                    "ExpireTime": 1629550200
                },
                "DateGreaterThan": {
                    "StartTime": 1627821119
                },
                "IpAddress": {
                    "SourceIp": "192.168.1.1/32"
                }
            }
        }
    ]
}
```

则计算出来的 TC-Policy 结果为：

```
TC-Policy=eyJQb2xpY3kiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vaT9hZ2UvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiRXhwaXJlVGltZSI6MTYyOTU1MDIwMH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJTdGFydFRpbWUiOjE2Mjc4MjExMTl9LCJJcEFkZHJlc3MiOnsiU291cmNlSXAiOiIxOTIuMTY4LjEuMS8zMiJ9fX1dfQ__
```

>? 计算脚本：`cat policy.json | tr -d "\n" | tr -d " \t\n\r" |  openssl base64 |  tr -- '+=/' '-_~'`

计算出来的 TC-Sign 结果应为：

```
TC-Sign=82c628299e93a05c513378363e876fcdb4973b66b5981f188665463bd74ff1c8
```

>? 计算脚本：`cat policy.json | tr -d "\n" | tr -d " \t\n\r" |  openssl dgst -hmac TencentCDN -hex`

[](id:TypeB)
### Type B 示例

假设密钥为`TencentCDN`，对应的访问控制条件设为：

```
acl=`https://www.example.com/i?age/*`
st=`1627821119`
exp=`1629550200`
ip=`192.168.1.1/32`
```

则计算出来的 TC-HMAC 结果为：

```
TC-HMAC=acl=https://www.example.com/i?age/*~st=1627821119~exp=1629550200~ip=192.168.1.1/32~hmac=b6cc0b55861fb03f3cd5db299ef54a359490ab3715252a5e9151c1b963279235
```

>? 计算脚本：`echo 'https://www.example.com/i\?age/\*16278211191629550200192.168.1.1/32' | tr -d "\n" | tr -d " \t\n\r" | openssl dgst -hmac TencentCDN -hex`



## 最佳实践
假设 0.cooke.test.scdn.team 负责 set-cookie, 1.cooke.test.scdn.team 负责向 CDN 请求资源，使用 Type A 的签名方式，密钥为`TencentCDN`。

1. 终端用户向 0.cooke.test.scdn.team 请求资源 /image/test.jpg，通过鉴权后，源站返回 set-cookie 响应头，源站配置的访问控制策略为（后续访问将命中第二组策略）：
```
{
    "Policy":[
        {
            "Condition":{
                "DateGreaterThan":{
                    "StartTime":45
                },
                "DateLessThan":{
                    "ExpireTime":999999999999
                },
                "IpAddress":{
                    "SourceIp":"192.168.1.1/32"
                }
            },
            "Resource":"https://1.cookie.test.scdn.team/movie/*"
        },
        {
            "Condition":{
                "DateGreaterThan":{
                    "StartTime":45
                },
                "DateLessThan":{
                    "ExpireTime":999999999999
                },
                "IpAddress":{
                    "SourceIp":"192.168.1.1/32"
                }
            },
            "Resource":"https://1.cookie.test.scdn.team/i?age/*.jpg"
        }
    ]
}
```
则计算出来
```
set-cookie: TC-Policy=eyJQb2xpY3kiOlt7IkNvbmRpdGlvbiI6eyJEYXRlR3JlYXRlclRoYW4iOnsiU3RhcnRUaW1lIjo0NX0sIkRhdGVMZXNzVGhhbiI6eyJFeHBpcmVUaW1lIjo5OTk5OTk5OTk5OTl9LCJJcEFkZHJlc3MiOnsiU291cmNlSXAiOiIxOTIuMTY4LjEuMS8zMiJ9fSwiUmVzb3VyY2UiOiJodHRwczovLzEuY29va2llLnRlc3Quc2Nkbi50ZWFtL21vdmllLyoifSx7IkNvbmRpdGlvbiI6eyJEYXRlR3JlYXRlclRoYW4iOnsiU3RhcnRUaW1lIjo0NX0sIkRhdGVMZXNzVGhhbiI6eyJFeHBpcmVUaW1lIjo5OTk5OTk5OTk5OTl9LCJJcEFkZHJlc3MiOnsiU291cmNlSXAiOiIxOTIuMTY4LjEuMS8zMiJ9fSwiUmVzb3VyY2UiOiJodHRwczovLzEuY29va2llLnRlc3Quc2Nkbi50ZWFtL2k~YWdlLyouanBnIn1dfQ__; Path=/; Domain=test.scdn.team; Max-Age=600; Secure

set-cookie: TC-Sign=aafc24c523636050e57e50388a35fd6999528b7848a521d171e67d8df350f4b2; Path=/; Domain=test.scdn.team; Max-Age=600; Secure
```
2. 终端用户携带该 Cookie 访问 CDN 资源`https://1.cookie.test.scdn.team/image/test.jpg`，请求示例如下：
```
curl 'https://1.cookie.test.scdn.team/image/test.jpg' \
  -H 'authority: 1.cookie.test.scdn.team' \
  -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73' \
  -H 'accept: */*' \
  -H 'origin: https://0.cookie.test.scdn.team' \
  -H 'sec-fetch-site: same-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://0.cookie.test.scdn.team/' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cookie: TC-Policy=eyJQb2xpY3kiOlt7IkNvbmRpdGlvbiI6eyJEYXRlR3JlYXRlclRoYW4iOnsiU3RhcnRUaW1lIjo0NX0sIkRhdGVMZXNzVGhhbiI6eyJFeHBpcmVUaW1lIjo5OTk5OTk5OTk5OTl9LCJJcEFkZHJlc3MiOnsiU291cmNlSXAiOiIxOTIuMTY4LjEuMS8zMiJ9fSwiUmVzb3VyY2UiOiJodHRwczovLzEuY29va2llLnRlc3Quc2Nkbi50ZWFtL21vdmllLyoifSx7IkNvbmRpdGlvbiI6eyJEYXRlR3JlYXRlclRoYW4iOnsiU3RhcnRUaW1lIjo0NX0sIkRhdGVMZXNzVGhhbiI6eyJFeHBpcmVUaW1lIjo5OTk5OTk5OTk5OTl9LCJJcEFkZHJlc3MiOnsiU291cmNlSXAiOiIxOTIuMTY4LjEuMS8zMiJ9fSwiUmVzb3VyY2UiOiJodHRwczovLzEuY29va2llLnRlc3Quc2Nkbi50ZWFtL2k~YWdlLyouanBnIn1dfQ__;TC-Sign=aafc24c523636050e57e50388a35fd6999528b7848a521d171e67d8df350f4b2 \
  --compressed
```
>?
>1. 由于涉及到跨域访问，需要在 CDN/源站上配置如下响应头部，用于跨域请求。
>access-control-allow-credentials: true
>access-control-allow-methods: GET, POST
>access-control-allow-origin: `https://0.cookie.test.scdn.team`
>2. 前端发起请求时设置 xhr.withCredentials = true，用于携带 Cookie 发送跨域请求。
	
3. CDN 节点会对用户携带的 Cookie 进行校验，如果通过则会返回 /image/test.jpg 文件内容，如果不通过则返回403。

## 费用说明

Cookie 鉴权为免费功能，不收取任何额外费用。

