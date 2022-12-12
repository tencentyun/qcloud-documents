## 接口描述
- **描述：**调用 permission.checkJsApiConfig，检查当前应用的 JSAPI 鉴权状态。
- **支持的版本：**2.17.0
- **是否需要鉴权：**否


## 参数说明
### 输入参数
timeout：超时时间（可选）

### 返回参数
Promise：JsApiConfigData（0：失败，1：成功）

## 代码示例
```plaintext
wemeet.permission.checkJsApiConfig()
```
