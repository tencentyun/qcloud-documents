
您可以通过 NPM 安装 Serverless Cloud Framework。




[](id:npm)
## 通过 NPM 安装
#### 安装前提
使用 npm 安装前，需要确保您的环境中已安装好了 Node（**版本需要 > 12**）以及 npm（查看 [Node.js 安装指南](https://nodejs.org/zh-cn/download/)）。
```sh
$ node -v
v12.18.0

$ npm -v
7.0.10
```

>!
>- 为保证安装速度和稳定性，建议您使用 cnpm 来完成安装：先下载安装 cnpm，然后将下面所有使用的 npm 命令替换为 cnpm 即可。
>- scf 是 serverless-cloud-framework 命令的简写。

#### 安装步骤

在命令行中运行如下命令：
```sh
npm i -g serverless-cloud-framework
```
>?如 MacOS 提示无权限，则需要运行`sudo npm i -g serverless-cloud-framework`进行安装。

如果之前您已经安装过 Serverless Cloud Framework，可以通过以下命令升级到最新版。
```sh
npm update -g serverless-cloud-framework
```

#### 查看版本信息
安装完毕后，通过运行`scf -v`命令，查看 Serverless Cloud Framework 的版本信息：
```sh
scf -v
```


[](id:binary)
## 相关操作
下一步：快速开始
 - [快速部署函数模板](https://cloud.tencent.com/document/product/1154/50938)
 - [快速创建应用模板](https://cloud.tencent.com/document/product/1154/50933)

