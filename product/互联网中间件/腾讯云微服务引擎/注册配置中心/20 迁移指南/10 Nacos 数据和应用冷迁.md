
## 适用场景

将业务应用从自建 Nacos 冷迁到 TSE Nacos，在迁移过程中，新部署的服务暂不可用，存量服务不受影响。
## 迁移步骤

### 步骤1：配置数据迁移（若有）

将配置数据迁移到 TSE Nacos。
1. 将原有配置从 nacos 导出。
![](https://qcloudimg.tencent-cloud.cn/raw/60ff3dd695628774334350eb3c42f600.png)
2. 将导出的配置导入到 TSE Nacos。
![](https://qcloudimg.tencent-cloud.cn/raw/9ed695d5a4de86a359f8c58e44cf7e46.png)
3. 依次将所有命令空间按照1、2步骤进行导出导入操作即可。

### 步骤2：新部署的业务应用接入

新部署的业务应用接入 TSE Nacos，暂时不对外提供服务。

### 步骤3：新部署的业务应用上线

1. 验证新部署的业务应用运行正常。
2. 将请求切换到新部署的业务应用。
3. 下线存量的业务应用。
