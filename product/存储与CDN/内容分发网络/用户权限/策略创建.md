为方便用户更加细粒度的配置域名查询、管理权限，CDN 权限策略已全面完成升级，用户可通过自定义策略语句，实现域名级别的权限分配。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) ，单击【策略】菜单，即可进入策略管理页面，单击【新建自定义策略】：
![](https://main.qcloudimg.com/raw/6570c1642d59bf00b5dee346f48ddf0e.png)
2. 选择【按策略生成器创建】：
![](https://main.qcloudimg.com/raw/12a78b0a490d6cd95a4427b92710400f.png)
3. 在产品选框中选择【内容分发网络】，并选择需要授权的功能集合，若授权全读写权限，可勾选【All】选中全部服务，功能与控制台映射关系可查看 [Action 映射表](https://cloud.tencent.com/document/product/228/41867)。
![](https://main.qcloudimg.com/raw/16c968c01bb9811df5a6356f4a364928.png)
4. 在资源处填充需要授权的域名，`*`代表所有域名，完成配置后，单击【添加声明】并单击【下一步】，即可创建策略，将创建好的策略关联已有用户 / 用户组，即可进行授权：
![](https://main.qcloudimg.com/raw/0497f341d3ad51b56e07682aadc23ba8.png)

