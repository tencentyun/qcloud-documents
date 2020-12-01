## 功能介绍
CDN 上分发的内容默认为公开资源，为了避免恶意用户盗刷内容进行牟利，腾讯云 CDN 支持 URL 鉴权配置。

## 算法说明
### TypeA
- 访问 URL 格式：`http://DomainName/Filename?sign=timestamp-rand-uid-md5hash`
- 算法说明：
  - timestamp：十进制（UNIX 时间戳）。
  - rand：随机字符串，0 - 100位随机字符串，由大小写字母与数字组成。
  - uid：0。
  - md5hash：MD5（文件路径-timestamp-rand-uid-自定义密钥）。

> !若请求原始 URL 为`http://www.test.com/test/1.jpg`，此时计算 MD5 时文件路径为 `/test/1.jpg`。

### TypeB
- 访问 URL 格式：`http://DomainName/timestamp/md5hash/FileName`
- 算法说明：
  - timestamp：时间戳，格式为 YYYYMMDDHHMM。
  - md5hash：MD5（自定义密钥 + timestamp + 文件路径）。

> !若请求原始 URL 为`http://www.test.com/test/1.jpg`，此时计算 MD5 时文件路径为 `/test/1.jpg`。

### TypeC
- 访问 URL 格式：`http://DomainName/md5hash/timestamp/FileName`
- 算法说明：
  - timestamp：十六进制（UNIX 时间戳）。
  - md5hash：MD5（自定义密钥 + 文件路径 + timestamp）。

> ! 若请求原始 URL 为`http://www.test.com/test/1.jpg`，此时计算 MD5 时文件路径为 `/test/1.jpg`。

### TypeD
- 访问 URL 格式：`http://DomainName/FileName?sign=md5hash&t=timestamp`
- 算法说明：
  - timestamp：十进制/十六进制（UNIX 时间戳）可选。
  - md5hash：MD5（自定义密钥 + 文件路径 + timestamp）。

> ! 若请求原始 URL 为`http://www.test.com/test/1.jpg`，此时计算 MD5 时文件路径为 `/test/1.jpg`。

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 单击【安全配置】，您可以看到**鉴权配置**模块，默认情况下为关闭状态。
![image](https://main.qcloudimg.com/raw/6c74dadfd6d5eb65d59134d5647c1116.png)
3. 在**鉴权配置**模块下，单击开启【鉴权配置】，目前提供三类模式可选：
> !TypeB 功能升级中，暂无法选择。
> 
![img](https://main.qcloudimg.com/raw/90f6a122795f2baecc281f267a6c5611.png)
4. 选定类型后，可进行鉴权参数配置（以 **TypeA** 为例）：
   - 鉴权密钥：可根据自身业务情况指定字符串作为鉴权密钥。
   - 签名参数：设置携带签名串的参数名称，默认填充为 **sign**，可指定为其他参数名。
   - 有效时间：服务端会通过签名解析出来的 **timestamp**，加上有效时间，与当前时间对比，判定签名是否有效。

<img src="https://main.qcloudimg.com/raw/abf68477508155f85d888668fc6b2b99.png"  style="margin: 0px 0px 0px 30px;">

5. 完成鉴权参数配置后，需指定鉴权范围与对象：
![img](https://main.qcloudimg.com/raw/353bcd539cb3a9d183b089d56fd54bae.png)

## 鉴权计算器
> ?您可以使用鉴权计算器来核对请求路径、签名是否计算正确。
> 
在**鉴权配置**模块中，单击【鉴权计算器】，目前提供三类模式可选，选定类型并配置鉴权参数后可计算出鉴权 URL（以 **TypeA** 为例）：
![img](https://main.qcloudimg.com/raw/c74fcdb0416d52b266ff3d1e54d0172f.png)
> !
> - TypeB 功能升级中，暂无法选择。
> - 若访问路径是包含有中文的 URL，您需要先进行 URL 编码转义后再进行鉴权配置。

