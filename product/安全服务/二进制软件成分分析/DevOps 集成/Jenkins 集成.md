本文介绍如何使用二进制软件成分分析（Binary Software Composition Analysis, BSCA）的 Jenkins 插件。您可以在 Jenkins 构建任务中集成该插件，对制品进行自动上传和分析。

## 步骤1：下载插件 
访问 [BSCA Jenkins Plugin](https://bsca-production-1251316161.cos.ap-guangzhou.myqcloud.com/jenkins-plugin/BSCAJenkins.hpi) 下载插件。 

## 步骤2：发布插件 
1. 登录 Jenkins 系统，进入**系统管理** > **插件管理** > **高级** > **Deploy Plugin**，在**选择文件**中选择下载的插件，并单击 **Deploy**。
![安装插件.png](https://qcloudimg.tencent-cloud.cn/raw/478cdf4f07a00e8c690a78222ee96581.png) 
2. 此时插件正在安装。等待片刻后，若提示安装完成，则单击**返回首页**即可。若提示需要重启，请重启 Jenkins 以确保安装生效。
 ![安装完成.png](https://qcloudimg.tencent-cloud.cn/raw/c1c8ad3d38229e9ba85817a38884ef13.png) 
3. 插件安装完成之后，可在已安装栏目中看到“BSCA Jenkins Plugin”。
 ![已安装.png](https://qcloudimg.tencent-cloud.cn/raw/28a56be3576cf26eb163355268a8a981.png)

## 步骤3：使用插件 
1. 在构建任务中，单击**配置 > 构建 > 增加构建步骤**，选择“BSCA Jenkins Plugin”。
 ![添加插件.png](https://qcloudimg.tencent-cloud.cn/raw/41f4b807da61e7b6da820bf94745d6c5.png) 
2. 在对话框中，填写参数，示例如下：
 ![插件参数.png](https://qcloudimg.tencent-cloud.cn/raw/ca0bc6fbf4f07c261b0f33da016bcc20.png) 
**参数说明：**
 - SecretId：腾讯云 API SecretId，用于标识 API 调用者的身份，可在腾讯云平台的**访问管理** > **访问密钥** > **[API 密钥管理](https://console.cloud.tencent.com/cam/capi)** 中获取。**建议配置环境变量并加密，防止 SecretId 泄露**。 
 - SecretKey：腾讯云 API SecretKey，用于加密和验证签名字符串，可在腾讯云平台的**访问管理** > **访问密钥** > **[API 密钥管理](https://console.cloud.tencent.com/cam/capi)** 中获取。**建议配置环境变量并加密，防止 SecretKey 泄露。** 
 - 文件路径：待分析文件所在路径，示例：`/bin/echo` 。 
 -  分析名称：创建分析的名称。 
 -  分析项类型：创建分析的类型，与文件类型直接相关。目前支持 RTOS 固件、Docker 镜像、其他制品文件（各类二进制构建产物），默认为“其他制品文件”。
 - 分析参数：分析项参数，目前**仅 RTOS 固件类型**的分析需要，包括 bin、s19、hex。 
3. 参数填写完成后，单击**立即构建**运行构建任务。
4. 任务结束后可前往 [二进制软件成分分析控制台](https://console.cloud.tencent.com/bsca/sca/index) 查看插件创建的分析。
 ![示例分析](https://qcloudimg.tencent-cloud.cn/raw/16f6e5cd83992900b1a478d2c5dc3acd.png)
