本篇文档将为您指导，如何通过 Web Function，将您的本地 Express 项目快速部署到云端。

### 模版部署 -- 一键部署 Express 项目
1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的【函数服务】。
2. 在主界面上方选择期望创建函数的地域，并单击【新建】，进入函数创建流程。

3. 选择使用【模版创建】来新建函数，在搜索框里筛选 `WebFunc`，筛选所有 Web 函数模版，选择 `Express 框架模版`，点击“下一步”。如下图所示：
![](https://main.qcloudimg.com/raw/10cb2b9714ee259475f1b67813a53570.png)
4. 在“配置”页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击【完成】，即可创建函数。
函数创建完成后，您可在“函数管理”页面，查看 Web 函数的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Express 项目
![](https://main.qcloudimg.com/raw/d17b4eed35144ba019429a114601cb9a.png)

### 自定义部署 -- 快速迁移本地项目上云
#### 本地开发
1. 首先，在确保您的本地已安装 Node.js 运行环境后，安装 Express 框架和express-generator 脚手架，初始化您的 Express 示例项目
```shell
npm install express --save
npm install express-generator --save
express WebApp
```

2. 进入项目目录，安装依赖包
```
cd WebApp
npm install
```

3. 安装完成后，本地直接启动，在浏览器里访问 `http://localhost:3000`，即可在本地完成Express 示例项目的访问
```
npm start
```

#### 部署上云

接下来，我们对已初始化的项目进行简单修改，使其可以通过 Web Function 快速部署，此处项目改造通常分为两步：

- 修改监听地址与端口，改为 `0.0.0.0:9000`
- 新增 `scf_bootstrap` 启动文件

具体步骤如下：
1. 已知在 Express 示例项目中，通过 `./bin/www` 设置监听地址与端口，打开该文件可以发现，我们可以通过环境变量，设置指定监听端口，否则将自动监听 `3000`
![](https://main.qcloudimg.com/raw/a32fd560e9a6e58e6a1f6a46356324e6.png)
2. 接下来，在项目根目录下新建 `scf_bootstrap` 启动文件，在里面配置环境变量，并指定服务启动命令
```shell
#!/bin/bash
export PORT=9000
npm run start
```
创建完成后，注意修改您的可执行文件权限，默认需要 `777` 或 `755` 权限才可以正常启动
```
chmod 777 scf_bootstrap
```
3. 本地配置完成后，执行启动文件，确保您的服务可以本地正常启动，接下来，登陆腾讯云云函数控制台，新建 Web 函数以部署您的 Express 项目：
![](https://main.qcloudimg.com/raw/a4535e25ce752c3e78fd23e60a6c4744.png)

#### 开发管理
部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势。
![](https://main.qcloudimg.com/raw/2fe04528bf2e33c04ffea558d423ffa1.png)
