## 登出

通常在切换帐号的时候调用，清除登录态以及内存中的所有数据。

注意： 在多实例被踢时（同一设备，多个页面登录同一账号），SDK 内部会执行登出流程，再抛出 [KICKED_OUT ](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.KICKED_OUT)事件。接入侧可在事件触发时，跳转到登录页面。

**接口名**

```js
tim.logout();
```

**请求参数**

无

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data`为空对象。表示成功登出。

- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.logout();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登出成功
}).catch(function(imError) {
  console.warn('logout error:', imError);
});
```

