## 操作场景
假设一款智能灯接入到物联网开发平台，通过物联网开发平台可以远程控制灯的亮度、颜色、开关，并实时获取智能灯上报到开发平台的数据，千帆鹊桥 iPaaS 可通过配置一个集成流实现通过 HTTP 请求触发集成流通过 IOT 接口远程控制灯的亮度、颜色、开关等。

您可以参考如下流程配置一个简单的远程控制智能灯的流。

## 准备工作
#### 1. 获取物联网开发平台相关配置
在 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，获取 SecretId 和 SecretKey，通过 API 获取物联网开发平台的相关数据。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/222ebb51241eb592d4ff12d471991e90.png)


#### 2. 完成物联网开放平台智能灯接入准备
详细操作请参考 [物联网开发平台 - 智能灯接入指引](https://cloud.tencent.com/document/product/1081/41155#.E6.9F.A5.E7.9C.8B.E8.AE.BE.E5.A4.87.E9.80.9A.E4.BF.A1.E6.97.A5.E5.BF.97)。



## 集成流设计
### 步骤1：创建集成流
1. 登录 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，在左侧导航栏，单击**深度集成** 
2. 在深度集成页面，选择对应项目后，单击**添加应用**。
3. 在添加应用窗口，选择空白应用，并命名为 “IOT测试”（应用名称可自行定义）。
![](https://qcloudimg.tencent-cloud.cn/raw/07abe45201b7e786975051d15822094b.png)
4. 单击**确定**，自动跳转进入应用编辑页。单击画布左侧“NewFlow” 进入集成流编辑页面。
![](https://qcloudimg.tencent-cloud.cn/raw/b57ae2f5682acf8796a7ba2378082c28.png)

### 步骤2：配置 “Trigger-HTTP Listener”
配置 Trigger-HTTP Listener，作为集成流的触发器，具体步骤如下：
1. 单击应用编辑页“Trigger 框”中的未配置。在弹框提示选择 “Trigger 组件”，此处请选择 HTTP Listener 作为触发器。
![](https://qcloudimg.tencent-cloud.cn/raw/978f0b768bfe786f4531a4f81ad0c0af.png)
2. 填写 HTTP Listener 配置信息。
	- 监听路径：必填，可默认自动生成的路径或者自定义路径填写，此处填写为 `/iottest`。
	- 监听方法：必填，含 POST、GET 等多种方法，此处选择全部即可。
	- 其余参数：此处保持默认即可。更多请查看 [HTTP Listener 连接器使用指南](https://cloud.tencent.com/document/product/1270/55459)。
![](https://qcloudimg.tencent-cloud.cn/raw/79db466fe9d3f38b5e2d6a4d06faf482.png)
	
	
### 步骤3：设置可共享变量-PID（产品ID）
使用逻辑组件 Set Variable 流级别的组件间的可共享变量，此处主要是设置物联网开放平台中“产品ID”为共享变量。具体步骤如下：
1. 单击画布中的 “+” 弹出组件筛选框。选择 Set Variable 组件。
![](https://qcloudimg.tencent-cloud.cn/raw/23c3c2ee60d242e725e9163e57d53e4f.png)
2. 将物联网开放平台“产品ID”用变量名 PID 通过存在 message 的 variables 进行保留。后续节点可通过 msg.vars.get('PID') 形式引用该变量。
	- 变量名：必填，用户可自定义，此处填写为 PID。
	- 变量值：必填，此处填写 string：产品 ID   
       产品ID获取：进入 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer)单击【实例管理】       >【对应公共实例】>【项目列表】>【对应项目名称】进入产品开发页面，即可获取对应产品ID。
![](https://qcloudimg.tencent-cloud.cn/raw/12f5fc637364ce838cc95aa3016dc0f1.png)(https://console.cloud.tencent.com/iotexplorer/project/prj-h7cotfew/product/list) 获取。
![](https://qcloudimg.tencent-cloud.cn/raw/0ab7e664e882221fe82542b08c8bcde7.png)

### 步骤4：配置腾讯云物联网开发平台-获取设备列表[](step4)
1. 单击画布中的 “+” 弹出组件筛选框。选择腾讯云物联网开发平台连接器。
2. 此处请选择获取设备列表。
![](https://qcloudimg.tencent-cloud.cn/raw/cdefd937a561c30b0b1359ec4d70d7ae.png)
3. 单击**新建**，进行腾讯云物联网开发平台连接器配置。
![](https://qcloudimg.tencent-cloud.cn/raw/c3fad7ee1077719395fbee98fd82cc2e.png)
4. 填写连接器配置名称为 “腾讯云物联网开发平台 #0”（可自定义名称），并单击下一步。
	- SecretId 及 SecretKey：请通过 [API密钥管理](https://console.cloud.tencent.com/cam/capi ) 获取。
	- 地域：推荐选择广州，部分接口的地域会有所要求，具体请参考 [地域列表](https://cloud.tencent.com/document/api/1081/34961#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
	![](https://qcloudimg.tencent-cloud.cn/raw/ac62d818ec5e755936492ea324790652.png)
5. 填写通用配置。
	- 需要查看设备列表的产品ID（单击f(x)切换到表达式输入）：必填，参数如下：
	```
	def dw_process(msg):
				return msg.vars["PID"]
	```
	- 分页的大小：可自定义数值范围 10-100，此处填写10。
![](https://qcloudimg.tencent-cloud.cn/raw/8f620cb4770ee570040cf55f189aeaa6.png)


### 步骤5：设置数据循环处理
1. 单击画布中的 “+” 弹出组件筛选框。选择 For Each 组件。
![](https://qcloudimg.tencent-cloud.cn/raw/94fc3f7f62ee0864e7f8d4d60577380c.png)
2. 填写基本配置。
数据集：必填，填写参数如下：
```
def dw_process(msg):
       return msg.payload.get("Response", {}).get("Devices", [])
```
![](https://qcloudimg.tencent-cloud.cn/raw/df28f6ab2a6a2c414b094c9e23cfb923.png)

### 步骤6：设置可共享变量-PName（设备名）
使用逻辑组件 Set Variable 流级别的组件间的可共享变量，此处主要是设置物联网开放平台中“产品ID”为共享变量。具体步骤如下：
1. 单击画布中的 “+” 弹出组件筛选框。选择 Set Variable 组件。
2. 将物联网开放平台“设备名” 用变量名pName 通过存在 message 的 variables 进行保留。后续节点可通过 msg.vars.get('pName') 形式引用该变量。
	- 变量名：必填，用户可自定义，此处填写为pName
	- 变量值：必填，此处填写如下(单击f(x)以函数形式填写)：
	```
	def dw_process(msg):
				return msg.payload.get("DeviceName")
	```
	![](https://qcloudimg.tencent-cloud.cn/raw/d7f5d002fc5092444d6f493f14823653.png)

### 步骤7：配置腾讯云物联网开发平台-查看设备详情
1. 单击画布中的 “+” 弹出组件筛选框。选择腾讯云物联网开发平台连接器。
2. 此处请选择查看设备详情。
![](https://qcloudimg.tencent-cloud.cn/raw/0a443ed36f75f81a1eb166a4f5ff1d6f.png)
3. 已创建过的连接器配置可复用，单击绑定选择已有连接器配置即可。
![](https://qcloudimg.tencent-cloud.cn/raw/f524585b721f8b050d5fe7afd654b99b.png)
4. 通用配置填写。
	- 产品ID：必填，参数如下：
	```
	def dw_process(msg):
				return msg.vars["PID"]
	```
	- 设备名：必填，参数如下：
	```
	def dw_process(msg):
				return msg.vars["pName"]
	```
	![](https://qcloudimg.tencent-cloud.cn/raw/8440bf425ab638c0341da1eae24fdcad.png)

### 步骤8：配置腾讯云物联网开发平台-设备远程控制
1. 单击画布中的 “+” 弹出组件筛选框。选择腾讯云物联网开发平台连接器。
2. 此处请选择设备远程控制。
![](https://qcloudimg.tencent-cloud.cn/raw/2cfb305484ea3b4f25aad09974c67a33.png)
3. 已创建过的连接器配置可复用，单击绑定选择已有连接器配置即可。
![](https://qcloudimg.tencent-cloud.cn/raw/a6a34c7f8b39e326e7f1b86a40a83959.png)
4. 通用配置填写。
	- 产品 ID（单击f(x)函数模数输入）：必填，参数如下：
	```
	def dw_process(msg):
				return msg.vars["PID"]
	```
	- 设备名（单击f(x)函数模数输入）：必填，参数如下：
	```
	def dw_process(msg):
				return msg.vars["pName"]
	```
	- 属性数据：必填，string{"brightness":1}
	![](https://qcloudimg.tencent-cloud.cn/raw/04477fb7a05e0f147f87914b13ced6dd.png)

## 发布应用
单击画布右侧发布按钮，发布应用。
![](https://qcloudimg.tencent-cloud.cn/raw/8ea96012a3e71583b9fe61b6245fcaed.png)

## 验证结果
### 步骤1：触发集成流
发布成功后，复制触发链接，进行访问触发。如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/674dd4cf07b2e0f65d8996fc3bc3e7c7.png)

### 步骤2：触发结果展示
访问结果如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/76b611843583c34f1d213b98ecf3b52e.png)
展示对应智能灯的产品 ID 状态等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/f421d0cb80b37ec6590551759e1d98b2.png)

### 步骤3：在腾讯云物联网开放平台查看日志信息
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，在实例管理页面单击实例，进入项目列表页。
2. 在项目列表页，单击对应项目名称，选择**设备管理**，并单击操作列的**查看**进入设备详情页。
3. 在设备详情页的**设备云端日志**标签页，可看到对应时间设备的通信内容等信息，对应千帆鹊桥 iPaaS 侧的触发记录。
![](https://qcloudimg.tencent-cloud.cn/raw/c96e2bb0286f02a6f957562c2e59bc31.png)




