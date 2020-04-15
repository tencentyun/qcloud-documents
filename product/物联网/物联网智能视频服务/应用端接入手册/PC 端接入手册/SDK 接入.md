## 简介
使用接口函数前，需先进行 SDK 接入，才可使用 IoT Video SDK。

## IoT Video SDK 类的接口函数
**用户接入**
```
 /**
    @\brief 用户接入
    @\param accessId 用户id
    @\param accessToken 用户token
*/
void Register(std::string accessId, const std::string& accessToken);
```

**用户退出**
```
/**
    @\brief 用户退出
*/
void unRegister();

```
**添加状态消息回调**
```
/**
    @\brief 添加状态消息回调
    @\param fn 第一个参数是设备id，第二个参数是物模型消息
*/
void addModelDataListener(std::function<void(std::string, std::string)> fn);
```
**添加事件消息回调**
```
/**
    @\brief 添加事件消息回调
    @\param fn,第一个参数是设备id，第二参数是事件消息
*/
void addEventListener(std::function<void(std::string, std::string)> fn);
```
**获取 SDK 版本号 **
```
    /**
     * @brief getSdkVersion 获取SDK版本号
     */
    std::string getSdkVersion();
```
**获取局域网设备**
```
    /**
     * @brief getLanDevice 获取局域网内的设备
     */
    std::list<DeviceInfo> getLanDevice();
```



### IoT Write Request 类接口函数

**消息请求对象构造**
```
 /**
    @\brief 消息请求构造
    @\param devid 设备id
    @\param objLeaf 物模型类型
    @\param jData   物模型设置参数
*/
IoTWriteRequest(const std::string& devid,const std::string& objLeaf, const std::string& jData);

```

**发送消息**
```
/**
    @\brief 发送消息

*/
IoTWriteRequest& IotSend();
```

**设置超时回调函数**
```
/**
    @\brief 设置超时回调函数
    @\param fn 第一个参数超时错误信息
*/
IoTWriteRequest& IoTTimeout(std::function<void(std::string)> fn);
```

**设置错误回调函数**
```
/**
    @\brief 设置错误回调函数
    @\param fn 第一个参数：错误信息，第二个参数：错误码
*/
IoTWriteRequest& IoTError(std::function<void(std::string,int err)> fn);
```

**设置成功回调函数**
```
/**
    @\brief 设置成功回调函数
    @\param fn 第一个参数：成功返回信息
*/
IoTWriteRequest& IoTSuccess(std::function<void(std::string)> fn);
```
