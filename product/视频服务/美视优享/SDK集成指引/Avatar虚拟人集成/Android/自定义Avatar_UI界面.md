## Demo UI 说明
<img src="https://qcloudimg.tencent-cloud.cn/raw/738b3b8c78db02f370a158b1090c9d92.png" width=300>

## 实现方式
面板配置信息可存放在任何路径， Demo 中存放在 assets，Demo 在首次使用面板文件时会复制到安装目录下。
![](https://qcloudimg.tencent-cloud.cn/raw/5d189eae1fce1f079ed33394309144cb.png)

**Json 结构和 UI 面板对应关系**：

- 左侧 item 对应右侧页面一级菜单，head 为第一个 icon 选中的内容：
<img src="https://qcloudimg.tencent-cloud.cn/raw/c82ae2cc6f05ee85bab3ac9e4810a3c7.png" width=800>
- 左侧红框 subTabs 对应右侧二级菜单：
<img src="https://qcloudimg.tencent-cloud.cn/raw/4ea127296fe999c32ae10eda949b8929.png" width=800>
- 左侧的 icon 数据在 resources 文件夹中进行配置，右侧展示的是面板的配置数据，两者之间是通过面板数据中的 **category 进行关联**，SDK 会解析 resources 文件夹中的数据，放入对应的 map 中，map 的 key 是 category 的值，所以在 Demo 中解析完 `panel.json` 文件后，可通过 SDK 提供的方法获取数据进行关联。
![](https://qcloudimg.tencent-cloud.cn/raw/bf53c4e59cd8cdbae61649eeba74399e.png)

## Demo 重要类说明
路径：`com.tencent.demo.avater.AvatarResManager.java`

### 1. 加载 Avatar 资源
```java
/**
     * 用于加载Avatar 资源
     *
     * @param xmagicApi      XmagicApi对象
     * @param avatarResName  名称
     * @param avatarSaveData 加载模型的默认配置，如果没有则传null
     */
    public void loadAvatarRes(XmagicApi xmagicApi, String avatarResName, String avatarSaveData)
```

### 2. 获取面板数据
```java
 /**
     * 获取avatar面板数据，
     *
     * @param avatarResName      avatar素材名称
     * @param avatarDataCallBack 由于此方法会访问文件，所以会在子线程中进行文件操作，获取到数据后会在主线程回调
     *                           返回的数据是已经包含了resources文件夹下的数据
     */
    public void getAvatarData(String avatarResName, String avatarSaveData, LoadAvatarDataCallBack avatarDataCallBack)
```

### 3. 从面板数据中解析出用户设置的属性或默认属性
```java
//从面板的配置文件中解析出用户设置的属性或默认属性
public static List<AvatarData> getUsedAvatarData(List<MainTab> mainTabList) 
```

###  4. 获取切换模型背景数据
```java
 /**
     * 获取对应的plane Config数据
     *
     * @param avatarResName 资源名称
     * @param avatarType    背景类型
     * @return
     */
    public AvatarData getAvatarPlaneTypeConfig(String avatarResName, AvatarBgType avatarBgType) 
```

## 附录

[MainTab.java](#maintab)、[SubTab.java](#subtab) 中的字段介绍。

### MainTab

| 字段 | 类型  | 是否必填 | 含义  |
| ----------- | ----------- | ----------- | ----------- |
| id   | String| 是 | 主菜单唯一标识，用于区分主菜单，所以需要全局唯一 |
| label| String| 否 | 以及 tab 上展示的名称（ Demo 中暂时不展示       |
| iconUrl        | String| 是 | 图片地址，未选中时的图片地址 |
| checkedIconUrl | String| 是 | 图片地址，选中时的图片地址 |
| subTabs | [SubTab 类型列表](#subtab) | 是       | 二级菜单列表 |

### SubTab

| 字段 | 类型     | 是否必填 | 含义 |
| --------------- | -------- | -------- | ----------- |
| label | String   | 是       | 二级菜单名称 |
| category | String   | 是       | 二级菜单的分类类型，在 SDK 中 `com.tencent.xmagic.avatar.AvatarCategory` 类中定义 |
| relatedCategory | String   | 否       | 用于标识依赖关系，例如：发型和发色有依赖关系，发型修改的时还需使用上次用户设置过的发色，这个时候就需要在发型的中设置此字段，值是发色中的 category 字段的值（依赖关系暂时只存在 type 值为 TYPE_SELECTOR 类型的数据） |
| avatarDataList  | 列表类型 | 是 | [AvatarIcon 类型列表数据](#avataricon) |

### AvatarIcon

| 字段 | 类型 | 是否必填 | 含义 |
| ----------- | ----------- | ----------- | ----------- |
|id| String| 是 |每一个属性的 ID，和 SDK 返回的 AvatarData 数据中的 ID 相对应 |
| icon | String| 是       | 图片地址或者 ARGB 色值（”#FF0085CF“）    |
| type | Int   | 是       | UI 展示类型，`AvatarData.TYPE_SLIDER` 为滑竿类型，`AvatarData.TYPE_SELECTOR` 为 icon 类型 |
| selected    | boolean | 是       | 如果 type 为 AvatarData.TYPE_SELECTOR 类型，此字段用于表示此item是否被选中 |
| downloadUrl | String| 否 | 配置文件的下载地址，用于动态下载配置文件 |
| category    | String| 是 | 和 SubTab 中的 category 同义             |
| labels | Map&lt;String, String&gt; | 否       | 在 type 为 AvatarData.TYPE_SLIDER 类型时有值，存放面板左侧展示的 label |
| avatarData  | AvatarData      | 是       | SDK 定义了捏脸属性操作类 |

