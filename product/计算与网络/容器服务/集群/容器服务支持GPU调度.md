## 容器服务支持GPU调度

### 简介
如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持GPU功能，通过该功能可以帮助您快速使用GPU容器。如需要开通GPU功能，您可以[提交工单](https://console.qcloud.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1CCS&step=1)进行申请。

### 使用指南
#### 第一步：在集群中添加GPU节点
添加GPU节点有两种方法：
**方法1：新建GPU云主机**
![][1]
选择GPU机型
![][2]
选择GPU的操作系统，并完成创建。

**方法2：添加已有GPU云主机**
选择GPU的节点
![][3]
选择GPU的操作系统，并完成添加
![][4]

#### 第二步：创建GPU服务的容器
您可以直接通过控制台创建服务时选择容器占用的GPU的个数。
![][5]

或者你通过应用或kubectl命令创建，在YAML文件中添加GPU字段
![][6]

### 注意事项
1. 仅在集群kubernetes版本大于1.8.*中支持使用GPU调度。
2. 当前GPU仅支持Centos系统，请留意您的集群的操作系统。
3. 容器之间不共享GPU，每个容器可以请求一个或多个GPU。无法请求GPU的一小部分。
4. 建议搭配亲和性调度来使用GPU功能。



[1]: https://main.qcloudimg.com/raw/be839f6e431eb74d2b1cea2b4d785209.png
[2]: https://main.qcloudimg.com/raw/980efc42700803ce25fedfc8c692cafe.png
[3]: https://main.qcloudimg.com/raw/83701fb1644bd2be8f7adf408fff9ef8.png
[4]: https://main.qcloudimg.com/raw/72dd3a0c581e9157a51e09f4c3f1c058.png
[5]: https://main.qcloudimg.com/raw/a768a0610894587528573f959277ab9f.png
[6]: https://main.qcloudimg.com/raw/2f2b3a751fd4bc0a3d443d7495fb1050.png