## 操作场景
本文档介绍在 Linux 操作系统的腾讯云云服务器（CVM）上通过镜像完成 Node.js 环境搭建。

## 技能要求
腾讯云市场中提供了各个版本的 Node.js 环境，如果您不熟悉 Linux 命令的使用或想快速搭建环境，建议您通过镜像部署 Node.js 环境。如果您对 Linux 系统的使用较为熟悉，需要定制化配置 Node.js 环境，您也可以 [手动搭建 Node.js 环境](https://cloud.tencent.com/document/product/213/38237)。

## 注意事项
- 如果您**未购买**云服务器，您可以在购买云服务器时，通过选择镜像市场中的 Node.js 镜像直接搭建环境。详情可参考 [创建云服务器时搭建 Node.js 环境](#create)。
- 如果您**已购买**云服务器，但该云服务器的操作系统并不具备 Node.js 环境，您可以参考 [更换系统镜像](#change) 完成 Node.js 环境搭建。

## 操作步骤
### 搭建 Node.js 环境
#### 创建云服务器时搭建 Node.js 环境
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“选择镜像”窗口中，选择 nodejs-mysql 镜像。如下图所示：
>?
>- 本文以下图所示 nodejs-mysql 环境系统镜像为例，您可根据实际需求进行选择。
>- 单击镜像名，查看镜像详情。
>
![](https://main.qcloudimg.com/raw/0465b5b0ebd73c0d0dff0ab938a496b7.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。
云服务器创建成功后，您可通过 [部署及测试项目](#inspect) 步骤测试 Node.js 环境是否搭建成功。

#### 更换系统镜像
>!
>- 此步骤通过重装云服务器操作系统来搭建 Java Web 环境，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 了解注意事项。
>- 如果您的云服务器之前使用 Windows 操作系统并挂载了数据盘，请参考 [Windows 重装为 Linux 后读写原 NTFS 类型数据盘](https://cloud.tencent.com/document/product/213/3857) 进行数据盘格式更换，防止重要数据损坏。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，找到需搭建 Node.js 环境的云服务器。
2. 选择右侧的【更多】>【重装系统】。如下图所示：
![](https://main.qcloudimg.com/raw/7f8ccb797a27eb113b32678e7437c86f.png)
3. 在弹出的“重装系统”窗口中，选择【服务市场】，单击 nodejs-mysql 镜像。如下图所示：
![](https://main.qcloudimg.com/raw/6f9ce50a8cd0f571d32fb65939c498b5.png)
4. 根据您的实际需求，选择 Node.js 环境的镜像，并可调整磁盘大小，确认配置信息后，单击【开始重装】。
云服务器创建成功后，您可通过 [部署及测试项目](#inspect) 步骤测试 Node.js 环境是否搭建成功。


### 部署及测试项目<span id="inspect"></span>
>!搭建 Node.js 环境的系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
>
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/2f6c1d0c3ce0b474b0b12bd9c6c9eec5.png)
2. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
3. 执行以下命令，新建并编辑 `test.js` 文件。
```
vim test.js
```
4. 按 “**i**” 切换至编辑模式，将以下内容输入到文件中：
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

## 常见问题
如果您在搭建 Node.js 环境的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。



