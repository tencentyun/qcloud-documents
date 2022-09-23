

## 简介

Synchronized 是一个分布式锁。对并发处理的请求进行加锁保护，可应用在对资源互斥的访问场景中。目前加锁保护支持流级别加锁。在不同的项目中，即使“加锁对象”名称相同，也是不同的两把锁，但在同一个项目中，如果“加锁对象”名称相同，则只定义了一把锁。

## 操作配置

### 参数配置

| 参数           | 数据类型 | 描述                                   | 是否必填 | 默认值 |
| :------------- | :------- | :------------------------------------- | :------- | ------ |
| 加锁对象       | string   | 声明一个锁对象。                         | 是       | 无     |
| 最大锁持有时间 | int      | 锁最大占有时间，目前最大支持3600秒。     | 是       | 3600   |
| 最大锁等待时间 | int      | 最长等待时间，目前最长等待时间为3600秒。 | 是       | 3600   |

### 配置界面
![image-20210325155723303](https://main.qcloudimg.com/raw/d7f6f50cff8cf85cf590383009ed1fbb/image-20210325155723303.png)

### 输入到子流中的 message 

| message 属性 | 值                                        |
| ----------- | ----------------------------------------- |
| payload     | 继承 Synchronized 上一个组件的 payload。       |
| error       | 空。                                        |
| attribute   | 继承 Synchronized 上一个组件的 attribute 信息。 |
| variable    | 继承 Synchronized 上一个组件的 variable 信息。  |

### 输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承子流输出的 payload。                                        |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承子流输出的 attribute 信息。                                  |
| variable    | 继承子流输出的 variable 信息。                                   |

## 案例
在资源互斥的场景中，可以使用 Synchronzied 对资源进行加锁，例如：库存扣减操作，对库存查询和库存扣减加锁，防止超卖。
1. 添加 Synchronzied 组件，声明锁对象 stock。
![image-20210406111647518](https://main.qcloudimg.com/raw/a15bdc886fcd5d74a0e4a090e4b3263a/image-20210406111647518.png)
 ![image-20210406111737245](https://main.qcloudimg.com/raw/c045eb18dd7dfe7c8886b2c0bb208547/image-20210406111737245.png)
2. 在 Synchronized 中配置子流，添加 Database 组件，查询库存。
   ![image-20210406112809529](https://main.qcloudimg.com/raw/234aeca05335c49dddc1e3c638cd5de2/image-20210406112809529.png)
3. 库存足够时，进行扣减操作。
   ![image-20210406112854159](https://main.qcloudimg.com/raw/25d2fb56da15c44c3c1de679a122d542/image-20210406112854159.png)
