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

## AvatarData 高级说明
AvatarData 是 SDK 自动从素材根目录的 custom_configs 目录中解析出来返回给应用层的。通常您不需要手动构造 AvataData。
AvatarData 中，对捏脸起关键作用的是 [entityName](entityName)、[action](#action)，[value](#action) 三个字段。这3个字段的值是 SDK 在解析素材配置时自动填入的。大多数情况下，您不需要了解这3个字段的含义，仅在 UI 层展示时，如果是滑竿类型，则需要解析 value 中的形变 key-value 与 UI 操作进行对应。

[](id:entityName)
### entityName 字段
捏脸时，需要明确指定捏哪个部位，比如脸、眼睛、头发、上衣、鞋子 等等。entityName 字段就是描述这些身体部位名称的。

[](id:action)
### action 和 value字段
action 字段表示对 entityName 执行什么操作（action）。SDK 内定义了五种 action，每种 action 的含义及 value 要求如下：

| action         | 含义                                                         | value 要求                                                   |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| changeColor    | 修改当前材质的颜色，包括基础色、自发光色等颜色属性           | JsonObject 类型，必填。由素材制作工具自动生成。              |
| changeTexture  | 修改当前材质的贴图，包括颜色纹理贴图、金属粗糙度纹理贴图、AO 纹理贴图、法线纹理贴图、自发光纹理贴图等等 | JsonObject 类型。必填。由素材制作工具自动生成。              |
| shapeValue     | 修改blendShape形变值，一般用于面部细节形变微调               | JsonObject 类型。里面的 key 是形变名称，value 是 float 类型的值。必填。由素材制作工具自动生成。 |
| replace        | 替换子模型，例如替换眼镜、发型、衣服等                       | JsonObject 类型。里面描述了新的子模型的3D变换信息、模型路径、材质路径。如果要隐藏当前位置的子模型，则使用null。由素材制作工具自动生成。 |
| basicTransform | 调整位置、旋转、缩放。一般用于调整摄像机的远近、角度，从而实现模型全身和半身视角的切换 | JsonObject 类型。必填。由素材制作工具自动生成。              |

## 配置 Avatar 捏脸换装数据

Avatar 属性配置存放在 resources 文件夹下（路径为：`素材/custom_configs/resources`）：
![](https://qcloudimg.tencent-cloud.cn/raw/fcc5d2d5173afe13008b8369c63b1a32.png)

这些配置文件是自动生成的，通常不需要手动配置。自动生成的方式如下：
设计师用 TencentEffectStudio 设计好一套形象后，运行我们提供的 resource_generator_gui 这个 app（目前仅支持 MacOS 平台），即可自动生成这些配置，详情请参见 [设计规范](https://doc.weixin.qq.com/doc/w3_ALoA-gYYAAgV0MAAbjtQfO4EWXhI9?scode=AJEAIQdfAAoU7K9sLCAGMA3QZFAAg&version=4.0.19.6020&platform=win)。



