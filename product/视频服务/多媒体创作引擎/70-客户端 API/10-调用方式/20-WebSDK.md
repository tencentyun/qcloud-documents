## 步骤1：初始化 SDK 
在您的 Web 页面中引入 SDK 资源文件：
```html
<script src="https://vs-cdn.tencent-cloud.com/sdk/cme_v2.0.1.js"/>
```
引入完成后，全局将挂载一个`CME`实例。
## 步骤2：获取客户端访问签名
开发者前端向自身服务端请求客户端访问签名（其`action`字段值为`Login`），详情请参见 [签名算法](https://cloud.tencent.com/document/product/1156/43777) 及 [签名示例](https://cloud.tencent.com/document/product/1156/43778)。
## 步骤3：创建 Net 实例
```JavaScript 
/*   @create  创建实例方法。没调用该方法之前。调用 fetch 方法通信无效。
 *    @param sign {{ string }}，客户端访问签名（其`action`字段值为`Login`）。参见签名算法。
 *    @return 返回一个 Net 组件实例。
 **/
let myCmeNet = CME.Net.create({
  sign: "your_signature",
});
```
## 步骤4：发起访问调用
```JavaScript 
  /**
   *
   *    @send 发送命令字方法,
   *    @param path {{string}} 字符串 Web 路径,参考 API 概览https://cloud.tencent.com/document/product/1156/50861。
   *    @param param {{object}} 命令入参。
   *    @return Promise {{function}} 完成命令的回调函数。
   *
   **/
  let result = myCmeNet.fetch("/path/to/a/action", {
    k1 : 'v1',
    k2 : 'v2'
  });

  result.then((res)=>{
    /***
     * res
     * 响应结果
     * */

  }).catch(err=>{
    /**
     * err
     * 异常信息抛出
     * */
  })
```


