## 操作场景

Malagu 提供了一个很强大的命令行工具 `@malagu/cli`，设计思路部分借鉴了 `@vue/cli`。应用的初始化、运行、构建和部署等操作都是基于该命令行工具完成。了解更多请参见 [命令行工具](https://www.yuque.com/cellbang/malagu/xbfpir) 文档。本文将通过以下步骤为您介绍如何创建第一个应用。



## 操作步骤

### 快速初始化

1. 执行以下命令，安装 `@malagu/cli` 命令行工具。
```sh
npm i -g @malagu/cli
```
2. 使用 `malagu init` 命令初始化一个模板应用， `malagu init` 可以指定项目名称和模板，如果未指定，则会让您选择一个合适的模板，并且项目名称为模板名称。
```sh
malagu init
## 国内用户可以使用镜像源加速
npm i @malagu/cli -g --registry=https://registry.npm.taobao.org
malagu init
```
选择模板：
```
➜  js malagu init
                   ___
 /'\_/`\          /\_ \
/\      \     __  \//\ \      __       __   __  __
\ \ \__\ \  /'__`\  \ \ \   /'__`\   /'_ `\/\ \/\ \
 \ \ \_/\ \/\ \L\.\_ \_\ \_/\ \L\.\_/\ \L\ \ \ \_\ \
  \ \_\\ \_\ \__/.\_\/\____\ \__/.\_\ \____ \ \____/
   \/_/ \/_/\/__/\/_/\/____/\/__/\/_/\/___L\ \/___/
                                       /\____/
                   @malagu/cli@1.18.3  \_/__/
? Select a template to init (Use arrow keys or type to search)
❯ backend-app Official
  sample-app Official
  vue-app Official
  database-app Official
  admin-app Official
  microservice Official
  file-service Official
  puppeteer Official
  monorepo Official
  mycli Official
```
3. 选择完模板类型后，会基于该模板创建好应用，并安装好相关依赖。安装的时候，命令行工具根据当前环境，智能选择包管理器。如果环境中只存在 npm 工具，则选择 npm，否则优先使用 yarn 工具。
本文示例选择 `backend-app` 模板，应用初始化好后，效果如下：
```
➜  js malagu init
                   ___
 /'\_/`\          /\_ \
/\      \     __  \//\ \      __       __   __  __
\ \ \__\ \  /'__`\  \ \ \   /'__`\   /'_ `\/\ \/\ \
 \ \ \_/\ \/\ \L\.\_ \_\ \_/\ \L\.\_/\ \L\ \ \ \_\ \
  \ \_\\ \_\ \__/.\_\/\____\ \__/.\_\ \____ \ \____/
   \/_/ \/_/\/__/\/_/\/____/\/__/\/_/\/___L\ \/___/
                                       /\____/
                   @malagu/cli@1.18.3  \_/__/
? Select a template to init backend-app Official
yarn install v1.22.4
info No lockfile found.
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
[4/4] 🔨  Building fresh packages...
success Saved lockfile.
✨  Done in 57.52s.
Success! Initialized "backend-app" example in /Users/kevin/js/backend-app.
```
初始化后的项目关键目录结构如下：
```sh
.
├── src
│   ├── module.ts # 模块入口文件
│   └── home-controller.ts
├── tsconfig.json
└── package.json
```
可以发现 Malagu 的应用没有应用启动入口文件，本质上该文件存在，只不过框架默认实现了应用启动入口文件。
绝大部分情况，开发者无需关心。当然，开发者也可以自定义入口文件。在 Malagu 里，一切皆组件，应用也是一个组件，是一个根组件。组件也是一个普通的 nodejs 包，自定义组件将极其简单且统一。需要注意框架会约定模块入口文件的加载位置，开发者也可以自定义模块入口文件加载位置。
>?Malagu 的一个核心设计原则是，约定大于配置。


### 本地运行应用

Malagu 命令行工具提供了一个支持 HMR（热模块替换）能力的本地运行命令 `malagu serve` 。另外，除了 `malagu init` 命令外，其他命令都是应用上下文感知命令，也就是说，Malagu 会将这些命令委托给应用中依赖的 `@malagu/cli-service` 去执行。这样做的好处是让全局命令的行为永远与当前应用依赖的框架版本保持一致，同时，也让 `@malagu/cli` 体积变小且稳定，安装速度很快，也无需经常升级。
```sh
malagu serve
open http://localhost:3000
```
运行实例如下：
```
➜  backend-app malagu serve
                   ___
 /'\_/`\          /\_ \
/\      \     __  \//\ \      __       __   __  __
\ \ \__\ \  /'__`\  \ \ \   /'__`\   /'_ `\/\ \/\ \
 \ \ \_/\ \/\ \L\.\_ \_\ \_/\ \L\.\_/\ \L\ \ \ \_\ \
  \ \_\\ \_\ \__/.\_\/\____\ \__/.\_\ \____ \ \____/
   \/_/ \/_/\/__/\/_/\/____/\/__/\/_/\/___L\ \/___/
                                       /\____/
                   @malagu/cli@1.18.3  \_/__/
malagu mode - local
malagu component - @malagu/core@^1.18.2
malagu component - @malagu/web@^1.18.2
malagu component - @malagu/mvc@latest
malagu component - @malagu/cloud@^1.18.2
malagu component - @malagu/faas-adapter@^1.18.2
malagu component - @malagu/fc-adapter@latest
malagu component - backend-app@0.0.0
malagu target - backend
malagu module - @malagu/web/lib/common/module
malagu module - @malagu/web/lib/node/module
malagu module - @malagu/mvc/lib/node/module
malagu module - @malagu/cloud/lib/node/module
malagu module - @malagu/faas-adapter/lib/node/module
malagu module - @malagu/fc-adapter/lib/node/module
malagu module - /Users/kevin/js/backend-app/src/module
 DONE  Compiled successfully in 1028ms 上午10:21:03
 I  The backend is running at http://localhost:3000
Build completed in 0.722s
```
支持 HMR 功能，修改代码无需重启，快速调试验证。另外，Malagu 模板默认提供了与 vscode 单步调试能力，开箱即用。

### 部署应用

Malagu 框架提供了 `malagu deploy` 命令用于部署。与传统框架最大的区别在于提供了体验极致的一键部署、多环境支持、开箱即用的 CICD 能力。该能力的实现得益于 Serverless 技术的发展。

执行以下命令，如果您是首次部署，命令行工具会自动提示您输入云平台相关的访问密钥信息（AccessKey），您也可以在项目根目录下执行 `malagu config` 手动配置或修改访问密钥信息。了解更多请参见 [平台访问密钥配置](https://www.yuque.com/cellbang/malagu/ktefxi)。
```sh
malagu deploy
```
![](https://main.qcloudimg.com/raw/6304e789ecad77458aebf176c8036424.png)
部署成功后的效果图如下：
![](https://main.qcloudimg.com/raw/909bb22722a4da57a9609ed85a5a9105.png)
