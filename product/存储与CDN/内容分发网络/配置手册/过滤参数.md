CDN 为您提供了过滤参数开关，您可以根据业务需要，控制在缓存时是否对用户请求 URL 中 **“?”** 之后的参数进行过滤。您可以利用过滤参数灵活的进行版本控制，或对资源进行带有 Token 的鉴权。
>?若您的资源 URL 中不同参数代表相同的内容，建议开启过滤参数，有效提升缓存命中率。

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧目录单击【域名管理】，进入管理页面。
2. 在列表中，找到您要编辑的域名所在行，单击操作栏中的【管理】。
 ![](https://main.qcloudimg.com/raw/18a3dd6931e3fe4ea109f971e5afe410.png)
3. 单击【访问控制】选项卡，在**过滤参数配置**模块，进行过滤参数配置。
 ![](https://main.qcloudimg.com/raw/77b13228a87729324cb0c27f6b17af3e.png)
>?若您的加速类型为下载、点播、直播，则过滤参数默认为开启状态，若您接入时加速类型选择为静态，过滤参数默认为关闭状态。

## 配置案例
CDN 在节点存储结构上缓存资源时，根据 cache_key 作为索引，来查找存储的资源。
1. 若配置如下：
 ![](https://main.qcloudimg.com/raw/989e3e911163345f523ac6567f134289.png)
 + 用户 A 请求 URL 为： `http://www.test.com/1.jpg?version=1.1` 的资源，节点存储资源时，对应的 `cache_key` 为 `www.test.com/1.jpg`，忽略了 "?" 之后的参数。
 + 用户 B 也请求 URL 为： `http://www.test.com/1.jpg?version=1.2` 的资源 ，也按照`cache_key`为 `www.test.com/1.jpg`查找资源，因此与用户 A 请求的为同一份内容，可直接命中。
2. 若配置如下：
 ![](https://main.qcloudimg.com/raw/cb67d1acee6ff68f06e7c33b2016d78c.png)
 - 用户 A 请求 URL 为： ```http://www.test.com/1.jpg?version=1.1``` 的资源，节点存储资源时，对应的 ```cache_key``` 为 ```www.test.com/1.jpg?version=1.1```，未忽略 "?" 之后的参数。
 - 用户 B 也请求 URL 为： ```http://www.test.com/1.jpg?version=1.2``` 的资源 ，按照```cache_key```为 ```www.test.com/1.jpg?version=1.2``` 来查找资源，未命中，因此会重新回源站获取对应内容，进行缓存。 
