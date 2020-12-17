# 轨道元素

> 决定展示内容的容器，只能承载云媒资，关于云媒资请参考[文档](https://cloud.tencent.com/document/product/1156/43243)

## 元素类型

主要支持以下类型素材:

| 名称                  | 说明                           |
| --------------------- | ------------------------------ |
| [video](#video)       | 视频。                         |
| [audio](#audio)       | 音频。                         |
| [image](#image)       | 图片。                         |
| [title](#title)       | 作为内容填充的文本文字。       |
| [subtitle](#subtitle) | 字幕，语音内容的文字展示形式。 |
| [frame](#frame)       | 特效。                         |

## 元素类型及轨道关系

| 资源类型   | 元素子类型     | 元素子类型    | 所在轨道类型            |
| ---------- | -------------- | ------------- | ----------------------- |
| 自由文字   | advanced_title | advanced_text | title                   |
| 动效文字   | title          | text          | title                   |
| 图文特效   | title          | text_image    | title                   |
| 音频       | audio          | audio         | audio                   |
| 贴片       | image          | sticker       | image                   |
| 马赛克     | frame          | frame         | frame                   |
| 图片       | image          | image         | video                   |
| 视频、特效 | video          | video         | video                   |
| 转场       | transition     | transition    | video                   |
| 字幕       | subtitle       | subtitle      | subtitle                |
| 风格       | frame          | style         | frame, subType="shader" |

## 必要属性

必要属性如下:

```js
let trackItem = {
  id: "61afa77e-8c1f-4fcb-8255-f4d8f4617d0b", //元素ID,单个剪辑协议内唯一，如果使用我们的sdk，可以不关注此id的的生产。
  start_time: 880, //剪辑时间线上的开始时间。
  type: "video", //素材类型.表明当前素材类型,以决定如何处理.
  duration: 3000, //播放持续时间。
  asset_id: "731195088946733255", //云媒资id。
};
```

## 位置计算

默认的舞台分辨率为`960 * 540`，采用直角坐标系确定元素位置，以左上角为原点(0,0)。整个舞台位于坐标系第一象限内。元素的`position`属性默认描述元素中心点。例如一张`100*100`的图片紧贴原点完整放置在舞台上，那么它的`position`值为(50,50)。

### position 位置信息:

| 属性值 | 类型   | 说明     |
| :----- | :----- | :------- |
| `x`    | number | 横坐标。 |
| `y`    | number | 纵坐标。 |

---

### section 截取信息:

> 仅在自身有时间线的元素上存在，例如 音频，视频。

| 属性值 | 类型   | 说明                            |
| :----- | :----- | :------------------------------ |
| `from` | number | 片段起始时间戳，单位为毫秒 ms。 |
| `to`   | number | 片段末尾时间戳，单位为毫秒 ms。 |

---

### video

该种类的素材我们提供了更丰富的处理形式，具体请参考[多媒体处理](#多媒体处理)，元素示例如下：

```js
let videoItem = {
  id: "45ea83ad-a770-4e4a-a9b2-93cdefa4d369",
  start_time: 1440, //剪辑时间线上的开始时间
  duration: 7880, //剪辑时间线上的持续时间
  type: "video", //素材类型
  section: {
    // 素材时间戳截取，素材有自身时间线时，才有此属性。
    from: 0,
    to: 7880,
  },
  asset_id: "5f6464c6ccbc8d0001fc308b",
  width: 540,
  height: 304,
  position: {
    x: 270,
    y: 480,
  },
  operations: [
    //对该元素的操作处理，这里是指的旋转，具体请参考多媒体处理章节。
    {
      type: "image_rotate",
      params: {
        angle: 0,
      },
    },
  ],
};
```

### image

该种类的素材我们提供了更丰富的处理形式，具体请参考[多媒体处理](#多媒体处理)，图片除开没有自身时间线外，与视频类型素材基本一致，示例如下：

```js
let imageItem = {
  id: "45ea83ad-a770-4e4a-a9b2-93cdefa4d369",
  start_time: 1440, //剪辑时间线上的开始时间
  duration: 7880, //剪辑时间线上的持续时间
  type: "image", //素材类型
  asset_id: "5f6464c6ccbc8d0001fc308b",
  width: 540,
  height: 304,
  position: {
    x: 270,
    y: 480,
  },
  operations: [
    //详情参见多媒体处理章节。
    {
      type: "image_rotate",
      params: {
        angle: 0,
      },
    },
  ],
};
```

### audio

该种类的素材我们提供了更丰富的处理形式，具体请参考[多媒体处理](#多媒体处理)，示例如下：

```js
let audioItem = {
  id: "3259bbc5-c581-43eb-96a3-1fac66c46aa8",
  type: "audio",
  order: 0,
  items: [
    {
      id: "c6424c76-0320-4f92-9607-d2a53748fb14",
      start_time: 0,
      duration: 60080,
      type: "audio",
      asset_id: "281921553743719902@Public@CME",
      section: {
        from: 0,
        to: 60080,
      },
      operations: [], //详情参见多媒体处理章节。
    },
  ],
};
```

### title

作为内容填充的文本文字，内容填充的文字可以调整样式，示例数据如下:

```js
let titleItem = {
  id: "f83a90eb-a9d9-4634-81d4-c7dc130afaec",
  start_time: 80,
  duration: 3000,
  type: "advanced_title", // 固定文字类型不可变更。
  content: {
    template_id: "yj_templ_title_text", //固定模版ID,不可变更
    params: {
      text: "文字标题", //文字内容
      text_style: {
        //具体属性可参考下面的列表
        font_size: 60,
        font_color: "#ffffff",
        align: "center",
        height: 220,
        bold: 0,
        italic: 0,
      },
    },
  },
  position: {
    x: 270,
    y: 480,
  },
  width: 240,
  height: 69,
  transition: [
    //动画效果
    {
      start_time: 0, //动画效果起始时间
      duration: 500, //动画效果持续时间
      type: "in", //动画类型入场
      name: "fade",
    },
    {
      start_time: 2500,
      duration: 500,
      type: "out", //动画类型出场
      name: "move", //
    },
  ],
};
```

> 文字`text_style`可支持文字的[通用属性设置](#文字通用属性)。

> 自由文字动画效果，**_暂时只支持一个入场一个出场_**。

| 名称   | 描述   | 出入场限制 |
| ------ | ------ | ---------- |
| fade   | 淡入   | in,out     |
| move   | 左移入 | in,out     |
| scale  | 放大   | in,out     |
| bounce | 弹跳   | in         |

### subtitle

字幕类型基本示例如下，字幕类型素材的文字样式轨道通用，所以文字样式是挂载在轨道数据结构：

```js
let subTitleItem = {
  id: "3d343d8d-f950-40ea-aa50-e4e0c16cf2f2",
  start_time: 480,
  duration: 3000,
  type: "subtitle",
  style_id: "381921553743708206@Public@CME",
  text: "字幕文字1",
  asset_id: "381921553743708206@Public@CME",
};

/*****
 *  字幕样式对象
 * **/
let styleItem = {
  id: "381921553743708206@Public@CME",
  content: {
    template_id: "yj_templ_subtitle_common",
    params: {
      font_size: 60,
      font_color: "#ffffff",
      align: "center",
      height: 110,
      bold: 0,
      italic: 0,
      background_color: "#000000",
      background_alpha: 100,
      font: "SimHei",
      margin_bottom: 125,
      font_align: "right",
      font_align_margin: 30,
      bottom_color: "#3A1616",
      bottom_alpha: 100,
      border_color: "#FFFFFF",
      border_width: 2,
    },
  },
};
```

> 字幕文字的`params`支持[文字通用设置](#文字通用属性)。

### frame

> 特效元素,只支持固定模版，和固定操作，**_注: 特效必须覆盖其它素材,所以轨道层级处于顶层位置 _**。

更多内容请参考[image-glshader](#image-glshader)

示例:

```js
let item = {
  id: "7ae45f5d-f351-4351-b501-64f36ab74f2d",
  width: 960,
  height: 540,
  start_time: 0,
  duration: 3000,
  type: "frame",
  operations: [
    {
      type: "image_glshader",
      params: {
        name: "LightCircle", //可替换模版
      },
    },
  ],
  shaderName: "LightCircle", //预览模版
  controlVisible: true,
};
```

## 通用数据类型

### 文字通用属性

> 适用于`title`的`text_style`属性，以及`subtitle`的`params`属性。

| 属性值            | 类型   | 说明                                                                            |
| :---------------- | :----- | :------------------------------------------------------------------------------ |
| height            | number | 高度。 `必要`                                                                   |
| font_size         | number | 字体大小。`必要`                                                                |
| font_color        | string | 字体颜色，16 进制 RGB，如'#ffffff'。 `必要`                                     |
| font              | string | 字体名。                                                                        |
| font_alpha        | number | 背景透明度，范围[0, 100]。                                                      |
| font_align        | string | 水平对齐方式：center（默认）、left、right。                                     |
| font_uline        | number | 下划线宽度。                                                                    |
| font_align_margin | number | 大于等于 0，font_align=left 表示左边距，font_align=right 表示右边距，其他无效。 |
| bold              | number | 字体加粗，默认 0(不加粗)、1(加粗)。                                             |
| italic            | number | 字体倾斜，默认 0(正常)、1(斜体)。                                               |
| border_width      | number | 边框宽度。                                                                      |
| border_color      | string | 边框颜色，border_width 不为 0 时有效。                                          |
| border_alpha      | number | 边框透明度，border_width 不为 0 时有效。                                        |
| shadow_color      | string | 文字阴影。                                                                      |
| shadow_alpha      | number | 背景透明度，范围[0, 100]，shadow_color 存在时有效。                             |
| bottom_color      | string | 文字底色。                                                                      |
| bottom_alpha      | number | 文字底色透明度，范围[0, 100]，bottom_color 存在时有效。                         |
| background_color  | string | 全屏背景颜色，16 进制 RGB，如'#000000'。                                        |
| background_alpha  | number | 全屏背景透明度，范围[0, 100]，background_color 存在时有效。                     |
| margin_bottom     | number | 字幕的底边距，默认为 0。                                                        |

### 多媒体处理

> 该属性允许调整素材的一些基础信息，通过`operations`字段进行设置，完整能力如下列表，`Y`表示支持此操作，`N`表示不支持。

| operation                                   | video | image | audio | transition | frame | 备注                   |
| ------------------------------------------- | ----- | ----- | ----- | ---------- | ----- | ---------------------- |
| image_mirror                                | Y     | Y     | N     | N          | N     | 图像镜像               |
| image_rotate                                | Y     | Y     | N     | N          | N     | 图像旋转               |
| [image_filter_normal](#image-filter-normal) | Y     | Y     | N     | N          | N     | 普通图像滤镜           |
| [image_filter_lut](#image-filter-lut)       | Y     | Y     | N     | N          | N     | Lut 滤镜模版           |
| image_transparent                           | Y     | Y     | N     | N          | N     | 图像透明度             |
| [image_crop](#crop)                         | Y     | Y     | N     | N          | N     | 图像剪切`不可单独预览` |
| image_space                                 | Y     | Y     | N     | N          | N     | 图像缩放`不可单独预览` |
| [image_mosaic](#image-mosaic)               | N     | N     | N     | N          | Y     | 马赛克                 |
| [image_glshader](#image-glshader)           | N     | N     | N     | N          | Y     | 特效                   |

基础示例:

```js
/* 图像(图片、视频图像) 相关的操作 */
let imageMirrorOp = {
  type: "image_mirror", // 【必选】【string】 operation 类型，
  params: {
    left_right: 1, // 【必选】【int】 取值：1-左右镜像
    up_down: 1, // 【必选】【int】 取值：1-上下镜像
  },
};
//  图像旋转
let imageRotateOp = {
  type: "image_rotate", // 【必选】【string】 operation 类型，
  params: {
    angle: 90, // 【必选】【int】 旋转角度
  },
};
// 图像简单滤镜
let imageFilterNormalOp = {
  type: "image_filter_normal",
  params: {
    contrast: 100, // 【必选】【int】 对比度，取值范围 [-100, 100]，0 表示不处理
    brightness: 50, // 【必选】【int】 亮度，取值范围 [-100, 100]，0 表示不处理
    saturation: -20, // 【必选】【int】 饱和度，取值范围 [-100, 100]，0 表示不处理
  },
};

// 图像透明
let imageTransparentOp = {
  type: "image_transparent",
  params: {
    alpha: 0, // 【必选】【int】 透明度，取值范围[0,100]，0表示透明
  },
};
// 图像裁剪
let imageCropOp = {
  type: "image_crop",
  params: {
    x: 0, // 【必选】【int】 裁剪起始点(相对于item的)
    y: 0, // 【必选】【int】 裁剪起始点(相对于item的)
    width: 0, // 【必选】【int】 裁剪宽度
    height: 0, // 【必选】【int】 裁剪高度
  },
};
// 图像马赛克
let imageMosaicOp = {
  type: "image_mosaic",
  params: {
    name: "vague", // 【必选】【string】 马赛克类型，目前只支持模糊(vague)、方块（mosaic）
    x: 0, // 【必选】【int】 马赛克起始点(相对于item的)
    y: 0, // 【必选】【int】 马赛克起始点(相对于item的)
    width: 0, // 【必选】【int】 马赛克宽度
    height: 0, // 【必选】【int】 马赛克高度
    degree: 100, // 【可选】【int】 马赛克程度，范围[0,100]
  },
};

// 调整大小和位置

let imageSpaceOp = {
  type: "image_space",
  params: {
    x: 0, // 【可选】【int】 存在表示新的中心点x
    y: 0, // 【可选】【int】 存在表示新的中心点y
    width: 0, // 【可选】【int】 存在且大于0，表示新的宽度
    height: 0, // 【可选】【int】 存在且大于0，表示新的高度
  },
};
// 图像opengl shader效果

let imageGlshaderOp = {
  type: "image_glshader"
  params: {
    name: "xxx", // 【必选】【string】 效果名称
  },
};

```

#### crop

裁剪功能预览的流程如下:

1. 将待裁剪视频按照满屏的方式放置到舞台内。
2. 在满屏基础上设置裁剪区域。
3. 还原视频位置信息。

裁剪数据设置流程复杂，如需设置也可以使用我们`sdk`提供的`crop`方法。

示例如下:

```js
let item = {
  id: "0bfdd748-b548-42f4-9711-09ae5c534061",
  start_time: 0,
  duration: 63560,
  type: "video",
  section: {
    from: 0,
    to: 63560,
  },
  asset_id: "5f6464c6ccbc8d0001fc308b",
  width: 960, //视频原始宽高
  height: 254, //视频原始宽高
  position: {
    //元素原本位置信息
    x: 480,
    y: 270,
  },
  operations: [
    {
      /**
       * 对视频重设，让其满屏
       **/
      type: "image_space",
      params: {
        x: 480,
        y: 270,
        width: 960,
        height: 540,
      },
      from: "crop_start", //表示裁剪开始
    },
    {
      /**
       * 设置裁剪区域，裁剪区域是一个矩形，
       * x,y为裁剪位置
       * width,height表示裁剪区域
       **/
      type: "image_crop",
      params: {
        x: 376,
        y: 28,
        width: 223,
        height: 59,
      },
    },
    {
      /**
       * 还原元素位置和大小，这个示例里裁剪开始前与裁剪结束后位置是一样的。
       **/
      type: "image_space",
      params: {
        x: 480,
        y: 270,
        width: 960,
        height: 254,
      },
      from: "crop_end", //裁剪结束
    },
  ],
  sizeControl: 0,
};
```

### image-mosaic

> 特效类轨道必须是覆盖在普通视频轨道之上。

示例:

```js
/***
 * 必须使用特效类轨道。
 ***/
let trackItem = {
  id: "adfe3eab-db8f-4b4c-96e8-730bf3a9226d",
  type: "frame",
  order: 0,
  items: [],
};

let item = {
  id: "0c5e990d-bdf9-47f6-b1a5-ac7639060e4f",
  asset_id: "fe-731195088946733254",
  start_time: 0,
  duration: 3000,
  type: "frame",
  operations: [
    {
      type: "image_mosaic", //类型固定为 image_mosaic
      params: {
        name: "mosaic", //名字固定为 image_mosaic
        degree: 20,
        x: 311,
        y: 40,
        width: 320,
        height: 180,
      },
    },
  ],
};

/**
 * 放入轨道
 * */
track.items.push(trackItem);

/**
 * 最终数据结构
 * */
let data = [trackItem];
```

### image-filter-lut

示例:

```js
let item = {
  id: "7edc76a8-1a28-4546-b0ca-fd7403660ca1",
  start_time: 0,
  duration: 63560,
  type: "video",
  section: {
    from: 0,
    to: 63560,
  },
  asset_id: "5f6464c6ccbc8d0001fc308b",
  width: 960,
  height: 540,
  position: {
    x: 480,
    y: 270,
  },
  operations: [
    {
      type: "image_rotate",
      params: {
        angle: 0,
      },
    },
    {
      type: "image_filter_lut",
      params: {
        name: "yj_templ_lut_24", //修改此模版ID即可变更效果
        image_url:
          "https://1810000000.vod2.myqcloud.com/b64e98acvodcq1810000000/thumbnail/filter/yj_templ_lut_24.png",
      },
    },
  ],
};
```

**_注:请严格按照模版 ID 使用_**

| 模版 ID         | 描述   |
| --------------- | ------ |
| yj_templ_lut_21 | 初秋   |
| yj_templ_lut_12 | 冷光   |
| yj_templ_lut_17 | 温暖   |
| yj_templ_lut_18 | 老相片 |
| yj_templ_lut_15 | 傍晚   |
| yj_templ_lut_25 | 金秋   |
| yj_templ_lut_24 | 梦幻   |
| yj_templ_lut_23 | 早春   |
| yj_templ_lut_20 | 藕荷   |
| yj_templ_lut_26 | 古铜   |
| yj_templ_lut_2  | 薄暮   |
| yj_templ_lut_5  | 晨光   |
| yj_templ_lut_4  | 自然   |
| yj_templ_lut_1  | 清晨   |
| yj_templ_lut_3  | 宁静   |

具体可以参考[这里](https://yunjian.qq.com)，如下图:

<img src='../../img/filter.png'>

### image-filter-normal

```js
let item = {
  id: "7edc76a8-1a28-4546-b0ca-fd7403660ca1",
  start_time: 0,
  duration: 63560,
  type: "video",
  section: {
    from: 0,
    to: 63560,
  },
  asset_id: "5f6464c6ccbc8d0001fc308b",
  width: 960,
  height: 540,
  position: {
    x: 480,
    y: 270,
  },
  operations: [
    {
      type: "image_rotate",
      params: {
        angle: 0,
      },
    },
    {
      type: "image_filter_normal", //修改params值即可调整对应效果
      params: {
        contrast: 100, //对比度
        brightness: 0, //明亮度
        saturation: 0, //饱和度
      },
    },
  ],
};
```

### image-glshader

基础示例:

```js

/**
 * 特效视频只能放到特效轨道上.注意特效必须覆盖其它素材。
 * **/
let track = {
  id: "61eed235-a61a-4ae0-baaf-49dda661c962",
  type: "frame",
  order: 1,
  items: [],
  subType: "shader",
};

/****
 * 特效元素
 * **/
let trackItem = {
  id: "03816c76-4ba0-48bd-b7c7-289f45002652",
  width: 960, //宽高取值与舞台保持一致
  height: 540, //宽高取值与舞台保持一致
  asset_id: "5f0aba91cb093b30566c5da9@Public@CME",
  start_time: 0,
  duration: 3000,
  type: "frame",
  operations: [
    /**
     * 如果是组合特效，则有两个操作对象
     * */
    {
      type: "image_glshader",
      params: {
        name: "LightCircle", //导出替换值
      },
    // 注: 组合特效需要注意顺序，顺序改变导出效果会有变化
    // {
    //   type: "image_glshader",
    //   params: {
    //     name: "ScBlurThreeY", //导出替换值
    //   },
    // },
    // {
    //   type: "image_glshader",
    //   params: {
    //     name: "ScBlurThreeX", //导出替换值
    //   },
    // },
  ],
  /***
   * 由于部分滤镜特效是由多种操作组合成，例如注释内的高斯模糊效果，
   * 所以预览值和导出值有可能不一样。预览值表示可以在预览组件上看的效果。
   * **/
  shaderName: "LightCircle", //预览值
  // shaderName: "ScBlurThree" // 模糊
};

track.items.push(trackItem)

/**
 * 最终数据结构
 * */
let data = [trackItem]

```

> 所有的特效描述:

| 预览名称      | 描述     | 组合                       |
| ------------- | -------- | -------------------------- |
| LightCircle   | 光斑     | LightCircle                |
| Heart         | 爱心     | Heart                      |
| Shining       | 光芒四射 | Shining                    |
| Blink         | 亮晶晶   | Blink                      |
| Bubble        | 泡泡     | Bubble                     |
| Snow          | 飘雪     | Snow                       |
| Rain          | 雨滴     | Rain                       |
| Duotone       | 双色调   | Duotone                    |
| FlowingLight  | 流光     | FlowingLight               |
| ChasingLight  | 逐光     | ChasingLight               |
| Rainbow       | 彩虹     | Rainbow                    |
| Multicoloured | 炫彩     | Multicoloured              |
| Shake         | 抖动     | Shake                      |
| Swing         | 摇晃     | Swing                      |
| SoulOut       | 灵魂     | SoulOut                    |
| Hallucination | 幻觉     | Hallucination              |
| ShineWhite    | 闪白     | ShineWhite                 |
| Glitch        | 故障     | Glitch                     |
| OldVideo      | 老电影   | OldVideo                   |
| Mirror        | 镜像     | Mirror                     |
| ScBlurThree   | 模糊分屏 | ScBlurThreeY、ScBlurThreeX |
| ScGrayThree   | 黑白三屏 | ScGrayThree                |
| ScTwo         | 两屏     | ScTwo                      |
| ScThree       | 三屏     | ScThree                    |
| ScFour        | 四屏     | ScFour                     |
| ScSix         | 六屏     | ScSix                      |
| ScNine        | 九屏     | ScNine                     |

具体可以参考[这里](https://yunjian.qq.com)，如下图:
<img src='../../img/texiao.png'>
