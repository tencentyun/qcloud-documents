[Vue](https://cn.vuejs.org/) 是一款流行的 Web 开源框架。

代码示例：[Vue.js](https://github.com/TencentCloudBase/cloudbase-templates/tree/master/vue-hello-world)

## 步骤1：初始化项目

使用 [vue-cli](https://cli.vuejs.org/zh/guide/) 命令行初始化一个项目：

```sh
npx vue create vue-hello-world
```

## 步骤2：发布项目

安装并登录 CloudBase Framework，在项目根目录下运行：

```sh
cloudbase framework deploy -e <your-env-id>
```

或单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-templates&workDir=vue-hello-world&branch=master" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div><br>

更多内容请参见 [CloudBase Framework 文档](https://docs.cloudbase.net/framework/index)。


