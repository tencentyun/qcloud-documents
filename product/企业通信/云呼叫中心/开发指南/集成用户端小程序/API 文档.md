## 通用 API
#### login — 登录
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='6'>options</td>
      <td>sdkAppId</td>
      <td>string</td>
      <td>是</td>
      <td>腾讯云呼叫中心应用 SdkAppId</td>
   </tr>
   <tr>
      <td>jsCode</td>
      <td>string</td>
      <td>是</td>
      <td>通过 wx.login 获取</td>
   </tr>
   <tr>
      <td>dataEnv</td>
      <td>string</td>
      <td>否</td>
      <td>wx.getUserProfile 的 encryptedData</td>
   </tr>
   <tr>
      <td>dataIv</td>
      <td>string</td>
      <td>否</td>
      <td>wx.getUserProfile 的 iv</td>
   </tr>
   <tr>
      <td>mobileEnv</td>
      <td>string</td>
      <td>否</td>
      <td>通过 button open-type="getPhoneNumber" 方式获取</td>
   </tr>
   <tr>
      <td>mobileIv</td>
      <td>string</td>
      <td>否</td>
      <td>通过 button open-type="getPhoneNumber" 方式获取</td>
   </tr>
</table>

#### checkLogin — 检查是否已登录
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>sdkAppId</td>
      <td>string</td>
      <td>是</td>
      <td>腾讯云呼叫中心应用 SdkAppId</td>
   </tr>
</table>

```javascript
import { login, checkLogin } from 'tccc-wx-sdk/login'
const sdkAppId = '1400000000'
// 登录示例代码
checkLogin({ sdkAppId })
  .then((result) => {   
    if (result) {     
      // 检查登录成功   
    } else {
      throw new Error('登录已过期')
    }
  }).catch(() => {
    wx.login({
      success: ({ code }) => {
      // 登录tccc      
        login({         
          jsCode: code,       
          sdkAppId
        }).then(() => {     
          // 登录成功   
        }).catch(e => {  
           wx.showToast({ 
             icon: 'error',
             title: e.message
           })      
         })
     }
    })
})
```

## 音频呼叫 API
#### startCall — 发起音频通话
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>channelId</td>
      <td>string</td>
      <td>是</td>
      <td>IVR 入口 ID</td>
   </tr>
</table>
```javascript
try {
    const channelId = 'xxx'
    const { sessionId } = await this.selectComponent('#tcccSdk').startCall({ channelId })
} catch (e) {
    wx.showToast({ 
      icon: 'error',
      title: e.message
    })
}
```

#### endCall — 挂断通话
```javascript
this.selectComponent('#tcccSdk').endCall();
```

#### sendDigits — 发送分机号
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>digits</td>
      <td>string</td>
      <td>是</td>
      <td>分机号</td>
   </tr>
</table>
```javascript
this.selectComponent('#tcccSdk').sendDigits(options)
```


## 视频呼叫 API
#### startSession — 发起视频通话
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>options</td>
      <td>channelId</td>
      <td>string</td>
      <td>是</td>
      <td>IVR 入口 ID</td>
   </tr>
</table>
```javascript
try {
    const channelId = 'xxx'
    const { sessionId } = await this.selectComponent('#tcccSdk').startSession({ channelId })
} catch (e) {
    wx.showToast({ 
      icon: 'error',
      title: e.message
    })
}
```

#### endSession — 挂断视频通话
```javascript
this.selectComponent('#tcccSdk').endSession();
```

#### switchCamera — 切换摄像头
```javascript
this.selectComponent('#tcccSdk').switchCamera();
```


#### disableCamera — 关闭摄像头
```javascript
this.selectComponent('#tcccSdk').disableCamera();
```

#### enableCamera — 开启摄像头
```javascript
this.selectComponent('#tcccSdk').enableCamera();
```

## 会话通用 API
#### setSoundMode — 设置声音输出方式
<table>
   <tr>
      <th width="0px" style="text-align:center" colspan="2">参数</td>
      <th width="0px" style="text-align:center">类型</td>
      <th width="0px"  style="text-align:center">必填</td>
      <th width="0px"  style="text-align:center">备注</td>
   </tr>
   <tr>
      <td rowspan='2'>soundMode</td>
      <td>'ear' | 'speaker'</td>
      <td>string</td>
      <td>是</td>
      <td>speaker：扬声器，ear：听筒</td>
   </tr>
</table>

#### muteAudio — 静音
```javascript
this.selectComponent('#tcccSdk').muteAudio();
```

#### unmnuteAudio — 取消静音
```javascript
this.selectComponent('#tcccSdk').unmnuteAudio();
```

## 通用事件
#### sessionStart — 会话开始
```html
<tccc-wx-sdk bind:sessionStart="handleStart"/>
```
```javascript
handleStart() {
  wx.showToast({
    icon: 'success',
    title: '通话开始'
  })
}
```

#### accepted — 对方接听
```html
<tccc-wx-sdk bind:accept="handleAccepted"/>
```
```javascript
handleAccepted() {
  wx.showToast({
    icon: 'nonce', // 自选合适的图标
    title: '对方已接听'
  })
}
```


#### sessionEnded — 会话结束
```html
<tccc-wx-sdk bind:sessionEnded="handleSessionEnded"/>
```
```javascript
handleSessionEnded({ closeBy }) {
  if (closeBy === 'admin') {
    wx.showToast({
      icon: 'none', // 自选合适的图标
      title: '系统原因挂断'
    })
  } else if(cloeBy === 'seat') {
    wx.showToast({
      icon: 'none', // 自选合适的图标
      title: '通话结束，对方已挂断'
    })   
  } else {
    // 挂断成功   
  }
}
```

#### error — 通话错误
```html
<tccc-wx-sdk bind:error="handleError"/>
```
```javascript
handleError(error) {
  wx.showToast({
    icon: 'error',
    title: error.message || '发生错误，请重试'
  })
}
```