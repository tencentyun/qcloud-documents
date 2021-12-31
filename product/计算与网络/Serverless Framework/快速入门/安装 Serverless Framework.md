## 操作场景
您可以通过 [NPM 安装](#npm) 或 [二进制安装](#binary) 的方式，快速安装 Serverless Framework。


## 安装方式

[](id:npm)
### 方式1：NPM 安装
#### 安装前提
使用 npm 安装前，需要确保您的环境中已安装好了 Node（版本需要 > 10）以及 npm（查看 [Node.js 安装指南](https://nodejs.org/zh-cn/download/)）。
```sh
$ node -v
v12.18.0

$ npm -v
7.0.10
```

>!为保证安装速度和稳定性，建议您使用 cnpm 来完成安装：先下载安装 cnpm，然后将下面所有使用的 npm 命令替换为 cnpm 即可。

#### 安装步骤

在命令行中运行如下命令：
```sh
npm install -g serverless
```
>?如 MacOS 提示无权限，则需要运行`sudo npm install -g serverless`进行安装。

如果之前您已经安装过 Serverless Framework，可以通过以下命令升级到最新版。
```sh
npm update -g serverless
```

#### 查看版本信息
安装完毕后，通过运行`serverless -v`命令，查看 Serverless Framework 的版本信息：
```sh
serverless -v
```


[](id:binary)
### 方式2：二进制安装

如果您的本地环境没有安装 Node.js，您可以直接使用二进制的方式进行安装：

#### MacOS/Linux 系统 

打开命令行，输入以下命令：
```sh
curl -o- -L https://slss.io/install | bash
```

如果之前您已经安装过二进制版本，可以通过下列命令进行升级：
```sh
serverless upgrade
```

#### Windows 系统 

Windows 系统支持通过 [chocolatey](https://chocolatey.org/) 进行安装。打开命令行，输入以下命令：

```sh
choco install serverless
```
如果之前您已经安装过二进制版本，可以通过下列命令进行升级：
```sh
choco upgrade serverless
```


#### 查看版本信息
安装完毕后，通过运行 `serverless -v` 命令，查看 Serverless Framework 的版本信息：
```sh
serverless -v
```

## 相关操作
下一步：快速开始
 - [快速部署函数模版](https://cloud.tencent.com/document/product/1154/50938)
 - [快速创建应用模版](https://cloud.tencent.com/document/product/1154/50933)


