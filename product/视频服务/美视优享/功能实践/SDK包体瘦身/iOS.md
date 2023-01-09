## 资源动态下载
为了减少包大小，您可以将 SDK 所需的模型资源和动效资源 MotionRes（部分基础版 SDK 无动效资源）改为联网下载。在下载成功后，将上述文件的路径设置给 SDK。

1. 把美颜资源的 ZIP 包上传至云端，生成下载 URL。例如：`https://服务器地址/LightCore.bundle.zip`。
2. 在工程里面使用生成的 URL 下载文件并解压到沙盒（例如：沙盒路径 `Document/Xmagic`）。此时 Document/Xmagic 文件夹里面有 SDK 需要的资源。
![](https://qcloudimg.tencent-cloud.cn/raw/f90fe608cc12156a3b4b778f0ad4d969.png)   
3. SDK 初始化时，在 root_path 字段传入上一步的沙盒路径。
```objectivec
 NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",
                              @"root_path":_filePath ,//_filePath为美颜资源下载到本地后的父目录:Ducument/Xmagic,
                              @"tnn_"
                              @"beauty_config":beautyConfigJson
 };
 // Init beauty kit                                 @"root_path":Ducument/Xmagic,
 self.beautyKit = [[XMagic alloc] initWithRenderSize:_inputSize assetsDict:assetsDict];
```
4. 设置美颜面板各个美颜效果的 icon，在下载的资源文件里面获取对应的 image。
```objectivec
NSMutableArray *arrayModels = [NSMutableArray array];
for (NSDictionary* dict in motionArray) {
	BeautyCellModel* model = [BeautyCellModel beautyWithDict:dict];
	// Load default mainbundle path of motionres
	if ([model.title isEqualToString:NSLocalizedString(@"item_none_label",nil)]) {
		model.icon = [NSString stringWithFormat:@"%@/%@.png", [[NSBundle mainBundle] bundlePath], model.key];
		[arrayModels addObject:model];
	} else {
		if(_useNetResource && _filePath != nil){ //使用网络资源时
			NSString *DirPath = [_filePath stringByAppendingPathComponent:@"2dMotionRes.bundle/"]; //获取美颜资源的绝对路径
			model.icon = [NSString stringWithFormat:@"%@/%@/template.png", DirPath, model.key];
		}else{
			model.icon = [NSString stringWithFormat:@"%@/%@/template.png", [[NSBundle mainBundle] pathForResource:@"2dMotionRes" ofType:@"bundle"], model.key];
		}
		if ([fileManager fileExistsAtPath:model.icon]) {
			[arrayModels addObject:model];
		}
	}
}
```
5. 设置美颜效果的参数传递（参数的具体设置请参见 [API 文档](https://cloud.tencent.com/document/product/616/76025)）：
```objectivec
/// @brief 配置美颜各种效果
/// @param propertyType 效果类型 字符串：beauty, lut, motion
/// @param propertyName 效果名称
/// @param propertyValue 效果数值
/// @param extraInfo 预留扩展, 附加额外配置dict
/// @return 成功返回0，失败返回其他
/// @note 具体说明
/**
| 效果类型 | 效果名称 | 效果值 | 说明  | 备注 |
| :---- | :---- |:---- | :---- | :---- |
|  beauty  | 美颜id名称 | 美颜效果强度数值 |美颜类型配置接口 | 无 |
|  lut  | 滤镜路径+滤镜名称 | 滤镜强度数值 | 滤镜类型配置接口 | 无 |
|  motion  | 动效路径名称 | 动效路径 | 动效类型配置接口| **注意**：如果资源中有zip，请确保传入动效路径为可写路径，否则跟app包走需要手动unzip才可以使用 |
**/
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```

## 示例
### 设置美颜效果
“美颜”和“美体”的特效，不需要做处理，在 SDK 内部会自动使用下载的资源文件。以使用美颜中的美白效果为例，SDK 传参示例：
```objectivec
[self.beautyKitRef configPropertyWithType:@"beauty" withName:@"beauty.whiten" withData:@"30" withExtraInfo:nil];
```
此时，传入到 SDK 的各参数的值分别是：

| 字段          | 值            |
| ------------- | ------------- |
| propertyType  | beauty        |
| propertyName  | beauty.whiten |
| propertyValue | 30            |
| extraInfo     | nil           |

### 设置滤镜效果
需要对 key 做处理，可以使用内置的本地美颜资源或者网络下载到本地以后的美颜资源：
```objectivec
NSString *key = [_model.lutIDs[index] path];
if (key != nil) {
    key = [@"lut.bundle/" stringByAppendingPathComponent:key];//滤镜效果图片的相对路径
}
if(_useNetResource && _filePath != nil){ //如果使用下载的美颜资源
    key = [_filePath stringByAppendingPathComponent:key];//生成效果图片的绝对路径
}
[self.beautyKitRef configPropertyWithType:@"lut" withName:key withData:[NSString 
stringWithFormat:@"%f",value] withExtraInfo:nil];
```

### 设置滤镜中的白皙效果
使用本地资源和网络资源的传参示例：

| 字段          | 使用本地资源时传入的参数 | 使用网络资源时传入的参数                                     | 备注     |
| ------------- | ------------------------ | ------------------------------------------------------------ | -------- |
| propertyType  | lut                      | lut                                                          |     -     |
| propertyName  | lut.bundle/n_baixi.png   | `/var/mobile/Containers/Data/Application/25C7D01A-73F6-4F1B-AEB6-5EE03A221D18/Documents/Xmagic/lut.bundle/n_baixi.png` | 文件路径 |
| propertyValue | 60.000000                | 60.000000                                                    |    -      |
| extraInfo     | null                     | null                                                         |      -    |

### 设置动效、美妆、分割效果
需要对 propertyValue 字段做处理，可以使用内置的本地美颜资源或者网络下载到本地以后的美颜资源。
```objectivec
NSString *key = [_model.motionIDs[index] key];
        NSString *path = [_model.motionIDs[index] path];
        NSString *motionRootPath = path==nil?[[NSBundle mainBundle] pathForResource:@"MotionRes" ofType:@"bundle"]:path;
        if(_useNetResource && _filePath != nil){//如果使用下载的美颜资源
            motionRootPath = [_filePath stringByAppendingPathComponent:@"2dMotionRes.bundle"];//生成2dMotionRes的绝对路径
        }
        [self.beautyKitRef configPropertyWithType:@"motion" withName:key withData:motionRootPath withExtraInfo:nil];
```

### 设置2D动效—可爱涂鸦的效果
使用本地资源和网络资源的传参示例：

| 字段          | 使用本地资源时传入的参数 | 使用网络资源时传入的参数 | 备注     |
| ------------- | ------------- | ------------- | -------- |
| propertyType  | motion | motion |        -  |
| propertyName  | video_keaituya | video_keaituya |       -   |
| propertyValue | `/private/var/containers/Bundle/Application/FD2D7912-E58E-4584-B7E4-8715B8D2338F/BeautyDemo.app/2dMotionRes.bundle` | `/var/mobile/Containers/Data/Application/25C7D01A-73F6-4F1B-AEB6-5EE03A221D18/Documents/Xmagic/2dMotionRes.bundle` | 文件路径 |
| extraInfo     | nil | nil |     -     |

