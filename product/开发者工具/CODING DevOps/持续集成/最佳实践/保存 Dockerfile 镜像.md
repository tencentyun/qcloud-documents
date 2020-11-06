本文为您详细介绍如何在持续集成中保存 Dockerfile 镜像用于下次构建任务。

## 前提条件

使用 CODING 持续集成的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见  [开通服务](https://cloud.tencent.com/document/product/1115/37268)。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 进入项目后点击左下角的《项目设置》。

## 功能介绍

在持续部署中，有时候会需要用到第三方供应商所提供的服务，这时候就需要调用相关的凭据来获取权限。目前持续部署功能已集成内置插件，支持快速调取相关凭据。

## 使用插件快速调取已录入的凭据

在 CODING 持续集成任务构建过程当中，如果将 Github 的账号密码等重要信息硬编码在配置文件内，将会有极大的安全隐患。通过 CODING 的 [凭据管理](https://cloud.tencent.com/document/product/1113/48846) 功能，将凭据 ID 写入配置文件中进行服务调用。在接下来的插件功能使用中，请确保您已将凭据托管至 CODING 中。

## 快速开始

下面以调取凭据管理中的云 API 密钥为例，演示如何使用 Jenkinsfile 配置快速调取已录入的凭据。

1.  将获取到的 API 密钥上传至 CODING 进行托管以获得凭据 ID。
![](https://main.qcloudimg.com/raw/9dbe0deb533ee222d0871bfa55c6ec4d.png)
2.  在变量与缓存中选择【增加环境变量】>【类别选择 CODING 凭据】>【选择您需调取的凭据】。
![](https://main.qcloudimg.com/raw/9ab5c8d6ce931fba2f3b5dfa4489bfc1.png)
3.  在构建于部署中新建计划列表，并填写相应的 Jenkinsfile 配置

## Jenkinsfile 配置

```groovy
pipeline {
    agent any
    stages {
        stage('获取云 API 密钥') {
            steps {

                withCredentials([cloudApi(credentialsId: '此处填写您上传凭据后所生成的凭据 ID', secretIdVariable: 'CLOUD_API_SECRET_ID', secretKeyVariable: 'CLOUD_API_SECRET_KEY')]) {
                       sh 'CLOUD_API_SECRET_ID=${CLOUD_API_SECRET_ID}'
                       sh 'CLOUD_API_SECRET_KEY=${CLOUD_API_SECRET_KEY}'
                 }
                 withCredentials([[$class: 'CloudApiCredentialsBinding', credentialsId: '此处填写您上传凭据后所生成的凭据 ID', secretIdVariable: 'CLOUD_API_SECRET_ID', secretKeyVariable: 'CLOUD_API_SECRET_KEY']]) {
                       sh 'CLOUD_API_SECRET_ID=${CLOUD_API_SECRET_ID}'
                       sh 'CLOUD_API_SECRET_KEY=${CLOUD_API_SECRET_KEY}'
                 }
            }
        }
    }
}

```

4.  构建完成

![](https://main.qcloudimg.com/raw/7c59555ce5909dd1a08e77ffdd8349fc.png)

## 参数说明

| 参数名称              | 是否必填 | 默认值 | 说明                             |
|-------------------|------|-----|--------------------------------|
| credentialsId     | 是    | \-  | 需要获取的凭据 ID，仅支持云 API 类型的凭据      |
| secretIdVariable  | 是    | \-  | secretId 环境变量的名称，会用配置名称注入环境变量  |
| secretKeyVariable | 是    | \-  | secretKey 环境变量的名称，会用配置名称注入环境变量 |
