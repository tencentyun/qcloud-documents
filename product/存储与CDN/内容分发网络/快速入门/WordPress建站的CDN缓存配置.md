## 使用 WordPress 建站的节点缓存过期配置建议 


- 后台登入地址 /wp-admin 目录下的资源，需要设置不缓存，否则会导致后台登入相关资源被缓存，登录出错。如果有其他接口相关的资源，同样需要设置不缓存。
- php;jsp;asp;aspx动态文件后缀的资源，需要设置不缓存（CDN 默认缓存规则）；
- html;js;css后缀文件更新较频繁，需要根据更新频率设置缓存时间。建议设置缓存时间7天，不设置强制缓存（若您需在缓存未过期场景下，主动更新 CDN 节点的缓存资源，可通过缓存刷新功能提前删除指定 URL 或目录的缓存）；
- 其余全部文件缓存30天（CDN 默认缓存规则）。

 

## 在 CDN 默认缓存规则的基础下，按如下操作新增规则 

1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)；
2. 单击左侧菜单内的**域名管理**，进入域名管理列表；
3. 选择需要配置的域名，单击**管理**进入域名配置页面；
4. 单击**缓存配置**，切换至缓存配置标签页，即可查看节点缓存过期配置；
![](https://qcloudimg.tencent-cloud.cn/raw/a89e125f5db6ae80a7bf7a62c26c9542.png)
5. 单击**新增规则**，类型为目录，内容为/wp-admin，缓存选项为不缓存，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/0e0b724d81d4a3bcdd511de60db4bdfe.png)
6. 单击**新增规则**，类型为文件后缀，内容为 html;js;css，缓存选项为缓存，缓存时间为7天，强制缓存为否，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/ec7e8d45f19ad999cc951278c6d31e6c.png)
7. 按照优先级顺序，底部优先级高于顶部，单击**调整优先级**，拖动"/wp-admin目录不缓存规则"规则调整至底部，使该规则优先级最高。
![](https://qcloudimg.tencent-cloud.cn/raw/f0bca7ad61377536303a26c14c5e52d2.png)
8. 调整完成后的缓存规则为：
 - /wp-admin 目录下的所有资源不缓存；
 - php;jsp;asp;aspx 文件后缀的资源不缓存；
 - html;js;css 文件后缀的资源缓存7天；
 - 其余全部文件缓存30天。
![](https://qcloudimg.tencent-cloud.cn/raw/f8ea1939723b36287ca854c68a7eef30.png)
