#### How to set up an image?  
Android:  
![mirrorAndroid](//mccdn.qcloud.com/static/img/9148c0611d28be304e4bd96dd20341ba/image.png)
	
iOS:   
Please see the content in the bold red box.
![mirrorIOS](//mccdn.qcloud.com/static/img/484da1414d62848bf0d77845586b7f02/image.png)

#### How to interpret the beauty filter parameters?  
Beautifying level is represented by a value ranging from 0 to 9.  
If the value is 0, beauty filter is disabled; A value of 9 indicates the highest level of beautifying effect.

#### The screen is blurred during an LVB.  
Use Data_Format_I420, instead of Data_Format_NV12, to render the remote frame.
![Blurred Screen](//mccdn.qcloud.com/static/img/1545ecd928d6cd59c2944b5699a2c02b/image.png)

#### How to deal with the black screen at viewer side when VJ returns to the foreground after switching to the background for a while (15s)?
Solution: VJ needs to disable the camera before switching to the background, and enable the camera again when switching back to the foreground.

	
#### The screen is flickering during an LVB.  
If the screen only flickers once when you join the room, refer to the latest version of FreeShow.  
If the screen keeps flickering, you should check if opengl was completely released last time at business side.
		
#### For some mobile phones, green screen occurs during an LVB.  
This is a compatibility issue on some special phones.  
Create screenshots of the model information in system settings of the phone and of the blurred video,  and then submit them to technical support.
		
#### A small screen occurs on the upper right corner of the LVB.    
id in MySelfInfo cannot be empty.

#### Solution to reverse of camera in versions earlier than Android 1.7

Modification to AvActivity class

Add the code in the yellow box shown below to the corresponding location in AvActivity class.

![AvActivity](//mccdn.qcloud.com/img56cde3ee57ed1.png)

```c++
Log.d("shixu", "isfront: " + isFront);
				
if (isFront) {
	mQavsdkControl.setMirror(true, mSelfIdentifier);
} else {
	mQavsdkControl.setMirror(false, mSelfIdentifier);
}
```

Modification to AVUIControl class

Add the code in the yellow box shown below to the corresponding location in AVUIControl class.

![AVUIControl](//mccdn.qcloud.com/img56cde50e6c1dc.png)

```c++
if (isFrontCamera()) {
	view.setMirror(true);
} else {
 view.setMirror(false);
}
```

```c++
private boolean isFrontCamera() {
    QavsdkControl mQavsdkControl = ((QavsdkApplication)(mContext.getApplicationContext())).getQavsdkControl();
		
    Log.d("shixu", "is front camera: " + mQavsdkControl.getIsFrontCamera());
    return mQavsdkControl.getIsFrontCamera();
}
	
public void setMirror(boolean isMirror, String identifier) {
    GLVideoView view = null;
    int index = getViewIndexById(identifier, AVConstants.VIDEO_SRC_CAMERA);		
    if (index >= 0) {
        view = mGlVideoView[index];
        view.setMirror(isMirror);
    }
}
```

Modification to QavsdkControl class

Add the code in the yellow box shown below to the corresponding location in QavsdkControl class.

![](//mccdn.qcloud.com/img56cde60fd1e7c.png)

```c++
public void setMirror(boolean isMirror, String identifier) {
    if (null != mAVUIControl) {
        mAVUIControl.setMirror(isMirror, identifier);
    }
}
```
