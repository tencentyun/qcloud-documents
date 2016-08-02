## CDN配置--过滤参数

### 功能简介

过滤参数设置即指CDN节点将忽略用户的访问URL中"?"之后的参数。

### 配置说明

您可在CDN控制台的“域名管理”页面中点击域名右侧的“管理”进入“域名基本配置”页面中修改过滤参数配置。

![](//mccdn.qcloud.com/static/img/ddca74efca292f215c6a11bd5d608a3b/image.png)

**开启**过滤参数设置：则CDN节点将忽略URL请求中"?"之后的参数。如：用户第一次访问 http://www.test.com/2.jpg ，CDN 需直接回源访问数据并进行缓存。

  用户第二次访问 http://www.test.com/2.jpg?abc ，由于开启了“过滤参数设置”，CDN将不进行"?"后的参数匹配，所以不论"?"后面带的是什么参数，无需匹配即可命中CDN缓存 http://www.test.com/2.jpg

**未开启**过滤参数设置：则CDN节点将精确匹配用户的访问URL中"?"之后的参数，用户请求只有精确匹配"?"后面的参数，才能命中CDN缓存内容。如：用户第一次访问 http://www.test.com/1.jpg?abc ，CDN需回源访问数据并进行缓存。

  用户第二次访问 http://www.test.com/1.jpg?abc ，由于未开启“过滤参数设置”，故CDN节点会精确匹配"?"后的参数，匹配成功即命中CDN缓存。

  若用户第二次访问 http://www.test.com/1.jpg?efg ，由于"?"后的参数”efg”与CDN缓存的“abc”参数不匹配，则不命中CDN节点缓存，CDN需直接回源拉取信息。

**注意：使用FTP托管源的域名，已默认开启过滤参数设置**