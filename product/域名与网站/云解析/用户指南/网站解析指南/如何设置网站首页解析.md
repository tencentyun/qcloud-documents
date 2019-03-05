设置网站首页解析，需要设置子域名www和@的A记录类型解析，例如一级域名是qlcoud.com，指向IP为183.60.118.195：

## 1. 设置 cloud.tencent.com 解析

![](https://mccdn.qcloud.com/static/img/c1aa0b88e7ad1f6b571ed14ad7224667/A-1.png)

1.1 主机记录处填子域名www。
1.2 记录类型为A。
1.3 线路类型（默认为必填项，否则会导致部分用户无法解析）。
1.4 记录值为一个iPv4地址地址，例如：183.60.118.195I。
1.5 TTL为缓存时间，数值越小，修改记录各地生效时间越快，默认为10分钟，即600秒。

## 2. 设置 qcloud.com 域名解析

主机记录直接留空或者填写一个@，记录类型为A，记录值同为183.60.118.195。

## 3. 其他
也可以直接使用快速设置添加网站解析。

#### 3.1 进入域名的记录管理页面，点击【新手快速设置】。
![](https://mc.qcloudimg.com/static/img/23084c8b6865d15ca8e3941a5e47778e/0.png)

#### 3.2 选择【网站解析】。
![](https://mc.qcloudimg.com/static/img/3653431d2e84fe18100c9faf1a67d7be/1.png)

#### 3.3 填入主机IP，点击【确定】。
![](https://mc.qcloudimg.com/static/img/c6f422d44cbf1b540f19b9ed31fda0f6/2.png)

#### 3.4 添加完成后，将看到www和@的A记录解析已经设置完成了。
![](https://mc.qcloudimg.com/static/img/acc5e2775b0f73182a4243a2c13f54e7/3.png)
