用户可以在TencentHub中创建DevOps工作流，根据自己的业务选用相关组件自定义工作流程，一键启动，快速进行任务计算与处理，提升持续集成/持续交付效率。    
## 操作步骤：
### 1.创建仓库
登录腾讯云，进入到TencentHub控制台 [https://console.cloud.tencent.com/tencenthub](https://console.cloud.tencent.com/tencenthub)，点击左侧的【仓库管理】，在管理页面中点击左上角【新建】，创建一个新仓库。    

![](https://main.qcloudimg.com/raw/f9e70f59712a119b029fb31f82ea5431.png)    

填写仓库信息。根据业务填写相关信息，所有者可选择自己的账号或者所在的组织。仓库类型可选择public共有型或者private私有型。填写后点击【完成】    

![](https://main.qcloudimg.com/raw/1eecfc9df84d2d12d64a555c70454a10.png)    

在管理页面中会新增该仓库列表项，点击产品名，可进入到【我的仓库】，默认展示仓库信息。    

### 2.创建DevOps工作流
在我的仓库中选择【工作流】，在工作流管理界面上点击【新建】，进入到工作流编辑页面。  

![](https://main.qcloudimg.com/raw/a9a5ae0efc1eb34131f4c7c60e2404e7.png)    

点击“+”号可以创建stage, 每个stage下可以创建多个job处理单元，同时可以通过右侧编辑栏设置stage名称，选择串行/并行的job执行方式。     

![](https://main.qcloudimg.com/raw/1ce645a5a2f72fae98eb6e032811aa55.png)    

![](https://main.qcloudimg.com/raw/cec7cfe54e6447ab2e28cb173e870037.png)    

选中某个job,可以在右侧编辑栏中对job进行镜像选择与参数相关设置。    

![](https://main.qcloudimg.com/raw/5d34f6b2f3b81d1e40801fcc5693cc3d.png)    

在编辑页面中可设置全局环境变量，以Key-Value的形式作为传参量，可以供stage下各个job使用。     

![](https://main.qcloudimg.com/raw/66547da3250a137b1529285e60a63b98.png)    

![](https://main.qcloudimg.com/raw/e4f44d089803fdb2eccb2b1f85a2a976.png)     

工作流创建后点击左下方【完成】，整个devops工作流创建完毕。    

###  3. 运行DevOps工作流
在【工作流】中可看到遗传建的工作流列表。点击“立即执行”，运行DevOps工作流。    

![](https://main.qcloudimg.com/raw/59da734e73c26514fcf002958fa1e756.png)    

运行结束后，可在状态中看到最新工作流的运行结果，同时可展开工作流执行历史查看详细执行信息。    

![](https://main.qcloudimg.com/raw/424a689756fda626911aeeec9c9cca6b.png)     

查看每条执行历史，可进入工作流页面，查看详细日志输出。     

![](https://main.qcloudimg.com/raw/462b56e020e0c3c49f6c277f9a8d445d.png)     

