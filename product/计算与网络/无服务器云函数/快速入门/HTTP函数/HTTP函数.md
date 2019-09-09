### 操作场景

本文介绍如何上手创建您的第一个HTTP函数。

### 前提条件

* 已注册腾讯云账户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。

* 已开通HTTP函数功能。

  HTTP函数目前为内测发布功能，可通过提交内测申请表单申请试用。

### 操作步骤

### 创建函数

1. 单击左侧导航栏【函数服务】，进入“函数服务”页面。

2. 在页面上方选择**广州**地域，单击【新建】。如下图所示：
   ![img](https://main.qcloudimg.com/raw/3336661866d7dd0fce459b0d49fb9ee3.png)

3. 在“新建函数”页面填写函数基础信息，单击【下一步】。如下图所示：

   ![](https://main.qcloudimg.com/raw/d9d0c611df5d0013b620f2b651d34172.png)

   - 函数名称：命名为 “express-helloworld”。
   - 运行环境：选择 “Nodejs 8.9”。
   - 创建方式：选择 “模版函数”。
   - 模板搜索：选择 “Express” 模版。

4. 函数配置保持默认，并单击【完成】。如下图所示：

   ![](https://main.qcloudimg.com/raw/243d67eaa345a99d2e7afbdff4cdebcc.png)

5. 函数创建完成后，自动进入创建成功函数的“访问控制”页面，可查看HTTP函数的访问路径URL。

   ![](https://main.qcloudimg.com/raw/270fef7d4b39b40077e46284dc6baef9.png)

### 云端测试

您可以直接在浏览器中打开上面的URL，点击后应该会在浏览器中看到：

![](https://main.qcloudimg.com/raw/a44559a1517a4e798bed61362af187b4.png)

您也可以使用其他HTTP测试工具，如CURL、POSTMAN等测试您的HTTP函数。

### 查看日志

在已创建函数的详情页面，选择【运行日志】，即可查看函数详细日志。如下图所示：
![img](https://main.qcloudimg.com/raw/520a0499b08bf6a04da90ce7e1e24396.png)
更多关于日志信息请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

#### 查看监控

在已创建函数的详情页面，选择【监控信息】，即可查看函数调用次数/运行时间等情况。

> 注意：
>
> 监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。

![img](https://main.qcloudimg.com/raw/949a925cc9b88aa6bfb595de77f2d461.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。