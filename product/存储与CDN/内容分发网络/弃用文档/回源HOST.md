## 什么是回源 Host
回源 Host 指明了加速节点在发起回源请求时，在源站访问的站点。请保证您配置的回源 Host 能够正常访问，否则会导致回源失败，影响您的业务。您也可以根据自身业务情况配置自定义回源 HOST。
>?
> - 源站域名与回源 Host：在加速节点发起回源请求时，通过源站域名解析出源站服务器 IP，源站服务器上可能存在若干 Web 站点，回源 Host 指明了资源所在的站点。
> - 根据有关部门规定，源站为腾讯云 CVM 的加速域名，配置的回源域名需要在腾讯云备案。

## 配置指引
### 查看配置
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![域名列表](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 在基本配置页面最下方，可以看到回源域名配置信息。
![img](https://main.qcloudimg.com/raw/88420f34964c14d554b8f48b10304491.png)
默认情况下，子域名的回源 Host 为所配置的加速域名，泛域名回源 Host 为访问域名：
	- 若您接入的加速域名为 `www.test.com`，则此节点对此域名下资源发起回源请求时，Request HTTP Header 中 Host 字段的值为 `www.test.com`。
	- 若您接入的加速域名为泛域名，如 `*.test.com`，若访问域名为 `abc.test.com`，则回源 Host  为 `abc.test.com`。

### 修改回源 HOST
在回源配置信息处，单击【编辑】，可以对回源 Host 配置进行调整。**仅支持自有源站回源 Host 编辑，COS 源站回源 Host 默认为存储桶对应的额外网域名，不可修改。**
![img](https://main.qcloudimg.com/raw/43f9b9cc952c77169d8eecda4f8fa6df.png)

## 配置案例
用户访问域名为`www.test.com`，源站配置为域名`origin.test.com`，`origin.test.com` 对应的 A 记录为`1.1.1.1`。
用户请求为：`http://www.test.com/1.jpg`。
1. 若配置如下：
![img](https://main.qcloudimg.com/raw/43f9b9cc952c77169d8eecda4f8fa6df.png)
默认情况下，回源 HOST 为加速域名，回源时实际请求发往`1.1.1.1`。
   获取的资源为：`http://www.test.com/1.jpg`。
2. 若配置如下：
![img](https://main.qcloudimg.com/raw/7b3821894aafae537a818ab862129cda.png)
回源 HOST 为`origin.test.com`，回源时实际请求发往`1.1.1.1`。
获取的资源为：`http://origin.test.com/1.jpg`。
