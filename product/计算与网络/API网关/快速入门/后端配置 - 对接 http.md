# API网关后端对接公网http资源

配置说明：
1）后端对接 http 时，需要选择您的后端类型为 http 或 https。

2）输入后端地址，以 `http://` 或 `https://` 开头，不包括后面的路径，例如 `http://api.myservice.com` 或 `http://108.160.162.30`。

3）输入后端路径以 / 开头，如 `/path` 或 `/path/{petid}`。

4）选择请求方法，前后端选择的请求方法可不一致。

5）设置后端超时时间。

6）设置映射前端的后端参数。

7）单击【完成】。
![后端配置](https://i.imgur.com/pQfgDqp.png)

# API网关后端对接VPC内资源

## API网关后端对接VPC内的CLB资源

当用户在配置后端对接服务为VPC内的CLB时，前端配置与其他API配置方法相同，后端配置方法如下：

1、在后端配置中需要先选择所需对接的VPC：

![](https://main.qcloudimg.com/raw/15e6d1daba72708d28747fa38ad1dcfd.png)

2、选择了您资源所在的VPC后，选择VPC内资源为CLB。目前API网关仅支持对接VPC内的CLB，后续还会陆续支持VPC内的其他云资源

![](https://main.qcloudimg.com/raw/0be3289e9aa42e8cef8bf0062a1a00bf.png)

3、当您选择后，在后端地址处填写 http://vip+port 或https://vip+port， 这里根据您填写的不同我们发往CLB的请求会分别为http请求或https请求。此处的vip是CLB的vip，您可在应用型内网CLB的基本信息中查询到。

![](https://main.qcloudimg.com/raw/dda0cba1faf5a0276c9dab5dff1e75f5.png)


4.1、若您选择的是HTTP/HTTPS的CLB监听类型，在后端路径配置中，需要将后端路径配置为用户在CLB中监听器中配置的路径，如下图：

此图为CLB中监听器配置的域名及路径

![](https://main.qcloudimg.com/raw/0343ecb570624f0c71f11e3ca0805a63.png)

此处为API网关中的后端路径，需要和CLB中的路径一致。

![](https://main.qcloudimg.com/raw/4637b8ae237e84dc3632ee1a5abf36f4.png)


此外，还需要在常量参数处配置一个名为host的参数，放在header中，参数值为CLB监听器中配置的域名。

![](https://main.qcloudimg.com/raw/d1d6bb3a99344099385dc8b19ee23386.png)


4.2、若您选择的是TCP/UDP的CLB监听类型，在后端配置中，需要将后端路径配置为CLB后端挂载CVM中业务所需的路径。

另外，若您在CVM中配置了host校验，则如同使用七层监听器一样，需要在常量参数中配置名为host的参数，根据您自身的业务选择所需放置的地址。


后续的配置与其他的API配置相同。


**注意**：当后端对接CLB时，需要将后端挂载的CVM上的安全组放通100.64.0.0/10，9.0.0.0/8网段。
