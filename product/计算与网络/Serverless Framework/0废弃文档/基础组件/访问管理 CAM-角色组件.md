## 操作场景
访问管理 CAM-角色（CAM-role）组件是 serverless-tencent 组件库中的基础组件之一。通过 CAM-role 组件，您可以快速且方便地创建、配置和管理腾讯云的 CAM 角色。

## 操作步骤

通过 CAM-role 组件，对一个 CAM 的角色进行完整的创建、配置、部署和删除等操作。支持命令如下：


#### 安装

通过 npm 安装 Serverless：

```console
$ npm install -g serverless
```

#### 创建

本地创建 `serverless.yml` 和 `.env` 两个文件：

```console
$ touch serverless.yml
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 APPID、SecretId 和 SecretKey 信息并保存。
```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
TENCENT_APP_ID=123
```
>?
> - 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
> - 如果已有腾讯云账号，可以在 [API 密钥管理
](https://console.cloud.tencent.com/cam/capi) 中获取 APPID、SecretId 和 SecretKey。

#### 配置

在 serverless.yml 中进行如下配置：

```yml
# serverless.yml

myRole:
  component: "@serverless/tencent-cam-role"
  inputs:
    roleName: QCS_SCFExcuteRole
    service:
      - scf.qcloud.com
      - cos.qcloud.com
    policy:      
      policyName:
        - QCloudResourceFullAccess
        - QcloudAccessForCDNRole
```

 
[查看详细配置文档>>](https://github.com/serverless-tencent/tencent-cam-role/blob/master/docs/configure.md)

 
#### 部署

通过如下命令进行部署，并查看部署过程中的信息：

```shell
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Syncing role c0hhdv-qt9mh6xj in region ap-guangzhou.
  DEBUG ─ Updating policy for role c0hhdv-qt9mh6xj.
  DEBUG ─ Saved state for role c0hhdv-qt9mh6xj.
  DEBUG ─ Role c0hhdv-qt9mh6xj was successfully deployed to region ap-guangzhou.
  DEBUG ─ Deployed role roleId is 4611686018427945536.

  myRole: 
    roleName:    QCS_SCFExcuteRole
    description: This is tencent-cam-role component.
    roleId:      4611686018427945536
    service: 
      - cos.qcloud.com
      - scf.qcloud.com
    policy: 
      policyId: 
        - 16313162
        - 2
      policyName: 
        - QCloudResourceFullAccess
        - QcloudAccessForCDNRole

  17s › myRole › done

```



####  移除
```shell
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing role c0hhdv-qt9mh6xj from region ap-guangzhou.
  DEBUG ─ Role c0hhdv-qt9mh6xj successfully removed from region ap-guangzhou.

  1s › myRole › done

```
