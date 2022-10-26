## SDK 接入

SDK 的下载、接入、鉴权、跑通 Demo 请参见 [独立集成腾讯特效](https://cloud.tencent.com/document/product/616/65891)。

## 准备捏脸素材

目前我们随 SDK 提供了若干套捏脸、换装素材，素材在 SDK 解压后的 `MotionRes/avatarRes` 目录中，与其他的动效素材一样，您需要把它 copy 到工程的 assets 目录：
![](https://qcloudimg.tencent-cloud.cn/raw/53a584f0807dfa3df82808589b2fc7eb.png)

## 捏脸流程与 SDK 接口
<table>
<tr>
	<th style="text-align:center">捏脸流程</th>
	<th style="text-align:center">拍照捏脸流程</th>
</tr>
<tr>
	<td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/c5185834386c44e9b5fd0c9cdb03bf8a.png" width=650></td>
	<td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/b6f018b6a757a556c9f0682342330a4b.png" width=550></td>
</tr>
</table>
XMagicApi 的加载数据、捏脸、导出配置、拍照捏脸接口详情如下：

### 1. 加载 Avatar 素材（loadAvatar）
```java
public void loadAvatar(XmagicProperty<?> property, UpdatePropertyListener updatePropertyListener)
```
Avatar 素材与普通的动效素材的加载方式是类似的，loadAvatar 接口与 SDK 的 updateProperty 接口是等价的，因此请参考 [updateProperty 接口说明和 Demo 代码](https://cloud.tencent.com/document/product/616/65896#updateproperty)。

### 2. 加载 Avatar 源数据（getAvatarConfig）
```java
public static Map<String,List<AvatarData>> getAvatarConfig(String avatarResPath, String savedAvatarConfigs)
```

- 输入参数：
	- **avatarResPath**：avatar 素材在手机上的绝对路径，例如 `/data/data/com.tencent.pitumotiondemo.effects/files/xmagic/MotionRes/avatarRes/animoji_0624`。
	- **savedAvatarConfigs**：用户上次捏脸之后保存的数据，是 JSON 格式的字符串。首次使用或用户之前没有保存过的话，这个值为 null。
- 输出参数：
  以 map 的形式返回，map 的 key 是数据的 category，详见 AvatarCategory 类，map 的 value 是这个 category 下的全部数据。应用层拿到这份 map 后，按需展示成自己想要的 UI 样式。

### 3. 捏脸、换装（updateAvatar）
```java
public void updateAvatar(List<AvatarData> avatarDataList, UpdateAvatarConfigListener upDataAvatarConfigListener)
```
调用后实时更新当前素材的预览形象，一个 AvatarData 对象是一个原子配置（如换发型），一次可以传入多个原子配置（例如既换发型，又换发色）。该接口会检查传入 AvatarData 的有效性，有效的设置给 SDK，无效的数据会 callback 回去。
- 例如要求修改发型，但是头发模型文件（配置在 AvatarData 的 value 字段里）在本地找不到，就认为该 AvatarData 无效。
- 再例如要求修改瞳孔贴图，但是贴图文件（配置在 AvatarData 的 value 字段里）在本地找不到，就认为该 AvatarData 无效。

### 4. 导出捏脸配置（exportAvatar）
```java
public static String exportAvatar(List<AvatarData> avatarDataList)
```
用户捏脸时，会修改 AvatarData 中的 selected 状态或形变值。捏完后，传入新的全量 AvatarData 列表，即可导出一份json字符串。这份字符串您可以存在本地，也可以上传到服务器。
导出的这份字符串有两个用途：
- 当下次再通过 XMagicApi 的 loadAvatar 接口加载这份 Avatar 素材时，您需要把这份 JSON 字符串设置给 XMagicProperty的customConfigs 字段，这样才能在预览中呈现出用户上次捏脸的形象。
- 如上文所述，调用 getAllAvatarData 时需要传入这个参数，以便修正Avatar源数据中的选中态和形变值。

### 5. 拍照、捏脸（createAvatarByPhoto）
该接口需要联网。
```java
public void createAvatarByPhoto(String photoPath, List<String> avatarResPaths, boolean isMale,
            final FaceAttributeListener faceAttributeListener)
```
- **photoPath**：照片路径，请确保人脸位于画面中间。建议画面中只包含一个人脸，如果有多个人脸，SDK会随机选择一个。建议照片的短边大于等于500px，否则可能影响识别效果。
- **avatarResPaths**：您可以传入多套Avatar素材，SDK会根据照片分析的结果，选择一套最合适的素材进行自动捏脸。注：目前只支持一套，如果传入多套，SDK只会使用第一套。
- **isMale**：是否是男性。暂未用到该属性，但建议准确传入，SDK后续会优化。
- **faceAttributeListener**：如果失败，会回调 `void onError(int errCode, String msg)`。如果成功，会回调`void onFinish(String matchedResPath, String srcData)`,第一个参数是匹配到的Avatar素材路径，第二个参数是匹配结果，与上文中的exportAvatar接口的返回值是一样的含义。
- onError 的错误码定义在 `FaceAttributeHelper.java`，具体如下：
```
    public static final int ERROR_NO_AUTH = 1;//没有权限
    public static final int ERROR_RES_INVALID = 5;//传入的Avatar素材路径无效
    public static final int ERROR_PHOTO_INVALID = 10;//读取照片失败
    public static final int ERROR_NETWORK_REQUEST_FAILED = 20;//网络请求失败
    public static final int ERROR_DATA_PARSE_FAILED = 30;//网络返回数据解析失败
    public static final int ERROR_ANALYZE_FAILED = 40;//人脸分析失败
    public static final int ERROR_AVATAR_SOURCE_DATA_EMPTY = 50;//加载Avatar源数据失败

```

### 6. 将下载好的配置文件放置到对应的文件夹中（addAvatarResource）

```
public static Pair<Integer, List<AvatarData>> addAvatarResource(String resourceRootPath, String category, String zipFilePath)
```

该接口主要用于动态下载Avatar配件的场景。举个例子，您的Avatar素材中有10种发型，后来想动态下发一种发型给客户端，下载完成后，得到一个压缩包，然后调用该接口，把压缩包路径传给SDK，SDK会解析这份压缩包，将它放到对应的category目录下。下次您在调用 getAllAvatarData 接口时，SDK就能解析出新添加的这份数据。
参数说明：

- resourceRootPath：Avatar素材的根目录，例如 /data/data/com.tencent.pitumotiondemo.effects/files/xmagic/MotionRes/avatarRes/animoji_0624
- category：下载的这份配件的分类
- zipFilePath：下载的zip包地址
  接口返回 `Pair<Integer, List<AvatarData>>`，pair.first是错误码，pair.second是新添加的数据集合。
  错误码如下：

```
    public interface AvatarActionErrorCode {
        int OK = 0;
        int ADD_AVATAR_RES_INVALID_PARAMS = 1000;
        int ADD_AVATAR_RES_ROOT_RESOURCE_NOT_EXIST = 1001;
        int ADD_AVATAR_RES_ZIP_FILE_NOT_EXIST = 1002;
        int ADD_AVATAR_RES_UNZIP_FILE_FAILED = 1003;
        int ADD_AVATAR_RES_COPY_FILE_FAILED = 1004;
    }
```

### 7. 调用 AvatarData
下述接口的核心都是 AvatarData 类，其主要内容如下：
```
public class AvatarData {
    /**
     * 选择型数据。例如眼镜，有很多种眼镜，使用时只能从中选择一个。
     */
    public static final int TYPE_SELECTOR = 0;

    /**
     * 滑竿调节型数据。例如调整脸颊宽度。
     */
    public static final int TYPE_SLIDER = 1;

    //例如 脸型、眼睛微调 等。AvatarCategory.java中定义了标准的category，如果不满足需求，也可以自定义category字符串，跟已有的不冲突即可
    //不能为空。
    public String category;

    //标识每一个具体item 或者 每一组微调项。
    //例如每个眼镜都有自己的id。每一组微调项也有自己的id。
    //不能为空。
    public String id;

    //TYPE_SELECTOR 或者 TYPE_SLIDER
    public int type;

    //如果是selector类型，则它表示当前有无被选中
    public boolean selected = false;

    //每一个图标 或 每一组微调项 背后都对应着具体的配置详情，即下面这三要素。
    public String entityName;
    public String action;
    public JsonObject value;
}
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

- 捏脸时，如果数据是 selector 类型，则修改 AvatarData 的 selected 字段。例如有4种眼镜 A、B、C、D，默认选中的是 A，那么 A 的 selected 为 true，B、C、D 为 false。如果用户选择了眼镜 B，则把 B 的 selected 为 true，A、C、D 为false。
- 捏脸时，如果数据是 slider 类型，则修改 AvatarData 的 value 字段。value 字段是一个 JsonObject，里面是若干对 key-value，把 key-value 中的 value 修改为滑竿的值即可。

## AvatarData 高级说明
AvatarData 中，对捏脸起关键作用的是 entityName、action、value 三个字段。这三个字段的值是 SDK 在解析素材配置时自动填入的。大多数情况下，您不需要了解这三个字段的含义，仅在 UI 层展示时，如果是滑竿类型，则需要解析 value 中的形变 key-value 与 UI 操作进行对应。
其中，AvatarData 要素分为：[entityName](#entityName)、[action](#action) 和 [value](#value) 字段

[](id:entityName)
### entityName 字段

捏脸时，需要明确指定捏哪个部位，例如脸、眼睛、头发、上衣、鞋子 等等。entityName 字段就是描述这些身体部位名称的。以我们的 Demo 素材为例，用 TencentEffectStudio 打开素材工程（xxx.studio）后，可以看到这样一个列表：
<img src="https://qcloudimg.tencent-cloud.cn/raw/06a4860a9b6f1b1cf3350d0dfbfbd68b.png" width=300>
列表里的每一项就是一个身体部位。**命名时，应确保命名在 studio 工程中全局唯一**。

[](id:action)
### action 字段

action 字段表示对 entityName 执行什么操作（action）。SDK 内定义了五种 action，均定义在`AvatarAction.java`中，每种 action 的含义及 value 要求如下：

| action         | 含义                                                         | value要求                                                    |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| changeColor    | 修改当前材质的颜色，包括基础色、自发光色等颜色属性           | JsonObject 类型，必填。详见下文                               |
| changeTexture  | 修改当前材质的贴图，包括颜色纹理贴图、金属粗糙度纹理贴图、AO 纹理贴图、法线纹理贴图、自发光纹理贴图等等 | JsonObject 类型。必填。详见下文 |
| shapeValue     | 修改blendShape形变值，一般用于面部细节形变微调 | JsonObject 类型。里面的key是形变名称，value是float类型的值。必填。详见下文 |
| replace        | 替换子模型，例如替换眼镜、发型、衣服等    | JsonObject 类型。里面描述了新的子模型的3D变换信息、模型路径、材质路径。如果要隐藏当前位置的子模型，则使用null。详见下文 |
| basicTransform | 调整位置、旋转、缩放。一般用于调整摄像机的远近、角度，从而实现模型全身和半身视角的切换 | JsonObject 类型。必填。详见下文                               |

[](id:value)
### value 字段
<dx-tabs>
::: action 等于 changeColor 场景
[](id:changeColor)
**配置示例**
```java
{
	"key": "baseColorFactor",
	"value": [43, 26, 23, 255],
	"subMeshIndex":0,
	"materialIndex":0
}
```
- **key**：必填。修改当前材质的颜色，包括基础色、自发光色、其他自定义颜色等颜色属性。如下图：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/d4f7e9d682a4c2384d4f6dfc67274335.png" width=300>
<br>key 具体取什么值，与当前这个材质使用的 shader 有关。上面的截图使用的是内置的 lit_fade 这个 shader，里面定义的基础色的名称是 baseColorFactor、自发光色是 emissiveFactor，所以 key 值就取其中之一。另外，您还可以直接以文本形式打开材质文件，也可以在里面看到各颜色的 key 值，例如这里使用的是 hair.fmaterial 这个材质文件，在 TEStudio 工程目录中找到并打开它，其内容如下：
<br><img src="https://qcloudimg.tencent-cloud.cn/raw/184145d79f7f10eb34c4ad1396e6a7d2.png" width=500>
<br>SDK 的 `AvatarConfigKey` 类中定义了一些常用的 key 值，您可以引用它们，也可以根据您实际的 shader 内容自定义这里的 key 值。
- **value**：必填。四个值分别是 RGBA。
- **subMeshIndex 和 materialIndex**：非必填。如果不填该字段，则 SDK 内取默认值0。[](id:subMeshIndex)
在 TEStudio中，Mesh(一个可以理解为一个子模型，例如眼镜、头发、面部)一般没有配置子Mesh，且一个 Mesh 只有一份材质，如下图：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/b7e0c6dce61bee40d530ac00b9b3338c.png" width=400>
<br>一些较复杂的 Mesh 可能有多个子 Mesh，一个 Mesh 可以有多份材质，如下图：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/8f5020bc0917a50939eea7ae96a6160f.png" width=400>
<br>因此当我们想要 changeColor 时，就需要明确指出 change 的是哪一个材质的 color。subMeshIndex 和 materialIndex 就是用于定位具体的材质。要确定这两个 index 的值，需要打开素材工程目录下的 template.json，找到当前的 mesh，查看 subMeshConfigs 属性，例如搜索“hair”，定位到 hair 的配置，可以看到如下的 subMesh 配置：
<br><img src="https://qcloudimg.tencent-cloud.cn/raw/85e39b3f3492b2aed27a67bbd3394c60.png" width=600>
<br>然后通过 subMeshIndex 和 materialIndex 的组合就能定位到具体的材质了。
:::
::: action 等于 changeTexture 场景
**[](id:changeTexture)
**配置示例
```java
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
<dx-alert infotype="explain" title="<b>如何填写 switchKey 和 key 的值？</b>">
与 [action ==  changeColor](#changeColor) 时的 key 的取值说明类似，switchKey 和 key 与 material 使用的 shader 有关，例如 TEStudio 里内置 shader 的“颜色纹理”开关及值，对应的就是这里的 baseColorEnableTexture 和 baseColorMap。类似地，还有 AO 纹理、法线纹理等字段。在我们的官方捏脸素材中，我们还自定义了 shader，添加了口红贴图开关、面部贴纸开关等等。
您可以直接以文本形式打开材质文件，在里面看到各个贴图的 switchKey 和 key 值，例如我们 Demo 素材里 face_main 使用的材质文件 face.fmaterial，打开后可以看到如下内容：
<img src="https://qcloudimg.tencent-cloud.cn/raw/883ca597bde464a8752b7460f0af754a.png" width=600>
要修改哪个贴图，就在 switchKey 和 key 两个字段中填入该贴图对应的值。
</dx-alert>
- **subMeshIndex 和 materialIndex**：非必填。如果不填该字段，则 SDK 内取默认值0。详细说明见上文 `action ==  changeColor` 时的说明，具体请参见 [action 等于 changeColor 场景](#subMeshIndex)。
- **textureOptions**：非必填。贴图解析参数。决定贴图的展开和渲染样式。如无特殊配置需求，不建议填写此字段。
:::
::: action 等于 shapeValue 场景
[](id:shapeValue)
**配置示例**：
```java
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
`action == replace` 时的 value 字段描述了子模型的3D变换信息、模型路径、材质路径。可以从素材根目录的 template.json 中找到每个模型的这些信息。
**配置示例**
```java
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
- **position、rotation、scale**：分别描述了模型的位置、旋转、缩放属性。非必填。如果不填，则使用默认值。position 的默认值是0,0,0。rotation 的默认值是0,0,0。scale 的默认值是1,1,1。
>! rotation 的单位是角度，例如45度就填45。它对应的是素材 `template.json` 里的 eEuler 字段的值。
- **meshResourceKey**：必填。描述了模型 mesh 文件的路径。路径可以是 mesh 文件与素材根目录的相对路径（如配置示例所示），也可以是文件在手机上的绝对路径。
- **subMeshConfigs**：必填。如上文对 subMeshIndex 和 materialIndex 的说明，一个 mesh 可以包含多个 subMesh，一个 subMesh 可以包含多个材质。subMeshConfigs 字段配置的就是 mesh 与材质的关联关系。materialResourceKeys 里的取值可以是 material 文件与素材根目录的相对路径（如配置示例所示），也可以是文件在手机上的绝对路径。
:::
::: action 等于 basicTransform 场景
[](id:basicTransform)

**配置示例**：
```java
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
用于调整位置、旋转、缩放。一般用于调整摄像机的远近、角度，从而实现模型全身和半身视角的切换。position、rotation 和 scale 字段的说明请参见 [action 等于 replace 场景](#replace)。
:::
</dx-tabs>

## 配置 Avatar 捏脸换装数据

avatar 属性配置存放在 resources 文件夹下（路径为：`素材/custom_configs/resources`）：
<img src="https://qcloudimg.tencent-cloud.cn/raw/fcc5d2d5173afe13008b8369c63b1a32.png" width=800>

这些配置文件是自动生成的，通常不需要手动配置。自动生成的方式如下：
设计师按照设计规范，用TencentEffectStudio设计好一套形象后，运行我们提供的 resource_generator_gui 这个 App（目前仅支持 MacOS 平台），即可自动生成这些配置，详情请参见 [设计规范说明](https://doc.weixin.qq.com/doc/w3_ALoA-gYYAAgV0MAAbjtQfO4EWXhI9?scode=AJEAIQdfAAoU7K9sLCAGMA3QZFAAg&version=4.0.19.6020&platform=win)。



