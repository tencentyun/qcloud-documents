## TEduBoard.EVENT.TEB_ERROR

白板错误事件 [TEB_ERROR](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ERROR)

>!
1. 白板错误事件一定要监听。
2. 白板错误事件属于白板致命错误，只能重新初始化白板才能解决，在重新初始化之前请先调用 destroy 方法进行销毁当前实例。

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| errorCode  |	number |	错误码 |
| errorMessage | string | 错误描述 |

```
teduBoard.on(TEduBoard.EVENT.TEB_ERROR, (errorCode, errorMessage) => {
   console.log('======================:  ', 'TEB_ERROR', ' errorCode:', errorCode, ' errorMessage:', errorMessage);
});
```

## TEduBoard.EVENT.TEB_WARNING

白板警告事件 [TEB_WARNING](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_WARNING)

>!
1. 白板警告事件一定要监听。
2. 警告事件不是致命事件，不影响白板运行，但需要您针对警告码找出原因并修复。


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| warnCode |	number |	警告码 |
| warnMessage |	string |	警告描述 |

```
teduBoard.on(TEduBoard.EVENT.TEB_WARNING, (warnCode, warnMessage) => {
   console.log('======================:  ', 'TEB_WARNING', ' warnCode:', warnCode, ' warnMessage:', warnMessage);
});
```

## TEduBoard.EVENT.TEB_HISTROYDATA_SYNCCOMPLETED

白板历史数据同步完成回调 [TEB_HISTROYDATA_SYNCCOMPLETED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_HISTROYDATA_SYNCCOMPLETED)

>!针对白板行为的操作，一定要在该事件回调完成后再进行操作，否则无效。如翻页，设置背景色等行为

```
teduBoard.on(TEduBoard.EVENT.TEB_HISTROYDATA_SYNCCOMPLETED, () => {
   console.log('======================:  ', 'TEB_HISTROYDATA_SYNCCOMPLETED');
});
```

## TEduBoard.EVENT.TEB_ADDBOARD

新增白板事件 [TEB_ADDBOARD](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDBOARD)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| boardIds | Array  | 新增的白板 ID 列表 |
| fileId | string	|文件 ID|

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDBOARD, (boardIds, fileId) => {
   console.log('======================:  ', 'TEB_ADDBOARD', ' boardIds:', boardIds, ' fileId:', fileId);
});
```

## TEduBoard.EVENT.TEB_ADDELEMENT

增加元素回调 [TEB_ADDELEMENT](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDELEMENT)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | object | 回调数据 |
| `data.id` | string | 元素的 ID |
| data.userData | string | 透传 userData 数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDELEMENT, (data) => {
   console.log('======================:  ', 'TEB_ADDELEMENT', data);
});
```

## TEduBoard.EVENT.TEB_ADDFILE

新增普通文件事件 [TEB_ADDFILE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDFILE)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| fileId |	string |	新增文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDFILE, (fileId) => {
   console.log('======================:  ', 'TEB_ADDFILE', ' fileId:', fileId);
});
```

## TEduBoard.EVENT.TEB_ADDH5PPTFILE

新增动画 PPT 文件事件 [TEB_ADDH5PPTFILE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDH5PPTFILE)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| fileId |string | 新增文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDH5PPTFILE, (fileId) => {
   console.log('======================:  ', 'TEB_ADDH5PPTFILE', ' fileId:', fileId);
});
```

## TEduBoard.EVENT.TEB_ADDIMAGEELEMENT

添加图片元素回调 [TEB_ADDIMAGEELEMENT](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDIMAGEELEMENT)

>!如果您添加的图片元素直接设置的是一个 HTTPS 的 url，则图片名称和 userData 为空

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| name | string | 图片名称 |
| url |string | 图片 url |
| userData | string	| 透传上传文件配置的 userData 数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDIMAGEELEMENT, (name, url, userData) => {
   console.log('======================:  ', 'TEB_ADDIMAGEELEMENT', name, url, userData);
});
```

## TEduBoard.EVENT.TEB_ADDIMAGESFILE

增加图片文件回调 [TEB_ADDIMAGESFILE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDIMAGESFILE)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| fileId | string | 新增文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDIMAGESFILE, (fileId) => {
   console.log('======================:  ', 'TEB_ADDIMAGESFILE', fileId);
});
```

## TEduBoard.EVENT.TEB_ADDTRANSCODEFILE

增加转码文件回调 [TEB_ADDTRANSCODEFILE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_ADDTRANSCODEFILE)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| fileId | string | 新增文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_ADDTRANSCODEFILE, (fileId) => {
   console.log('======================:  ', 'TEB_ADDTRANSCODEFILE', fileId);
});
```

## TEduBoard.EVENT.TEB_AUDIO_STATUS_CHANGED

媒体播放状态 [TEB_AUDIO_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_AUDIO_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | object | 回调数据 |
| `data.id` | string | 媒体 ID |
| data.status| number |媒体播放状态码 |
| data.progress| number |当前进度（秒） |
| data.duration| number |总时长（秒） |

```
teduBoard.on(TEduBoard.EVENT.TEB_AUDIO_STATUS_CHANGED, (data) => {
   console.log('======================:  ', 'TEB_AUDIO_STATUS_CHANGED', ' data:', data);
});
```

## TEduBoard.EVENT.TEB_DELETEBOARD

删除白板回调 [TEB_DELETEBOARD](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_DELETEBOARD)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| boardIds | Array | 删除的白板 ID 列表 |
| fileId | string | 删除白板所在的文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_DELETEBOARD, (boardIds, fileId) => {
   console.log('======================:  ', 'TEB_DELETEBOARD', ' boardIds:', boardIds, ' fileId:', fileId);
});
```

## TEduBoard.EVENT.TEB_DELETEFILE

删除文件事件 [TEB_DELETEFILE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_DELETEFILE)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| fileId | string | 删除文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_DELETEFILE, (fileId) => {
   console.log('======================:  ', 'TEB_DELETEFILE', ' fileId:', fileId);
});
```



## TEduBoard.EVENT.TEB_FILEUPLOADPROGRESS

文件上传进度 [TEB_FILEUPLOADPROGRESS](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_FILEUPLOADPROGRESS)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | object | 回调数据 |
| data.loaded | number | 当前已上传大小，单位 bytes |
| data.percent | number | 文件上传进度，取值范围 [0, 1] |
| data.speed | number | 文件上传速度，单位 bytes |
| data.total | number | 文件总大小，单位 bytes |
| data.userData | number | 透传上传文件配置的 userData 数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_FILEUPLOADPROGRESS, (name, url, userData) => {
   console.log('======================:  ', 'TEB_FILEUPLOADPROGRESS', name, url, userData);
});
```

## TEduBoard.EVENT.TEB_FILEUPLOADSTATUS

文件上传状态 [TEB_FILEUPLOADSTATUS](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_FILEUPLOADSTATUS)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data |	object |	回调数据 |
| data.code |	number |	文件上传状态 |
| data.message |	string |	状态秒速 |
| data.userData |	string |	透传上传文件配置的 userData 数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_FILEUPLOADSTATUS, (data) => {
   console.log('======================:  ', 'TEB_FILEUPLOADSTATUS', ' data:', data);
});
```

## TEduBoard.EVENT.TEB_GOTOBOARD

跳转白板页回调 [TEB_GOTOBOARD](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_GOTOBOARD)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| boardIds |	Array |	跳转到的白板页 ID |
| fileId |	string |	跳转到的白板页所属的文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_GOTOBOARD, (boardId, fileId) => {
   console.log('======================:  ', 'TEB_GOTOBOARD', ' boardId:', boardId, ' fileId:', fileId);
});
```

## TEduBoard.EVENT.TEB_GOTOSTEP

动画 PPT 步数变化回调 [TEB_GOTOSTEP](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_GOTOSTEP)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| currentStep |	number	| 当前白板页动画步数，取值范围 [0, totalStep) |
| totalStep |	number	| 当前白板页动画总步数 |

```
teduBoard.on(TEduBoard.EVENT.TEB_GOTOSTEP, (currentStep, totalStep) => {
   console.log('======================:  ', 'TEB_GOTOSTEP', currentStep, totalStep);
});
```

## TEduBoard.EVENT.TEB_H5BACKGROUND_STATUS_CHANGED

白板背景 H5 加载状态 [TEB_H5BACKGROUND_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_H5BACKGROUND_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| status |	number |	背景 H5 加载状态码 |
| data |	object |	回调数据 |
| data.currentBoardId |	string |	当前白板 ID |
| data.url |	string |	加载的 H5 页面 url |

```
teduBoard.on(TEduBoard.EVENT.TEB_H5BACKGROUND_STATUS_CHANGED, (status, data) => {
   console.log('======================:  ', 'TEB_H5BACKGROUND_STATUS_CHANGED', ' status:', status, ' data:', data);
});
```

## TEduBoard.EVENT.TEB_H5FILE_STATUS_CHANGED

白板 H5 文件加载状态 [TEB_H5FILE_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_H5FILE_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data |	object |	回调数据 |
| data.fileId |	string |	文件 ID |
| data.status |	number |	H5 文件加载状态码 |

```
teduBoard.on(TEduBoard.EVENT.TEB_H5FILE_STATUS_CHANGED, (data) => {
   console.log('======================:  ', 'TEB_H5FILE_STATUS_CHANGED', ' data:', data);
});
```

## TEduBoard.EVENT.TEB_H5PPT_STATUS_CHANGED

动画 PPT 加载状态回调 [TEB_H5PPT_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_H5PPT_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| status	| number |	动画 PPT 状态 |
| data	| object |	回调数据 |
| fid	| string |	当前文件 fid |
| message	| string |	描述信息 |

```
teduBoard.on(TEduBoard.EVENT.TEB_H5PPT_STATUS_CHANGED, (status, data) => {
   console.log('======================:  ', 'TEB_H5PPT_STATUS_CHANGED', status, data);
});
```

## TEduBoard.EVENT.TEB_IMAGE_STATUS_CHANGED

白板背景图片加载状态 [TEB_IMAGE_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_IMAGE_STATUS_CHANGED)

>!如果监听到 TEduBoard.TEduBoardImageStatus.TEDU_BOARD_IMAGE_STATUS_LOAD_ERROR, TEduBoard.TEduBoardImageStatus.TEDU_BOARD_IMAGE_STATUS_LOAD_TIMEOUT 事件，请引导用户调用 refresh 接口进行重新渲染白板。

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| status |	number |	图片加载状态码 |
| data |	object |	回调数据 |
| data.currentBoardId |	string |	当前白板 ID |
| data.imgUrl |	string |	加载的 url |
| data.currentImgUrl |	string |	已废弃，请忽略 |

```
teduBoard.on(TEduBoard.EVENT.TEB_IMAGE_STATUS_CHANGED, (status, data) => {
   console.log('======================:  ', 'TEB_IMAGE_STATUS_CHANGED', ' status:', status, ' data:', data);
});
```

## TEduBoard.EVENT.TEB_INIT

白板初始化事件 [TEB_INIT](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_INIT)

```
teduBoard.on(TEduBoard.EVENT.TEB_INIT, () => {
   console.log('======================:  ', 'TEB_INIT');
});
```

## TEduBoard.EVENT.TEB_OPERATE_CANREDO_STATUS_CHANGED

白板可恢复状态改变回调 [TEB_OPERATE_CANREDO_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_OPERATE_CANREDO_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| enable |	boolean |	白板当前是否还能执行 redo 恢复操作 |

```
teduBoard.on(TEduBoard.EVENT.TEB_OPERATE_CANREDO_STATUS_CHANGED, (enable) => {
   console.log('======================:  ', 'TEB_OPERATE_CANREDO_STATUS_CHANGED', enable);
});
```


## TEduBoard.EVENT.TEB_OPERATE_CANUNDO_STATUS_CHANGED

白板可撤销状态改变回调 [TEB_OPERATE_CANUNDO_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_OPERATE_CANUNDO_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| enable |	boolean	| 白板当前是否还能执行 undo 撤销操作 |

```
teduBoard.on(TEduBoard.EVENT.TEB_OPERATE_CANUNDO_STATUS_CHANGED, (enable) => {
   console.log('======================:  ', 'TEB_OPERATE_CANUNDO_STATUS_CHANGED', enable);
});
```

## TEduBoard.EVENT.TEB_RECTSELECTED

框选工具选中元素回调 [TEB_RECTSELECTED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_RECTSELECTED)

```
teduBoard.on(TEduBoard.EVENT.TEB_RECTSELECTED, () => {
   console.log('======================:  ', 'TEB_RECTSELECTED');
});
```

## TEduBoard.EVENT.TEB_REFRESH

刷新白板回调 [TEB_REFRESH](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_REFRESH)

```
teduBoard.on(TEduBoard.EVENT.TEB_REFRESH, () => {
   console.log('======================:  ', 'TEB_REFRESH');
});
```

## TEduBoard.EVENT.TEB_SETBACKGROUNDIMAGE

设置白板背景图片回调 [TEB_SETBACKGROUNDIMAGE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_SETBACKGROUNDIMAGE)

>!如果您设置背景图片直接设置的是一个 HTTPS 的 url，则图片名称和 userData 为空

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| name |	string	| 图片名称 |
| url |	string	| 图片 url |
| userData |	string	| 透传上传文件配置的 userData 数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_SETBACKGROUNDIMAGE, (name, url, userData) => {
   console.log('======================:  ', 'TEB_SETBACKGROUNDIMAGE', name, url, userData);
});
```

## TEduBoard.EVENT.TEB_SNAPSHOT

截图回调 [TEB_SNAPSHOT](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_SNAPSHOT)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data |	object	| 回调数据 |
| image |	string	| 图片的base64数据 |
| userData |	string	| 透传 userData 数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_SNAPSHOT, (data) => {
   console.log('======================:  ', 'TEB_SNAPSHOT', data);
});
```

## TEduBoard.EVENT.TEB_SWITCHFILE

切换文件事件 [TEB_SWITCHFILE](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_SWITCHFILE)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
|fileId	|string	|当前的文件 ID|

```
teduBoard.on(TEduBoard.EVENT.TEB_SWITCHFILE, (fileId) => {
   console.log('======================:  ', 'TEB_SWITCHFILE', ' fileId:', fileId);
});
```

## TEduBoard.EVENT.TEB_SYNCDATA

白板同步数据回调 [TEB_SYNCDATA](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_SYNCDATA)

1. 主动操作白板会回调该事件。
2. 收到该回调时需要将回调数据通过信令通道发送给房间内其他人，接受者收到后调用 addSyncData 接口将数据添加到白板以实现数据同步。
3. 切记该数据不需要再添加给操作者自己。
4. 如果您已经同时接入了 TIC，可忽略该事件，TIC 内部已经处理好了。

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | object | 操作白板数据 |

```
teduBoard.on(TEduBoard.EVENT.TEB_SYNCDATA, (data) => {
   console.log('======================:  ', 'TEB_SYNCDATA', data);
});
```

## TEduBoard.EVENT.TEB_TRANSCODEPROGRESS

转码进度回调 [TEB_TRANSCODEPROGRESS](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_TRANSCODEPROGRESS)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data |	object |	回调数据 |
| data.code |	number |	转码错误码 |
| data.message |	string |	转码错误信息 |
| data.userData |	string |	透传上传文件配置的 userData 数据 |
| data.status |	string |	转码状态 |
| data.taskId |	string |	转码任务 ID |
| data.progress |	string |	上传进度/转码进度<br/>1.当状态为 UPLOADING 的时候，进度值为上传进度<br/>2.当状态为 PROCESSING 的时候，进度值为转码进度 |
| data.pages |	string |	文件总页数 |
| data.resolution |	string |	文件分辨率 |
| data.resultUrl |	string |	转码完成后的 url |
| data.title |	string |	文件标题 |
| data.thumbnailResolution |	string |	缩略图分辨率 |
| data.thumbnailUrl |	string |	缩略图基础 url |

```
teduBoard.on(TEduBoard.EVENT.TEB_TRANSCODEPROGRESS, (data) => {
   console.log('======================:  ', 'TEB_TRANSCODEPROGRESS', data);
   if (res.code) {
     this.showErrorTip('转码失败code:' + res.code + ' message:' + res.message);
   } else {
     let status = res.status;
     if (status === TEduBoard.TEduBoardTranscodeFileStatus.TEDU_BOARD_TRANSCODEFILE_STATUS_ERROR) {
       this.showErrorTip('转码失败');
     } else if (status === TEduBoard.TEduBoardTranscodeFileStatus.TEDU_BOARD_TRANSCODEFILE_STATUS_UPLOADING) {
       this.showTip('上传中，当前进度:' + parseInt(res.progress) + '%');
     } else if (status === TEduBoard.TEduBoardTranscodeFileStatus.TEDU_BOARD_TRANSCODEFILE_STATUS_CREATED) {
       this.showTip('创建转码任务');
     } else if (status === TEduBoard.TEduBoardTranscodeFileStatus.TEDU_BOARD_TRANSCODEFILE_STATUS_QUEUED) {
       this.showTip('正在排队等待转码');
     } else if (status === TEduBoard.TEduBoardTranscodeFileStatus.TEDU_BOARD_TRANSCODEFILE_STATUS_PROCESSING) {
       this.showTip('转码中，当前进度:' + res.progress + '%');
     } else if (status === TEduBoard.TEduBoardTranscodeFileStatus.TEDU_BOARD_TRANSCODEFILE_STATUS_FINISHED) {
       this.showTip('转码完成');
       let config = {
         url: res.resultUrl,
         title: res.title,
         pages: res.pages,
         resolution: res.resolution
       }
       console.log('transcodeFile:', config);
       this.teduBoard.addTranscodeFile(config);
     }
   }
});
```

## TEduBoard.EVENT.TEB_VIDEO_STATUS_CHANGED
视频播放状态 [TEB_VIDEO_STATUS_CHANGED](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_VIDEO_STATUS_CHANGED)

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data	| object |	回调数据|
| data.fileId	| string |	文件 ID|
| data.status	| number |	视频播放状态码|
| data.progress	| number |	当前进度（秒）|
| data.duration	| number |	总时长（秒）|

```
teduBoard.on(TEduBoard.EVENT.TEB_VIDEO_STATUS_CHANGED, (data) => {
   console.log('======================:  ', 'TEB_VIDEO_STATUS_CHANGED', ' data:', data);
});
```

## TEduBoard.EVENT.TEB_VODEXTPARAM

需要设置点播视频的额外参数回调 [TEB_VODEXTPARAM](https://doc.qcloudtiw.com/web/TEduBoard.html#.event:TEB_VODEXTPARAM)

主要应用场景：老师设置了一个点播视频，若学生没有播放相关信息，学生可以再收到该事件后调用 setVODExtParam 接口设置

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data	| object |	回调参数 |
| fileId	| string |	白板文件 ID |
| appId	| string |	点播应用 ID |
| vodId	| string |	点播文件 ID |

```
teduBoard.on(TEduBoard.EVENT.TEB_VODEXTPARAM, (data) => {
   console.log('======================:  ', 'TEB_VODEXTPARAM', data);
});
```
