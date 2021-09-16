本文为您详细介绍如何使用持续集成自动上传 API 文档。

## 前提条件

设置 CODING 持续集成插件的前提：您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见 [开通服务](https://cloud.tencent.com/document/product/1115/37268)。

## 进入持续集成

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 进入左侧菜单中的**持续集成** > **构建计划** > **API 文档** > **自定义构建过程**。

## 功能介绍

CODING 持续集成插件**读取代码生成 API 文档**可以提取代码中的注释，生成 API 文档并发布。

### 在代码中编写注释

在代码中编写注释，参考 [OpenAPI/Swagger 编写与导入指南](https://help.coding.net/docs/management/api/import/openapi.html#Code-First)。

并且在本地调试通过，例如 PHP Laravel Swagger 生成文档的命令是：

```shell
php artisan l5-swagger:generate
ls storage/api-docs/api-docs.json
```

### 创建空的 API 文档

在**文档管理** > **API 文档**中创建一个空的 API 文档。
![1](https://main.qcloudimg.com/raw/c91b59c7beeb8e73f272b59d90ae97c9.png)

### 使用图形化界面生成并上传 API 文档

使用**持续集成**的图形化编辑器，添加一个步骤**执行 Shell 脚本**，填入生成 API 文档的命令。
![2](https://main.qcloudimg.com/raw/329f139cfea29e1f6dda5b8dd3a9ea87.png)

再添加一个步骤**读取代码生成 API 文档**，**语言 & 注释库**选择**其他**，填写之前生成的 `json` 文件路径，并且选择之前创建的**API 文档**。
![3](https://main.qcloudimg.com/raw/27db1f312c5f32f9ac1562fd5bc9a343.png)
![4](https://main.qcloudimg.com/raw/9d911dfd256114c7e65d7682c93e2e9a.png)

### Jenkinsfile

也可以使用持续集成的**文本编辑器**，填入以下代码：

```groovy
pipeline {
  agent {
    docker {
      image 'sinkcup/laravel-demo:6-dev'
      args '-v /root/.composer:/root/.composer'
      reuseNode true
    }
  }
  stages {
    stage('检出') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: env.GIT_BUILD_REF]],
        userRemoteConfigs: [[url: env.GIT_REPO_URL, credentialsId: env.CREDENTIALS_ID]]])
      }
    }
    stage('安装依赖') {
      steps {
        sh 'composer install'
      }
    }
    stage('生成 API 文档') {
      steps {
        sh 'php artisan l5-swagger:generate'
        codingReleaseApiDoc(apiDocId: '1', apiDocType: 'specificFile', resultFile: 'storage/api-docs/api-docs.json')
      }
    }
  }  
}
```

手动或自动执行构建计划，成功后，即可通过**文档管理** > **API 文档**中的链接进行访问。


