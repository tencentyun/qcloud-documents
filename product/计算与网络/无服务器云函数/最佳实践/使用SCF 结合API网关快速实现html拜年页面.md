## 示例说明

本示例主要说明怎样通过SCF结合API网关，快速实现一个对公网服务的web页面。

## 步骤详情
1. 登录[【无服务器云函数控制台】](https://console.cloud.tencent.com/scf/list?rid=1)，选择`上海`地域，单击【创建】按钮，进入新建函数页面。
2. 选择`模板函数`，填写函数名称为“HtmlDemo”，选择“API 网关返回自定义html页面”模板，单击【下一步】，单击【完成】完成函数创建。
    ![](https://main.qcloudimg.com/raw/eea9313e0901df670020c29f20574c5b.jpg) 
3. 选择【触发方式】选项页，单击【添加触发方式】，为云函数添加API网关 触发器。API触发器参数选择默认参数即可。单击【保存】完成创建。
    ![](https://main.qcloudimg.com/raw/2f00115a1f26f346ddd905c2fdad0151.jpg) 
4. 单击API网关触发器的访问路径，查看自定义的HTML页面。如果需要自定义页面展示内容，可以在【函数代码】选项页进行配置。页面效果如下：
    ![](https://main.qcloudimg.com/raw/4f0b9e29419f69aef24e922a9c016faf.png) 
