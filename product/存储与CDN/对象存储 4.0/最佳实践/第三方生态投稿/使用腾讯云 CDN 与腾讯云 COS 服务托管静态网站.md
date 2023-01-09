>?本文以国内的 COS 存储桶为例，请准备好一个已经备案了的域名，否则将无法自定义域名以及无法使用腾讯云 [CDN](https://cloud.tencent.com/product/cdn?from=10680) 服务。

大部分个人主页，hexo 和 hugo 等博客，以及静态化后的 wordpress 博客等都适用于此方法。

## 操作步骤
### 步骤1：创建腾讯云 COS 存储桶
进入 [腾讯云对象存储控制台](https://console.cloud.tencent.com/cos) ，单击**存储桶列表**，单击**创建储存桶**。
![](https://qcloudimg.tencent-cloud.cn/raw/f4f8547ad5e713e6d9587a4132b9d657.png)
我们以创建北京的存储桶为例，名称随意但创建后不可修改，最好方便自己记忆，访问权限设置请看下面的 Tips。

>?公有读私有写 和 私有读写的具体描述如下：
- 公有读私有写：任何人（包括匿名访问者）都对该存储桶中的对象有读权限，但只有存储桶创建者及有相应权限的账号才对该存储桶中的对象有写权限。
- 私有读写：只有该存储桶的创建者及有相应权限的账号才对该存储桶中的文件有读写权限，其他任何人对该存储桶中的对象都没有读写权限。

由于 COS 没有**用量封顶**这个设置项，故如果您选择公有读私有写则**可能被别人恶意刷取流量造成经济损失**。

**所以如果为了省事可以选择公有读私有写，但出于安全考虑建议选择私有读写。**
1. 单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/89dba8f5145a5f6df9c61f4313860460.png)
2. **高级可选配置**默认即可，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/6e192b974d843c32631f6b9007bf006a.png)
3. 确认无误单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/9b1a5fb5f62d747bff65f40a7778d240.png)

### 步骤2：上传网站源码到存储桶
1. 单击**上传文件**，将网站源码拖动到上传区域上传至存储桶，单击**上传**，等待完成。
![](https://qcloudimg.tencent-cloud.cn/raw/3edb418c4bfffdbed6a5c336fda4d335.png)
![](https://qcloudimg.tencent-cloud.cn/raw/deae2e0228beb46cd9939c9b1cd977ec.png)

### 步骤3：配置腾讯云 COS 存储桶
1. 单击**基础配置** - **静态网站**，将静态网站功能打开，一般来说默认即可，也可以按需配置。
![](https://qcloudimg.tencent-cloud.cn/raw/6493c313794183a9c4f00333e51af73c.png)
2. 我们复制上图中的访问节点进行访问，如果您存储桶选择的是公有读私有写，那么您已经能访问到您的网站内容了，如果您选择的是私有读写，那么由于您使用浏览器的访问不属于 “ 3. 有相应权限的账号 ” ，所以您的访问会被拒绝，状态码为403，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/751cb35e4c1f82c31547762c7bcc25a6.png)

### 步骤4：添加腾讯云 CDN 服务（二选一）

<dx-tabs>
::: 直接在存储桶中配置自定义 CDN 域名
单击**域名与传输管理** - **自定义 CDN 加速域名**，**添加域名**。
![](https://qcloudimg.tencent-cloud.cn/raw/e130addb9d452cdf42da18a2b6be8efd.png)

输入域名，加速地域按需选择，源站类型选择静态网站源站，如果是私有读写存储桶的话开启**回源鉴权**，强烈建议配置 HTTPS 证书，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/0b752378b9467a14bde9860618f68040.png)
在[ DNSPod 控制台 ](https://console.dnspod.cn/dns/list )给域名添加 CNAME 解析，记录值为上图中的 **CNAME**。
![](https://qcloudimg.tencent-cloud.cn/raw/29f0a89f70db96cab0d14d735466885c.png)
这时我们发现提醒：当前存在域名开启了回源鉴权，但该存储桶未**开启 CDN 服务授权**，单击**添加 CDN 服务授权**。
![](https://qcloudimg.tencent-cloud.cn/raw/a8e8df5e87715d871104b6f3d6636061.png)
单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/6f09f8086eb59e42e696fd335ffd7c85.png)
:::
::: 在 CDN 控制台添加 CDN 域名
进入 [腾讯云内容分发网络控制台](https://console.cloud.tencent.com/cdn) ，单击**域名管理**，**添加域名**。
![](https://qcloudimg.tencent-cloud.cn/raw/b03e9bfc3b6210521c334a5faa0f93e8.png)
域名配置加速区域按需选择，填写好加速域名，加速类型为 CDN 网页小文件，IPv6 访问按需开启。
![](https://qcloudimg.tencent-cloud.cn/raw/730d792a79cec7effea79b29e005716e.png)
源站配置 类型选择 COS 源，回源协议选择 HTTPS ，选择之前的存储桶作为源站地址，选择静态网站，开启私有存储桶访问。
![](https://qcloudimg.tencent-cloud.cn/raw/d81d2ff6c21251cde2bffd1f86cc48c7.png)
如果没有添加授权单击**添加授权服务**，确定即可。
![](https://qcloudimg.tencent-cloud.cn/raw/9674ea61e86e3cfa30b0bdeb019713b0.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ce85fe76ba2f03b12eabbdbebdf8570a.png)
服务配置默认即可，按需修改。
![](https://qcloudimg.tencent-cloud.cn/raw/fe740874cb937f2c61ac69ce1cc46894.png)
为了防止有人恶意刷流量造成经济损失，建议开启用量封顶，确认提交。
![](https://qcloudimg.tencent-cloud.cn/raw/84050f1f29e2cf32f73b362588e700e3.png)
在[ DNSPod 控制台](https://console.dnspod.cn/dns/list)  给域名添加 CNAME 解析，记录值为下图中的 CNAME。
![](https://qcloudimg.tencent-cloud.cn/raw/1775fd3755c599faf73d5052443fdd04.png)

:::
</dx-tabs>

### 步骤5：配置腾讯云 CDN 服务
<dx-tabs>
::: 配置证书
单击**管理**
![](https://qcloudimg.tencent-cloud.cn/raw/83ae785e62b129e3436dd690640df17f.png)
5.1 配置 SSL 证书  并开启强制跳转 （强制跳转按需开启，通常建议开启 HTTP --> HTTPS ）
>?强烈建议网站配置 HTTPS。

首先单击 HTTPS 配置，配置证书。
![](https://qcloudimg.tencent-cloud.cn/raw/8cd2f91e3db605d3ec1880bd1a6cfc6e.png)
如果已经在腾讯云申请了 SSL 证书则直接添加。
![](https://qcloudimg.tencent-cloud.cn/raw/58d33d14ac49389f8bcea211ac2709d2.png)
如果没有在腾讯云申请 SSL 证书那么将自己在其他地方手动申请的 SSL 证书添加。
![](https://qcloudimg.tencent-cloud.cn/raw/dc9c65833c6f61d6176a6a6685492fd0.png)
然后开启强制跳转，**跳转类型设置**为 HTTP -> HTTPS ，**跳转方式**选择301跳转，携带头部为 是（可选）。
![](https://qcloudimg.tencent-cloud.cn/raw/edbc9dbae3ffee84543f95d9dca69ae7.png)
:::
::: 节点缓存过期配置
首先单击**缓存配置**，进行节点**缓存过期配置**
![](https://qcloudimg.tencent-cloud.cn/raw/4ad1ecab3c8019c6cc7454dc41ece180.png)
由于我们托管的是静态网站，所以应该配置所有的动态文件不缓存。
![](https://qcloudimg.tencent-cloud.cn/raw/f182822d0bad74fa19a844c1a9c50814.png)
如果网站更新比较频繁，那么建议将更新频繁的**文件后缀**设置较短的缓存时间，比如博客站就可以将 HTML 后缀的文件设置1天或者更短的缓存时间。
![](https://qcloudimg.tencent-cloud.cn/raw/53fa6eb37e3c2bc41cc5c26a89daff2b.png)
对于那些几乎不会变动的文件我们就可以设置一个较长的缓存时间，比如图片文件一般人是不会更新的，我们就可以将图片文件设置180天或者更长的缓存时间（如果文件经常变化的则不建议）。
![](https://qcloudimg.tencent-cloud.cn/raw/18bdac501aebc6c51f6922f658fa703f.png)
剩下的文件我们按照默认设置为缓存30天即可。根据您的实际需求，无论是1秒还是4629天（留意：最多只能缓存4629天）。
![](https://qcloudimg.tencent-cloud.cn/raw/232d5de92091ba62f7aab5f7d3034fc3.png)
您也可以进行更高级的配置；文件后缀就是对某个或某几个后缀的所有文件进行配置，文件目录就是对某个或某几个目录进行配置，全路径文件就是单独对某个文件或某些文件进行配置（支持通配符 * ），首页就是单独对 index.html 进行的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/dcab88518fef38f699b1581f9897ca9e.png)
然后我们需要知道 越下面的缓存规则 权重越高 优先级越高 ，所以我们要给上面的配置排个序，主要是将全部文件的缓存配置放到最上面，其他的就是按照您的具体需求进行排序了。
单击**调整优先级**，进行拖动排序，单击**保存**。

![](https://qcloudimg.tencent-cloud.cn/raw/e2584f774edab47b783254cb6085c4e6.png)
比如我配置的规则如下：
![](https://qcloudimg.tencent-cloud.cn/raw/163be1d64d683c5692d9a3d155e98b5d.png)
一般只需配置上述两项即可，如有更多需求请自行按需配置。
:::
</dx-tabs>


### 步骤6：访问网站
现在访问您的 CDN 域名，您就能访问到属于自己的网站。
