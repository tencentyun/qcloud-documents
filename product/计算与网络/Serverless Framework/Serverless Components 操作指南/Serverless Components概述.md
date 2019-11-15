# Serverless Components介绍

## 什么是Serverless Components？

Serverless Components是支持多个云资源编排和组织的场景化解决方案，主要基于客户的具体场景，如Express框架支持，网站部署等。Serverless Components可以有效简化云资源的配置和管理，将网关，COS和CAM等产品联动起来，让客户更多关注场景和业务。


## Serverless Components和 Serverless Framework CLI的区别是什么？
Serverless Framework CLI是一个覆盖了测试/部署等步骤的工作流框架，主要围绕SCF云函数及其触发器进行配置，支持云函数平台的除Java外所有开发语言（Node.js, Python, PHP, Go等）。

Serverless Components更多面向客户实现场景，支持对云上的多种资源进行部署和编排（COS，API网关，CAM，DB等），同时支持客户自定义对应资源的配置，目前Component主要用Node.js实现。

## 优势特性

- 简便易用：
Serverless Components更多的围绕客户场景进行构建，如网站，博客系统，支付服务，图像处理场景等。通过抽象了底层的基础设施配置信息，开发者可以通过十分简单的配置实现场景。
- 可复用性：
Serverless Components可以通过非常简单的`serverless.yml`创建和部署，但同时也支持用十分简单的语法对javascript库`serverless.js`进行扩展编写和复用。
- 秒级部署：
大多数Serverless Components比传统的配置工具部署快20倍左右，Components可以通过快速的部署和远端验证，有效减少本地模拟和调试的环节。

## 最佳实践

- [Express框架组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/Express%E6%A1%86%E6%9E%B6%E7%BB%84%E4%BB%B6.md)：通过Express 组件，您无需对项目进行大量更改，就可以将现有服务轻松上云：只需短短几秒，便能在腾讯云 Serverless 架构上部署按需计费的 Express.js 应用程序。

- [静态网站组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E9%9D%99%E6%80%81%E7%BD%91%E7%AB%99%E7%BB%84%E4%BB%B6.md)：静态网站组件现已支持最新的 Web 框架和技术（例如：React 和 Vue.js 等应用程序），您可以在几秒钟内将自己的静态网站部署到对象存储COS中。

- [全栈组件(vue.js+express.js)](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E5%85%A8%E6%A0%88%E7%BB%84%E4%BB%B6(vue.js%2Bexpress.js).md)：结合Express组件和Website组件，构建完整前后端的Serverless应用。

## 基础组件列表

最佳实践由基础的产品组件构成，您也可以自行针对基础组件组合，结合自身应用场景进行编排和部署。

- [云函数SCF组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E4%BA%91%E5%87%BD%E6%95%B0SCF%E7%BB%84%E4%BB%B6.md)

- [API网关组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/API%E7%BD%91%E5%85%B3%E7%BB%84%E4%BB%B6.md)

- [对象存储 COS 组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8COS%E7%BB%84%E4%BB%B6.md)

- [访问管理CAM-角色组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E8%AE%BF%E9%97%AE%E7%AE%A1%E7%90%86CAM-%E8%A7%92%E8%89%B2%E7%BB%84%E4%BB%B6.md)

- [访问管理CAM-策略组件](https://github.com/tinafangkunding/qcloud-documents/blob/patch-38/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/Serverless%20Components%20%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E8%AE%BF%E9%97%AE%E7%AE%A1%E7%90%86CAM-%E7%AD%96%E7%95%A5%E7%BB%84%E4%BB%B6.md)


