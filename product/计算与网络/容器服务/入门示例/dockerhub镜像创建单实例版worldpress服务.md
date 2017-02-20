### 说明
WordPress是一个注重美学、易用性和网络标准的个人信息发布平台。作为一款免费的开源软件，它的图形设计在性能上易于操作、易于浏览；在外观上优雅大方、风格清新。

这里展示如何使用tutum/wordpress Docker镜像来创建一个公开访问的Wordpress网站。

创建单实例版的wordpress仅供测试使用，该镜像中包含了wordpress所有的运行环境，直接拉取创建服务即可；但使用单实例版的wordpress不能保证数据的持久化存储，建议您使用自建的mysql或使用腾讯云数据库CDB来保存您的数据，详情请参考[CDB版的wordpress搭建](https://www.qcloud.com/document/product/457/7447)。

### 详细步骤
#### 第一步：创建集群
1.首先要拥有一个可运行容器的集群。如无集群新建一个集群，详情查看[新建集群](https://www.qcloud.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4)。


#### 第二步：创建wordpress服务

1.输入服务名称，选择运行集群。

2.填写镜像tutum/wordpress，选择latest版本。

3.填写端口映射。

![Alt text](https://mc.qcloudimg.com/static/img/27a0a00a151c5f5ebacffca5fc8f832a/Image+025.png)

4.点击【创建服务】完成配置。
### 访问wordpress服务
点击服务，查看服务外网IP，在浏览器输入IP地址即可访问。
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)
