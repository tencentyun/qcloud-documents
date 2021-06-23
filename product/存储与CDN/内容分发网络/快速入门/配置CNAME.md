您的域名接入 CDN 后，系统会为您自动分配一个以 `.cdn.dnsv1.com` 为后缀的 CNAME 域名，可在 CDN 控制台 [域名管理页](https://console.cloud.tencent.com/cdn/domains) 查看。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 CDN 加速服务。
![img](https://main.qcloudimg.com/raw/64aa3f78c45b66f2387d64b54d77f75d.png)

## 配置步骤

本文提供腾讯云和阿里云的 CNAME 配置步骤说明，您可以根据域名所在的服务商进行设置：

- [腾讯云设置方法](#m1)
- [阿里云设置方法](#m2)

[](id:m1)
### 腾讯云设置方法

> !域名解析各种记录类型之间是有优先级差异的，在主机记录相同的情况下，同一条线路有几种不同的记录类型不能共存，否则将会提示冲突。CNAME 记录与除 CNAME 记录以外的任何记录类型都冲突，需要先删除掉其他记录，再进行配置。详情请参见 [为什么添加解析记录的时候提示 "记录有冲突" ](https://cloud.tencent.com/document/product/302/3468#.E4.B8.BA.E4.BB.80.E4.B9.88.E6.B7.BB.E5.8A.A0.E8.A7.A3.E6.9E.90.E8.AE.B0.E5.BD.95.E7.9A.84.E6.97.B6.E5.80.99.E6.8F.90.E7.A4.BA-.26quot.3B.E8.AE.B0.E5.BD.95.E6.9C.89.E5.86.B2.E7.AA.81.26quot.3B-.EF.BC.9F)。

以下视频将为您演示如何在腾讯云中对 CDN 的接入域名、CNAME 记录进行配置，从而实现使用 CDN 进行加速的效果：

<iframe src="https://cloud.tencent.com/edu/learning/quick-play/2209-31077?source=gw.doc.media&amp;withPoster=1&amp;notip=1" allowfullscreen="true" style="border-width: 0px; border-style: none; box-sizing: border-box; list-style: inherit; display: block; width: 610px; height: 380px;"></iframe>

1. 登录 [域名服务](https://console.cloud.tencent.com/domain) 控制台，在列表中，找到需要添加 CNAME 记录的域名所在行，单击操作栏的【解析】。
   ![CNAME配置](https://main.qcloudimg.com/raw/dd299f2ef44538523622a7de978d5995.png)
2. 在跳转到的DNSPOD页面中，单击【添加记录】，通过如下步骤添加 CNAME 记录。
   ![img](https://main.qcloudimg.com/raw/489791e8d992b47ed300e30899050c67.png)
	- **主机记录**：填写子域名。例如，要添加 `www.dnspod.com`这个域名的解析，您在 “主机记录” 处选择 “www” 即可。如果只是想添加 `dnspod.com` 这个域名的解析，您在 “主机记录” 处选择 “@” 即可。
	- **记录类型**：选择 “CNAME”。
	- **线路类型**：选择 “默认” 类型。DNSPod 支持按多种方式划分线路，让指定用户访问该记录。详细说明请查看[解析线路说明](https://docs.dnspod.cn/dns/5f4775898ae73e11c5b01afc/)
	- **记录值**：指向的域名，一般填写加速域名的 CNAME 值：xxx.xxx.com.cdn.dnsv1.com。记录生成后会自动在域名后面补一个“.”，这是正常现象。
	- **权重**：同一条主机记录相同的线路,可以针对不同的记录值设置权重,解析时将根据设置的权重比例进行返回。输入范围
		为0-100的整数。
	- **MX 优先级**：不需要填写。
	- **TTL**：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
3. 填写完成后，单击【确认】，即可完成CNAME配置。

   

####  扩展设置
- 您可以将单个主机记录的【线路类型】设置为 “默认” ，则是为整站开启加速服务。
例如，您需要将所有用户都指向 `1.com`，您可以通过添加线路类型为默认、记录值为`1.com`的这一条 CANME 记录来实现。
![img](https://main.qcloudimg.com/raw/be770e0f8b91c33ae7c41f1e50e633af.png)

- 您也可以分线路开启加速服务。
如果您需要将移动用户指向 `1.com`，联通用户都指向 `2.com`。您可以通过添加【线路类型】为“移动”、记录值为`1.com` 和【线路类型】为“联通”、记录值为 `2.com` 的两条 CNAME 记录来实现。
 ![](https://main.qcloudimg.com/raw/a10e6be051e2b90a323cb8e07081fb63.png)

>?更多线路配置说明请查看 [解析线路说明](https://docs.dnspod.cn/dns/5f4775898ae73e11c5b01afc/)。



[](id:m2)
### 阿里云设置方法

若您的 DNS 服务商为阿里云，您可通过如下步骤添加 CNAME 记录。

1. 登录阿里云控制台云解析DNS。
2. 单击要解析的域名，进入解析记录页。
3. 进入解析记录页后，单击【添加记录】按钮，开始设置解析记录。
4. 若要设置 CNAME 解析记录，将记录类型选择为 CNAME。主机记录即域名前缀，可任意填写（如：`www`）。记录值填写为当前域名指向的另一个域名。解析线路，TTL 默认即可。
![img](https://main.qcloudimg.com/raw/1e5d2b3e6e142b5f0900cc4065bd0864.png)
5. 填写完成后，单击【确认】，即可完成解析设置。



## 验证 CNAME 是否生效

最后，不同的 DNS 服务商，CNAME 生效的时间略有不同，一般在半个小时之内生效。您可以通过 nslookup 或 dig 的方式来查询 CNAME 是否生效，若应答的CNAME记录是我们配置的CNAME，则说明配置成功，此时您已成功开启加速服务。

- `nslookup -qt=cname <加速域名>`
  ![img](https://main.qcloudimg.com/raw/ed15d49b7d2fee9cf8830d4bf9ca51a2.png)
- `dig <加速域名>`
  ![img](https://main.qcloudimg.com/raw/2ba5ec76f1671c3b8ee345cef896de10.png)
