## 操作场景
当前容器镜像服务 TCR 同时提供个人版服务和企业版服务。个人版服务面向个人开发者，仅提供容器镜像存储分发的基础功能。企业版服务可为企业客户提供安全、独享的高性能云原生应用制品托管分发服务。个人版与企业版服务区别可参见 [规格说明](https://cloud.tencent.com/document/product/1141/40540#.E8.A7.84.E6.A0.BC.E8.AF.B4.E6.98.8E)。

部分正在使用个人版服务的客户，出于保障业务依赖的容器镜像的数据安全及可用性、提高容器镜像在多地域内加速分发等需要，需要将服务切换至企业版。

本文主要介绍企业客户如何将容器镜像及相关依赖配置从个人版迁移至企业版。


## 前提条件
从个人版服务迁移至企业版，您需要确认并完成以下准备工作：
- 已开通并使用个人版服务，且迁移操作账号具有拉取个人版镜像仓库内所有镜像的权限，请参考 [个人版授权方案示例](https://cloud.tencent.com/document/product/1141/41409) 提前为子账号授予个人版的全部管理权限。
- 已 [购买企业版实例](https://cloud.tencent.com/document/product/1141/51110)，且迁移操作账号具有向该企业版实例内推送镜像的权限，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的容器镜像、Helm Chart 推送权限，建议将容器镜像服务全读写权限授予配置同步的子账号。
- 已设置迁移工具运行的运行环境。建议在私有网络 VPC 内执行该迁移任务，以提升迁移速度，并避免公网流量成本。
  - 在私有网络 VPC 内运行迁移工具：在目标企业版实例的内网访问中添加迁移工具运行服务器所在的私有网络。详情可参见 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)。
  - 在公网环境内运行迁移工具：开启目标企业版实例的公网访问入口，并放通访问来源。详情可参见 [公网访问控制](https://cloud.tencent.com/document/product/1141/41837)。

## 操作步骤
### 下载并安装迁移工具
执行如下命令，下载并安装迁移工具：
```
wget https://github.com/tkestack/image-transfer/releases/download/v1.0.0/image-transfer-linux-amd64.tar.gz
tar -xzvf image-transfer-linux-amd64.tar.gz
cd image-transfer
```


### 初始化迁移工具配置
1. 配置镜像仓库鉴权配置文件 security.yaml，即配置源仓库及目标仓库的用户名及密码，允许迁移工具登录镜像仓库，批量拉取、推送镜像。
```
tcr-enterprise-demo.tencentcloudcr.com:
        username: xxx
        password: xxx
ccr.ccs.tencentyun.com:
        username: xxx
        password: xxx
```
   - **企业版**：支持临时访问凭证及长期访问凭证，请登录【容器镜像服务控制台】>【[实例列表](https://console.cloud.tencent.com/tcr/instance?rid=1)】，并选择已经提前创建好的企业版实例。在实例详情页，新建一个镜像迁移专用的访问凭证。详情可参见 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829)。  
   - **个人版**：仅支持固定密码，在您初始化该服务时设置了此密码。如忘记密码，可在【容器服务控制台】>【镜像仓库】>【[个人版](https://console.cloud.tencent.com/tke2/registry/user?rid=1)】中选择【重置密码】，并在弹出的“重置密码”窗口中确认用户名后重新设置密码。
2. 配置腾讯云鉴权配置文件 secret.yaml。参考以下代码，配置腾讯云的 SecretId、SecretKey，允许迁移工具调用 TCR 相关云 API，获取镜像列表及基础信息。
```
tcr:
        secretId: xxx
        secretKey: xxx
ccr:
        secretId: xxx
        secretKey: xxx
```
其中，tcr 代表企业版，ccr 代表个人版，共用一对腾讯云 secretId，secretKey。您可在【访问管理】>【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】中查看您的腾讯云 API 密钥。

### 运行迁移工具
在迁移工具的安装文件夹内执行以下命令：
```
./image-transfer --ccrToTcr=true --routines=5 --securityFile=./security.yaml --secretFile=./secret.yaml --tcrName=tcr-enterprise-demo --retry=3 --tcrRegion=ap-guangzhou --ccrRegion=ap-guangzhou --qps=3000
```

| 参数 | 参数说明 | 
|---------|---------|
| ccrToTcr=true | 表示开启 TCR 一键全量迁移模式，此模式下迁移工具将全量迁移个人版内所有镜像至指定的企业版实例。 | 
| securityFile | 指定 security.yaml 配置文件。 | 
| secretFile | 指定 secret.yaml 配置文件。 | 
| tcrName | 指定目标企业版实例的名称。 | 
| tcrRegion | 指定目标企业版实例所在的地域。 | 
| ccrRegion | 指定源个人版仓库所在的地域，默认与目标企业版实例所在地域一致。 | 





### 查看运行结果
因个人版迁移至企业版默认使用全量迁移模式，迁移时间直接与当前个人版内镜像仓库数量及大小有关，请耐心等待。
若运行后展示如下代码，即表示全量迁移成功。否则请重新运行该迁移工具进行重试。
```
################# Finished, 0 transfer jobs failed, 0 jobs generate failed #################
```

