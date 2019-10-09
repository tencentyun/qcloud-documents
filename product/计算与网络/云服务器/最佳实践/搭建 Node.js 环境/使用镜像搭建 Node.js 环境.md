## 操作场景
本文档介绍在 Linux 操作系统的腾讯云云服务器（CVM）上通过镜像完成 Node.js 环境搭建。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应的操作系统。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择机型，并选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“选择镜像”窗口中，选择 nodejs-mysql 镜像。如下图所示：
>?
>- 本文以下图所示 nodejs-mysql 环境系统镜像为例，您可根据实际需求进行选择。
>- 单击镜像名，查看镜像详情。
>
![](https://main.qcloudimg.com/raw/0465b5b0ebd73c0d0dff0ab938a496b7.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。


### 部署及测试项目
>!
>- 云服务器实例处于运行中时，即可进行测试。
>- 搭建 Node.js 环境的系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
>
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/2f6c1d0c3ce0b474b0b12bd9c6c9eec5.png)
2. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
3. 执行以下命令，新建并编辑 `test.js` 文件。
```
vim test.js
```
4. 按 “**i**” 或 “**Insert**” 切换至编辑模式，将以下内容输入到文件中：
```
const http = require('http');
const hostname = '0.0.0.0';
const port = 8080;
const server = http.createServer((req, res) => { 
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World!\n');
}); 
server.listen(port, hostname, () => { 
    console.log(`Server running at http://${hostname}:${port}/`);
});
```
>?本文在 `test.js` 测试文件中设置端口号为8080，您可根据实际需求自行修改。
>
5. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
4. 执行以下命令，进行测试。
```
node test.js 
```
6. 在浏览器中访问以下地址，查看项目是否正常运行。
```
http://云服务器实例的公网 IP:已配置的端口号
```
显示结果如下，则说明 Node.js 环境搭建成功。
![](https://main.qcloudimg.com/raw/1e552742bacbfbc4d2164f5efe3fc09c.png)



