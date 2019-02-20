## 功能介绍

CDN 上分发的内容为默认公开资源，为了避免恶意用户通过技术手段，盗链服务商提供的内容进行牟利，腾讯云 CDN 支持 URL 鉴权配置。URL 鉴权多用于视频、安装包等内容的安全保护。
>? 不同鉴权模式算法公式不同，本篇文档为 TypeB 的配置说明。

## 字段含义

| 字段       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| 鉴权密钥   | 用户自定义设置或随机生成的6-32位字符，由大小写字母或数字组成 |
| 签名参数   | 自定义签名参数，格式为1-100个字符，由数字、英文大小写字母及下划线组成，不能以数字开头 |
| 有效时间   | 过期时间，签名有效时间                                       |
| 时间格式   | 携带时间戳为十进制 UNIX 时间，或十六进制 UNIX 时间           |
| 时间戳参数 | 自定义时间戳参数，格式为1-100个字符，由数字、英文大小写字母及下划线组成，不能以数字开头 |

## 算法说明
- 访问加密 URL 格式：
```
http://DomainName/Filename?auth_key=timestamp-rand-uid-md5hash
```
- 字段解析：
   - `timestamp`：UTC 时间，十进制
   - `rand`：随机数，0 - 100位随机数，大小写字母与数字组成
   - `uid`：0
   - `md5hash`：MD5（URI-Timestamp-rand-uid-PrivateKey）

## 配置指引

1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn/access/manage/1444090?tab=secure)，进入【域名管理】页面，选择需要设置的域名，单击【管理】。
![](https://main.qcloudimg.com/raw/801ab697e2728cb0ab8d56ac5204e433.png)
2. 在【安全配置】中找到【鉴权配置】模块，单击开启【鉴权配置】。
![](https://main.qcloudimg.com/raw/f83e9780cd0ad338b71bbe8aa1ddea2f.png)
3. 弹出【鉴权配置】弹窗，选中模式 B 并展示模式示例：
   ![](https://main.qcloudimg.com/raw/fa4384310e16f52f2b4fa7e869826763.png)
4. 单击【下一步】，进入**设置参数**窗口，填写鉴权密钥及有效时间：
   ![](https://main.qcloudimg.com/raw/10d6c4433a7eef1c2c2d4388b4a0143b.png)
5. 单击【下一步】，进入**配置鉴权对象**窗口，选择鉴权范围，若制定文件类型鉴权/不鉴权，请填写鉴权对象：
   ![](https://main.qcloudimg.com/raw/cf29224f1ac7f83fd1a452c432a46c1c.png)

## 鉴权计算器

>? 您可以使用鉴权计算器来核对请求路径、签名是否计算正确。

1. 选择模式 B，填写鉴权密钥、访问路径、时间设置及有效时间：
  ![](https://main.qcloudimg.com/raw/0c187b452e0b2fb509e50828e756ccdc.png)
2. 单击【生成】，下框会展示鉴权 URL 及过期时间：
  ![](https://main.qcloudimg.com/raw/802de90d0495fd611467166638179edb.png)
