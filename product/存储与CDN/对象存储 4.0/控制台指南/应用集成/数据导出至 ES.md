## 简介

数据导出至 Elasticsearch Service（ES）是腾讯云对象存储（Cloud Object Storage，COS）基于 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 为用户提供的数据出湖方案，可以帮助用户将 CSV、JSON 等文件格式的数据导出至同地域的腾讯云 Elasticsearch 服务，用于快速构建日志分析、异常监控等各类业务。

## 注意事项

- 数据导出至 ES 功能涉及 COS 数据检索接口，相关的限制说明请参见 [Select 概述](https://cloud.tencent.com/document/product/436/37635)。
- 若您此前在对象存储控制台上为存储桶添加了数据导出至 ES 规则，可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上看到您所创建的数据导出至 ES 函数，请**不要**删除或修改该数据导出至 ES 函数，否则可能导致您的规则不生效。
- 当前数据导出至 ES 功能仅支持广州、上海、北京、成都。
- 对象存储数据导出至 ES 功能依赖于云函数服务，云函数服务为用户提供了 [免费额度](https://cloud.tencent.com/document/product/583/12282)，超出免费额度的部分需要按照 [云函数产品定价](https://cloud.tencent.com/document/product/583/12281) 收费。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航中，单击**应用集成 > 数据导出**，找到**数据导出至 ES**。
3. 单击**配置规则**，进入规则配置页面。
4. 单击**添加函数**。
>! 如果您尚未开通云函数服务，请前往 [云函数控制台](https://console.cloud.tencent.com/scf) 开通云函数服务，按照提示完成服务授权即可。
>
5. 在弹出的窗口中，配置如下信息：
![](https://qcloudimg.tencent-cloud.cn/raw/03588587fc6d52647aacb968b880abaa.png)
  - **函数名前缀**：作为函数的唯一标识名称，创建后不可修改。您可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上查看该函数。
  - **场景选择**：选择您希望导出的日志来源，推荐使用 COS 日志文件导出。
  - **源存储桶**：日志所保存的存储桶名称，如果选择 COS 日志文件导出，需要先开启 COS 日志存储功能。
  - **SCF 授权**：数据导出至 ES 需要授权云函数从您的存储桶中读取日志文件。因此需要添加此授权。
6. 单击**填写预设参数**，进行数据导出至 ES 配置，配置项说明如下：
![](https://qcloudimg.tencent-cloud.cn/raw/d815330550e2b2389d0b04170fb331c2.png)
  - **服务版本**：ES 的版本，支持7.x和6.x。
  - **访问方式**：您的 ES 的访问方式。如果选择 VPC 内网访问，需要填写对应的 VPC 。
  - **访问地址**：您的 ES 的访问地址，必须以`http://`或`https://`开头。
  - **索引名称**：您创建的 ES 检索索引。
  - **鉴权配置**：您的 ES 鉴权方式，如果是腾讯云 ES，目前仅支持**需鉴权**，您需要填写对应的用户名称和用户密码。
  - **速率上限**：导出至 ES 的速率上限。
7. 如果您希望做一些个性化的日志数据提取，请单击**上一步**进行配置，通常情况，建议直接单击**确认**，完成函数的添加。
![https://qcloudimg.tencent-cloud.cn/raw/45aad35859d960b3e0689b29e0ed9578.png](https://qcloudimg.tencent-cloud.cn/raw/45aad35859d960b3e0689b29e0ed9578.png)
  您可以对新创建的函数进行如下操作：
 - 单击**日志**，查看数据导出至 ES 的历史运行情况。当数据导出至 ES 出现报错时，您还可以通过单击**日志**，快速跳转到云函数控制台查看日志错误详情。
 - 单击**详情**，查看当前函数的详细配置。
 - 单击**编辑**，修改数据导出至 ES 规则。
 - 单击**触发**，可以选择存储桶内已有的一份日志直接触发导出至 ES。
 - 单击**删除**，删除不使用的数据导出至 ES 规则。
