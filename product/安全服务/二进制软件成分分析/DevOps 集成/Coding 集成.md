本文介绍如何使用二进制软件成分分析（Binary Software Composition Analysis, BSCA）的 Coding 构建插件。您可以在 Coding 平台的构建计划中集成该插件，对制品进行自动上传和分析。 


## 步骤1：下载插件 
访问 [BSCA Coding Plugin](https://bsca-production-1251316161.cos.ap-guangzhou.myqcloud.com/coding-plugin/BSCACoding.zip) 下载插件压缩包。 

## 步骤2：发布插件 
1. 登录 [Coding 平台](https://coding.net/)，进入**团队设置中心** > **功能设置** > **持续集成** > **构建插件**。
![构建插件入口](https://qcloudimg.tencent-cloud.cn/raw/06b69b9f9d6342d470e4d563c06c4e41.png)
2. 单击右上角**新建构建插件**。
 ![新建构建插件.png](https://qcloudimg.tencent-cloud.cn/raw/be38579ab27abfcde8ef248928833726.png) 
3. 在**选择文件**中选择下载的压缩包，单击**发布插件**。 
![发布插件.png](https://qcloudimg.tencent-cloud.cn/raw/c3b897d456523ef69f4a11c19bf42c75.png) 
4. 发布完成后，可在团队插件中看到“二进制软件成分分析”。
![团队内插件.png](https://qcloudimg.tencent-cloud.cn/raw/d853aa3cab5f520b87d22dd84bc50eb7.png)


## 步骤3：使用插件
1. 在构建计划中新增阶段，选择**安全** > **二进制软件成分分析**。
 ![构建计划选择插件.png](https://qcloudimg.tencent-cloud.cn/raw/a036f5eb3701da073cfb59de1d1d62e7.png)	 
2. 在对话框中，填写参数，示例如下：
 ![插件参数.png](https://qcloudimg.tencent-cloud.cn/raw/3795bc5d7ac6c8f382d87e90fd9cf5c7.png) 
**参数说明**： 
 - SecretId：腾讯云 API SecretId，用于标识 API 调用者的身份，可在腾讯云平台的**访问管理** > **访问密钥** > **[API 密钥管理](https://console.cloud.tencent.com/cam/capi)** 中获取。**建议配置环境变量并加密，防止 SecretId 泄露**。 
 - SecretKey：腾讯云 API SecretKey，用于加密和验证签名字符串，可在腾讯云平台的**访问管理** > **访问密钥** > **[API 密钥管理](https://console.cloud.tencent.com/cam/capi)** 中获取。**建议配置环境变量并加密，防止 SecretKey 泄露。** 
 - 文件路径：待分析文件所在路径，示例：`/bin/echo` 。 
 -  分析名称：创建分析的名称。 
 -  分析项类型：创建分析的类型，与文件类型直接相关。目前支持 RTOS 固件、Docker 镜像、其他制品文件（各类二进制构建产物），默认为“其他制品文件”。
 - 分析参数：分析项参数，目前**仅 RTOS 固件类型**的分析需要，包括 bin、s19、hex。 
3. 参数填写完成之后单击**保存**并**立即构建**，即可运行流水线。
4. 运行结束之后可前往 [二进制软件成分分析控制台](https://console.cloud.tencent.com/bsca/sca/index) 查看插件创建的分析。
![示例分析.png](https://qcloudimg.tencent-cloud.cn/raw/a583fdf6eeb8726c0c4bbe80b9e31271.png)
