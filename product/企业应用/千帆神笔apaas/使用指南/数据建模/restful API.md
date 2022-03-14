## 功能介绍

千帆神笔 aPaaS中 Restful API 为开发者提供了一种通过 HTTP 请求与外部数据远程交互的方式。通过 Restful API 用 Json 携带数据发送 HTTP 请求后，会收到对应的 Json 格式的响应数据包。开发者可以通过 Restful API 请求对数据进行增、删、改、查操作。

>?本功能属于平台高级能力，暂未全面开放，如您有意使用，请先发送邮件至 gqtian@tencent.com 并提供您的租户 ID，平台审核通过后方可使用。


## 通过 Restful API 新建外部数据源
1. 登录 [千帆神笔 aPaaS设计态首页](https://apaas.cloud.tencent.com/)，单击**对象建模**。
2. 在右侧单击**外部数据源**，进入查看外部数据源列表。
![1639033394351](https://qcloudimg.tencent-cloud.cn/raw/649b23feb849ebb03fab74ed4ab355d2.png)
3. 在外部数据源列表页面，单击**新建**，创建外部数据源。![img](https://qcloudimg.tencent-cloud.cn/raw/52a4979b1a4c2abb2474e10372dc25e6.png)

### 基本信息

新建外部数据源时，"类型"选择 Rest API，填写基本信息即可创建外部数据源。

+ 类型：外部数据源获取类型，目前支持 Rest API、OData、数据库。
+ 名称 ：外部数据源名称，创建修改时，名称不可重复。
+ 外部数据源 ID：创建修改时，名称不可重复。

![img](https://qcloudimg.tencent-cloud.cn/raw/ba3547ca316c938969d2437956559b48.png)

### 数据源实体字段

实例化外部数据源对象，依据接口请求的返回数据结构配置相应的数据源实体字段，且在设置完成后，可快速生成外部数据源对象。

![img](https://qcloudimg.tencent-cloud.cn/raw/d0b6a7b1f73b8b68097e8a09258fe8ca.png)

#### 添加数据源实体字段

外部数据源 "新建/编辑" 页签，单击"数据源实体字段"中**添加一条**，弹窗显示数据源实体字段添加页面，填写字段相关信息，单击**确定**，添加实体字段。

| 参数 | 是否必填 | 说明 | 
|---------|---------|---------|
| 字段标识 | 是 | 字段唯一标识， 同 aPaaS 中对象的字段 ID。 |
| 字段类型 | 是 | <li> string：文本类型</li><li> int：整数类型</li><li> number：数值类型</li><li> array：列表数组</li><li> objcet：实例 Json 对象</li><li> objcetArray：对象数组</li> |
|  字段名称 | 是 | 字段显示名称，同 aPaaS 中对象的字段名称。|
|  主键字段 | 否 |是否实体对象主键字段，数据源实体字段中只能设置一个主键字段。|

![img](https://qcloudimg.tencent-cloud.cn/raw/03deb4676be38ccc99a593508126bae0.png)



### 全局变量

自定义变量参数，作为外部数据源请求接口中的默认请求参数。在外部接口调用都需要使用共同的变量时，我们可将这些变量定义为全局变量。 配置全局变量后，接口请求时，header 中默认已附带全局变量中的请求参数。

### 接口定义

通过 HTTP 请求，调用外部接口，并获得接口返回值。通过接口定义可对外部对象进行增、删、改、查操作。

#### 列表查询

查询外部数据源对象列表信息。

![img](https://qcloudimg.tencent-cloud.cn/raw/83be4fd5f35bca64036a307640b57a99.png)

**基本信息**

| 参数 | 是否必填 | 说明 | 
|---------|---------|---------|
| 接口标识 | 是 | - |
| 接口名称 | 是 | - |
| 请求路径  | 是 | 支持 GET、POST、PUT、DELETE，查询接口选择 GET、POST 方法即可|
| 成功响应码 | 否 | 可自定义接口成功响应码 |
| 超时时间  | 否 | 等待接口的响应时间，默认15000，单位 ms（毫秒）|

**请求信息**

参数取值可选择对象字段、系统参数、常量。

- 对象字段：选择当前外部数据源配置的实体字段
- 系统参数：设置系统参数，进行数据过滤、分页查询等，精确查询目标数据。
- 常量： 一个具体的值，如 true/1.11/222/zhangsan。 

![img](https://qcloudimg.tencent-cloud.cn/raw/6da9c845c6b4cd0814e71f19cc3fec5e.png)

**请求处理函数**

可通过 Dataway 表达式对请求参数进行处理，达到请求地址的参数要求。

Dataway详细使用方法可参考 专题指南>Dataway                                     ![img](https://qcloudimg.tencent-cloud.cn/raw/e1febffbdb76a438c49fba75ef9064cd.png)

**请求头**

接口请求头，根据调用接口，设置请求参数与参数值，如设置了全局变量，则默认已添加全局变量中的请求参数。

![img](https://qcloudimg.tencent-cloud.cn/raw/32a3c75327372da65e95d5f8cde00b49.png)

**请求体**

接口请求头，GET方法，无需设置请求体，根据调用接口，设置接口请求体。

![img](https://qcloudimg.tencent-cloud.cn/raw/a4769a83f2a8bb602a8566aedfad4089.png)

**返回参数**

根据请求接口的响应结果，设置对应返回参数映射。

![img](https://qcloudimg.tencent-cloud.cn/raw/6463f573207ad1155c8c5c0555f877e6.png)

**响应处理函数**

可通过 Dataway 表达式对返回数据进行处理，处理后的返回数据可与实体字段相匹配。

Dataway 详细使用方法可参考 [Dataway 使用指南](https://cloud.tencent.com/document/product/1365/67908)。                              
![img](https://qcloudimg.tencent-cloud.cn/raw/ac9badfc8d41dacef9a6d02c50aad168.png)

**调试**

单击右上角**调试**按钮，可进行请求测试。

![img](https://qcloudimg.tencent-cloud.cn/raw/fde000656159638c1853632d6deebfba.png)

调试信息页面，可编辑设置请求头与请求体参数信息，配置参数需与接口设置的请求参数一致。![img](https://qcloudimg.tencent-cloud.cn/raw/22ca182d5cb2dfa1b338969ebbb87563.png)

调试参数设置完成后，单击**查看响应结果**，接口右下方即显示响应结果。
![img](https://qcloudimg.tencent-cloud.cn/raw/ba3ce695edfbcceefee86099521becd2.png)

#### 单条查询

查询外部数据源对象单条数据，相关设置与上面"列表查询"相似，可通过系统参数"id"查询外部数据源单条数据。
![img](https://qcloudimg.tencent-cloud.cn/raw/73ec1f1a25d4c87f341411b8a3f43c8a.png)

#### 删除接口

删除外部数据源对象信息，相关设置与上面"列表查询"相似，请求路径中方法选择DELETE，一般通过系统参数id删除外部数据源数据。
![img](https://qcloudimg.tencent-cloud.cn/raw/230682a1ba974d52216a6adb85fc4aa5.png)

#### 新增接口

新增外部数据源对象信息，相关设置与上面"列表查询"相似，请求路径中方法选择POST，并根据实体字段，设置接口请求体。
![img](https://qcloudimg.tencent-cloud.cn/raw/60f6045eeddfbd088c09bcb1acceba91.png)

#### 更新接口

更新外部数据源对象信息，相关设置与上面"列表查询"相似，请求路径中方法选择POST，并根据实体字段，设置接口请求体。
![img](https://qcloudimg.tencent-cloud.cn/raw/69d7b6bc46a0958ca5d16155cb5ec36e.png)

#### 批量删除

批量删除外部数据源对象信息，相关设置与上面"列表查询"相似，在请求路径中方法选择 DELETE，可通过系统参数"ids"批量删除外部数据源数据。
![img](https://qcloudimg.tencent-cloud.cn/raw/d2428d5def18a6edb54b642b53cea770.png)



#### 快速创建外部对象

1. 当接口配置完毕后，外部数据源 "编辑" 页签，单击**创建外部对象**，弹窗显示外部对象创建页面。
![img](https://qcloudimg.tencent-cloud.cn/raw/0fbdb45d7c067b1f9bf70cd4c8d76561.png)
2. 输入对象名称、对象ID，单击**确定**即可创建外部对象。
![img](https://qcloudimg.tencent-cloud.cn/raw/05eb1735438a77d2169032577366a96a.png)
3. 在对象建模画布页面可查看到外部数据源创建的对象。
![img](https://qcloudimg.tencent-cloud.cn/raw/7c59f0ad1af65513dbc73cd7232f34de.png)

