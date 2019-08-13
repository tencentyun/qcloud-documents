
## TIMLogin

登录。

**原型：**

```c
TIM_DECL int TIMLogin(const char* user_id, const char* user_sig, TIMCommCallback cb, const void* user_data);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| user_id | const char\* | 用户的 indentifier  |
| user_sig | const char\* | 用户的 sig  |
| cb | TIMCommCallback | 登录成功与否的回调。回调函数定义请参考 [TIMCommCallback](https://cloud.tencent.com/document/product/269/33552#timcommcallback)  |
| user_data | const void\* | 用户自定义数据，IM SDK 只负责传回给回调函数 cb，不做任何处理 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功（接口只有返回 TIM_SUCC，回调 cb 才会被调用），其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?用户登录腾讯后台服务器后才能正常收发消息，登录需要用户提供 identifier、userSig 等信息，具体含义请参考 [登录鉴权](https://cloud.tencent.com/document/product/269/31999)。


## TIMLogout

登出。

**原型：**

```c
TIM_DECL int TIMLogout(TIMCommCallback cb, const void* user_data);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cb | TIMCommCallback | 登出成功与否的回调。回调函数定义请参考 [TIMCommCallback](https://cloud.tencent.com/document/product/269/33552#timcommcallback)  |
| user_data | const void\* | 用户自定义数据，IM SDK 只负责传回给回调函数 cb，不做任何处理 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功（接口只有返回 TIM_SUCC，回调 cb 才会被调用），其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?如用户主动登出或需要进行用户的切换，则需要调用登出操作。


