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
