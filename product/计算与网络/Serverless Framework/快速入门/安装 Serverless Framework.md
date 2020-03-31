
通过该指南，您可以通过[二进制安装](#二进制安装)或[npm安装](#Npm-安装) 的方式，快速安装 Serverless Framework

## 二进制安装

如果您的本地环境没有安装 Node.js，您可以直接使用二进制的方式进行安装：

### MacOS/Linux 系统 

打开命令行，输入以下命令：
```sh
$ curl -o- -L https://slss.io/install | bash
```

如果之前您已经安装过二进制版本，可以通过下列命令进行升级：
```sh
$ serverless upgrade
```

### Windows 系统 

Windows 系统支持通过[chocolatey](https://chocolatey.org/)进行安装。打开命令行，输入以下命令：
```sh
$ choco install serverless
```
更新命令
```sh
$ choco upgrade serverless
```
## Npm 安装

在命令行中运行如下命令：
```sh
$ npm install -g serverless
```
>? 如 MacOS 提示无权限，则需要运行`sudo npm install -g serverless`进行安装。

如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：
```sh
$ npm update -g serverless
```

安装完毕后，通过运行`serverless -v`命令，查看 Serverless Framework 的版本信息。
```sh
$ serverless -v
```

>? 注：如果您的环境中没有安装 Node.js，可以参考 [Node.js 安装指南](https://nodejs.org/zh-cn/download/) 根据您的系统环境进行安装。



