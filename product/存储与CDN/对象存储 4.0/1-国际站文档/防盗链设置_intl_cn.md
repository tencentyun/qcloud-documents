## 简介

为了避免恶意程序使用资源 URL 盗刷公网流量或使用恶意手法盗用资源，给用户带来不必要的损失。腾讯云对象存储支持防盗链配置，建议您通过控制台的防盗链设置配置黑/白名单，来进行安全防护。

## 设置步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos4/index)，进入左侧菜单栏【Bucket 列表】，选择需要设置防盗链的存储桶（如 example），进入存储桶。 
   ![访问权限1](//mc.qcloudimg.com/static/img/b51d5a77d53c3416324ea3eb283c788c/image.png)
2. 单击【基础配置】，找到防盗链设置，单击【编辑】按钮进入可编辑状态。
   ![防盗链设置1](//mc.qcloudimg.com/static/img/3d76b7e130d8917a41c4b2b7e8b1a730/image.png)
3. 确认当前状态为开启，选择名单类型（黑名单或白名单），设置好相应域名，设置完成单击【保存】即可。
   ![防盗链设置2](//mc.qcloudimg.com/static/img/26a0d84534965325ca6902d7262181a8/image.png)

- 用户设置防盗链状态为开启后，必须填入相应的域名。
- 名单类型黑、白名单二选一：
  黑名单：限制名单内的域名访问存储桶的默认访问地址，若名单内的域名访问存储桶的默认访问地址，则返回403。
  白名单：限制名单外的域名访问存储桶的默认访问地址，若名单外的域名访问存储桶的默认访问地址，则返回403。
- 设置域名支持最多十条域名且为前缀匹配；域名、IP 和通配符 \* 等形式的地址；一个地址占一行，多个地址请换行。
  示例（仅作示例，无实际意义）：
  配置 www.example.com，可限制如 www.example.com/123、www.example.com.cn 等以 www.example.com 为前缀的地址；
  支持带端口的域名和 IP，如 www.example.com:8080、10.10.10.10:8080 等地址；
  配置 * .example.com，可限制如 a.b.example.com/123、a.example.com 等地址。
- 如果通过 CDN 域名加速访问，则优先执行 CDN 的防盗链规则，再执行对象存储服务的防盗链规则。

## 示例

APPID 为 1250000000 的用户创建了一个名为 example 的存储桶，并在根目录下放置了一张图片 1.jpg，COS 根据规则生成了一个默认访问地址 ：

```
example-1250000000.file.myqcloud.com/1.jpg
```

用户 A 拥有网站：

```
www.example.com
```

并将该图片嵌入了首页 index.html 中。
此时站长 B 持有网站：

```
www.fake.com
```

 想把这张图片放入他的网站中。由于不想付流量费用，他便直接通过：

```
example-1250000000.file.myqcloud.com/1.jpg
```

地址引用了这张图片，并放置到首页 index.html 。

为了避免用户 A 的损失，针对以上状况，我们提供两种开启防盗链的方式。

#### 开启方式一

 配置**黑名单**模式，域名设置填入 `*.fake.com`并保存生效。

#### 开启方式二

配置**白名单**模式，域名设置填入`*.example.com`并保存生效。

#### 开启前

访问 `http://www.example.com/index.html` 图片显示正常。
访问 `http://www.fake.com/index.html` 图片也显示正常。

#### 开启后

访问`http://www.example.com/index.html` 图片显示正常。
访问 `http://www.fake.com/index.html` 图片无法显示。