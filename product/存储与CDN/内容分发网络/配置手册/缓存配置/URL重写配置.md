## 配置场景

若您需要将实际访问的 URL 修改为与源站匹配的 URL，腾讯云 CDN 为您提供了访问 URL 重写配置功能。

您可通过自定义访问 URL 重写配置，将 URL 302 重定向到目标 URL。

## 配置指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择【域名管理】，单击域名操作列的【管理】，进入域名配置页面，切换 Tab 至【缓存配置】，即可找到【访问 URL 重写配置】。

默认情况下，访问 URL 重写配置为关闭状态：
![](https://main.qcloudimg.com/raw/d99843ee78a3c4d7a63059ffc7784970.png)


### 新增规则

您可按需添加重写规则，单击【新增重写规则】：
<img src="https://main.qcloudimg.com/raw/189b7ddd0b5767e6d259dce3bfd4db8e.png"  style="height:300px"></img>

**配置约束**
+ 单个域名至多可添加10条重写规则。
+ 多条规则支持调整优先级：底部优先级大于顶部。
+ 待重写 URL：以/开头，支持全路径匹配（例如：/test/a.jpg）和通配符 `*` 匹配（例如：/test/\*/\*.jpg），若指定文件目录，不能以“/”结尾（例如：/test）。
+ 目标 Host：默认为当前域名（默认带http头），可修改为其他域名，必须包含 `http://` 或 `https://` 头。
+ 目标 Path：以/开头（例如：/newtest/b.jpg），通配符 `*` 可通过 `$n` 捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg），若指定文件目录，不能以“/”结尾（例如：/test）。
+ 通配符`*`最多可输入5个，捕获占位符`&n`最多可输入10个。
+ 不支持提交中文内容，输入框中的内容长度不可超过1024个字符




## 配置示例

若加速域名`www.test.com`的 **访问 URL 重写配置** 如下：
![](https://main.qcloudimg.com/raw/a12a1057246e1baca35e81c25f0b1c3a.png)

则实际访问情况如下：

+ 客户端请求 `www.test.com/test/a.jpg`，CDN 节点将返回 `www.test.com/newtest/b.jpg` 的内容。
+ 客户端请求 `www.test.com/test/a.png`，CDN 节点将返回 `www.newtest.com/newtest/a.png` 的内容。



