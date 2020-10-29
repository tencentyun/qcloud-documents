### 不建议继续使用 ci-init

**Q：为什么 2019 年 10 月 10 号 之后使用带有 ci-init 的 Jenkinsfile， 创建一个新的构建计划会提示无法拉取代码？**

A：2019 年 10 月 10 日 之前创建的构建计划（ Job ）中的 ci-init 命令会为用户创建一对公私钥，并使其能够拉取项目中的代码仓库。之后创建的构建计划在调用 ci-init 时，将不会创建拉取代码的公私钥对了。

新创建的构建计划, 我们都会为用户内置一个可以用于拉取对应代码仓库的凭据 ID，直接使用 env.CREDENTIALS_ID 作为 userRemoteConfigs 的 credentialsId 即可。

旧的语法：

```groovy
pipeline {
    agent any
        stages {
        stage('检出') {
            steps {
                // 旧版本的语法含有 ci-init 
                sh 'ci-init'

                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: env.GIT_BUILD_REF]],
                    userRemoteConfigs: [[url: env.GIT_REPO_URL]]
                ])
            }
        }
    }
}
```

新的语法：

```groovy
pipeline {
    agent any
        stages {
        stage('检出') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: env.GIT_BUILD_REF]],
                    // 请注意新版的检出语法比旧版新增了 credentialsId: env.CREDENTIALS_ID
                    userRemoteConfigs: [[url: env.GIT_REPO_URL, credentialsId: env.CREDENTIALS_ID]]
                ])
            }
        }
    }
}
```

**CODING 目前已经支持了凭据管理，我们强烈建议用户使用更安全的凭据 ID 来代替之前的 ci-init 操作。**

>? 关于凭据如果您想了解更多可以参考 [凭据管理](https://cloud.tencent.com/document/product/1113/48846)。


**Q：之前创建的构建计划会受到影响么？**
A：不会，我们保障了之前创建的构建计划依然能够正常生效，会注入有效的公私钥，但建议用户尽快替换成新的 checkout 语法。

### 单引号和双引号用法有什么差异

您在使用 CODING  持续集成时，经常需要在 Jenkinsfile 内拼接字符串或使用环境变量作为参数， Jenkinsfile 中的单引号和双引号在使用时，会有些不同的差异， 这里演示一下常用的 echo 与 sh 两个命令的差异。

```groovy
pipeline {
    agent any
    environment {
        MY_ENV = 'this is my env'
    }
    stages {
        stage('Test') {
            steps {
                script    {
                    def MY_ENV = 'define in script'

                    echo "${env.MY_ENV}"
                    // 输出内容为 this is my env

                    echo "\${env.MY_ENV}"
                    // 输出内容为 ${env.MY_ENV}

                    echo "${MY_ENV}"
                    // 输出内容为 define in script

                    echo '${MY_ENV}'
                    // 输出内容为 ${MY_ENV}

                    sh 'echo ${MY_ENV}'
                    // 输出内容为 this is my env

                    sh "echo ${MY_ENV}"
                    // 输出内容为 define in script

                    sh "echo ${env.MY_ENV}"
                    // 输出内容为 this is my env
                }
            }
        }
    }
}
```

从上图输出的结果可以看出：
echo 在使用单引号时，并不会解析里面的 $ 符号，而是直接输出原文；在使用双引号时，会打印出环境变量里的 MY_ENV。
sh 在使用单引号时，将原文当作我们平时在终端里 sh 的命令一样执行，所以可以打印出环境变量里的 MY_ENV。

### 如何在 CODING 持续集成内推送代码

在某些场景下，您可能需要在持续集成阶段推送代码。CODING 的持续集成内置了 Git、SVN 等命令工具，您可以参考如下示例。

Jenkinsfile 配置语法如下：

```groovy
pipeline {
  agent any
  stages {
    stage('检出') {
      steps {
        checkout([
            $class: 'GitSCM', 
            branches: [[name: env.GIT_BUILD_REF]], 
            userRemoteConfigs: [[url: env.GIT_REPO_URL, credentialsId: env.CREDENTIALS_ID]]])
      }
    }
    stage('修改') {
        steps {
            sh "echo '# Hello CODING' > README.md"
            sh "git add ."
            sh "git commit -m 'add README.md' "

        }
    }
    stage('推送') {
        steps {
            // 使用了 CODING 持续集成系统预置的项目令牌环境变量 PROJECT_TOKEN_GK 和 PROJECT_TOKEN 来推送
            // 若希望推送到非本项目或第三方平台的代码仓库，需要自行换成有效的凭据信息
            sh "git push https://${PROJECT_TOKEN_GK}:${PROJECT_TOKEN}
              @e.coding.net/myteam/myrepo.git HEAD:master"
        }
    }
  }
}
```

### Jenkinsfile 两种配置来源的区别

在创建构建计划时，您可以设置 Jenkinsfile 的配置来源，**使用代码仓库中的 Jenkinsfile** 和**使用静态配置的 Jenkinsfile** 有什么区别？

**使用代码仓库中的 Jenkinsfile 有以下特点：**

1. Jenkinsfile 文件存储在所选择的代码仓库中，修改 Jenkinsfile 的同时也更新代码仓库。
2. 任务 Job 的构建可由更新代码触发规则定义，若修改 Jenkinsfile 将会自动触发构建。
3. 在任务 Job 点击立即构建，选择构建目标进行构建时，构建任务的配置将会从所构建目标拉取代码的 Jenkinsfile 进行构建，而不是该任务 Job 里当时配置的 Jenkinsfile。

**使用静态配置的 Jenkinsfile 有以下特点：**

1. 静态配置的 Jenkinsfile 将不会保存在代码仓库中，修改 Jenkinsfile 的同时不会更新代码仓库。
2. 任务 Job 的构建可由更新代码触发规则定义，修改静态配置文件 Jenkinsfile 不会自动触发构建。
3. 在任务 Job 点击立即构建，选择构建目标进行构建时，构建任务将统一使用该静态配置，不再使用代码仓库中的 Jenkinsfile。

**两者区别**

1. 使用代码仓库中的 Jenkinsfile 进行配置，可将 Jenkinsfile 保存到仓库中进行版本记录。而选择使用静态配置的 Jenkinsfile 将不存储在代码版本中，无法进行版本记录。
2. 使用静态配置的 Jenkinsfile 进行配置，构建时所有的构建任务将统一使用该静态配置，每次代码版本更新时将会执行相同的 Jenkinsfile 进行构建。保障构建流程相同。
