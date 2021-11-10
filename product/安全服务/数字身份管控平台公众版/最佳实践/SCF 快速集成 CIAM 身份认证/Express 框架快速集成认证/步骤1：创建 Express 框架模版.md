## 操作场景
通过 云函数 SCF 来完成创建 Express 框架模版(Auth)。
## 操作步骤
1.	登录 [Serverless 应用控制台](https://console.cloud.tencent.com/scf/list?rid=4&ns=default)，在左侧导航栏选择**函数服务**，进入函数服务页面。
2.	在函数服务页面，单击**新建**，进入新建页面。
![](https://qcloudimg.tencent-cloud.cn/raw/4a1e28c7586f98574250866c73d07eae.png)
3.	在新建页面，创建方式选择**模板创建**，在模糊搜索框中输入 CIAM，并选择 **Express框架模版(Auth)**，单击**下一步**，完成模版选择。
![](https://qcloudimg.tencent-cloud.cn/raw/fa65602cbdc550a648f70845515d3db9.png)	
4.	单击**完成**，即可创建函数，创建完成后即可在函数管理中看到函数配置信息。
5.	单击**函数代码**，下拉页面获取访问路径的地址，它会用于后续的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/6198933cbef14cba25c268d430a528d8.png)
5. 至此，您已经完成了 Serverless Express 框架模版(Auth)模板的创建，接下来只需要将函数代码中的初始化参数进行更新，就可以完成集成。初始化参数见下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ca97611adcd8c5495a9103903d38e7d7.jpg)
