# wx.onThemeChange(function listener)

## 功能描述

监听系统主题改变事件。

<!-- 该事件与 [`App.onThemeChange`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onThemeChange-Object-object) 的回调时机一致。 -->

## 参数

### function listener

系统主题改变事件的监听函数

#### 参数

##### Object res

| 属性  | 合法值及说明                      | 类型   | 说明                                  |
| :---- | --------------------------------- | :----- | :------------------------------------ |
| theme | dark：深色主题<br>light：浅色主题 | string | 系统当前的主题，取值为`light`或`dark` |

## 注意

- 只有在全局配置"darkmode": true时才会触发此事件。