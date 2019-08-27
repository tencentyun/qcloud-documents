## 操作场景
本示例主要为您介绍如何通过 SCF 结合 API 网关，快速实现一个对公网服务的 Web 页面。

## 操作步骤
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1)，进入【函数服务】页面。
2. 选择**广州**地域，单击【新建】，进入新建函数页面。
3. 填写以下参数信息，单击【下一步】。如下图所示：
 - 创建方式：选择 “模板函数”。
 - 函数名称：命名为 “HtmlDemo”。
 - 模板搜索：选择 “语言” 为 “Python 2.7” 的 “API 网关返回自定义 html 页面” 模板。
![](https://main.qcloudimg.com/raw/ac4f11bc4af0a945410b470ce3ac592e.jpg) 
4. 保持默认配置，单击【完成】，完成函数的创建。
5. 选择【触发方式】页签
>! “触发方式” 选择 “API网关触发器”，并勾选 “启用集成响应” 功能，其它参数保持默认参数。
>
单击【添加触发方式】，为云函数添加 API 网关触发器。如下图所示：
![](https://main.qcloudimg.com/raw/93777d431d3edaf4b4eaad449b957d3c.jpg) 
6. 单击 API网关触发器的 “访问路径”，查看自定义的 HTML 页面。如下图所示：
![](https://main.qcloudimg.com/raw/4f0b9e29419f69aef24e922a9c016faf.png) 
>? 如果您需要自定义页面展示内容，可以在【函数代码】页签中进行配置。
