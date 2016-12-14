### 说明
本文旨在帮助大家了解如何快速创建一个容器集群内的nginx服务。

### 详细步骤

#### 创建容器服务集群
详情见基本教程中[集群基本教程](https://www.qcloud.com/document/product/457/6779)
#### 创建nginx服务
1.服务列表页点击"新建"按钮
![Alt text](https://mc.qcloudimg.com/static/img/11081690d6b480bd66c68a3c2982b04d/Image+007.png)

2.填写服务基本信息

服务名称只能由小写字母和数字组成，并由小写字母开头，此次填写nginx

服务运行集群需是运行中和集群内有可用主机的集群。
![Alt text](https://mc.qcloudimg.com/static/img/3b93df809521fdc3086e17629adf0bb2/Image+008.png)

3.填写容器基本设置

当前只能选择腾讯云镜像仓库的镜像

后续将可选择dockerhub官方镜像以及使用第三方镜像仓库创建服务，此处填写nginx和latest版本

![Alt text](https://mc.qcloudimg.com/static/img/c4f8632bce7f8ab2318f055fbfb7feea/Image+040.png)

4.填写高级设置

这里我们直接点完成，不填写高级设置
![Alt text](https://mc.qcloudimg.com/static/img/e3da911abb3387b3af845d01897e6266/Image+010.png)


5.创建完成，查看负载均衡器域名或VIP
![Alt text](https://mc.qcloudimg.com/static/img/755679dd56c950a86b7c18ff77472cb0/Image+013.png)

6.通过域名或VIP访问服务
![Alt text](https://mc.qcloudimg.com/static/img/e48f617e80dce415d83aff243d299268/Image+015.png)