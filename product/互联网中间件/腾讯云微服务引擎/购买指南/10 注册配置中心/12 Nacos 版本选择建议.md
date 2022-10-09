
本文介绍常见的微服务框架（Spring Boot，Spring Cloud，Spring Cloud Alibaba）与开源版本 Nacos 的对应关系、和腾讯云 TSE Nacos 和社区版 Nacos 的兼容性说明、以及 Nacos 客户端与服务端的版本兼容关系，帮助您在使用腾讯云 TSE Nacos 注册配置中心时根据业务需求选择更加适合您的版本。



## 微服务框架与开源版本 Nacos 关系说明

由于 Spring Boot 2.4+ 和以下版本之间变化较大，目前企业级客户老项目相关 Spring Boot 版本仍停留在 Spring Boot 2.4 以下，为了同时满足存量用户和新用户不同需求，社区以 Spring Boot 2.4 为分界线，同时维护 2.2.x 和 2021.x 两个分支迭代。

### 2021.x 分支

适配 Spring Boot 2.4，Spring Cloud 2021.x 版本及以上的 Spring Cloud Alibaba 版本如下表（最新版本用 `*` 标记）：
>! 该分支 Spring Cloud Alibaba 版本命名方式进行了调整，未来将对应 Spring Cloud 版本， 前三位为 Spring Cloud 版本，最后一位为扩展版本，例如适配 Spring Cloud 2021.0.1 版本对应的 Spring Cloud Alibaba 第一个版本为：2021.0.1.0，第个二版本为：2021.0.1.1，依此类推。

| Spring Cloud Alibaba 版本 |   Spring Cloud 版本   | Spring Boot 版本 |
| ------------------------- | :-------------------: | :--------------: |
| 2021.0.1.0\*               | Spring Cloud 2021.0.1 |      2.6.3       |
| 2021.1                    | Spring Cloud 2020.0.1 |      2.4.2       |

### 2.2.x 分支

适配 Spring Boot 为 2.4，Spring Cloud Hoxton 版本及以下的 Spring Cloud Alibaba 版本如下表（最新版本用 `*` 标记）：

| Spring Cloud Alibaba 版本         |      Spring Cloud 版本      | Spring Boot 版本 |
| --------------------------------- | :-------------------------: | :--------------: |
| 2.2.8.RELEASE\*                    |  Spring Cloud Hoxton.SR12   |  2.3.12.RELEASE  |
| 2.2.7.RELEASE                     |  Spring Cloud Hoxton.SR12   |  2.3.12.RELEASE  |
| 2.2.6.RELEASE                     |   Spring Cloud Hoxton.SR9   |  2.3.2.RELEASE   |
| 2.1.4.RELEASE                     | Spring Cloud Greenwich.SR6  |  2.1.13.RELEASE  |
| 2.2.1.RELEASE                     |   Spring Cloud Hoxton.SR3   |  2.2.5.RELEASE   |
| 2.2.0.RELEASE                     | Spring Cloud Hoxton.RELEASE |  2.2.X.RELEASE   |
| 2.1.2.RELEASE                     |   Spring Cloud Greenwich    |  2.1.X.RELEASE   |
| 2.0.4.RELEASE(停止维护，建议升级) |    Spring Cloud Finchley    |  2.0.X.RELEASE   |
| 1.5.1.RELEASE(停止维护，建议升级) |    Spring Cloud Edgware     |  1.5.X.RELEASE   |

### 组件版本关系

每个 Spring Cloud Alibaba 版本及其自身所适配的 Nacos 组件对应版本如下表所示：

| Spring Cloud Alibaba 版本                                 | 社区版 Nacos 版本 |
| --------------------------------------------------------- | :---------------: |
| 2.2.8.RELEASE                                             |       2.1.0       |
| 2021.0.1.0                                                |       1.4.2       |
| 2.2.7.RELEASE                                             |       2.0.3       |
| 2.2.6.RELEASE                                             |       1.4.2       |
| 2021.1 or 2.2.5.RELEASE or 2.1.4.RELEASE or 2.0.4.RELEASE |       1.4.1       |
| 2.2.3.RELEASE or 2.1.3.RELEASE or 2.0.3.RELEASE           |       1.3.3       |
| 2.2.1.RELEASE or 2.1.2.RELEASE or 2.0.2.RELEASE           |       1.2.1       |
| 2.2.0.RELEASE                                             |       1.1.4       |
| 2.1.1.RELEASE or 2.0.1.RELEASE or 1.5.1.RELEASE           |       1.1.4       |
| 2.1.0.RELEASE or 2.0.0.RELEASE or 1.5.0.RELEASE           |       1.1.1       |



## TSE Nacos 版本兼容性说明

腾讯云 TSE Nacos 完美兼容社区版 Nacos，其中高版本和低版本是完全向下兼容的。例如：开源版本 1.4.2 ，可以在云上选择 2.0.3 版本的 TSE Nacos。

| TSE Nacos 版本 | 可兼容社区版本 | 兼容性 |
| -------------- | -------------- | ------ |
| 2.0.3          | ≤ 2.0.3        | 100%   |





## 客户端兼容性说明

针对 Nacos2.x 服务端：配置中心兼容支持 Nacos1.0 起的所有版本客户端，服务发现兼容 Nacos1.2 起所有版本客户端。 因此建议使用 Nacos 1.2.0 之后版本客户端。 

Nacos1.X 的客户端不具有长连接能力，如果需要使用到此能力建议使用 Nacos2.0.0客户端。



