## 单实例版wordpress服务
### 说明
1.确保您有可用集群，创建集群详情见：[集群基本教程](https://www.qcloud.com/doc/product/457/6779)
2.这里使用了tutum/wordpress Docker镜像来创建一个公开访问的Wordpress网站

### 创建wordpress服务
1.输入服务名称，选择运行集群
2.填写镜像tutum/wordpress，选择latest版本
3.填写端口映射
![Alt text](https://mc.qcloudimg.com/static/img/36d6ff6880bca5f8f4603c4531e1b842/%7BAC1A39EF-CC1F-4623-90F1-722E2178FB1F%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/0fd614e229b74e168cc3eb6d6d88cefb/%7B43D44BC2-2162-406D-9732-58B592903E50%7D.png)
### 访问wordpress服务
点击服务，查看服务外网ip，在浏览器输入ip地址即可访问
![Alt text](待补充)