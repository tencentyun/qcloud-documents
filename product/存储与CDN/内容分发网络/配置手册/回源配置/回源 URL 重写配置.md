## 配置场景

若您需要将回源请求 URL 修改为与源站匹配的 URL，腾讯云 CDN 为您提供了回源 URL 重写配置功能。

>! ECDN 域名暂不支持此功能配置。


## 配置指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择【域名管理】，单击域名操作列的【管理】，进入域名配置页面，切换 Tab 至【回源配置】，即可找到【回源 URL 重写配置】。
![](https://main.qcloudimg.com/raw/5f6bd6d64b3936b559df390c8b5e855d.png)



### 新增规则

您可按需添加重写规则，单击【新增规则】：
<img src="https://main.qcloudimg.com/raw/06701590fc240a68a7854b11cf722035.png" style="height:300px"/>


**配置约束**

- 单个域名至多可添加100条重写规则。
- 多条规则支持调整优先级：底部优先级大于顶部。
- 待重写回源 URL：以 `/` 开头，默认为前缀匹配，支持通配符 `*` 匹配（例如：/test/\*/\*.jpg）。若指定文件目录，不能以“/”结尾（例如：/test）。如需全路径匹配，可在上方匹配设置中勾选开启，开启后将不支持通配符`*` 。
- 目标回源 Host：默认为当前域名，可修改，不包含 `http://` 或 `https://` 头。
- 目标回源 Path：以 `/` 开头（例如：/newtest/b.jpg），通配符 `*` 可通过 `$n` 捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg）。若指定文件目录，不能以“/”结尾（例如：/test）。
- 通配符 `*` 最多可输入5个，捕获占位符 `$n` 最多可输入10个。
- 不支持提交中文内容，目标回源 Host 不可超过250个字符，其他输入框中的内容长度不可超过1024个字符。



## 配置示例：

若加速域名`www.test.com`的 **回源 URL 重写配置** 如下：
![](https://main.qcloudimg.com/raw/b0e22164d86b86617c4e90aed020f5f1.png)

如上配置，则实际回源情况如下：
- 回源请求 `www.test.com/images/2.jpg`，命中第2、3、4条规则，则底部优先级最大，实际回源请求为 `www.test.com/index.html`。
- 回源请求 `www.test.com/images`，命中第3条规则，则实际回源请求为 `www.test.com/goodboy.html`。
- 回源请求 `www.test.com/images/1.jpg`，命中第1、2、3、4条规则，底部优先级最大，实际回源请求为 `www.test.com/index.html`。
