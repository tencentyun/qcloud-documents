## Net 模块
>? 辅助用户完成云平台基础业务 Web 接口复用。

使用以下 CDN 引入 sdk。
```js
<script src="https://vs-cdn.tencent-cloud.com/sdk/cme_v2.1.js"></script>
```
在页面初始化完成以后填入如下代码，创建`CME.Net`实例。

### 创建实例
创建一个`CME.Net`实例，并传入登录签名，详情请参见 [签名综述](https://cloud.tencent.com/document/product/1156/51127)。 
```js
/*   @create  创建实例方法。
 *    @param sign {{string}} 传入登录签名。
 *    @return 返回一个 cme 组件实例。
 **/
let myCmeNet = CME.Net.create({
  sign: "your_signature",
});

myCmeNet.then(res=>{
  /**
   * 响应结果
   **/
  console.log(res)
}).catch(err=>{
  /**
   * 请求异常 
   **/
  console.error(err)
})
```

### 实例方法

Web 请求包装实例如下代码所示：
#### post
```js
  /**
   *
   *    @send 发送命令字方法,
   *    @param path {{string}} 字符串WEB路径。
   *    @param param {{object}} 查询入参。
   *    @return Promise {{function}} 响应返回值。
   **/
  let result = myCmeNet.fetch("come_path", {
    lo:'123'
  });

  result.then((res)=>{
    /***
     * res
     * 响应结果。
     * */

  }).catch(err=>{
    /**
     * err
     * 异常信息抛出
     * */
  })

```
>?具体的请求地址和响应，详情请参见 [Web 接口文档](https://cloud.tencent.com/document/product/1156/40338)。相关接口调试可单击 [ **在线调试** ](https://video-caster-sdk-1258344699.cos-website.ap-guangzhou.myqcloud.com/demo/debug.html)。
