 
## 背景  
- 客户需求：云服务作为大客户的核心 IT 资产，大客户需要对云上的资源操作进行记录，以便发生问题时，进行溯源，保证企业人员资产操作安全性；  
-  现有操作日志情况：通过操作日志提供的 API，云产品将操作信息推送给操作日志应用，这样的操作日志记录字段有限，日志内容不完整，且需要云产品一个个接入，不同的操作也要一个个接入，会造成人力资源的浪费。  

## 工作原理  
在您创建 AWS 账户时，将对账户启用 CloudAudit。当您的 AWS 账户中发生活动时，该活动将记录在 CloudAudit 事件中。您可以通过转到 Event history 轻松查看 CloudAudit 控制台中的事件。

利用事件历史记录，您可以查看、搜索和下载 AWS 账户中过去七天的受支持活动。此外，您还可以创建一个 CloudAudit 跟踪，以进一步存档、分析和响应您的 AWS 资源的变化。跟踪是一种配置，可用于将事件传送到您指定的 Amazon S3 存储桶。也可以使用 Amazon CloudWatch Logs 和 Amazon CloudWatch Events 传送和分析跟踪中的事件。您可使用 CloudAudit 控制台、AWS CLI 或 CloudAudit API 创建跟踪。

可创建两种类型的跟踪：  
### 应用于所有区域的跟踪  
在创建应用于所有区域的跟踪时，CloudAudit 会在每个区域中创建相同的跟踪。然后，它会在每个区域中记录事件，并将这些 CloudAudit 事件日志文件传送至您指定的 S3 存储桶。在 CloudAudit 控制台中创建跟踪时，这是默认选项。  
### 应用于一个区域的跟踪  
当您创建适用于一个区域的跟踪时，CloudAudit 仅记录该区域中的日志文件。然后它将 CloudAudit 事件日志文件传送到您指定的 S3 存储桶。如果您另外创建了单个跟踪，可以让这些跟踪将 CloudAudit 事件日志文件传送到同一个 Amazon S3 存储桶或单独的存储桶。  
	**注意**
	对于这两种类型的跟踪，您可以指定来自任何区域的 Amazon S3 存储桶。  
默认情况下，将使用 Amazon S3 服务器端加密 (SSE) 对 CloudAudit 事件日志文件进行加密。您还可以选择使用 AWS Key Management Service (AWS KMS) 密钥加密您的日志文件。日志文件可以在存储桶中存储任意长时间。您也可以定义 Amazon S3 生命周期规则以自动存档或删除日志文件。如果您想接收有关日志文件传送和验证的通知，可以设置 Amazon SNS 通知。  

CloudAudit 通常会在账户活动发生后的 15 分钟内传送日志文件。此外，CloudAudit 一小时内会多次发布日志文件，通常约每 5 分钟发布一次。这些日志文件包含账户中来自支持 CloudAudit 的服务的 API 调用。
	**注意**
	CloudAudit 可捕获由用户直接执行或通过 AWS 服务代表用户执行的操作。例如，AWS CloudFormation CreateStack 调用会导致对 Amazon EC2、Amazon RDS、Amazon EBS 或其他服务发起其他的 API 调用 (根据 AWS CloudFormation 模板的要求)。这是正常的，也是预期的行为。您可以使用 CloudAudit 事件中的 invokedby 字段确定操作是否由 AWS 服务执行。  
若要开始使用 CloudAudit，请参阅[CloudAudit 快速入门](#jump)。  
 
对于 CloudAudit 定价，请参阅 [AWS CloudAudit 定价](#jump)。

## CloudAudit 工作流程  
### 查看 AWS 账户的事件历史记录  
您可以通过 CloudTrail 控制台或使用 AWS CLI 查看和搜索过去七天由 CloudTrail 记录的事件。
### 下载事件  
您可以下载 CSV 或 JSON 文件，其中包含您的 AWS 账户过去七天的 CloudTrail 事件。
### 创建跟踪
通过跟踪，CloudTrail 可将日志文件传送至 Amazon S3 存储桶。默认情况下，在控制台中创建跟踪时，此跟踪应用于所有区域。此跟踪在 AWS 分区中记录所有区域中的事件，并将日志文件传送至您指定的 S3 存储桶。

### 创建并订阅 Amazon SNS 主题
订阅主题以接收有关将日志文件传送至您的存储桶的通知。Amazon SNS 可通过多种方式通知您，包括使用 Amazon Simple Queue Service 以编程方式通知您。
	**注意**
	如果您要接收有关从所有区域传送日志文件的 SNS 通知，请为您的跟踪仅指定一个 SNS 主题。
####查看您的日志文件
使用 Amazon S3 检索日志文件。

### 管理用户权限
使用 AWS Identity and Access Management (IAM) 管理哪些用户有权创建、配置或删除跟踪、启动和停止日志记录，以及访问包含日志文件的存储桶。
### 使用 CloudWatch Logs 监控事件
您可以配置自己的跟踪，将事件发送到 CloudWatch Logs。然后，您可以使用 CloudWatch Logs 监控账户中的特定 API 调用和事件。

	**注意**
	如果您将应用于所有区域的跟踪配置为将事件发送到 CloudTrail 日志组，则 CloudWatch Logs 会将所有区域中的事件都发送到单个日志组。
### 记录管理和数据事件
将您的跟踪配置为记录只读、只写或所有管理和数据事件。默认情况下，跟踪会记录 管理事件。

### 启用日志加密
日志文件加密为您的日志文件提供额外的安全层。

### 启用日志文件完整性
日志文件完整性验证可帮助您验证日志文件在由 CloudTrail 传送后是否一直保持不变。

### 与其他 AWS 账户共享日志文件
您可以在账户之间共享日志文件。
### 聚合多个账户中的日志
您可以将多个账户中的日志文件聚合到单个存储桶中。

### 使用合作伙伴解决方案
使用与 CloudTrail 集成的合作伙伴解决方案来分析您的 CloudTrail 输出。合作伙伴解决方案提供了一组广泛的功能，例如，更改跟踪、故障排除和安全分析。