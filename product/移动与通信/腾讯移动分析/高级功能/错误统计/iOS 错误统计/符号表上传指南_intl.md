### Instructions on Exception Reporting
Exception reporting feature is enhanced in the new version of MTA. When an exception occurs with an App, MTA can collect the latest NSLog, page information and crash stack for reporting. Besides, you can also report business-related tag and diagnostic information based on your needs for debugging purpose. The API for reporting diagnostic information is in the MTACrashReporter.h header file. Refer to the header file notes for usage.
In addition, to more accurately restore the crash stack, you need to provide the dSYM file of the App. The steps for creating the dSYM are as follows.
1. Find **Debug Information Format** in Xcode project configuration, and change its value to **DWARF with dSYM File**, as shown below:
![](//mc.qcloudimg.com/static/img/9a797e9bd724ec827bc5d0e1af12d321/image.png)
2. Follow the steps for packaging. After this, right click on the popup window and select **Show in Finder** in the menu, as shown below:
![](//mc.qcloudimg.com/static/img/98bf5d84bac542fa5d8453924242e3ab/image.png)
3. You can see the xcarchive file generated in the previous step in the popped-up Finder page. Right click on the file, and select **Show Package Contents**, as shown below:
![](//mc.qcloudimg.com/static/img/5c06bd953d098c9b9e2558fb89975c20/image.png)
4. Find the dSYM file in the dSYMs directory, right click on it and select **Show Package Contents**, as shown below:
![](//mc.qcloudimg.com/static/img/e359d923d75558867c76a549485905b1/image.png)
5. Find the file in the Contents/Resources/DWARF directory and directly upload it.
![](//mc.qcloudimg.com/static/img/0d4c0241010770be6be4bb8220fc20d3/image.png)
Find the dSYM file and upload it using an upload tool or on the web-based console.

### iOS Crash Error Analysis Upload Tool

iOS Crash symbol table upload tool is mainly used to upload App's symbol table file (dSYM file), so that the stack information of the App crash is displayed on the web page to restore the symbols. In this case, developers can directly see the location and reason of the occurrence of the program Crash. You can click [Download](http://mta.qq.com/mta/resource/download/MTAdSYMUploader.dmg) or download it from the error management window. The usage is as follows:
![](http://developer.qq.com/wiki/mta/imgs/20170122160938_18410.jpg)
**Parameters of the tool:**
QQ account: Admin of the App in the MTA frontend web page.
App ID: The App ID in the **App Management** tab at the MTA frontend.
App Key: The App KEY in the **App Management** tab at the MTA frontend.
dSYM: Symbol table file generated when compiling the App.
>**Note:**
>Generally, you can see the symbol table file generated when the App is compile from the DebugInformation in the **Xcode** -> **Target** -> **BuildSetting** -> **Build Options** tab. The location of the symbol table file is the same as that of the generated App.

![](http://developer.qq.com/wiki/mta/imgs/20170122160956_87481.png)
