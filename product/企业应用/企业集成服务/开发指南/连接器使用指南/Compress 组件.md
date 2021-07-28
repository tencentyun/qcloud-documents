
## 简介
iPaaS Compress 组件可对数据进行压缩和解压，支持的压缩和解压方式有：DEFLATE、GZIP、ZLIB。

## 操作说明
### 压缩操作

#### 参数配置

| 参数           | 数据类型 | 描述                                           | **是否必填** | **默认值** |
| -------------- | -------- | ---------------------------------------------- | ------------ | ---------- |
| 待压缩内容     | binary   | 待执行压缩操作的内容                           | 是           |       -     |
| 压缩方式       | enum     | 压缩方式，支持DEFLATE、GZIP、ZLIB              | 是           |    -        |
| 压缩等级       | enum     | 压缩等级，支持默认压缩、完全不压缩、自定义压缩 | 是           | 默认压缩   |
| 自定义压缩等级 | int      | 用户可自定义压缩等级，等级范围为[1,9]          | 否           |     -       |

![image-20210521115119416](https://main.qcloudimg.com/raw/90fd46e4b66ecd480680ffc6a4e33b47.png)

####  输出
查询操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回压缩后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Compress 连接器组件，选择压缩操作。
2. 在通用配置中，填写相关参数。例如，待压缩内容使用 Dataway 表达式输入:
```python
def dw_process(msg):
    return Entity.from_bytes('ipaas-test', mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
![](https://main.qcloudimg.com/raw/1eddd53aec073266f27e666f6c0d2d65/compress13.png)
3. 执行成功后，message payload 中包含压缩后的二进制内容：
![image-20210521114703633](https://main.qcloudimg.com/raw/e67f0d3a4bccd682f94c69420188053d/compress4.png)

### 解压操作
#### 参数配置

| 参数       | 数据类型 | 描述                              | **是否必填** | **默认值** |
| ---------- | -------- | --------------------------------- | ------------ | ---------- |
| 待解压内容 | binary   | 待执行解压操作的内容              | 是           |     -       |
| 解压方式   | enum     | 解压方式，支持 DEFLATE、GZIP、ZLIB | 是           |    -        |

![image-20210629113951982](https://main.qcloudimg.com/raw/8f3d62f6c760352708a5e8f5d54cefe5/compress12.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 binary 类型，返回解压后的内容；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Compress 连接器组件，选择解压操作。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：待解压内容使用 Dataway 表达式输入:
```python
def dw_process(msg):
    return Entity.from_bytes(msg.payload, mime_type='text/plain', encoding='utf-8')
```
 - 配置界面如下：
 ![image-20210521125904775](https://main.qcloudimg.com/raw/d6c6c5b4dfe4aee5e32adb498af700e5/compress7.png)
4. 插入成功后，message payload 中包含执行结果：
![image-20210521130040100](https://main.qcloudimg.com/raw/e74c1539f43366e7457062210b21013c/compress8.png)
 - 该结果可读性较差，可以对二进制内容进行解码，例如：添加“Set Payload”组件，输入 Dataway 表达式：
```python
def dw_process(msg):
    return msg.payload.decode('utf-8')
```
 - “Set Payload”组件的输出如下，解压后的值和压缩前的内容一致：
![image-20210521131153851](https://main.qcloudimg.com/raw/593ab282da5a799f3b451c31fdd7e121/compress9.png)
5. 若插入过程中出现错误，message error 中会包含错误信息：
![image-20210521131627310](https://main.qcloudimg.com/raw/9135b6ab9bb960038f4af1f9e100eb11/compress10.png)

