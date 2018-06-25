如果您在腾讯云中使用到了云服务器（CVM，Cloud Virtual Machine）、私有网络、数据库等服务，这些服务由不同的人管理，但都共享您的云账号密钥，将存在以下问题：

- 您的密钥由多人共享，泄密风险高；
- 您无法限制其它人的访问权限，易产生误操作造成安全风险。

这个时候，您就可以通过子帐号实现不同的人管理不同的服务，以避免以上的问题。默认情况下，子帐号没有使用CVM的权利或者CVM相关资源的的权限。因此，我们就需要创建策略来允许子帐号使用他们所需要的资源或者权限。

访问管理（CAM，Cloud Access Management）是腾讯云提供的一套Web服务，它主要用于帮助客户安全管理腾讯云账户下的资源的访问权限。通过CAM，您可以创建、管理和销毁用户(组)，并通过身份管理和策略管理控制哪些人可以使用哪些腾讯云资源。

当您使用CAM的时候，可以将策略与一个用户或者一组用户关联起来，策略能够授权或者拒绝用户使用指定资源完成指定任务。有关CAM策略的更多相关基本信息，请参照[策略语法](https://cloud.tencent.com/document/product/378/8962)。有关CAM策略的更多相关使用信息，请参照[策略](https://cloud.tencent.com/document/product/378/8955)。

如果您不需要对子账户进行CVM相关资源的访问管理，您可以跳过此章节。跳过这些部分并不影响您对文档中其余部分的理解和使用。

该功能目前处于灰度中，可提[工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM)。

**入门**

CAM 策略必须授权使用一个或多个 CVM 操作或者必须拒绝使用一个或多个 CVM 操作。同时还必须指定可以用于操作的资源（可以是全部资源，某些操作也可以是部分资源），策略还可以包含操作资源所设置的条件。

CVM 部分 API 操作支持资源级权限，意味着，对于该类 API操作，您不能在使用该类操作的时候指定某个具体的资源来使用，而必须要指定全部资源来使用。




| 任务 | 链接 | 
|---------|---------|
|了解策略基本结构|[策略语法](https://cloud.tencent.com/document/product/213/10313?!preview&lang=cn/#celueyufa)|
|在策略中定义操作| [CVM的操作](https://cloud.tencent.com/document/product/213/10313?!preview&lang=cn/#caozuo) | 
|在策略中定义资源|[CVM的资源路径](https://cloud.tencent.com/document/product/213/10313?!preview&lang=cn/#ziyuanlujing)|
|使用条件来限制策略|[CVM的条件密钥](https://cloud.tencent.com/document/product/213/10313?!preview&lang=cn/#tiaojianmiyue)|
|CVM支持的资源级权限|[CVM支持的资源级权限](https://cloud.tencent.com/document/product/213/10314?!preview&lang=cn)|
|控制台示例|[控制台示例](https://cloud.tencent.com/document/product/213/10312?!preview&lang=cn )|