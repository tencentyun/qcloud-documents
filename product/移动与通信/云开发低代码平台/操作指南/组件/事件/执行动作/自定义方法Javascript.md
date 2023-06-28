## 介绍
运行在前端的 JavaScript 代码块，遵循标准的 JS 语言规范。可通过自定义 JavaScript 方法实现自定义的业务逻辑，或者调用微搭官方的 [前端 API](https://cloud.tencent.com/document/product/1301/56700) 以及外部 JSSDK 等。


## 如何新建自定义 JavaScript 方法
- 建议通过编辑器左下角代码区，单击 **+** 直接新建自定义 JavaScript 方法。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f0d36e96342d6325c9388646ac48056c.png" />
>?自定义 JS 方法的作用域分为页面作用域和应用全局作用域，可以按需声明。默认情况下，使用页面作用域即可。
- 也可在代码编辑器中直接新建自定义 JavaScript 方法，具体请参见 [代码编辑器](https://cloud.tencent.com/document/product/1301/57912)。


## 如何调用自定义 JavaScript 方法
- 在内部**自定义 JS** 代码之间进行调用。
例如：定义了一个全局 JS 方法 `getBalance()`，则在代码中的调用路径为 `$app.common.getBalance({...})`。若定义了一个页面作用域的 JS 方法 `getChatList()`，则调用路径为 `$page.handler.getChatList({...})`。
>?自定义 JavaScript 方法以及自定义变量和 Query 对象等的引用路径都可以在编辑器左下角代码区 > 单击 **···** > 复制调用路径快捷获取，如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/445e6096c21dcb2a6af7cbbba6b8a10f.png)
- 在**表达式**中进行调用。
在表达式中调用 JS 方法的传参方式，与上述自定义 JavaScript 方法传参相同。
![](https://qcloudimg.tencent-cloud.cn/raw/a9565fa76df5bac73b9e2ddf89641702.png)
- 在事件面板的**JavaScript代码方法**节点中进行调用，例如：
![](https://qcloudimg.tencent-cloud.cn/raw/52d0f4a328c0065e3278a706b6a93d61.png)
![](https://qcloudimg.tencent-cloud.cn/raw/6a6f9f50f9492328d68626941f51f0f4.png)


## 应用场景示例

### 示例1：通过自定义 JS 代码打印当前登录用户信息
该示例以点击某个按钮时，触发一个自定义 JS 方法，来打印当前登录用户的详细信息。
首先，在编辑器左下角代码区单击 **+** 新建一个 **JavaScript 方法**，例如命名为 logger 并保存, 函数体示例代码如下。
```javascript
export default function({event, data}) {
  console.log('data',  data) // 打印入参data
  console.log('event', event) //打印event对象
  if(!data) {
    throw Error; //如需要在事件中触发动作执行失败的分支，则在判断分支中throw Error
  }
  return 'success'
}
```
>?在多个事件动作节点的执行过程中，某个节点执行完成后默认进入执行成功的分支，如果需要在节点执行之后触发动作执行失败的分支，则可在自定义 JS 方法中添加抛出异常代码，如上述的 `throw Error` 即可。

![](https://qcloudimg.tencent-cloud.cn/raw/93311114bc894103f6966538bd8a2c61.png)
然后，可在编辑区拖入一个**按钮**组件，选中**按钮**组件后，在右侧组件属性面板的右下角为其配置**点击**事件，打开**事件面板** > 选择 **JavaScript 代码方法**节点 > 选择**已有方法**中刚新建的`logger`自定义JS方法，如下所示：

![](https://files.mdnice.com/user/39160/6fdfd21f-de88-405d-8be2-6e3ada2016b7.png)

在事件面板中，为选择的自定义JS方法`logger`配置方法入参，如根据表达式提示选择入参为`$w.auth.currentUser`(currentUser为微搭[内置系统变量](https://cloud.tencent.com/document/product/1301/86577#.E5.86.85.E7.BD.AE.E7.B3.BB.E7.BB.9F.E5.8F.98.E9.87.8F)，表示当前登录用户)，完成配置后点击保存。

![](https://files.mdnice.com/user/39160/27fc8d35-f9d0-43ca-8d43-e2bdf90ab6a8.png)

确认上述配置后，回到编辑区点击“按钮”即可触发事件对应的自定义JS方法，打开编辑器右下角**开发调试工具**，即可查看点击时的打印日志，如下所示：

![](https://files.mdnice.com/user/39160/7ca6717c-2494-4692-97ef-9900390261f5.png)



### 示例2 实现通过用户openid来查询用户表中的详细信息
该示例以在**页面加载**时，通过一个自定义JS方法，实现通过已知的小程序`openid`来从数据表中查询当前用户的更多详细信息为例，具体操作过程如下。

首先，在编辑器左下角代码区点击`+`新建一个**JavaScript方法**，如命名为`getUserInfo`, 函数体示例代码如下。

```javascript
export default async function({event, data}) {

    const wxcloud = await app.cloud.getCloudInstance();
    const openid = wxa.OPENID || wxa.FROM_OPENID || app.auth.currentUser.openId;
    console.log("get userinfo openid: ", openid);

    // 提前定义一个全局变量`userInfo`，用于存储获取到的用户信息，方便其他地方引用
    $app.dataset.state.userInfo = await app.cloud.callModel({
        name: 'diy_user_xxxx', // 数据源标识，请自行新建一个用户表`diy_user`，之后可在数据源列表中看到该标识 
        methodName: 'wedaGetItem', 
        params: {
          where: [{
              key: "openid",
              rel: "eq",
              val: openid,
          }],
        },
    });

    console.log("getuserinfo: ", $app.dataset.state.userInfo);

}

```
然后，在编辑器左侧大纲树选择**页面根节点**之后，在右侧属性面板右下角可选择对应的事件触发条件，如选择**页面加载**，在之后打开的事件面板中选择**JavaScript代码**节点，即可完成在页面加载时，如上自定义JS方法的调用，参考步骤如下：

![](https://files.mdnice.com/user/39160/4829f6b8-f8b5-41a6-8690-160fe10ad20f.png)

完成上述配置之后，可刷新页面，打开编辑器右下角的**开发调试工具**，即看到打印日志。
![](https://files.mdnice.com/user/39160/6e9df9f9-363d-4b6e-809c-1734028e7ddc.png)
