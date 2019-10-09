## 操作场景
本文档以 CentOS 7.6 的 Linux 操作系统为例的腾讯云云服务器（CVM）为例，手动部署 Node.js 环境并创建示例项目。
本文档包含软件安装内容，请确保您已熟悉软件安装方法，详情请参见 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046)。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤

### 创建并登录云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应的操作系统。
>
1. 在实例的管理页面，单击【新建】。
具体操作请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回至 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看和获取实例的以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/96a5f8e2eca54d4ea3ec56cb439b025a.png)
 - 云服务器实例用户名和密码。
 - 云服务器实例公网 IP。
3. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
登录云服务器后，默认已获取 root 权限，以下步骤需在 root 权限下操作。

### 安装 Node.js
1. 执行以下命令，下载 Node.js Linux 64位二进制安装包。
>?本文以 Node.js 10.16.3 版本为例，请根据您的实际需求从 [Node.js 官网](https://nodejs.org/zh-cn/download/) 下载对应版本。
>
```
wget https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz
```
2. 执行以下命令，解压安装包。
```
tar xvf node-v10.16.3-linux-x64.tar.xz
```
3. 依次执行以下命令，创建软链接。
```
ln -s /root/node-v10.16.3-linux-x64/bin/node /usr/local/bin/node
ln -s /root/node-v10.16.3-linux-x64/bin/npm /usr/local/bin/npm
```
成功创建软链接后，即可在云服务器任意目录下使用 node 及 npm 命令。
4. 依次执行以下命令，查看 Node.js 及 npm 版本。
```
node -v
npm -v
```

### 安装 Node.js 多版本（可选）
>?此步骤使用 NVM（Node Version Manager）Node.js 节点版本管理器，来管理多个 Node.js 版本，您可根据实际需求进行安装。
>
1. 执行以下命令，安装 git。
```
yum install -y git
```
2. 执行以下命令，下载 NVM 源码并检查最新版本。
```
git clone https://github.com/cnpm/nvm.git ~/.nvm && cd ~/.nvm && git checkout `git describe --abbrev=0 --tags`
```
3. 依次执行以下命令，配置 NVM 环境变量。
```
echo ". ~/.nvm/nvm.sh" >> /etc/profile
source /etc/profile
```
4. 执行以下命令，查看 Node.js 所有版本。
```
nvm list-remote
```
5. 依次执行以下命令，安装多个版本的 Node.js。
>?本文以 Node.js 6.9.5 及 10.16.3 为例，您可根据实际需求进行安装。
>
```
nvm install v6.9.5
nvm install v10.16.3
```
6. 执行以下命令，查看已安装的 Node.js 版本。
```
nvm ls
```
返回结果如下所示，则表示安装成功，且当前使用版本为 Node.js 10.16.3。
![](https://main.qcloudimg.com/raw/a315fe51314357fb44ec725f20c101ed.png)
7. 执行以下命令，切换 Node.js 使用版本。
```
nvm use v6.9.5
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/817fd96fef77f818e65ce41a3723e5bc.png)

### 创建 Node.js 项目
1. 依次执行以下命令，创建项目文件 `index.js`。
```
cd ~
vim index.js
```
2. 按 “**i**” 或 “**Insert**” 切换至编辑模式，并将以下内容输入 `index.js` 文件中。
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
>?本文在 `index.js` 项目文件中使用端口号为7500，您可根据实际需求自行修改。
>
3. 按“**Esc**”，输入“**:wq**”，保存文件并返回。
4. 执行以下命令，运行 Node.js 项目。
```
node index.js
```
5. 在浏览器中访问以下地址，查看项目是否正常运行。
```
http://云服务器实例的公网 IP:已配置的端口号
```
显示结果如下，则说明 Node.js 环境搭建成功。
![](https://main.qcloudimg.com/raw/5b72798dc9e988eee8d8186055aa45e9.png)
