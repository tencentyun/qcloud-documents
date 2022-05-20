## 调整详情
腾讯云 TI 平台 TI-ONE【重庆】地域将于2019年12月31日无法新增任务，于2020年3月31日正式下线。为避免造成数据的丢失，请您在下线前将重要数据迁移至广州地域。具体迁移方法请参考以下**迁移指南**。       
<table>
     <tr>
         <th colspan="2" align="center">重庆地域下线功能模块</th>  
     </tr>
  <tr>      
         <td rowspan="3">工程列表</td>   
      <td>新建工程</td>   
     </tr> 
  <tr>
 <td>新建工作流</td> 
     </tr> 
  <tr>      
			<td>运行已有的工作流</td>   
     </tr> 
		   <tr>      
         <td rowspan="3">Notebook</td>   
      <td>新增容器</td>   
     </tr> 
  <tr>
 <td>打开运行中的容器</td> 
     </tr> 
  <tr>      
			<td>启动已终止的容器</td>   
     </tr> 
<tr>      
       <td rowspan="2">模型仓库</td>   
      <td>部署模型</td>   
     </tr> 
  <tr>
 <td>离线批量预测</td> 
     </tr> 
		<td rowspan="4">模型服务-在线服务</td>   
      <td>获取模型访问地址及密钥</td>   
     </tr> 
  <tr>
 <td>测试</td> 
     </tr> 
  <tr>      
			<td>升级/回退</td>   
     </tr>  
<tr>      
			<td>负载均衡</td>   
     </tr> 
</table>

## 迁移指南
### 数据迁移
对象存储 COS 为腾讯云的分布式存储服务，将会应用于腾讯云 TI 平台 TI-ONE 中的各个环节，包括训练数据、中间结果数据和模型文件的存放与读取等。
- **迁移准备**
首先，您需要创建**【广州】**地区存储桶。操作详见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
- **批量迁移**
 - 如果您的文件较多，您可以使用 COS 的 [设置跨地区复制](<https://cloud.tencent.com/document/product/436/19235>) 功能进行操作。
 - 设置跨地域复制功能时，目标存储桶选择**广州**地区的存储桶。
 - 启用跨地域复制后，COS 将精确复制源存储桶中的对象内容（如对象元数据和版本 ID 等）到目标存储桶中，复制的对象副本拥有完全一致的属性信息。此外，源存储桶中对于对象的操作，如添加对象、删除对象等操作，也将被复制到目标存储桶中。
- **少量数据迁移**
您可以选中想要迁移的目标文件，在更多操作中单击**复制**，再到**广州**地区的目标路径，单击更多操作中的**粘贴**即可。具体操作说明详见 [复制对象](https://cloud.tencent.com/document/product/436/39849)。
- **数据销毁**
在迁移完成后，您可以通过 [清空存储桶](https://cloud.tencent.com/document/product/436/35247) 和 [删除存储桶](https://cloud.tencent.com/document/product/436/32433) 操作对**重庆**地区的 COS 数据进行销毁。

### 工作流迁移
- **工作流**
您在【重庆】地域搭建的工作流，在【广州】地域不再可用。您需要在【广州】地域重新搭建。工作流的创建请参考 [新建工程与工作流](https://cloud.tencent.com/document/product/851/19069)。
- **脚本与数据**
【重庆】地域工作流内的资源（脚本、jar包、本地数据等），在【广州】地域不再可用。您需要自行下载，在【广州】地域重新上传。


### Notebook 迁移
- **Notebook 实例**
您在【重庆】地域创建的 Notebook 实例，在【广州】地域不再可用。您需要手动停止 Notebook 实例，并在【广州】地域重新创建。
- **`/cos_person`目录下的文件**
【重庆】地域 Notebook 中的`/cos_person`目录下的所有文件均自动保存在您创建 Notebook 时选择的 COS 存储桶中，文件不被销毁。您可以从 COS 下载文件到本地，也可参照上文 **COS 迁移**进行迁移，在【广州】地域重新上传使用。
- **其他文件**
【重庆】地域 Notebook 中其他目录下的个人文件在地域下线后会自动销毁，您可以自行下载，在【广州】地域重新上传。

### 库表迁移
- **迁移准备**
库表的数据依赖 COS，在做库表迁移前，您要先完成 **COS 迁移**。库表的使用和之前保持一致。
- **库迁移**
对于【重庆】地域已有的库，您需要在【广州】地域重新创建对应的库，填写的信息和之前保持一致。
- **表迁移**
对于【重庆】地域已有的表，您需要在【广州】地域重新创建对应的表。
**COS 存储桶**，**文件路径**填写您在【广州】地域的相关 Bucket 与路径，其他信息和之前保持一致。

  
### 模型服务迁移
- **在 TI-ONE 获取模型文件夹的 COS 地址** 
用户可以通过 【TensorFlow 控制台】>【App 详情】或者【Spark控制台】的日志里找到模型文件的 COS 路径，例如 `model_dir:/cephfs/tesla_common/deeplearning/model/100010875047/285382/`
- **登录 TI-EMS**
[单击登录](https://console.cloud.tencent.com/tiems) TI-EMS 控制台。
- **用户对 TI-EMS 的授权**
用户初次使用 TI-EMS 服务需要额外进行服务角色授权，如果您使用的是子账号，还需要主账户对子账号进行额外授权，操作详情见 [TI-EMS 文档](https://cloud.tencent.com/document/product/1120/38967) 。
- **用户使用 TI-EMS 创建模型服务配置**
TI-EMS 模型服务除了支持 TI-ONE 原有的 TensorFlow 、 PMML 和 ANGEL 外，还支持 TensorRT，OpenVINO 等框架，提供专业级的模型部署服务，只需要将 TI-ONE 中生成模型的 COS 地址，转换为 TI-EMS 支持的模型路径地址便可创建 TI-EMS 服务配置，操作详情见 [TI-EMS 文档](https://cloud.tencent.com/document/product/1120/36585)。

模型地址转换示例如下：
-  tione 模型文件的 COS 路径：`/cephfs/tesla_common/deeplearning/model/100010875047/285382/`
-  对应的 TI-EMS 模型文件 cos 路径：`cos://haoyuanpeng-1256975134.cos.ap-guangzhou.myqcloud.com/cephfs/tesla_common/deeplearning/model/100010875047/285382/`（TI-EMS 模型 COS 文件路径规范：`cos://${bucket_name}-${appid}.cos.{region}.myqcloud.com/模型文件夹路径/`，其中 COS 访问域名查看方法请详见 [文档](https://cloud.tencent.com/document/product/436/6224)）。

>!目前 TI-EMS 只支持北京、上海、广州地域的服务，如果您的工作流绑定的 Bucket 是其他地域的，请先将模型上传至北上广地域的 COS 中。

- **用户使用 TI-EMS 启动模型服务**
目前 TI-EMS 支持模型部署至公共资源组和专用资源组，预付费购买专用资源组已经开放使用，公共资源组按量计费暂未开放，可申请白名单进行试用，资源组使用方式请详见 [TI-EMS 文档](https://cloud.tencent.com/document/product/1120/38968)。
- **用户使用 TI-EMS 服务调用**
TI-EMS 模型部署后提供公网地址和 vpc 地址访问，用户可以在您的本地或生产环境中进行 API 调用。服务调用案例详情请见 [TI-EMS 文档](https://cloud.tencent.com/document/product/1120/36610)。
- **用户使用 TI-EMS 的计费说明**
TI-EMS 目前支持预付费的计费方式，支持 CPU 和 GPU 的包月服务，计费详情请见 [TI-EMS 文档]( https://cloud.tencent.com/document/product/1120/38717)。
- **其他关于 TI-EMS 的使用方法请参考  [TI-EMS 产品文档](https://cloud.tencent.com/document/product/1120)**
TI-ONE 未来会整合云上各种资源，后续将推出一键部署到 TI-EMS 等功能，尽情期待。


