[Hexo](https://hexo.io/) 是一款基于 Node.js 的静态博客生成器。

代码示例：[Hexo](https://github.com/TencentCloudBase/cloudbase-templates/tree/master/hexo)

## 步骤1：初始化项目

使用 hexo 命令行初始化一个项目：

```sh
npm hexo init hexo-hello-world
```

## 步骤2：发布项目

安装并登录 CloudBase Framework，在项目根目录下运行：

```sh
cloudbase framework deploy -e <your-env-id>
```

或单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-templates&workDir=hexo&branch=master" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div><br>

更多内容请参见 [CloudBase Framework 文档](https://docs.cloudbase.net/framework/index)。


