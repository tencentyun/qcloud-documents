## 功能介绍

本模块主要实现用户将需要检测的图片上传至 COS，并请求 AI 后台完成推理，实现用户数据上云 AI 检测功能。



## 使用流程

```
iv_ai_init
    |
iv_ai_notify_event
    |
iv_ai_start/iv_ai_stop 
    |
iv_ai_add_model_id / iv_ai_del_mode_id
    |
iv_ai_upload_cos_result_cb // 收到sdk 处理回调
    |
iv_ai_deinit
```



## 接口参考

该功能模块提供以下接口：
- iv_ai_init()：AI 模块初始化
- iv_ai_deinit()：AI 系统去初始化
- iv_ai_start()：启动 AI 推理
- iv_ai_stop()：停止 AI 推理
- iv_ai_set_notify_event()：通知 SDK 发生抓图等时间
- iv_ai_add_model_id()：添加模型 ID
- iv_ai_del_model_id()：删除模型 ID


<dx-alert infotype="notice" title="用户需注册以下回调函数">
(*iv_ai_upload_cos_result_cb)() ：SDK 结果处理回调。
</dx-alert>




#### iv_ai_init

**函数原型**

```
void *iv_ai_init(iv_ai_init_parm_s params);
```

**功能描述**
进行 AI 功能初始化的接口函数，返回 AI 处理的 handle。


**参数说明**

| 参数名称 | 类型              | 描述                   | 输入/输出 |
| -------- | ----------------- | ---------------------- | --------- |
| params   | iv_ai_init_parm_s | 初始化 AI 需要传入的参数 | 输入      |



**返回值**
初始化成功，则返回对应的 handle，失败返回 NULL



#### iv_ai_deinit

**函数原型**

```
int iv_ai_deinit(void **pp_handle);
```

**功能描述**
销毁 AI 功能

**参数说明**

| 参数名称  | 类型    | 描述                          | 输入/输出 |
| --------- | ------- | ----------------------------- | --------- |
| pp_handle | void ** | 通过 iv_ai_init 初始化的 handle | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315) |



#### iv_ai_start

**函数原型**

```
int iv_ai_start(void *handle);
```

**功能描述**
开始 AI 服务

**参数说明**

| 参数名称 | 类型   | 描述                          | 输入/输出 |
| -------- | ------ | ----------------------------- | --------- |
| handle   | void * | 通过 iv_ai_init 初始化的 handle | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315) |



#### iv_ai_stop

**函数原型**

```
int iv_ai_stop(void *handle);
```

**功能描述**
停止 AI 服务

**参数说明**

| 参数名称 | 类型   | 描述                          | 输入/输出 |
| -------- | ------ | ----------------------------- | --------- |
| handle   | void * | 通过 iv_ai_init 初始化的 handle | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315) |


#### iv_ai_notify_event

**函数原型**

```
int iv_ai_notify_event(void *handle, int evt_id, void *arg);
```

**功能描述**

通知 SDK 发生了相关的事件，例如抓图事件。

**参数说明**

| 参数名称 | 类型   | 描述                                                         | 输入/输出 |
| -------- | ------ | ------------------------------------------------------------ | --------- |
| handle   | void * | 通过 iv_ai_init 初始化的 handle                                | 输入      |
| evt_id   | int    | 事件 ID，目前只支持抓图事件（IV_AI_EVENT_PIC_TRIG）           | 输入      |
| arg      | void * | 事件相关的参数，例如抓图事件需要告知抓图的 ID，以便 SDK 获取图片路径 | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315) |



#### iv_ai_add_model_id

**函数原型**

```
int iv_ai_add_model_id(void *handle, int model_id);
```

**功能描述**

通过此接口动态添加 AI 的模型 ID。

**参数说明**

| 参数名称 | 类型   | 描述                          | 输入/输出 |
| -------- | ------ | ----------------------------- | --------- |
| handle   | void * | 通过 iv_ai_init 初始化的 handle | 输入      |
| model_id | int    | 模型 ID，需要添加的推理模型 ID  | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315) |

#### iv_ai_del_model_id


**函数原型**

```
int iv_ai_del_mode_id(void *handle, int model_id);
```

**功能描述**
通过此接口动态删除AI的模型ID

**参数说明**

| 参数名称 | 类型   | 描述                          | 输入/输出 |
| -------- | ------ | ----------------------------- | --------- |
| handle   | void * | 通过 iv_ai_init 初始化的 handle | 输入      |
| model_id | int    | 模型 ID，需要添加的推理模型 ID  | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应 [错误码](https://cloud.tencent.com/document/product/1131/55315)|


#### iv_ai_upload_cos_result_cb

**函数原型**

```
int32_t (*iv_ai_upload_cos_result_cb)(char *file_path, int err_code);

```

**功能描述**
- 上传图片结束回调，并通知上传结果。
- 在收到对应图片回调前不得回收图片资源，否则 SDK 上传图片可能失败。

**参数说明**

| 参数名称  | 类型             | 描述                   | 输入/输出 |
| --------- | ---------------- | ---------------------- | --------- |
| file_path | 上传图片绝对路径 | 上传对应图片的文件路径 | 输出      |
| err_code  | int              | 上传图片的结果         | 输出      |

**返回值**
 无
 
 ## 数据结构
 
该模块提供以下数据结构：
- iv_ai_init_parm_s ：初始化 AI 需要传入的参数 。

#### iv_ai_init_parm_s 

**参数说明**

| 名称                       | 类型                   | 描述                                                         |
| -------------------------- | ---------------------- | ------------------------------------------------------------ |
| work_dir                   | char *                 | 需要 AI 推理图片存储路径，需要 AI 推理图片存储路径，长度限定为128字节 |
| model_id                   | int                    | AI 模型 ID，目前只支持1 - 128，1为人形检测模型                   |
| iv_ai_upload_cos_result_cb | void (*) (char *, int) | 用来处理 COS 上传的结果，参数为上传 COS 的图片路径和上传的结果   |
 
 
 **返回值**
初始化成功，则返回对应的 handle，失败返回 NULL。

## 注意事项

1. 上传图片要求如:
	- 图片 base64 编码后大小不可超过5M。
	- 图片分辨率不得超过 1920 * 1080。
	- 图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
	- 非腾讯云存储的Url速度和稳定性可能受一定影响。
	- 支持 PNG、JPG、JPEG、BMP，不支持 GIF 图片
2. 按照格式准备图片：在推理图片的工作路径 iv_ai_init_parm_s 传入的 work_dir<device_name>_<id>.jpg 的图片。
	- 其中 ID 与调用 iv_ai_notify_event 中图片 ID 保持一致。

## 示例代码
<dx-codeblock>
:::  c
//AI模块初始化
#define CLOUDAI_TEST_ID     (1)
#define cloudai_work_dir     ("./demo_media/ai_pic/")
static void test_upload_cos_result_cb(char *file_path, int result) 
{
    if(IV_AI_UPLOAD_COS_SUCCESS == result) {
        printf("Upload file [%s] to COS successful!\n", file_path);
    } else {
        printf("Failed to upload file [%s]!\n", file_path);
    }
}

iv_ai_init_parm_s params = {cloudai_work_dir, CLOUDAI_MODEL_ID, test_upload_cos_result_cb};

ai_handle = iv_ai_init(params);
if (!ai_handle) {
    Log_d("Failed to initialize cloudai client");
    return IV_ERR_CLOUDAI_INIT_FAIL;;
}

//通知sdk抓图
#define CLOUDAI_TEST_ID     (1)

int cur_id = CLOUDAI_TEST_ID;
ret = iv_ai_notify_event(ai_handle, IV_AI_EVENT_PIC_TRIG, &cur_id);
if(0 != ret) {
    Log_e("send event failed!");
}

:::
</dx-codeblock>


