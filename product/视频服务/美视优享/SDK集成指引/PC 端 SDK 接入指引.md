## 集成准备
### 开发者环境要求
- 开发工具：VS2019（建议）
- 运行环境依赖：QT5.15.2  + QT VS 插件 

### 配置开发者环境

1. 安装 QT 插件。QT 插件安装成功后界面如下：
 ![](https://qcloudimg.tencent-cloud.cn/raw/9802c87be7f2a567668a2907708f7ff4.png)

2. 配置 QT 插件版本，选择对应的 QT 版本。
 ![](https://qcloudimg.tencent-cloud.cn/raw/d8039c6393f957fab4038d7a5f03be3d.png)

3. 配置工程依赖的 QT 组件。
 ![](https://qcloudimg.tencent-cloud.cn/raw/234df69677a51198fb59f453cb291278.png)

4. 添加头文件和 Xmagic 的 dll 库。
 ![](https://qcloudimg.tencent-cloud.cn/raw/08f51f856240effbc42e40547afd0b60.png)


## 接口概览
Windows 端 SDK 的集成涉及到的接口如下：

<table>
<thead>
<tr>
<th>接口名</th>
<th>描述功能</th>
<th>代码示例</th>
</tr>
</thead>
<tbody><tr>
<td><a href="#setTELicense">setTELicense</a></td>
<td>鉴权接口</td>
<td><a href="#setTELicense1">示例</a></td>
</tr>
<tr>
<td><a href="#createXmagic">createXmagic</a></td>
<td>Xmagic 创建接口</td>
<td><a href="#createXmagic1">示例</a></td>
</tr>
<tr>
<td><a href="#destroyXmagic">destroyXmagic</a></td>
<td>Xmagic 销毁接口</td>
<td><a href="#destroyXmagic1">示例</a></td>
</tr>
<tr>
<td><a href="#updateProperty">updateProperty</a></td>
<td>设置美颜参数（如美颜、动效、化妆等）</td>
<td rowspan="3"><a href="#updateProperty1">示例</a></td>
</tr>
<tr>
<td><a href="#process">process</a></td>
<td>处理美颜接口，返回对应的美颜处理数据（如像素、纹理）</td>
</tr>
<tr>
<td><a href="#setSegmentBg">setSegmentBg</a></td>
<td>设置自定义人像分割</td>
</tr>
<tr>
<td><a href="#setRenderSize">setRenderSize</a></td>
<td>重置输入数据大小</td>
<td>-</td>
</tr>
<tr>
<td><a href="#onPasue">onPasue</a></td>
<td>暂停美颜</td>
<td>-</td>
</tr>
<tr>
<td><a href="#onResume">onResume</a></td>
<td>开始美颜</td>
<td>-</td>
</tr>
</tbody></table>

## 接口使用说明

[](id:setTELicense)
### 鉴权接口

```c++
XMAGIC_API void setTELicense(const char* url, const char* key, int (*TELicenseCallback)(int, const char*));

```

参数含义：

| 参数              | 含义                             |
| ----------------- | -------------------------------- |
| url               | 对应的鉴权证书链接（在后台获取） |
| key               | 对应的鉴权证书 key（在后台获取）  |
| TELicenseCallback | 鉴权成功或者失败的回调           |

鉴权回调 code 的含义：

| 错误码 | 说明                                                    |
| :----- | :------------------------------------------------------ |
| 0      | 成功。Success。                                           |
| -1     | 输入参数无效，例如 URL 或 KEY 为空。                      |
| -3     | 下载环节失败，请检查网络设置。                            |
| -4     | 从本地读取的 TE 授权信息为空，可能是 IO 失败引起。        |
| -5     | 读取 VCUBE TEMP License文件内容为空，可能是 IO 失败引起。 |
| -6     | v_cube.license 文件 JSON 字段不对。请联系腾讯云团队处理。 |
| -7     | 签名校验失败。请联系腾讯云团队处理                      |
| -8     | 解密失败。请联系腾讯云团队处理                          |
| -9     | TELicense 字段里的 JSON 字段不对。请联系腾讯云团队处理。  |
| -10    | 从网络解析的TE授权信息为空。请联系腾讯云团队处理。        |
| -11    | 把 TE 授权信息写到本地文件时失败，可能是 IO 失败引起。      |
| -12    | 下载失败，解析本地 asset 页失败。                         |
| -13    | 鉴权失败。                                                |
| 其他   | 请联系腾讯云团队处理。                                    |


[](id:createXmagic)
### 创建 Xmagic 接口

```c++
XMAGIC_API IXmagic* createXmagic(std::string& resDir, int width, int height);
```

参数含义：

| 参数   | 含义                                |
| ------ | ----------------------------------- |
| resDir | 对应的资源文件（sdk依赖的资源路径） |
| width  | 处理数据宽                          |
| height | 处理数据高                          |


[](id:destroyXmagic)
### 销毁 Xmagic 接口

```c++
XMAGIC_API void destroyXmagic(IXmagic** xmagic);
```


[](id:updateProperty)
### 设置美颜参数

```c++
virtual void updateProperty(XmagicProperty* property) = 0;
```

参数含义：

| 参数     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| category | 美颜类型，包括以下几种：<ul style="margin:0;"><li>美颜：BEAUTY = 0</li><li>美体：BODY_BEAUTY</li><li>滤镜：LUT</li><li>动效：MOTION</li><li>人像分割：SEGMENTATION</li><li>化妆：MAKEUP</li></ul>|
| resPath  | 对应设置资源的地址（如动效、化妆、人像分割等）                   |
| effKey   | 美颜的 key                                                    |
| effValue | 美颜的值                                                     |
| isAuth   | 默认 true                                                     |


[](id:process)
### 处理美颜（像素）

```c++
virtual void process(YTImagePixelData* srcImage, YTImagePixelData* dstImage) = 0;

```

参数说明：

| 参数     | 说明           |
| -------- | -------------- |
| srcImage | 输入的美颜数据 |
| dstImage | 输出的美颜数据 |



YTImagePixelData 结构说明：

```c++
struct YTImagePixelData {
		/// 字段含义：像素格式
		PixelFormat pixelFormat;

		/// 字段含义
		uint8_t* data;

		/// 字段含义：数据的长度，单位是字节
		int32_t length;

		/// 字段含义：宽度
		int32_t width;

		/// 字段含义：高度
		int32_t height;

		YTImagePixelData() : pixelFormat(PixelFormat::PixelFormatRGBA32), data(nullptr), length(0), width(0), height(0) {}
	};
```


#### 处理美颜纹理，返回对应的处理纹理

```
virtual int process(int textureId, int width, int height) = 0;
```

参数说明：

| 参数      | 说明         |
| --------- | ------------ |
| textureId | 输入的纹理 ID |
| width     | 纹理宽度    |
| height    | 纹理高度   |


[](id:setSegmentBg)
### 设置自定义人像分割

```c++
virtual void setSegmentBg(std::string &segmentBgName ,int segmentBgType ,int timeOffset) = 0;
```

参数说明

| 参数          | 说明                             |
| ------------- | -------------------------------- |
| segmentBgName | 自定义人像分割路径                     |
| segmentBgType | 设置背影类型（0为图片，1为视频） |
| timeOffset    | 如果为视频，设置视频播放时长     |


[](id:setRenderSize)
### 重置输入大小

```c++
virtual void setRenderSize(int width, int height) = 0;
```



参数说明：

| 参数   | 说明       |
| ------ | ---------- |
| width  | 重置后的宽度 |
| height | 重置后的高度 |


[](id:onPasue)
### 暂停美颜

```c++
virtual void onPasue() = 0;
```


[](id:onResume)
### 开始美颜

```
virtual void onResume() = 0;
```



## 代码示例
>?以下仅为部分示例代码。

[](id:setTELicense1)
### 鉴权接口
```c++
//鉴权接口
	auto respCallback = [](
		int ret, const char* data) -> int {
			int retCode = ret;
			const char* msg = data;
			return 0;
	};

	setTELicense("url", "key", respCallback);
```

[](id:createXmagic1)
### 创建 Xmaigc
```c++
//创建Xmaigc
	std::string exeFilePath = "资源位置";
    IXmagic* xmagic = createXmagic(exeDirectory, 720, 1280);

```

[](id:destroyXmagic1)
### 销毁 Xmaigc
```c++
//销毁
if (xmagic) {
    destroyXmagic(&xmagic);
}
```

[](id:updateProperty1)
### 设置属性和输出
```c++
//设置属性和输出
    YTImagePixelData src,dst;
	src.width = 720;
	src.height = 1280;
	src.length = 4 * 720 * 1280;
	src.pixelFormat = PixelFormat::PixelFormatRGBA32;
	//uint8_t* rgbaBuffer = (uint8_t*)malloc(src.length);
	//int w = 0, h = 0, comp = 0;
	uint8_t* imageData;
	int w = 0, h = 0, comp = 0;
	stbi_set_flip_vertically_on_load(false);  // SDK要求输入的图是倒置的，否则有问题
	imageData = stbi_load(path.c_str(), &w, &h, &comp, STBI_rgb_alpha);
	src.data = imageData;

	dst.width = 720;
	dst.height = 1280;
	dst.length = 4 * 720 * 1280;
	dst.pixelFormat = PixelFormat::PixelFormatRGBA32;
	uint8_t* rgbaBuffer = (uint8_t*)malloc(dst.length);//这个要释放
	dst.data = rgbaBuffer;

    std::string bgPath = exeDirectory + "bg.jpg";
	xmagic->setSegmentBg(bgPath, 0, 0);

	XmagicProperty property;
	property.category = Category::SEGMENTATION;
	property.resPath = exeDirectory + "segmentMotionRes.bundle/video_empty_segmentation/template.json";
	xmagic->updateProperty(&property);


	for(int i =0; i < 2; i++){
		xmagic->process(&src, &dst);
	}
```



