PAG 插件同时支持**矢量预合成**直接导出和 **BMP 预合成**导出两种方式。

- **矢量预合成**：导出的方式文件极小，并性能会优于 BMP 预合成，但仅支持部分 AE 特性。矢量预合成导出通常用于 UI 动画等对于文件大小和性能敏感，以及需要贴纸内容可编辑的场合。
- **BMP 预合成**：可以支持所有的 AE 特性，但是文件体积较大，也无法运行时编辑内容。BMP 预合成通常用于无法矢量导出的场景，例如用了粒子效果或者第三方插件等。

为了保持动效的可编辑性，支持矢量和 BMP 预合成混合导出，BMP 预合成可以被矢量预合成嵌套，作为它的一个图层来实现 AE 特效和可编辑的结合。


## BMP 预合成导出

BMP 预合成导出模式可以支持所有的 AE 特效，设计师只需要关注视觉效果本身即可，但是会有一定的性能开销，并且无法做到运行时对动效内容修改编辑。BMP 预合成目前支持**视频序列帧**和**位图序列帧**两种导出的存储格式，位图存储格式做了简单的帧间压缩，每帧只记录改变的区域。平均可以比传统的 PNG 序列帧文件小 50% 。而视频存储格式帧基于 H264 帧间压缩并补充了透明通道，相同动效文件大小非常有优势。相比位图存储格式只有 10 % ~ 25% 左右的文件大小。下表是一些常用的动效效果在两种导出模式下的文件大小对比：

![](https://qcloudimg.tencent-cloud.cn/raw/276162740e85c46bb3a4f53ba8db27ce.png)

>?
> - 目前位图存储格式主要使用在部分不支持视频存储格式的场景，比如 Web 端。
> 视频存储格式是 BMP 预合成的默认导出格式，除了文件大小的优势，渲染时还可以开启硬件加速解码，能显著降低设备发热量。


### 矢量预合成导出
矢量预合成导出无法支持所有的 AE 特性，但我们推荐尽可能使用矢量预合成方式导出，可以获得更好的性能和更小的动效文件。目前已支持的矢量直接导出的 AE 特性如下：**（所有关键帧动效属性都支持）**

#### 图层类型 (Layer Types)
```bash
├─ 虚拟对象 (Null Object)
├─ 实色图层 (Solid Layer)
├─ 文字图层 (Text Layer)
├─ 形状图层 (Shape Layer)
├─ 预合成图层 (PreCompose Layer)
└─ 图片图层 (Image Layer)
```

#### 变换 (Transforms)

```bash
├─ 定位点 (Anchor Point)
├─ 位置 (Position)
├─ 位置分离XY轴 (Position Separated X/Y )
├─ 缩放 (Scale)
├─ 旋转 (Rotation)
└─ 透明度 (Opactiy) [注：不支持整体透明度(可能产生叠影)，只支持分散到各个图层的透明度]
```

#### 混合模式 (Blend Modes)

```bash
├─ 正常 (Normal)
├─ 变暗 (Darken)
├─ 相乘 (Multiply)
├─ 颜色加深 (ColorBurn)
├─ 相加（Add）
├─ 变亮 (Lighten)
├─ 屏幕 (Screen)
├─ 颜色减淡 (ColorDodge)
├─ 叠加 (Overlay)
├─ 柔光 (SoftLight)
├─ 强光 (HardLight)
├─ 差值 (Difference)
├─ 排除 (Exclusion)
├─  色相 (Hue)
├─ 饱和度 (Saturation)
├─ 颜色 (Color)
└─ 发光度 (Luminosity)
```

#### 轨道遮罩 (Track Mattes)

```bash
├─ 无 (None)
├─ Alpha 遮罩 (Alpha Matte)
├─ Alpha 反转遮罩 (Alpha Inverted Matte)
├─ Luma 遮罩 (Luma Matte)
├─ Luma 反转遮罩 (Luma Inverted Matte)
└─ [注：均可支持半透明擦除]
```

#### 蒙版 (Masks)

```bash
├─ 蒙版路径 (Mask Path)
├─ 蒙版扩展 (Mask Expansion)
├─ 蒙版模式 (Mask Modes)
│  ├─ 无 (None)
│  ├─ 相加 (Add)
│  ├─ 相减 (Subtract)
│  ├─ 交集 (Intersect)
│  └─ 差值 (Difference)
├─ 蒙版不透明度 (Mask Opacity)
└─ 蒙版羽化 (Mask Feather)
```

#### 图层样式 (Layer Styles)

```bash
├─ 投影 (Drop Shadow)
│  ├─ 颜色 (Color)
│  ├─ 不透明度 (Opacity)
│  ├─ 角度 (Angle)
│  ├─ 距离 (Distance)
│  ├─ 扩展（Spread）
│  └─ 大小 (Size)
└─ 渐变叠加 (Gradient Overlay)
```

#### 特效 (Effect)

```bash
├─ 运动模糊 (Motion Blur)
├─ 高斯模糊（Gaussian Blur）
├─ 凹凸效果 (Bulge)
├─ 辉光效果 (Glow)
├─ 色阶控制 (Levels Individual Controls)
├─ 边角定位 (Corner Pin)
├─ 动态拼贴 (Motion Tile)
├─ 置换效果（Displacement Map）[注：暂要求将置换图层修改为预合成图层并改合成名为"_bmp"后缀]
├─ 径向模糊 (Radial Blur)
└─ 马赛克 (Mosaic)
```

>? 效果预览请点击查看 [当前支持的 AE 内置特效](https://pag.art/docs/ae-effect.html)。

#### 其他图层属性 (Others Layer Properties)

```bash
└─ 图层父级 (Layer Parenting)
```

#### 形状图层 (Shapes)

```bash
├─ 组 (Group)
├─ 矩形 (Rectangle)
├─ 椭圆 (Ellipse)
├─ 多边星形 (Polystar)
├─ 路径 (Path)
├─ 填充 (Fill)
├─ 描边 (Stroke)
├─ 合并路径 (Merge Paths)
├─ 中继器 (Repeater)
├─ 修剪路径 (Trim Paths)
├─ 圆角 (Round Corners)
├─ 渐变填充 (Gradient Fill)
└─ 渐变描边 (Gradient Stroke)
```

#### 文本图层 (Texts)

```bask
├─ 源文本 (SourceText)
│  ├─ 基线偏移 (Baseline Shift)
│  ├─ 点文本 (Point Text)
│  ├─ 带框文本 (Box Text)
│  ├─ 仿粗体 (Faux Bold)
│  ├─ 仿斜体 (Faux Italic)
│  ├─ 文本颜色 (Fill Color)
│  ├─ 字体名称 (Font Family)
│  ├─ 字体样式 (Font Style)
│  ├─ 字号 (Font Size)
│  ├─ 描边颜色 (Stroke Color)
│  ├─ 描边宽度 (Stroke Width)
│  ├─ 交换图层和描边 (Stroke Over Fill)
│  ├─ 行距 (Leading)
│  ├─ 字间距 (Tracking)
│  ├─ 文本对齐 (Paragraph Justification)
│  ├─ 左对齐 (Left)
│  ├─ 居中对齐 (Center)
│  ├─ 右对齐 (Right)
│  ├─ 最后一行左对齐 (Full Justify Last Line Left)
│  ├─ 最后一行居中对齐 (Full Justify Last Line Center)
│  ├─ 最后一行右对齐 (Full Justify Last Line Right)
│  └─ 两端对齐 (Full Justify Last Line Full)
├─ 路径选项 (Path Options)  [注：不支持竖排文字图层]
│  ├─ 路径 (Path)
│  ├─ 反转路径 (Reverse Path)
│  ├─ 垂直于路径 (Perpendicular To Path)
│  ├─ 强制对齐 (Force Alignment)
│  ├─ 首字边距 (First Margin)
│  └─ 末字边距 (Last Margin)
└─ 动效制作工具（Animates）
├─ 属性
│  ├─ 字间距（Tracking）
│  │  ├─ 字符间距类型（Track Type）
│  │  └─ 字符间距大小（Tracking Amount）
│  ├─ 位置（Position）
│  ├─ 旋转（Rotation）
│  ├─ 缩放（Scale）
│  └─ 不透明度（Opacity）
├─ 范围选择器（Range Selector）
│  ├─ 起始（Start）
│  ├─ 结束（End）
│  ├─ 偏移（Offset）
│  ├─ 单位（Units）: (仅支持默认值"百分比")
│  ├─ 依据（Based On）:（仅支持默认值"字符"）
│  ├─ 模式（Mode）
│  ├─ 数量（Amount）
│  ├─ 形状（Shape）
│  ├─ 平滑度（Smoothness）: (仅支持默认值 100%)
│  ├─ 缓和高（Ease High）: (除三角形，其他仅支持默认值 0%)
│  ├─ 缓和低（Ease Low）: (除三角形，其他仅支持默认值 0%)
│  ├─ 随机排序（Randomize Order）
│  └─ 随机植入（Random Seed）
├─ 摆动选择器（Wiggly Selector）
│  ├─ 模式（Mode）
│  ├─ 最大量（Max Amount）
│  ├─ 最小量（Min Amount）
│  ├─ 依据（Based On）:（仅支持默认值"字符"）
│  ├─ 摇摆/秒（Wiggly Per Secend）
│  ├─ 关联（Correlation）
│  ├─ 时间相位（Temporal Phase）
│  ├─ 空间相位（Spatial Phase）
│  └─ 随机植入（Random Seed）
└─ (支持多个动效制作工具/属性/选择器的叠加)
```

### 计划中将要支持的特性

#### 变换 (Transforms)

```bash
└─3D 属性 (3D Properties)
```

#### 文本图层 (Texts)

```bash
├─ 更多选项 (More Options)
└─ 动效制作工具 (Animate)
```

#### 图层效果 (Layer Effects)
```bash
├─ 浅色调 (Tint)
├─ 填充 (Fill)
├─ 描边 (Stroke)
├─ 三色调 (Tritone)
└─ 径向擦除 (Radial Wipe)
```

## 总结
学习完本教程后，我们已初步了解 PAG 导出插件支持的 AE 功能。

