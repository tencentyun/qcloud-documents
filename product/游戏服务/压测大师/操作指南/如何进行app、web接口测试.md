## 操作场景
该文档指导您在使用压测大师时，如何在工具中进行用例配置，以及如何进行参数化变量的配置和使用，有助于快速入手工具。

#### URL测试介绍
WeTest 的 URL 测试主要有以下几个特点：
- 简单：人类懒的特性驱动着科技的进步，使用简单模式的时候用户不用写代码，只需简单的点点就可以啦。
- 易用：WeTest 平台提供压力机，可以无上限从云端产生压力。
- 可视化：通过在服务器部署监控进程可以生成多种性能报表，指标一目了然，方便分析和诊断问题。
- 业务场景模拟：对于复杂的场景可以通过编程来实现，真实模拟现网业务。

#### 适用范围
- app、web 单接口。
- 上下文场景压测。
- URL 测试。

## 操作步骤
我们以百度首页为例，看看如何在一分钟内发起压力的。
1. 进入测试服务 WeTest 控制台，选择【压测大师】>【用例列表】，单击新建 URL 测试按钮。
 ![](https://main.qcloudimg.com/raw/bfa4107abd7c793fb02b2b51e116f9bb.png)
2. 填写"测试标题"和“备注”，“起始人数”这里选择5人，每隔30秒增加5人，直到增加至最大人数10人。
 ![](https://main.qcloudimg.com/raw/1302c08319e53c79f02dd671816d2747.png)
3. 新建一个客户端请求，方法选择 GET，URL 填写 `http://www.baidu.com` ，URL 变量和 Header 变量这里可以不用填写。
![](https://main.qcloudimg.com/raw/2b230af649224f4f2fe995aeb3128bd2.png)
 >!填写Header信息或修改参数化变量可以满足更高要求的测试场景，具体可以查看进一步的帮助，在本篇中不作展开
4. 编辑一下“测试模型”，增加一个“场景名”，“压测场景”选择百度的 URL，由于只有一个压测场景，所以把所有100%的压力都放在该场景上。
![](https://main.qcloudimg.com/raw/caf38a41b03272e93e49406d0d6a119f.png)
由于我们测的是百度首页，不是我们自己的服务器，无法去服务器上部署性能观测工具监测 CPU，内存等性能情况，这里就可以不用填写。
 ![](https://main.qcloudimg.com/raw/af221823b20558fa14f9883d5b9ada6e.png)
5. 保存设置。
![](https://main.qcloudimg.com/raw/d4936e773ae7ee6352f5dff60c54934e.png)
 您也可以选择‘立即执行’这个测试，测试会马上进入排队系统，如果压力源系统内有空闲资源将马上为您执行测试。
6. 保存之后会跳转到测试用例列表，这里我们点击运行即可进行测试。
 ![](https://main.qcloudimg.com/raw/980aa6f77cb1b1b5593f2231625b7458.png)

## 如何进行参数化变量的配置和使用
除了以上简单的接口测试，URL 测试还全面支持 app、网站上下文场景压测以及 HTTPS 协议测试。
关于上下文场景测试，简单点来说就是我需要测试一个 URL，但是需要另外一个 URL 的返回值作为输入参数。
数据的来源可以来自上文的 Header 以及 Body 中。提取方式可以按照键值对、全部提取、正则表达式提取以及 json 格式的提取。
 
#### Json 格式提取举例说明
URL1 是向服务器获取一个 json 格式的 Body 请求，然后我们需要提取 json 格式中的 ["projectinfo"][0]["user_id"] 这个路径下的值作为 URL2 的一个 Header 中 hh 变量的值。那么我们的场景配置可以是这样：
URL1 的配置如下图。
 ![](https://main.qcloudimg.com/raw/43afa80ddf5184635b6ba90467377bce.png)
URL1 的返回值如下图。
![](https://main.qcloudimg.com/raw/1d528c4aae3bec5ea4b96480b1083754.png)
 ["projectinfo"][0]["user_id"] 路径的值为“9K810642422”。
URL2 的配置如下图。
![](https://main.qcloudimg.com/raw/a12bcb40f24b7463f94b717c9ff37b3e.png)
hh 是我们 URL2 中需要添加的 Header 字段，它的值来自与上一个 URL1 中的返回值 jsonv1 变量，这里我们用两个大括号把这个变量名括起来。需要注意的是我们在定义变量的时候变量名（比如jsonv1）是不能一样的。testheader 还在 jsonv1 基础上加了 aa 两个字符，这也是可以的。
配置好这两个 URL 之后我们可以在测试模型中把他们的关系配置好，如下所示。
 ![](https://main.qcloudimg.com/raw/532b8e1e28f64bc37095d591ff541e08.png)

#### 键值对方式提取
目前键值对的编写规则是这样的 K1=V1;K2=V2，键值对可以在 URL1 的 Response Header 中，也可以在 URL1 的 Response Body 中。
 ![](https://main.qcloudimg.com/raw/93ac4c01eb64489f7190bf3c5c321829.png)
K1 变量表示来自 URL1 中返回的 Header 的 Set-Cookie 部分，其中的 uid 字段的值；K2 变量表示来自 URL1 中返回的 Body 中，Body 本身是多个键值对的字符串，我们取其中名字为 name 的值。至于 URL2 中的配置跟上面一样。
 
#### 全部提取
全部提取就是把 URL1 中的 Response Header 某个字段的内容全部提取出来，这里不具体阐述了。
 
#### 正则表达式提取
正则表达式的提取是提供给用户一个自定义提取规则的方式，用户首先确定好来自 Response Header 还是 Response Body，对于 Response Body 还要给出 Header 名称，最后在提取规则中给出要提取内容的正则表达式。
 ![](https://main.qcloudimg.com/raw/1e7af7d38b90a638c9e75796c9e1391c.png)
比如在上面文本中需要提取"wetest123"，使用该正则表达式即可。

## 如何设置全局参数
最后，URL 测试还有一个功能，支持“全局参数化”功能。
单击【全局参数设置】按钮，开始设置全局参数化。
 ![](https://main.qcloudimg.com/raw/7665766661bcd0905018a9c8b027da6d.png)
单击【添加】，添加参数，将参数名修改为想要测试的字段，比如上面的“index"字段。另外参数化形式中有“自增”、“随机值”和“定长”三种配置方式。

## 自动设置参数化形式
- 自增：可以设置”最大值“和”最小值“，比如最小值设置1，最大值设置100，就可以自定义服务器压力，比如遍历电商平台上参数值为1-100的所有商品。
- 随机值：可以实现在自定义范围内随机对某页面进行压力测试。
- 定长：通过设置一定长度下的数值，在这个范围内的所有页面进行随机的压力测试，比如定长设置为3，则会在“000-999”“aaa-zzz”之间进行随机的压力测试。
 ![](https://main.qcloudimg.com/raw/da9d7ecf2ff794c5b0e2c1d5d3eb71b9.png)
 
## 定义好的参数如何使用？
在用例中使用{{}}声明为参数变量，如{{var1}}。
参数化后的变量可以使用在以下几个地方。

#### URL 中参数
URL 参数示例:
URL 为`http://wetest.qq.com/Case?projectid=100`，希望 projectid 为参数，动态变化，则定义一个参数为pid，
修改 URL 为`http://wetest.qq.com/Case?projectid={{pid}}`
 ![](https://main.qcloudimg.com/raw/c85bff0cb731a95eb56eb787bb9c6e86.png)

#### Body 参数
Body 参数化示例:
POST 表单时，希望每次填写的用户名是变化的，以模拟正常并发登录时，各个用户使用各自的用户名登录网址，
则定义一个 userid 参数，然后在 POST 请求的 Body 体中，设置以 form-data 格式提交 username，赋值部分填入{{userid}}。
 ![](https://main.qcloudimg.com/raw/a9df2912eff065b9f77d3260c40e9626.png)

#### Header 参数
Header 参数化示例:
请求中 Cookie 具有校验功能，需要输入真实的用户 ID 和 token。
以用户 ID 为例，需要 Cookie 中包含一个键值对为 o_cookie=用户 ID。
则首先定义一个 userid 参数，然后在 Header 体中添加一个 Cookie 键，输入值为 o_cookie={{userid}}。
 ![](https://main.qcloudimg.com/raw/e3a139ffd105e355f38315ec160545c2.png)

## 手动上传参数化源文件
根据用户需求，自主配置参数规则，上传.xls 格式的文件
第一行必须为字段名称。
第二行开始为具体的参数值。
 ![](https://main.qcloudimg.com/raw/e0e422a3120dc785b1f336a1a0d53b5a.png)
参数化源文件使用说明：
现参数化功能已支持从外部文件导入参数值，允许在一个文件中存入多个参数化变量的值，如下图所示。
 ![](https://main.qcloudimg.com/raw/392f3a81c2de3db5e78764f7177645b4.png)
第一行必须包含列头，第二行开始为具体的变换的值，测试执行时，依顺序取用数据，不够则循环。

[看了这么多，赶紧体验吧！](https://console.cloud.tencent.com/wetest/master/testcase)

