## 拍摄组件
在需要展示视频编辑能力的页面 JSON 内引入插件，名称可自定义，如下以 my-clip 为例：
```
{
  "usingComponents": {
    "my-clip": "plugin://myPlugin/clip"
  }
}
```
在页面的 wxml 内写入插件标签：
```
<view>
    <my-clip></my-clip>
</view>
```
js 里获取插件实例：
```
const plugin = requirePlugin("myPlugin")
console.log(plugin)
```
clip 为插件的入口，因此插件内部除导出功能外所用到的参数均从 clip 传入。
1.4.2 版本以后加入了字体功能，需要额外进行字体配置：
字体的下载需要借助小程序的 loadFontFace 方法，需要在`index.js`中，将 loadFontFace 方法通过 exports 输出。
```javascript
module.exports = {
  downloadFile: wx.downloadFile,
  loadFontFace: wx.loadFontFace
}
```
在`app.json`中将 loadFontFace 方法导出到插件。
```json
"myPlugin": {
  "provider": "wx76f1d77827f78beb",
  "version": "1.4.3",
  "export": "index.js"
}
```

> !1.4.2 版本以后加入了字体功能，需要 export 小程序的 loadFontFace 方法, 并将`https://cdn.cdn-go.cn`配置到小程序后台的 `reuqest` 和 `downloadFile` 白名单中。
##  导出组件
export 是一个集成了视频导出功能的可定义外观组件。
>!受微信 Android 客户端 7.0.19 版本策略影响，导出表现偏慢，预计在11月底的版本修复。
### 组件引入
```
{
    "usingComponents": {
      "export": "plugin://myPlugin/export"
    },
 }
```
编写 wxml：
```
<export //内部元素的tap事件触发导出操作
  showloading="{{false}}" // 导出时会自动显示loading，如不需要传false隐藏
  watermark="https://cdn.cdn-go.cn/mp-video-edit-static/latest/images/watermark.png" //水印地址
  bindexportsuccess="handleExportSuccess" //返回导出的文件临时路径，供调用者使用
  bindprogress="handleProgress" // 导出进度更新，返回值0-100
  bindthumbready="handleThumbReady" //导出页面预览图绘制完成回调
  >
    <button class="customContent">导出</button> // 自定义UI，由slot实现
</export>
```
导出需要 tap 事件触发，内部需要包含可点击的组件，并且不能 catch 事件。

### 处理返回的数据
```
handleExportSuccess(e) {
  console.log(e.detail)
}
```
`e.detail`包含导出视频的信息:
```
{
  code: 0, //成功
  tempFilePath: 'wxfile://xxx.mp4',
  coverInfo: {
    path: xxx,
    width: 544,
    height: 960
  }, // 封面信息
  video: {
    width: '544', //视频分辨率
    height: '960',
    fps: 30, //帧率
  }
  duration: 3000 //单位 ms
}
```
### 处理预览图数据
```
handleThumbReady(e) {
  console.log(e.detail)
}
```
`e.detail`包含预览图的信息:
```
{
    path: 'xxx' // 预览图的地址或生成的base64数据
    width: 100 // 预览图的宽度
    height: 100 // 预览图的高度
}
```

##  插件参数

| 参数名称        | 类型     | 是否必填 | 说明                       |
| --------------- | -------- | -------- | -------------------------- |
| appid           | string   | 否       | 请到 [腾讯云账号信息](https://console.cloud.tencent.com/developer) 中查看   |
| settings        | object   | 否       | 用于自定义配置，包括 UI 样式 |
| bindInitedEvent | function | 否       | 插件初始化事件回调         |

### settings 参数说明
settings 参数用来修改插件内置的一些基本参数，通过修改 settings 可以达到定制部分编辑能力或定制 UI 界面的功能 下面是关于 settings 的具体说明：
- settings 整体为一个 Object，如果不设置改属性则取插件内置默认值。
- settings 对象主要有两部分的配置：common 和页面配置。
- 插件包含若干个组件，会暴露组件的样式配置项。每个组件包含了自己的 state，默认 state 为 `default`，部分组件包含特殊 state，例如 camera 有 `recording` 这个状态。
- 页面配置分为 `camera`/`previewer`/`editor` 等几个主界面，分别代表拍摄页，预览页，编辑主页面，不填写则默认取 common 中的配置。
- 每个组件暴露的最内层属性 value 为可修改部分，例如设置`settings.previewer.nextButton.default.fontColor = '#fff'`表示把该按钮字体设置为白色。

### settings 参数使用
在初始化的时候，传入 settings 参数：
```
<view>

<my-clip settings="{{myCustomSettings}}"></my-clip>

</view>
```
settings 对象默认值示例如下：
```javascript
export default {
  // 通用配置
  common: {
    videoMaxDuration: 30, // 小程序限制最多拍摄30秒
    chooseMaxDuration: 1000, // 选择视频的默认时长限制
    clipMaxDuration: 60, // 裁切时长的默认限制
    imgDisplayDuration: 3, // 单张图片默认展示时间（秒）
    exportPagePath: "/pages/main/export/index", // 默认跳进插件自己提供的页面
    editMode: ['album', 'manual']// 启用的编辑模式
    style: {
      // 主题色
      primaryColor: "#ff584c",
      // 文字色
      textColor: "#fff",
      // 禁用色
      disableColor: "#ddd",
      // 整体背景色
      backgroundColor: "#000",
      // 通用按钮配置
      button: {
        state: {
          default: {
            backgroundColor: "#ff584c",
            fontColor: "#fff"
          },
          disable: {
            backgroundColor: "#ddd",
            fontColor: "#fff"
          }
        }
      },
      // 通用二级按钮配置
      secondaryButton: {
        state: {
          default: {
            backgroundColor: "#ffffff",
            fontColor: "#ff584c"
          },
          disable: {
            backgroundColor: "#ddd",
            fontColor: "#fff"
          }
        }
      }
    }
  },
    // 以下配置均可选，单独配置覆盖上面的通用色配置
  // 拍摄界面
  camera: {
    // 录制按钮
    recordButton: {
      state: {
        default: {
          backgroundColor: "#ff584c",
          borderColor: "rgba(255,88,76,0.5)"
        },
        recording: {
          backgroundColor: "#fff"
        }
      }
    },
    // 下一步按钮
    nextButton: {
        state: {
        default: {
          backgroundColor: "#ff584c",
          borderColor: "rgba(255,88,76,0.5)"
        },
        recording: {
          backgroundColor: "#fff"
        }
      }
    },
    // 重新选择按钮
    rechooseButton: {
      // 同上
    }
  },

  previewer: {
    //下一步按钮，可以不配，配了覆盖style.style.button
    nextButton: {
      state: {
        default: {
          backgroundColor: "#ff584c",
          fontColor: "#fff"
        }
      }
    },
    // 覆盖common.style.primaryColor
    clipper: {
      borderColor: "#ff584c"
    }
  },
  // 编辑页面
  editor: {
    //下一步按钮
    nextButton: {
      state: {
        default: {
          backgroundColor: "#ff584c",
          fontColor: "#fff"
        }
      }
    },

    //操作面板
    operatePanel: {
      // 面板背景色,覆盖common.style.backgroundColor
      backgroundColor: "rgba(0,0,0,0.8)",
      // 特效面板
      effect: {
        // 自定义icon，不传使用默认icon
        icon: "https://xx.xx.xx",
        // 游标颜色，此处的movableColor和下面的highlightColor不填则取common.style.primaryColor
        movableColor: "#ff584c"
      },
      // 滤镜面板
      filter: {
        icon: "https://xx.xx.xx",
        highlightColor: "#ff584c"
      },
      // 音乐面板
      music: {
        icon: "https://xx.xx.xx",
        highlightColor: "#ff584c",
        useButton: {
          state: {
            default: {
              backgroundColor: "#ff584c"
            }
          }
        }
      },
      // 文字面板
      text: {
        icon: "https://xx.xx.xx",

      }
    }
  }
};

```


