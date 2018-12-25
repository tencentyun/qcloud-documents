## SDK Information

You can update the [LVB SDK](https://cloud.tencent.com/document/product/454/7873#Windows) on Tencent Cloud's official website. The SDK for Windows only offers simplified features:

| Version Type  | Feature      |
| ----- | ------- |
| LVB simplified version | Support push and LVB |

The decompressed SDK is composed as follows:

| File Name | Description |
| ---- | ---------------------------------------- |
| SDK | SDK include, lib, and dll files with detailed API description |
| Demo | The simplified Demo based on the implicitly linked dynamic library, including a simple demonstration of UI and main SDK features. Use VS2015 to quickly import the demo and try it out. |



# Visual Studio Project Settings

### Environment requirements

OS: Windows 7 and later

Visual Studio: 2008 and later

Note: For the project of CustomServiceDemo, Visual Studio 2015 and later as well as Qt 5.9 and later are supported.

### Qt project settings

After installing Qt 5.9 32bit and Visual Studio Add-in For Qt plug-in, add Qt Versions to the Qt VS Tools-Qt Options in Visual Studio, as shown below:

 ![Qt Configuration](https://mc.qcloudimg.com/static/img/346ddef0ba104dc80d9c97c26cbb491c/image.png)

 

### Project settings

The following describes how to configure the SDK in a Visual Studio project using a simple Qt GUI application project.

#### 1. Create a Qt project

In this example, create a Qt GUI application named HelloSDK, as shown below:

![Create a Qt Project](https://mc.qcloudimg.com/static/img/534bd4cce457177fcfa881f6210c94c7/image.png)



Right-click the project, and select Qt Project Settings to set Version. See the figure below:

![Qt Project Settings](https://mc.qcloudimg.com/static/img/dae8799af9bff189aa3d99c6e1bd1dea/projectSettings.png)



#### 2. Copy the SDK file

Create a LiteAV folder in the project directory, and copy the content of the downloaded SDK folder to the project directory. The figure below shows the directory structure:

![Add an SDK](https://mc.qcloudimg.com/static/img/9711459381060166cb58d377ab012ef4/image.png)



#### 3. Add a library dependency

Add an additional library directory from **Project Attribute** -> **Linker** -> **General**, as shown below:

![Library Dependency Directory](https://mc.qcloudimg.com/static/img/c3d07c0e1ef204769c9f225a45ae8ddb/image.png)

 

Add liteav.lib from **Project Attribute** -> **Linker** -> **Input** -> **Add a Dependency**, as shown below:

![Add a Dependency](https://mc.qcloudimg.com/static/img/0622a4c4de74fe428fec29a5a77ccf7c/image.png)



#### 4. Add a header file

Add additional include directories from **Project Attribute** -> **C/C++** -> **General**, as shown below:

![Header File Directory](https://mc.qcloudimg.com/static/img/3cb935ab16af77b328feb7798a68ccf2/image.png)



Note that this operation is not mandatory. If you do not add the header file search path for LiteAV/include, "LiteAV/include" needs to be added before the SDK-related header file when the header file is referenced, as shown below:

```
#include "LiteAV\include\TXLivePusher.h"
```



### Verification

#### 1. Add a rendering control

Open HelloSDK.ui from the project "From Files", and drag a Widget control to the form, as shown below:

![Add a Widget](https://mc.qcloudimg.com/static/img/b66c3b6e742172a31f84449f4c05c232/image.png)



#### 2. Reference the header file

Reference the SDK header file at the beginning of HelloSDK.cpp:

```
#include "TXLivePusher.h"
```



#### 3. Add calling code

Declaration

```
#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_HelloSDK.h"
#include "TXLivePusher.h"

class HelloSDK : public QMainWindow
{
	Q_OBJECT

public:
	HelloSDK(QWidget *parent = Q_NULLPTR);

private:
	Ui::HelloSDKClass ui;
	TXLivePusher m_pusher;
};
```

Implementation

```
#include "HelloSDK.h"

HelloSDK::HelloSDK(QWidget *parent)
	: QMainWindow(parent)
{
	ui.setupUi(this);
	m_pusher.startPreview((HWND)ui.widget->winId(), RECT{ 0, 0, ui.widget->width(), ui.widget->height() }, 0);
}
```



#### 4. Copy dll

Copy the dll required by the program from LiteAV to the release path, as shown below:

![dll List](https://mc.qcloudimg.com/static/img/5106cb967e9c43e8ae39b1ed6824bcab/image1.png )



#### 5. Compile and run the project

The HelloSDK project can be successfully compiled and run if you performed the previous steps correctly. Launch the project under Release, and then you can see the screen captured by the camera display on the program form:

![Effect Picture](https://mc.qcloudimg.com/static/img/f65f857ac26d5ca67653953381cbd3e9/image.png)

