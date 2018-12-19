您可以在 CDN 控制台中接入域名，享受腾讯云 CDN 为您提供的加速服务，具体操作步骤如下。

## 第一步：添加域名
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧【域名管理】菜单，选择【添加域名】。
![](https://mc.qcloudimg.com/static/img/b1c4623293ce5e4600bd905d5a795622/addhost.png)
进入添加域名页面，您可以在此完成域名的相关配置。
![](https://mc.qcloudimg.com/static/img/4a91aee865755eb8a6b3e2fdfd672f88/adddomain.png)
1.在 **域名** 位置填入需要加速的域名。支持泛域名接入，如：```*.test.com```。支持域名批量接入，通过单击【添加】按钮最多可添加 10 个域名。域名需要满足以下条件：
+ 域名已经在工信部进行过备案
+ 域名尚未被接入过腾讯云 CDN

2.在 **所属项目** 处选择域名对应的项目，进行域名的分项目管理，这里的项目为腾讯云所有产品共享，您可以在 [项目管理](https://console.cloud.tencent.com/project) 中添加项目。

3.选择 **源站类型** 并填写 **源站设置**。源站类型可分为自有源和 COS 源。
+ 自有源：如果您已经拥有稳定运行的业务服务器（即源站），您可以通过自有源方式接入 CDN。源站本身无需做任何修改，仅通过 CDN 控制台接入流程，以及 DNS 配置即可享受加速服务。接入方式如下：
	1. **源站类型** 为源站 IP 或源站域名，**源站设置** 中填入的 IP 地址和源站域名需要满足以下条件。
	2. 若填入的为域名，则 **必须不能** 与访问域名（即接入的加速域名）一样。支持“域名:port”格式，端口号需 **大于0小于等于65535**。
	3. 若填入的为 IP，可填入多个 IP，支持“IP:port”格式，端口号 **大于0小于等于65535**。当填入多个 IP 的时候，回源请求会依次轮流访问各 IP。
	4. 填入的 IP 不能是内网 IP。

+ COS源：若您的业务服务器能力有限，想使用腾讯云 [对象存储](https://cloud.tencent.com/product/cos.html)，或您已经使用了腾讯云的对象存储服务，您可以直接使用 COS 源接入方式，将域名接入 CDN。接入方式如下：
	1. **源站类型** 为对象存储（COS），您可通过下拉菜单或输入关键字选择 Bucket 的域名。
	2. 若对应项目下无存储桶，您需要登录 [COS 控制台](https://console.cloud.tencent.com/cos) 创建存储桶（如何创建？请查阅 [创建存储桶](https://cloud.tencent.com/document/product/436/6245#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6)）。
	3. 选择了存储桶作为源站后，您可以在 [COS 控制台](https://console.cloud.tencent.com/cos) 对源站内容进行管理。
	![](https://mc.qcloudimg.com/static/img/29c2831770c54390c8173fdcd8a00eee/addhostcos.png)

4.选择加速服务业务类型及基础配置。
![](https://mc.qcloudimg.com/static/img/1cb32d26230380e8b22cc4f6663042ad/speedset.png)
**业务类型** 选择，决定了域名调度的资源平台，不同资源平台加速配置存在一定差异，请选择与您业务相匹配的业务类型：
-  静态加速：适用于电商类、网站类、游戏图片类静态资源加速场景。
-  下载加速：适用于游戏安装包、音视频原文件下载、手机固件分发等场景。
-  流媒体点播加速：适用于音视频点播加速等场景。
-  流媒体直播加速：适用于直播、互动直播下行加速等场景。

**基本配置**：CDN 为您提供了过滤参数开关，您可以根据业务需要，控制是否对用户请求 URL 中 **“?”** 之后的参数进行过滤。您可以利用过滤参数灵活的进行版本控制，或对资源进行带有 Token 的鉴权。详情请查看 [过滤参数配置](https://cloud.tencent.com/doc/product/228/6291)。

**缓存过期配置**：缓存过期配置是指 CDN 加速节点在缓存您的业务内容时遵循的一套过期规则。详情请查看 [缓存过期配置](https://cloud.tencent.com/doc/product/228/6290)。

5.单击【提交】完成添加域名操作。
![](https://mc.qcloudimg.com/static/img/c3ff6aae83f3b19b242f859df32ab7bd/addok.png)
## 第二步：配置 CNAME
添加成功的域名，在域名管理页面，可以查看到 CDN 为您的域名分配的加速 CNAME，您需要前往接入域名的 DNS 服务商（如 Dnspod）处，为此域名添加一条 CNAME 记录，待 **DNS 配置生效后**，即可进行加速服务。具体配置方法请查阅 [CNAME 配置](https://cloud.tencent.com/doc/product/228/3121)。