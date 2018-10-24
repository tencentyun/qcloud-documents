CDN 为您提供了过滤参数开关，您可以根据业务需要，控制是否对用户请求 URL 中 **“?”** 之后的参数进行过滤。您可以利用过滤参数灵活的进行版本控制，或对资源进行带有 Token 的鉴权。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【访问控制】，您可以看到 **过滤参数配置** 模块，设置是否过滤参数。
![](https://mc.qcloudimg.com/static/img/7599154d615d6c1132fd749bfdefe38e/filter.png)

### 使用默认配置
默认情况下，过滤参数的开关处于关闭状态，此时将不会忽略用户请求 URL 中 **“?”** 之后的参数。
1. 假设用户请求 URL 为： ```http://www.test.com/1.jpg?version=1.1``` 的资源，接收此请求的节点未缓存该内容，则会进行回源获取，并缓存至节点。
2. 假设用户再次请求 URL 为： ```http://www.test.com/1.jpg?version=1.1``` 的资源 ，此时节点已经存在该资源，则直接命中资源并返回给用户。
3. 在进行过步骤1后，假设用户请求 URL 为： ```http://www.test.com/1.jpg?version=1.2 ``` 的资源，此时由于过滤参数已经关闭，则无法全路径匹配内容，因此会再次回源进行资源的拉取。

### 开启过滤参数
当你开启了过滤参数配置时，此时将会忽略用户请求 URL 中 **“?”** 之后的参数。
1. 假设用户请求 URL 为： ```http://www.test.com/1.jpg?version=1.1 ``` 的资源，接收此请求的节点未缓存该内容，则会进行回源获取，并缓存至节点，由于用户开启了过滤参数，因此节点存放的资源URL为 ```http://www.test.com/1.jpg```。
2. 假设用户再次请求 URL 为： ```http://www.test.com/1.jpg?version=1.1``` 的资源，此时在节点实际查找的资源为 ```http://www.test.com/1.jpg```，节点已经缓存，因此会直接命中资源，并返回给用户。
3. 在进行过步骤1后，假设用户请求 URL 为： ```http://www.test.com/1.jpg?version=1.2``` 的资源，此时在节点实际查找的资源为 ```http://www.test.com/1.jpg```，节点已经缓存，因此会直接命中资源，并返回给用户。