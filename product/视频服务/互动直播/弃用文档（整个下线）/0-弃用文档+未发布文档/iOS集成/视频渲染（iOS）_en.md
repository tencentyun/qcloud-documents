## Overview
You can render the video frame data returned by the video API of audio/video SDK by writing your own video rendering code to present the video view on the screen. The audio/video SDK does not provide API for rendering video, but provides a set of class libraries for video rendering that are embedded in the demo. You can also directly use the class libraries to implement rendering, quickly converting the data to video views to be displayed on screen.

## Procedures for Integration
### 1. Import the files
Location of class libraries:
- (1) %root%\samples\sample2\public\QAVSDKDemo\AVWrapper\AVFrameDispatcher.h and AVFrameDispatcher.m
The %root% here and below indicates the root directory of the SDK provided by Tencent Cloud.
- (2) %root%\samples\sample2\public\QAVSDKDemo\OpenGL_Restruct folder
Integrate it into your own project, as shown in the figure:
![](//mccdn.qcloud.com/static/img/52c94ef63daf4dabb92f941db2e6100b/image.png)

### 2. Resolve the compilation issue
As the rendering module is not in an ARC mode, if the project uses an MRC module, you need to go to "Targets" -> "Build Phrases" -> "Compile Sources" to add the compiling tag -fno-objc-arc in all the files of rendering module that were just imported, as shown below:
![](//mccdn.qcloud.com/static/img/32213471324acf314e8883f1c52b19ed/image.png)

### 3. Add the header file

Add the header file of the rendering module. A success of the compilation indicates the success of integration.


```
#import "AVFrameDispatcher.h"
#import "AVGLBaseView.h"
```

## Use the rendering module to render the local video stream
Use the rendering module to render the local video into a 90*120 small view

### 1. Create a rendered container
The declaration for adding rendered container and dispatcher in .h file:


```
    AVGLBaseView *avGLImageView;     //Rendered container
    AVSingleFrameDispatcher *frameDispatcher;//Dispatcher

```
Instanced rendered container and dispatcher

```
    CGRect imageRect = CGRectMake(0, 0, [UIScreen mainScreen].bounds.size.width, [UIScreen mainScreen].bounds.size.height);
    avGLImageView = [[AVGLBaseView alloc]initWithFrame:imageRect];
    avGLImageView.backgroundColor = [UIColor clearColor];
    [avGLImageView setBackGroundTransparent:YES];
    [self.view addSubview:avGLImageView];
    avGLImageView.hidden = YES;
    
    [avGLImageView initOpenGL];
    [avGLImageView startDisplay];
    
    frameDispatcher = [[AVSingleFrameDispatcher alloc]init];
    frameDispatcher.imageView = avGLImageView;

```
### 2. Create a small view and add it to rendering module
 

```
    AVGLRenderView *smallView = [[AVGLRenderView alloc]initWithFrame:CGRectMake([UIScreen mainScreen].bounds.size.width - 120, [UIScreen mainScreen].bounds.size.height - 200 - 120, 90, 120)];
    
    NSString *renderKey = [NSString stringWithFormat:@"%@%d",[AVUtil sharedContext].Config.identifier,1];
    
    [frameDispatcher.imageView addSubview:smallView forKey:renderKey];
    [frameDispatcher.imageView bringSubviewToFront:renderKey];
    [frameDispatcher.imageView setBackGroundTransparent:YES];
    frameDispatcher.imageView.hidden = NO;
    avGLImageView.hidden = NO;

```
### 3. Start rendering with the dispatcher
You just need to add a code line in the local video data callback OnLocalVideoPreview method.

```
#pragma mark - Local video data callback -
- (void)OnLocalVideoPreview:(QAVVideoFrame *)frameData
{
    [frameDispatcher dispatchVideoFrame:frameData isSubFrame:NO];
}

```
## Use the rendering module to render the remote video stream
Render the remote video with the rendering module and display it in full screen, in a similar way as rendering local video stream as described in Section 3.

 ### 1. Create a rendered container
Create a rendered container in the same way as described in Step 1 for rendering local video stream.

### 2. Create a large view and add it to the rendering module
After obtaining the identifier of remote end and video source type requestedScrTyp, you can use the following sample code:


```
            NSString *renderKey = [NSString stringWithFormat:@"%@%d",identifier,requestedScrType];
            
            CGRect rect = CGRectMake(0, 0, [UIScreen mainScreen].bounds.size.width, [UIScreen mainScreen].bounds.size.height);
            
            AVGLRenderView *glView = [avGLImageView getSubviewForKey:renderKey];
            if (glView == nil) {
                glView = [[AVGLRenderView alloc]initWithFrame:rect];
                [avGLImageView addSubview:glView forKey:renderKey];
                
                [glView setBoundsWithWidth:0];
                [glView setHasBlackEdge:NO];
                
                glView.nickView.hidden = YES;
                [glView setBoundsWithWidth:0];
                [glView setDisplayBlock:NO];
                
                [glView setCuttingEnable:YES];
            }
            else
            {
                [glView setFrame:rect];
            }
```
### 3. Start rendering with the dispatcher
You just need to add a code line in the peer video data callback OnVideoPreview method.

```
#pragma mark - Peer video data -
- (void)OnVideoPreview:(QAVVideoFrame *)frameData
{
    [frameDispatcher dispatchVideoFrame:frameData isSubFrame:NO];
}
```
 Through the above steps, you can render and display the remote video and local video in a big view and small view, respectively.

## Stop Video Rendering
To stop the video rendering and exit the room, you need to call the method to stop rendering. The sample code is as follows:

```
#pragma mark - Stop rendering -
- (void)destroyRendering
{
    if ([identifierListArray count]) {
        //Traverse all members, and get and remove their renderKeys
        for (int index = 0 ; index < [identifierListArray count];index++) {
            NSString *identifier = [identifierListArray objectAtIndex:index];
            int requestedScrType = [[scrTypeListArray objectAtIndex:index]intValue];
            
            NSString *renderKey = [NSString stringWithFormat:@"%@%d",identifier,requestedScrType];
            
            [avGLImageView removeSubviewForKey:renderKey];
        }
        [NSObject cancelPreviousPerformRequestsWithTarget:avGLImageView selector:@selector(startDisplay) object:nil];
        [avGLImageView destroyOpenGL];
        [avGLImageView stopDisplay];
        [avGLImageView removeFromSuperview];
        
        [avGLImageView removeSubviewForKey:[AVUtil sharedContext].Config.identifier];
        
        avGLImageView = nil;
    }
        frameDispatcher.imageView = nil;
}

```
