## 单实例版wordpress服务
### 说明
1.确保您有可用集群，创建集群详情见：[集群基本教程](https://www.qcloud.com/doc/product/457/6779)
2.这里使用了tutum/wordpress Docker镜像来创建一个公开访问的Wordpress网站

### 创建wordpress服务

1.输入服务名称，选择运行集群

2.填写镜像tutum/wordpress，选择latest版本

3.填写端口映射

![Alt text](https://mc.qcloudimg.com/static/img/3b40d7cd09c0850569fa7967b7aaa362/Image+024.png)
![Alt text](https://mc.qcloudimg.com/static/img/27a0a00a151c5f5ebacffca5fc8f832a/Image+025.png)
### 访问wordpress服务
点击服务，查看服务外网ip，在浏览器输入ip地址即可访问
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)