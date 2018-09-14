# Configuring Project

## SDK

You can obtain [Tencent Video Cloud SDK](https://cloud.tencent.com/document/product/454/7873#Windows) from the Tencent Cloud official website.

![img](https://mc.qcloudimg.com/static/img/df957e048bec696128c99c1eee9cac5b/image.png)

| File Name | Description |
| ---- | ---------------------------------------- |
| Demo | Contains the Demo installation package and source code. Upon the quick installation of the Demo package, the SDK features are ready to use. You can use Visual Studio to open the project of the source code. |
| doc | Contains project configuration and SDK connection documents. |
| SDK | ".dll" file. The C# assembly "ManageLiteAV.dll" can be imported to the C# project. |

## Visual Studio Project Configuration

### Development environment

- Visual Studio: 2010 and later.
- .Net framework: 4.0 and later.
- Windows: Windows 7 and later.

### C# Project Reference SDK

The following describes how to configure the SDK in a Visual Studio project using a simple C# WinForm project.

#### Step 1: Copy the SDK file

Create a C# WinForm application project and name it "HelloSDK". Make sure you use .NET Framework 4 or above.

![img](https://mc.qcloudimg.com/static/img/668b22b88f23371392887c1bcf45bc9c/image.png)

Copy the downloaded SDK file to the project directory.

![img](https://mc.qcloudimg.com/static/img/c42d7e6bac46055d6e1883f2d873fafa/image.png)

Open the reference manager page in the HelloSDK project and click **Browse**. Add the reference "ManageLiteAV.dll", as shown below:

![img](https://mc.qcloudimg.com/static/img/70adffa08d71e3c9fd0ecf04609b7163/image.png)

#### Step 2: Verify the configuration

Call SDK API in the HelloSDK code and display the camera preview to verify whether the project is correctly configured.

#### Add code

Add a "ManageLiteAV.TXLivePusher" instance to the Form1 class.

```c#
private ManageLiteAV.TXLivePusher pusher = new ManageLiteAV.TXLivePusher();

```

Add the "Load" event to the attribute panel. Add the code to enable the camera preview feature for "ManageLiteAV.TXLivePusher".

```c#
private void onLoaded(object sender, EventArgs e)
{
  // At least one camera is available by default. So, enter 0 for cameraIndex.
  pusher.startPreview(this.Handle, 0, 0, this.Width, this.Height, 0);
}

```

#### Compile code and run project

Open the attribute page of the HelloSDK project. Add the post-build command line, which is used to copy the .dll files to the directory where the exe file is located.


```
copy /Y $(ProjectDir)SDK\*dll $(ProjectDir)bin\$(ConfigurationName)
```

The command line is added as follows:

![img](https://mc.qcloudimg.com/static/img/78ae9d86c9ed6a52134b045dfcf7759a/image.png)



Compile (F7) the code, and then run and debug (F5) the project. You can see the camera image displayed in the window.

![img](https://mc.qcloudimg.com/static/img/f65f857ac26d5ca67653953381cbd3e9/image.png)

Now, the project configuration is completed.

