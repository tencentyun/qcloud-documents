## 操作场景

[腾讯云鹊桥企业集成服务](https://cloud.tencent.com/product/eis)（Enterprise Integration Service, EIS）作为一种新型的云集成服务，将企业内外部间不同的系统或业务连接到一个统一的平台中，通过复用最佳实践范例、快速搭建系统集成模型实现各个系统间的资源整合、数据编排、业务衔接等功能，满足企业轻量级、全方位、高灵活度的一体化系统集成需求。

目前企业集成服务已经全面接入事件总线，您可以通过配置 SaaS 连接器，来接收并消费来自 EIS 的第三方 SaaS 服务事件，完成云上事件与 SaaS 业务的联动，本文为您介绍如何创建 SaaS 连接器和介绍 SaaS 连接器数据结构。


## 前提条件

已 [创建事件集](https://cloud.tencent.com/document/product/1359/56080)。



## 操作步骤

### 事件集与连接器创建
1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb/)，选择左侧导航栏中的【事件集】。
2. 在“事件集”列表，选择期望配置 SaaS 连接器的事件集。
3. 在“事件集详情”页事件连接器配置项中单击【添加】，如下图所示：
![](https://main.qcloudimg.com/raw/becfdcc055c2eb05638e662454f9d2cb.jpg)
4. **连接器类型**选择【SaaS】连接器，如图：
	![](https://main.qcloudimg.com/raw/83382ef7880263015af1a81f02675dc6.png)
5. 进入 [EIS 控制台](https://console.cloud.tencent.com/eis/project)，依次选择您的项目与应用，进入应用详情页进行配置。
<dx-alert infotype="notice" title="">
如果是子账号，需要管理员权限才可以进行更多操作，请在 EIS 控制台左侧“成员管理”处配置。
</dx-alert>
- 选择项目
![](https://main.qcloudimg.com/raw/b86123f1e07227c332b169a05448b977.png)
- 选择或创建应用
![](https://main.qcloudimg.com/raw/34704fbc676d880d2b0a72b11497da85.png)
- 进入应用详情页，选择对应流
![](https://main.qcloudimg.com/raw/278e0aac540f8b28136f74fba09721f8.png)

6. 在流详情页面，选择新建连接器，依次选择【腾讯云事件总线】-- 【Events 事件投递】
![](https://main.qcloudimg.com/raw/b927e1c309298635a7470e33eae09a20.png)
![](https://main.qcloudimg.com/raw/448a26e379c883fd9dd594d7f60ea5ff.png)

7. 根据指引，配置物理配置与连接器配置
- 默认配置：
![](https://main.qcloudimg.com/raw/f774a021aad18a7bb0b5a66dfd93fc8d.png)
![](https://main.qcloudimg.com/raw/c2b13dd001e06111c3feafd7f72a1a8d.png)

- 连接器配置
![](https://main.qcloudimg.com/raw/ddb90456b96d2144f5496d9ba26256a4.png)

完成后，点击右上角【发布】，完成 SaaS 连接器的创建与配置

### 事件规则创建
1. 回到事件总线控制台，选择左侧导航栏中的【事件规则】。
2. 在“事件规则”顶部选框，选择与之前创建一致的事件集信息，并单击【新建事件规则】，如下图所示：
  ![](https://main.qcloudimg.com/raw/722e3a30a77d81c606a929d20191e349.jpg)
3. 根据页面提示填写相关信息，如下图所示：
![](https://main.qcloudimg.com/raw/5d4adfe4d4956e38986118c0fe28d74c.png)
   其中**云服务类型**选择【SaaS 事件投递】，并配置触发目标端。
4. 单击【确定】即可完成连接器创建与匹配规则设置，所有来自与 EIS 的 SaaS 事件，都可以通过事件总线，完成事件的处理与消费。

     


#### SaaS 连接器的数据结构说明

```json
{      
    "specversion": "0",      
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",  
    "type": "adapter:eis",  
    "source": "eis.cloud.tencent",
    "subjuect":"qcs::eis:${region}:uin/${uin}:application/${projectId}/${applicationId}",  
    "time": "1615430559146",  
    "region": "ap-guangzhou",  
    "datacontenttype": "application/json;charset=utf-8",  
    "resource": [    "qcs::eb:ap-guangzhou:uid1250000000:eventbusid/eventruleid"  ],  
    "data": {
          "payload": "test_value" 
           } 
}
```

`data` 部分参数完全由 EIS 投递的事件内容为准，您可以根据实际业务需求，决定 `data` 字段内需要传递的内容。
