## 现象描述

域名接入 CDN 后部分参数加载不了。

## 可能原因

CDN 对应的加速域名开启了忽略参数的功能，该功能如果开启则请求到 CDN 节点后，会截取到没有参数的 URL 向源站请求，并且 CDN 节点仅保留一份副本，导致域名接入 CDN 后部分参数加载不了。

如果用户回源的很多资源是通过 URL 中“?”后面的参数来区分和获取，则需要关闭该参数。

## 解决思路

CDN 对应的加速域名关闭忽略参数的功能，则每个不同的 URL 都缓存不同的副本在 CDN 的节点上。

## 处理步骤
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择【域名管理】找到对应的域名配置， 查看【缓存配置】>【缓存键规则配置】的“忽略参数”项。
![](https://main.qcloudimg.com/raw/53ceba436ae110bd0dafef8bad72ceff.png)
[](id:step2)
2. 在【缓存键规则配置】对应规则的操作栏，单击【修改】，在弹出的“修改规则”框关闭忽略参数功能，然后单击【保存】。
![](https://main.qcloudimg.com/raw/f866bc80c384bc6daca649dbeb006fdb.png)
>?CDN 也提供了保留指定参数的忽略功能， 用户可以根据实际的业务需求选择使用。具体用法可参见 [缓存键规则配置](https://cloud.tencent.com/document/product/228/47671)。
