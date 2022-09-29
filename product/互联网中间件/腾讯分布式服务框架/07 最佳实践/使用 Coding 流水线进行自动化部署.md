
## 操作场景

TSF 应用可以使用 CODING 流水线进行部署，通过流水线及插件一键创建应用、上传文件、创建部署组、导入服务器、部署应用。

## 前提条件

- 已创建好集群并导入云主机，容器部署场景请参见 [快速创建一个容器集群](https://cloud.tencent.com/document/product/649/55505)，虚拟机部署场景请参见 [快速创建一个虚拟机集群](https://cloud.tencent.com/document/product/649/55498)。
- 腾讯云主账号已开通 [CODING DevOps](https://console.cloud.tencent.com/coding)，并创建好 CODING 项目、代码仓库和提交代码。
  

## 操作步骤

### 步骤1：构建流水线

1. 登录 [CODING 控制台](https://tencent.coding.woa.com/)，进入示例项目。
2. 在左侧导航栏选择**持续集成** > **流水线**，单击右上角的**新建流水线**。
3. 选择**自定义构建流程** ，填写流水线相关信息。
- 代码库：代码库列表数据来源于当前项目已登记的代码库。选择应用代码存放的仓库地址。
- 认证：用于代码库 webhook 触发构建、拉取代码、读取 YAML 文件等的权限认证。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/4f90cce09a4628410ffc631745707f67.png" style = "width:60%"> 
4. 单击**完成创建**，在流水线编辑页面点击**上传配置文件**并**保存**，通过 yaml 配置文件的方式构建完整流水线。
配置文件下载地址：
- [虚拟机部署场景](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/coding/create_group_vm.yaml)
- [容器部署场景](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/coding/create_group_container.yaml)
![](https://qcloudimg.tencent-cloud.cn/raw/766b991bc2bb712e06d4fe62e64cafb3.png) 

### 步骤2：运行流水线

1. 在流水线编辑页面点击右上角**触发**，填写启动参数。
	- TSF_CLUSTER_NAME：填写提前创建好的集群的名称
	- TSF_NAMESPACE_NAME：填写提前创建好的命名空间的名称。
	- TSF_APPLICATION_NAME：自定义填写应用名称。
	- TSF_GROUP_NAME：自定义填写部署组名称。
	- INSTANCE_ID_LIST：云主机的 ID，格式为["ins-xxxx1"undefined"ins-xxxx2"]。
	- TSF_ENV：选择 tsf_public
	- SECRET_ID、SECRET_KEY：云 API 密钥，在访问管理控制台中的 **访问密钥** > **API 密钥管理**获取。
![](https://qcloudimg.tencent-cloud.cn/raw/2c2577871a2eb9c16c9988211bf83ad8.png)
	- ACCOUNT_APPID：API 密钥管理中的的APPID
	- REGION：在下拉选项中选取对应ap开头的可用区。
2. 填写完成后，开始执行构建任务。

### 步骤3：验证构建结果

1. 构建任务通常会执行几分钟，查看构建任务的结果。
![](https://qcloudimg.tencent-cloud.cn/raw/67e5184c21a378522b8f34cf067094cf.png)
2. 在 TSF 控制台，查看对应部署组的状态。
![](https://qcloudimg.tencent-cloud.cn/raw/482d2af2697a93da455f8f9a276afeb0.png) 

### 编辑插件

单击**编辑**，再点击具体某个阶段可以在该面板中配置一些非必传的参数。

![](https://qcloudimg.tencent-cloud.cn/raw/23ff62e3fbf512fbdc66f123c5d5dc29.png)

在该位置单击查看完整介绍可以看到插件的完整参数描述。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/090ea639a81f4cd96ad9af3cacc070e3.png" style = "width:60%"> 


插件完整描述：
![](https://qcloudimg.tencent-cloud.cn/raw/31efb5323ce42d157bc7e6dd0c45a061.png)

### 添加流水线插件

在使用 yaml 文件构建好流水线后还可以在页面中通过 UI 编辑的方式添加之外的插件。

例如在创建应用后需添加配置，就可在点击下图所示的“+”，在搜索栏中查询“TSF(general)”就可查到 TSF 自动化部署的插件，在选取对应的“创建配置项”插件。

![](https://qcloudimg.tencent-cloud.cn/raw/99f65f1a483a012385719df7d149a546.png)

插件添加完成后在该阶段会多出一个版块，单击该版块，填入具体信息即可使用该插件

![](https://qcloudimg.tencent-cloud.cn/raw/400ec38a82677553da65bb1d0bc36951.png)
