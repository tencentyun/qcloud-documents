Serverless Components 是支持多个云资源编排和组织的场景化解决方案，主要基于客户的具体场景，如 Express 框架支持、网站部署等。Serverless Components 可以有效简化云资源的配置和管理，将网关、COS 和 CAM 等产品联动起来，让客户更多关注场景和业务。


## Components 和 Framework CLI 的区别


| 对比项 | 功能描述 | 配置说明 | 支持的语言 |
|---------|---------|---------|---------|
| Serverless Framework | 覆盖了测试/部署等步骤的工作流框架 | 主要围绕云函数 SCF 及其触发器进行配置 | 支持云函数平台的除 Java 外所有开发语言（Node.js、Python、PHP、Go 等） |
| Serverless Components | 面向客户实现场景，支持对云上的多种资源进行部署和编排（COS、API 网关、CAM、DB 等） | 支持客户自定义对应资源的配置| Component 本身由 Node.js 开发，但使用时支持多种语言及开发框架  |

## 优势特性

- **简便易用**
Serverless Components 更多的围绕客户场景进行构建，如网站、博客系统、支付服务、图像处理场景等。通过抽象了底层的基础设施配置信息，开发者可以通过十分简单的配置实现场景。
- **可复用性**
Serverless Components 可以通过非常简单的`serverless.yml`创建和部署，但同时也支持用十分简单的语法对 JavaScript 库`serverless.js`进行扩展编写和复用。
- **秒级部署**
大多数 Serverless Components 比传统的配置工具部署快20倍左右，Components 可以通过快速的部署和远端验证，有效减少本地模拟和调试的环节。

## 最佳实践
 
- **[快速部署 Express 框架](https://cloud.tencent.com/document/product/1154/39269)**
通过Express 组件，您无需对项目进行大量更改，就可以将现有服务轻松上云：只需短短几秒，便能在腾讯云 Serverless 架构上部署按需计费的 Express.js 应用程序。
- **[快速部署静态网站](https://cloud.tencent.com/document/product/1154/39276)**
静态网站组件现已支持最新的 Web 框架和技术（例如：React 和 Vue.js 等应用程序），您可以在几秒钟内将自己的静态网站部署到对象存储 COS 中。
- **[快速部署一个全栈应用（vue.js+express.js）](https://cloud.tencent.com/document/product/1154/39272)**
结合 Express 组件和 Website 组件，构建完整前后端的 Serverless 应用。

## 基础组件

最佳实践由基础的产品组件构成，您也可以自行针对基础组件组合，结合自身应用场景进行编排和部署。

- [云函数 SCF 组件](https://cloud.tencent.com/document/product/1154/39271)
- [API 网关组件](https://cloud.tencent.com/document/product/1154/39268)
- [对象存储 COS 组件](https://cloud.tencent.com/document/product/1154/39273)
- [访问管理 CAM-角色组件](https://cloud.tencent.com/document/product/1154/39275)
- [访问管理 CAM-策略组件](https://cloud.tencent.com/document/product/1154/39274)


