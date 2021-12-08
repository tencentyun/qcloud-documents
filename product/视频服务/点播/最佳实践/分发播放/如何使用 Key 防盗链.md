

## 使用须知

### Demo 功能介绍
本 Demo 向开发者展示云点播（VOD）[Key 防盗链](https://cloud.tencent.com/document/product/266/14047)  机制的使用方法，包括在控制台启用 Key 防盗链、搭建一个防盗链签名派发服务、以及使用防盗链签名播放视频。

### 架构和流程

Demo 基于云函数（SCF）搭建了一个 HTTP 服务，用于接收来自客户端的获取防盗链签名请求。服务从请求 Body 中获取 VOD 的视频原始 URL，计算防盗链签名，并返回带防盗链签名的 URL 给客户端。

系统主要涉及四个组成部分：开发者、API 网关、云函数和云点播，其中 API 网关和云函数即是本 Demo 的部署对象，如下图所示：
<img src="https://main.qcloudimg.com/raw/e2397093b8cd9d0aabf228ef41ecac45.png" width="600">

具体业务流程为：

1. 开发者在 VOD 控制台上获取到视频的原始 URL（实际生产环境中，应当是由播放器向业务后台请求视频的 URL，本文为了简化流程由开发者模拟该业务行为）。
2. 开发者使用视频原始 URL 向 SCF 请求防盗链签名。
3. 开发者使用带防盗链签名的视频 URL 请求 VOD CDN，播放视频。

> ?Demo 中的 SCF 代码使用 Python3.6 进行开发，此外 SCF 还支持 Python2.7、Node.js、Golang、PHP 和 Java 等多种编程语言，开发者可以根据情况自由选择，具体请参考 [SCF 开发指南](https://cloud.tencent.com/document/product/583/11061)。

### 费用
本文提供的云点播 Key 防盗链签名派发服务 Demo 是免费开源的，但在搭建和使用的过程中可能会产生以下费用：

- 购买腾讯云云服务器（CVM）用于执行服务部署脚本，详见 [CVM 计费](https://cloud.tencent.com/document/product/213/2180)。
- 使用腾讯云云函数（SCF）提供签名派发服务，详见 [SCF 计费](https://cloud.tencent.com/document/product/583/12284) 和 [SCF 免费额度](https://cloud.tencent.com/document/product/583/12282)。
- 使用腾讯云 API 网关为 SCF 提供外网接口，详见 [API 网关计费](https://cloud.tencent.com/document/product/628/39300)。
- 消耗云点播（VOD）存储用于存储上传的视频，详见 [存储计费](https://cloud.tencent.com/document/product/266/14666#.E5.AA.92.E8.B5.84.E5.AD.98.E5.82.A8.3Cspan-id.3D.22media_storage.22.3E.3C.2Fspan.3E) 和 [存储资源包](https://cloud.tencent.com/document/product/266/14667#1.-.E5.AD.98.E5.82.A8.E8.B5.84.E6.BA.90.E5.8C.85)。
- 消耗云点播流量用于播放视频，详见 [流量计费](https://cloud.tencent.com/document/product/266/14666#.E5.8A.A0.E9.80.9F.E6.9C.8D.E5.8A.A1.3Cspan-id.3D.22speed.22.3E.3C.2Fspan.3E) 和 [流量资源包](https://cloud.tencent.com/document/product/266/14667#2.-.E6.B5.81.E9.87.8F.E8.B5.84.E6.BA.90.E5.8C.85)。

## 快速部署 Key 防盗链签名派发服务

### 步骤1：准备腾讯云 CVM[](id:p1)

部署脚本需要运行在一台腾讯云 CVM 上，要求如下：

- 地域：任意。
- 机型：官网最低配置（1核1GB）即可。
- 公网：需要拥有公网 IP，带宽1Mbps或以上。
- 操作系统：官网公共镜像`Ubuntu Server 16.04.1 LTS 64位`或`Ubuntu Server 18.04.1 LTS 64位`。

购买 CVM 的方法请参见 [操作指南 - 创建实例](https://cloud.tencent.com/document/product/213/4855)。重装系统的方法请参见 [操作指南 - 重装系统](https://cloud.tencent.com/document/product/213/4933)。

>!
>- Key 防盗链签名派发服务 Demo 本身并不依赖于 CVM，仅使用 CVM 来执行部署脚本。
>- 如果您没有符合上述条件的腾讯云 CVM，也可以在其它带外网的 Linux（如 CentOS、Debian 等）或 Mac 机器上执行部署脚本，但需根据操作系统的区别修改脚本中的个别命令，具体修改方式请开发者自行搜索。

### 步骤2：开通云点播并配置 Key 防盗链[](id:p2)

1. 参考 [快速入门 - 步骤1](https://cloud.tencent.com/document/product/266/8757#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E4.BA.91.E7.82.B9.E6.92.AD) 开通云点播服务。
2. 开通完成后，参考 [设置防盗链](https://cloud.tencent.com/document/product/266/33469) 文档启用 Key 防盗链，并记录下防盗链 Key：
![](https://main.qcloudimg.com/raw/04d1a39b76fdb3bef5acebe57f3edb16.png)
>!此处是开通 Key 防盗链，而非开通 Referer 防盗链。如果您同步开通了 Referer 防盗链，那么下文的测试方法有可能因为不符合 Referer 防盗链的要求而导致请求失败。

### 步骤3：获取 API 密钥和 APPID[](id:p3)

Key 防盗链签名派发服务 Demo 的部署和运行过程需要使用到开发者的 API 密钥（即 SecretId 和 SecretKey）和 APPID。

- 如果还未创建过密钥，请参见 [创建密钥文档](https://cloud.tencent.com/document/product/598/40488#.E5.88.9B.E5.BB.BA.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 生成新的 API 密钥；如果已创建过密钥，请参见 [查看密钥文档](https://cloud.tencent.com/document/product/598/40488#.E6.9F.A5.E7.9C.8B.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 获取 API 密钥。
- 在控制台 [账号信息](https://console.cloud.tencent.com/developer) 页面可以查看 APPID，如下图所示：
  ![](https://main.qcloudimg.com/raw/0e7dda93add5f53b2da07d16cf6f4406.png)

### 步骤4：部署防盗链签名派发服务

登录 [步骤1准备的 CVM](#p1)（登录方法详见 [操作指南 - 登录 Linux](https://cloud.tencent.com/document/product/213/5436)），在远程终端输入以下命令并运行：

```
ubuntu@VM-69-2-ubuntu:~$ export SECRET_ID=AKxxxxxxxxxxxxxxxxxxxxxxx; export SECRET_KEY=xxxxxxxxxxxxxxxxxxxxx;export APPID=125xxxxxxx;export ANTI_LEECH_KEY=xxxx;git clone https://github.com/tencentyun/vod-server-demo.git ~/vod-server-demo; bash ~/vod-server-demo/installer/anti_leech_sign_scf.sh
```

>?请将命令中的 SECRET_ID、SECRET_KEY 和 APPID 赋值为 [步骤3](#p3) 中获取到的内容；将 ANTI_LEECH_KEY 赋值为 [步骤2](#p2) 中获取到的防盗链 Key。

该命令将从 Github 下载 Demo 源码并自动执行安装脚本。安装过程需几分钟（具体取决于 CVM 网络状况），期间远程终端会打印如下示例的信息：

```
[2020-06-04 15:57:10]开始安装 pip3。
[2020-06-04 15:57:18]pip3 安装成功。
[2020-06-04 15:57:18]开始安装腾讯云 SCF 工具。
[2020-06-04 15:57:19]scf 安装成功。
[2020-06-04 15:57:19]开始配置 scf。
[2020-06-04 15:57:20]scf 配置完成。
[2020-06-04 15:57:20]开始部署云点播 Key 防盗链签名派发服务。
[2020-06-04 15:57:30]云点播 Key 防盗链签名派发服务部署完成。
[2020-06-04 15:57:32]服务地址：https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/anti_leech_sign
```

复制输出日志中的签名派发服务地址（示例中的`https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/anti_leech_sign`）。

> !如果输出日志中出现如下所示的警告，一般是由于 CVM 无法立即解析刚部署好的服务域名，可尝试忽略该警告。
> ```
> [2020-04-25 17:18:44]警告：Key 防盗链签名派发服务测试不通过。
> ```

### 步骤5：测试 Key 防盗链

按照 [上传视频 - 本地上传步骤](https://cloud.tencent.com/document/product/266/2841#.E6.9C.AC.E5.9C.B0.E4.B8.8A.E4.BC.A0.E6.AD.A5.E9.AA.A4) 的说明，上传一个测试视频到云点播。上传完成后，单击【快捷查看】，然后单击右侧【复制地址】复制该视频的 URL。
![](https://main.qcloudimg.com/raw/b93899bb2d2335ce3212ca9c024df10a.png)
在 CVM 命令行执行`curl`命令尝试直接访问该 URL，结果会因不符合 Key 防盗链规则而被服务器拒绝访问，HTTP 返回码为403（测试时，请将命令中的 URL 替换为实际 URL，下同）：

```
ubuntu@VM-69-2-ubuntu:~$ curl -I "http://125xxxxxxx.vod2.myqcloud.com/f888c998vodcq125xxxxxxx/c849148f528xxxxxxxxxxxxxxxx/xxxxxxxxxx.mp4"
HTTP/1.1 403 Forbidden
Server: NWS_VP
Connection: keep-alive
Date: Thu, 04 Jun 2020 08:27:54 GMT
Content-Type: text/plain
Content-Length: 14
```
在 CVM 命令行执行`curl`命令来请求步骤4中部署的服务，获取带防盗链签名的 URL（`-d`表示使用 POST 方式发起请求，所带的参数为视频 URL）：
```
ubuntu@VM-69-2-ubuntu:~$ curl -d 'http://125xxxxxxx.vod2.myqcloud.com/f888c998vodcq125xxxxxxx/c849148f528xxxxxxxxxxxxxxxx/xxxxxxxxxx.mp4' https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/anti_leech_sign; echo
http://125xxxxxxx.vod2.myqcloud.com/f888c998vodcq125xxxxxxx/c849148f528xxxxxxxxxxxxxxxx/xxxxxxxxxx.mp4?t=5ed8b8d2&exper=0&rlimit=0&us=455041&sign=fe6394007c2e7aef39fc70a02e897f69
```
再次使用`curl`命令访问上一步得到的带防盗链签名的 URL，能够正常访问（HTTP 返回码为200）：
```
ubuntu@VM-69-2-ubuntu:~$ curl -I "http://125xxxxxxx.vod2.myqcloud.com/f888c998vodcq125xxxxxxx/c849148f528xxxxxxxxxxxxxxxx/xxxxxxxxxx.mp4?t=5ed8b8d2&exper=0&rlimit=0&us=455041&sign=fe6394007c2e7aef39fc70a02e897f69"
HTTP/1.1 200 OK
Server: tencent-cos
Connection: keep-alive
Date: Thu, 04 Jun 2020 08:37:17 GMT
Last-Modified: Fri, 22 May 2020 15:06:15 GMT
Content-Type: video/mp4
Content-Length: 232952632
Accept-Ranges: bytes
ETag: "1da6be3a0d1da5edae4ff0b1feff02cf-223"
x-cos-hash-crc64ecma: 16209801220610226954
x-cos-request-id: NWVkOGIyYmVfZDUyMzYyNjRfYWMwMF85YjkyNzA=
X-Daa-Tunnel: hop_count=4
X-NWS-LOG-UUID: b404f43e-3c86-4c54-8a78-fb78e4e85cf2 add71e19fb08c6d9dbe1b21a2fb157bf
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Origin,No-Cache,X-Requested-With,If-Modified-Since,Pragma,Last-Modified,Cache-Control,Expires,Content-Type,X_Requested_With,Range
Access-Control-Allow-Methods: GET,POST,OPTIONS
Access-Control-Allow-Origin: *
```
>?您可以在浏览器中访问带防盗链签名的 URL，通过播放视频的方式来验证防盗链签名。但这种方式对视频格式有要求，一般来说使用 H.264 编码的 MP4 文件具有较好的兼容性，建议选用这类视频；您也可以使用 Postman 等第三方工具来发送 HTTP 请求，具体用法请自行搜索。 

## 系统设计说明

### 接口协议

Key 防盗链签名派发云函数通过 API 网关对外提供接口，具体接口协议如下：

| 服务               | 云函数名        | 接口形式  | 请求内容     | 返回内容         |
| ------------------ | --------------- | --------- | ------------ | ---------------- |
| Key 防盗链签名派发 | anti_leech_sign | HTTP POST | 视频原始 URL | 带防盗链签名 URL |

### 签名派发服务代码解读

1. `main_handler()`为入口函数。
2. 调用`parse_conf_file()`，从`config.json`文件中读取配置信息。配置项说明如下（详细参数请参见 [Key 防盗链签名参数](https://cloud.tencent.com/document/product/266/14047#.E9.98.B2.E7.9B.97.E9.93.BE-url-.E7.94.9F.E6.88.90.E6.96.B9.E5.BC.8F)）：
<table>
<thead>
<tr>
<th>字段</th>
<th>数据类型</th>
<th>功能</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td>String</td>
<td>Key 防盗链密钥</td>
</tr>
<tr>
<td>t</td>
<td>Integer</td>
  <td>签名有效时间，单位：秒。在处理请求时，该参数与 SCF 服务器的当前时间相加后，才是防盗链参数中的 t</td>
</tr>
<tr>
<td>exper</td>
<td>Integer</td>
<td>试看时长</td>
</tr>
<tr>
<td>rlimit</td>
<td>Integer</td>
<td>签名最多允许被多少个客户端 IP 访问</td>
</tr>
</tbody></table>
3. 从请求 Body 中解析出`Dir`参数，本地生成`t`和`us`参数，从配置文件中读取`exper`和`rlimit`参数：
```
       original_url = event["body"]
       parse_result = urlparse(original_url)
       directory = path.split(parse_result.path)[0] + '/'
       # 签名参数
       timestamp = int(time.time())
       rand = random.randint(0, 999999)
       sign_para = {
           "t": hex(timestamp + configuration['t'])[2:],
           "exper": configuration['exper'],
           "rlimit": configuration['rlimit'],
           "us": rand
       }	
```
4. 调用`generate_sign()`计算防盗链签名，详细算法请参见 [Key 防盗链签名](https://cloud.tencent.com/document/product/266/14047#.E9.98.B2.E7.9B.97.E9.93.BE-url-.E7.94.9F.E6.88.90.E6.96.B9.E5.BC.8F)。
5. 生成 QueryString，拼接在原始 URL 后组成带防盗链签名的 URL：
```
       sign_para["sign"] = signature
       query_string = urlencode(sign_para)
       new_parse_result = parse_result._replace(query=query_string)
       signed_url = urlunparse(new_parse_result)
```
6. 返回签名。返回的数据格式及含义请参见 [云函数集成响应](https://cloud.tencent.com/document/product/583/12513#.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94.E4.B8.8E.E9.80.8F.E4.BC.A0.E5.93.8D.E5.BA.94)。
```
       return {
           "isBase64Encoded": False,
           "statusCode": 200,
           "headers": {"Content-Type": "text/plain; charset=utf-8",
                       "Access-Control-Allow-Origin": "*",
                       "Access-Control-Allow-Methods": "POST,OPTIONS"},
           "body": signed_url
       }
```

   
   

