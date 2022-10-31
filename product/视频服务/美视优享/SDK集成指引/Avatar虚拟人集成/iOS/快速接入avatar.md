由于 Avatar 是腾讯特效的部分功能，所以需要先集成腾讯美颜特效 SDK，再加载 Avatar 素材即可。若未接入腾讯美颜特效 SDK，可参考 [ 独立集成腾讯特效 >](https://cloud.tencent.com/document/product/616/65894) 进行了解与集成。

## 步骤1：准备 Avatar 素材
1. 集成腾讯特效 SDK。
2. 在官网下载对应的 Demo 工程，并解压。
3. 将 Demo 中的 `BeautyDemo/bundle/avatarMotionRes.bundle` 素材文件复制到您的工程中。

## 步骤2：接入 Demo 界面
### 接入方法
1. 在项目中使用与 BeautyDemo 一样的 Avatar 操作界面。
2. 复制 Demo 中 `BeautyDemo/Avatar` 文件夹下的所有类到您的工程中，添加如下代码即可：
```objective-c
	 AvatarViewController *avatarVC = [[AvatarViewController alloc] init];
	 avatarVC.modalPresentationStyle = UIModalPresentationFullScreen;
	 avatarVC.currentDebugProcessType = AvatarPixelData; // 图像或者纹理Id方式
	 [self presentViewController:avatarVC animated:YES completion:nil];
```

### Demo 界面说明

#### 1. Demo UI 界面[](id:demoui)
<img src="https://qcloudimg.tencent-cloud.cn/raw/738b3b8c78db02f370a158b1090c9d92.png" style="zoom:30%;" />

#### 2. 实现方案
操作面板数据是解析一份 JSON 文件获得的，Demo 中的这份文件放在 `BeautyDemo/Avatar/` 目录。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7ae4858642c7dedcba05514a2ffed06a.png" style="zoom:100%;" />
- **JSON 结构与 UI 面板对应得关系**
	- head 为第一个 icon 选中的内容：
	<img src="https://qcloudimg.tencent-cloud.cn/raw/733a8cf85285c56632f1a213523be893.png" width=900 />
	- subTabs 对应右侧二级菜单：
	<img src="https://qcloudimg.tencent-cloud.cn/raw/347db8c590313a8e8b950be793e984f0.png" width=900 />
	- items 对应右侧三级菜单：<br>
	<img src="https://qcloudimg.tencent-cloud.cn/raw/09ec311908c93b8e31a7747a0304cdfd.png" width=900 />
- **面板解析出来得数据关联 SDK 接口获取的 Avatar 对象数据**
下图中上半部分为 SDK 获取得 avatar 字典（key 为 categor，value 为 avatar 数组），下半部分为面板的数据。当点击面板的选项时，从面板二级标题获取 category（**红框标记**），通过该 cetogory 可以在 SDK 返回的 avatar 字典内获取到对应的avatarData数组。从面板三级标题处获取 ID（**蓝框标记**），通过该 ID 可以在 avatarData 数组匹配到对应的 avatarData 对象，将此对象传入 SDK 的 updateAvatar 接口即可完全捏脸。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/e3970084f75f10bf6713b9084b6fd63c.png" width=900 />


#### 3. 修改标题的图标/文字
修改 [Demo UI](#demoui) 图片所示 JSON 文件，例如修改**头部**展示的 icon，则修改下图红框中的 iconUrl 与 checkedIconUrl 即可。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e597044b64447ca676e7bb407070b945.png" width=900 />

## 步骤3：自定义捏脸功能
可参考 `BeautyDemo/Avatar/Controller` 中的 **AvatarViewController** 相关代码。
>? 接口说明请参见 [Avatar SDK 说明](https://cloud.tencent.com/document/product/616/81995)。

1. 创建 xmagic 对象，设置 Avatar 默认模版。
```objectivec
- (void)buildBeautySDK {

	CGSize previewSize = CGSizeMake(kPreviewWidth, kPreviewHeight);
	NSString *beautyConfigPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) lastObject];
	beautyConfigPath = [beautyConfigPath stringByAppendingPathComponent:@"beauty_config.json"];
	NSFileManager *localFileManager=[[NSFileManager alloc] init];
	BOOL isDir = YES;
	NSDictionary * beautyConfigJson = @{};
	if ([localFileManager fileExistsAtPath:beautyConfigPath isDirectory:&isDir] && !isDir) {
			NSString *beautyConfigJsonStr = [NSString stringWithContentsOfFile:beautyConfigPath encoding:NSUTF8StringEncoding error:nil];
			NSError *jsonError;
			NSData *objectData = [beautyConfigJsonStr dataUsingEncoding:NSUTF8StringEncoding];
			beautyConfigJson = [NSJSONSerialization JSONObjectWithData:objectData                                                           options:NSJSONReadingMutableContainers
																															 error:&jsonError];
	}
	NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",
															 @"root_path":[[NSBundle mainBundle] bundlePath],
															 @"tnn_"
															 @"beauty_config":beautyConfigJson
	};
	// Init beauty kit
	self.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];
	// Register log
	[self.beautyKit registerSDKEventListener:self];
	[self.beautyKit registerLoggerListener:self withDefaultLevel:YT_SDK_ERROR_LEVEL];

	// 传入素材文件对应的路径即可加载avatar默认形象
	AvatarGender gender = self.genderBtn.isSelected ? AvatarGenderFemale : AvatarGenderMale;
	NSString *bundlePath = [self.resManager avatarResPath:gender];
	[self.beautyKit loadAvatar:bundlePath exportedAvatar:nil];

}
```
2. 获取素材的 Avatar 源数据。
```objectivec
@implementation AvatarViewController
_resManager = [[AvatarResManager alloc] init];
NSDictionary *avatarDict = self.resManager.getMaleAvatarData;
@end


@implementation AvatarResManager

- (NSDictionary *)getMaleAvatarData
{
	if (!_maleAvatarDict) {
			NSString *resDir = [self avatarResPath:AvatarGenderFemale];
			NSString *savedConfig = [self getSavedAvatarConfigs:AvatarGenderMale];
			// 通过sdk接口解析出素材源数据
			_maleAvatarDict = [XMagic getAvatarConfig:resDir exportedAvatar:savedConfig];
	}
	return _maleAvatarDict;
}
@end
```
3. 捏脸操作。
```objectivec
// 从sdk接口解析出来的素材源数据中拿到想要形象的avatar对象，传入sdk
NSMutableArray *avatars = [NSMutableArray array];
// avatarConfig是从sdk接口getAvatarConfig:exportedAvatar:获取的其中一个avatar对象
[avatars addObject:avatarConfig];
// 捏脸/换装接口，调用后实时更新当前素材呈现出的形象
[self.beautyKit updateAvatar:avatars];
```
4. 导出捏脸字符串：
将当前 Avatar 配置的对象导出为字符串，可自定义存储。
```objectivec
- (BOOL)saveSelectedAvatarConfigs:(AvatarGender)gender
{
	NSMutableArray *avatarArr = [NSMutableArray array];
	NSDictionary *avatarDict = gender == AvatarGenderMale ? _maleAvatarDict : _femaleAvatarDict;
	// 1、遍历找出选中的avatar对象
	for (NSArray *arr in avatarDict.allValues) {
			for (AvatarData *config in arr) {
					if (config.type == AvatarDataTypeSelector) {
							if (config.isSelected) {
									[avatarArr addObject:config];
							}
					} else {
							[avatarArr addObject:config];
					}
			}
	}
	// 2、调用sdk接口将选中的avatar对象导出为字符串
	NSString *savedConfig = [XMagic exportAvatar:avatarArr.copy];
	if (savedConfig.length <= 0) {
			return NO;
	}
	NSError *error;
	NSString *fileName = [self getSaveNameWithGender:gender];
	NSString *savePath = [_saveDir stringByAppendingPathComponent:fileName];
	// 判断目录是否存在，不存在则创建目录
	BOOL isDir;
	if (![[NSFileManager defaultManager] fileExistsAtPath:_saveDir isDirectory:&isDir]) {
			[[NSFileManager defaultManager] createDirectoryAtPath:_saveDir withIntermediateDirectories:YES attributes:nil error:nil];
	}
	// 3、将导出的字符串写入沙盒，下次取出来可用
	[savedConfig writeToFile:savePath atomically:YES encoding:NSUTF8StringEncoding error:&error];
	if (error) {
			return NO;
	}
	return YES;
}
```
5. 切换虚拟与真实背景。
```objectivec
- (void)bgExchangeClick:(UIButton *)btn
{
	btn.selected = !btn.isSelected;
	NSDictionary *avatarDict = self.resManager.getFemaleAvatarData;
	NSArray *array = avatarDict[@"background_plane"];
	AvatarData *selConfig;
	// 背景实际上也是一个avatar对象，category为background_plane，替换背景就是设置不同的avatar对象
	for (AvatarData *config in array) {
			if ([config.Id isEqual:@"none"]) {
					if (btn.selected) {
							selConfig = config;
							break;
					}
			} else {
					selConfig = config;
			}
	}
	[self.beautyKit updateAvatar:@[selConfig]];
}
```
