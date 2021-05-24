Serverless Components 是支持多个云资源编排和组织的场景化解决方案，主要基于客户的具体场景，如 Express 框架支持、网站部署等。Serverless Components 可以有效简化云资源的配置和管理，将网关、COS 和 CAM 等产品联动起来，让客户更多关注场景和业务。

详细介绍可以参考 [Github 上的 Serverless Components 项目](https://github.com/serverless/components/blob/master/README.cn.md)。

### Serverless Components 优势

- **简便易用**
Serverless Components 更多的围绕客户场景进行构建，如网站、博客系统、支付服务、图像处理场景等。通过抽象了底层的基础设施配置信息，开发者可以通过十分简单的配置实现场景。
- **可复用性**
Serverless Components 可以通过非常简单的`serverless.yml`创建和部署，但同时也支持用十分简单的语法对 JavaScript 库`serverless.js`进行扩展编写和复用。
- **秒级部署**
大多数 Serverless Components 比传统的配置工具部署快20倍左右，Components 可以通过快速的部署和远端验证，有效减少本地模拟和调试的环节。

### Serverless Framework Components 最佳实践

- [@serverless/tencent-scf](https://github.com/serverless-components/tencent-scf/tree/master/) - 腾讯云云函数组件
- [@serverless/tencent-express](https://github.com/serverless-components/tencent-express/tree/master/) - 快速部署基于 Express.js 的后端服务到腾讯云函数的组件
- [@serverless/tencent-website](https://github.com/serverless-components/tencent-website/tree/master/) - 快速部署静态网站到腾讯云的组件


### Serverless Components 支持列表

当前 Serverless Components 支持丰富的多语言开发框架和应用，具体如下：

**基础组件**：
-  [@serverless/tencent-postgresql](https://github.com/serverless-components/tencent-postgresql/tree/master) - 腾讯云 PG DB Serverless 数据库组件
- [@serverless/tencent-apigateway](https://github.com/serverless-components/tencent-apigateway) - 腾讯云 API 网关组件
- [@serverless/tencent-cos](https://github.com/serverless-components/tencent-cos) - 腾讯云对象存储组件
- [@serverless/tencent-scf](https://github.com/serverless-components/tencent-scf/tree/master) - 腾讯云云函数组件
- [@serverless/tencent-cdn](https://github.com/serverless-components/tencent-cdn) - 腾讯云 CDN 组件
- [@serverless/tencent-vpc](https://github.com/serverless-components/tencent-vpc/tree/master) - 腾讯云 VPC 私有网络组件



**高阶组件**：
- [@serverless/tencent-nextjs](https://github.com/serverless-components/tencent-nextjs/tree/master) - 快速部署基于 Next.js 框架到腾讯云函数的组件
- [@serverless/tencent-nuxtjs](https://github.com/serverless-components/tencent-nuxtjs/tree/master) - 快速部署基于 Nuxt.js 框架到腾讯云函数的组件
- [@serverless/tencent-express](https://github.com/serverless-components/tencent-express/tree/master) - 快速部署基于 Express.js 的后端服务到腾讯云函数的组件
- [@serverless/tencent-egg](https://github.com/serverless-components/tencent-egg/tree/master) - 快速部署基于 Egg.js 的后端服务到腾讯云函数的组件
- [@serverless/tencent-koa](https://github.com/serverless-components/tencent-koa/tree/master) - 快速部署基于 Koa.js 的后端服务到腾讯云函数的组件
- [@serverless/tencent-flask](https://github.com/serverless-components/tencent-flask) - 腾讯云 Python Flask RESTful API 组件
- [@serverless/tencent-django](https://github.com/serverless-tencent/tencent-django/tree/master) - 腾讯云 Python Django RESTful API 组件
- [@serverless/tencent-laravel](https://github.com/serverless-components/tencent-laravel) - 腾讯云 PHP Laravel RESTful API 组件
- [@serverless/tencent-thinkphp](https://github.com/serverless-components/tencent-thinkphp) - 腾讯云 ThinkPHP RESTful API 组件
- [@serverless/tencent-website](https://github.com/serverless-components/tencent-website/tree/master) - 快速部署静态网站到腾讯云的组件

**第三方贡献**：
- [@authing/serverless-oidc](https://github.com/Authing/serverless-oidc) - 快速部署基于 Authing 的身份认证组件
- [@twn39/tencent-fastify](https://github.com/twn39/tencent-fastify) - 快速部署基于 fastify.js 的后端服务到腾讯云函数的组件
- [@twn39/tencent-php-slim](https://github.com/twn39/tencent-php-slim) - 快速部署基于 Slim PHP 微框架的后端服务到腾讯云函数的组件

此外，所有的 Serverless Components 均可在 [Github 仓库](https://github.com/serverless-components?q=tencent) 中查看，查看时请注意切换至最新的**v2**版本。
![](https://main.qcloudimg.com/raw/8d30e522c8a8d3e46a8b057eaa161a13.png)
