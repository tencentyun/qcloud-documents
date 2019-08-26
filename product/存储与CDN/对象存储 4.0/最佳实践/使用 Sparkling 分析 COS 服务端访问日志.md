本文详细介绍如何使用 Sparkling 分析日志。

## 前提条件

- 已开通 COS 存储桶的日志管理功能。
- 已开通腾讯云 Sparkling 服务，并且保证运行版本在0.5.0以上，Sparkling 服务需要额外收费。

#### 开通 COS 日志管理功能

> ?开通 COS 日志管理功能，您可以参见 [设置日志管理](https://cloud.tencent.com/document/product/436/17040) 控制台指南进行设置，下面为举例说明。

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，选择需要分析访问记录的存储桶，并开通日志管理功能，此后根据需要开启相应存储桶的访问日志功能。例如用户需要分析访问记录的存储桶为`loggingbucket-1250000000`，其所有的访问记录投递到目标存储桶`deliverybucket-1250000000`下，并且路径前缀为`cos-access-log/ap-guangzhou/deliverybucket/`，如下图所示：
![](https://main.qcloudimg.com/raw/ccb0a757d1f4b841b359559d9b96ebc2.png)
2. 目标存储桶和路径前缀配置完成后，COS 存储桶的日志管理功能即可开通完毕。

#### 开通 Sparkling 服务

1. 登录到 [Sparkling 服务控制台](https://console.cloud.tencent.com/sparkling)（需申请试用），创建与目标存储桶**相同地域**的 sparkling 集群。

> !由于目前 Sparkling 只能支持从 COS 加载待分析日志到 Sparkling 本地集群中进行分析，因此您需要根据日志规模选择合适的集群配置。
![](https://main.qcloudimg.com/raw/7b34b39f941351269abb7e3971fa4615.jpg)

2. 等待集群创建完成。
![](https://main.qcloudimg.com/raw/fa2c2b84b799a044767b19cbb0b2cbec.png)

## 操作步骤


#### 导入日志

1. 登录 [Sparkling 控制台](https://console.cloud.tencent.com/sparkling)，在左侧菜单栏中单击【数据】，进入数据配置页面，配置说明如下：
	- **数据类型**：COS。
	- **接入方式**：新建数据源。
	- **地域**：目标存储桶的地域（示例为广州）。
	- **SecretId 和 SecretKey**：填写访问 COS 目标存储桶的 SecretId 和 SecretKey。
	- **存储桶**：填写目标存储桶，并单击**浏览存储桶**来导入待分析的数据所在的目录。
	- **文件格式**：其他分隔符日志。
	- **字段分隔符**：\x20。
  ![](https://main.qcloudimg.com/raw/f084ae60f7b2bf708208fc34bac1eecf.jpg)
2. 单击【下一步】，完成数据导入后，可以获得数据预览。
> !这里 sparkling 会做字段的类型推断，字段名为`_c0,_c1,...,_cN`，并且字段名暂时不支持修改。

	![](https://main.qcloudimg.com/raw/6bf1dd9d5da5a13d612357ab1d7882ff.jpg)

3. 单击【下一步】，创建待分析数据的表。
   ![](https://main.qcloudimg.com/raw/9a757c809e0d2890725597f579a74a86.png)
4. 完成上面步骤后，可以在左侧菜单栏【任务】中查看到数据源导入完成。
   ![](https://main.qcloudimg.com/raw/c99eb7310dffae304d2a57bdf1c40680.png)

#### 基于 Notebook 笔记簿使用 SQL 对日志进行分析

#### 简单查询

1. 在左侧菜单栏中单击【工作区】，并新建一个 Notebook 笔记簿，然后执行一个简单 SQL 语句；
   ![](https://main.qcloudimg.com/raw/80ac3cf51b859c3be9264f812d4f819f.jpg)
2. 分析错误码的分布并可视化，这里的错误字段名是`_c16`，执行如下 SQL 语句：`select _c14, count(*) from cos_logging group by _c16`。
   ![](https://main.qcloudimg.com/raw/fea191f726ec270801a14dac8d33b49f.jpg)
3. 选择柱状图进行可视化，如下图所示：
   ![](https://main.qcloudimg.com/raw/630f7e6223a7894ba34b7595f67f4fe3.jpg)
