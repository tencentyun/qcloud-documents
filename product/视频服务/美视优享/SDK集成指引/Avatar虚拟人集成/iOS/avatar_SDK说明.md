## SDK 接入

SDK 的下载、接入、鉴权、跑通 Demo 请参见 [独立集成腾讯特效](https://cloud.tencent.com/document/product/616/65894)。

## 准备捏脸素材

目前我们随 SDK 提供了若干套捏脸、换装素材，素材在 SDK 解压后的 `MotionRes/avatarRes` 目录中，与其他的动效素材一样，您需要把它 copy 到工程的 assets 目录
<img src="https://qcloudimg.tencent-cloud.cn/raw/a5887d6cf3fddfeaf509e7f30ccb1e1d.png" width=800>

## 捏脸流程与 SDK 接口
<table>
<tr>
	<th style="text-align:center">捏脸流程</th>
	<th style="text-align:center">拍照捏脸流程</th>
</tr>
<tr>
	<td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/95472a4ba7abe2755799f5fff0dd2fc3.png" width=650></td>
	<td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d3dce2bb47f7a3790a20fd4c6557f.png" width=550></td>
</tr>
</table>

XMagicApi 的加载数据、捏脸、导出配置、拍照捏脸接口详情如下：

### 1. 获取 Avatar 源数据接口（getAvatarConfig）
```swift
+ (NSDictionary <NSString *, NSArray *>* _Nullable)getAvatarConfig:(NSString * _Nullable)resPath exportedAvatar:(NSString *_Nullable)exportedAvatar;
```

- **输入参数**：
	- resPath：Avatar 素材在手机上的绝对路径，例如：`/var/mobile/Containers/Data/Application/C82F1F7A-01A1-4404-8CF6-131B26B4DA1A/Library/Caches/avatarMotionRes.bundle/avatar_v2.0_male`。
	- exportedAvatar：用户上次捏脸之后保存的数据，是 JSON 格式的字符串。首次使用或用户之前没有保存过的话，这个值为 nil。
- **输出参数**：
	以 NSDictionary 的形式返回，dictionary 的 key 是数据的 category，详见 TEDefine 类，dictionary 的 value 是这个 category 下全部数据。应用层拿到这份 dictionary 后，按需展示成自己想要的 UI 样式。

### 2. 加载 Avatar 素材接口（loadAvatar）
```swift
- (void)loadAvatar:(NSString * _Nullable)resPath exportedAvatar:(NSString * _Nullable)exportedAvatar;
```
- **输入参数**：
	- resPath：avatar素材在手机上的绝对路径，例如：`/var/mobile/Containers/Data/Application/C82F1F7A-01A1-4404-8CF6-131B26B4DA1A/Library/Caches/avatarMotionRes.bundle/avatar_v2.0_male`。
	- exportedAvatar：用户上次捏脸之后保存的数据，是json格式的字符串。首次使用或用户之前没有保存过的话，这个值为 nil。
- **输出参数**：
以 NSDictionary 的形式返回，dictionary 的 key 是数据的 category，详见 TEDefine 类，dictionary 的 value 是这个 category 下的全部数据。应用层拿到这份 dictionary 后，按需展示成自己想要的 UI 样式。

### 3. 捏脸、换装接口（updateAvatar）
```swift
- (void)updateAvatar:(NSArray<AvatarData *> *_Nonnull)avatarDataList;
```

调用后实时更新当前素材的预览形象，一个 AvatarData 对象是一个原子配置（如换发型），一次可以传入多个原子配置（比如既换发型，又换发色）。该接口会检查传入的 AvatarData 的有效性，有效的设置给SDK，无效的数据会 callback 回去。
- 比如要求修改发型，但是头发模型文件（配置在 AvatarData 的 value 字段里）在本地找不到，就认为该 AvatarData 无效。
- 再比如要求修改瞳孔贴图，但是贴图文件（配置在 AvatarData 的 value 字段里）在本地找不到，就认为该 AvatarData 无效。

### 4. 导出捏脸配置接口（exportAvatar）
```swift
+ (NSString *_Nullable)exportAvatar:(NSArray <AvatarData *>*_Nullable)avatarDataList;
```

用户捏脸时，会修改 AvatarData 中的 selected 状态或形变值。捏完后，传入新的全量 AvatarData 列表，即可导出一份 JSON 字符串。这份字符串您可以存在本地，也可以上传到服务器。
导出的这份字符串有两个用途：
- 当下次再通过 XMagic 的 **loadAvatar** 接口加载这份 Avatar 素材时，把这份 JSON 字符串设置给 **exportedAvatar**，这样才能在预览中呈现出用户上次捏脸的形象。
- 如上文所述，调用 getAllAvatarData 时需要传入这个参数，以便修正 Avatar 源数据中的选中态和形变值。


### 5. 拍照捏脸接口（createAvatarByPhoto）
该接口需要联网。
```swift
+ (void)createAvatarByPhoto:(NSString * _Nullable)photoPath avatarResPaths:(NSArray <NSString *>* _Nullable)avatarResPaths isMale:(BOOL)isMale success:(nullable void (^)(NSString *_Nullable matchedResPath, NSString *_Nullable srcData))success failure:(nullable void (^)(NSInteger code, NSString *_Nullable msg))failure;
```

- **photoPath**：照片路径，请确保人脸位于画面中间。建议画面中只包含一个人脸，如果有多个人脸，SDK 会随机选择一个。建议照片的短边大于等于500px，否则可能影响识别效果。
- **avatarResPaths**：您可以传入多套 Avatar 素材，SDK 会根据照片分析的结果，选择一套最合适的素材进行自动捏脸。
>! 目前只支持一套，如果传入多套，SDK 只会使用第一套。
- **isMale**：是否是男性。暂未用到该属性，但建议准确传入，SDK 后续会优化。
- **success**：成功回调。 matchedResPath—匹配的素材路径、srcData—匹配结果，与上文中的 exportAvatar 接口返回的是一样的含义。
- **failure**：失败回调。code—错误码，msg—错误信息。

### 6. 将下载好的配置文件放置到对应的文件夹中（addAvatarResource）
```swift
+ (void)addAvatarResource:(NSString * _Nullable)rootPath category:(NSString * _Nullable)category filePath:(NSString * _Nullable)filePath completion:(nullable void (^)(NSError * _Nullable error, NSArray <AvatarData *>* _Nullable avatarList))completion;
```

该接口主要用于动态下载 Avatar 配件的场景。举个例子，您的 Avatar 素材中有10种发型，后来想动态下发一种发型给客户端，下载完成后，得到一个压缩包，然后调用该接口，把压缩包路径传给 SDK，SDK 会解析这份压缩包，将它放到对应的 category 目录下。下次您在调用 getAllAvatarData 接口时，SDK就能解析出新添加的这份数据。

参数说明：
- **rootPath**：Avatar 素材的根目录，例如 `/var/mobile/Containers/Data/Application/C82F1F7A-01A1-4404-8CF6-131B26B4DA1A/Library/Caches/avatarMotionRes.bundle/avatar_v2.0_male`。
- **category**：下载的这份配置的分类。
- **zipFilePath**：下载下来的 ZIP 包存放的本地地址。
- **completion**: 结果回调。error—错误信息。avatarList—解析的avatar数据数组。

### 7. 发送自定义事件
发送自定义事件，如：开启无人脸时的闲置显示状态。
```swift
- (void)sendCustomEvent:(NSString * _Nullable)eventKey eventValue:(NSString * _Nullable)eventValue;
```
- **eventKey**：自定义事件 key，可参考 TEDefine 的 AvatarCustomEventKey。
- **eventValue**：自定义事件 value，为 JSON 字符串，例如 `@{@"enabel" : @(YES)}转json字符串，或者直接写@"{\\"enable\\" : true}"`。

### 8. 调用 AvatarData
这几个接口的核心都是 AvatarData 类，其主要内容如下：
```
/// @brief 捏脸配置类型
@interface AvatarData : NSObject
/// 例如 脸型、眼睛微调 等。TEDefine中定义了标准的category，如果不满足需求，也可以自定义category字符串，跟已有的不冲突即可,不能为空
@property (nonatomic, copy) NSString * _Nonnull category;
// 标识每一个具体item 或者 每一个微调项。比如每个眼镜都有自己的id。每一个微调项也有自己的id。不能为空
@property (nonatomic, copy) NSString * _Nonnull Id;
// selector选择类型或者AvatarDataTypeSlider值类型
@property (nonatomic, assign) AvatarDataType type;
/// 如果是selector类型，则它表示当前有无被选中
@property (nonatomic, assign) BOOL isSelected;

/// 捏身体某个部位 如：脸、眼睛、头发、上衣、鞋子等等。如何设值参考官方文档
@property (nonatomic, copy) NSString * _Nonnull entityName;
/// 表示对entityName执行什么操作(action)。 规范参考官方文档
@property (nonatomic, copy) NSString * _Nonnull action;
/// 表示对entityName执行action操作的具体值。 规范参考官方文档
@property (nonatomic, copy) NSDictionary * _Nonnull value;
@end
```

一个 AvatarData 对象是一个原子配置，如换发型、调整脸颊等：
<table>
<tr>
	<th style="text-align:center">换发型</th>
	<th style="text-align:center">调整脸颊</th>
</tr>
<tr>
	<td><img src="https://qcloudimg.tencent-cloud.cn/raw/ddfefa54998a25b3764c2ab918977ae4.png"></td>
	<td><img src="https://qcloudimg.tencent-cloud.cn/raw/66cac959a581a6ce1b66decc3f6e16e2.png"></td>
</tr>
</table>

- 捏脸时，如果数据是 selector类型，则修改 AvatarData 的 selected 字段。例如有4种眼镜 A、B、C、D，默认选中的是 A，那么 A 的 selected 是 true，B、C、D 为 false。如果用户选择了眼镜 B，则把 B 的 selected 为 true，A、C、D 为 false。
- 捏脸时，如果数据是 slider 类型，则修改 AvatarData 的 value 字段。value 字段是一个 JsonObject，里面是若干对 key-value，把 key-value 中的 value 修改为滑竿的值即可。

## AvatarData 高级说明（非必看）
AvatarData 是 SDK 自动从素材根目录的 custom_configs 目录中解析出来返回给应用层的。通常您不需要手动构造 AvataData。
AvatarData 中，对捏脸起关键作用的是 [entityName](entityName)、[action](#action)，[value](#value) 三个字段。这3个字段的值是 SDK 在解析素材配置时自动填入的。大多数情况下，您不需要了解这3个字段的含义，仅在 UI 层展示时，如果是滑竿类型，则需要解析 value 中的形变 key-value 与 UI 操作进行对应。

[](id:entityName)
### entityName 字段
捏脸时，需要明确指定捏哪个部位，比如脸、眼睛、头发、上衣、鞋子 等等。entityName 字段就是描述这些身体部位名称的。以我们的 Demo 素材为例，用 TencentEffectStudio 打开素材工程（xxx.studio）后，可以看到这样一个列表：
<img src="https://qcloudimg.tencent-cloud.cn/raw/06a4860a9b6f1b1cf3350d0dfbfbd68b.png" width=300>
列表里的每一项就是一个身体部位。**命名时，应确保命名在 studio工程中全局唯一**。

[](id:action)
### action 字段
action 字段表示对 entityName 执行什么操作（action）。SDK 内定义了五种 action，每种 action 的含义及 value 要求如下：

| action         | 含义                                                         | value 要求                                                    |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| changeColor    | 修改当前材质的颜色，包括基础色、自发光色等颜色属性           | JsonObject 类型，必填。详见下文 |
| changeTexture  | 修改当前材质的贴图，包括颜色纹理贴图、金属粗糙度纹理贴图、AO 纹理贴图、法线纹理贴图、自发光纹理贴图等等 | JsonObject 类型。必填。详见下文 |
| shapeValue     | 修改blendShape形变值，一般用于面部细节形变微调 | JsonObject 类型。里面的 key 是形变名称，value 是 float 类型的值。必填。详见下文 |
| replace        | 替换子模型，例如替换眼镜、发型、衣服等 | JsonObject 类型。里面描述了新的子模型的3D变换信息、模型路径、材质路径。如果要隐藏当前位置的子模型，则使用 null。详见下文 |
| basicTransform | 调整位置、旋转、缩放。一般用于调整摄像机的远近、角度，从而实现模型全身和半身视角的切换 | JsonObject类 型。必填。详见下文 |

[](id:value)
### value 字段
<dx-tabs>
::: action 等于 changeColor 场景
[](id:changeColor)
**配置示例**：

```swift
{
		"key": "baseColorFactor",
        "value": [43, 26, 23, 255],
		"subMeshIndex":0,
		"materialIndex":0
}
```
- **key**：必填。修改当前材质的颜色，包括基础色、自发光色、其他自定义颜色等颜色属性。如下图：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/d4f7e9d682a4c2384d4f6dfc67274335.png" width=300>
<br>key 具体取什么值，与当前这个材质使用的 shader 有关。上面的截图使用的是内置的 lit_fade 这个 shader，里面定义的基础色的名称是 baseColorFactor、自发光色是 emissiveFactor，所以 key 值就取其中之一。另外，您还可以直接以文本形式打开材质文件，也可以在里面看到各颜色的 key 值，比如这里使用的是 `hair.fmaterial` 这个材质文件，在TEStudio 工程目录中找到并打开它，其内容如下：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/184145d79f7f10eb34c4ad1396e6a7d2.png" width=500>
- **value**：必填。四个值分别是 RGBA。
- **subMeshIndex 和 materialIndex**：[](id:subMeshIndex)非必填。如果不填该字段，则 SDK 内取默认值0。
	在 TEStudio 中，Mesh(一个可以理解为一个子模型，例如眼镜、头发、面部)一般没有配置子Mesh，且一个Mesh只有一份材质，如下图：<br>
	<img src="https://qcloudimg.tencent-cloud.cn/raw/b7e0c6dce61bee40d530ac00b9b3338c.png" width=300>
	<br>一些较复杂的 Mesh 可能有多个子 Mesh，一个 Mesh 可以有多份材质，如下图：<br>
	<img src="https://qcloudimg.tencent-cloud.cn/raw/8f5020bc0917a50939eea7ae96a6160f.png" width=300>
	<br>因此当我们想要 changeColor 时，就需要明确指出 change 的是哪一个材质的 color。subMeshIndex 和 materialIndex 就是用于定位具体的材质。要确定这两个 index 的值，需要打开素材工程目录下的 template.json，找到当前的 mesh，查看 subMeshConfigs 属性，例如我们搜索“hair”，定位到 hair 的配置，可以看到如下的 subMesh 配置：
	<img src="https://qcloudimg.tencent-cloud.cn/raw/85e39b3f3492b2aed27a67bbd3394c60.png" width=500>
	<br>然后通过 subMeshIndex 和 materialIndex 的组合就能定位到具体的材质了。
	:::
	::: action 等于 changeTexture 场景
	[](id:changeTexture)
	**配置示例**：
```swift
{
	"switchKey": "baseColorEnableTexture",
	"switchValue": true,
	"key": "baseColorMap",
	"value": "0622-1/Images/face_tex_base_3.png",
	"subMeshIndex":0,
	"materialIndex":0,
	"textureOptions": {
            "wrapS": "REPEAT",
            "wrapT": "REPEAT",
            "magFilter": "LINEAR",
            "minFilter": "LINEAR_MIPMAP_LINEAR",
            "sRGB": false,
            "mipmap": true,
            "samplerType": "SAMPLER_2D"
         }
}
```
- **switchKey 和 switchValue**：必填。控制是否显示贴图。当 switchValue 为 false 时，表示不设置贴图纹理，此时可以不用填其他字段。switchKey 的取值和 key 的取值要搭配使用。
- **key 和 value**：当 switchValue 为 true 时，这两个字段必填。value 取值为贴图文件与素材根目录的相对路径（如配置示例所示），或者在手机上的绝对路径。
>? 与 [action ==  changeColor](#changeColor) 时的 key 的取值说明类似，switchKey 和 key 与 material 使用的 shader 有关，例如 TEStudio 里内置 shader 的“颜色纹理”开关及值，对应的就是这里的 baseColorEnableTexture 和 baseColorMap。类似地，还有 AO 纹理、法线纹理等字段。在我们的官方捏脸素材中，我们还自定义了 shader，添加了口红贴图开关、面部贴纸开关等等。
您可以直接以文本形式打开材质文件，在里面看到各个贴图的 switchKey 和 key 值，比如我们 Demo 素材里 face_main 使用的材质文件 face.fmaterial，打开后可以看到如下内容：
<img src="https://qcloudimg.tencent-cloud.cn/raw/883ca597bde464a8752b7460f0af754a.png" width=500>
<br>要修改哪个贴图，就在 switchKey 和 key 两个字段中填入该贴图对应的值。
- **subMeshIndex 和 materialIndex**：非必填。如果不填该字段，则 SD K内取默认值0。详细说明请参见 [action ==  changeColor](#subMeshIndex) 说明。
- **textureOptions**：非必填。贴图解析参数。决定贴图的展开和渲染样式。如无特殊配置需求，不建议填写此字段。
:::
::: action 等于 shapeValue 场景
[](id:shapeValue)
**配置示例**
```
{
	"chin_length": 0.0,
	"cheek_width": 0.0,
	"chin_width": 0.0
}
```
分别是形变的名称和形变值，形变名称请参见 [素材设计规范](https://doc.weixin.qq.com/doc/w3_ALoA-gYYAAgV0MAAbjtQfO4EWXhI9?scode=AJEAIQdfAAoU7K9sLCAGMA3QZFAAg&version=4.0.19.6020&platform=win)，形变值取 -1.0 到 1.0 之间。
:::
::: action 等于 replace 场景
[](id:replace)
action == replace 时的 value 字段描述了子模型的3D变换信息、模型路径、材质路径。可以从素材根目录的 template.json 中找到每个模型的这些信息。
**配置示例**：
```
{
	"position": {
		"x": -0.424766392,
		"y": -29.969169617,
		"z": -25.769769669
	},
	"rotation": {
		"x": 0,
		"y": 0,
		"z": 0
	},
	"scale": {
		"x": 1,
		"y": 1,
		"z": 1
	},
	"meshResourceKey": "meshFolder/glass_A.fmesh",
	"subMeshConfigs": [{
		"materialResourceKeys": ["/sdcard/xmagic_res/glass_red.fmaterial"]
	}，{
		"materialResourceKeys": ["/sdcard/xmagic_res/test1.fmaterial"，"/sdcard/xmagic_res/test2.fmaterial"]
	}]
}
```
- **position、rotation、scale**：分别描述了模型的位置、旋转、缩放属性。非必填。如果不填，则使用默认值。position 的默认值是0,0,0，rotation 的默认值是0,0,0，scale 的默认值是1,1,1。
>! rotation 的单位是角度，例如45度就填45。它对应的是素材 template.json 里的 eEuler 字段的值。
- **meshResourceKey**：必填。描述了模型 mesh 文件的路径。路径可以是 mesh 文件与素材根目录的相对路径（如配置示例所示），也可以是文件在手机上的绝对路径。
-  **subMeshConfigs**：必填。如对 [subMeshIndex 和 materialIndex](#subMeshIndex) 的说明，一个mesh可以包含多个 subMesh，一个 subMesh 可以包含多个材质。 subMeshConfigs 字段配置的就是 mesh 与材质的关联关系。materialResourceKeys 里的取值可以是 material 文件与素材根目录的相对路径（如配置示例所示），也可以是文件在手机上的绝对路径。
:::
::: action 等于 basicTransform 场景
**配置示例**：
```swift
{
	"position": {
		"x": -0.424766392,
		"y": -29.969169617,
		"z": -25.769769669
	},
	"rotation": {
		"x": 0,
		"y": 0,
		"z": 0
	},
	"scale": {
		"x": 1,
		"y": 1,
		"z": 1
	}
}
```
用于调整位置、旋转、缩放。一般用于调整摄像机的远近、角度，从而实现模型全身和半身视角的切换。position、rotation、scale 字段 说明请参见 [action 等于 replace 场景](#replace)。
:::
</dx-tabs>

## 配置 Avatar 捏脸换装数据

Avatar 属性配置存放在 resources 文件夹下（路径为：`素材/custom_configs/resources`）：
![](https://qcloudimg.tencent-cloud.cn/raw/fcc5d2d5173afe13008b8369c63b1a32.png)

这些配置文件是自动生成的，通常不需要手动配置。自动生成的方式如下：
设计师用 TencentEffectStudio 设计好一套形象后，运行我们提供的 resource_generator_gui 这个 app（目前仅支持 MacOS 平台），即可自动生成这些配置，详情请参见 [设计规范](https://doc.weixin.qq.com/doc/w3_ALoA-gYYAAgV0MAAbjtQfO4EWXhI9?scode=AJEAIQdfAAoU7K9sLCAGMA3QZFAAg&version=4.0.19.6020&platform=win)。



