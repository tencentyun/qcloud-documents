应用中心框架部署方案已经全新升级，您可以通过 `SCF Web Function`，快速部署您的 Egg 业务上云。

>! **应用控制台部署与函数直接部署有什么区别？**
通过应用部署或函数部署，均可以基于 Web 函数，快速部署常见 Web 框架。
- 如果您只关注代码逻辑开发，无需额外资源创建，可以通过 SCF 云函数控制台，完成快速部署。
- 如果除了代码部署外，您还需要更多能力或资源创建，如自动创建层托管依赖、一键实现静态资源分离、支持代码仓库直接拉取等，可以通过应用控制台，完成 Web 应用的创建工作。

本篇文档为您介绍应用控制台的部署方案，您也可以通过命令行完成部署，具体操作请参考 [产品文档](https://cloud.tencent.com/document/product/583/58183)。

## 模版部署 -- 部署 Egg 示例代码
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)。
2. 选择**Web 应用>Egg 框架**，如下图所示：
![](https://main.qcloudimg.com/raw/379ce45910fccfa28f3e8c50de0fa00d.png)
3. 单击“下一步”，完成基础配置选择。
![](https://main.qcloudimg.com/raw/9f22f8c1e5426b5d3d54631caabde012.png)
4. 上传方式，选择**示例代码**直接部署，单击**完成**，即可开始应用的部署。
5. 部署完成后，您可在应用详情页面，查看示例应用的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Egg 项目。
![](https://main.qcloudimg.com/raw/34cffcca8981ad1d207ee7fc4d32bd53.png)

## 自定义部署 -- 快速部署 Web 应用
### 前提条件

本地已安装 Node.js 运行环境。

### 本地开发

1. 参考 [Egg.js](https://eggjs.org/zh-cn/intro/quickstart.html) 官方文档，快速初始化示例项目：
```sh
mkdir egg-example && cd egg-example
npm init egg --type=simple
npm i
```

2. 在根目录下，执行以下命令在本地直接启动服务。
```shell
npm run dev
open http://localhost:7001
```

3. 打开浏览器，即可在本地完成 Egg 示例项目的访问。

### 部署上云

接下来执行以下步骤，对本地已创建完成的项目进行简单修改，使其可以通过 Web Function 快速部署，对于 Egg 框架，具体改造说明如下：

- 修改监听地址与端口为 `0.0.0.0:9000`。
- 修改写入路径，serverless 环境下只有 `/tmp` 目录可读写。
- 新增 `scf_bootstrap` 启动文件。

**1. (可选)配置 scf_bootstrap 启动文件**

>? 您也可以在控制台完成该模块配置。
>

在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件添加如下内容（用于配置环境变量和启动服务，此处仅为示例，具体操作请以您实际业务场景来调整）：

```sh
#!/var/lang/node12/bin/node

'use strict';

/**
 * docker 中 node 路径：/var/lang/node12/bin/node
 * 由于 serverless 函数只有 /tmp 读写权限，所以在启动时需要修改两个环境变量
 * NODE_LOG_DIR 是为了改写 egg-scripts 默认 node 写入路径（~/logs）-> /tmp
 * EGG_APP_CONFIG 是为了修改 egg 应有的默认当前目录 -> /tmp
 */

process.env.EGG_SERVER_ENV = 'prod';
process.env.NODE_ENV = 'production';
process.env.NODE_LOG_DIR = '/tmp';
process.env.EGG_APP_CONFIG = '{"rundir":"/tmp","logger":{"dir":"/tmp"}}';

const { Application } = require('egg');

// 如果通过层部署 node_modules 就需要修改 eggPath
Object.defineProperty(Application.prototype, Symbol.for('egg#eggPath'), {
  value: '/opt',
});

const app = new Application({
  mode: 'single',
  env: 'prod',
});

app.listen(9000, '0.0.0.0', () => {
  console.log('Server start on http://0.0.0.0:9000');
});
```

新建完成后，还需执行以下命令修改文件可执行权限，默认需要 `777` 或 `755` 权限才可正常启动。示例如下：
```sh
chmod 777 scf_bootstrap
```


**2. 控制台上传**


登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，选择**Web 应用>Egg 框架**，上传方式可以选择**本地上传**或**代码仓库拉取**。

您可以在控制台完成启动文件 `scf_bootstrap` 内容配置，配置完成后，控制台将为您自动生成 启动文件，和项目代码一起打包部署。
>! 启动文件以项目内文件为准，如果您的项目里已经包含 `scf_bootstrap` 文件，将不会覆盖该内容。
>

配置完成后，单击**完成**，部署您的 Egg 项目。
![](https://main.qcloudimg.com/raw/a28efc9156bc3ba9ab817be16a463a02.png)

#### 高级配置管理
您可在“高级配置”里进行更多应用管理操作，如创建层、绑定自定义域名、配置环境变量等。
![](https://main.qcloudimg.com/raw/5a788f4872c1e431e375f445f157b1e2.png)
