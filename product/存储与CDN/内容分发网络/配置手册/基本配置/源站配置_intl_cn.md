您可以对域名的源站配置进行修改：
+ 支持自有源站、COS 源站相互修改。
+ 支持自有源域名配置热备源站，当回源请求至主源站错误（包括4XX、5XX错误码及 TCP 连接错误）后，会直接回源至热备源站。
+ 支持主备源站配置切换。

配置热备源站能够有效降低回源失败率，提升服务质量。
> **注意**：热备源站暂时不支持 HTTPS 回源，配置了热备源站的域名在配置证书时，请勿选择 HTTPS 回源。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【基本配置】，您可以看到 **源站信息** 模块，查看域名当前的源站配置。
![](https://mc.qcloudimg.com/static/img/7e218acca2ef3a4f146afe74e35bc129/host_info.png)

## 修改源站
您可以在 CDN 控制台中对主源站类型进行修改，支持自有源站、COS 源站相互切换。
> **注意**：仅支持修改用户自行接入的域名的源站，不支持修改 [对象存储](https://cloud.tencent.com/product/cos) 中 Bucket 自动创建的 CDN 加速域名的源站。

单击 **主源站** 右上角【修改】按钮，可对源站配置进行修改,在 COS 源与自有源站之间进行切换。
![](https://mc.qcloudimg.com/static/img/05bbce4f60fe74c679f218de44551407/origin_change.png)

## 添加热备源站
当回源请求至主源站错误（包括4XX、5XX错误码及 TCP 连接错误）后，会直接回源至热备源站。
您可以在【基本配置】中的 **源站信息** 模块，单击【添加热备源站】进行配置，热备源站仅支持配置为 **自有源站**，源站地址支持自有源域名。
![](https://mc.qcloudimg.com/static/img/04bcc3829b957f9f33e118b3076c817c/back_origin.png)

## 切换主备配置
配置好备用源站后，单击【主备切换】图标即可一键切换主源站/备用源站的配置。
![](https://mc.qcloudimg.com/static/img/1fd99aab6968ee200b94abb3e59bf056/switch.png)