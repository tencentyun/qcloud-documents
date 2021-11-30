## 操作场景

该任务指导您在使用消息队列 CKafka 时，通过控制台配置 SASL 鉴权和 ACL 规则，增强对公网/内网传输中的用户访问控制，增加对 Topic 等资源的生产消费权限控制。

>?
>- Kafka 提供了多种安全认证机制，主要分为 SSL 和 SASL2 大类，其中 SASL/PLAIN 是基于账号密码的认证方式，比较常用。CKafka 支持 SASL_PLAINTEXT 认证（参考  [添加路由策略-公网域名接入](https://cloud.tencent.com/document/product/597/36348#public)）。
>- ACL 访问控制列表（Access Control List），帮助用户定义一组权限规则，允许/拒绝用户 user 通过 IP 读/写 Topic 资源。


## 操作步骤

### 配置 ACL 策略

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在顶部菜单栏，选择地域后，单击目标实例“ID/名称”。
3. 在实例详情页面，单击顶部**用户管理**页签。
4. 在用户管理页面，单击**新建**，填写用户名和密码信息，创建用户。
5. 单击顶部 **ACL策略管理**。
6. 在 ACL 策略详情页面，单击**批量配置**，为用户授予权限。
>?
>- 若只设置允许规则，则除允许的规则外的其他 IP 都无法连接实例。
>- 若只设置拒绝规则，则除拒绝的规则外的其他 IP 都可以连接实例。
>- 若同时设置允许规则和拒绝规则，则只有允许规则中的IP可以连接实例，其他 IP 都无法连接实例。 
<dx-tabs>
::: 2.4.1版本及以上实例
支持**批量勾选**，**按前缀模糊匹配**和**预设规则**三种方式为用户授予权限。
> ?配置ACL策略时支持输入多个IP或网段，用 `;` 隔开，若IP为空，则默认为**全部 IP** 添加权限。

- **批量勾选：**选择多个需要配置相同 ACL 策略的 Topic。
- **按前缀模糊：**按 Topic 名称前缀模糊匹配需要配置相同 ACL 策略的 Topic，需要指定模糊匹配规则名称。设置后，新增按指定前缀命名的 Topic 时，系统自动配置指定 ACL 策略。
<dx-alert infotype="explain" title="">
模糊匹配规则最多支持设置五条。  
</dx-alert>
 ![](https://main.qcloudimg.com/raw/302ef1adfcd93b5fcae7ebaed583c7f9.png)
- **预设规则：**预设一套策略，后续创建 Topic 的时候可以自动应用这套规则。
<dx-alert infotype="explain" title="">
预设规则最多支持设置五条。  
</dx-alert>
![](https://main.qcloudimg.com/raw/b38a23497f64826702aa539cd46098d7.png)
:::
::: 其他版本实例
支持**批量勾选**和**预设规则**两种方式为用户授予权限。

> ?支持输入多个IP或网段，用 `;` 隔开；若IP为空，则默认为**全部 IP** 添加权限。




- **批量勾选：**选择多个需要配置相同 ACL 策略的 Topic。
- **预设规则：**预设一套策略，后续创建 Topic 的时候可以自动应用这套规则。
<dx-alert infotype="explain" title="">
预设规则最多支持设置五条。  
</dx-alert>
![](https://main.qcloudimg.com/raw/44a93270d0fd9ac4ef1a287eabac5d95.png)
:::
</dx-tabs>
后续处理：完成授权后，用户可以通过 SASL 接入点接入消息队列 CKafka 并使用 PLAIN 机制消费消息（参考 <a href="https://cloud.tencent.com/document/product/597/54816">SDK 文档</a>）。



### 使用限制

1. 开通路由只影响接入时的验证方式，设置的 ACL 权限则是全局的。
2. 如果您在开通公网访问路由的同时还使用了 PLAINTEXT 方式接入 CKafka，那么之前为 Topic 设置的 ACL 仍然会生效。若您希望 PLAINTEXT 方式的访问不受影响，请为 PLAINTEXT 需要访问的 Topic 添加全部用户的可读写的权限。
<dx-alert infotype="explain" title="">
在添加ACL策略时，不需要选择任何用户，默认为**全部用户**添加了读写权限。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/27e8e0b9b20da5f123eaee2212633dba.png"><br>
 添加完成效果如下：
<img src="https://main.qcloudimg.com/raw/6d1b4b5dd89343530deae827e76d38ab.png"><br>
3. 如果该 Topic 已经在有其他云产品在使用（例如：日志服务 CLS 的日志投递、云函数 SCF 消息转储、大数据 EMR 组件的消费等），开启 ACL 策略相当于对这些联动能力的权限加以限制，会直接导致这些能力不可用，请一定谨慎操作。对于此类情况建议生产同一份数据到另一个 Topic 做分别处理，不要在同一个 Topic 上配置统一的 ACL 策略。

### 查看预设规则

1. 在 ACL 策略管理页面，选择**预设规则**。
2. 在预设规则列表，单击操作列的**详情**，可查看预设规则详情。
   ![](https://main.qcloudimg.com/raw/d2d0869f2d356557ee5f09e2a4ebd354.png)



### 删除预设规则

1. 在 ACL 策略管理页面，选择**预设规则**。
2. 在预设规则列表，单击操作列的**删除**，可删除预设规则。
   根据是规则匹配类型不同，预设规则删除后的影响也有所不同：
   ![](https://main.qcloudimg.com/raw/b41807c61c26e582578810ef382874d8.png)
   - 当规则是模糊匹配规则时，新增 Topic 不会再自动应用该规则，对于已经应用前缀匹配规则的 Topic，该规则也将不再生效。
   - 当规则不是模糊匹配规则时，新增 Topic 不会再自动应用该规则，对于已自动应用该规则的 Topic，相应规则不会一并删除。

   

