## 操作场景
本文档介绍如何在腾讯云云服务器（CVM）上手动部署 Node.js 环境，并创建示例项目。

进行手动搭建 Node.js 环境，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件使用、配置和兼容性比较了解。
<dx-alert infotype="explain" title="">
腾讯云建议您可以通过云市场的镜像环境部署 Node.js 环境，手动搭建 Node.js 环境可能需要较长的时间。具体步骤可参考 [镜像部署 Node.js 环境](https://cloud.tencent.com/document/product/213/38236)。
</dx-alert>



## 示例软件版本
本文搭建 Node.js 环境使用软件版本及组成说明如下：
- 操作系统：Linux 系统，本文以 CentOS 7.6 为例。
- Node.js：JavaScript 的运行环境，本文以 Node.js 10.16.3 及 Node.js 6.9.5 为例。
- npm：Node.js 节点版本管理器，管理多个 Node.js 版本，本文以 npm 6.9.0 为例。

## 前提条件
已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)


### 步骤2：安装 Node.js
1. 执行以下命令，下载 Node.js Linux 64位二进制安装包。
```
wget https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz
```
<dx-alert infotype="explain" title="">
您可前往 [Node.js 官网](https://nodejs.org/zh-cn/download/) 获取更多安装信息。
</dx-alert>
2. 执行以下命令，解压安装包。
```
tar xvf node-v10.16.3-linux-x64.tar.xz
```
3. 依次执行以下命令，创建软链接。
```
ln -s /root/node-v10.16.3-linux-x64/bin/node /usr/local/bin/node
```
```
ln -s /root/node-v10.16.3-linux-x64/bin/npm /usr/local/bin/npm
```
成功创建软链接后，即可在云服务器任意目录下使用 node 及 npm 命令。
4. 依次执行以下命令，查看 Node.js 及 npm 版本信息。
```
node -v
```
```
npm -v
```

### 步骤3：安装 Node.js 多版本（可选）


<dx-alert infotype="explain" title="">
此步骤通过 npm 安装多个版本的 Node.js，并可快速进行切换。适用于开发人员，您可根据实际需求进行安装。
</dx-alert>


1. 执行以下命令，安装 git。
```
yum install -y git
```
2. 执行以下命令，下载 NVM 源码并检查最新版本。
```
git clone git://github.com/cnpm/nvm.git ~/.nvm && cd ~/.nvm && git checkout `git describe --abbrev=0 --tags`
```
3. 执行以下命令，配置 NVM 环境变量。
```
echo ". ~/.nvm/nvm.sh" >> /etc/profile
```
4. 执行以下命令，读取环境变量。
```
source /etc/profile
```
4. 执行以下命令，查看 Node.js 所有版本。
```
nvm list-remote
```
5. 依次执行以下命令，安装多个版本的 Node.js。
```
nvm install v6.9.5
```
```
nvm install v10.16.3
```
6. 执行以下命令，查看已安装的 Node.js 版本。
```
nvm ls
```
返回结果如下所示，则表示安装成功，当前使用版本为 Node.js 10.16.3。
![](https://main.qcloudimg.com/raw/a315fe51314357fb44ec725f20c101ed.png)
7. 执行以下命令，切换 Node.js 使用版本。
```
nvm use v6.9.5
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/817fd96fef77f818e65ce41a3723e5bc.png)

### 步骤4：创建 Node.js 项目
1. 依次执行以下命令，在根目录创建项目文件 `index.js`。
```
cd ~
```
```
vim index.js
```
2. 按 **i** 切换至编辑模式，并将以下内容输入 `index.js` 文件中。
```
const http = require('http');
const hostname = '0.0.0.0';
const port = 7500;
const server = http.createServer((req, res) => { 
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
}); 
server.listen(port, hostname, () => { 
    console.log(`Server running at http://${hostname}:${port}/`);
});
```
<dx-alert infotype="explain" title="">
本文在 `index.js` 项目文件中使用端口号为7500，您可根据实际需求自行修改。
</dx-alert>
3. 按 **Esc**，输入 **:wq** 并按 **Enter**，保存文件并返回。
4. 执行以下命令，运行 Node.js 项目。
```
node index.js
```
5. 在本地浏览器中访问以下地址，查看项目是否正常运行。
```
http://云服务器实例的公网 IP:已配置的端口号
```
显示结果如下，则说明 Node.js 环境搭建成功。
![](https://main.qcloudimg.com/raw/5b72798dc9e988eee8d8186055aa45e9.png)


## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。


