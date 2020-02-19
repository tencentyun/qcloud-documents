### 命名空间相关接口
| API 名                 | API 描述          | 资源类型 | 资源六段式示例                                                                           |
| :--------------------- | :--------------- | :------- | :--------------------------------------------------------------------------------------- |
| CreateNamespacePersonal         | 创建个人版命名空间         | repo | `qcs::tcr:$region:$account:repo/$namespace`                                         |
| DeleteNamespacePersonal         | 删除个人版命名空间         | repo | `qcs::tcr:$region:$account:repo/$namespace`                                         |

### 镜像仓库相关接口
| API 名                 | API 描述          | 资源类型 | 资源六段式示例                                                                           |
| :--------------------- | :--------------- | :------- | :--------------------------------------------------------------------------------------- |
| DescribeRepositoryOwnerPersonal      | 获取个人版用户自身的所有仓库列表     | repo | `qcs::tcr:$region:$account:repo/*` |
| CreateRepositoryPersonal      | 创建个人版镜像仓库     | repo | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| DeleteRepositoryPersonal      | 删除个人版镜像仓库     | repo | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| BatchDeleteRepositoryPersonal      | 批量删除个人版镜像仓库     | repo | `qcs::tcr:$region:$account:repo/$namespace/*` |
| DeleteImagePersonal      | 删除个人版镜像版本     | repo | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| BatchDeleteImagePersonal      | 批量删除个人版镜像版本     | repo | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| PullRepositoryPersonal      | 拉取个人版镜像仓库内镜像     | repo | `qcs::tcr:$region:$account:repo/$namespace/$repo` |
| PushRepositoryPersonal      | 推送个人版镜像仓库内镜像     | repo | `qcs::tcr:$region:$account:repo/$namespace/$repo` |