本文为您详细介绍如何在持续集成中使用 SSH 登录远端服务器。

## 前提条件

使用 CODING 持续集成的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见  [开通服务](https://cloud.tencent.com/document/product/1115/37268)。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 进入项目后单击左下角的**项目设置**。

## 功能介绍

在持续集成中执行构建时，您可能需要 SSH 登录到一个远端服务器以执行必要的脚本或者指令。CODING 持续集成当中已预装了 SSH 相关插件。

## 如何使用 SSH 相关指令

CODING 持续集成中内置了 SSH 相关指令，支持您通过 SSH 对远端机器进行操作。

-   sshCommand：在远端机器执行指定命令
-   sshPut：将当前工作空间的文件/目录放置到远端机器
-   sshGet：从远端机器获取文件/目录到当前工作空间
-   sshScript：读取本地 shell 脚本，在远端机器执行，而不是执行远端机器上的脚本，否则将会报错：**does not exists**。
-   sshRemove：将远端机器的某个文件/目录移除

如何通过账号 + 密码连接远端机器并执行 SSH 相关命令？Jenkinsfile 配置示例如下：

```groovy
def remote = [:]
remote.name = "node"
remote.host = "node.abc.com"
remote.allowAnyHosts = true

node {
    withCredentials([usernamePassword(credentialsId: 'sshUserAcct', 
        passwordVariable: 'password', usernameVariable: 'userName')]) {
        remote.user = userName
        remote.password = password

        stage("SSH Steps Rocks!") {
            writeFile file: 'test.sh', text: 'ls'
            sshCommand remote: remote, 
                command: 'for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done'
            sshScript remote: remote, script: 'test.sh'
            sshPut remote: remote, from: 'test.sh', into: '.'
            sshGet remote: remote, from: 'test.sh', into: 'test_new.sh', override: true
            sshRemove remote: remote, path: 'test.sh'
        }
    }
}
```

## 如何使用 SSH 私钥连接到远端服务

除了上述示例通过账号 + 密码连接远端服务外 ，您还可以通过 SSH 私钥来连接到远端服务，Jenkinsfile 配置示例如下：

```groovy
def remote = [:]
remote.name = "node"
remote.host = "node.abc.com"
remote.allowAnyHosts = true

node {
    withCredentials([sshUserPrivateKey(credentialsId: 'sshUser', keyFileVariable: 'identity')]) {
        // ssh 登录用户名
        remote.user = 'root'
        // 私钥文件地址
        remote.identityFile = identity
        stage("SSH Steps Rocks!") {
            writeFile file: 'abc.sh', text: 'ls'
            sshCommand remote: remote, 
                command: 'for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done'
            sshPut remote: remote, from: 'abc.sh', into: '.'
            sshGet remote: remote, from: 'abc.sh', into: 'bac.sh', override: true
            sshScript remote: remote, script: 'abc.sh'
            sshRemove remote: remote, path: 'abc.sh'
        }
    }
}
```

## 拓展阅读
[](id:java)
-   想要查看一个通过 SSH 登录远程 Linux Docker 服务器并将镜像部署上去的配置，您可以查看帮助文档 [持续集成的自动化部署](https://cloud.tencent.com/document/product/1115/49472)

-   想要了解更多 Jenkinsfile 中关于 SSH 命令的内容，您可以查看 Jenkins 帮助文档 [SSH Pipeline Steps](https://jenkins.io/doc/pipeline/steps/ssh-steps/)

-   想要了解更多 Jenkins 的 SSH 插件相关内容，您可以查看该插件的官方主页 [ssh-steps-plugin](https://github.com/jenkinsci/ssh-steps-plugin)



