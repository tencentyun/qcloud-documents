## 概述

日志服务（Cloud Log Service，CLS）提供一站式的日志数据解决方案。您无需关注扩缩容等资源问题，五分钟快速便捷接入，即可享受日志的采集、存储、加工、检索分析、消费投递、生成仪表盘、告警等全方位稳定可靠服务。全面提升问题定位、指标监控的效率，大大降低日志运维门槛。

为了帮助您快速入门日志服务，本文将演示如何使用日志服务的基本功能：
- 使用 LogListener 采集服务器中的日志文件。
- 检索分析日志。

如果您没有合适的资源来采集日志，可 [使用 Demo 日志快速体验 CLS](https://cloud.tencent.com/document/product/614/64538)，无需采集日志即可体验日志检索分析、仪表盘和告警功能，且不产生任何费用。


## 步骤1：开通服务

登录 [腾讯云日志服务控制台](https://console.cloud.tencent.com/cls/overview)。若您的账户此前未开通日志服务，该页面将提示您开通，单击**开通**即可。

## 步骤2：安装 LogListener

LogListener 是日志服务的采集客户端，通过 LogListener 可将日志文件采集至日志服务。下文将演示如何在腾讯云 CVM/Lighthouse 中安装 LogListener。
此外，LogListener 也支持 [非腾讯云服务器](https://cloud.tencent.com/document/product/614/17414)、[容器服务 TKE](https://cloud.tencent.com/document/product/457/36771) 和 [自建 K8s 集群](https://cloud.tencent.com/document/product/614/61244)。

#### 步骤2.1：获取密钥

登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)，查看（或创建）并记录密钥，并确认密钥状态为启用。
![](https://main.qcloudimg.com/raw/def581cc17891febfab6ecd1d616327c.png)

#### 步骤2.2：安装 LogListener

1. 前往 [机器组管理](https://console.cloud.tencent.com/cls/hosts)，在页面左上角将地域切换为需要安装 LogListener 的CVM/Lighthouse 所属的地域，单击页面右上角**实例批量部署**。
![](https://qcloudimg.tencent-cloud.cn/raw/902899636f58398872a39c417a857b5a.png)
2. 勾选需要安装 LogListener 的机器实例，在**输入 SecretId 信息**中填写步骤2.1的 **SecretId** 及 **SecretKey**，并填写**机器标识**（例如 test，相当于对机器实例的分类，便于后续按照该标识批量采集多台机器的日志）。
![](https://qcloudimg.tencent-cloud.cn/raw/b9bc1a8df98d1fb7b60f0fe4de0a02e6.png)
3. 等待安装完成后，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/66ba1bb5f90a5b4cc125678d6b0f964a.png)
4. 将安装好 LogListener 的机器实例加入至新的机器组中（机器组是一组需要采集日志的机器实例列表，可针对同一机器组内的多个实例批量采集相同路径下的日志文件），填写**机器组名称**，单击**加入**。
![](https://qcloudimg.tencent-cloud.cn/raw/e9ddc47a57cbffaf23f0fb3b0b2db478.png)

## 步骤3：创建日志主题

日志主题是日志数据采集、存储、检索和分析的基本单元，一个日志主题通常对应某一个应用/服务（具备类似的日志结构）。还可以使用日志集对日志主题进行分组，日志集本身不存储任何日志数据，仅方便用户管理日志主题。

1. 前往 [日志主题](https://console.cloud.tencent.com/cls/topic) 管理页面，在页面左上角将地域切换为步骤2.2的地域，单击**创建日志主题**。
![](https://qcloudimg.tencent-cloud.cn/raw/037dda612aa5c1f6751bdd3aac7c9034.png)
2. 在弹出的创建日志主题窗口中，填写相关信息，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/7038d575db8cbe2af535e2837a5714b5.png)
 - 日志主题名称：例如 test
 - 存储类型：标准存储
 - 日志集操作：创建日志集
 - 日志集名称：例如 test

## 步骤4：配置采集规则及索引配置

1. 前往 [日志主题](https://console.cloud.tencent.com/cls/topic) 管理页面，单击步骤3创建的日志主题名称/ID，进入该日志主题管理页面。
2. 选择**采集配置**页签，在**LogListener采集配置**中单击**新增**。
![](https://qcloudimg.tencent-cloud.cn/raw/d7dd437abb775fb1cdba049f21e516cb.png)
3. 在日志数据源页面，选择**单行全文日志**。
![](https://qcloudimg.tencent-cloud.cn/raw/d1059298722055b8224dcd265817ecc8.png)
>?
> - **单行全文日志**会将日志原文直接上报至 CLS，不会对日志内的字段进行分割和提取，该提取方式配置比较简单，便于快速入门 CLS，但不利于后续使用更加丰富的日志检索分析功能（例如按特定字段检索日志或对日志进行统计分析）。建议在实际使用时，请参照 [日志结构化](https://cloud.tencent.com/document/product/614/33494#.E6.97.A5.E5.BF.97.E7.BB.93.E6.9E.84.E5.8C.96) 文档选择合适的日志格式对日志字段进行分割和提取。
> - 如果日志为 JSON，可选择 **JSON 格式日志**。
> 
4. 选择步骤2.2创建的机器组，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/b38bee83133c7fec614cafbb90cf070e.png)
5. 填写**采集规则名称**及**采集路径**（即需要采集的日志文件路径），单击**下一步**。
例如，待采集文件的绝对路径是`/root/test.log`，则采集路径填写的目录前缀是`/root`，日志文件名填写`test.log`。
![](https://qcloudimg.tencent-cloud.cn/raw/198392d503147d66e626f69e67aac793.png)
6. 填写索引配置，开启全文索引。
![](https://qcloudimg.tencent-cloud.cn/raw/958441f6a0e25a029bce486d5354494f.png)
>?
> - 如果日志提取模式不是单行全文，可开启键值索引，单击**自动配置**，采集到的日志自动配置键值索引。
> - 修改索引配置仅对新写入的日志生效，已有数据不会更新。
> - 索引配置中的各个配置项说明请参见 [配置索引](https://cloud.tencent.com/document/product/614/50922) 文档。
> 

## 步骤5：检索分析日志

1. 前往 [检索分析](https://console.cloud.tencent.com/cls/search)，在页面顶部选择步骤3创建的日志主题，即可查看采集到的日志数据。
![](https://qcloudimg.tencent-cloud.cn/raw/aba111bdab7be906365382d71b0c5387.png)
2. 在顶部的输入框中填写需要检索的文本作为检索条件，单击**检索分析**，即可检索符合检索条件的日志。
例如，下图中为检索包含"/online/sample"的日志。
![](https://qcloudimg.tencent-cloud.cn/raw/c7c4b0b27d5f11371a45780b094f848b.png)
3. 基于检索到的原始数据，使用管道符和 SQL 进行统计分析。
例如，统计日志的来源分布。
![](https://qcloudimg.tencent-cloud.cn/raw/c47d88750ba61be787fa2497579ae3e0.png)
>?
> - 更多检索及分析语法说明请参见 [语法规则](https://cloud.tencent.com/document/product/614/47044) 文档。
> - `__SOURCE__`为系统预置字段，代表日志的来源 IP。对日志进行 [结构化](https://cloud.tencent.com/document/product/614/33494#.E6.97.A5.E5.BF.97.E7.BB.93.E6.9E.84.E5.8C.96) 处理，且在 [键值索引](https://cloud.tencent.com/document/product/614/50922#.E9.94.AE.E5.80.BC.E7.B4.A2.E5.BC.95) 中为日志字段开启统计后，还可以对日志内的字段进行统计分析，例如按 URL 统计日志条数等。



## 扩展阅读

- [基本概念](https://cloud.tencent.com/document/product/614/35675)：通过该文档，您可以系统了解 CLS 基本产品概念，包括日志主题、日志集、索引和分词等。
- [采集检索 Nginx 访问日志](https://cloud.tencent.com/document/product/614/37735)：通过该文档，您可以了解如何采集 nginx 日志并使用正则表达式对日志内的字段进行分割和提取。
- [将通过 grep 命令查找的本地日志迁移至 CLS](https://cloud.tencent.com/document/product/614/64305)：通过该文档，您可以将习惯使用的 grep 命令转换为 CLS 检索语法，更快的掌握 CLS 语法规则。
- [云产品日志接入](https://cloud.tencent.com/document/product/614/47611)：CLS 已集成了部分常见云产品日志，可轻松采集这些云产品的日志。
- [数据加工任务](https://cloud.tencent.com/document/product/614/63940)：可通过数据加工对原始日志进行过滤、清洗、脱敏、富化和分发。
- [监控告警简介](https://cloud.tencent.com/document/product/614/51741)：可针对日志设置告警策略，例如1分钟内 ERROR 日志大于10条即触发告警。

