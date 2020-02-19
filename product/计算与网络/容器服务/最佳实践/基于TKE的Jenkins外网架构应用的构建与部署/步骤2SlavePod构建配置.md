本步骤介绍了如何在 Jekins 中通过创建新任务、配置任务参数来构建 slave pod。

## 创建新任务
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


## 任务参数配置
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
  - **Parameter Type**：选择【Check Boxes】。
  - **Value**：选择此项，并输入自定义镜像名称，该值将传递给变量 `name`，本文以 `nginx.php` 为例。
3. 选择【添加参数】>【Extended Choice Parameter】，在打开的 “Extended Choice Parameter” 面板中设置以下参数。如下图所示：
![](https://main.qcloudimg.com/raw/b1cf3b28eb257c944591f63a64319959.png)
主要参数信息如下，其余选项请保持默认设置：
 - **Name**：输入 `version`，该参数用于获取镜像版本变量。
 - **Basic Parameter Types**：选择此项。
 - **Parameter Type**：选择【Text Boxe】 ，表示以文本形式获取镜像值，并传递给变量 `version`。
4. 勾选【限制项目的运行节点】，标签表达式填写[ 配置 slave pod 模板 ](https://cloud.tencent.com/document/product/457/41396#PodTemplates)步骤中已设置的 Pod 标签  `jnlp-agent`。如下图所示：
![](https://main.qcloudimg.com/raw/14af6a18f81bdd91657d7b91869ad1ed.png)

## 源码管理配置
在“源码管理”模块中，勾选【Git】，并进行以下信息配置。如下图所示：
![](https://main.qcloudimg.com/raw/0cac3f82568d7dda39154d191305c336.png)
- **Repositories**：
  - **Repository URL**：输入您的 gitlab 地址。例如 `https://gitlab.com/user-name/demo.git`。
  - **Credentials**：选择已在 [添加 gitlab 认证](https://cloud.tencent.com/document/product/457/41396#addGitlab) 步骤中创建的认证凭据。
- **Branches to build**：
  - **指定分支（为空时代表any）**：输入`$mbranch`，用于动态获取分支，其值与 Git Parameter 参数中定义的 `mbranch` 值对应。


## Shell 打包脚本配置
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

## 后续操作
至此您已成功将镜像推送至 TKE 镜像仓库，请前往 [构建测试](https://cloud.tencent.com/document/product/457/41398) 进行验证操作。
