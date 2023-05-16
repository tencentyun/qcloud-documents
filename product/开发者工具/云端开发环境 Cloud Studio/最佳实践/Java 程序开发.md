Cloud Studio 预置了 Java 开发必备的 JDK 和插件，您只需创建一个 Java 空项目或导入您在 Git 仓库的 Java 代码即可快速打开一个工作空间，马上进行开发工作。接下来您将会了解如何在 Cloud Studio 编写与调试 Java 代码。

## 创建项目
### Maven 项目
1.	新建一个 Java 预置环境工作空间。
![](https://qcloudimg.tencent-cloud.cn/raw/97f54cc4e0b4908b99ddf4d0d4a983ac.png)
2.	进入工作空间后，打开命令面板，输入 Create Java Project ，选择 Maven create from archetype ，选择 maven-archetype-quickstart。
![](https://qcloudimg.tencent-cloud.cn/raw/7b077bfa9d483a90fcbbd487c7e1ce09.png)
![](https://qcloudimg.tencent-cloud.cn/raw/9da10fe3fe2dcdca7c5f10427a89f85a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/b08d3ce6b8d8cf6f6871052deacbba72.png)
![](https://qcloudimg.tencent-cloud.cn/raw/fbbc0420fe55af6b7e5facb8cffa0e5b.png)
![](https://qcloudimg.tencent-cloud.cn/raw/c633b117c45b2812f25159f039f6e045.png)
配置 Maven 国内源 访问 Maven 默认远程中央镜像特别慢，可以用国内的镜像仓库替代。
![](https://qcloudimg.tencent-cloud.cn/raw/0f26ea9c62210d27dd2c87b8962223b9.png)

### SpringBoot 项目
1.	新建一个 SpringBoot 预置环境工作空间。
2.	进入工作空间后，打开命令面板，输入 Spring Initializr。
![](https://qcloudimg.tencent-cloud.cn/raw/7b92881e75ef66d87440c553375b7e0e.png)
3.	创建工程时要选择依赖，Web 开发选择如下的包： DevTools（代码修改热更新，无需重启）、Web（集成tomcat、SpringMVC）、Lombok（智能生成 setter、getter、toString 等接口）等。
![](https://qcloudimg.tencent-cloud.cn/raw/fafe8a39a1d2e64091497531be13492b.png)

### 代码编辑
Cloud Studio 提供自动导入包，语法高亮，代码补全，代码跳转等特性，像本地 IDE 一样自然。
![](https://qcloudimg.tencent-cloud.cn/raw/8e0a71fbb1a21635a370b95d9fffc469.png)

### 代码调试与运行
Cloud Studio 提供的是开箱即用的云原生应用开发平台，为了实现代码调试，您所要做的就是打开您的 Java 项目，然后找到您的代码 main 所在的代码文件，等待IDE底部状态栏的 Java 项目加载完毕即可进行。
![](https://qcloudimg.tencent-cloud.cn/raw/fc891a82f7944cdd262bfa53ce894be2.png)
