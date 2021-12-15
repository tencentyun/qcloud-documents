域名接入云直播后，系统会为您自动分配一个 CNAME 域名（以`.tlivecdn.com`为后缀)，可在 **[域名管理](https://console.cloud.tencent.com/live/domainmanage)** 列表中查看。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受云直播服务。

以下视频将为您介绍如何在腾讯云配置域名 CNAME 解析的过程：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2751-53266?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 注意事项
- 推流域名和播放域名均需完成 CNAME 解析。
- 请前往您的域名解析服务商处配置 CNAME 记录，具体操作请咨询您的域名解析服务提供商。
- CNAME 设置完成后约15分钟生效。若您设置多层 CNAME，云直播无法有效监测解析结果，请以实际的访问情况为参考。
- 若 CNAME 设置完成后长时间未显示成功，请参见 [域名配置相关](https://cloud.tencent.com/document/product/267/45252)。

## 前提条件
- 已准备域名，并完成域名备案。
	- 若您需要购买自有域名，可前往[ ](https://cloud.tencent.com/document/product/242/9595)[**域名注册**](https://cloud.tencent.com/document/product/242/9595)[ ](https://cloud.tencent.com/document/product/242/9595)完成 [域名购买](https://buy.cloud.tencent.com/domain?from=console)。您也可以前往其它域名服务商进行购买。
	- 若您的域名未完成备案，您可前往腾讯云的 [网站备案](https://cloud.tencent.com/product/ba) 完成域名备案。
- 已在云直播控制台的 **[域名管理](https://console.cloud.tencent.com/live/domainmanage)** 中成功 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)，且域名 CNAME 地址状态为![](https://main.qcloudimg.com/raw/ed1ac2f8541f629814a3f2420b1eb79c.png)（CNAME 未配置）。



## 配置步骤
本文以在腾讯云、阿里云、百度云、DNSPod、万网、新网配置 CNAME 域名解析为例。操作步骤仅供参考，如与实际配置不符，请以各自 DNS 服务商的信息为准。域名 CNAME 设置完成后，您可根据 [验证 CNAME 是否生效](#check) 所述方法验证域名是否已 CNAME 成功。


[](id:tencent)
### 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可根据如下步骤添加 CNAME 记录。

1. 登录 [域名服务控制台](https://console.cloud.tencent.com/domain)。
2. 选择您需添加 CNAME 的域名，单击 **解析**。
3. 进入指定域名的域名解析页，单击 **添加记录**。
4. 在该新增列填写域名 CNAME 记录，具体填写内容如下所示：
<table>
    <tr><th width="12%" >参数名</th><th width="38%">参数描述</th><th width="50%">如何配置</th></tr>
    <tr>
    <td><a href="https://cloud.tencent.com/document/product/302/3468#.E4.B8.BB.E6.9C.BA.E8.AE.B0.E5.BD.95.E7.9A.84.E7.94.A8.E6.B3.95.E6.9C.89.E4.BB.80.E4.B9.88.EF.BC.9F">主机记录</a>  </td>
        <td>填写子域名的前缀  </td>
        <td>
            <ul style="margin-bottom:0;">
                <li>若域名为<code>play.myqcloud.com</code>，请选择：<code>play</code></li>
                <li>若解析主域名<code>myqloud.com</code>，请选择：<code>@</code></li>
                <li>若解析泛域名，请选择：<code>\*</code></li>
            </ul>
        </td>
    </tr>
    <tr>
    <td><a href="https://cloud.tencent.com/document/product/302/3468#.E8.AE.B0.E5.BD.95.E7.B1.BB.E5.9E.8B.E7.9A.84.E5.90.AB.E4.B9.89.E6.98.AF.E4.BB.80.E4.B9.88.EF.BC.9F">记录类型</a></td>
        <td>记录类型，此处为 CNAME 类型</td>
        <td>将域名指向另一个域名，请选择：<b>CNAME</b></td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/302/3468#.E7.BA.BF.E8.B7.AF.E7.9A.84.E7.94.A8.E6.B3.95.E6.9C.89.E4.BB.80.E4.B9.88.EF.BC.9F">线路类型</a></td>
        <td>用于 DNS 服务器在解析域名时，根据访问者的来源，返回对应的服务器 IP 地址</td>
        <td>选择：<b>默认</b></td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/302/3468#.E8.AE.B0.E5.BD.95.E5.80.BC.E5.A6.82.E4.BD.95.E5.A1.AB.E5.86.99.EF.BC.9F">记录值</a></td>
        <td>需指向的域名，填写腾讯云控制台 **<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>** 域名对应的 CNAME 值</td>
        <td>在 **<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>** 里查看对应域名分配的未配置 CNAME，复制填至 **记录值**。填写格式为：<ul style="margin:0">
            <li/><code><b style="color:red;">xxxx</b>.tlivecdn.com</code>
            <li/><code><b style="color:red;">xxxx</b>.tlivepush.com</code>
            </ul></td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/302/3468#.E8.AE.B0.E5.BD.95.E5.80.BC.E5.A6.82.E4.BD.95.E5.A1.AB.E5.86.99.EF.BC.9F">TTL(秒)</a></td>
        <td>缓存的生存时间，默认最常用的<b>600秒</b></td>
        <td>建议填写<b>600秒</b></td>
    </tr>
</table>
5. 单击 **保存**，配置 CNAME 完毕。
![](https://main.qcloudimg.com/raw/d7babb75869f1b8285e32bff75ccf817.png)

>! 
>- 更多域名解析记录相关问题，请参见 [主机记录和记录值](https://cloud.tencent.com/document/product/302/3468)。
>- 域名解析各种记录类型之间是有优先级差异的，在主机记录相同的情况下，同一条线路有几种不同的记录类型不能共存，否则将会提示冲突。CNAME 记录与除 CNAME 记录以外的任何记录类型都冲突，需要先删除掉其他记录，再进行配置。详情请参见 [为什么添加解析记录的时候提示 "记录有冲突" ](https://cloud.tencent.com/document/product/302/3468#.E4.B8.BA.E4.BB.80.E4.B9.88.E6.B7.BB.E5.8A.A0.E8.A7.A3.E6.9E.90.E8.AE.B0.E5.BD.95.E7.9A.84.E6.97.B6.E5.80.99.E6.8F.90.E7.A4.BA-.26quot.3B.E8.AE.B0.E5.BD.95.E6.9C.89.E5.86.B2.E7.AA.81.26quot.3B-.EF.BC.9F)。

[](id:ali)
### 阿里云设置方法
若您的 DNS 服务商为阿里云，且已完成域名备案，可参考下述步骤进行 CNAME 设置。

1.  登录阿里云控制台，进入 **云解析DNS** >[ **域名解析** ](https://dns.console.aliyun.com/#/dns/domainList)。
2. 选择您需添加 CNAME 的域名，单击 **解析设置**。
3. 选择 **添加记录**，在添加记录页进行如下设置：
  -  记录类型：选择 `CNAME`。
  -  主机记录：填写子域名的前缀。若播放域名为`play.myqcloud.com`，则添加`play`；若需要直接解析主域名`myqloud.com`，则输入`@`；若需要解析泛域名，则输入`\*`。
  -  解析路线：建议选择`默认`。
  -  记录值：填写腾讯云控制台域名管理页域名对应的 CNAME 值，格式为`domain.tlivecdn.com`。
  -  TTL：建议填写`10分钟`。
4. 单击 **确定** 即可。

![](https://main.qcloudimg.com/raw/28612fcd318e59e517165caf60591648.png)


[](id:baidu)
### 百度云设置方法
若您的域名服务商为百度云，您可通过如下步骤添加 CNAME 记录。
1. 登录百度云控制台，选择[ **域名管理** ](https://console.bce.baidu.com/bcd/?_=1550137564099#/bcd/manage/list)，进入域名管理列表页。
2. 选择云直播添加的域名，在操作列单击 **解析** 进入 DNS 解析页面。
3. 添加解析记录，在该页面进行如下配置：
 - 主机记录：填写二级域名，即域名前缀。若播放域名为`play.myqcloud.com`，则添加`play`；若需要直接解析主域名`myqloud.com`，则输入`@`；若需要解析泛域名，则输入`\*`。
 - 记录类型：选择 `CNAME 记录`。
 - 解析路线：建议选择`默认`。
 - 记录值：云直播控制台域名管理页域名对应的 CNAME 值，格式为`domain.tlivecdn.com`。
 - TTL：建议填写`10分钟`。
4. 单击 **确定** 提交即可。
![](https://main.qcloudimg.com/raw/cd4305b5313e8d4a61772745e3c10e12.png)

[](id:dnspod)
### DNSPod 设置方法
若您的 DNS 服务商为 DNSPod，您可通过如下步骤添加 CNAME 记录。
1. 登录 [DNSPod 域名服务控制台](https://console.dnspod.cn/dns/list)。
2. 在列表中，找到需要添加 CNAME 记录的域名所在行，单击对应域名名称，跳转至“添加记录”界面。
3. 通过如下步骤添加 CNAME 记录：
  1. 主机记录处填子域名（例如需要添加`www.123.com`的解析，只需要在主机记录处填写`www`即可。如果只是想添加`123.com`的解析，主机记录直接留空，系统会自动填一个“@”到输入框内，@的 CNAME 会影响到 MX 记录的正常解析，添加时慎重考虑）。
  2. 记录类型为 CNAME。
  3. 线路类型（默认为必填项，否则会导致部分用户无法解析。在上图中，默认的作用为：除了联通用户之外的所有用户，都会指向 1.com）。
  4. 记录值为 CNAME 指向的域名，只可以填写域名，记录生成后会自动在域名后面补一个“.”，这是正常现象。
  5. MX 优先级不需要填写。
  6. TTL 不需要填写，添加时系统会自动生成，默认为600秒（TTL 为缓存时间，数值越小，修改记录各地生效时间越快）。
![](https://main.qcloudimg.com/raw/ee19f4ea9269c340d8622a945e86fb87.png)


[](id:wwwnet)
### 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。

1. 登录万网会员中心。
2. 单击会员中心左侧导航栏中的 **产品管理** ->  **我的云解析** 进入万维网云解析列表页。
3. 单击要解析的域名，进入解析记录页。
4. 进入解析记录页后，单击 **新增解析**，开始设置解析记录。
5. 若要设置 CNAME 解析记录，将记录类型选择为 CNAME。主机记录即域名前缀，可任意填写（如：`www`）。记录值填写为当前域名指向的另一个域名。解析线路，TTL 默认即可。
![](https://main.qcloudimg.com/raw/3ffd9282393424cd721b48b26f166d4d.png)
6. 填写完成后，单击 **保存**，完成解析设置。


[](id:xinnet)
### 新网设置方法
若您的 DNS 服务商为新网，您可通过**设置别名（CNAME 记录）**添加 CNAME 记录。
别名记录允许将多个名字映射到同一台计算机。通常用于同时提供 WWW 和 MAIL 服务的计算机。例如，有一台计算机名为`host.mydomain.com`（A记录）。它同时提供 WWW 和 MAIL 服务，为了便于用户访问服务。可以为该计算机设置两个别名（CNAME）：WWW 和 MAIL 。如下图：
![](https://main.qcloudimg.com/raw/48a5cb7a7301e49edb85edbc19e1bcbd.png)

[](id:check)
## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您可通过以下方式查询 CNAME 是否配置生效。
- **方法1：**进入云直播控制台的 **[域名管理](https://console.cloud.tencent.com/live/domainmanage)** 查询后缀为`.myqcloud.com`的域名状态符号是否变成![](https://main.qcloudimg.com/raw/0fc346399ae095d69113d4944e511a20.png)表明 CNAME 已成功。
![](https://main.qcloudimg.com/raw/b5150f5442f48a38bf9a972a84f43122.png)
- **方法2：**Linux/Mac 系统下，通过 dig 命令查看，命令格式为：`dig 自有域名`。若第一行显示解析到云直播提供的目标域名，表明 CNAME 已成功。 
![](https://main.qcloudimg.com/raw/2cbe7fdc1c9d7dbed7851aa86dd64ff1.png)
- **方法3：**Windows 系统，可通过 **开始** → **运行** →输入 cmd 并回车，在命令行模式下输入：`nslookup 自有域名`。若已解析至云直播提供的目标域名，表明 CNAME 已成功。
![](https://main.qcloudimg.com/raw/765ac099e7c79a70496563f00cdab9a7.png)


>!若 CNAME 设置完成后长时间未显示成功，可参考 [域名配置相关](https://cloud.tencent.com/document/product/267/45252)。
