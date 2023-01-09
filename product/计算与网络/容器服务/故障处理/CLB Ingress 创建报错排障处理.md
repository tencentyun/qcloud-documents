
## 现象描述
创建 CLB 类型的 Ingress 报错，错误码`E6009`。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0106a5ab44ffb045216c6f634168d938.png)

## 可能原因

Nginx Ingress 社区1.0.0之前的版本，不支持 networking.k8s.io/v1 类型资源的 Validating Webhook 回调。需要在负责验证的 CRD 里面，去掉 v1类型资源的验证。


## 解决思路

您可参考以下两种方法处理问题：


### 方法1：取消 v1类型资源的验证

将 validatingwebhookconfigurations 类型资源的 webhooks.rules 的 apiVersions 字段调整为 v1beta1。


1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=4)，选择集群所在地域。
2. 在“集群管理”列表中，单击集群名称，进入集群详情页。
3. 选择左侧导航中的“资源对象浏览器”，并在资源类型页中搜索：`validatingwebhookconfigurations`。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/aed36b4e39b448a7529c866888d80184.png)
4. 在搜索结果中选择 `validatingwebhookconfigurations`，单击资源对象列表右侧的**编辑YAML**，检查每一个资源对象的 webhooks.rules 的 apiVersions 字段是否为 v1beta1。
![](https://qcloudimg.tencent-cloud.cn/raw/784a35a42ab4ed1a8394506f70b936f6.png)
5. 升级组件。上述步骤解决的是存量 Nginx Ingress 实例资源验证的问题，要避免新增实例出现类似的问题，需要升级 Nginx Ingress 扩展组件。升级组件步骤如下：
   1. 在集群详情页，选择左侧导航中的**组件管理**。
   2. 单击 Nginx Ingress 右侧的**升级**，将 Nginx Ingress 升级到1.1.0版本。

### 方法2：取消资源的验证
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=4)，选择集群所在地域。
2. 在“集群管理”列表中，单击集群名称，进入集群详情页。
3. 选择左侧导航中的“资源对象浏览器”，并在资源类型页中搜索：`validatingwebhookconfigurations`。
4. 在搜索结果中选择 `validatingwebhookconfigurations`，单击资源对象列表右侧的**删除**，
5. 升级组件。上述步骤解决的是存量 Nginx Ingress 实例资源验证的问题，要避免新增实例出现类似的问题，需要升级 Nginx Ingress 扩展组件。升级组件步骤如下：
   1. 在集群详情页，选择左侧导航中的**组件管理**。
   2. 单击 Nginx Ingress 右侧的**升级**，将 Nginx Ingress 升级到1.1.0版本。

