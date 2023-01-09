由于 Avatar 只是腾讯特效的部分功能，所以在接入的时需参考特效接入文档，然后加载 Avatar 素材即可。如果您已经接入特效，则忽略下边第一步内容。
1. 按照腾讯特效文档进行接入，请参见 [独立集成腾讯特效](https://cloud.tencent.com/document/product/616/65891)。
2. 按照如下方法加载 Avatar 素材。

## 使用 Avatar 功能具体步骤

###  步骤1：复制 Demo 中的文件
1. 在官网下载对应的demo工程，并解压。
2. 将 Demo 中的 `demo/app/assets/MotionRes/avatarRes` 文件夹复制到您的工程中（和 Demo 位置保持一致）。
3. 复制 Demo 中 `com.tencent.demo.avatar` 文件夹下的所有类到您的工程中。

### 步骤2：添加关键代码
参考 Demo 中的 `com.tencent.demo.avatar.AvatarActivity` 类，添加如下代码
1. 在页面的 xml 文件文件中配置面板信息：
```xml
	<com.tencent.demo.avatar.view.AvatarPanel
			 android:id="@+id/avatar_panel"
			 android:layout_width="match_parent"
			 android:layout_height="300dp"
			 app:layout_constraintBottom_toBottomOf="parent" />
```
2. 在页面中获取面板对象并设置对应的数据回调接口：
```java
 avatarPanel.setAvatarPanelCallBack(new AvatarPanelCallBack() {
					 @Override
					 public void onItemChecked(AvatarIcon avatarIcon) {
							 if (avatarIcon.avatarData == null && URLUtil.isNetworkUrl(avatarIcon.downloadUrl)) {  //此处表示要进行动态下载
									 downloadAvatarData(avatarIcon, () -> updateConfig(avatarIcon));
							 } else {
									 updateConfig(avatarIcon);
							 }
					 }

					 @Override
					 public void onItemValueChange(AvatarIcon avatarIcon) {
							 updateConfig(avatarIcon);
					 }

					 @Override
					 public boolean onShowPage(AvatarPageInf avatarPageInf, AvatarIcon avatarIcon){
							 if ( avatarIcon.avatarData == null && URLUtil.isNetworkUrl(avatarIcon.downloadUrl)) {  //此处表示要进行动态下载
									 downloadAvatarData(avatarIcon, () -> {
											 if(avatarPageInf!=null){
													 avatarPageInf.refresh();
											 }
									 });
									 return false;
							 }
							 return true;
					 }

					 private void updateConfig(AvatarIcon avatarIcon) {
							 if (mXmagicApi != null && avatarIcon != null) {
									 List<AvatarData> avatarConfigList = new ArrayList<>();
									 avatarConfigList.add(avatarIcon.avatarData);
									 mXmagicApi.updateAvatarConfig(avatarConfigList);
							 }
					 }
			 });
```
3. 获取面板数据，并设置给面板：
```java
AvatarResManager.getInstance().getAvatarData(avatarResName, false, allData -> avatarPanel.initView(allData));
```
4. 创建 xmagicApi 对象，并加载捏脸资源：
```java
private void initXMagic() {
		if (mXmagicApi == null) {
				mXmagicApi = XmagicApiWrapper.createXmagicApi(getApplicationContext(), false, null);
				AvatarResManager.getInstance().loadAvatarRes(mXmagicApi, avatarResName, !isCaptureMod);
				if(isCaptureMod){  //如果是拍照捏脸需要手动获取设置的数据，手动设置
						List<AvatarData> avatarDataList = AvatarResManager.getUsedAvatarData(avatarPanel.getMainTabList());
						mXmagicApi.updateAvatarConfig(avatarDataList);
				}
				setAvatarPlaneType();
		} else {
				mXmagicApi.onResume();
		}
}
```
5. 保存 Avatar 属性，可参考 Demo 中的 saveAvatarConfigs 方法：
```java
/**
 * 保存用户设置的属性或者默认属性值
 */
private void saveAvatarConfigs() {
		if (mXmagicApi != null && avatarPanel != null) {
				List<AvatarData> avatarDataList = AvatarResManager.getUsedAvatarData(avatarPanel.getMainTabList());
				new Thread(() -> {
						String content = XmagicApi.exportAvatarConfig(avatarDataList);
						boolean result = FileUtil.writeContentToFile(AvatarResManager.getAvatarConfigsDir(), AvatarResManager.getAvatarConfigsFileName(avatarResName), content);
						String tip = result ? "save avatar data successfully " : "Save avatar data failed";
						runOnUiThread(() -> Toast.makeText(getApplicationContext(), tip, Toast.LENGTH_LONG).show());
				}).start();
		}
}
```
6. 切换背景参考 Demo 中的 changeAvatarBgType 方法：
```java
/**
 * 背景切换
 */
private void changeAvatarBgType() {
		if (currentAvatarType == AvatarResManager.AvatarType.VIRTUAL_BG) {
				currentAvatarType = AvatarResManager.AvatarType.REAL_BG;
		} else {
				currentAvatarType = AvatarResManager.AvatarType.VIRTUAL_BG;
		}
		saveCurrentAvatarType();
		setAvatarPlaneType();
}

/**
 * 设置模型背景类型
 */
private void setAvatarPlaneType() {
		AvatarData avatarData = AvatarResManager
						.getInstance().getAvatarPlaneTypeConfig(avatarResName, currentAvatarType);
		if (mXmagicApi != null && avatarData != null) {
				List<AvatarData> avatarDataList = new ArrayList<>();
				avatarDataList.add(avatarData);
				mXmagicApi.updateAvatarConfig(avatarDataList);
		}
}
```

