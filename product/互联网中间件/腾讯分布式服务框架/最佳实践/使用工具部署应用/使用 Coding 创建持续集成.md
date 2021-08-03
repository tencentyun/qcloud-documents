## 操作场景
TSF 应用可以使用 CODING 构建持续集成方案。腾讯云 CODING 持续集成全面兼容 Jenkins 的持续集成服务，更多关于 CODING 持续集成功能和使用的说明，请参考 [CODING 持续集成](https://cloud.tencent.com/document/product/1115)。

#### CODING DevOps 工作流
下图展示了使用 CODING 持续集成，TSF 作为应用部署平台的工作流。
![work_flow](https://main.qcloudimg.com/raw/a545cdd47b51d7c73611d8a8adb5028d/work_flow.png)

## 准备工作

在开始持续集成之前，需要完成下述的准备工作：
1. 参考 [使用 Python 脚本部署应用](https://cloud.tencent.com/document/product/649/40407) 获取部署脚本及使用说明。
2. 在 TSF 平台创建了 [虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524) 或 [容器应用部署组](https://cloud.tencent.com/document/product/649/15525)。
3. 获取 TSF 私服地址，详情请参见 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)。  
4. 腾讯云主账号已开通 [CODING DevOps](https://console.cloud.tencent.com/coding)，并创建 CODING 项目、代码仓库等基础环境。
   

## CODING 平台操作
### 步骤一：创建代码仓库并提交代码
1. 登录 [CODING DevOps 控制台](https://console.cloud.tencent.com/coding)，进入示例项目。
2. 单击左侧导航栏【代码仓库】> 【代码浏览】，单击顶部导航栏，创建代码仓库（如 `provider-demo`）。
![](https://main.qcloudimg.com/raw/6080d4953c1c88265aed6021406e22c8.png)
3. [下载](https://github.com/tencentyun/tsf-snippet) 演示工程源码，上传到 Coding 的 `provider-demo` 代码仓库中。
  ![](https://main.qcloudimg.com/raw/be8ddefc4dd61b61569d2317789937a2.png)

更多关于如何创建代码仓库，以及如何提交代码的说明请参考 [CODING 代码托管](https://help.coding.net/docs/host/introduce.html)。
>!用户需要修改示例代码中的 Python 部署脚本，替换其中访问密钥、地域等信息，参考  [使用 Python 脚本部署应用](https://cloud.tencent.com/document/product/649/40407)。


### 步骤二：创建并配置构建任务
#### 创建构建任务
1. 单击 Coding 控制台左侧导航栏【构建与部署】>【构建】。
2. 单击【新建】。
3. 填写新建信息，选择代码仓库 `provider-demo`，使用静态配置的 Jenkinsfile ，选择简易模板。

#### 设置环境变量
单击【变量与缓存】选项卡，输入环境变量：
- PKG_VERSION：程序包/镜像版本号
- TSF_GROUP_ID: TSF 平台的部署组 ID
- TSF_APPLICATION_ID：TSF 平台的应用 ID （仅适用于虚拟机应用部署）
- TSF_APPID：用户在腾讯云上的 APPID （仅适用于虚拟机应用部署）
- TSF_STARTUP_PARAM：Java 应用启动参数，注意**不要**带上引号（仅适用于虚拟机应用部署）

![](https://main.qcloudimg.com/raw/6da8b6410f846bcb8f1446804d921934.png)


#### 流程配置-构建
1. 在【流程配置】选项卡【图形化编辑器】中，选中【构建】阶段方块。
2. 单击【执行 Shell 脚本】。
![](https://main.qcloudimg.com/raw/ac1f0d9b8f197354e408d4d7cf433a48.png)
3. 编辑【Shell 脚本】，填写 maven package 命令 ，并使用工程中包含 TSF 私服地址的settings.xml。单击【保存】。
   ```shell
   mvn clean package -U --settings settings.xml -Dmaven.test.skip=true
   ```
   ![](https://main.qcloudimg.com/raw/98ec1c08723c5ccd12d2c9e345904896.png)

#### 流程配置-部署
1. 在【流程配置】选项卡【图形化编辑器】中，选中【部署】阶段方块。
2. 单击【增加步骤】。
3. 单击【执行 Shell 脚本】，输入 Shell 脚本，填写 Python 部署脚本执行命令。

![](https://main.qcloudimg.com/raw/6fb189196aa2ed004d6e28fda67ac94c/coding_add_python_cmd.png)
   a. 虚拟机应用部署脚本命令：  
   ```shell
   python upload_virtual_machine_deploy.py provider-demo/target/provider-demo-0.0.1-SNAPSHOT.jar ${TSF_APPLICATION_ID} ${PKG_VERSION} ${TSF_APPID} ${TSF_GROUP_ID} ${TSF_STARTUP_PARAM}
   ```

b. 容器应用部署脚本命令：
   ```shell
   python upload_container_deploy.py ${TSF_GROUP_ID} ${PKG_VERSION}
   ```

### 步骤三：执行构建任务
构建任务可以通过代码提交等方式自动触发，也可以手动执行。
1. 选中目标构建任务，单击【立即构建】。
![](https://main.qcloudimg.com/raw/0a41295d27d259f199783b3d4e6e5193.png)
2. 填写环境变量，将【值】替换为用户自己的参数，单击【立即构建】。
![](https://main.qcloudimg.com/raw/2a9433eb86bc6045d244d62e022fda00.png)

### 步骤四：验证构建结果
1. 构建任务通常会执行几分钟，查看构建任务的结果。
![](https://main.qcloudimg.com/raw/67b86412646260fa93cce10b40343893.png)
2. 在 TSF 控制台，查看对应部署组的状态。
![](https://main.qcloudimg.com/raw/04a6b482ee4a031b0a688859a9eacfdf.png)

