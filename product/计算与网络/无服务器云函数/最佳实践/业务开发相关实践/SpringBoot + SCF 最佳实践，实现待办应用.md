
## 操作场景

 [Spring Boot](https://spring.io/projects/spring-boot) 是由 Pivotal 团队提供的框架，用来简化新 Spring 应用的初始搭建以及开发过程。该框架使用了特定的方式来进行配置，从而使开发人员不再需要定义样板化的配置。

本文将介绍如何通过 SCF 使用 SpringBoot 搭建一个待办应用。SCF 提供事件触发的 [事件函数](https://cloud.tencent.com/document/product/583/9210) 和 HTTP 请求触发的 [Web 函数](https://cloud.tencent.com/document/product/583/56124) 两种函数类型，在 SpringBoot 场景下推荐使用 Web 函数。

## 前提条件

请参考 [云函数 JAVA 开发指南](https://cloud.tencent.com/document/product/583/12214) 准备开发环境和工具。




## 操作步骤

### 使用 Web 函数

SCF 提供模板函数，按照如下流程操作可使用 Web 函数快速创建一个待办应用并体验待办事项的增删改查功能。

>! 本模板仅作为示例提供，待办事项数据实际存储在实例缓存中，不作为持久化存储。

#### 创建函数[](id:createwebfunc)

1.  登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
2.  在**函数服务页**中单击**新建**。
3. 在**新建**页中，选择**模板创建**，并搜索关键词 `springboot`、`webfunc`。在查询结果中选择 **SpringBoot 待办应用**并单击**下一步**。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/2d969cfd33c1af14c8a4d913e758a079.png )
4. 保持默认配置，单击**完成**，完成函数创建。


#### 测试函数

在**函数代码**页签，按照如下流程操作，通过测试模板发起模拟请求体验待办应用增删改查功能：

-   查询待办列表：
 请求方式选择 GET, path 填写 `/todos`，单击**测试**后，在响应 Body 中可以查看到当前的待办事项。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/848f77562bfcd160ed6ce63befcbbc4b.png )

-   增加待办事项：
 请求方式选择 POST, path 填写 `/todos`，body 填写 `{"key":"3","content":"Third todo","done": false}`，单击**测试**增加一个待办事项。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/3660186c9ed79d085fe996d328b24050.png )

-   删除待办事项：
 请求方式选择 DELETE，以删除 key 为 2 的待办事项为例，path 填写 `/todos/2`，单击**测试**。如下图所示： 
  ![](https://qcloudimg.tencent-cloud.cn/raw/0e360c365bf56fec6743965c744b56e6.png )

-   修改待办事项：
 请求方式选择 PUT，以将 key 为 3 的待办事项由未完成改为完成为例，path 填写 `/todos/3`，body 填写 `{"key":"3","content":"Third todo","done": true}`，单击**测试**。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/059637de6730a53a0b13ca912c17e882.png )



#### 代码示例

在 [创建函数](#createwebfunc) 步骤中，您也可以根据业务需求修改函数模板。在**模板选择**页面，单击模板卡片右上角的**查看详情**，在展开的页面中单击**单击下载模板函数**即可获取模板函数源码。

原生 SpringBoot 项目迁移到 Web 函数需要执行如下步骤：

-   确保 Spring 监听端口为 9000（SCF Web 函数指定监听端口）。
 ![](https://qcloudimg.tencent-cloud.cn/raw/d47575ec0139f5eb6f4293e87fd93a4a.png )

-   编译 JAR 包。
 下载代码之后，在目录 `Webfunc-Java8-SpringBoot` 下运行编译命令：
  ```shell
  gradle build
  ```
 编译完成后可在 `build/libs` 目录下获取到打包完成的 jar 包，选择后缀为 `-all` 的 jar 包。

-   准备一个可执行文件 `scf_bootstrap` 用于启动 Web Server，文件内容可参考下文:
  ``` shell
  #!/bin/bash
  /var/lang/java8/bin/java -Dserver.port=9000 -jar scf-springboot-java8-0.0.2-SNAPSHOT-all.jar
  ```
>! 在 scf_bootstrap 文件所在目录执行 `chmod 755 scf_bootstrap` 来保证 scf_bootstrap 文件具有可执行权限。

-   将 `scf_bootstrap` 文件与生成的 jar 包一起打包为 zip 部署到云函数。部署函数步骤如下：
    1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
    2. 在**函数服务页**中单击**新建**。
    3. 在**新建**页中，选择**从头开始**。参考以下内容进行配置：
          **函数类型**：web 函数
          **运行环境**：Java8
          **提交方法**：本地上传 zip 包
          **函数代码**：单击上传选择打包好的 zip 文件
    4. 其他保持默认配置，单击**完成**即可完成函数创建。如下图所示： 
  ![](https://qcloudimg.tencent-cloud.cn/raw/a7d6a46da50b4b036052fbffbbdc3f64.png )



### 使用事件函数



SCF 提供模板函数，按照如下流程操作可使用事件函数快速创建一个待办应用并体验待办事项的增删改查功能。

>! 本模板仅作为示例提供，待办事项数据实际存储在实例缓存中，不作为持久化存储。

#### 创建函数[](id:createnew)
1.  登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
2.  在**函数服务页**中单击**新建**。
3. 在**新建**页中，选择**模板创建**，并搜索关键词 `springboot`。在查询结果中选择 **SpringBoot** 并单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/65b09f8bb55d040c671e14f8181f4042.png )
4. 保持默认配置，单击**完成**，完成函数创建。

#### 创建触发器

>! 如果在创建函数过程中已经创建好 API 网关触发器，核对已有触发器与下文配置一致即可。

1.  函数创建完成后，在**触发管理**页签，单击**创建触发器**。
 ![](https://qcloudimg.tencent-cloud.cn/raw/ca56ea1857c4d2cc9fc80b278850cf4f.png )
2.  在弹窗中进行触发器配置。参考以下内容进行选择，其余保持默认配置，单击**提交**。
 -   触发方式：API 网关触发
 -   集成响应：启用
3.  创建完成后需要调整 API 网关触发器的参数，单击 **API 服务名**跳转到 API 网关控制台进行下一步操作。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/54306b91af946ec7fc47625ec2323630.png )
4.  在 API 网关控制台找到函数使用的 API，单击**编辑**。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/05698d7a681e6d031c1b72438cdc42fe.png )
修改前端配置页面中的路径为 `/todos`，单击**立即完成**，并按照引导发布服务。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/46c44df4249e235e7ef2101956d60c53.png )

#### 测试函数

在**函数代码**页签，按照如下流程操作，通过测试模板发起模拟请求体验待办应用增删改查功能：

-   查询待办列表：
 请求方式选择 GET, path 填写 `/todos`，单击**测试**后，在响应 Body 中可以查看到当前的待办事项。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/e4b753286399d7f114297d07dcdefd18.jpg )

-   增加待办事项：
 请求方式选择 POST, path 填写 `/todos`，body 填写 `{"key":"3","content":"Third todo","done": false}`，单击**测试**增加一个待办事项。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/b40a2869449b491b1911a9d1c7c603f8.jpg )

-   删除待办事项：
 请求方式选择 DELETE，以删除 key 为 2 的待办事项为例，path 填写 `/todos/2`，单击**测试**。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/5288a5fe3ef6e5a0aad1568bd0292a52.jpg )

-   修改待办事项：
 请求方式选择 PUT，以将 key 为 3 的待办事项由未完成改为完成为例，path 填写 `/todos/2, body 填写 `{"key":"2","content":"Third todo","done": true}`，单击**测试**。如下图所示： 
 ![](https://qcloudimg.tencent-cloud.cn/raw/ecd542994b7637ed17fe5a8e72214463.jpg )

#### 代码示例
在 [创建函数](#createnew) 步骤中，您也可以根据业务需求修改函数模板。在**模板选择**页面，单击模板卡片右上角的**查看详情**，在展开的页面中单击**单击下载模板函数**即可获取模板函数源码。


可参考以下流程操作：

-   增加一个 `ScfHandler` 类，`ScfHandler` 类主要用于接收事件触发，并转发消息给 Spring 服务，函数接收到 Spring 服务的返回后再把结果返回给调用方。
  `ScfHandler` 类增加后项目结构如下：
  ```
  .
  ├── src
  |   └── main
  |        |        ├── java
  |        |        |        └── com.tencent.scfspringbootjava8
  |        |        |        |        ├── controller
  |        |        |        |        ├── model
  |        |        |        |        └── repository
  |        |        |        |        |        ├── ScfHandler.java
  |        |        |        |        |        └── ScfSpringbootJava8Application.java
  |        |        └── resources
  ```

-   编译 JAR 包
  下载代码之后，在根目录下运行编译命令：
  ```shell
  gradle build
  ```
  编译完成后可在 `build/libs` 目录下获取到打包完成的 jar 包，选择后缀为 `-all` 的 jar 包。

-   将编译生成的 jar 包部署到云函数。部署函数步骤如下：
   1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
   2. 在**函数服务页**中单击**新建**。
   3. 在**新建**页中，选择**从头开始**。参考以下内容进行配置：
     **函数类型**：事件函数函数
     **运行环境**：Java8
     **提交方法**：本地上传 zip 包
		 **执行方法**：com.tencent.scfspringbootjava8.ScfHandler:: mainHandler
		 **函数代码**：单击上传选择打包好的 zip 文件
	4. 其他保持默认配置，单击**完成**即可完成函数创建。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/7dc7b8546a710bfe12f9852a7a0f0563.png )



