CDN 为您提供了 IP 访问限频配置，通过对客户端 IP 在每一个节点每一秒钟访问次数进行限制，进行 CC 攻击的抵御。配置开启后，超出 QPS 限制的请求会直接返回514，设置较低频次限制可能会影响您的正常高频用户的使用，请根据业务情况、使用场景合理设置阈值。

## 配置指引

### 配置查看
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 单击【访问控制】选项卡，可以在 **IP 访问限频配置**模块进行配置。默认情况下，IP 访问限频配置为关闭状态。
![img](https://main.qcloudimg.com/raw/1c44d24f8c157868f3f20a9e17b62e5d.png)

### 修改限频配置
1. 在 **IP 访问限频配置**模块，开启 IP 访问限频开关，可设置 IP 访问阈值，建议您根据业务波动合理设置阈值。
![img](https://main.qcloudimg.com/raw/9fe680ad79b6806b33aaf46829097f58.png)
2. 单击【编辑】，可修改 IP 访问阈值。
![img](https://main.qcloudimg.com/raw/baeac4932ef1a1c88ada1357b4e226ed.png)

## 配置案例
若域名`www.test.com`的 IP 访问限频配置如下：
![img](https://main.qcloudimg.com/raw/268e6bf919bf4b0bfaed0ad88877ce68.png)
则：

- IP 为`1.1.1.1`的用户，在1s中请求了11次资源`http://www.test.com/1.jpg`，均访问至 CDN 加速节点 A 中的一台 server，此时在该 server 上产生11条访问日志，其中有一条因超出 QPS 限制，状态码为514。
- IP 为`2.2.2.2`的用户，在1s中请求了11次资源`http://www.test.com/1.jpg`，访问平均分布在多个 CDN 加速节点上，此时每一个加速节点均会正常返回内容。

