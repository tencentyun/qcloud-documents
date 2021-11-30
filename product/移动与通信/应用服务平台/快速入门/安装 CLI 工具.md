云开发官方提供 [命令行工具（CLI）](https://github.com/TencentCloudBase/cloudbase-cli)，可以使用 CLI 进行云开发资源管控、函数部署等。下面是安装过程：

## 步骤1：确保安装 Node.js 和 npm
如果本机没有安装 Node.js , 建议从 [Node.js 官网](https://nodejs.org/zh-cn/) 下载二进制文件直接安装，建议选择版本为 LTS。

## 步骤2：安装命令行工具
确保步骤1 Node.js 和 npm 安装成功后，使用 npm 命令来安装  cloudbase/cli ，打开命令行终端，输入如下命令：
```bash
npm i -g @cloudbase/cli
```
>? 如果 `npm install -g @cloudbase/cli` 失败，您可能需要 [修改 npm 权限](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)，或者以系统管理员身份运行：
 ```sh
sudo npm install -g @cloudbase/cli
```


## 步骤3：测试安装是否成功
如果安装过程没有错误提示，则安装成功。我们可以输入以下命令测试安装是否成功，如果输出版本号，说明  CLI 工具安装成功。
```bash
cloudbase -v
```

## 查看命令及使用说明
为了简化输入，cloudbase 命令可以简写成 tcb。tcb 是云开发产品英文的简称：Tencent CloudBase。

### 具体命令查看
输入以下命令，可查看目前 CLI 命令行工具支持的所有能力和命令。
```bash
tcb -h
```


### 使用说明
使用 CloudBase CLI 时，需要您的终端能够访问网络。如果您的终端无法直接访问公网，您可以设置 HTTP 代理使 CLI 能够正常使用，CLI 会读取 `http_proxy` 或 `HTTP_PROXY` 环境变量，自动设置网络代理服务。
 例如，您可以在终端中运行以下命令，设置 CLI 通过 `http://127.0.0.1:8000` 的代理服务访问网络：
 ```bash
 export HTTP_PROXY=http://127.0.0.1:8000
 ```
 
>?上面的命令只是临时设置，当您关闭终端后，代理会自动失效，下次开启终端后需要重新设置。如果您需要一直通过代理访问公网，可以把命令加入到终端的配置文件中。


