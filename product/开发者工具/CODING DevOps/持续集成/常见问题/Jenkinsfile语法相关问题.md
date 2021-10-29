[](id:ci-init)
### 为什么使用 ci-init 提示无法拉取代码？

2019 年 10 月 10 日 之前创建的构建计划（ Job ）中的 ci-init 命令会为用户创建一对公私钥，并使其能够拉取项目中的代码仓库。之后创建的构建计划在调用 ci-init 时，将不会创建拉取代码的公私钥对了。

在此之后新创建的构建计划, 我们都会为用户内置一个可以用于拉取对应代码仓库的凭据 ID，直接使用 env.CREDENTIALS_ID 作为 userRemoteConfigs 的 credentialsId 即可。

#### 旧的语法

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

#### 新的语法

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

**CODING 目前已经支持了凭据管理，我们建议用户使用更安全的凭据 ID 来代替之前的 ci-init 操作。**

>? 关于凭据如果您想了解更多请参见 [凭据管理](https://cloud.tencent.com/document/product/1113/48846)。

[](id:apostrophe)
### 单引号和双引号用法差异是什么？

使用 CODING  持续集成时经常需要在 Jenkinsfile 内拼接字符串或使用环境变量作为参数， Jenkinsfile 中的单引号和双引号在使用时，会有些许差异， 以下演示常用的 echo 与 sh 两个命令的差异。

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

- echo 在使用单引号时，并不会解析里面的 $ 符号，而是直接输出原文；在使用双引号时，会打印出环境变量里的 MY_ENV。
- sh 在使用单引号时，将原文当作我们平时在终端里 sh 的命令一样执行，所以可以打印出环境变量里的 MY_ENV。

[](id:source)
### 在创建构建计划时选择使用代码仓库中的 Jenkinsfile 与静态配置的 Jenkinsfile 有什么区别？

- 选择使用代码仓库中的 Jenkinsfile 后，该文件将存储至代码仓库中。修改 Jenkinsfile 意味着需在代码仓库中提交修改记录，若修改持续集成的触发条件，还可以自动触发集成任务。
- 使用静态配置的 Jenkinsfile 后，该文件将不会存储在代码仓库中，修改 Jenkinsfile 不会更新代码仓库内容，执行构建时将统一使用静态配置，保障构建流程的一致性。
