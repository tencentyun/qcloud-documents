## 操作场景
API 列表显示服务对外暴露的 API 列表。API 调试提供用户在线调试 API 的能力。
您可以在 TSF 控制台中，通过 API 列表查看 API 的详细信息，并进行 API 在线调试。

## 前提条件
要使用 API 列表和调试功能，需要先将服务的 API 注册到注册中心，具体请参考开发手册 [API 注册](https://cloud.tencent.com/document/product/649/30604)。

## 操作步骤
### API 列表
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)，在左侧导航栏中，选择【服务治理】。
2. 单击服务名称，进入服务详情页。
3. 在服务详情页，单击顶部的【API列表】，会显示服务对外提供的 API。
	![](https://main.qcloudimg.com/raw/79686eece8f40b048c241c8222a1b0b5.png)
4. 单击 API 名称进入详情页，可以查看到 API 的详细信息。
  API 详情按照【应用名/版本号】划分显示了 API 的详细信息，包括：路径、方法、描述、入参、出参。其中 Models 表示参数中的复杂类型。
  ![](https://main.qcloudimg.com/raw/a3c7492e80d624202a0d20d7ba6f1207.jpg)


### 手动录入API
TSF 当前支持手动录入API。手动录入 API 的场景主要有：当微服务尚未注册到注册中心，但是希望将 API 进行提前录入，方便配置一些服务治理规则时，可以手动录入。

**录入方式：**
1.  登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)，在左侧导航栏中，单击【服务治理】。
2.  在服务治理列表页，单击微服务名称进入微服务详情页，单击【API列表】。
2. 单击【手动录入API】，输入 API 路径（其中 path 参数可以使用 {param} 来进行描述），并填写请求方法。
3. 同一个微服务下，通过请求路径和请求方法确认唯一一个API。不允许创建同请求方法和路径的API。

>?
- 当注册中心获取到微服务注册的 API 与手动录入的 API 相同时，会认为是同一个 API。
- 当注册中心判断某个 API 在当前任何一个部署组上都没有注册，会展示 API 状态为离线。
- 仅当 API 状态为离线时，该 API 才可以被删除。





### API 调试
1. 在 API 列表页，单击 API 路径，进入 API 详情页。
2. 在 API 详情页，单击右上角的【调试】，进入 API 调试页面。
	![](https://main.qcloudimg.com/raw/fb834f7f00ad8d1a7b30150c3d395513.png)
3. 填写调用 API 的默认参数，单击【发送请求】。
	![](https://main.qcloudimg.com/raw/4982370916dd143bdb57e7ea2d984abe.png)
4. 右侧会展示调用 API 的返回结果。
	![](https://main.qcloudimg.com/raw/b8746e14de991b756e275af9be771b80.png)

