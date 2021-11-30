[Next.js](https://nextjs.org/) 是一款 Vercel 推出的 React 框架。

代码示例：[Next.js](https://github.com/TencentCloudBase/cloudbase-templates/tree/master/react-hello-world)

## 第 1 步：初始化项目

使用 [create-react-app](https://zh-hans.reactjs.org/docs/create-a-new-react-app.html) 命令行初始化一个项目：

```sh
npx create-react-app react-hello-world
```

## 第 2 步：发布项目

安装并登录 CloudBase Framework，在项目根目录下运行：

```sh
cloudbase framework deploy -e <your-env-id>
```

或单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-templates&workDir=react-hello-world&branch=master" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div><br>

更多内容请参见 [CloudBase Framework 文档](https://docs.cloudbase.net/framework/index)。


