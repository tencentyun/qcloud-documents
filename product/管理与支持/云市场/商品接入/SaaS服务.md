## 操作场景
云市场 SaaS 服务提供“自动交付”的接入方式：相较于传统的兑换码换商品方式，自动交付可以给用户更佳的用户体验，从而获得腾讯云更多的流量推荐。该方式下，用户购买后会接收应用访问 URL 地址，通过服务商提供的账号密码访问或免登 URL 访问应用，直接使用服务。同时，支持版本升级、续费等特性。 
## 流程图  
![](https://main.qcloudimg.com/raw/b41ad4b56260336df8b1f95cda91b230.png) 

## 操作步骤
为了保证服务商可自动接收到客户在云市场发生的购买、续费、退款等一系列行为的消息通知，云市场提供了发货接口的API文档，需服务商参考[《云市场软件服务接入-SaaS商品自动交付接入方案》](https://main.qcloudimg.com/raw/fe02e53747346320763c5e178fc53e54.pdf)进行 API 接口开发，以实现相关消息通知功能，主要包括创建实例、续费通知、配置变更通知、退款通知等。

1. 根据以上文档完成 [服务商管理 > 开发 > 基本配置](https://console.cloud.tencent.com/serviceprovider/setting) 中 URL 和 Token 的填写和 API 接口开发。 
![](https://main.qcloudimg.com/raw/1e3c81bd02190970fde266c0e036f2c6.png)
2. 完成 API 开发后，登录 [服务商管理 > 开发 > 在线接口调试](https://console.cloud.tencent.com/serviceprovider/ondebug) 填写测试地址，调试相关接口。
![](https://main.qcloudimg.com/raw/4facac5cbf4ff29ed57d10d9c333b52b.png)
3. 登录 [云市场 > 服务商管理后台](https://console.cloud.tencent.com/serviceprovider/products) 。  
4. 进入商品管理页面，单击【新建】，选择“SaaS 交付”。
5. 在 [新建 SaaS 交付商品](https://console.cloud.tencent.com/isv/products/create/saas) 页面，填写商品信息。   
![](https://main.qcloudimg.com/raw/3043f8ddc80becde5b5cb0c48546b092.png)   
**【填写说明】**   
**商品名称**：必填，输入商品名称，80字内。   
**商品分类**：必填，选择发布商品对应的分类。   
**商品标签**：必填，选择标签，以描述商品的属性。   
**规格管理**：必填，规格信息填写详情可参考 [关于 SaaS 和人工交付类商品规格周期设置的说明](https://cloud.tencent.com/document/product/306/31732)。 
**Logo 图片**：必填，商品缩略图上传。尺寸建议390x260，格式 jpg/png，大小不超过2M（Logo 图片将展示在云市场商品列表页、云市场商品详情页内）。
**商品缩略图**：非必填，部分运营活动需要引用的图标尺寸建议333x150，格式 jpg/png ，大小不超过2M。  
**商品摘要**：必填，简要描述服务内容与优势，将展示在商品详情页内，商品标题下方的简介文字。
**商品详情**：必填，详细描述服务内容，包括不限于服务介绍、服务流程、使用方法、交付物、帮助文档、过往案例、客户评价。
**依赖的云产品**：非必填，填写本服务所依赖、关联的腾讯云产品名称。   
**上传文档**：非必填，支持本地文档上传，文档格式 PDF、Word、PPT、ZIP、RAR，大小不超过5M。                                                   
**商品服务协议**：必填，是您和服务购买者之间默认的服务协议，可以选择引用既有协议，也可以手动添加新协议，详情可参考 [关于云市场《商品服务协议》上线的通知](https://cloud.tencent.com/document/product/306/17853) 。  
7. 填写完商品信息，单击【提交】。  
8. 提交后商品为“审核中”状态，云市场运营人员会在7个工作日内完成审核。   
9. 审核中的商品，可以单击【预览】查看效果，需要修改继续单击【修改】即可。   
![](https://main.qcloudimg.com/raw/b43d08d5a320a8a3d9133800b432e3c6.png)  

