## 操作场景

对象存储 COS 组件是 serverless-tencent 组件库中的基础组件之一。通过对象存储 COS 组件，可以快速且方便的创建、配置和管理腾讯云的 COS 存储桶。

## 操作步骤

通过 COS 组件，对一个 COS 存储桶进行完整的创建、配置、部署和删除等操作。支持命令如下：

#### 安装

通过 npm 安装 Serverless：

```console
$ npm install -g serverless
```

####  创建

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
```
>?
> - 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
> - 如果已有腾讯云账号，可以在 [API密钥管理
](https://console.cloud.tencent.com/cam/capi) 中获取APPID、SecretId 和 SecretKey。

####  配置

在 serverless.yml 中进行如下配置：

```yml
# serverless.yml

myBucket:
  component: '@serverless/tencent-cos'
  inputs:
    bucket: my-bucket
    region: ap-guangzhou

```
[查看详细配置文档>>](https://github.com/serverless-tencent/tencent-cos/blob/master/docs/configure.md)


#### 部署

通过如下命令进行部署，并查看部署过程中的信息：

```
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Deploying "my-bucket-1300415943" bucket in the "ap-guangzhou" region.
  DEBUG ─ "my-bucket-1300415943" bucket was successfully deployed to the "ap-guangzhou" region.
  DEBUG ─ Setting ACL for "my-bucket-1300415943" bucket in the "ap-guangzhou" region.
  DEBUG ─ Ensuring no CORS are set for "my-bucket-1300415943" bucket in the "ap-guangzhou" region.
  DEBUG ─ Ensuring no Tags are set for "my-bucket-1300415943" bucket in the "ap-guangzhou" region.

  myBucket: 
    bucket: my-bucket-1300415943
    region: ap-guangzhou

  10s › myBucket › done
```

#### 移除

通过以下命令移除部署的存储桶：

```
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing files from the "my-bucket-1300415943" bucket.
  DEBUG ─ Removing "my-bucket-1300415943" bucket from the "ap-guangzhou" region.
  DEBUG ─ "my-bucket-1300415943" bucket was successfully removed from the "ap-guangzhou" region.

  2s › myBucket › done
```
