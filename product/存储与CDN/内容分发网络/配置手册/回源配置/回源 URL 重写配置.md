## 配置场景

若您需要将回源请求 URL 修改为与源站匹配的 URL，腾讯云 CDN 为您提供了回源 URL 重写配置功能。



## 配置指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择【域名管理】，单击域名操作列的【管理】，进入域名配置页面，切换 Tab 至【回源配置】，即可找到【回源 URL 重写配置】。
![](https://main.qcloudimg.com/raw/c91b122b8c9a237c42110d2fb55ae2cc.png)



### 新增规则

您可按需添加重写规则，单击【新增规则】：
<img src="https://main.qcloudimg.com/raw/94ec103cd5ff0a60ab01385305b6fa1a.png" style="height:300px"/>


**配置约束**

- 单个域名至多可添加10条重写规则。
- 多条规则支持调整优先级：底部优先级大于顶部。
- 待重写回源 URL：以 `/` 开头，支持全路径匹配（例如：/test/a.jpg）和通配符 `*` 匹配（例如：/test/\*/\*.jpg），若指定文件目录，不能以“/”结尾（例如：/test）。
- 目标回源 Host：默认为当前域名，可修改，不包含 `http://` 或 `https://` 头。
- 目标回源 Path：以 `/` 开头（例如：/newtest/b.jpg），通配符 `*` 可通过 `$n` 捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg），若指定文件目录，不能以“/”结尾（例如：/test）。
- 通配符`*`最多可输入5个，捕获占位符`&n`最多可输入10个。
- 不支持提交中文内容，目标回源 Host 不可超过250个字符，其他输入框中的内容长度不可超过1024个字符。



## 配置示例：

若加速域名`www.test.com`的 **回源 URL 重写配置** 如下：
![](https://main.qcloudimg.com/raw/f1e680ed405b2b3d56702ffbf7c2715f.png)

则实际回源情况如下：

- 回源请求 `www.test.com/test/`，实际回源请求为 `www.test.com/newtest/` 。
- 回源请求 `www.test.com/test/a.jpg`，实际回源请求为 `www.newtest.com/newtest/a.jpg` 的内容。
