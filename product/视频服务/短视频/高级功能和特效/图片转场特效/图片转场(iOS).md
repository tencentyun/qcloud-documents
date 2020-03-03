 SDK 在4.7版本后增加了图片编辑功能，用户可以选择自己喜欢的图片，添加转场动画、BGM、贴纸等效果。  
接口函数如下：

```
/*
 *pitureList：转场图片列表,至少设置三张图片（tips：图片最好压缩到720P以下（参考 demo 用法），否则内存占用可能过大，导致编辑过程异常）
 *fps：转场图片生成视频后的 fps（15 - 30）
 * 返回值：
 *       0：设置成功；
 *      -1：设置失败，请检查图片列表是否存在，图片数量是否大于等于3张，fps 是否正常；
 */
- (int)setPictureList:(NSArray<UIImage *> *)pitureList fps:(int)fps;

/*
 *transitionType：转场类型，详情见 TXTransitionType
 * 返回值：
 *       duration：转场视频时长（tips：同一个图片列表，每种转场动画的持续时间可能不一样，这里可以获取转场图片的持续时长）；
 */
- (void)setPictureTransition:(TXTransitionType)transitionType duration:(void(^)(CGFloat))duration;
```

- setPictureList 接口用于设置图片列表，最少设置三张，如果设置的图片过多，要注意图片的大小，防止内存占用过多而导致编辑异常。
- setPictureTransition 接口用于设置转场的效果，目前提供了6种转场效果供用户设置，每种转场效果持续的时长可能不一样，这里可以通过 duration 获取转场的时长。  
- 需要注意接口调用顺序，先调用 setPictureList，再调用 setPictureTransition。
- 图片编辑暂不支持的功能：重复、倒放、快速/慢速、片尾水印。其他视频相关的编辑功能，图片编辑均支持，调用方法和视频编辑完全一样。
