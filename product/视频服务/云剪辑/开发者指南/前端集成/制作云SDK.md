# Net模块

> 辅助用户完成制作云平台基础业务WEB接口复用。

## create

创建一个 `CME.Net` 实例。[如何计算签名?](../客户端访问签名/授权签名综述.md)

```js
/* @create  创建实例方法。
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

## 实例方法

WEB请求包装实例。具体的请求地址和响应，请参考[WEB接口文档]。

> 相关接口可以到这里在线[调试](https://video-caster-sdk-1258344699.cos-website.ap-guangzhou.myqcloud.com/demo/debug.html)

### post

```js

  /**
   *
   * @send 发送命令字方法,
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
