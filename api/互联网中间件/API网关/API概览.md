>?
>- 当前页面接口为旧版 API，未来可能停止维护。API 网关 API3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [API 网关 API3.0](https://cloud.tencent.com/document/product/628/45247)。
>- 如果您需要访问 API 网关旧版 API，可继续阅读本章节内容。

## API 相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [修改 API 接口](https://cloud.tencent.com/document/product/628/14880) | ModifyApi | 用于修改 API 接口。|
| [删除 API 接口](https://cloud.tencent.com/document/product/628/14881)  | DeleteApi| 用于删除 API 接口。|
| [查询 API 接口信息](https://cloud.tencent.com/document/product/628/14882) | DescribeApi | 用于查询用户部署于 API 网关的 API 接口的详细信息。|
| [查询 API 接口列表](https://cloud.tencent.com/document/product/628/14883) | DescribeApisStatus | 用于查看一个服务下的某个 API 或所有 API 列表及其相关信息。|
| [调试 API 接口](https://cloud.tencent.com/document/product/628/14884) | RunApi | 用于调试 API 接口。|
| [创建 API 接口](https://cloud.tencent.com/document/product/628/14886) | CreateApi | 用于创建 API 接口。|
| [查询 API 使用计划详情](https://cloud.tencent.com/document/product/628/18900) | DescribeApiUsagePlan | 用于查询服务中 API 使用计划详情。|

## 服务相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [下线服务](https://cloud.tencent.com/document/product/628/14896) | UnReleaseService | 用于下线服务。下线后的服务不可被调用。|
| [修改服务](https://cloud.tencent.com/document/product/628/14897)  | ModifyService| 用于修改服务的相关信息。|
| [切换服务版本](https://cloud.tencent.com/document/product/628/14898) | UpdateService | 用于从服务发布的环境中运行版本切换到特定版本。|
| [创建服务](https://cloud.tencent.com/document/product/628/14899) | CreateService | 用于创建服务。|
| [删除服务](https://cloud.tencent.com/document/product/628/14902) | DeleteService | 用于删除 API 网关中某个服务。|
| [删除自定义域名的路径映射](https://cloud.tencent.com/document/product/628/14903) | DeleteServiceSubDomainMapping | 用于删除服务中某个环境的自定义域名映射。|
| [发布服务](https://cloud.tencent.com/document/product/628/14904) | ReleaseService | 用于发布服务。|
| [服务修改自定义域名](https://cloud.tencent.com/document/product/628/14905) | ModifySubDomain | 用于修改服务的自定义域名设置中的路径映射，可以修改绑定自定义域名之前的路径映射规则。|
| [服务绑定自定义域名](https://cloud.tencent.com/document/product/628/14906)  | BindSubDomain| 用于绑定自定义域名到服务。|
| [服务解绑自定义域名](https://cloud.tencent.com/document/product/628/14907) | UnBindSubDomain | 用于解绑自定义域名。|
| [查询服务使用计划详情](https://cloud.tencent.com/document/product/628/14908) | DescribeServiceUsagePlan | 用于查询服务使用计划详情。|
| [查询服务列表](https://cloud.tencent.com/document/product/628/14909) | DescribeServicesStatus | 用于搜索查询某一个服务或多个服务的列表，并返回服务相关的域名、时间等信息。|
| [查询服务已发布的版本](https://cloud.tencent.com/document/product/628/14910) | DescribeServiceReleaseVersion | 用于查询一个服务下面所有已经发布的版本列表。|
| [查询服务环境列表](https://cloud.tencent.com/document/product/628/14911) | DescribeServiceEnvironmentList | 用于查询一个服务下所有环境及其状态。|
| [查询服务环境的发布历史](https://cloud.tencent.com/document/product/628/14912) | DescribeServiceEnvironmentReleaseHistory | 用于查询服务环境的发布历史。|
| [查询服务详情](https://cloud.tencent.com/document/product/628/14913) | DescribeService | 用于查询一个服务的详细信息、包括服务的描述、域名、协议、创建时间、发布情况等信息。|
| [查询自定义域名列表](https://cloud.tencent.com/document/product/628/14914) | DescribeServiceSubDomains | 用于查询用户绑定在服务的自定义域名列表。|
| [查询自定义域名的路径映射](https://cloud.tencent.com/document/product/628/14915) | DescribeServiceSubDomainMappings | 用于查询绑定服务的自定义域名的路径映射列表。 |

## 密钥相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [创建密钥](https://cloud.tencent.com/document/product/628/14916) | CreateApiKey | 用于创建一对新的 API 密钥。 |
| [删除密钥](https://cloud.tencent.com/document/product/628/14917) | DeleteApiKey | 用于删除一对 API 密钥。 |
| [启用密钥](https://cloud.tencent.com/document/product/628/14918) | EnableApiKey | 用于启动一对被禁用的 API 密钥。 |
| [更换密钥](https://cloud.tencent.com/document/product/628/14919) | UpdateApiKey | 用于更换用户已创建的一对 API 密钥。|
| [查询密钥列表](https://cloud.tencent.com/document/product/628/14920) |DescribeApiKeysStatus | 用于查询一个或多个 API 密钥信息，该接口不会显示密钥 Key。| 
| [查询密钥详情](https://cloud.tencent.com/document/product/628/14940) | DescribeApiKey | 用于查询一个 API 密钥的详情，该接口会显示密钥 Key。|
| [禁用密钥](https://cloud.tencent.com/document/product/628/14941) | DisableApiKey | 用于禁用一对 API 密钥。|

## 使用计划相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [从服务环境解绑使用计划](https://cloud.tencent.com/document/product/628/14943) | UnBindEnvironment | 用于将使用计划从特定环境解绑。|
| [使用计划绑定密钥](https://cloud.tencent.com/document/product/628/14944) |  BindSecretIds | 用于为使用计划绑定密钥。|
| [使用计划解绑密钥](https://cloud.tencent.com/document/product/628/14945) | UnBindSecretIds | 用于为使用计划解绑密钥。|
| [修改使用计划](https://cloud.tencent.com/document/product/628/14946) | ModifyUsagePlan | 用于修改使用计划的名称、描述及 QPS。|
| [创建使用计划](https://cloud.tencent.com/document/product/628/14947) | CreateUsagePlan | 用于创建使用计划。 |
| [删除使用计划](https://cloud.tencent.com/document/product/628/14948) |  DeleteUsagePlan | 用于删除使用计划。|
| [查询使用计划状态](https://cloud.tencent.com/document/product/628/14949) | DescribeUsagePlansStatus | 用于查询一个或多个使用计划列表。可查询到这些使用计划的名称、描述、QPS 等信息。|
| [查询使用计划绑定密钥列表](https://cloud.tencent.com/document/product/628/14950) | DescribeUsagePlanSecretIds | 用于查询使用计划绑定的密钥列表。|
| [查询使用计划绑定环境列表](https://cloud.tencent.com/document/product/628/14951) | DescribeUsagePlanEnvironments | 用于查询使用计划绑定的所有服务的环境。|
| [查询使用计划详情](https://cloud.tencent.com/document/product/628/14952) | DescribeUsagePlan | 用于查询一个使用计划的详细信息，包括名称、QPS、创建时间绑定的环境等。|
| [绑定使用计划到服务环境](https://cloud.tencent.com/document/product/628/14953) | BindEnvironment | 用于绑定使用计划到服务环境。|
| [服务级别使用计划降级](https://cloud.tencent.com/document/product/628/18899) |  DemoteServiceUsagePlan | 用于将某个服务在某个环境的使用计划，降级到 API上。|


## 文档和 SDK 相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [生成文档和 SDK](https://cloud.tencent.com/document/product/628/14942) | GenerateApiDocument | 用于自动生成 API 文档和 SDK，一个服务的一个环境生成一份文档和 SDK。|






