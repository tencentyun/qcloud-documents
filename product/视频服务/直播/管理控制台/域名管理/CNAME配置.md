您的域名接入云直播后，系统会为您自动分配一个 CNAME 域名（以 .liveplay.myqcloud.com 为后缀)。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受云直播服务。播放域名和推流域名均需完成 CNAME 解析。

## 注意事项
- 请前往您的域名解析服务商处配置 CNAME 记录，具体操作请咨询您的域名解析服务提供商。
- 以下以在腾讯云、阿里云、百度云、DNSPod、万网、新网配置CNAME域名解析为例，操作步骤仅供参考。如与实际配置不符，请以各自DNS服务商的信息为准。

## 前提条件
登录云直播控制台，进入[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)查看域名列表，获取域名的 CNAME 地址。
![](https://main.qcloudimg.com/raw/a1a4cf2a596a842d456897e63cff8b46.png)

## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录：
1. 登录 [域名服务控制台](https://console.cloud.tencent.com/domain)。
2. 选择您需添加 CNAME 的域名，单击【解析】。
3. 进入指定域名的域名解析页，单击【添加记录】
4. 在该新增列填写域名前缀为主机记录，选择记录类型为 CNAME，填写 CNAME 域名为记录值。
	- 记录类型：选择 `CNAME`。
	- 主机记录：填写子域名的前缀。若播放域名为 play.myqcloud.com，则添加 `play`；若需要直接解析主域名 myqloud.com，则输入`@`；若需要解析泛域名，则输入`\*`。
	- 解析路线：建议选择“默认”。
	- 记录值：填写腾讯云控制台[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)域名对应的 CNAME 值，格式为 `domain.livecdn.liveplay.myqcloud.com`。
	- TTL：建议填写10分钟。
5. 单击【保存】即可。
![](https://main.qcloudimg.com/raw/e6efcdbf6b973e84f217968bdb3653d9.png)
6. 验证 CNAME 生效。CNAME 设置完成后约15分钟生效，当云直播[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)中域名对应 CNAME 值显示![](https://main.qcloudimg.com/raw/bd92cce6703d3703582c0c2a194fd866.png)则 CNAME 成功。若 CNAME 设置完成后长时间未显示成功，可参考 [CNAME 配置问题定位。](https://cloud.tencent.com/document/product/267/30010#.E9.85.8D.E7.BD.AE.E5.AE.8C.E6.88.90-cname-.E5.90.8E.EF.BC.8C.E4.BE.9D.E6.97.A7.E6.98.BE.E7.A4.BA-cname-.E6.9C.AA.E9.85.8D.E7.BD.AE.E6.98.AF.E4.BB.80.E4.B9.88.E5.8E.9F.E5.9B.A0.EF.BC.9F)


## 阿里云设置方法
若您的 DNS 服务商为阿里云，且已完成域名备案，可参考下述步骤进行 CNAME 设置。

1.  登录阿里云控制台，进入【云解析DNS】>[【域名解析】](https://dns.console.aliyun.com/#/dns/domainList)。
2. 选择您需添加 CNAME 的域名，单击【解析设置】。
3. 选择【添加记录】，在添加记录页进行如下设置：
	-  记录类型：选择 `CNAME`。
	-  主机记录：填写子域名的前缀。若播放域名为 play.myqcloud.com，则添加 `play`；若需要直接解析主域名 myqloud.com，则输入`@`；若需要解析泛域名，则输入`\*`。
	-  解析路线：建议选择`默认`。
	-  记录值：填写腾讯云控制台域名管理页域名对应的 CNAME 值，格式为 `domain.livecdn.liveplay.myqcloud.com`。
	-  TTL：建议填写`10分钟`。
4. 单击【确定】即可。
![](https://main.qcloudimg.com/raw/c1c1966aa54b0eb263e057ed2534965b.png)
4. 验证 CNAME 生效。CNAME 设置完成后约15分钟生效，当云直播 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 中域名对应 CNAME 值显示![](https://main.qcloudimg.com/raw/ca12667bfcfd9716639c27d51f3beed3.png)则 CNAME 成功。若 CNAME 设置完成后长时间未显示成功，可参考 [CNAME 配置问题定位。](https://cloud.tencent.com/document/product/267/30010#.E9.85.8D.E7.BD.AE.E5.AE.8C.E6.88.90-cname-.E5.90.8E.EF.BC.8C.E4.BE.9D.E6.97.A7.E6.98.BE.E7.A4.BA-cname-.E6.9C.AA.E9.85.8D.E7.BD.AE.E6.98.AF.E4.BB.80.E4.B9.88.E5.8E.9F.E5.9B.A0.EF.BC.9F)

>?本文档基于阿里云 2019年10月31日版本进行说明，如阿里云控制台更新，本文档暂未更新，请根据说明路径自行调整。如无法设置成功的，请 [与客服联系](https://cloud.tencent.com/about/connect)。

## 百度云设置方法
若您的域名服务商为百度云，且已完成域名备案，可参考下述步骤进行 CNAME 设置。
1. 登录百度云控制台，选择[【域名管理】](https://console.bce.baidu.com/bcd/?_=1550137564099#/bcd/manage/list)，进入域名管理列表页。
2. 选择云直播添加的域名，在操作列单击【解析】进入 DNS 解析页面。
3. 添加解析记录，在该页面进行如下配置：
 - 主机记录：填写二级域名，即域名前缀。若播放域名为 play.myqcloud.com，则添加 `play`；若需要直接解析主域名myqloud.com，则输入`@`；若需要解析泛域名，则输入`\*`。
 - 记录类型：选择 `CNAME 记录`。
 - 解析路线：建议选择`默认`。
 - 记录值：云直播控制台域名管理页域名对应的 CNAME 值，格式为 `domain.livecdn.liveplay.myqcloud.com`。
 - TTL：建议填写`10分钟`。
4. 单击【确定】提交即可。
![](https://main.qcloudimg.com/raw/7ed00d812a79bb472c6d5395ea5c8783.png)
5. 验证 CNAME 生效。CNAME 设置完成后约15分钟生效，当云直播域名管理中域名对应 CNAME 值显示![](https://main.qcloudimg.com/raw/bd92cce6703d3703582c0c2a194fd866.png)则 CNAME 成功。若 CNAME 设置完成后长时间未显示成功，可参考 [CNAME 配置问题定位。](https://cloud.tencent.com/document/product/267/30010#.E9.85.8D.E7.BD.AE.E5.AE.8C.E6.88.90-cname-.E5.90.8E.EF.BC.8C.E4.BE.9D.E6.97.A7.E6.98.BE.E7.A4.BA-cname-.E6.9C.AA.E9.85.8D.E7.BD.AE.E6.98.AF.E4.BB.80.E4.B9.88.E5.8E.9F.E5.9B.A0.EF.BC.9F)

>?本文档基于百度云 2019年03月01日版本进行说明，如百度云控制台更新，本文档暂未更新，请根据说明路径自行调整。如 无法设置成功，请 [与客服联系](https://cloud.tencent.com/about/connect)。

## DNSPod 设置方法
若您的 DNS 服务商为 DNSPod，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/c78f494c6b550562ddb49a255f1caf0d.png)

## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/2d5e7afc347f2dd549c2e83c5e2c3f46.png)
![](https://main.qcloudimg.com/raw/0640d16350ad8d8e54ff5d8cf2230c8b.png)



## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/656a08fdc068ef7189a8aee89521fb85.png)


## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 dig 或 nslookup 命令来查询 CNAME 是否生效，如果查询到后缀为 .myqcloud.com 的域名表示域名 CNAME 已生效。
![](https://main.qcloudimg.com/raw/8684b716b879c5d8ad519b5f220b520e.png)
