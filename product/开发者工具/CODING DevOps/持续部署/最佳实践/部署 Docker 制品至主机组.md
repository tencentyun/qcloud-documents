>? 本次实践仅在通过 Docker 制品触发后才会生效，手动提交发布单不生效。

本文将演示如何以 Docker 制品为触发器，启动部署流程后将制品自动部署至主机组中。
 
[](id:create)
## 创建应用与流程
您可以参见 [应用与项目](https://cloud.tencent.com/document/product/1159/45163) 在部署控制台中创建应用与流程，本文不再赘述。

[](id:config)
## 配置流程触发器
1. 在流程的基础配置中添加触发器，并且触发器类型选择 Docker 仓库触发器。
![](https://qcloudimg.tencent-cloud.cn/raw/ceeb564dd7a2b629cbccf72a66bfd089.png)
2. 单击 **自定义**，选择能够触发此流程的制品。<br>
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/a5067b6491d807a499eed5fcb4d8cd0f.png" />

[](id:add-stage)
## 添加阶段
1. 在流程中添加阶段，选择**通用类型**下的 **自定义变量**。
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7637e6889013d81c44e144c038ccc3ba.png" />
2. 在阶段中添加两个变量：
 -   dockerImageVersion：获取触发本次流程的 docker 镜像的版本，值为：
```bash
${trigger["artifacts"].?[name=="jiyunkeji-docker.pkg.coding.net/ccj-demo/test_demo/java-spring-app"][0]["version"]}
```
 -   dockerImageName：获取触发本次流程的 docker 镜像的名称，值为：
```bash
${trigger["artifacts"].?[name=="jiyunkeji-docker.pkg.coding.net/ccj-demo/test_demo/java-spring-app"][0]["name"]}
```
 -   dockerRepoURL：制品仓库的 URL，一般为 “`CODING 域名 - docker.pkg.coding.net`”，例如 `jiyunkeji-docker.pkg.coding.net`
其中需将示例 URL：`jiyunkeji-maven.pkg.coding.net/ccj-demo/mvn-test/com.example:spring-boot` 部分替换为实际团队中 docker 镜像的 URL。您可以参见下图进行获取。
![](https://qcloudimg.tencent-cloud.cn/raw/a98451643bd56820901f8971324c1c3b.png)
3. 添加后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a87d7299e3f0b18a7f4bd86dcf8a8911.png)

[](id:add-host-stage)
## 添加部署（主机组）阶段
在流程中添加部署（主机组）阶段，选择对应的主机组与服务名称。在阶段中填写后置脚本。其中的 `docker run` 命令需根据团队中的镜像运行命令进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/5a9a1b3efc6fc016b1d0082948d631e2.png)

[](id:finish)
## 执行完成
运行部署流程后出现下图结果说明制品发布成功。
![](https://qcloudimg.tencent-cloud.cn/raw/4751052ccf08dd8f965c06a235fb12bb.png)
