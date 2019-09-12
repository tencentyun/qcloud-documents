## 服务概述
服务是由多个相同配置的容器和访问这些容器的规则所组成。

### 服务类型
服务分为内网服务和外网服务。

**集群内服务**：访问方式不启用的，不绑定外网负载均衡，该服务只能在集群内部访问。

**外网服务**：访问方式选择了公网，自动绑定外网负载均衡，可通过外网负载均衡访问该服务。

**内网服务**：访问方式选择了内网，绑定内网负载均衡，可通过内网负载均衡访问该服务。

### 服务配置
用户在创建时可以自行配置服务，也可通过更新服务的方式来更新配置。

## 使用帮助

- [服务的基本操作](https://cloud.tencent.com/document/product/457/9096)
- [服务的生命周期](https://cloud.tencent.com/document/product/457/9097)
- [服务的访问方式设置](https://cloud.tencent.com/document/product/457/9098)
- [服务的资源限制设置](https://cloud.tencent.com/document/product/457/9099)
- [服务的运行命令和参数设置](https://cloud.tencent.com/document/product/457/9100)
- [服务的健康检查设置](https://cloud.tencent.com/document/product/457/9094)
