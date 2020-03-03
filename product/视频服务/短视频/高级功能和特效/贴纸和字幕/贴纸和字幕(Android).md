## 静态贴纸
设置静态贴纸的方法：
```
public void setPasterList(List pasterList);

// TXPaster 的参数如下：
public final static class TXPaster {
    public Bitmap pasterImage;                                // 贴纸图片
    public TXRect frame;                                      // 贴纸的 frame（注意这里的 frame 坐标是相对于渲染 view 的坐标）
    public long startTime;                                    // 贴纸起始时间(ms)
    public long endTime;                                      // 贴纸结束时间(ms)
}

```
## 动态贴纸
设置动态贴纸的方法：

```
public void setAnimatedPasterList(List animatedPasterList);

// TXAnimatedPaster 的参数如下：
public final static class TXAnimatedPaster {
    public String animatedPasterPathFolder;                  // 动态贴纸图片地址
    public TXRect frame;                                      // 动态贴纸 frame (注意这里的 frame 坐标是相对于渲染 view 的坐标）
    public long startTime;                                    // 动态贴纸起始时间(ms)
    public long endTime;                                      // 动态贴纸结束时间(ms)
    public float rotation;
}
```
Demo示例：

```
List animatedPasterList = new ArrayList<>();
List pasterList = new ArrayList<>();
for (int i = 0; i < mTCLayerViewGroup.getChildCount(); i++) {
    PasterOperationView view = (PasterOperationView) mTCLayerViewGroup.getOperationView(i);
    TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
    rect.x = view.getImageX();
    rect.y = view.getImageY();
    rect.width = view.getImageWidth();
    TXCLog.i(TAG, "addPasterListVideo, adjustPasterRect, paster x y = " + rect.x + "," + rect.y);

    int childType = view.getChildType();
    if (childType == PasterOperationView.TYPE_CHILD_VIEW_ANIMATED_PASTER) {
        TXVideoEditConstants.TXAnimatedPaster txAnimatedPaster = new TXVideoEditConstants.TXAnimatedPaster();

        txAnimatedPaster.animatedPasterPathFolder = mAnimatedPasterSDcardFolder + view.getPasterName() + File.separator;
        txAnimatedPaster.startTime = view.getStartTime();
        txAnimatedPaster.endTime = view.getEndTime();
        txAnimatedPaster.frame = rect;
        txAnimatedPaster.rotation = view.getImageRotate();

        animatedPasterList.add(txAnimatedPaster);
        TXCLog.i(TAG, "addPasterListVideo, txAnimatedPaster startTimeMs, endTime is : " + txAnimatedPaster.startTime + ", " + txAnimatedPaster.endTime);
    } else if (childType == PasterOperationView.TYPE_CHILD_VIEW_PASTER) {
        TXVideoEditConstants.TXPaster txPaster = new TXVideoEditConstants.TXPaster();

        txPaster.pasterImage = view.getRotateBitmap();
        txPaster.startTime = view.getStartTime();
        txPaster.endTime = view.getEndTime();
        txPaster.frame = rect;

        pasterList.add(txPaster);
        TXCLog.i(TAG, "addPasterListVideo, txPaster startTimeMs, endTime is : " + txPaster.startTime + ", " + txPaster.endTime);
    }
}

mTXVideoEditer.setAnimatedPasterList(animatedPasterList);  //设置动态贴纸
mTXVideoEditer.setPasterList(pasterList);                  //设置静态贴纸
```
## 自定义动态贴纸
动态贴纸的本质是：将**一串图片**，按照**一定的顺序**以及**时间间隔**，插入到视频画面中去，形成一个动态贴纸的效果。

#### 封装格式
以 Demo 中一个动态贴纸为例：
```
{
  "name":"glass",                        // 贴纸名称
  "count":6,                             // 贴纸数量
  "period":480,                          // 播放周期：播放一次动态贴纸的所需要的时间(ms)
  "width":444,                           // 贴纸宽度
  "height":256,                          // 贴纸高度
  "keyframe":6,                          // 关键图片：能够代表该动态贴纸的一张图片
  "frameArray": [                        // 所有图片的集合
                 {"picture":"glass0"},
                 {"picture":"glass1"},
                 {"picture":"glass2"},
                 {"picture":"glass3"},
                 {"picture":"glass4"},
                 {"picture":"glass5"}
               ]
}
```
SDK 内部将获取到该动态贴纸对应的 config.json，并且按照 json 中定义的格式进行动态贴纸的展示。

>?该封装格式为 SDK 内部强制性要求，请严格按照该格式描述动态贴纸。

## 添加字幕
### 1. 气泡字幕
您可以为视频设置气泡字幕，我们支持对每一帧视频添加字幕，每个字幕您也可以设置视频作用的起始时间和结束时间。所有的字幕组成了一个字幕列表， 您可以把字幕列表传给 SDK 内部，SDK 会自动在合适的时间对视频和字幕做叠加。

设置气泡字幕的方法为：
```
public void setSubtitleList(List subtitleList);

//TXSubtitle 的参数如下：
public final static class TXSubtitle {
        public Bitmap titleImage;                                // 字幕图片
        public TXRect frame;                                      // 字幕的 frame
        public long startTime;                                    // 字幕起始时间(ms)
        public long endTime;                                      // 字幕结束时间(ms)
}

public final static class TXRect {
        public float x;
        public float y;
        public float width;
}
```

- titleImage：表示字幕图片，如果上层使用的是 TextView 之类的控件，请先把控件转成 Bitmap，具体方法可以参照 demo 的示例代码。
- frame：表示字幕的 frame，注意这个 frame 是相对于渲染 view（initWithPreview 时候传入的 view）的 frame，具体可以参照 demo 的示例代码。
- startTime：字幕作用的起始时间。
- endTime：字幕作用的结束时间。

因为字幕的 UI 逻辑比较复杂，我们已经在 demo 层有一整套的实现方法，推荐客户直接参考 demo 实现， 可以大大降低您的接入成本。

Demo 示例：
```
mSubtitleList.clear();
for (int i = 0; i < mWordInfoList.size(); i++) {
    TCWordOperationView view = mOperationViewGroup.getOperationView(i);
    TXVideoEditConstants.TXSubtitle subTitle = new TXVideoEditConstants.TXSubtitle();
    subTitle.titleImage = view.getRotateBitmap();  //获取Bitmap
    TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
    rect.x = view.getImageX();        // 获取相对 parent view 的 x 坐标
    rect.y = view.getImageY();        // 获取相对 parent view 的 y 坐标
    rect.width = view.getImageWidth(); // 图片宽度
    subTitle.frame = rect;
    subTitle.startTime = mWordInfoList.get(i).getStartTime();  // 设置开始时间
    subTitle.endTime = mWordInfoList.get(i).getEndTime();      // 设置结束时间
    mSubtitleList.add(subTitle);
}
mTXVideoEditer.setSubtitleList(mSubtitleList); // 设置字幕列表
```
### 2.自定义气泡字幕？
**气泡字幕所需要的参数**
* 文字区域大小： top、left、right、bottom
* 默认的字体大小
* 宽、高

>?以上单位均为 px。

#### 封装格式
由于气泡字幕中携带参数较多，我们建议您可以在 Demo 层封装相关的参数。如腾讯云 Demo 中使用的 json 格式封装。

```
{
  "name":"boom",     // 气泡字幕名称
  "width": 376,      // 宽度
  "height": 335,     // 高度
  "textTop":121,     // 文字区域上边距
  "textLeft":66,     // 文字区域左边距
  "textRight":69,    // 文字区域右边距
  "textBottom":123,  // 文字区域下边距
  "textSize":40      // 字体大小
}
```
>?该封装格式用户可以自行决定，非 SDK 强制性要求。

#### 字幕过长
**字幕若输入过长时，如何进行排版才能够使字幕与气泡美观地合并？**
我们在 Demo 中提供了一个自动排版的控件。若在当前字体大小下，字幕过长时，控件将自动缩小字号，直到能够恰好放下所有字幕文字为止。
您也可以修改相关控件源代码，来满足自身的业务要求。
