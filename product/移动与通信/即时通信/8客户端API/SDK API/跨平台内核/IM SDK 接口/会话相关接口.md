IM SDK 中会话（Conversation）分为两种。
- C2C 会话，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成。
- 群会话，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。


## TIMConvCreate

创建会话。

**原型：**

```c
TIM_DECL int TIMConvCreate(const char* conv_id, enum TIMConvType conv_type, TIMCommCallback cb, const void* user_data);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| conv_id | const char\* | 会话的 ID  |
| conv_type | enum TIMConvType | 会话类型，请参考 [TIMConvType](https://cloud.tencent.com/document/product/269/33553#timconvtype)  |
| cb | TIMCommCallback | 创建会话的回调。回调函数定义和参数解析请参考 [TIMCommCallback](https://cloud.tencent.com/document/product/269/33552#timcommcallback)  |
| user_data | const void\* | 用户自定义数据，IM SDK 只负责传回给回调函数 cb，不做任何处理 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功（接口只有返回 TIM_SUCC，回调 cb 才会被调用），其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?
- 会话是指面向一个人或者一个群组的对话，通过与单个人或群组之间会话收发消息。
- 此接口创建或者获取会话信息，需要指定会话类型（群组或者单聊），以及会话对方标志（对方帐号或者群号）。会话信息通过 cb 回传。


**示例一、获取对方 identifier 为 Windows-02 的单聊会话示例：**

```c
const void* user_data = nullptr; // 回调函数回传
const char* userid = "Windows-02";
int ret = TIMConvCreate(userid, kTIMConv_C2C, [](int32_t code, const char* desc, const char* json_param, const void* user_data) {
    if (ERR_SUCC != code) {
        return;
    }
    // 回调返回会话的具体信息
}, user_data);
if (ret != TIM_SUCC) {
    // 调用 TIMConvCreate 接口失败
}
```


**示例二、获取群组 ID 为 Windows-Group-01 的群聊会话示例：**

```c
const void* user_data = nullptr; // 回调函数回传
const char* userid = "Windows-Group-01";
int ret = TIMConvCreate(userid, kTIMConv_Group, [](int32_t code, const char* desc, const char* json_param, const void* user_data) {
    if (ERR_SUCC != code) {
        return;
    }
    // 回调返回会话的具体信息
}, user_data);
if (ret != TIM_SUCC) {
    // 调用 TIMConvCreate 接口失败
}
```


## TIMConvDelete

删除会话。

**原型：**

```c
TIM_DECL int TIMConvDelete(const char* conv_id, enum TIMConvType conv_type, TIMCommCallback cb, const void* user_data);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| conv_id | const char\* | 会话的 ID  |
| conv_type | enum TIMConvType | 会话类型，请参考 [TIMConvType](https://cloud.tencent.com/document/product/269/33553#timconvtype)  |
| cb | TIMCommCallback | 删除会话成功与否的回调。回调函数定义请参考 [TIMCommCallback](https://cloud.tencent.com/document/product/269/33552#timcommcallback)  |
| user_data | const void\* | 用户自定义数据，IM SDK 只负责传回给回调函数 cb，不做任何处理 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功（接口只有返回 TIM_SUCC，回调 cb 才会被调用），其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?此接口用于删除会话，删除会话是否成功通过回调返回。


## TIMConvGetConvList

获取本地缓存的会话列表。

**原型：**

```c
TIM_DECL int TIMConvGetConvList(TIMCommCallback cb, const void* user_data);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cb | TIMCommCallback | 获取会话缓存列表的回调。回调函数定义和参数解析请参考 [TIMCommCallback](https://cloud.tencent.com/document/product/269/33552#timcommcallback)  |
| user_data | const void\* | 用户自定义数据，IM SDK 只负责传回给回调函数 cb，不做任何处理 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功（接口只有返回 TIM_SUCC，回调 cb 才会被调用），其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

## TIMConvSetDraft

设置指定会话的草稿。

**原型：**

```c
TIM_DECL int TIMConvSetDraft(const char* conv_id, enum TIMConvType conv_type, const char* json_draft_param);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| conv_id | const char\* | 会话的 ID  |
| conv_type | enum TIMConvType | 会话类型，请参考 [TIMConvType](https://cloud.tencent.com/document/product/269/33553#timconvtype)  |
| json_draft_param | const char\* | 被设置的草稿 JSON 字符串 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功，其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?会话草稿一般用在保存用户当前输入的未发送的消息。


**示例**

```c
Json::Value json_value_text;  // 构造消息
json_value_text[kTIMElemType] = kTIMElem_Text;
json_value_text[kTIMTextElemContent] = "this draft";
Json::Value json_value_msg;
json_value_msg[kTIMMsgElemArray].append(json_value_text);

Json::Value json_value_draft; // 构造草稿
json_value_draft[kTIMDraftEditTime] = time(NULL);
json_value_draft[kTIMDraftUserDefine] = "this is userdefine";
json_value_draft[kTIMDraftMsg] = json_value_msg;

if (TIM_SUCC != TIMConvSetDraft(userid.c_str(), TIMConvType::kTIMConv_C2C, json_value_draft.toStyledString().c_str())) {
    // TIMConvSetDraft 接口调用失败
} 

// json_value_draft.toStyledString().c_str() 得到 json_draft_param JSON 字符串如下
{
   "draft_edit_time" : 1551271429,
   "draft_msg" : {
      "message_elem_array" : [
         {
            "elem_type" : 0,
            "text_elem_content" : "this draft"
         }
      ]
   },
   "draft_user_define" : "this is userdefine"
}
```


## TIMConvCancelDraft

删除指定会话的草稿。

**原型：**

```c
TIM_DECL int TIMConvCancelDraft(const char* conv_id, enum TIMConvType conv_type);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| conv_id | const char\* | 会话的 ID  |
| conv_type | enum TIMConvType | 会话类型，请参考 [TIMConvType](https://cloud.tencent.com/document/product/269/33553#timconvtype)  |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功，其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

