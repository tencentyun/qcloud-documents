## 一. 介绍
音视频SDK的视频接口返回了视频帧数据，用户可以通过自己编写视频渲染的代码对视频帧数据进行渲染，将画面展现在屏幕上。虽然音视频SDK没有提供视频渲染的接口，但是提供了一套视频渲染的类库嵌入在demo中，用户也可以使用我们的类库直接地实现渲染功能，将数据快速转换为画面展示在屏幕上。

## 二.  集成指引
### 1.导入文件
类库位置：
- 1.%root%\samples\sample2\public\QAVSDKDemo\AVWrapper\AVFrameDispatcher.h和AVFrameDispatcher.m
此处及以下的%root%都表示腾讯云官网提供的SDK包的根目录
- 2.%root%\samples\sample2\public\QAVSDKDemo\OpenGL_Restruct文件夹
将其集成进入自己的工程中，集成后如图所示
![](//mccdn.qcloud.com/static/img/52c94ef63daf4dabb92f941db2e6100b/image.png)

### 2.解决编译问题
由于渲染的模块不是ARC模式的，假如工程使用MRC的模块，要在Targets -> Build Phrases -> Compile Sources里面将刚刚导入的渲染模块的全部文件加入编译标记 -fno-objc-arc 即可解决，效果如图所示：
![](//mccdn.qcloud.com/static/img/32213471324acf314e8883f1c52b19ed/image.png)

### 3.添加头文件

添加渲染模块的头文件，若编译通过，则集成成功


```
#import "AVFrameDispatcher.h"
#import "AVGLBaseView.h"
```

## 三. 使用渲染模块渲染本地视频流
用渲染模块渲染本地视频进一个90*120的小画面

### 1.创建渲染的容器
.h文件里添加渲染的容器和分发器的声明：


```
    AVGLBaseView *avGLImageView;     //渲染的容器
    AVSingleFrameDispatcher *frameDispatcher;//分发器

```
实例化渲染的容器和分发器：

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
### 2. 创建小画面并添加入渲染模块中
 

```
    AVGLRenderView *smallView = [[AVGLRenderView alloc]initWithFrame:CGRectMake([UIScreen mainScreen].bounds.size.width - 120, [UIScreen mainScreen].bounds.size.height - 200 - 120, 90, 120)];
    
    NSString *renderKey = [NSString stringWithFormat:@"%@%d",[AVUtil sharedContext].Config.identifier,1];
    
    [frameDispatcher.imageView addSubview:smallView forKey:renderKey];
    [frameDispatcher.imageView bringSubviewToFront:renderKey];
    [frameDispatcher.imageView setBackGroundTransparent:YES];
    frameDispatcher.imageView.hidden = NO;
    avGLImageView.hidden = NO;

```
### 3.开始用分发器渲染
在本地视频数据回调OnLocalVideoPreview方法中添加一句代码即可。

```
#pragma mark - 本地视频数据回调 -
- (void)OnLocalVideoPreview:(QAVVideoFrame *)frameData
{
    [frameDispatcher dispatchVideoFrame:frameData isSubFrame:NO];
}

```
## 四. 使用渲染模块渲染远端视频流
用渲染模块渲染远端的视频，并以全屏显示，中心思想大致与第三条渲染本地视频流一样

### 1.创建渲染的容器
创建渲染容器与渲染本地视频流第一步一致，请参考

### 2.创建大画面并添加入渲染模块中
在得到要请求的远端的identifier和视频源类型requestedScrType的前提下，可用以下示例代码：


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
### 3. 开始用分发器渲染
在对端视频数据回调OnVideoPreview方法中添加一句代码即可。

```
#pragma mark - 对端视频数据 -
- (void)OnVideoPreview:(QAVVideoFrame *)frameData
{
    [frameDispatcher dispatchVideoFrame:frameData isSubFrame:NO];
}
```
 通过以上步骤即可得到把远端视频在大画面中渲染并显示，把本地视频在小画面中渲染并显示的效果。

## 五. 停止视频渲染
假如用户要停止视频渲染，退出房间，则需要调用停止渲染的方法，示例代码如下：

```
#pragma mark - 停止渲染 -
- (void)destroyRendering
{
    if ([identifierListArray count]) {
        //遍历所有成员，取得他们的renderKey并移除
        for (int index = 0 ; index < [identifierListArray count]; index++) {
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