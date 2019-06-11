## 功能简介
腾讯云 WAF IP 管理，对经过 WAF 防护域名的访问源 IP 进行管理，包括状态查询，IP 黑白名单设置。
## 配置步骤
- **示例一 IP 查询**
1.进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【IP 管理】>【IP 查询】输入需要查询的 IP 地址查看该 IP 状态。
![](https://main.qcloudimg.com/raw/0614d8e5e63f82b80b08dcf8def3153b.png)
2.查询出的 IP 地址，可手动添加黑白名单。
![](https://main.qcloudimg.com/raw/669233546bd59d717c8461bc9a9fd1fc.png)
- **示例二 添加 IP 黑名单**
1.进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【IP 管理】>【IP 黑白名单】进入配置页面。
![](https://main.qcloudimg.com/raw/d70f15d68748b23e2985f559d4d98dfd.png)
**配置项说明：**
**类别：**黑名单、白名单。
**来源：**CC 防护、自定义规则。
**高级筛选：**利用创建时间和有效截止时间进行 IP 信息筛选。
2.添加黑白名单。黑白名单支持导入和筛选结果导出，导入 IP 信息，请求参考导出格式。
![](https://main.qcloudimg.com/raw/61eb54e1f9349638467f7c39514b7e0b.png)
- **示例三 IP 封堵状态查询**
1.进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【IP管理】>【IP封堵状态】进入查询页面，可以查询自定义规则、CC 防护模块拦截的 IP 信息。
![](https://main.qcloudimg.com/raw/32939501d834ac6f39bc4566f416d808.png)
可对查询结果进行导出，对单个 IP 进行加黑加白操作。
