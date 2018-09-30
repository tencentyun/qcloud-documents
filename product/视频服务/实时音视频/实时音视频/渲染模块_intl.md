
## Overview
Previously, after iLiveSDK discloses the decoded video frame image data to its user, the user must render these video data. But iLiveSDK 1.7.1.2 provides a rendering module, which is recommended for video rendering. This rendering module uses DX to render in GPU, reducing the CPU usage. Users only need to pass in a window handle to render a video in a specified window. Of course, users can also perform video rendering without the rendering module.

## iLiveSDK Rendering Module
### Detecting supported rendering modes
The iLiveSDK rendering module uses DX acceleration by default. DX is not supported by the system in rare cases (such as in safe mode) and GDI will then be used for rendering. The current rendering module only supports the I420 color format for the DX mode and RGB24 for GDI, which can be obtained as follows:
```
iLiveRootView* pView = iLiveCreateRootView();
E_RootViewType viewType = pView->getRootViewType(); //COLOR_FORMAT_I420\COLOR_FORMAT_RGB24
pView->destroy();
```
### Setting the color format for video callback
You need to set a color format for iLiveSDK video callback, as it varies with the rendering mode.
The API setVideoColorFormat() can be used to set the color format (RGB24\I420) for video callback. After that, the specified color format will be used for both local and remote video callbacks, as shown below.
```
E_ColorFormat fmt;  //COLOR_FORMAT_I420\COLOR_FORMAT_RGB24
GetILive()->setVideoColorFormat(fmt);
```
### Renderer initialization and setup
To render a video, you must specify a window handle for video rendering, as shown below:
```
HWND hwnd; //Window handle for video rendering
iLiveRootView* pRootView = iLiveCreateRootView();
bool bRet = pRootView->init( hwnd );
```
After the renderer is initialized, you must assign a View to it, that is, setup the user ID of the video to be rendered and the position of the rendered image in the window, as shown below:
```
String      identifier; //User ID of the video to be rendered
E_VideoSrc  type;        //Type of the video to be rendered (main camera, screen sharing, and file playback);
iLiveView   view;
view.mode = VIEW_MODE_HIDDEN;    //VIEW_MODE_HIDDEN - Scale to fill the black border; VIEW_MODE_FIT - Stretch the screen to fit the control size;
view.exclusive = true; //Whether this view exclusively uses the entire window; If not, you need to set the x, y, width, height, zorder and other parameters of the view, as detailed in the API.
pRootView->setView(identifier, type, view, false);
```
When the program exits, it is better to release and terminate the renderer.
```
pRootView->uninit();
pRootView->destroy();
```
### Register video callback and video rendering
After registering video callback in iLiveSDK, you will receive the video data for each frame. During the callback of video data, the doRender() API of the rendering module can be called for video rendering. For example, the code for rendering the local video is as follows.
```
void OnLocalVideo(const LiveVideoFrame* frame, void* data)
{
    //Each frame of the local video will be received here and the color format set above is used for rendering.
    m_pRootView->doRender(frame); //The rendering module will rotate and render video frames with rendering angles;
}
GetILive()->setLocalVideoCallBack(OnLocalVideo, NULL);
```
### Video cleanup in renderer
Generally, when video streaming is disconnected (for example, camera is disabled), it is necessary to clean up the rendered images so that it does not stay on the last frame. This can be done by calling renderer's removeView()\removeAllView() API, as shown below:

`pRootView->removeAllView();`

