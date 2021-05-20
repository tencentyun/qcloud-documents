

## 简介
Async 属于流程控制类组件，在该组件中，可以配置子流执行异步任务，类似于开辟线程。对于写文件、写数据库等任务，可以放置在 Async 中执行。子流在执行时，父流中的 message 会全部传递到 Async 的子流中，子流在执行完成后，结果不会传递给父流，同时，子流在报错时，父流也不会感知，因此需要在子流中进行错误处理。所以，Async 多适合执行一些写文件等耗时操作。

## 操作说明
### 参数配置
无
### 输入到子流中的 message

| message 属性 | 值                                 |
| ----------- | ---------------------------------- |
| payload     | 继承 Async 上一个组件的 payload       |
| error       | 空                                 |
| attribute   | 继承 Async 上一个组件的 attribute 信息 |
| variable    | 继承 Async 上一个组件的 variable 信息  |

### 输出
组件输出的 message 信息如下：

| message 属性 | 值                                 |
| ----------- | ---------------------------------- |
| payload     | 继承 Async 上一个组件的 payload       |
| error       | 空                                 |
| attribute   | 继承 Async 上一个组件的 attribute 信息 |
| variable    | 继承 Async 上一个组件的 variable 信息  |

## 案例
1. 添加 Async 组件。
![image-20210330101109311](https://main.qcloudimg.com/raw/c6f80c00a23a78ec7c053b5da35f2f20/image-20210330101109311.png)
2. 使用 SFTP 组件，向目标服务器写入数据。当执行到 Async 时，系统会异步执行 Async 中的子流。
![image-20210330101430763](https://main.qcloudimg.com/raw/31a1b1f8562d5b2ab2093ae4cabd9f7b/image-20210330101430763.png)
