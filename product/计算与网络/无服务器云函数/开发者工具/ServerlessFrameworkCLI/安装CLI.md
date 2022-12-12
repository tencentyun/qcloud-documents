## 操作场景
本文介绍通过 [NPM 安装](#npm) 快速安装 Serverless Cloud Framework。


##  通过 NPM 安装
>?如果您的本地环境未安装 Node.js，可参考 [Node.js 安装指南](https://nodejs.org/zh-cn/download/) 根据本地系统环境进行安装。
>
在命令行中，执行以下命令。
```sh
npm i -g serverless-cloud-framework
```
若 MacOS 或 Linux 系统提示无权限，则需执行 `sudo npm i -g serverless-cloud-framework` 命令进行安装。
如果之前您已经安装过 Serverless Cloud Framework，可以通过下列命令升级到最新版：
```sh
npm update -g serverless-cloud-framework
```


### 安装验证
安装完毕后，在命令行中执行以下命令，查看 Serverless Cloud Framework 的版本信息。
```sh
scf -v
```
返回类似如下信息，则表示安装成功。
```
Framework Core: 1.71.1
Plugin: 3.6.12
SDK: 2.3.0
Components: 2.30.11
```

