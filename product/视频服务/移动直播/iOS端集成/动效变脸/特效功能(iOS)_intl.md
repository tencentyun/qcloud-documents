# Special Effects (Eye Enlarging, Face Slimming, Dynamic Effect, Green Screen)

## Feature Description

Eye enlarging, face slimming, dynamic sticker, green screen and other special effects are licensed features developed based on the face recognizing technology of YouTu Lab and the beautifying technology of Pitu. By working with YouTu Lab and Pitu, Tencent Cloud Mini LVB integrates these special effect features into the image processing process of RTMP SDK to achieve better video effects.

## Integration Procedure

Application procedure:

1. Submit a ticket or contact one of our customer service representatives by calling 400-9100-100.

2. Download the [sample form](https://mc.qcloudimg.com/static/archive/766c9092424d0440a31c56c81f34a629/archive.xlsx), fill in the information, and send it to jerryqian@tencent.com and copy it to your customer service representative (important).

3. Ask your customer service representative to confirm the e-mail by replying to it. Otherwise, the e-mail may be treated as a harassing e-mail.

4. As soon as the e-mail is confirmed, we will apply for a trial License from Youtu Lab and send the License along with the package decompression password to you.

   Two types of License:

   - Trial License: It is **valid for one month**, and used to debug and test the dynamic effects SDK. If your App is published with a trial License, the dynamic effects will not work normally after the License expires.
   - Official License: The validity period (usually one year) is subject to the contract.

## Version Download
You can download the compressed SDK package (VIP version) at the bottom of the [RTMP SDK package](https://cloud.tencent.com/document/product/454/7873). The compressed SDK package is encrypted, and you can obtain the decompression password & License in the integration procedure. After the package is decompressed successfully, you will get `Demo` and `SDK`. Resources related to special effects are placed in SDK/Resource.

> You can distinguish the VIP version and non-VIP version by viewing the SDK's bundler id. > - The bundler id of the non-VIP version is com.tencent.TXRTMPSDK, and that of the VIP version com.tencent.TXRTMPSDK.pitu.
>
> VIP and non-VIP SDKs can also be intuitively distinguished by size, because VIP SDK is much greater than non-VIP SDK.



## Xcode Project Settings

For more information, please see [Project Configuration](https://cloud.tencent.com/document/product/454/7876) 

### 1. Add frameworks

The VIP edition requires to link with additional system frameworks.
> 1. AssetsLibrary.framwork
> 2. CoreMedia.framework
> 3. Accelerate.framework
> 4. Metal.framework 

### 2. Add link parameters

Under **Build Setting** -> **Other Link Flags**, add the `-ObjC` option.

### 3. Add Dynamic Effect Resources

Add the following files in SDK/Resource to the project

> 1. 3DFace
> 2. detector.bundle
> 3. FilterEngine.bundle
> 4. model  
> 5. PE.dat
> 6. poseest.bundle
> 7. RPNSegmenter.bundle
> 8. ufa.bundle


Add the SegmentationShader.metal file under Demo/TXLiteAVDemo/Resource/Beauty/pitu/data/ to the project
> 1. SegmentationShader.metal

### 4. Add dynamic effect resources

Add the resources under the Resource of the zip package to the project as groups reference. Note: handdetect, handtrack, and res18_3M are to be added as folder reference. You can directly add SegmentationShader.metal under Demo/TXLiteAVDemo/Resource/Beauty/pitu/data/. Specific operations are shown below:
![](https://mc.qcloudimg.com/static/img/d9c501a923b7dbc08f9467da07595b58/image.png)  
![](https://mc.qcloudimg.com/static/img/7a4c4c93298ba65b83fdd63b8b52de42/image.png)

These resources must be added correctly. Otherwise, a crash may occur when the material is switched to the face-transforming type.

### 5. Import license files
The license of the VIP version needs to be verified to enable some of the features. You can contact one of our customer service representatives to apply for a 30-day free license for debugging.
After you obtain a license, name the license as **YTFaceSDK.licence** and place it in the project as shown in the figure above.

> Each license is bound with a specific Bundle Identifier. Modifying the Bundle Identifier of the App will result in verification failure.
>
> YTFaceSDK.licence cannot be renamed or modified.
> 
> You do not need to apply for licenses for iOS and Android separately. One license can be used to authorize the bundleid in iOS and the packageName in Android simultaneously.

## Feature Calling

### 1. Dynamic sticker

Example:

![](https://mc.qcloudimg.com/static/img/a320624ee8d3a82ee07feb05969e5290/A8B81CB6-DBD3-4111-9BF0-90BD02779BFC.png)

A dynamic effect template is a directory, which contains a lot of resource files. The directory number and file size of each dynamic effect template vary depending on the complexity of the dynamic effect.

The sample code in Mini LVB downloads the dynamic effect resources from the backend, and then the resources are decompressed to the Resource directory. You can find the download addresses of the dynamic effect resources and thumbnails in the Mini LVB code in the following format:

> `https://st1.xiangji.qq.com/yunmaterials/{Dynamic Effect Name}.zip`
>
> `https://st1.xiangji.qq.com/yunmaterials/{Motion Effect Name}.png`
>

You are strongly recommended to put the dynamic effect resources on your own servers to avoid being affected by Mini LVB changes.

When the decompression is completed, you can enable the dynamic effect via the following API.

```objective-c
/**
 *  Select the dynamic effect
 *
 * @param tmplName: Dynamic effect name
 * @param tmplDir: The directory in which the dynamic effect locates
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```
### 2. AI background keying-out

Example:

![](https://mc.qcloudimg.com/static/img/0f79b78687753f88af7685530745a8d4/98B403B8-1DEC-4130-B691-D9EB5E321162.png)

The resources for AI background keying-out need to be downloaded, and the API is the same as that of dynamic effects.

```objective-c
/**
 * Select background keying-out
 *
 * @param tmplName: Dynamic effect name
 * @param tmplDir: The directory in which the dynamic effect locates
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```

### 3. Beautifying

```objective-c
/* setEyeScaleLevel  Set eye enlargement level. This parameter is valid only for value-added version.
 * Parameter:
 *          eyeScaleLevel     : Available value range for eye enlargement level: 0-9. 0 means disabling eye enlargement. A higher value means a stronger effect.
 */
-(void) setEyeScaleLevel:(float)eyeScaleLevel;

/* setFaceScaleLevel  Set face slimming level. This parameter is valid only for value-added version.
 * Parameter:
 *          faceScaleLevel    :Available value range for face slimming level: 0-9. 0 means disabling face slimming. A higher value means a stronger effect.
 */
-(void) setFaceScaleLevel:(float)faceScaleLevel;

/* setFaceVLevel  Set V-shaped face level. This parameter is valid only for value-added version.
 * Parameter:
 *          faceVLevel    : Available value range for V-shaped face level: 0-9. 0 means disabling V-shaped face. A higher value means a stronger effect.
 */
- (void) setFaceVLevel:(float)faceVLevel;

/* setChinLevel  Set chin stretching or contracting level. This parameter is valid only for value-added version.
 * Parameter:
 *          chinLevel    : Available value range for chin stretching or contracting level: -9-9. 0 means disabling chin stretching or contracting. -9 means stretching the chin to the maximum extent. 9 means contracting the chin to the maximum extent.
 */
- (void) setChinLevel:(float)chinLevel;

/* setFaceShortLevel  Set short face level. This parameter is valid only for value-added version.
 * Parameter:
 *          faceShortlevel    :Available value range for short face level: 0-9. 0 means disabling short face. A higher value means a stronger effect.
 */
- (void) setFaceShortLevel:(float)faceShortlevel;

/* setNoseSlimLevel  Set nose narrowing level. This parameter is valid only for value-added version.
 *  Parameter:
 *          noseSlimLevel    : Available value range for nose narrowing level: 0-9. 0 means disabling nose narrowing. A higher value means a stronger effect.
 */
- (void) setNoseSlimLevel:(float)noseSlimLevel;

```

### 4. Green screen

You need to prepare an mp4 file in advance and call the following API to enable the green screen effect.

```objective-c
/**
 * Set green screen file
 * 
 * @param file: Path to the green screen mp4 is supported. nil means disabling green screen.
 */
-(void)setGreenScreenFile:(NSURL *)file;
```
## Troubleshooting
### 1. Why does the project failed to be compiled?  
 > 1. Check whether dependent libraries AssetsLibrary.framwork, CoreMedia.framework, Accelerate.framework, and Metal.framework have been added.
                 
### 2. What should I do if crash occurs during project operation?  
 > 1. Check whether -ObjC is configured in the project.  
 > 2. Check whether Metal API Validation is set to Disabled.
     
### 3. Why don't the dynamic effects take effect?  
 > 1. Check if YTFaceSDK.licence is named correctly.  
 > 2. Check if the license expired (download [Query Tool](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) or contact our developers).  
 > 3. Check whether the Pitu resources are added correctly. Note that handdetect, handtrack, and res18_3M must be added as folder reference. The easiest way is to compare the dynamic effect files added in your project with those in our demo.  
 > 4. If you update the license, make sure to use the latest license. If you are not sure, check the validity period of the license (download [Query Tool](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) or contact our developers). If the license in the project is changed, clean the project and delete the local installation package for compilation.     
 
##### [Query Tool](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) is an xcode project, which is only supported on Mac. Other query methods will be available soon.

