腾讯云设备管理接口，主要用于管理摄像头和麦克风设备。

### getDevicesList

获取设备列表。

```typescript
getDevicesList(type?: string): Promise<TXMediaDeviceInfo[]>;
```

**参数**

`type`：设备类型，可选参数，不传返回所有设备列表。传 video 返回摄像头设备列表，传 audio 返回麦克风设备列表。

**返回**

返回 Promise 对象，其中设备信息 `TXMediaDeviceInfo` 结构如下：

| 字段       | 类型                      | 描述                                     |
| ---------- | ------------------------- | ---------------------------------------- |
| type       | string, 'video' \|'audio' | 设备类型，video - 摄像头，audio - 麦克风 |
| deviceId   | string                    | 设备 Id                                  |
| deviceName | string                    | 设备名称                                 |

**说明**

- 该接口不支持在 HTTP 协议下使用，请使用 HTTPS 协议部署您的网站。
- 浏览器出于安全的考虑，在用户未授权摄像头或麦克风访问权限前，deviceId 及 deviceName 字段可能都是空的。因此建议在用户授权访问后，再调用该接口获取设备详情。

---

### setCurrentDevice

设置要使用的设备。

```typescript
setCurrentDevice(type: string, deviceId: string): void;
```

**参数**

- `type`：设备类型，video - 摄像头设备，audio - 麦克风设备。
- `deviceId` 从 [getDevicesList](#getdeviceslist) 中得到的设备 ID。

---

### getCurrentDevice

获取当前的设备信息。

```typescript
getCurrentDevice(type: string): Promise<TXMediaDeviceInfo | null>;
```

**参数**

`type`：设备类型，video - 摄像头设备，audio - 麦克风设备。

**返回**

返回 Promise 对象，其中设备信息 `TXMediaDeviceInfo` 结构请参见 [getDevicesList](#getdeviceslist) 返回说明。

---

### switchDevice

切换当前正在使用的设备。

```typescript
switchDevice(type: string, deviceId: string): void;
```

**参数**

- `type`：设备类型，video - 摄像头设备，audio - 麦克风设备。
- `deviceId` 从 [getDevicesList](#getdeviceslist) 中得到的设备 ID。

**说明**

- 该方法仅适用于从摄像头和麦克风采集音视频时调用，屏幕录制和本地媒体文件采集流时不支持调用该接口。
- 如果还没开始推流，则只更新本地流；如果已经开始推流，同步更新推到服务器的音视频流。

---

### switchCamera

切换摄像头设备。等同于 `switchDevice('video', deviceId)` 。

```typescript
switchCamera(deviceId: string): void;
```

**参数**

`deviceId`：从 `getDevicesList('video')` 中得到的设备 ID。

---

### switchMicrophone

切换麦克风设备。等同于 `switchDevice('audio', deviceId)` 。

```typescript
switchMicrophone(deviceId: string): void;
```

**参数**

`deviceId`：从 `getDevicesList('audio')` 中得到的设备 ID。