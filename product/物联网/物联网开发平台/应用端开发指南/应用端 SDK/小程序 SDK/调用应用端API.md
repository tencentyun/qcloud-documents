应用端 API 是物联网开发平台为了满足智能家居场景，为用户开发自有品牌的小程序或 App 而提供的云端服务，包括用户管理、设备管理、设备定时、家庭管理等基础能力。关于应用端 API 的更多信息，请参见 [应用端 API 简介](https://cloud.tencent.com/document/product/1081/40773)。

## 调用应用端 API

调用应用端 API 并获得响应数据。

**接口定义**

```typescript
sdk.requestApi(Action: string, payload?: object, options?: object) => Promise< response >
```

**参数说明**

| 参数名  | 参数描述                                                     | 类型   | 必填 |
| ------- | ------------------------------------------------------------ | ------ | ---- |
| Action  | 请求应用端 API 的 Action 名                                  | string | 是   |
| payload | 请求应用端 API 的数据，会自动带上公共参数 `AccessToken` 与 `RequestId` | object | 否   |
| options | 请求的选项，将透传给 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html) | object | 否   |

**返回值**

- 请求成功（code=0）：返回一个 resolved 的 Promise，其值为应用端 API 响应中的 `Response` 部分数据。
- 请求失败：返回一个 rejected 的 Promise，其值的数据结构为：`{ code, msg, ...detail }`。

**示例代码**

```javascript
sdk.requestApi('AppGetFamilyDeviceList', { FamilyId: 'default' })
  .then(data => {
    // 请求成功
    console.log(data);
  })
  .catch(err => {
    // 请求失败
    console.error(err);
  });
```

> ! 
>- 腾讯云物联网开发平台是基于**家庭**的设备体系，每个家庭有其对应的 `FamilyId`，每台设备均归属一个家庭。
>- 开发者也可以选择不关注家庭这一概念，对所有需要传 `FamilyId` 的接口（例如 [获取用户绑定设备列表](https://cloud.tencent.com/document/product/1081/40803)）传入 `default` 作为 `FamilyId`，SDK 会自动完成内部的家庭相关的逻辑（SDK 会为用户创建一个默认家庭，若 `FamilyId` 入参的值为 `default`，SDK 会自动替换为用户默认家庭的 `FamilyId`）。

