# SCF 云函数日志接入

在使用云函数（SCF）进行函数计算时，会产生大量的函数运行日志，云函数（SCF）运行日志已经和腾讯云的日志服务（CLS）平台打通，实时采集函数运行日志至日志服务平台。在日志服务平台您可以进行检索、投递和消费等更多操作。
![](https://main.qcloudimg.com/raw/ceb1528c2150af09913cac3c0a77f420.png)

## 接入步骤

1. 使用云函数实时日志服务功能之前，需要您开通[日志服务](https://cloud.tencent.com/product/cls)，并在[日志服务控制台](https://console.cloud.tencent.com/cls)上创建好日志集以及日志主题（日志集地域请选择函数服务所在地域，暂不支持跨地域日志推送），具体操作步骤请参见[创建日志集和日志主题](https://cloud.tencent.com/document/product/614/34340)。
   ![](https://main.qcloudimg.com/raw/3badd6648a7bff7587098fb4ded4f2ac.png)
2. 登录[云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，选择导航栏**函数服务**，点击需要实时采集日志的函数名，进入**函数配置**页面，点击**编辑**。
   ![](https://main.qcloudimg.com/raw/3a3c027710b2ef538586e681d0bd0b1d.png)
3. 在**函数配置**中，为该函数服务配置之前已创建好的日志集和日志主题，点击保存。
   ![](https://main.qcloudimg.com/raw/21c4bcebc1a8597b3c2082fb0248bf76.png)
4. 您已成功接入日志服务平台。如需进行日志检索，需要手动开启索引。请您登录[日志服务控制台](https://console.cloud.tencent.com/cls)，导航栏选择日志集管理，依次进入目标日志集、日志主题，在日志主题选项卡中，选择**索引配置**。
   ![](https://main.qcloudimg.com/raw/9e0c82b2e14b0dafc7aceb2deb21af5b.png)
5. 点击编辑，打开索引状态，开启全文索引，点击保存。
   ![](https://main.qcloudimg.com/raw/f7b1fe01a789b3231f51a22f49ca3313.png)
   如需进行更多操作如日志实时检索，日志投递消费等，请登录[日志服务控制台](https://console.cloud.tencent.com/cls)。更多功能请参见[日志服务文档](https://cloud.tencent.com/document/product/614)。

## 实时检索示例

使用实时检索功能之前，请确保您的函数服务日志已接入日志服务平台，并且需检索的日志主题已开启索引功能。如未开启索引，可参见文档[开启索引](https://cloud.tencent.com/document/product/614/16981)。
登陆 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏单击**日志检索**，进入到日志检索页。选择检索的时间范围和日志主题，然后在输入框填写检索语法（语法支持关键词检索、模糊检索、范围检索等方式，详情参考 [语法规则](https://cloud.tencent.com/document/product/614/16982)），最后单击**搜索**，即可检索日志。
如：检索包含Memory的日志数据

```
Memory
```

![](https://main.qcloudimg.com/raw/5d26d0da9aa86f9eb6fbea1f544d9420.png)
