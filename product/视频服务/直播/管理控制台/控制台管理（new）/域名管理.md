![](https://main.qcloudimg.com/raw/b8b296e72d182446a11b6cf91bac79c4.svg)

### 第一步：域名备案

控制台进行域名提交管理前，需对域名进行备案，详情请查看 [域名备案](https://cloud.tencent.com/product/ba) 和 [域名备案和配置常见问题](https://cloud.tencent.com/document/product/267/30010) 文档。

>!域名完成备案以域名服务提供商的拟定时间为准，若已收到工信部备案完成的通知，请耐心等待1小时 - 24小时，待 [工信部备案查询网站](http://www.beian.miit.gov.cn) 可查询到您的备案域名，即可在腾讯云直播添加已备案的域名。

### 第二步：添加域名

在视频直播菜单栏内选择【域名管理】，在域名管理页面可以看到已创建域名、类型、状态、添加时间和操作。
可添加和管理的域名类型有播放域名和推流域名两种。
![](https://main.qcloudimg.com/raw/dc1bae6af06b7fc09dac4af3f378f420.png)


- **添加播放域名**
单击【添加域名】，输入域名，并选择域名类型为【播放域名】，单击【提交】即可。
>! 域名的位数限制为29位，暂不支持大写的域名，请输入不超过29位的小写域名地址。
>
![](https://main.qcloudimg.com/raw/6071c0aa2fee29a467c96509f8fce2c9.png)

-  **添加推流域名**
单击【添加域名】，输入域名，并选择域名类型为【推流域名】，单击【提交】即可。
>! 域名的位数限制为29位，暂不支持大写的域名，请输入不超过29位的小写域名地址。
>
![](https://main.qcloudimg.com/raw/0ae9e626ff819deefca4f7dbc4fa81c5.png)


添加播放域名后如果出现 CNAME 未配置的情况，请参考 [CNAME 配置](https://cloud.tencent.com/document/product/267/19908) 里的内容对 CNAME 进行配置。
![](https://main.qcloudimg.com/raw/911b09bc98388c3c93e0a0433a2c8d08.png)



###  第三步：查看和配置信息
-  **配置播放域名**
单击【管理】，查看域名基本信息和播放设置。
![](https://main.qcloudimg.com/raw/bae2c64b74762252db43a951af1f41f2.png)
单击【播放设置】，可以查看 RTMP、FLV、HLS 格式的播放地址。
![](https://main.qcloudimg.com/raw/a833ed0a0d21cb0af95c871e6b6f99c9.png)

- **配置推流域名**
单击【管理】，查看域名基本信息和推流配置。
![](https://main.qcloudimg.com/raw/7ed36f55e5367cb1369c3547f1e6db97.png)

单击【推流配置】，可在设置页面单击【生成推流地址】，则会在推流地址处显示出推流的地址。
>!  Stream name（流 ID）仅支持英文字母、数字和符号，不支持中文输入。

在页面最下方可查看推流地址的 PHP 和 Java 示例代码：
![](https://main.qcloudimg.com/raw/3ccb6118abc4f4e4ed49d6906a5adf74.png)


### 第四步：禁用、启用和删除域名
禁用域名后该域名无法访问，重新启用后可正常访问。播放域名和推流域名操作相同。

- **禁用域名**
在域名管理页，单击需要禁用的域名右侧【禁用】，弹框中单击【确认】禁用该域名即可。
![](https://main.qcloudimg.com/raw/07c5ea78118b2cc3d9e08e201f651ca6.png)


- **启用域名**
在域名管理页，单击需要启用的域名右侧【启用】即可。
![](https://main.qcloudimg.com/raw/f80ed962c0fbb18e7248d9baaead7da6.png)

- **删除域名**
在域名管理页，单击需要删除的域名右侧【删除】即可。
![](https://main.qcloudimg.com/raw/b12dfc80839851784176c5380130296c.png)

