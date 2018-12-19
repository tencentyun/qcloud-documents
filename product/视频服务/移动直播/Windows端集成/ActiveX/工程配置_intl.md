## Application Scenarios

IE browser is suitable for **ToB** scenarios, such as **enterprise customer service** and **online education**. These scenarios share a common feature: operators can accept unified training and can be required to use IE browser. But in ToC scenarios, the users are picky.

It is not easy to realize audio/video feature with excellent experience and performance on a Web page. HTML5 provides a weak &lt;video&gt; tag capability. Browser support and customization capabilities of WebRTC is not good (for example, beauty filter is not supported). So the ActiveX plug-in technology of IE browser is still popular in some vertical scenarios of ToB.

## The principle of ActiveX
![](https://mc.qcloudimg.com/static/img/7f306e37bc3b66e0cf2bb778d0f4726e/image.png)

The principle of the ActiveX plug-in is to add new objects to your web pages in a way approved by the IE browser. These objects are not supported on native browsers. When your pages are using these objects, the IE browser will show a prompt window to prompt the user whether to install the ActiveX plug-in. When the user clicks "Install", the new object capability will be loaded into your page along with the installation of the plug-in.

The ActiveX plug-in mainly adds two useful objects to your IE browser: pusher and player.

| Object | CLSID | Description |
|---------|---------|---------|
| pusher | 01502AEB-675D-4744-8C84-9363788ED6D6 | Push, also called audio/video upstream, includes collection, coding and transmission |
| player | 99DD15EF-B353-4E47-9BE7-7DB4BC13613C | Playback, also called audio/video downstream, including download, buffering, decoding and playback |

## How Do I Use It

### Environment requirements
- Windows 7 or above
- Internet Explorer 10, Internet Explorer 11

### Obtain CAB
You can obtain the latest ActiveX plug-in from [SDK Download](https://cloud.tencent.com/document/product/454/7873#Windows) on Tencent Cloud official website. After decompressing the downloaded zip package, you can obtain the following files:

| File Name | Description |
| ------- | ------------------------------------------------------------ |
| demo | The demo contains html and js source code for calling sdk/LiteAVAX.cab. You can directly refer to how to use activex plug-in to develop audios and videos. The supported demo includes push and pull, two-person video, multi-person video, LVB, etc. [Try Out Demo](https://cloud.tencent.com/document/product/454/6555) |
| sdk | The ActiveX plugin is LiteAVAX.cab, which is included in the html and js resource package. The version indicates the current plugin version number. |
| docment | Detailed access document |

### Sample code

The pusher and player objects in the ActiveX plug-in can be used with the &lt;object&gt; tag. Here is a sample of code:

```html
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
<TITLE> ActiveX Plug-in test code</TITLE>
<script type="text/javascript" src="pusher_player.js" charset="utf-8"></script>
</HEAD>
<BODY>
  Push URL:
  <input size="90" id="URLInputField" value="">
  <input type=submit value="Test push" onClick="doStartPush(document.getElementById('URLInputField').value);">
  <br/>
  <!--Warning: If you directly copy the code, you need to modify the LiteAVAX.cab path and version number.-->
  <object ID="pusher" CLASSID="CLSID:01502AEB-675D-4744-8C84-9363788ED6D6"
                        codebase="./LiteAVAX.cab#version=1,2,0,0"
                        width="640"
                        height="480">
  </object>
  <script>
	  function doStartPush(targetURL) {
			pusher.startPush(targetURL);
	  }
  </script>
</BODY>
</HTML>
```

### Plug-in deployment
Save the sample code above as a demo.html file, and put it on your server, and then copy LiteAVAX.cab to a directory (in the sample code above, LiteAVAX.cab and demo.html are located in the same directory).

### Test effect
Run demo.html using IE browser to check if the USB camera is plugged in properly. Enter the [push URL](https://cloud.tencent.com/document/product/454/7915) and click the "Test Push" button:

![](https://mc.qcloudimg.com/static/img/39fe0af10c43aa123c80e0887b66a227/image.jpg)


### Plug-in upgrade
After the Zip package is decompressed, name the folder as LiteAV_AX_SDK2.2.1.0, where 2,2,1,0 is the version number of the ActiveX plug-in. This version number should be clearly specified and aligned in the web page code "./LiteAVAX.cab#version=1,2,0,0", otherwise plug-in loading may fail.

![](//mc.qcloudimg.com/static/img/fcb7bafcdaae5878a63a50db2df7c8a8/image.jpg)

As the Tencent Cloud team will continue to improve the plug-in for better features and effects, how do you upgrade when you get a new version of cab?

- Replace the old version of the LiteAVAX.cab file on your server with the new version.
- Update the old version number in codebase with the new version number (1,2,1,0). The new plug-in version number must be greater than the old version number.



