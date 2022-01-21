## 须知

本文承接《使用 iPaaS 写入数据（一）》文档，主要讲附件、图片等二进制数据通过 iPaaS 写入到 aPaaS

## 适用场景

如下，我们通过 postman 模拟客户端请求 iPaaS 集成流后，并把数据写入到 aPaaS 中

> <img src="https://qcloudimg.tencent-cloud.cn/raw/1060f5b3123f71e651b22e15ee486eb5.png"></img>
## 关键字

<font color ="#0abf5b">iPaaS 集成流&nbsp;&nbsp;</font>
<font color ="#ff7200">数据写入&nbsp;&nbsp;</font>
<font color ="#e54545">附件、图片&nbsp;&nbsp;</font>

## 目标

aPaaS 主要对象数据字段类型的写入，包括文本、整数、枚举、文件、图片等

## 实施步骤

### postMan 配置

postman Body 配置为 form-data

> <img src="https://qcloudimg.tencent-cloud.cn/raw/b69417f4df20d658218063040e6b40a1.png"></img>
>     参数说明：
>       text_filed： 模拟文本字段
>       int_filed：  模拟数字字段
>       滴滴电子发票2.pdf：模拟的是附件文件
>       千帆连接器.png：模拟的是图片
>       fileInfos：  文件描述符列表，类型为Json数组，内容如下：
>                   ① fileType：标识文件类型，1：文件；2：图片
>                   ① fileName：标识文件名称
>
>     <img src="https://qcloudimg.tencent-cloud.cn/raw/f54810b697333ab0e35ffad049d489aa.png"></img>
```
[
    {
        "fileType":1,
        "fileName":"滴滴电子发票2.pdf"
    },
    {
        "fileType":2,
        "fileName":"千帆连接器.png"
    }
]
```

### iPaaS 配置

1.设置变量**param**，保存请求 payload

> <img src="https://qcloudimg.tencent-cloud.cn/raw/f235ef224abb7a16030dfa89f490e82c.png"></img>
```python
def dw_process(msg):
    return
    {
        "text_field": msg.payload["parts"]["text_field"]["content"]['^value'],
        "int_field": msg.payload["parts"]["int_field"]["content"]['^value']
    }
```

2.设置变量**fileInfos**，保存 fileInfos 参数：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/d2adea998643936a042d72523144dfc4.png"></img>
```
def dw_process(msg):
    return json.loads(msg.payload["parts"]["fileInfos"]["content"]['^value'])
```

3.设置变量**fileDataList**，保存文件/图片：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/a357a528400dafb9479a7ecb154693c8.png"></img>
```python
def dw_process(msg):
    data={}
    for file in msg.vars["fileInfos"]:
        name=file["fileName"]
        data[name]=msg.payload["parts"][name]["content"]
    return data
```

4.创建千帆连接器，选择文件上传：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/c0bb0fea2e6e6b62f354202adb3c9471.png"></img>
5.配置文件上传组件：

>       ① 配置应用code，方式见文档：《使用iPaaS写入数据（一）》
>       ② 配置文件名列表
>       ③ 配置文件内容列表
>
>       <img src="https://qcloudimg.tencent-cloud.cn/raw/ac8ef5d8a893d5cf70b23be47cd32836.png"></img>
6.配置创建记录组件，如下所示：

>       ① 配置应用code，方式见文档：《使用iPaaS写入数据（一）》
>       ② 配置对象key，方式见文档 ：《使用iPaaS写入数据（一）》
>       ③ 配置字段值列表：
>
>       <img src="https://qcloudimg.tencent-cloud.cn/raw/b81ea096d69d90cd3b646e0c44f4cee3.png"></img>
```python
def dw_process(msg):
    return
    {
        # 测试文本字段
        "text_field": msg.vars["param"]["text_field"],
        # 测试整型字段
        "int_field": msg.vars["param"]["int_field"],
        # 测试文件字段
        "file_field": msg.payload['Response']['Data'][0]["FileId"],
        # 测试图片字段
        "image_field": msg.payload['Response']['Data'][1]["FileId"],
    }
```

### 运行态效果

1.启动 postMan 进行请求，查看「数据对象列表」页面，此时数据已写入到 aPaaS，如下：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/e3f85917e027039d8e34983f2d0cde26.png"></img>
