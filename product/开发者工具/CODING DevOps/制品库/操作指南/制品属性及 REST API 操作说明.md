本文为您介绍如何使用制品库中的制品属性及 REST API 操作说明。

## 进入制品库功能页

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击【立即使用】进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 单击左侧菜单栏的【制品库】，进入制品库功能页面。

## 功能介绍

CODING 制品属性支持用户对制品版本的自定义属性，可以进行**查询**、**新增**、**删除**、**修改**的操作。制品属性同时支持通过**页面操作**以及 **REST API** 进行管理。

>? 制品属性制品元数据的区别：制品属性不同于制品元数据，**制品元数据通常为制品类型的原生属性**，如: npm 的 packageName 和 version 等信息。**制品属性更多的是用来描述元数据无法定义的内容**，您可以利用制品属性写入在  CODING 持续集成中的制品产出信息，或其它自定义内容。

## 通过页面操作管理属性

在【制品库】页面，单击指定仓库下的指定包名，进入包页面后，单击【属性】，可在页面上对制品属性进行**查看**、**新增**、**修改**、**删除**操作。
![](https://main.qcloudimg.com/raw/024f736fd37ff091e7d870165b945599.png)

### 如何在 CODING 持续集成中收集制品属性

下面给出一个 Docker 制品的属性收集的 Jenkinsfile 示例，可以使用该示例文件创建一个持续集成 Job。

```groovy
pipeline {
  agent any
  environment {
    ENTERPRISE = "myteam"
    PROJECT = "myproject"
    ARTIFACT_REPO = "myrepo"
    PACKAGE = "mypkg"
    VERSION = "myversion"

    ARTIFACT_BASE = "${ENTERPRISE}-docker.pkg.coding.net"

    ARTIFACT_IMAGE = "${ARTIFACT_BASE}/${PROJECT}/${ARTIFACT_REPO}/${PACKAGE}:${VERSION}"
    // 该 docker 镜像用于收集制品属性
    PROP_COLLECTOR = 'docker.pkg.coding.net/ci-props-collector:0.1.0'

  }
  stages {
    stage('检出') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: env.GIT_BUILD_REF]],
                          userRemoteConfigs: [[url: env.GIT_REPO_URL, credentialsId: env.CREDENTIALS_ID]]])
      }
    }
    stage('推送到制品库') {
      steps {
        // 此处使用 hello-world 的 docker 镜像作为演示
        // 您可以根据自己的实际情况将此处修改成其他制品类型的推送逻辑
        sh 'docker pull hello-world'
        sh 'docker tag hello-world ${ARTIFACT_IMAGE}'
        script {
          docker.withRegistry("https://${ARTIFACT_BASE}", "${env.DOCKER_REGISTRY_CREDENTIALS_ID}") {
            docker.image("${ARTIFACT_IMAGE}").push()
          }
        }
      }
    }
    stage('收集制品属性') {
      steps {
        script {
          // 使用 CODING 持续集成内置的服务连接作制品属性接口的认证方式
          // 您也可以使用自己创建的项目令牌，写入到 USERNAME 和 PASSWORD 中
          withCredentials([
              usernamePassword(
                  credentialsId: env.DOCKER_REGISTRY_CREDENTIALS_ID,
                  usernameVariable: 'USERNAME',
                  passwordVariable: 'PASSWORD'
              )]) {
                  // 将本次构建的信息写入到对应的制品属性中
                  sh '''
                    docker run --rm \
                        -e USERNAME=${USERNAME} \
                        -e PASSWORD=${PASSWORD} \
                        -e PROJECT=${PROJECT} \
                        -e REPO=${ARTIFACT_REPO} \
                        -e PACKAGE=${PACKAGE} \
                        -e VERSION=${VERSION} \
                        -e ENTERPRISE=${ENTERPRISE} \
                        -e CI_BUILD_NUMBER=${CI_BUILD_NUMBER} \
                        -e JOB_ID=${JOB_ID} \
                        -e JOB_NAME=${JOB_NAME} \
                        -e PROJECT_NAME=${env.PROJECT_NAME} \
                        -e GIT_REPO_URL=${GIT_REPO_URL} \
                        -e GIT_COMMITTER_NAME=${GIT_COMMITTER_NAME} \
                        -e GIT_COMMITTER_EMAIL=${GIT_COMMITTER_EMAIL} \
                        -e GIT_LOCAL_BRANCH=${GIT_LOCAL_BRANCH} \
                        -e GIT_COMMIT=${GIT_COMMIT} \
                        ${PROP_COLLECTOR}
                  '''
            }
        }
      }
    }
  }
}
```



## 通过 REST API 管理属性

制品属性支持用户使用 REST API 来直接对制品属性进行**查询**、**新增**、**删除**、**修改**的操作。

目前仅支持使用**项目令牌**调用制品属性的 REST API。



### 申请拥有制品属性权限的项目令牌

1. 单击左侧菜单【项目设置】>【开发者选项】>【项目令牌】>【新建项目令牌】。
![](https://main.qcloudimg.com/raw/d1cefeaafb269dae3b8aaa5bb63ea212.png)
2. 在新建令牌页面，填写令牌名称，选择令牌过期时间，勾选**制品属性**，单击【新建】。
![](https://main.qcloudimg.com/raw/2846da0c0104f542792a773828f4ed76.png)
3. 新建成功后，在项目令牌列表中，单击【查看密码】，校验身份后即可获得该令牌的用户名及密码。
![](https://main.qcloudimg.com/raw/d3ef71117a0c0ceaa48ff4e4ada52f07.png)

### $URL 的组成

```URL
https://{teamGK}.coding.net/api/projects/{projectName}/repositories/{repoName}/packages/{pkgName}/versions/{versionName}/properties
```

$URL 参数说明

| 参数        | 说明                                                         |
| :---------- | ------------------------------------------------------------ |
| teamGK      | 团队域名，如: `codingcorp.coding.net` 的 `teamGK`  为  `codingcorp` |
| projectName | 项目名称                                                     |
| repoName    | 制品仓库名称                                                 |
| pkgName     | 制品包名称                                                   |
| versionName | 制品版本名称                                                 |

示例：

```URL
https://myteam.coding.net/api/projects/myproject/repositories/myrepo/packages/mypkg/versions/myversion/properties
```



### 快速上手

#### 新增制品属性

```bash
curl -u 项目令牌:密码 -H "Content-Type: application/json" -d '{"properties":[{"name":"demo.name","value":"demo value"}]}' -X POST $URL
```


#### 查询制品属性

```bash
curl -u 项目令牌:密码 $URL
```

#### 修改制品属性

```bash
curl -u 项目令牌:密码 -H "Content-Type: application/json" -d '{"properties":[{"name":"demo.name","value":"new demo value"}]}' -X PUT $URL
```



#### 删除制品属性

```bash
curl -u 项目令牌:密码 -H "Content-Type: application/json" -d '{"names":["demo.name"]}' -X DELETE $URL
```

返回 code 为 0 则表示操作成功

```json
{"code":0}
```

### 详细说明

body 参数说明

| 参数  | 说明   |
| :---- | :----- |
| name  | 属性名 |
| value | 属性值 |

**其他说明**

- 制品属性名称以 **coding.** 开头的属性名将作为 CODING 平台内部的保留字段，这一类字段将会有特殊的解析含义和联动。
保留字段的属性目前**不支持删除和修改**操作，仅支持**新增**及**查询**。
- 制品属性值支持多个值的形式，以分号分隔即可，具体为： **value1;value2;value3** 。

**命名规则**
- 制品属性名称仅支持 1-128 位的小写英文字母、数字、下划线 (_)、小数点 (.)；
- 制品属性名称不允许以小数点 (.) 开头或结尾，且不允许包含连续的小数点 (.)；
- 制品属性名称和值均不能为空；
- 制品属性值不能以分号 (;) 开头或结尾；
- 制品属性值为以分号分隔的多个值时，不允许连续相同的值。
- 具体命令


1. **新增制品属性**

	```bash
	curl -u 项目令牌:密码 \
			 -H "Content-Type: application/json" \
			 -d '{"properties":[{"name":"demo.name","value":"demo value"}]}' \
			 -X POST $URL
	```
支持同时新增多个制品属性：

	```bash
	curl -u 项目令牌:密码 \
			 -H "Content-Type: application/json" \
			 -d '{"properties":[{"name":"demo.name","value":"demo value"},{"name":"demo.name2","value":"demo value2"}]}' \
			 -X POST $URL
	```
	
	示例：
	![新增制品属性示例](https://main.qcloudimg.com/raw/556fe58637903bfac7c553be91796699.png)



2. **查询制品属性**

	```bash
	curl -u 项目令牌:密码 $URL
	```

	示例：

	![制品属性查询示例](https://main.qcloudimg.com/raw/708ab2076d21ee415ca9a1f7743bbc88.png)

3. **修改制品属性**

	```bash
	curl -u 项目令牌:密码 \
			 -H "Content-Type: application/json" \
			 -d '{"properties":[{"name":"demo.name","value":"new demo value"}]}' \
			 -X PUT $URL
	```
支持同时修改多个制品属性：

	```bash
	curl -u 项目令牌:密码 \
			 -H "Content-Type: application/json" \
			 -d '{"properties":[{"name":"demo.name","value":"new demo value"},{"name":"demo.name2","value":"new demo value2"}]}' \
			 -X PUT $URL
	```
	示例：
	![img](https://main.qcloudimg.com/raw/dfbbba77b1f3612f0cfd8a24bd0b9757.png)

4. **删除制品属性**

	```bash
	curl -u 项目令牌:密码 \
			 -H "Content-Type: application/json" \
			 -d '{"names":["demo.name"]}' \
			 -X DELETE $URL
	```
支持同时删除多个制品属性，指定想要删除的制品属性名称即可：

	```bash
	curl -u 项目令牌:密码 \
			 -H "Content-Type: application/json" \
			 -d '{"names":["demo.name","demo.name2","demo.name3"]}' \
			 -X DELETE $URL
	```
示例：
![删除制品属性示例](https://main.qcloudimg.com/raw/8d13742699fff712c8e279f22ae47719.png)
返回 code 为 0 即表示操作成功

	```json
	{"code":0}

	```

	若不为 0 则表示操作有误，可根据提示来进行调整，例：
![删除失败示例](https://main.qcloudimg.com/raw/0967a2dbdaf2649fcbca48c0c6be01cc.png)
