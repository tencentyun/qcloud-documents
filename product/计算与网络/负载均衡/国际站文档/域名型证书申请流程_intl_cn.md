## 申请域名型（DV）SSL证书

### 1. 申请入口

进入SSL证书管理控制台
![](https://mc.qcloudimg.com/static/img/f990389699184b164082dce1ebe809c6/1.png)

点击【申请证书】
![](https://mc.qcloudimg.com/static/img/4efe78b416cc29cacba1cbc2ba475bb6/2.png)

查看申请域名型证书型号，点击【确定】

![](https://mc.qcloudimg.com/static/img/287bd4f6c633cb1a81e18a096f47d5ed/3.png)

### 2. 填写申请

填写申请域名，注意不支持一级域名申请（例如qcloud.com），请填写例如cloud.tencent.com，demo.test.qlcoud.com形式二级、三级等域名。
![](https://mc.qcloudimg.com/static/img/4961164252cd488c9695475e173c0b8c/4.png)

## 3. DNS验证
### 3.1 手动DNS验证方式

证书默认支持收到DNS验证，验证方法可查看[详情](https://cloud.tencent.com/doc/product/400/4142#2.-.E6.89.8B.E5.8A.A8dns.E9.AA.8C.E8.AF.81)。
![](https://mc.qcloudimg.com/static/img/2f90c6cdf51ec98ba0fd7a112a891e13/5.png)

### 3.2 选择自动DNS验证方式

如果所申请域名成功添加[云解析平台](https://console.cloud.tencent.com/cns/domains)，可以支持自动DNS验证，验证方法可查看[详情](https://cloud.tencent.com/doc/product/400/4142#1.-.E8.87.AA.E5.8A.A8dns.E9.AA.8C.E8.AF.81)。
![](https://mc.qcloudimg.com/static/img/8c10bfb9fa50a520e0b8b45f3b7a9f74/6.png)

## 4. 提交申请
### 4.1 提交申请后验证身份

提交申请成功后弹窗提示如下，需要前往【证书详情页】获取CName记录添加解析：
![](https://mc.qcloudimg.com/static/img/7d99496ed47a163a3ee25c728187bf45/7.png)

获取CName记录如Tips中显示，需要尽快成功添加解析，方可通过CA机构审核：
![](https://mc.qcloudimg.com/static/img/1f0d7d113cd4ee14cda423a32e853fe4/8.png)

### 4.2 提交申请失败

如遇到下图所示弹窗，是提交域名未通过CA机构安全审核，具体原因参考[安全审核失败原因](https://cloud.tencent.com/doc/product/400/5439)。
![](https://mc.qcloudimg.com/static/img/25451d24cf3c717454830a44925642ec/1.png)
