> 本次实践仅在通过 Docker 制品触发后才会生效，手动提交发布单不生效。

本文将演示如何以 Docker 制品为触发器，启动部署流程后将制品自动部署至主机组中。

## [创建应用与流程](#create)

您可以参考[此文档](/docs/cd/app-project.html)在部署控制台中创建应用与流程，本文不再赘述。

## [配置流程触发器](#config)

在流程的基础配置中添加触发器，并且触发器类型选择 Docker 仓库触发器。

![](https://help-assets.codehub.cn/enterprise/20220427095640.png)

点击自定义触，选择能够触发此流程的制品。

![](https://help-assets.codehub.cn/enterprise/20220426151521.png)

## [添加阶段](#add-stage)

在流程中添加阶段，选择“通用类型”下的“自定义变量”。

![](https://help-assets.codehub.cn/enterprise/20220426152049.png)

在阶段中添加两个变量：

-   dockerImageVersion：获取触发本次流程的 docker 镜像的版本，值为：

```bash
${trigger["artifacts"].?[name=="jiyunkeji-docker.pkg.coding.net/ccj-demo/test_demo/java-spring-app"][0]["version"]}
```

-   dockerImageName：获取触发本次流程的 docker 镜像的名称，值为：

```bash
${trigger["artifacts"].?[name=="jiyunkeji-docker.pkg.coding.net/ccj-demo/test_demo/java-spring-app"][0]["name"]}
```

-   dockerRepoURL：制品仓库的 URL，一般为 “CODING 域名-docker.pkg.coding.net”，例如 `jiyunkeji-docker.pkg.coding.net`

其中需将示例 URL：`jiyunkeji-maven.pkg.coding.net/ccj-demo/mvn-test/com.example:spring-boot` 部分替换为实际团队中 docker 镜像的 URL。您可以参考下图进行获取。

![](https://help-assets.codehub.cn/enterprise/20220427100849.png)

添加后如下图所示：

![](https://help-assets.codehub.cn/enterprise/20220427101343.png)

## [添加部署（主机组）阶段](#add-host-stage)

在流程中添加部署（主机组）阶段，选择对应的主机组与服务名称。在阶段中填写后置脚本。其中的 `docker run` 命令需根据团队中的镜像运行命令进行修改。

![](https://help-assets.codehub.cn/enterprise/20220427101816.png)

## [执行完成](#finish)

运行部署流程后出现下图结果说明制品发布成功。

![](https://help-assets.codehub.cn/enterprise/20220426155516.png)

![](https://help-assets.codehub.cn/enterprise/20220427102318.png)