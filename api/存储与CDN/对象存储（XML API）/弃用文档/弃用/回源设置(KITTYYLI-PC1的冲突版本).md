当 Bucket 中没有用户请求文件时、或者需要对特定的请求进行重定向时，设置回源可以有效满足用户需求。回源设置主要用于数据的热迁移、特定请求的重定向等场景。

当前回源设置支持源站 IP 为电信、移动、联通、长宽的 IP 段，并有其他运营商支持不断新增中。

![](//mccdn.qcloud.com/img5697c84160bd9.png)

## 配置说明

进入 COS 管理控制台，左侧选择 Bucket列表，进入 Bucket 列表页面。选择需要配置回源的 Bucket，点击进入文件列表后，顶部切换选项卡 **基础配置** ：

![](https://mc.qcloudimg.com/static/img/dbddd755f6b782d8f9857d6e0feb9806/image.png)

找到 **回源配置** 点击 **编辑** 按钮：

![](https://mc.qcloudimg.com/static/img/b8717b14f1e94c920679655df98cc693/image.png)

功能状态：用户设置回源状态为开启后，必须填入需要回源的域名或者 IP 地址。

配置说明：目前只支持 HTTP 回源，不支持 HTTPS。填入地址时只需填入域名或 IP 地址，无需带 http:// 前缀。亦支持以 :[port] 方式填写对应的端口号，: 使用英文字符。

配置合法的回源设置地址，例如：

```
abc.qq.com
abc.qq.com:8080
123.2.4.8
123.2.4.8:8080
```

## 示例
用户创建新 Bucket 并开启 CDN 加速访问域名`Bucket-1250000000.file.myqcloud.com`。设置 Bucket 回源地址为` abc.qq.com` ，在源站存放图片 `http://abc.qq.com/1.jpg`。

首次访问 `http://bucket-1250000000.file.myqcloud.com/1.jpg` 时 COS 发现文件不命中，对客户端返回 302 HTTP 状态码并跳转至 `http://abc.qq.com/1.jpg` ，这时文件由源站提供给客户端保证访问，同时 COS 会在源站复制 `1.jpg` 并保存至 bucket 根目录中。

第二次起访问 `http://bucket-1250000000.file.myqcloud.com/1.jpg` 将在 COS 中直接命中根目录下 `1.jpg` 文件并返回。


