## 功能说明
输入相机的 openGL 纹理，实时输出人脸52表情 BlendShape 数据，遵循苹果 ARKit 规范，详情请参见 [ARFaceAnchor](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation)。您可以利用这些表情数据做一进步的开发，例如传到 Unity 中驱动您的模型。

## Android 集成指引
Android 集成 SDK 指引，具体请参见 [独立集成腾讯特效](https://cloud.tencent.com/document/product/616/65891)。

### 接口调用
1. 打开功能开关：
```
//XmagicApi.java
//featureName = XmagicConstant.FeatureName.ANIMOJI_52_EXPRESSION
public void setFeatureEnableDisable(String featureName, boolean enable);

```
2. 设置人脸点位信息数据回调。
```java
//XmagicApi.java
void setYTDataListener(XmagicApi.XmagicYTDataListener ytDataListener)

public interface XmagicYTDataListener {
    void onYTDataUpdate(String data)
}
```
onYTDataUpdate 返回 JSON string 结构，最多返回5个人脸信息：
```json
{
 "face_info":[{
  "trace_id":5,
  "face_256_point":[
    180.0,
    112.2,
    ...
  ],
  "face_256_visible":[
    0.85,
    ...
  ],
  "out_of_screen":true,
  "left_eye_high_vis_ratio:1.0,
  "right_eye_high_vis_ratio":1.0,
  "left_eyebrow_high_vis_ratio":1.0,
  "right_eyebrow_high_vis_ratio":1.0,
  "mouth_high_vis_ratio":1.0,
  "expression_weights":[
		0.12,
		-0.32
		...
	]
 },
 ...
 ]
}
```

### 字段含义
- **trace_id**：人脸 ID，连续取流过程中，ID 相同的可以认为是同一张人脸。
- **expression_weights**：实时表情blendshape数据，数组长度为52，每个数值取值范围为 -1.0到1.0。
- 其他字段是 [人脸信息](https://cloud.tencent.com/document/product/616/65896#setytdatalistener)，只有当您购买了相关 License 才有那些字段。如果您只想获取表情数据，请忽略那些字段。
