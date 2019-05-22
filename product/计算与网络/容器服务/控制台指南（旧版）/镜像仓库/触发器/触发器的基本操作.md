## 如何使用镜像仓库触发器
使用仓库触发器的步骤分为如下三步：
1. 选择具体镜像仓库创建触发器，配置触发表达式和服务更新参数。
2. 通过腾讯云 CI 或者 docker push 镜像到镜像仓库，确认提交的镜像是否满足触发表达式的条件。
3. 查看触发器日志，检查触发动作是否执行成功。

## 创建镜像仓库触发器
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏的【镜像仓库】，在镜像仓库下拉列表中单击【我的镜像】。在我的镜像库页面单击镜像的 **名称**（如图中 test）。
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. 单击【触发器】>【添加触发器】。
![](//mc.qcloudimg.com/static/img/c63426ed0398fc08aa28e81ddf7be8aa/image.png)
4. 设置触发器属性。
 - **触发器名称**：创建的触发器名称。英文字母开头，2 - 64 个字符以内 。
 - **触发条件**：分为三种触发条件。
 i：**全部触发**：镜像仓库内，有新的 Tag（镜像版本）生成，或 Tag 发生更新时，触发动作。
 ii：**指定 Tag 触发**：镜像仓库内，有指定 Tag 生成或更新时，触发动作。
 iii：**正则触发**：镜像仓库内，有符合正则表达式的 Tag 生成或更新时，触发动作。
 - **触发动作**：更新容器的镜像。
 - **选择服务/镜像**：单击【请选择容器镜像】，在下拉列表中选择地域、集群、Namespace、服务、容器镜像属性。
![](//mc.qcloudimg.com/static/img/6e2200e24d13e873354bb38ade55e14d/image.png)
5. 单击【保存】。完成触发器的创建。

## 修改镜像仓库触发器
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏的【镜像仓库】，在镜像仓库下拉列表中单击【我的镜像】。在我的镜像库页面单击镜像的 **名称**（如图中 test）。
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. 单击【触发器】进入触发器列表页，单击触发器显示栏右侧修改图标。
![](//mc.qcloudimg.com/static/img/77b87f6ba86db13caa0bc6d9fb623499/image.png)

## 删除镜像仓库触发器
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏的【镜像仓库】，在镜像仓库下拉列表中单击【我的镜像】。在我的镜像库页面单击镜像的 **名称**（如图中 test）。
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. 单击【触发器】进入触发器列表页，单击触发器显示栏右侧删除图标。
![](//mc.qcloudimg.com/static/img/a453712626e6cf47f591e5142010f842/image.png)

## 查看触发日志
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏的【镜像仓库】，在镜像仓库下拉列表中单击【我的镜像】。在我的镜像库页面单击镜像的 **名称**（如图中 test）。
![](//mc.qcloudimg.com/static/img/9a03bc50e2504270bc784093441d91d0/image.png)
3. 单击【触发器】进入触发器列表页，即可浏览触发日志。
![](//mc.qcloudimg.com/static/img/f5751a02e2a899d97b2d46c2866e218e/image.png)
