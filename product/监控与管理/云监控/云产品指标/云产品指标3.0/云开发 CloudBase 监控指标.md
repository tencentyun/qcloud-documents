## 命名空间

Namespace=QCE/TCB_DOCKER

## 监控指标

| 指标英文名               | 指标中文名                 | 单位 | 维度                                | 统计粒度                             |
| ------------------------ | -------------------------- | ---- | ----------------------------------- | ------------------------------------ |
| VersionCpuUsed           | 版本 CPU 使用量            | MB   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| VersionMemUsed           | 版本内存使用量             | MB   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| VersionMemUsedNoCache    | 版本内存使用量(不含 Cache) | MB   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| VersionPodNum            | 版本 pod 个数              | 个   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| VersionPodUnavailableNum | 版本异常 pod 个数          | 个   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| VersionResourceCpu       | 版本 CPU 规格              | 核   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| VersionResourceMem       | 版本内存规格               | MB   | envid、<br>serviceid、<br>versionid | 60s、<br>300s、<br>3600s、<br>86400s |
| ServiceCpuUsed           | 服务 CPU 使用量            | MB   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| ServiceMemUsed           | 服务内存使用量             | MB   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| ServiceMemUsedNoCache    | 服务不含 Cache 内存使用量  | MB   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| ServicePodNum            | 服务 pod 个数              | 个   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| ServicePodUnavailableNum | 服务异常 pod 个数          | 个   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| ServiceResourceCpu       | 服务 CPU 规格              | 核   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| ServiceResourceMem       | 服务内存规格               | MB   | envid、<br>serviceid                | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvCpuUsed               | 环境 CPU 使用量            | MB   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvMemUsed               | 环境内存使用量             | MB   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvMemUsedNoCache        | 环境不含 Cache 内存使用量  | MB   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvPodNum                | 环境 pod 个数              | 个   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvPodUnavailableNum     | 环境异常 pod 个数          | 个   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvResourceCpu           | 环境 CPU 规格              | MB   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |
| EnvResourceMem           | 环境内存规格               | MB   | envid                               | 60s、<br>300s、<br>3600s、<br>86400s |


## 各维度对应参数总览

| 参数名称                       | 维度名称  | 维度解释          | 格式                                     |
| ------------------------------ | --------- | ----------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | envid     | 环境ID 的维度名称 | 输入 String 类型维度名称：envid          |
| Instances.N.Dimensions.0.Value | envid     | 具体环境 ID       | 输入具体环境 ID ，例如：yourenvid-2fb346 |
| Instances.N.Dimensions.0.Name  | serviceid | 服务号的维度名称  | 输入 String 类型维度名称：serviceid      |
| Instances.N.Dimensions.0.Value | serviceid | 具体服务号        | 输入具体服务号 ，例如：3                 |
| Instances.N.Dimensions.0.Name  | versionid | 版本号的维度名称  | 输入 String 类型维度名称：versionid      |
| Instances.N.Dimensions.0.Value | versionid | 具体版本 ID       | 输入具体版本 ID ，例如：1.11             |


## 入参说明


#### 查询云开发 CloudBase -版本数据，入参取值如下：

&Namespace=QCE/TCB_DOCKER
&Instances.N.Dimensions.0.Name=envid   
&Instances.N.Dimensions.0.Value=具体环境 ID 
&Instances.N.Dimensions.1.Name=versionid   
&Instances.N.Dimensions.1.Value= 具体版本号

#### 查询云开发 CloudBase -服务数据，入参取值如下：
&Namespace=QCE/TCB_DOCKER
&Instances.N.Dimensions.0.Name=envid   
&Instances.N.Dimensions.0.Value=具体环境 ID 
&Instances.N.Dimensions.1.Name=serviceid   
&Instances.N.Dimensions.1.Value= 具体服务号

#### 查询云开发 CloudBase -环境数据，入参取值如下：
&Namespace=QCE/TCB_DOCKER
&Instances.N.Dimensions.0.Name=envid   
&Instances.N.Dimensions.0.Value=具体环境 ID
