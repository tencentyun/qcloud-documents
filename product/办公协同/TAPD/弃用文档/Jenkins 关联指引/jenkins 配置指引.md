### Jenkins关联配置步骤
1. 由公司管理员在【TAPD】>【公司管理】>【服务集成】中开启 Jenkins 关联。
![](https://main.qcloudimg.com/raw/4db62c41d79b6598e5bde15f2a269ea9.png)

2. 根据提示指引，下载 TAPD Jenkins 插件，同时获取 Webhook URL 与 Secret Token 备用。
 ![](https://main.qcloudimg.com/raw/6b3d7a6e92356fe9371d5252125e19f6.png)

3. 访问您的 Jenkins，完成插件安装
使用管理员账号进入【Jenkins】>【系统管理】页面，单击【管理插件】，安装 TAPD 插件。
![](https://main.qcloudimg.com/raw/3ead8599cc2e157cfe812e4b706777f5.png)

选择【高级】>【上传插件】，选中下载好的插件进行安装。（代理与升级无需设置）
![](https://main.qcloudimg.com/raw/c27dca2a080e23d4c6c5cc576af376bd.png)

4. 在 Jenkins 中完成插件全局设置
插件安装完成后，使用管理员账号进入【Jenkins】>【系统管理】页面，单击 TAPD 插件配置，填写相关配置信息。
![](https://main.qcloudimg.com/raw/53667e6c1fe0eabe75f6bd4a3842c7a0.png)
![](https://main.qcloudimg.com/raw/6dd23b0c4851924ddcb3401946ad3b45.png)

**字段说明**
- Webhook 地址： Jenkins 与 TAPD 通过 Webhook 关联，可将第2步中获取的 Webhook 配置填入。也可以进入 TAPD 项目设置-应用设置，选择【持续集成】配置并获取地址填入 
- Secret Token： 用于 Webhook 安全校验，可将第 2 步中获取的Webhook配置填入。也可以进入TAPD 项目设置-应用设置，选择【持续集成】配置并获取
- Jenkins 名称： 给 Jenkins 命名，方便在 TAPD 管理 Jenkins 配置时，根据名称选择调用对应 Jenkins 服务 （格式要求：8-20 位字符，请输入中英文、下划线、英文句号和数字，且只能以中英文开头） 
- Jenkins 管理员： 填写 Jenkins 的管理员账号，以便管理 Job 构建 
- Jenkins 访问地址： 请确保当前 jenkins 服务器已开通外网访问策略，并填写可以从外网访问的 jenkins 主页链接地址（示例：http://123.207.x.x/jenkins）, 以支持从 TAPD 访问当前 Jenkins

5. 访问 TAPD，在目标项目下开启【持续集成】应用并完成应用配置
开启【持续集成】应用并完成应用配置。
![](https://main.qcloudimg.com/raw/861d5c2110a0e66124e4fe9db57e5705.png)
![](https://main.qcloudimg.com/raw/64af3ca5757384be1acbc519e925fb4f.png)

Webhook 配置： 获取 Webhook 配置并填入 Jenkins，如已完成第 4 步可跳过。
![](https://main.qcloudimg.com/raw/8ce1f0cd13bc308e815f61612c980c2c.png)

选择 Jenkins： 将 Jenkins 服务与当前项目关联，以便构建过程与结果在流水线中展示。
![](https://main.qcloudimg.com/raw/86df914b4843535be2cd5f2297b47d6b.png)

配置消息通知： 将每次构建结果，及构建包含的 TAPD 业务对象（需求/缺陷/任务）以邮件、站内信、企业微信等方式通知指定用户。
![](https://main.qcloudimg.com/raw/be77d90f6deeac70f46a68fe268646db.png)

6. 在 Jenkins 中新建构建 Job，填写 TAPD 项目 ID，即可开始使用
![](https://main.qcloudimg.com/raw/3bd24746f9086f1cb5be37573cb970be.png)

项目 ID 获取方式： 
进入【TAPD 项目】>【持续集成】应用右上角复制即可。
![](https://main.qcloudimg.com/raw/af46425098227a6dfb9986769600d4a9.png)

配置完成后，每次构建结果将会被自动推送至 TAPD 指定项目，通过 TAPD 即可查看构建结果、查询构建历史，获取构建业务对象信息。