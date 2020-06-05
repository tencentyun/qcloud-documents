## 使用须知

### Demo 功能介绍

本 Demo 以对 [视频上传完成事件通知](https://cloud.tencent.com/document/product/266/7830) 的接收和处理为例，向开发者展示云点播（VOD）[事件通知机制](https://cloud.tencent.com/document/product/266/33779)  的使用方法。Demo 基于云函数（SCF） 搭建了一个 HTTP 服务，用于接收来自 VOD 的事件通知请求。服务仅处理类型为 `NewFileUpload` 的事件，在解析事件通知内容后，调用 VOD 的 [`ProcessMedia`](https://cloud.tencent.com/document/product/266/33427) 接口对刚上传的视频发起转码，使用的转码模版为 [系统预置模版](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF) 100010和100020。

### 费用

本文提供的云点播事件通知接收服务 Demo 是免费开源的，但在搭建和使用的过程中可能会产生以下费用：

- 购买腾讯云云服务器（CVM）用于执行服务部署脚本，详见 [CVM 计费](https://cloud.tencent.com/document/product/213/2180)。
- 使用 SCF 提供签名派发服务，详见 [SCF 计费](https://cloud.tencent.com/document/product/583/12284) 和 [SCF 免费额度](https://cloud.tencent.com/document/product/583/12282)。
- 使用腾讯云 API 网关为 SCF 提供外网接口，详见 [API 网关计费](https://cloud.tencent.com/document/product/628/39300)。
- 消耗 VOD 存储用于存储上传的视频，详见 [存储计费](https://cloud.tencent.com/document/product/266/14666#.E8.A7.86.E9.A2.91.E5.AD.98.E5.82.A8) 和 [存储资源包](https://cloud.tencent.com/document/product/266/14667#1.-.E5.AD.98.E5.82.A8.E8.B5.84.E6.BA.90.E5.8C.85)。
- 消耗云点播转码时长用于对视频进行转码，详见 [转码计费](https://cloud.tencent.com/document/product/266/14666#.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81.3Cspan-id-.3D.22p2.22.3E.3C.2Fspan.3E) 和 [转码资源包](https://cloud.tencent.com/document/product/266/14667#3.-.E6.99.AE.E9.80.9A.E8.BD.AC.E7.A0.81.E5.8C.85)。

### 避免影响生产环境<span id="p0"></span>

事件通知接收服务 Demo 的业务逻辑使用到 VOD 事件通知机制，因此部署过程中需要开发者配置事件通知地址。如果该账号已经有基于 VOD 的生产环境，变更事件通知地址可能造成业务异常。**操作前请务必确认不会影响生产环境，如果您不能确定，请更换一个全新账号来部署 Demo**。

## 快速部署事件通知接收服务

### 步骤1：准备腾讯云 CVM<span id="p1"></span>

部署脚本需要运行在一台腾讯云 CVM 上，要求如下：

- 地域：任意。
- 机型：官网最低配置（1核1GB）即可。
- 公网：需要拥有公网 IP，带宽1Mbps或以上。
- 操作系统：官网公共镜像`Ubuntu Server 16.04.1 LTS 64位`或`Ubuntu Server 18.04.1 LTS 64位`。

购买 CVM 的方法请参见 [操作指南 - 创建实例](https://cloud.tencent.com/document/product/213/4855)。重装系统的方法请参见 [操作指南 - 重装系统](https://cloud.tencent.com/document/product/213/4933)。

>!
>
>- 事件通知接收服务 Demo 本身并不依赖于 CVM，仅使用 CVM 来执行部署脚本。
>
>- 如果您没有符合上述条件的腾讯云 CVM，也可以在其它带外网的 Linux（如 CentOS、Debian 等）或 Mac 机器上执行部署脚本，但需根据操作系统的区别修改脚本中的个别命令，具体修改方式请开发者自行搜索。

### 步骤2：开通云点播<span id="p2"></span>

请参考 [快速入门 - 步骤1](https://cloud.tencent.com/document/product/266/8757#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E4.BA.91.E7.82.B9.E6.92.AD) 开通云点播服务。

### 步骤3：获取 API 密钥和 APPID<span id="p3"></span>

事件通知接收服务 Demo 的部署和运行过程需要使用到开发者的 API 密钥（即 SecretId 和 SecretKey）和 APPID。

- 如果还未创建过密钥，请参见 [创建密钥文档](https://cloud.tencent.com/document/product/598/40488#.E5.88.9B.E5.BB.BA.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 生成新的 API 密钥；如果已创建过密钥，请参见 [查看密钥文档](https://cloud.tencent.com/document/product/598/40488#.E6.9F.A5.E7.9C.8B.E4.B8.BB.E8.B4.A6.E5.8F.B7-api-.E5.AF.86.E9.92.A5) 获取 API 密钥。
- 在控制台 [账号信息](https://console.cloud.tencent.com/developer) 页面可以查看 APPID，如下图所示：
  ![](https://main.qcloudimg.com/raw/0e7dda93add5f53b2da07d16cf6f4406.png)

### 步骤4：部署事件通知接收服务

登录 [步骤1准备的 CVM](#p1)（登录方法详见 [操作指南 - 登录 Linux](https://cloud.tencent.com/document/product/213/5436)），在远程终端输入以下命令并运行：

```
ubuntu@VM-69-2-ubuntu:~$ export SECRET_ID=AKxxxxxxxxxxxxxxxxxxxxxxx; export SECRET_KEY=xxxxxxxxxxxxxxxxxxxxx;export APPID=125xxxxxxx;git clone https://github.com/tencentyun/vod-server-demo.git ~/vod-server-demo; bash ~/vod-server-demo/installer/callback_scf.sh
```

>?请将命令中的 SECRET_ID、SECRET_KEY 和 APPID 赋值为 [步骤3](#p3) 中获取到的内容。

该命令将从 Github 下载 Demo 源码并自动执行安装脚本。安装过程需几分钟（具体取决于 CVM 网络状况），期间远程终端会打印如下示例的信息：

```
[2020-06-05 17:16:08]开始安装 pip3。
[2020-06-05 17:16:12]pip3 安装成功。
[2020-06-05 17:16:12]开始安装腾讯云 SCF 工具。
[2020-06-05 17:16:13]scf 安装成功。
[2020-06-05 17:16:13]开始配置 scf。
[2020-06-05 17:16:14]scf 配置完成。
[2020-06-05 17:16:14]开始部署云点播事件通知接收服务。
[2020-06-05 17:16:24]云点播事件通知接收服务部署完成。
[2020-06-05 17:16:26]服务地址：https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/callback
```

复制输出日志中的事件通知接收服务地址（示例中的`https://service-xxxxxxxx-125xxxxxxx.gz.apigw.tencentcs.com/release/callback`）。

> !如果输出日志中出现如下所示的警告，一般是由于 CVM 无法立即解析刚部署好的服务域名，可尝试忽略该警告。
>
> ```
> [2020-04-25 17:18:44]警告：事件通知接收服务测试不通过。
> ```

### 步骤5：配置事件通知地址并测试

如 [避免影响生产环境](#p0) 一节所述，操作之前请先确认您的线上业务不依赖于 VOD 普通回调。

登录 [VOD 控制台](https://console.cloud.tencent.com/vod/callback)，点击【设置】，回调模式选择【普通回调】，回调 URL 填写步骤4中获得的事件通知接收服务地址，回调事件全部勾选，然后点击【确定】。如下图所示：

![配置回调](https://main.qcloudimg.com/raw/80b4639ebd125e1f491f1f8fc2e48693.png)

> ! 如果您在控制台同时看到两个回调 URL 配置（2.0版本格式和3.0版本格式），请填写3.0版本，如下图：

![3.0版本格式回调配置](https://main.qcloudimg.com/raw/a6fba35464ce4e4ef4ddd37b1cfd55ce.png)

按照 [控制台上传本地视频](https://cloud.tencent.com/document/product/266/2841#.E6.9C.AC.E5.9C.B0.E4.B8.8A.E4.BC.A0.E6.AD.A5.E9.AA.A4) 的说明，上传一个测试视频到到云点播。上传完成后，在【已上传】标签页可以看到该视频的状态为“处理中”：

![视频处理中](https://main.qcloudimg.com/raw/f680a8a99bb2e5ff1a1a8b96cd87aa7c.png)

等待视频处理完成（状态变为“正常”）后，点击【快捷查看】，在页面右侧可以看到该视频有两个转码视频，如下图：

![获取视频 URL](https://main.qcloudimg.com/raw/91453a70fcc57c6e55ac95bc952a9d9f.png)

## 系统设计说明

### 系统框架

Key 防盗链主要涉及四个组成部分：控制台、、API 网关、云函数和云点播，其中 API 网关和云函数即是本 Demo 的部署对象。如下图所示：

![Key 防盗链框架](https://main.qcloudimg.com/raw/f8c60cfc1592f5fa752b77996dad8324.png)

### 接口协议

事件通知接收云函数通过 API 网关对外提供接口，具体接口协议请参考文档 [视频上传完成事件通知](https://cloud.tencent.com/document/product/266/7830)。

### 事件通知接收服务代码解读

1. `main_handler()`为入口函数。
2. 调用`parse_conf_file()`，从`config.json`文件中读取配置信息。配置项说明如下：

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
<td>region</td>
<td>String</td>
<td>云 API 请求地域，对 VOD 来说可以随意填写。</td>
</tr>
<tr>
<td>definitions</td>
<td>Array of Integer</td>
<td>转码模版</td>
</tr>
<tr>
<td>subappid</td>
<td>Integer</td>
<td>事件通知是否来自 <a href="https://cloud.tencent.com/document/product/266/14574" target="_blank">云点播子应用</a></td>
</tr>
</tbody></table>

3. 解析请求 Body，判断是否视频上传完成事件通知，是的话从中取出新上传视频的 FileId：

   ```
           body = json.loads(event["body"])
   
           event_type = body.get("EventType", None)
           if event_type == "NewFileUpload":
               upload_event = body.get("FileUploadEvent", None)
               if upload_event is None:
                   return ERR_RETURN
               fileid = upload_event.get("FileId", None)
   ```

4. 调用 `trans_media()` 发起转码，输出云 API 的回包到 SCF 日志，并回包给 VOD 的事件通知服务：

   ```
           rsp = trans_media(configuration, fileid)
           if rsp is not None:
               print(rsp)
           
           return OK_RETURN
   ```

5. `trans_media()` 中，调用云 API SDK 发起 `ProcessMedia` 请求：

```
        cred = credential.Credential(conf["secret_id"], conf["secret_key"])
        client = vod_client.VodClient(cred, conf["region"])

        method = getattr(models, API_NAME + "Request")
        req = method()
        req.from_json_string(json.dumps(params))

        method = getattr(client, API_NAME)
        rsp = method(req)
        return rsp
```

