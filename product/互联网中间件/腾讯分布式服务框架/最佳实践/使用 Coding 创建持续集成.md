# TSF持续集成之 Coding

TSF 应用可以使用 Coding 构建持续集成方案。腾讯云 Coding 持续集成全面兼容 Jenkins 的持续集成服务，更多关于 Coding 持续集成功能和使用的说明，参考 [Coding 持续集成](https://cloud.tencent.com/document/product/1115)。

## CICD 工作流
下图展示了使用 Coding 持续集成，TSF 作为应用部署平台的工作流。

![work_flow](https://main.qcloudimg.com/raw/a545cdd47b51d7c73611d8a8adb5028d/work_flow.png)

## 准备工作

在开始持续集成之前，需要完成下述的准备工作。

1. 参考 [使用Python脚本部署应用]() 获取部署脚本及使用说明。

2. 在 TSF 平台创建了[虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524)或[容器应用部署组](https://cloud.tencent.com/document/product/649/15525)。

3. 获取 TSF 私服地址的 `settings.xml`，请参见 [SDK篇](https://cloud.tencent.com/document/product/649/20231)。  
   
4. 腾讯云主账号已开通 [Coding 平台](https://console.cloud.tencent.com/coding)，并创建 Coding 项目、代码仓库等基础环境。
   
  
## Coding 平台操作
### 一、创建代码仓库并提交代码
1. 登录 Coding 控制台，进入示例项目。
3. 单击左侧导航栏【代码仓库】> 【代码浏览】，单击顶部导航栏，创建代码仓库（如 `provider-demo` 。 
![](https://main.qcloudimg.com/raw/934766be434586df56d2ffc40861bdc7/create-code-repo.png)
3. [下载](https://github.com/tencentyun/tsf-snippet) 演示工程源码，上传到 Coding 的 `provider-demo` 代码仓库中。
![](https://main.qcloudimg.com/raw/a57f805f9ba2be274d3fb94540225e45/coding_code_project.png)   

>**提示**：更多关于如何创建代码仓库，以及如何提交代码的说明请参考 [Coding 代码托管](https://help.coding.net/docs/host/introduce.html)。

>**注意**：用户需要修改示例代码中的 Python 部署脚本，替换其中访问密钥、地域等信息，参考  [使用Python脚本部署应用]()。

### 二、创建构建任务并配置流程
### 2.1 创建构建任务
1. 单击 Coding 控制台左侧导航栏【构建与部署】> 【构建】
2. 单击【新建】
3. 填写新建信息，选择代码仓库 `provider-demo`，使用静态配置的 Jenkinsfile ，选择简易模板。


### 2.2 设置环境变量
1. 单击【变量与缓存】选项卡，输入环境变量：
- PKG_VERSION：程序包/镜像版本号
- TSF_GROUP_ID: TSF 平台的部署组ID
- TSF_APPLICATION_ID: TSF 平台的应用ID
- TSF_APPID: 用户在腾讯云上的 APPID
- TSF_STARTUP_PARAM: Java 应用启动参数，注意**不要**带上引号。

![](https://main.qcloudimg.com/raw/3f974f69630f465e741db590ce759665/coding_add_env.png)

### 2.3 流程配置-构建
1. 在【流程配置】选项卡【图形化编辑器】中，选中【构建】阶段方块。
2. 单击【执行 Shell 脚本】按钮。
![](https://main.qcloudimg.com/raw/b9315d0660ffe2827c76d8168ac4d5c3/coding_execute_shell.png)
3. 编辑【Shell 脚本】，填写 maven package 命令 ，并使用工程中包含 TSF 私服地址的settings.xml。单击【保存】按钮。
   ```shell
   mvn clean package -U --settings settings.xml -Dmaven.test.skip=true
   ```
    ![](https://main.qcloudimg.com/raw/deea50842a4e940720671c920063b51b/coding_modify_shell.png)

### 2.4 流程配置-部署
1. 在【流程配置】选项卡【图形化编辑器】中，选中【部署】阶段方块。
2. 单击【增加步骤】。
3. 单击【执行 Shell 脚本】，输入 Shell 脚本，填写 Python 部署脚本执行命令。
![](https://main.qcloudimg.com/raw/6fb189196aa2ed004d6e28fda67ac94c/coding_add_python_cmd.png)
   i. 虚拟机应用部署脚本命令:   
   ```shell
   python upload_virtual_machine_deploy.py provider-demo/target/provider-demo-0.0.1-SNAPSHOT.jar ${TSF_APPLICATION_ID} ${PKG_VERSION} ${TSF_APPID} ${TSF_GROUP_ID} ${TSF_STARTUP_PARAM}
   ```

   ii. 容器应用部署脚本命令:
   ```shell
   python upload_container_deploy.py group-zvw397wa ${PKG_VERSION}
   ```

## 四、执行构建任务
构建任务可以通过代码提交等方式自动触发，也可以手动执行。
1. 选中目标构建任务，单击【立即构建】。
![](https://main.qcloudimg.com/raw/3fe1b4ad1858a5e2b3786947d6b495c1/coding_start_job.png)
1. 填写环境变量，将【值】替换为用户自己的参数，单击【立即构建】。
![](https://main.qcloudimg.com/raw/ed692037a9621ac9b98d894b89518f5e/coding_start_job2.png)

## 五、验证构建结果
1. 构建任务通常会执行几分钟，查看构建任务的结果
![](https://main.qcloudimg.com/raw/fedbc7ee95028b4c138dec24e6103262/coding_job_result.png)
2. 在 TSF 控制台，查看对应部署组的状态。
![](https://main.qcloudimg.com/raw/80ebd762b69154d8d807330b79566329/tsf_group.png)
