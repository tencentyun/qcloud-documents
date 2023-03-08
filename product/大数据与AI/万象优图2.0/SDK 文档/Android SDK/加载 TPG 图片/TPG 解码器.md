
本文提供直接使用解码器解码 TPG 图片的方法以及简单加载本地 TPG 图片。


### 安装 TPG SDK

**使用 Gradle 集成**
>? bintray 仓库已经下线，万象相关 SDK 已经迁移到 mavenCentral，引用路径和之前不同，您在更新的时候请使用新的引用路径。
>

在项目级别（通常是根目录下）的 `build.gradle` 中添加：
```
repositories {
    google()
    // 增加这行
    mavenCentral() 
}
```

在app或者其他类库的 `build.gradle` 中添加：

```
implementation 'com.qcloud.cos:tpg:1.3.8'    
```

安装时会自动包含 SO 库，建议在 Module 的 build.gradle 文件中使用 NDK 的“abiFilter”配置，设置支持的 SO 库架构。

```
defaultConfig {
    ndk {
        // 设置支持的 SO 库架构
        abiFilters 'armeabi' //, 'x86', 'armeabi-v7a', 'x86_64', 'arm64-v8a'
    }
}
```

### 直接使用解码器解码

- 判断是否是 TPG 格式以及动图格式。
```
import com.tencent.tpg.Tpg;  

// 图片的字节数组
byte[] buffer = new byte[XXX];
// 是否是 TPG 格式
boolean isTPG = Tpg.isTPG(buffer);
// 是否是 TPG 动图 
boolean isTPGAnimation = Tpg.isTPGAnimation(buffer);
```

- 解码 TPG 图片。
```
import com.tencent.tpg.Tpg;  

// 图片的字节数组
byte[] buffer = new byte[XXX];

// 原图解码
Bitmap bitmap = Tpg.decode(buffer);

// 宽度等比解码
// 目标宽度
int dstWidth = 500; 
Bitmap bitmap = Tpg.decode(buffer, dstWidth);

// 区域缩放解码
// 区域左上角x坐标
int x = 0;
// 区域左上角y坐标
int y = 0;
// 区域宽度
int width = 100;
// 区域高度
int height = 100;
// 缩放比, 大于1的时候才生效，小于等于1的情况下不作缩放
int inSampleSize = 2;
Bitmap bitmap = Tpg.decode(buffer, x, y, width, height, inSampleSize);
```

### 简单加载本地图片

应用内置的资源，例如 assets、drawable、raw 等，使用 TPG 格式可以有利于减小安装包大小。

```
//加载 Assets 中的 TPG 图片
TpgImageLoader.displayWithAssets(imageview, assetsName);
//加载 Resource 中的 TPG 图片
TpgImageLoader.displayWithResource(imageview, R.drawable.tpg);
//加载本地文件中的 TPG 图片
TpgImageLoader.displayWithFileUri(imageview, fileUri);
```
