在使用云函数 SCF 进行函数计算时，会产生大量的函数运行日志，云函数 SCF 运行日志已经和腾讯云的日志服务 CLS 平台打通，实时采集函数运行日志至日志服务平台。在日志服务平台您可以进行检索、投递和消费等更多操作。
![](https://main.qcloudimg.com/raw/ceb1528c2150af09913cac3c0a77f420.png)

## 前提条件

已开通 [日志服务](https://cloud.tencent.com/product/cls)。



## 接入步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，创建日志集以及日志主题（日志集地域请选择函数服务所在地域，暂不支持跨地域日志推送），详情请参见  [创建日志集和日志主题](https://cloud.tencent.com/document/product/614/34340)。

2. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，在左侧导航栏中，单击【函数服务】，进入函数服务列表页。

3. 单击需要实时采集日志的函数名，进入**函数配置**页面，单击右上角的【编辑】，编辑函数信息。

4. 在**函数配置**中，为该函数服务配置步骤1创建好的日志集和日志主题，并单击【保存】。
   ![](https://main.qcloudimg.com/raw/567e0889f2777caa4f1b15a82be6ef6b.jpg)

5. 至此您已成功接入日志服务平台。如需进行日志检索，需要手动开启索引。
   请您登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，单击【日志集管理】，并依次进入目标日志集、日志主题，在日志主题选项卡中，在日志主题右侧的操作栏中，选择【管理配置】>【索引配置】，进入索引配置页面。
   ![](https://main.qcloudimg.com/raw/9e0c82b2e14b0dafc7aceb2deb21af5b.png)

6. 单击右上角的【编辑】，打开索引状态，开启全文索引，点击保存。
   ![](https://main.qcloudimg.com/raw/8e7c084d37b9c9e46750a949d66f231b.png)

   > ?如需进行更多操作如日志实时检索，日志投递消费等，请登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。更多功能请参见 [日志服务文档](https://cloud.tencent.com/document/product/614)。

## 实时检索示例

使用实时检索功能之前，请确保您的函数服务日志已接入日志服务平台，并且需检索的日志主题已开启索引功能。若未开启索引，可参见文档 [开启索引](https://cloud.tencent.com/document/product/614/16981)。

1. 登陆 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏单击【日志检索】，进入到日志检索页。
2. 选择检索的时间范围和日志主题，在输入框填写检索语法（语法支持关键词检索、模糊检索、范围检索等方式，详情参考 [语法规则](https://cloud.tencent.com/document/product/614/16982)）.
3. 单击【搜索】，即可检索日志。
   如图示例：检索包含 Memory 的日志数据.
   ![](https://main.qcloudimg.com/raw/0137def3872bbce2911cfeef416d3a83.png)
