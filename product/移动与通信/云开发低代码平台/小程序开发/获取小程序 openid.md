

## 获取方式

我们可以通过微搭提供的 API 接口进行小程序 openid 的获取，API 使用说明请参见 [获取小程序信息](https://cloud.tencent.com/document/product/1301/56702#.E8.8E.B7.E5.8F.96.E5.B0.8F.E7.A8.8B.E5.BA.8F.E4.BF.A1.E6.81.AF)。

### 场景一：通过事件触发获取 openid

1. 我们可以在编辑器中通过低码编辑器调用API来实现获取小程序 openid 的方法，代码示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/631027d3585a6a246ce59f0cc4106906.png)
<dx-codeblock>
:::  js
export default async function({event, data}) {

var a=await app.utils.getWXContext()

console.log(a.OPENID);

}
:::
</dx-codeblock>
2. 在编辑器中创建一个按钮组件。
![](https://qcloudimg.tencent-cloud.cn/raw/46eb2da1ad476c9b9888d4f57aad8d44.png)
3. 为按钮组件配置点击触发获取 openid 方法的事件。
![](https://qcloudimg.tencent-cloud.cn/raw/aa5b203934510ec76c5c1a637b750f38.png)
4. 配置完成后，将应用发布为小程序，打开调试模式并单击按钮，查看 openid 输出结果。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b99d7ee9dbc271873017889bb9a42fca.jpg" style="zoom: 33%;" /> 
5. 新定义一个 string 类型的普通变量（$page.dataset.state.varopenid）：在获取小程序 OPENID 的代码中加入一行代码（$page.dataset.state.varopenid = a.OPENID），把获取的 OPENID 值给变量，OPENID 的值给变量之后，我们就可以通过该变量灵活使用获取的 OPENID 的值。
![](https://qcloudimg.tencent-cloud.cn/raw/a3ac5fb4f54fcd124287c68f2fefb6bc.png)
您可以尝试添加一个单行输入组件，输入值绑定 varopenid 变量：
![](https://qcloudimg.tencent-cloud.cn/raw/bd647c8745b30be4142c45097cde3391.png)
单击**按钮**后输入值显示内容如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/27cc0d3b39e54573835e41c952191e0a.png" style="zoom: 33%;" /> 


### 场景二：在生命周期中获取 openid

1. 我们同样可以通过在生命周期中实现当页面加载时获取 openid 的效果，代码示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/ef75b839810e13e7161f9ce29222d915.png)
<dx-codeblock>
:::  js
app.auth.currentUser.openId
:::
</dx-codeblock>
2. 将应用发布为小程序，打开调试模式并刷新页面，可以看到当页面加载时 openid 已经成功输出。
<img src="https://qcloudimg.tencent-cloud.cn/raw/000784181a9407081c2b586feaa44618.png" style="zoom: 50%;" />  



## 注意事项

若当前微搭环境下授权了多个小程序，则可能会导致 openid 无法正常获取，此时需要将 OPENID 字段更改为 FROM_OPENID，如下所示：
<dx-codeblock>
:::  js
export default {

 async onPageLoad(query) {

  var a=await app.utils.getWXContext()

   console.log(a.FROM_OPENID);

 }
:::
</dx-codeblock>


