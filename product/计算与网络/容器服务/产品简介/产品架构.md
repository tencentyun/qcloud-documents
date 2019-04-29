### 总体架构
本节介绍容器服务系统的设计和实现，产品架构如下图所示：
![Alt text][Architecture]

### 架构说明
1.  腾讯云容器服务基于原生Kubernetes进行适配和增加， 支持原生Kubernetes能力
2.  提供了腾讯云的kubernetes插件，帮助用户快速在腾讯云上构建Kubernetes集群
3.  腾讯云容器服务在kubernetes上层,提供了集群管理、应用管理、CI/CD等进阶能力

### 模块说明
1. **容器服务控制台和云API**：用户通过控制台或云API操作集群与服务。
2. **镜像服务CCR模块**：腾讯云提供的镜像服务模块，用户可以上传镜像，或将镜像下载到本地。
3. **容器服务TKE模块**：容器服务核心模块，包括集群的增删改查、服务的增删改查等。
4. **OSS和BSS**: 腾讯云提供的运维管理平台和计费管理平台。

[Architecture]:https://main.qcloudimg.com/raw/599ac1bdd73c895ba7ca6a23dc55790a.jpg