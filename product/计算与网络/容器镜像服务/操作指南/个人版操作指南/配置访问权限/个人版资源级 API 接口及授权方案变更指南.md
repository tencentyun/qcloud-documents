## 概述

容器镜像服务（TCR）同时向企业客户及个人用户提供容器镜像托管分发服务。其中，个人版为用户提供简单、免费的基础服务，即当前容器服务（TKE）内的镜像仓库。
为向用户提供接口定义更加规范，访问时延下降显著的 API 接口服务，原有个人版镜像仓库（CCR）的 API 接口已由 2.0 版本升级至最新的 3.0 版本，接口名称及授权方案也发生了相应变更。本文档介绍了支持资源级鉴权的 API 升级后新旧接口映射关系及如何使用最新的授权方案。

## API 映射关系
|  API 2.0 名称           | API 3.0 名称                     | 接口描述                 | 最新资源（Resource）描述方式                        |
| :-------------------- | :------------------------------ | :----------------------- | :------------------------------------------------ |
| CreateCCRNamespace    | CreateNamespacePersonal         | 创建个人版命名空间       | `qcs::tcr:$region:$account:repo/$namespace`       |
| DeleteUserNamespace   | DeleteNamespacePersonal         | 删除个人版命名空间       | `qcs::tcr:$region:$account:repo/$namespace`       |
| GetUserRepositoryList | DescribeRepositoryOwnerPersonal | 查询个人版所有仓库       | `qcs::tcr:$region:$account:repo/*`                |
| CreateRepository      | CreateRepositoryPersonal        | 创建个人版镜像仓库       | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| DeleteRepository      | DeleteRepositoryPersonal        | 删除个人版镜像仓库       | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| BatchDeleteRepository | BatchDeleteRepositoryPersonal   | 批量删除个人版镜像仓库   | `qcs::tcr:$region:$account:repo/$namespace/*`     |
| DeleteTag             | DeleteImagePersonal             | 删除个人版仓库 tag       | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| BatchDeleteTag        | BatchDeleteImagePersonal        | 批量删除个人版仓库 tag   | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| pull                  | PullRepositoryPersonal          | 拉取个人版镜像仓库内镜像 | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| push                  | PushRepositoryPersonal          | 推送个人版镜像仓库内镜像 | `qcs::tcr:$region:$account:repo/$namespace/$repo` |

## 授权方案映射关系
由于产品名称及 API 接口版本的升级变更，TCR 个人版原有的资源（Resource）描述方式及动作（Action）发生了相应变更，请您在使用 API 3.0接口的同时，使用最新的资源及操作授权方案。
API 升级期间，访问管理相关接口将同时兼容新旧的资源（Resource）描述方式及动作（Action），以保障用户自定义策略仍然生效。为方便您统一管理 API 接口及授权方案，建议您统一将授权方案升级为最新版本，详情请参考 [个人版授权方案示例](https://cloud.tencent.com/document/product/1141/41409)。

### 旧版资源级授权方案
- **动作（Action）**：以 `ccr` 作为产品前缀，API 接口名称为2.0版本。例如，创建命名空间为 `ccr:CreateCCRNamespace`。
- **资源描述（Resource）**：以 `ccr` 作为产品名称，仅有 `repo` 资源类型。例如，描述命名空间 namespace-a 下的镜像仓库 repo-b，则为 `qcs::ccr:::repo/namespace-a/repo-b`。其中，`$region`，`$account` 若置空，则默认为全部地域，账号默认为创建策略的 CAM 用户所属的主账号。
具体授权方案请参考：[TKE 镜像仓库资源级权限设置](https://cloud.tencent.com/document/product/457/11527)。

### 新版资源级授权方案
- **动作（Action）**： 以 `tcr` 作为产品前缀，API 接口名称为3.0版本。例如，创建个人版命名空间为 `tcr:CreateNamespacePersonal`。
- **资源描述（Resource）**：以 `tcr` 作为产品名称，具有 `instance`、`repository` 和`repo` 三种资源类型。其中，`repo` 为个人版专属的资源类型。例如，描述个人版命名空间 namespace-a 下的镜像仓库 repo-b，则为 `qcs::tcr:$region:$account:repo/namespace-a/repo-b`。其中，`$region`,`$account` 若置空，则默认为全部地域，账号默认为创建策略的 CAM 用户所属的主账号。
具体授权方案请参考：[个人版接入 CAM 的 API 列表](https://cloud.tencent.com/document/product/1141/41415) 及 [个人版授权方案示例](https://cloud.tencent.com/document/product/1141/41409)。

### 新旧授权方案兼容示例
例如，授权子账号可读默认地域下 namespace-a 命名空间内的 repo-b 的镜像仓库，该镜像仓库为个人版。则仅能查询仓库信息、拉取该仓库内镜像，但无法删除仓库、修改仓库属性及推送镜像。
 - **旧版授权方案：**
 ```
    {
        "version": "2.0",
        "statement": [{
            "action": [
                "ccr:pull"
            ],
            "resource": "qcs::ccr:::repo/namespace-a/repo-b",
            "effect": "allow"
        }]
    }
 ```
 - **新版授权方案：**
    ```
    {
        "version": "2.0",
        "statement": [{
            "action": [
                "tcr:PullRepositoryPersonal"
            ],
            "resource": "qcs::tcr:::repo/namespace-a/repo-b",
            "effect": "allow"
        }]
    }
    ```


