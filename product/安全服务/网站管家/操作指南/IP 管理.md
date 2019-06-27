## 功能简介
腾讯云 Web 应用防火墙 IP 管理，对经过 Web 应用防火墙防护域名的访问源 IP 进行管理，包括状态查询，IP 黑白名单设置。
## 配置步骤
- **示例一 IP 查询**
1.进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【IP 管理】>【IP 查询】输入需要查询的 IP 地址查看该 IP 状态。
![](https://main.qcloudimg.com/raw/0c845bb0732fe394c5aeff36d443389f.png)
2.查询出的 IP 地址，可手动添加黑白名单。
![](https://main.qcloudimg.com/raw/cc7737fbb7e8e5065c7f2a17dc39613b.png)
- **示例二 添加 IP 黑名单**
1.进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【IP 管理】>【IP 黑白名单】进入配置页面。
**配置项说明：**
类别：黑名单、白名单。
来源：CC 防护、自定义规则。
高级筛选：利用创建时间和有效截止时间进行 IP 信息筛选。
![](https://main.qcloudimg.com/raw/66b1d6bdf659d55da21969da7528958d.png)
2.添加黑白名单。黑白名单支持导入和筛选结果导出，导入 IP 信息时，请参考导出格式。
![](https://main.qcloudimg.com/raw/1cb1a2a169f996f6f70cbf52e7d0925e.png)
- **示例三 IP 封堵状态查询**
1.进入 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，单击【IP 管理】>【IP 封堵状态】进入查询页面，可以查询自定义规则、CC 防护模块拦截的 IP 信息。可对查询结果进行导出，对单个 IP 进行加黑加白操作。
![](https://main.qcloudimg.com/raw/0c6d50cd2155715e259e73690a7061ad.png)

