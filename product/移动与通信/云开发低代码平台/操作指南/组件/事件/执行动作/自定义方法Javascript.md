本文讲述了如何通过事件去调用 Javascript 自定义方法。

## 自定义方法（Javascript）

当平台的内置方法不满足你的场景时，您可以新建一个的 Javascript 函数，通过自定义方法调用。在该函数中，您可以调用平台的 API 方法实现业务逻辑。使用说明如下：

### 新建和调用自定义方法

如图点击时，新建一个 `console` 打印的方法，默认将方法的两个参数 `event` 和 `data` 打印出来，并返回文本`success`。
![](https://qcloudimg.tencent-cloud.cn/raw/7c21a92ede0b310a81d7b28e6dc47484.png)
代码如下：

```
export default function({event, data}) {
  console.log('data',  data) // 打印入参data
  console.log('event', event) //打印系统参数event
  return 'success'
}
```

### 配置方法入参和出参

#### 1、入参

点击【添加方法】后，可以设置方法的入参和出参：
![](https://qcloudimg.tencent-cloud.cn/raw/1310306b02993c1ea9ba87c809b0a0c9.png)
点击入参，您可以直接输入静态的数据，也可以直接从表达式中选择页面其他数据，本次我们选择 系统内置的`当前登录用户信息`。
![](https://qcloudimg.tencent-cloud.cn/raw/a2571867bc2d4628395a94a6934201c6.png)
通过此处配置的参数，会打到函数的参数`data`中。另系统自带的对象<a href="">event 对象</a>会自动携带其他参数。

#### 2、出参

调用的自定义函数内部中`return`后的数据，将作为方法出参。返回的出参按照如下方式使用：

点击出参，并将出参保存到定义的变量上。
![](https://qcloudimg.tencent-cloud.cn/raw/49202e82147eca3a95338105d7d5b9ba.png)

保存到变量后，即可按需将变量绑定在组件上显示。

### 测试入参和出参效果

- 测试入参：开启预览，打印入参`data`和`event`，打开`开发者调试工具`查看日志
- 测试出参：将出参的变量展示到`文本`组件上，展示出参的数据

  ![](https://qcloudimg.tencent-cloud.cn/raw/44d6727fd097adc4c95a92aa39f69b88.png)

### 自定义方法如何返回“失败”的事件

调用自定义方法后，事件流会有一个成功和失败的调用。
![](https://qcloudimg.tencent-cloud.cn/raw/4cd4e6118db548d0791aa51b056bfb0b.png)

您只需在自定义方法中写入如下代码时，就会触发失败回调用。

`throw Error`

如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/45d63a4a754565a689edf24a09d49ef5.png)

### 管理自定义方法

自定义方法中，点击左下角【管理自定义方法】，将会在代码编辑器中打开。
![](https://qcloudimg.tencent-cloud.cn/raw/e53b23562a73d45e3d7e5f0575e93d2d.png)
打开后可以进行自行进行代码编写，语法和使用详见<a href="https://cloud.tencent.com/document/product/1301/57912">代码编辑器使用说明</a>。
