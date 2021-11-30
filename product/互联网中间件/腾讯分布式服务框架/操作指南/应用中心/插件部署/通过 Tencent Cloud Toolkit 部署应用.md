## 操作场景
使用 Tencent Cloud Toolkit 可以将应用快速部署到 TSF，适用于快速迭代更新、开发阶段快速验证等场景。在 IntelliJ IDEA 安装和配置 Tencent Cloud Toolkit 后，只需在配置界面设置部署参数即可实现自动化部署，支持虚拟机部署场景和容器部署场景。

## 前提条件

您需要先在 TSF 中创建好相关的集群（Cluster）、应用（Application）、部署组（Group），具体操作部署如下（如已有相关资源请跳过这一步骤）：
  - [创建集群](https://cloud.tencent.com/document/product/649/13684)
  - [创建应用](https://cloud.tencent.com/document/product/649/13686)
  - [创建虚拟机部署组](https://cloud.tencent.com/document/product/649/15524)
  - [创建容器部署组](https://cloud.tencent.com/document/product/649/15525)

## 部署到 TSF 部署组
这里以部署 [consumer-demo](https://github.com/tencentyun/tsf-simple-demo/tree/release/1.23.0-greenwich/consumer-demo) 为例, 具体步骤如下：

### 虚拟机部署
1. 在 IntelliJ IDEA 中打开 consumer-demo 工程。
2. 在 IntelliJ IDEA 顶部菜单栏中选择 **Tools** > **Tencent Cloud Toolkit** > **Deploy to TSF for CVM Application...**。
3. 在 Deploy to CVM 对话框中部署配置。根据部署的程序包来源以及是否部署，插件提供三种选项：
   - Maven build：使用 maven 编译项目并打包、上传程序包至 TSF、部署。
   - Local file：选择本地文件上传至 TSF、部署。
   - Deploy to group：是否执行部署，默认执行。如果取消勾选，则仅上传程序包至 TSF 程序包仓库。
 
 ![](https://main.qcloudimg.com/raw/5dbef71c07478f3ec9e8e7871b935b14.png)
>?如果您尚未在 TSF 上创建应用，可在对话框右上角单击 Create application on TSF Console，跳转到 TSF 控制台创建应用。

部署参数说明如下：

<table>
<tr>
<th>参数名</th>
<th>参数</th>
<th>描述</th>
</tr>
<tbody><tr>
<td>地域</td>
<td>Region</td>
<td>服务所在地区。</td>
</tr>
<tr>
<td rowspan="2"><nobr>应用信息</nobr></td>
<td>Application</td>
<td>服务所在应用。</td>
</tr>
<tr>
<td>Group</td>
<td>服务所在部署组。</td>
</tr>
<tr>
<td rowspan="2">部署方式</td>
<td>Maven Build</td>
<td>若当前工程采用 Maven 构建，可以直接构建并部署。</td>
</tr>
<tr>
<td>Local File</td>
<td>若当前工程不是采用 Maven 构建，或本地已存在部署文件的压缩包，则上传本地的部署文件即可。</td>
</tr>
<tr>
<td rowspan="3">其他</td>
<td>Version</td>
<td>部署版本，缺省使用时间戳作为版本号。</td>
</tr>
<tr>
<td>Description</td>
<td>部署信息描述。</td>
</tr>
<tr>
<td>StartupParameters</td>
<td>启动参数。</td>
</tr>
</tbody></table>

4. 先单击 Apply，然后单击 Run。
5. 在 TSF 平台即可查看部署结果。

### 容器部署

1. 在 IDEA 中打开 consumer-demo 工程。
2. 在 IntelliJ IDEA 顶部菜单栏中选择 **Tools** > **Tencent Cloud Toolkit** > **Deploy to TSF for Kubernetes Application...**。
3. 在 TSF Deploy Container 中部署配置，跟虚拟机部署一样，根据镜像来源以及是否部署，插件提供三种选项:
   - Build image：制作镜像、上传镜像至TSF镜像仓库、部署。
   - Select image：选择镜像仓库中的镜像部署。
   - Deploy to group：是否执行部署，默认执行。如果取消勾选，则仅上传镜像至 TSF 镜像仓库。

 ![](https://main.qcloudimg.com/raw/a6de14f0ced5ddfc477bb2c9d881c8d1.png)

	- ServicePort：服务端口（该端口为服务启动时占用端口）。
	- ContainerPort：服务映射端口。
	- InstancePort：K8S 中使用 NodePort 方式部署时指定 NodePort 端口（端口范围：30000-32767）。这部分逻辑同 TSF。

Settings 页签部署参数配置说明如下：
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>地域</td>
<td>Region</td>
<td>服务所在地区。</td>
</tr>
<tr>
<td rowspan="2"><nobr>应用信息</nobr></td>
<td>Application</td>
<td>服务所在应用。</td>
</tr>
<tr>
<td>Group</td>
<td>服务所在部署组。</td>
</tr>
<tr>
<td rowspan="2">部署方式</td>
<td>Build Image</td>
<td>制作镜像、上传镜像至 TSF 镜像仓库、部署。</td>
</tr>
<tr>
<td>Select Image</td>
<td>选择镜像仓库中的镜像进行部署。</td>
</tr>
<tr>
<td rowspan="2">请求配置</td>
<td>Network AccessMode</td>
<td>部署方式。</td>
</tr>
<tr>
<td>Port</td>
<td>ContainerPort：服务映射端口；ServicePort（应用服务启动端口）；<br>IntancePort：K8S 中使用 NodePort 方式部署时指定 NodePort 端口（端口范围: 30000-32767）。</td>
</tr>
<tr>
<td rowspan="3">其他</td>
<td>Version</td>
<td>部署版本，缺省使用时间戳作为版本号。</td>
</tr>
<tr>
<td>Context Directory</td>
<td>Docker 命令执行目录，Dockerfile 文件中依赖的 context 目录。</td>
</tr>
<tr>
<td>Dockerfile</td>
<td>Dockerfile 所在文件目录。</td>
</tr>
</tbody></table>

4. Advanced 提供容器部署的相关高级参数设置，包括 pod 更新、调度规则、健康检查相关的配置。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>资源配置</td>
<td>ApplicationContianer</td>
<td>配置应用所在 POD 占用的内存和 CPU 大小。</td>
</tr>
<tr>
<td rowspan="3">应用管理</td>
<td>Update Method</td>
<td>POD 更新策略配置。</td>
</tr>
<tr>
<td>Schedule Rules</td>
<td>POD 调度策略。</td>
</tr>
<tr>
<td>HealthCheck</td>
<td>就绪检查（Readiness），存活检查（Liveness）。</td>
</tr>
<tr>
<td rowspan="2">其他</td>
<td>StartupParameters</td>
<td>容器应用启动参数。</td>
</tr>
<tr>
<td>Envs</td>
<td>容器应用环境变量。</td>
</tr>
</tbody></table>
>?相关参数详可参考 [TSF 容器部署](https://cloud.tencent.com/document/product/649/15525)。

5. 先单击 **Apply**，然后单击 **Run**。
6. 在 TSF 平台即可查看部署结果。
