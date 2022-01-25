## 适用场景

通过 iPaaS 集成流方式写入数据到 aPaaS 平台

## 关键字

<font color ="#0abf5b">iPaaS 集成流&nbsp;&nbsp;</font>
<font color ="#ff7200">数据写入&nbsp;&nbsp;</font>

## 目标

> aPaaS 主要对象数据字段类型的写入，包括文本、整数、枚举、文件、图片等

## 实施步骤

### 设计态配置

#### aPaaS 配置

1.对象「数据对象」模型设计如下：

>     对象ID：data_object
>     字段说明：
>       ① 编号(id)：自动编号类型，例如：1，2，3，4
>       ② 文本字段(text_field)： 文本类型
>       ③ 整数字段(int_field) ： 整数类型
>       ④ 日期字段(date_field)： 日期时间类型
>       ⑤ 文件字段(file_field)： 文件类型
>       ⑥ 枚举字段(enum_field)： 枚举类型
>       ⑦ 图片字段(image_field)：图片类型
>       ⑧ 关联关系字段(relation_field)：关联关系类型
>       ⑨ 级联枚举字段(cascade_enum_field)：级联枚举类型
>
>     <img src="https://qcloudimg.tencent-cloud.cn/raw/407ef2f0f79be26e80d582fe12070fd5.png"></img>

2.使用从对象创建页面快速创建出列表页面，效果如下：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/e05b2b99293f2956c281eaf2d6a906d8.png" width="40%"></img> > <img src="https://qcloudimg.tencent-cloud.cn/raw/b2ef9e5727f8362be9890705f831df84.png" width="40%"></img>

3.应用发布，打开通过步骤 2 创建的「数据对象列表」页面，效果如下：

> <font color ="#e54545">提示：目前只有 aPaaS 应用发布到运行态后，数据才可通过 iPaaS 等工具写入</font>

> 如下所示：此时列表无数据，符合预期
> <img src="https://qcloudimg.tencent-cloud.cn/raw/d200c876d608831ee132d05cde73159a.png"></img>

#### iPaaS 配置

##### 基本类型字段的写入（文本、数字、枚举、日期等）

1.在对应的 iPaaS 集成流中，添加神笔连接器节点，选择「创建业务数据」操作

> <img src="https://qcloudimg.tencent-cloud.cn/raw/aedc4b5574cd9141b44cb31b85cc8069.png" width = "40%"></img> > <img src="https://qcloudimg.tencent-cloud.cn/raw/daafa421de7150b4dd9e42abb4004985.png" width = "40%"></img>

2.配置「创建业务数据」链接，选择新建操作，填写 SecretId、SecretKey 配置项：

> 提示：SecretId、SecretKey 申请移步 <a href = "https://help.apaas.cloud.tencent.com/docs/open-api">接入准备</a>

> <img src="https://qcloudimg.tencent-cloud.cn/raw/ebe7a1a3188ad4348e83e35dcfba6ee8.png" width="40%"></img> > <img src="https://qcloudimg.tencent-cloud.cn/raw/47963e7397e3ed8185d27891484e09eb.png" width="40%"></img>

3.配置「创建业务数据」，填写「应用 code」和「对象 key」配置项：

> 应用 code 和对象 key 配置查询请移步：<a href = "https://help.apaas.cloud.tencent.com/docs/product/%E6%A1%88%E4%BE%8B%E6%8A%80%E5%B7%A7/%E5%B8%B8%E8%A7%81%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE%E7%B4%A2%E5%BC%95">常见系统配置索引</a> >

> <img src="https://qcloudimg.tencent-cloud.cn/raw/96a6d1c72fccaf35f9ff6ec60b2df9ce.png"></img>

4.配置「创建业务数据」，填写「字段值」配置项，选择表达式：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/218cb3361d350fc03ee7e19c446d78bf.png"></img>

```
def dw_process(msg):
    return
   {
        "text_field": "测试文本字段abc2434",  # 测试文本字段
        "int_field": 123456,  # 测试整形字段
        "date_field": 1636601778000,  # 测试日期时间字段
        "enum_field": ["枚举值1"],  # 测试枚举字段
        "cascade_enum_field": [["广东省", "广州市"]],  # 测试级联枚举字段
    }
```

### 运行态效果

1.启动 iPaaS 集成流，这里我们可以选择集成流测试，点击调试、应用测试

> <img src="https://qcloudimg.tencent-cloud.cn/raw/06fdad6854b486a408fcde359a408bfe.png" width="40%"></img> > <img src="https://qcloudimg.tencent-cloud.cn/raw/f1282ae59b25fd76b86a548f097fe665.png" width="40%"></img>

2.访问集成流，这里我们选择在浏览器发起 1 个 GET 请求：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/1cb78e2ccd306c953f66368851dc4c13.png"></img>

3.查看「数据对象列表」页面，此时数据已写入到 aPaaS，如下：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/7d6fcaac6ec2e3fa58424f19382908cb.png"></img>