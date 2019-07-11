您的域名接入云直播后，系统会为您自动分配一个 CNAME 域名（以 .liveplay.myqcloud.com 为后缀)。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受云直播服务。播放域名和推流域名均需完成 CNAME 解析。

## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录：
1. 登录 [域名服务控制台](https://console.cloud.tencent.com/domain)，单击要添加 CNAME 记录的域名右侧的【解析】。
![](https://main.qcloudimg.com/raw/418d01dad6a985c9f43995aafe48c95b.png)

2. 跳转到指定域名的域名解析页面，单击【添加记录】。
![](https://main.qcloudimg.com/raw/d0448ff0f3a6c74706e5e70dd8a52f53.png)
3. 在【主机记录】处选填写域名前缀（如：www，若需要直接解析主域名，则输入@；若需要解析泛域名，则输入\*），将【记录类型】设置为 CNAME，在【记录值】处填写 CNAME 域名，单击【保存】，即可添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/b734c87a34556a2be4bf3144d1549a50.png)

## 阿里云设置方法
若您的域名服务商为阿里云，且已完成域名备案，可参考下述步骤进行 CNAME 设置。
1. 登录腾讯云控制台，通过导航栏进入 [云直播服务](https://console.cloud.tencent.com/live)。单击左侧侧边栏【域名管理】，进入域名管理页，获取 CNAME 地址。
![](https://main.qcloudimg.com/raw/2fe116b9f76a910c84f162f9e80baf04.png)

2. 登录阿里云控制台，通过导航栏进入 [域名服务](https://dns.console.aliyun.com/#/dns/domainList)。单击左侧边栏【云解析 DNS】，进入域名管理页。
![](https://main.qcloudimg.com/raw/bd8dd79b92fd4e1200f76df1366dc47e.png)

3. 在操作列单击【解析设置】进入 DNS 解析页面，如下图所示：
![](https://main.qcloudimg.com/raw/af1df31710fa114949efdc334678308f.png)

4. 选择需要配置的域名，选择右上角【添加记录】，如下图所示：
![](https://main.qcloudimg.com/raw/2f3b789874c7c7968679e6282c14f260.png)

 - 记录类型：选 CNAME。
 - 主机记录：填写子域名的前缀。若播放域名为 play.myqcloud.com，则添加 play；若需要直接解析主域名 myqloud.com，则输入@；若需要解析泛域名，则输入\*。
 - 解析路线：建议选择“默认”。
 - 记录值：填写腾讯云控制台域名管理页域名对应的 CNAME 值，格式为 domain.livecdn.liveplay.myqcloud.com。
 - TTL：建议填写10分钟。
单击【确定】提交即可。

5. 验证 CNAME 生效。CNAME 设置完成后约15分钟生效，当云直播域名管理中域名对应 CNAME 值显示<img src="https://main.qcloudimg.com/raw/8283d3a1d6e6993df5b81f5034b3bbb9.png"  style="margin:0;">则 CNAME 成功。若 CNAME 设置完成后长时间未显示成功，可参考 [CNAME 配置问题定位。](https://cloud.tencent.com/document/product/267/30010#.E9.85.8D.E7.BD.AE.E5.AE.8C.E6.88.90-cname-.E5.90.8E.EF.BC.8C.E4.BE.9D.E6.97.A7.E6.98.BE.E7.A4.BA-cname-.E6.9C.AA.E9.85.8D.E7.BD.AE.E6.98.AF.E4.BB.80.E4.B9.88.E5.8E.9F.E5.9B.A0.EF.BC.9F)

>?本文档基于阿里云 2019年03月01日版本进行说明，如阿里云控制台更新，本文档暂未更新，请根据说明路径自行调整。如无法设置成功的，请 [与客服联系](https://cloud.tencent.com/about/connect)。

## 百度云设置方法
若您的域名服务商为百度云，且已完成域名备案，可参考下述步骤进行 CNAME 设置。
1. 登录腾讯云控制台，通过导航栏进入 [云直播服务](https://console.cloud.tencent.com/live)。单击左侧侧边栏【域名管理】，进入域名管理页，获取 CNAME 地址。
![](https://main.qcloudimg.com/raw/d5e022e12c9904cb482fb469dd73510b.png)

2. 登录百度云控制台，通过导航栏进入 [域名服务](https://console.bce.baidu.com/bcd/?_=1550137564099#/bcd/manage/list)。单击左侧边栏【域名管理】，进入域名管理列表页。
![](https://main.qcloudimg.com/raw/3e992eb24f22f68f36cb987813a1b6cd.png)

3. 选择云直播添加的域名，在操作列单击【解析】进入 DNS 解析页面，如下图所示：
![](https://main.qcloudimg.com/raw/f139c87b258c48981075de341c92e603.png)

4. 添加解析记录，如下图所示：
![](https://main.qcloudimg.com/raw/e7c11bc00e33e59676eb2945f1a4f963.png)
 - 主机记录：填写二级域名，即域名前缀。若播放域名为 play.myqcloud.com，则添加 play；若需要直接解析主域名myqloud.com，则输入@；若需要解析泛域名，则输入\*。
 - 记录类型：CNAME 记录。
 - 解析路线：建议选择“默认”。
 - 记录值：云直播控制台域名管理页域名对应的 CNAME 值，格式为 domain.livecdn.liveplay.myqcloud.com。
 - TTL：建议填写10分钟。
单击【确定】提交即可。

5. 验证 CNAME 生效。CNAME 设置完成后约15分钟生效，当云直播域名管理中域名对应 CNAME 值显示<img src="https://main.qcloudimg.com/raw/8283d3a1d6e6993df5b81f5034b3bbb9.png"  style="margin:0;">则 CNAME 成功。若 CNAME 设置完成后长时间未显示成功，可参考 [CNAME 配置问题定位。](https://cloud.tencent.com/document/product/267/30010#.E9.85.8D.E7.BD.AE.E5.AE.8C.E6.88.90-cname-.E5.90.8E.EF.BC.8C.E4.BE.9D.E6.97.A7.E6.98.BE.E7.A4.BA-cname-.E6.9C.AA.E9.85.8D.E7.BD.AE.E6.98.AF.E4.BB.80.E4.B9.88.E5.8E.9F.E5.9B.A0.EF.BC.9F)

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
![](https://main.qcloudimg.com/raw/caaa0fb6c0af5d58cc8012e9d090b5b9.png)


## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 dig 或 nslookup 命令来查询 CNAME 是否生效，如果查询到后缀为 .myqcloud.com 的域名表示域名 CNAME 已生效。
![](https://main.qcloudimg.com/raw/cc49dc693d41eefdc0130f0b8b3439e1.png)
