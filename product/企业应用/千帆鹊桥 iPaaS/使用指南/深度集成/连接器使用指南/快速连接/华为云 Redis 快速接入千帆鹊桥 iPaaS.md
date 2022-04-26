## 操作场景
iPaaS Redis 连接器支持 Redis 单点模式、哨兵模式、Cluster 集群模式的连接及常用操作。
本文以 Redis 单点模式为例，介绍主流云厂商 Redis 产品的接入流程。


## 前期准备
您需要先开通 Redis，并配置好外网访问规则和公网访问。

###  购买 Redis 实例

1. 购买 [分布式缓存服务 Redis](https://support.huaweicloud.com/usermanual-dcs/dcs-ug-0312003.html)。
![image-20220407111710317](https://qcloudimg.tencent-cloud.cn/raw/6fae405c9ec28cb4b822140ff2ab1442.png)
2. 创建实例时，提示“当前版本不支持安全组，请创建完成后配置白名单”，因此无需绑定安全组。
![](https://qcloudimg.tencent-cloud.cn/raw/6d7b57492cd60f1a261edbc2187c131b.png)

### 配置外网访问
#### 购买云服务器

<dx-alert infotype="explain" title="DCS 实例支持公网访问吗？">
- 华为云 DCS-Redis 只有3.0实例支持公网访问，Redis4.0和 Redis5.0实例不支持绑定弹性IP，无法通过公网访问，但是华为云官网目前Redis3.0已经下架，只能购买Redis4.0和Redis5.0实例且iPaaS处于华为云的外部需要外网访问，所以这里采用 Nginx 实现公网访问Redis 4.0/5.0实例的访问，也可参考华为云文档 [使用Nginx实现公网访问Redis 4.0/5.0的单机/主备/Proxy集群实例](https://support.huaweicloud.com/bestpractice-dcs/dcs-bp-0514001.html)。
- [华为云常见问题 >>](https://support.huaweicloud.com/dcs_faq/dcs-faq-0427001.html)
</dx-alert>


1. 购买与华为云 Redis 处于同一可用区同一 VPC 下内网互通的有外网的云服务器[](id:method2)。
可参考 [华为云 ECS 购买指引](https://support.huaweicloud.com/qs-ecs/zh-cn_topic_0163540195.html)。
2. 登录服务器，部署 Nginx。

#### 安装 Nginx
>?本文以云服务器操作系统为Centos7.x为例进行安装，不同操作系统命令稍有不同。

1. 执行以下命令，添加 Nginx 到 yum 源。
 ```
sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
```
2. 添加完之后，执行以下命令，查看是否已经添加成功。
```
yum search nginx
```
3. 添加成功之后，执行以下命令，安装 Nginx。
```
sudo yum install -y nginx
```
4. 执行以下命令安装 stream 模块。
```
yum install nginx-mod-stream --skip-broken
```
5. 启动 Nginx 并设置为开机自动运行。
```
sudo systemctl start nginx.service
sudo systemctl enable nginx.service
```
![image-20220407131842236](https://qcloudimg.tencent-cloud.cn/raw/f38cfb0f54acdf9dc64e1eba72e7c812.png)
6. 在本地浏览器中输入服务器地址（公网 IP 地址），查看安装是否成功。
如果出现下面页面，则表示安装成功。
![image-20220407131842236](https://qcloudimg.tencent-cloud.cn/raw/f38cfb0f54acdf9dc64e1eba72e7c812.png)

#### 修改 Nginx 配置文件
1. 打开并修改配置文件[](id:method1)。
>?proxy_pass 参数配置值为同一 VPC 下的 Redis 实例的 IP 地址，具体可从缓存实例详情页面的“连接信息”区域获取。
>
执行 `vi /etc/nginx.conf ` 打开配置文件。
配置示例如下，在 proxy_pass 中配置 Redis 实例连接地址。
```
stream {
    server {
        listen 8080;
        proxy_pass 192.168.0.6:6379;
    }
    server {
        listen 8081;
        proxy_pass 192.168.0.6:6379;
    }
}
```
- 重启 Nginx，并查看 Nginx 端口状态。
![image-20220407133338082](https://qcloudimg.tencent-cloud.cn/raw/563c8950bad1ba7a2fcd257b659c2a09.png)


### 设置安全组允许 iPaaS 访问

在 [ECS 实例控制台](https://console.huaweicloud.com/ecm/?agencyId=344eb50173f9430489ff1be6c4769e54&region=cn-south-1&locale=zh-cn#/ecs/manager/vmList)，修改 ECS 安全组配置，配置允许 iPaaS 访问。
>!若需配置指定的 iPaaS 出口 IP 访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
>
![](https://qcloudimg.tencent-cloud.cn/raw/4e399b110eb0104d8d3705fa546d288f.png)

## 接入配置
配置鹊桥 iPaaS Database 连接器连接属性的步骤如下：

1. 在 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择**Redis连接器**相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/865f5d010b10fd5084f3c02d121e9d48.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/b1a4c023f49bc1192b8c7b1a4347dc68.png)
4. 填写完连接器配置参数后，单击**测试连接**，测试连通性，测试成功后，会出现”连接配置正确“的提示，保存连接器配置即可，失败根据提示来重新填写对应信息。
 - Redis连接模式：此处选择 Noncluster 模式
 - 地址：填写 [配置外网访问中创建的ECS的外网IP](#method2)
 - 端口号：填写 [修改 Nginx 配置文件](#method1) 中 proxy_pass 设置的 listen 端口
 - 密码：填写购买数据库时的密码
![](https://qcloudimg.tencent-cloud.cn/raw/7b736e3781c8d4d65fb2f615a58bfab3.png)
5. 其他相关配置可参考 [Redis 连接器使用指南](https://cloud.tencent.com/document/product/1270/55479)。


