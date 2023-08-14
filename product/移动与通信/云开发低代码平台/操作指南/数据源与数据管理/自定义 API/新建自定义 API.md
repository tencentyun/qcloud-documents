腾讯云微搭低代码自定义 API 支持调用第三方服务接口或使用代码来实现自定义业务逻辑。本文将介绍如何创建自定义 API 。

## 操作步骤
### 步骤1：填写基础信息
进入**腾讯云微搭控制台** > [APIs](https://console.cloud.tencent.com/lowcode/datasource/connector) 页面，单击**新建 APIs**。
>!标识为自定义 API 的唯一标识，在微搭应用编辑器、自定义代码中均需要借助这个标识来使用。

### 步骤2：选择要创建的 APIs 类型
当前支持 Postman、OpenAPI 3.0、HTTP 请求、自定义代码、云开发云函数等多种类型的 APIs。

### 步骤3：实现 API 方法
开发者可以根据业务需求使用 **HTTP 请求**、**自定义代码**或**云开发云函数**方式实现自定义 API 方法。

#### HTTP 请求
可简单对接第三方 HTTP 接口，通过简单的配置 HTTP 请求地址 、方法 、参数等即可完成方法的配置。详情请参见 [HTTP 请求](https://docs.cloudbase.net/lowcode/datasource/add-methods#http%E8%AF%B7%E6%B1%82)。

#### 自定义代码
集成了常用 NPM 包、数据模型、 API 等 API，只支持 JS 开发语言，可以用来实现自定义业务逻辑，详情请参见 [自定义代码](https://cloud.tencent.com/document/product/1301/68440)。

#### 云开发云函数
云函数是一种特殊的 Javascript 函数，底层基于云开发的云函数能力封装，最终会运行在服务器端的 Nodejs 10.15环境中，可以通过函数的 context 参数来访问云开发 node sdk 的所有能力。详情请参见 [云函数](https://docs.cloudbase.net/lowcode/datasource/add-methods#%E4%BA%91%E5%87%BD%E6%95%B0)。

#### Postman
通过 Postman 导出的 Collection v2.1文件，生成包含对应 HTTP 方法的自定义 API。


### 步骤4：启用方法
最后请勾选方法以启用已经实现的方法。
