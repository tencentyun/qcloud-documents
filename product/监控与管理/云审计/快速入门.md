您可以通过腾讯云控制台快速了解云审计服务。通过控制台，您可以查看操作记录，创建一个跟踪集并编辑它的存储位置，还可以对已创建的跟踪集进行删除操作，以及关闭跟踪集记录日志。

 
## 注册与登录
- 如果您还没完成腾讯云账户的注册，请先 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F%3FfromSource%3Dgwzcw.184926.184926.184926%26gclid%3DEAIaIQobChMIoaGVwcT21gIVFSNoCh3VxAi-EAAYASAAEgId7PD_BwE)，注册完成后您需要进行实名认证，具体操作可参考 [实名认证指引](https://cloud.tencent.com/document/product/378/3629)。
- 如果您已注册腾讯云账户，并进行了实名认证，可直接 [登录腾讯云](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fcloud.tencent.com%2F%3FfromSource%3Dgwzcw.184926.184926.184926%26gclid%3DEAIaIQobChMIoaGVwcT21gIVFSNoCh3VxAi-EAAYASAAEgId7PD_BwE)， 
 单击【产品】>【管理工具】>【云审计】，进入云审计页面。
 
##  查看操作记录
### 列表
 1. 登录云审计控制台，单击左侧导航【操作记录】，进入操作记录页面。
![](//mc.qcloudimg.com/static/img/2188705c1326c9924b2f9f1411c4fa7e/image.png)
 2. 在操作记录页面中，您可以根据用户名、资源类型、资源名称、事件源、事件 ID 、关键词或对应操作事件时间，获取相关的操作记录信息，您需要查询的操作记录将会以列表的形式展示出来，默认情况下只会展示两行，需要了解更多的记录可单击【点击加载更多】。
![](//mc.qcloudimg.com/static/img/a83e486ba997acc90fa737b157b92b52/image.png)

### 详情
您在获取到相关的操作记录列表后，如果想更进一步了解单个操作记录，可以单击该操作记录左侧的【▼】，您就会得到此操作记录的详情，包括访问密钥、区域、错误码、事件 ID 、事件名称、事件源、事件时间、请求 ID 、源 IP 地址、用户名。同时，可以单击【查看事件】，进行了解事件的相关信息。
![](//mc.qcloudimg.com/static/img/7d233b2d18e021e3902786251dbe7ec3/image.png)

## 使用跟踪集
1. **创建跟踪集**
 1. 登录云审计控制台，单击左侧导航【跟踪集】>【创建】，进入跟踪集创建页面。 
 ![](//mc.qcloudimg.com/static/img/2f1078b545ae3eee0520a43174e4dc3d/image.png)
>  **注意：**
>  只支持创建一个跟踪集。
 2. 在页面上填写跟踪集名称、存储位置等相关信息，单击【保存】即可。
![](//mc.qcloudimg.com/static/img/4c1eefa5c16049cd7d525d8510efc445/image.png)
2. **关闭或开启跟踪集记录日志**
 1.  当您创建成功一个跟踪集后，跟踪集的状态显示默认为 **开启** 。
 ![](//mc.qcloudimg.com/static/img/7d154b1ba8d7ea49e390b1c11167872b/image.png)
 
 2.  单击名称下面对应的跟踪集名称（**test**），进入以下界面。
 ![](//mc.qcloudimg.com/static/img/90a2e1140a1c465f949dd734ab6315e4/image.png)
 3.  单击右侧【日志记录】旁边的开关按钮即可 **关闭或开启** 跟踪集记录日志。
3. **编辑存储位置**
在  **关闭或开启跟踪集记录日志** 页面中单击【编辑】，即可对存储桶以及日志文件前缀进行编辑处理，然后单击【保存】即可。
 ![](//mc.qcloudimg.com/static/img/d52bf9a7432e03dc6c8147c98f82db70/image.png)
4. **删除跟踪集**
在  **关闭或开启跟踪集记录日志** 页面中单击【删除】即可。

## 更多资源

除了上面通过控制台了解并使用云审计，您还可以通过腾讯云 [开发者实验室中提供的实验](https://cloud.tencent.com/developer/labs/lab/10328
) 快速了解云审计的使用情况。