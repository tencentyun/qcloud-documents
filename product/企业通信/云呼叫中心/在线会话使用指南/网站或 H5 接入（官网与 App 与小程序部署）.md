腾讯云呼叫中心 TCCC 网页端接入提供两种部署方式，分别为网页组件（Web JS）与会话链接（URL 链接），开发者通过简短的代码或地址调用，就可以直接将在线会话能力集成到网页中，省去大量的开发调试时间。

## 接入步骤
1. 登录 [腾讯云呼叫中心 TCCC 管理工作台](https://cloud.tencent.com/document/product/679/73497#logintccc)，左侧导航栏单击**在线客服**-**渠道管理**后选择**网站渠道**，单击**新增网站**。        
![](https://qcloudimg.tencent-cloud.cn/raw/d9d240db387a1b8d34f6c20617dac50d.png)
2. 在添加桌面网站对话窗口中填写“桌面网站名称”，单击**确认**。网站名称用于接入网页标题展示
![](https://qcloudimg.tencent-cloud.cn/raw/d7542ecec378d7953003e183bd827c8e.png)
3. 在线会话顶部展示网站名称效果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/7e6a422e1897dce07cf1d926617d30f2.png)
4. 新增网站后在操作列单击接入方式选择部署方式。
<dx-tabs>
::: 方法一：内嵌插件
单击**复制**内嵌插件代码粘贴到您的网站的标签之前，即可完成部署。
![](https://qcloudimg.tencent-cloud.cn/raw/842b30d5c6ee3f65884bd21263288a9b.png)
:::
::: 方法二：会话链接
单击**复制**会话链接嵌入，桌面版适用于电脑端网页接入，移动版适用于 App/H5/小程序接入。
![](https://qcloudimg.tencent-cloud.cn/raw/5475af72b8f063f2ea9aa510485082df.png)

:::
</dx-tabs>


## 移动版链接内嵌小程序
移动版链接内嵌入小程序如需正常使用，需在小程序后台配置业务域名。
1. 前往 [微信小程序后台](https://mp.weixin.qq.com/) 左侧导航栏单击**开发管理**进入**开发设置**页面。
![](https://qcloudimg.tencent-cloud.cn/raw/12f45a58f995a457b150d569eb2a1d97.png)
2. 下拉该页面找到**业务域名**配置项，单击**修改**。
![](https://qcloudimg.tencent-cloud.cn/raw/775c3a3fd55ba87f74cd904089edf440.png)
3. 添加腾讯云呼叫中心的业务域名（`tccc.qcloud.com`），如下图所示。同时单击下载校验文件，并 [提交工单](https://console.cloud.tencent.com/workorder/category) 发送该校验文件，由腾讯云呼叫中心业务人员进行操作后即可生效。
![](https://qcloudimg.tencent-cloud.cn/raw/89cde6098f734a7a2f84d2fbd33fae5f.png)
4. 以上配置步骤完成后，即可将会话链接移动版嵌入小程序 WebView 中。

## 隐藏标题栏方法
在 WebView 中出现双重标题栏，造成“双下巴”现象，如下图所示。如需隐藏该标题栏，可通过添加`&hideHeader=true` 使用 `https://tccc.qcloud.com/web/im/index.html#/H5chat?webAppId=XXXXXXXXXX&hideHeader=1`
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/847d762aaefc55b24831a3fd7309e275.png" />
