[Hexo](https://hexo.io/) 是一款基于 Node.js 的静态博客生成器。

代码示例：[https://github.com/TencentCloudBase/cloudbase-templates/tree/master/hexo](https://github.com/TencentCloudBase/cloudbase-templates/tree/master/hexo)

## 第 1 步：初始化项目

使用 hexo 命令行初始化一个项目：

```sh
npx hexo init hexo-hello-world
```

## 第 2 步：发布项目

安装并登陆 CloudBase Framework，在项目根目录下运行：

```sh
cloudbase framework deploy -e <your-env-id>
```

或点击下方按钮一键部署：

[![](https://main.qcloudimg.com/raw/67f5a389f1ac6f3b4d04c7256438e44f.svg)](https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-templates&workDir=hexo&branch=master)

更多内容请参见 [CloudBase Framework 文档](https://docs.cloudbase.net/framework/index.html)。
