



### Slave pod 构建配置<span id="slavepod"></span>

#### 步骤1：创建新任务
1. 登录 Jenkins 后台，单击【新建任务】或【创建一个新任务】。如下图所示：
![](https://main.qcloudimg.com/raw/9d55abf0cd2e3b37fa84b0d7b56952c3.png)
2. 在新建任务页，设置任务的基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/b4837f27503003894a512f52e9bfacaa.png)
 - **输入一个任务名称**：自定义，本文以 `test` 为例。
 - **类型**：选择【构建一个自由风格的软件软件项目】。
3. 单击【确定】，进入任务参数配置页，进行基本信息配置。如下图所示：
![](https://main.qcloudimg.com/raw/d4bba762fca6727fdee4fd62b8151faf.png)
 - **描述**：自定义填写任务的相关信息，本文以 slave pod test 为例。
 - **参数化构建过程**：勾选此项，并选择【添加参数】>【Git Parameter】。


#### 步骤2： 任务参数配置
1. 在打开的 “Git Parameter” 面板中，依次设置以下参数。如下图所示：
![](https://main.qcloudimg.com/raw/a6422d4faedba25661fb648f7bf71ab8.png)
主要参数信息如下，其余选项请保持默认设置：
 - **Name**：输入 `mbranch`，该参数可用于匹配获取分支。
 - **Parameter Type**：选择【Branch or Tag】。
2. 选择【添加参数】>【Extended Choice Parameter】，在打开的 “Extended Choice Parameter” 面板中设置以下参数。如下图所示：
![](https://main.qcloudimg.com/raw/f1ea047aaf190e3273dbfa2c937d4c42.png)
主要参数信息如下，其余选项请保持默认设置：
  - **Name**：输入 `name`，该参数可用于获取镜像名称。
  - **Basic Parameter Types**：选择此项。
  - **Parameter Type**：选择【Check Boxes】 。
  - **Value**：选择此项，并输入自定义镜像名称，该值将传递给变量 `name`，本文以 `nginx.php` 为例。
3. 选择【添加参数】>【Extended Choice Parameter】，在打开的 “Extended Choice Parameter” 面板中设置以下参数。如下图所示：
![](https://main.qcloudimg.com/raw/b1cf3b28eb257c944591f63a64319959.png)
主要参数信息如下，其余选项请保持默认设置：
 - **Name**：输入 `version`，该参数用于获取镜像版本变量。
 - **Basic Parameter Types**：选择此项。
 - **Parameter Type**：选择【Text Boxe】 ，表示以文本形式获取镜像值，并传递给变量 `version`。
4. 勾选【限制项目的运行节点】，标签表达式填写[ 配置 slave pod 模板 ](#PodTemplates)步骤中已设置的 Pod 标签  `jnlp-agent`。如下图所示：
![](https://main.qcloudimg.com/raw/14af6a18f81bdd91657d7b91869ad1ed.png)

#### 步骤3：源码管理配置
在“源码管理”模块中，勾选【Git】，并进行以下信息配置。如下图所示：
![](https://main.qcloudimg.com/raw/0cac3f82568d7dda39154d191305c336.png)
- **Repositories**：
  - **Repository URL**：输入您的 gitlab 地址。例如 `https://gitlab.com/user-name/demo.git`。
  - **Credentials**：选择已在 [添加 gitlab 认证](#addGitlab) 步骤中创建的认证凭据。
- **Branches to build**：
  - **指定分支（为空时代表any）**：输入`$mbranch`，用于动态获取分支，其值与 Git Parameter 参数中定义的 `mbranch` 值对应。


#### 步骤4：shell 打包脚本配置
1. 在“构建”模块中，选择【增加构建步骤】>【执行 shell】。如下图所示：
![](https://main.qcloudimg.com/raw/6c65ffbe6209bba313b8e82ad6c1da72.png)
2. 将以下脚本内容复制粘贴至“命令”输入框中，并单击【保存】。
>! 脚本中 gitlab 地址、TKE 镜像地址、镜像仓库用户名及密码等信息为示例使用，请根据实际需求进行更换。
>
```
	echo " gitlab 地址为：https://gitlab.com/[user]/[project-name]].git" 
	echo "选择的分支（镜像）为:"$mbranch，"设置的分支（镜像）版本为:"$version
	echo " TKE 镜像地址：hkccr.ccs.tencentyun.com/[namespace]/[ImageName]"

	echo "1.登录 TKE 镜像仓库"
	docker login --username=[username] -p [password] hkccr.ccs.tencentyun.com

	echo "2.基于源代码 Docker build 构建打包："
	cd /home/Jenkins/workspace/test && docker build -t $name:$version .

	echo "3.Docker镜像上传至TKE仓库："
	docker tag $name:$version hkccr.ccs.tencentyun.com/[namespace]/[ImageName]:$name-$version
	docker push hkccr.ccs.tencentyun.com/[namespace]/[ImageName]:$name-$version
```
该脚本提供以下功能：
    - 获取选择的分支、镜像名称及镜像版本。
    - 将与代码合并构建后的 docker 镜像推送至 TKE 镜像仓库。


### 构建测试

#### 步骤1：构建配置<span id="buildConfiguration"></span>
1. 登录 Jenkins 后台，单击任务列表中已在 [slave pod 构建配置](#slavepod) 步骤所创建的任务 test。如下图所示：
![](https://main.qcloudimg.com/raw/a20c4abc886959dac79199857354dd68.png)
2. 单击左侧菜单栏中的【Build with Parameters】，打开“工程 test ”面板，进行以下参数设置。如下图所示：
![](https://main.qcloudimg.com/raw/bf1ebecd4bc6a39da60a94f1afd7e749.png)
  - **mbranch**：选择构建所需分支，本文以 `origin/nginx` 为例。
  - **name**：根据实际需求选择所构建镜像的名称，本文以 `nginx.php`为例。
  - **version**：自定义输入镜像版本号，本文以 `v1` 为例。
3. 单击【开始构建】。
构建成功即前往 TKE 控制台 >【镜像仓库】>【[我的镜像](https://console.cloud.tencent.com/tke2/registry/user)】中进行查看。如下图所示：
![](https://main.qcloudimg.com/raw/8692532e791aaea3d964145b854ca627.png)

#### 步骤2：控制台发布
1. 登录 TKE 控制台，选择左侧导航栏中的【[集群](https://console.cloud.tencent.com/tke2/cluster)】。
2. 选择目标集群 ID，进入待创建 “Deployment” 的集群管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/8f231ef9688d171d4bcc6489cc26905c.png)
3. 单击【新建】，进入 “新建Workload ” 页面，参考 [ 创建 Deployment ](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 进行关键参数设置。
 在“实例内容器”中，可选择【选择镜像】>【我的镜像】，选择上述构建过程中已成功上传的镜像。如下图所示：
![](https://main.qcloudimg.com/raw/e992f2edade27b658d9e46a6a6dd589d.png)
4. 单击【保存】即可完成部署。
在【Pod 管理页】中，nginx pod 正常运行且为 Runing 状态即为部署成功。如下图所示：
![](https://main.qcloudimg.com/raw/fc6026a4a27234f9e9c6b1e3926d39b5.png)


## 相关操作
### 批量构建设置
1. 登录 Jenkins 后台，选择左侧导航栏中的【系统管理】，在打开的“管理Jenkins” 面板中单击【系统配置】。如下图所示：
![](https://main.qcloudimg.com/raw/e79a2e78e69de69954c75f4cf4c6feeb.png)
2. 在“系统配置”页，自定义修改“执行者数量”，本文以数量10为例。
>?执行者数量为10 ，则表示可以同时执行10 个 Job。
>
3. 其他配置项保持[ 配置 slave pod 模板 ](#PodTemplates)步骤中所设置的内容。
4. 参考[ Slave pod 构建配置 ](#slavepod)步骤，根据实际需求依次新建10个 test。如下图所示：
![](https://main.qcloudimg.com/raw/f4e63d7e897ceb84a68322104d6db571.png)
5. 参考 [构建配置](#buildConfiguration) 步骤依次执行多个任务构建。
6. 成功构建后，您可登录 node 节点，执行以下命令查看 job pod。
```
kubectl get pod
``` 
返回类似如下结果，则表示调用成功。
![](https://main.qcloudimg.com/raw/025eef4ec97671da2cc71508f4946820.png)
