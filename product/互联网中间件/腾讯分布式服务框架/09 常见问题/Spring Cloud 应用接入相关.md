### TSF 支持哪些 Spring Cloud 版本？
TSF 目前支持 Spring Cloud Edgware、Spring Cloud Finchley、Spring Cloud Greenwich、Spring Cloud Hoxton 四个版本。
- Spring Cloud Edgwar 对应 Spring Boot 1.5.x
- Spring Cloud Finchley 对应 Spring Boot 2.0.x
- Spring Cloud Greenwich 对应 Spring Boot 2.1.x
- Spring Cloud Hoxton	对应 Spring Boot 2.3.x

TSF 在开源 Spring Cloud 的基础上做了加强，用户只需要替换掉部分依赖并开启注解即可将改造后的应用部署在 TSF 平台上。更多关于 Spring Cloud 的兼容性说明请参考 [Spring Cloud 概述](https://cloud.tencent.com/document/product/649/36285)、[SDK 下载](https://cloud.tencent.com/document/product/649/20231)、[SDK 版本更新日志](https://cloud.tencent.com/document/product/649/38982) 文档。


### 在工程的配置文件中，是否需要填写服务注册中心地址？

- 对于本地开发调试的应用，在启动 Java 应用的启动参数中需要填写轻量级服务注册中心 consul 的 IP 和 Port。配置文件（如 application.yml）中则无需填写。
- 对于通过 TSF 平台部署的应用，既不需要在启动参数中设置注册中心的地址，也不需要在配置文件中设置注册中心地址。SDK 会通过环境变量获取注册中心地址。

