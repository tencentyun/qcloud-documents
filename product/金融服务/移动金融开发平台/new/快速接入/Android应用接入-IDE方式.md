# Android应用接入-IDE方式

## 1、软件安装

### 前提条件

1. 您已安装Android Studio 4.0及以上版本

2. 您已经获得了IDE插件的安装包，安装包名称为 TMF-AS-plugin-x.x.zip

   >![说明](/Users/pekinglin/Code/tmf/TMF_MD/03开发指南/接入Android/接入指南/images/说明.png)说明：下载IDE插件请点击：[开发者工具](https://tmf-warehouse-1257849200.cos.ap-beijing.myqcloud.com/tmf/ide/TMF-AS-plugin.zip)，插件安装包为压缩包文件形式，在安装前无需解压。

### 操作步骤

1. 在 Android Studio 中，通过 **Android Studio** > **Preference**打开设置对话框。
2. 在页面左侧，单击 **Plugins**，然后在右上方单击 <img src="../img/设置按钮.jpg" width="30"> ，并在下拉菜单中单击 **Install Plugin from Disk**。  
   ![image-20210820150801866](../img/软件安装01.png)
3. 选择您已经下载的 TMF 插件安装包，单击**Open**。
4. 安装完成后，单击**Restart IDE**，重启 Android Studio，您即可开始使用 TMF 插件。



## 2、新建工程

1. 登录控制台，下载应用配置文件(tmf-android-configurations.json)。

2. 在 Android Studio 欢迎页面，单击**Start a New TMF Project**，创建项目。   
   ![img](../img/创建项目.png)

   >![说明](/Users/pekinglin/Code/tmf/TMF_MD/03开发指南/接入Android/接入指南/images/说明.png)说明：您也可以通过单击**File** > **New** > **Start a New TMF Project**，创建项目。

3. 返回Android Studio创建TMF项目页面，配置项目参数，填写项目名称、包名，并选择编程语言、存储位置和控制台下载的应用配置文件（JSON）路径，单击**Next**。

   ![截屏2022-03-31 14.08.11](../img/配置项目参数2.png)

**字段说明**：

- Name: 项目名称。
- Package Name: 应用包名，**需与控制台配置的包名一致，否则运行时校验无法通过**。
- Language: 开发语言选择。
- Save location: 项目存储路径。
- ConfigFile location: 应用配置文件（tmf-android-configuratsion.json）路径。

4. 选择产品基线与依赖组件，单击**Finish**，结束向导。

   ![截屏2022-04-02 17.36.44](../img/选择基线.png)

5. 创建完成，开始编码。



## 3、已有工程

1. 登录控制台，下载应用配置文件(tmf-android-configurations.json)。

2. 在编码界面右侧侧边栏单击**TMF**，打开TMF助手。
   ![截屏2022-04-06 10.32.51](../img/TMF助手.png)

3. 单击**点击转换**，即可将现有的非TMF工程转换为TMF工程，此操作会在gradle中配置maven信息，以及在工程目录下生成 .tmf.config.json文件并添加基线配置。

   ```groovy
   build.gradle:
   buildscript {
      repositories {
      maven {
         url 'https://t.pinpad.qq.com/fHKFBbEjd/repository/mavenpublic/'
         credentials {
            username ''
            password ''
      }
   }
   
   .tmf.config.json:
   {
      "baseLine":"tmf-android-baseline-1.0#1.7.1"
   }
   ```

   > ![说明](/Users/pekinglin/Code/tmf/TMF_MD/03开发指南/接入Android/接入指南/images/说明.png)说明：仓库用户名和密码请向管理员获取。

4. 将下载的配置文件(tmf-android-configurations.json)拷贝至assets目录。

![config](../img/配置文件位置.png)

5. 校验项目包名是否与配置文件中包名一致，如果不一致需要将项目包名调整为与配置文件一致，否则运行阶段无法校验通过。

6. 单击**配置组件**， 根据情况进行选择接入组件，点击确定。
   ![截屏2022-04-06 10.49.40](../img/配置组件.png)

7. 等待Gradle同步完成后即可开始编码。