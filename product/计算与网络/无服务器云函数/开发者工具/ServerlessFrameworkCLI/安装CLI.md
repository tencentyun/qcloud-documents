## 操作场景
本文介绍通过 [二进制安装](#binary) 或 [NPM 安装](#npm) 的方式，快速安装 Serverless Framework。


## 操作步骤
<span id="binary"></span>
### 方式1：二进制安装

如果您的本地环境未安装 Node.js，您可以直接使用二进制的方式进行安装：

#### MacOS/Linux 系统 
在命令行中，执行以下命令。
```sh
curl -o- -L https://slss.io/install | bash
```
如果您已经安装过二进制版本，则可以通过执行以下命令进行升级。
```sh
serverless upgrade
```

#### Windows 系统 

Windows 系统支持通过 [chocolatey](https://chocolatey.org/) 进行安装。在命令行中，执行以下命令。
```sh
choco install serverless
```
如果您已经安装过二进制版本，则可以通过执行以下命令进行升级。
```sh
choco upgrade serverless
```

<span id="npm"></span>
### 方式2：NPM 安装
>?如果您的本地环境未安装 Node.js，可参考 [Node.js 安装指南](https://nodejs.org/zh-cn/download/) 根据本地系统环境进行安装。
>
在命令行中，执行以下命令。
```sh
npm install -g serverless
```
若 MacOS 或 Linux 系统提示无权限，则需执行 `sudo npm install -g serverless` 命令进行安装。
如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：
```sh
npm update -g serverless
```


### 安装验证
安装完毕后，在命令行中执行以下命令，查看 Serverless Framework 的版本信息。
```sh
serverless -v
```
返回类似如下信息，则表示安装成功。
```
Framework Core: 1.71.1
Plugin: 3.6.12
SDK: 2.3.0
Components: 2.30.11
```


