## 使用须知

### Demo 功能介绍

本 Demo 向开发者展示如何通过 Web 页面将视频上传到云点播。Demo 基于云函数（SCF）搭建了两个 HTTP 服务：

- 第一个服务用于接收来自浏览器获取 [客户端上传签名](https://cloud.tencent.com/document/product/266/9221) 的请求，计算上传签名并返回。
- 第二个服务使用 VOD [Web 上传 SDK](https://cloud.tencent.com/document/product/266/9239) 实现一个页面，用户可以通过浏览器访问该页面，并上传本地视频到 VOD。

### 架构和流程

系统主要涉及四个组成部分：浏览器、API 网关、云函数和云点播，其中 API 网关和云函数即是本 Demo 的部署对象，如下图所示：
<img src="https://main.qcloudimg.com/raw/ec886cea3098ad0256869ccdab22acb3.png" width="500">

主要业务流程为：

1. 浏览器向 SCF 请求上传页面。
2. 用户在上传页面进行操作，选中本地视频后点击上传，由浏览器向 SCF 请求上传签名。
3. 浏览器使用上传签名向 VOD 发起上传请求，完成后在上传页面上展示上传结果。

> ?Demo 中的 SCF 代码使用 Python3.6 进行开发，此外 SCF 还支持 Python2.7、Node.js、Golang、PHP 和 Java 等多种编程语言，开发者可以根据情况自由选择，具体请参考 [SCF 开发指南](https://cloud.tencent.com/document/product/583/11061)。

### 费用

本文提供的云点播 Web 上传 Demo 是免费开源的（含 Web 页面代码和业务后台代码），但在搭建和使用的过程中可能会产生以下费用：

- 购买腾讯云云服务器（CVM）用于执行服务部署脚本，详见 [CVM 计费](https://cloud.tencent.com/document/product/213/2180)。
- 使用腾讯云云函数（SCF）提供上传页面和签名派发服务，详见 [SCF 计费](https://cloud.tencent.com/document/product/583/12284) 和 [SCF 免费额度](https://cloud.tencent.com/document/product/583/12282)。
- 使用腾讯云 API 网关为 SCF 提供外网接口，详见 [API 网关计费](https://cloud.tencent.com/document/product/628/39300)。
- 消耗云点播（VOD）存储用于存储上传的视频，详见 [存储计费](https://cloud.tencent.com/document/product/266/14666#.E5.AA.92.E8.B5.84.E5.AD.98.E5.82.A8.3Cspan-id.3D.22media_storage.22.3E.3C.2Fspan.3E) 和 [存储资源包](https://cloud.tencent.com/document/product/266/14667#1.-.E5.AD.98.E5.82.A8.E8.B5.84.E6.BA.90.E5.8C.85)。
- 消耗云点播流量用于播放视频，详见 [流量计费](https://cloud.tencent.com/document/product/266/14666#.E5.8A.A0.E9.80.9F.E6.9C.8D.E5.8A.A1.3Cspan-id.3D.22speed.22.3E.3C.2Fspan.3E) 和 [流量资源包](https://cloud.tencent.com/document/product/266/14667#2.-.E6.B5.81.E9.87.8F.E8.B5.84.E6.BA.90.E5.8C.85)。

## 快速部署 Web 上传 Demo

Web 上传 Demo 部署在 SCF 上，并由 API 网关提供服务入口。为了方便开发者搭建服务，我们提供了快捷部署脚本，使用方法如下。

### 步骤1：准备腾讯云 CVM[](id:p1)

部署脚本需要运行在一台腾讯云 CVM 上，要求如下：

- 地域：任意。
- 机型：官网最低配置（1核1GB）即可。
- 公网：需要拥有公网 IP，带宽1Mbps或以上。
- 操作系统：官网公共镜像`Ubuntu Server 16.04.1 LTS 64位`或`Ubuntu Server 18.04.1 LTS 64位`。

购买 CVM 的方法请参见 [操作指南 - 创建实例](https://cloud.tencent.com/document/product/213/4855)。重装系统的方法请参见 [操作指南 - 重装系统](https://cloud.tencent.com/document/product/213/4933)。

>!
>- **Web 上传 Demo 本身并不依赖于 CVM，仅使用 CVM 来执行部署脚本**。
>- 如果您没有符合上述条件的腾讯云 CVM，也可以在其它带外网的 Linux（如 CentOS、Debian 等）或 Mac 机器上执行部署脚本，但需根据操作系统的区别修改脚本中的个别命令，具体修改方式请开发者自行搜索。

### 步骤2：开通云点播

请参考 [快速入门 - 步骤1](https://cloud.tencent.com/document/product/266/8757#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E4.BA.91.E7.82.B9.E6.92.AD) 开通云点播服务。

### 步骤3：获取 API 密钥和 APPID[](id:p3)

Web 上传 Demo 服务的部署和运行过程需要使用到开发者的 API 密钥（即 SecretId 和 SecretKey）和 APPID。
- 如果还未创建过密钥，请参见 [创建密钥文档](https://cloud.tencent.com/document/product/598/40488#.E5.88.9B.E5.BB.BA.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 生成新的 API 密钥；如果已创建过密钥，请参见 [查看密钥文档](https://cloud.tencent.com/document/product/598/40488#.E6.9F.A5.E7.9C.8B.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 获取 API 密钥。
- 在控制台 [账号信息](https://console.cloud.tencent.com/developer) 页面可以查看 APPID，如下图所示：
![](https://main.qcloudimg.com/raw/0e7dda93add5f53b2da07d16cf6f4406.png)

### 步骤4：部署业务后台和 Web 页面

登录 [步骤1准备的 CVM](#p1)（登录方法详见 [操作指南 - 登录 Linux](https://cloud.tencent.com/document/product/213/5436)），在远程终端输入以下命令并运行：

```
ubuntu@VM-69-2-ubuntu:~$ export SECRET_ID=AKxxxxxxxxxxxxxxxxxxxxxxx; export SECRET_KEY=xxxxxxxxxxxxxxxxxxxxx;export APPID=125xxxxxxx;git clone https://github.com/tencentyun/vod-server-demo.git ~/vod-server-demo; bash ~/vod-server-demo/installer/web_upload_scf.sh
```
>?请将命令中的 SECRET_ID、SECRET_KEY 和 APPID 赋值为 [步骤3](#p3) 中获取到的内容。

该命令将从 Github 下载 Demo 源码并自动执行安装脚本。安装过程需几分钟（具体取决于 CVM 网络状况），期间远程终端会打印如下示例的信息：

```
[2020-04-25 23:03:20]开始安装 pip3。
[2020-04-25 23:03:23]pip3 安装成功。
[2020-04-25 23:03:23]开始安装腾讯云 SCF 工具。
[2020-04-25 23:03:26]scf 安装成功。
[2020-04-25 23:03:26]开始配置 scf。
[2020-04-25 23:03:28]scf 配置完成。
[2020-04-25 23:03:28]开始部署云点播客户端上传签名派发服务。
[2020-04-25 23:03:40]云点播客户端上传签名派发服务部署完成。
[2020-04-25 23:03:44]开始部署云点播 Web 上传页面。
[2020-04-25 23:03:53]云点播 Web 上传页面部署完成。
[2020-04-25 23:03:53]请在浏览器访问以下地址进行体验：https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/web_upload_html
```

[](id:p4)复制输出日志中的 Web 页面地址（示例中的`https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/web_upload_html`）。

> !如果输出日志中出现如下所示的警告，一般是由于 CVM 无法立即解析刚部署好的服务域名，可尝试忽略该警告。
>```
>[2020-04-25 17:18:44]警告：客户端上传签名派发服务测试不通过。
>```

### 步骤5：体验 Web 上传 Demo

1. 在浏览器打开 [步骤4](#p4) 中复制的地址，即可开始体验 Web 上传 Demo。页面如下图所示：
<img src="https://main.qcloudimg.com/raw/fc377fc1c852cb1145686feeb40d7f9c.png" width="750">
2. 在该页面进行视频上传操作：
	1. 选择一个本地视频文件（推荐选择 MP4 文件）。
	2. 选择一张本地封面图片（可选，使用 JPG 或者 PNG 格式）。
	3. 填写视频名称（可选）。
	4. 单击【开始上传】即可上传视频。
<img src="https://main.qcloudimg.com/raw/57969d70fbe061d6135cbe38e3b9aeb9.png" width="700">
3. 上传完成后，页面下方会展示视频和封面的点播媒体 ID（即 fileId）和 URL 等信息。如下图所示：
<img src="https://main.qcloudimg.com/raw/502e1cd4eeeeca33d63680d40e4d614e.png" width="750"></span>
您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/media) 上查看刚上传的视频。如下图所示：
<img src="https://main.qcloudimg.com/raw/819f7638028b6e51e36646da0f396b6c.png" width="750">

>?您可根据页面提示，对上传页面的其它功能进行体验。

## 系统设计说明

### 接口协议及测试

**上传页面**和**上传签名派发**两个云函数都通过 API 网关对外提供接口，具体接口协议如下：

| 服务         | 云函数名        | 接口形式  | 返回内容  |
| ------------ | --------------- | --------- | --------- |
| 上传页面     | web_upload_html | HTTP GET  | HTML 页面 |
| 上传签名派发 | ugc_upload_sign | HTTP POST | 上传签名  |

#### 上传页面[](id:p6)

您可以访问 [SCF 服务列表](https://console.cloud.tencent.com/scf/list) 来查看上传页面服务的详细信息：
<img src="https://main.qcloudimg.com/raw/8480a9211c7d7cecebd105bb211858db.png" width="750">

>?
>- Demo 使用的两个 SCF 部署在广州地域，命名空间为 vod_demo。
>- 控制台上需要选择对应地域和命名空间才能看到部署好的云函数。

单击函数名，在左侧选择【触发管理】，右侧【访问路径】即是上传页面的 URL。单击【API服务名】即可跳转到对应的 API 网关页面。如下图所示：
<img src="https://main.qcloudimg.com/raw/eaf30a8f73e3f9d4247690ee1830b24c.png" width="750">
测试该服务的方法为：在浏览器上直接访问页面 URL，正常情况下能看到上传页面。

#### 上传签名派发

您可以访问 [SCF 服务列表](https://console.cloud.tencent.com/scf/list) 来查看上传签名派发服务的详细信息（查看方法同 [上传页面](#p6)）。

单击函数名，在左侧选择【触发管理】，右侧【访问路径】即是该服务的 URL。单击【API服务名】即可跳转到对应的 API 网关页面。如下图所示：
<img src="https://main.qcloudimg.com/raw/2507cd4953a24bbf670af4e3659eeed5.png" width="750">
测试该服务的方法为：选择手动发送 HTTP 请求的方式，在一台有外网的 Linux 或者 Mac 上执行以下命令（请根据实际情况修改服务 URL）：
```
curl -d '' https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/ugc_upload_sign
```
如果服务正常，则返回上传签名，签名示例如下：
```
VYapc9EYdoZLzGx0CglRW4N6kuhzZWNyZXRJZD1BS0lEZk5xMzl6dG5tYW1tVzBMOXFvZERia25hUjdZa0xPM1UmY3VycmVudFRpbWVTdGFtcD0xNTg4NTg4MDIzJmV4cGlyZVRpbWU9MTU4ODU4ODYyMyZyYW5kb209MTUwNzc4JmNsYXNzSWQ9MCZvbmVUaW1lVmFsaWQ9MCZ2b2RTdWJBcHBJZD0w
```
您也可以使用 Postman 等第三方工具来发送 HTTP 请求，具体用法请自行搜索。 

### 上传页面服务代码解读

1. `main_handler()`为入口函数。
2. 读取`web_upload.html`文件的内容，即上传页面内容。
```
		html_file = open(HTML_FILE, encoding='utf-8')
		html = html_file.read()
```
3. 从`config.json`中读取配置项。配置项是指您在编写 SCF 服务时无法预知，并且需要在部署过程中才能确定的内容。这些内容由部署脚本在部署上传页面服务之前实时写入到`config.json`中。
```
		conf_file = open(CONF_FILE, encoding='utf-8')
		conf = conf_file.read()
		conf_json = json.loads(conf)
```
4. 调用`render_template`，根据上一步得到的配置信息对上传页面内容进行修改。配置项在`config.json`文件中以`"变量名": "取值"`的形式来表示；在`web_upload.html`文件中以`{变量名}`的形式来表示，**修改时请替换为具体取值**。详情如下：
```
  def render_template(html, keys):
      """将 HTML 中的变量（形式为 ${变量名}）替换为具体内容。"""
      for key, value in keys.items():
          html = html.replace("${" + key + "}", value)
      return html
```
<table>
<thead>
<tr>
<th>变量名</th>
<th>含义</th>
<th>取值类型</th>
<th>取值来源</th>
</tr>
</thead>
<tbody><tr>
<td>UGC_UPLOAD_SIGN_SERVER</td>
<td>上传签名派发服务的 URL</td>
<td>String</td>
<td>上传签名派发服务部署完成后，由 SCF 命令行工具 <a href="https://cloud.tencent.com/document/product/583/33445" target="_blank">scf</a> 输出</td>
</tr>
</tbody></table>
5. 将修改后的上传页面内容返回。返回的数据格式及含义请参见 [云函数集成响应](https://cloud.tencent.com/document/product/583/12513#.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94.E4.B8.8E.E9.80.8F.E4.BC.A0.E5.93.8D.E5.BA.94)。
  ```
      return {
          "isBase64Encoded": False,
          "statusCode": 200,
          "headers": {'Content-Type': 'text/html'},
          "body": html
      }
  ```


### 上传签名派发服务代码解读

1. `main_handler()`为入口函数。
2. 调用`parse_conf_file()`，从`config.json`文件中读取配置信息。配置项说明如下（详细参数请参见 [客户端上传签名参数](https://cloud.tencent.com/document/product/266/9221#.3Ca-id.3D.22p2.22.3E.3C.2Fa.3E.E7.AD.BE.E5.90.8D.E5.8F.82.E6.95.B0.E8.AF.B4.E6.98.8E)）：
<table>
<thead>
<tr>
<th>字段</th>
<th>数据类型</th>
<th>功能</th>
</tr>
</thead>
<tbody><tr>
<td>secret_id</td>
<td>String</td>
<td>API 密钥</td>
</tr>
<tr>
<td>secret_key</td>
<td>String</td>
<td>API 密钥</td>
</tr>
<tr>
<td>sign_expire_time</td>
<td>Integer</td>
<td>签名有效时间，单位：秒</td>
</tr>
<tr>
<td>class_id</td>
<td>Integer</td>
<td>视频上传完成后的分类 ID，0表示默认分类</td>
</tr>
<tr>
<td>otp</td>
<td>Integer</td>
<td>签名是否单次有效</td>
</tr>
<tr>
<td>subappid</td>
<td>Integer</td>
<td>是否上传到 <a href="https://cloud.tencent.com/document/product/266/14574" target="_blank">云点播子应用</a></td>
</tr>
</tbody></table>
3. 调用`parse_source_context()`，从请求 Body 中解析`sourceContext`字段，用于在 [上传完成事件通知](https://cloud.tencent.com/document/product/266/7830) 中透传给事件通知接收服务（本 Demo 暂未使用事件通知）。
>?在上传过程中该字段是可选的，如果您无需使用该功能，则可以忽略这部分代码。
4. 调用`generate_sign()`函数计算签名，详细算法请参见 [客户端上传签名](https://cloud.tencent.com/document/product/266/9221)。
5. 返回签名。返回的数据格式及含义请参见 [云函数集成响应](https://cloud.tencent.com/document/product/583/12513#.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94.E4.B8.8E.E9.80.8F.E4.BC.A0.E5.93.8D.E5.BA.94)。
  ```
      return {
          "isBase64Encoded": False,
          "statusCode": 200,
          "headers": {"Content-Type": "text/plain; charset=utf-8",
                      "Access-Control-Allow-Origin": "*",
                      "Access-Control-Allow-Methods": "POST,OPTIONS"},
          "body": str(signature, 'utf-8')
      }
  ```


