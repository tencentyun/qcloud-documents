
## 适用场景

将业务应用从自建 Nacos 冷迁到 TSE Nacos，在迁移过程中，新部署的业务应用不提供服务

## 迁移步骤

### 步骤一：配置数据迁移（若有）

将配置数据迁移到 TSE Nacos
步骤1：将原有配置从nacos导出
![image](https://user-images.githubusercontent.com/14815194/173516008-618513c6-05ac-41a7-bc37-cdb45d937c6f.png)
步骤2：将导出的配置导入到TSE Nacos
![image](https://user-images.githubusercontent.com/14815194/173516580-52f8729d-4db4-4f4a-9165-dd2f771b870a.png)
步骤3：依次将所有命令空间按照1、2步骤进行导出导入操作即可。

### 步骤二：新部署的业务应用接入

新部署的业务应用接入 TSE Nacos，暂时不对外提供服务

### 步骤三：新部署的业务应用上线

验证新部署的业务应用运行正常

将请求切换到新部署的业务应用

下线存量的业务应用
