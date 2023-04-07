## 前提条件
1. 您已安装 Android Studio 4.0 及以上版本。
2. 您已经获得了 IDE 插件的安装包，安装包名称为 TMF-AS-plugin-x.x.zip。
>?下载 IDE 插件请单击：[开发者工具](https://tmf-warehouse-1257849200.cos.ap-beijing.myqcloud.com/tmf/ide/TMF-AS-plugin.zip)，插件安装包为压缩包文件形式，在安装前无需解压。

## 操作步骤

### 步骤一：软件安装[](id:install)
1. 在 Android Studio 中，通过 **Android Studio** > **Preference** 打开设置对话框。
2. 在页面左侧，单击 **Plugins**，然后在右上方单击<img src="https://qcloudimg.tencent-cloud.cn/raw/e618f71cd3c5384c31735f3354a2c805.png" width="2%"> ，并在下拉菜单中单击 **Install Plugin from Disk**。  
![](https://qcloudimg.tencent-cloud.cn/raw/fcd3ebc926d99ac2030545568852947d.png)
3. 选择您已经下载的 TMF 插件安装包，单击 **Open**。
4. 安装完成后，单击 **Restart IDE**，重启 Android Studio，您即可开始使用 TMF 插件。


### 步骤二：新建工程[](id:new)
1. 登录 [控制台](https://console.cloud.tencent.com/tmf)，下载应用配置文件（tmf-android-configurations.json）。
2. 在 Android Studio 欢迎页面，单击 **Start a New TMF Project**，创建项目。   
![](https://qcloudimg.tencent-cloud.cn/raw/f3dcddf0549f71a9d42aefb03f69969d.png)
>?您也可以通过单击 **File** > **New** > **Start a New TMF Project**，创建项目。
>
3. 返回 Android Studio 创建TMF项目页面，配置项目参数，填写项目名称、包名，并选择编程语言、存储位置和控制台下载的应用配置文件（JSON）路径，单击 **Next**。
![](https://qcloudimg.tencent-cloud.cn/raw/bb3352ee185c5b70776226bcb0180edc.png)
**字段说明**：
  - Name: 项目名称。
  - Package Name: 应用包名，**需与控制台配置的包名一致，否则运行时校验无法通过**。
  - Language: 开发语言选择。
  - Save location: 项目存储路径。
  - ConfigFile location: 应用配置文件（tmf-android-configuratsion.json）路径。
4. 选择产品基线与依赖组件，单击 **Finish**，结束向导。
![](https://qcloudimg.tencent-cloud.cn/raw/201d9618f5ef1fca46a9dfbc38d380ab.png)
5. 创建完成，开始编码。


### 步骤三：已有工程[](id:import)
1. 登录 [控制台](https://console.cloud.tencent.com/tmf)，下载应用配置文件(tmf-android-configurations.json)。
2. 在编码界面右侧侧边栏单击 **TMF**，打开 TMF 助手。
![](https://qcloudimg.tencent-cloud.cn/raw/ac1628da1f1126aca4fb91b6855492ce.png)
3. 单击**点击转换**，即可将现有的非 TMF 工程转换为 TMF 工程，此操作会在 gradle 中配置 maven 信息，以及在工程目录下生成 .tmf.config.json 文件并添加基线配置。
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
>?仓库用户名和密码请向管理员获取。
>
4. 将下载的配置文件（tmf-android-configurations.json）拷贝至 assets 目录。
![](https://qcloudimg.tencent-cloud.cn/raw/c768f103a1711f83f03520a73180ff15.png)
5. 校验项目包名是否与配置文件中包名一致，如果不一致需要将项目包名调整为与配置文件一致，否则运行阶段无法校验通过。
6. 单击**配置组件**， 根据情况进行选择接入组件，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/3b035146a03a44cdb9bce5e166be7a0e.png)
7. 等待 Gradle 同步完成后即可开始编码。
