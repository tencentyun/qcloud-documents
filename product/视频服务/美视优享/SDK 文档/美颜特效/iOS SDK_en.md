## Feature Description
Eye enlarging, face slimming, motion effect sticker, green screen and other special effects are licensed features developed based on the face recognizing technology of YouTu Lab and the beautifying technology of Pitu. By working with YouTu Lab and Pitu, Mini LVB of Tencent Cloud integrates these special effect features into the image processing process of RTMP SDK to achieve better video effects.

## Version Download
You can download the SDK zip file (VIP version) at the bottom of the [RTMP SDK](/doc/product/454/7873). The zip file is encrypted, and you can contact your business representative to obtain the password and the license file. After the zip file is decompressed, you will get a `txrtmpsdk.jar`, a `libtxrtmpsdk.so`, and other .so files. Replace the .jar files and .so files of non-VIP version in your project with the decompressed .so files.

> **Note:**
> You can distinguish the VIP version and non-VIP version by viewing the SDK's bundler id.
> - The bundler id of the non-VIP version is com.tencent.TXRTMPSDK.
> - The bundler id of the VIP version is com.tencent.TXRTMPSDK.pitu.

## Xcode Project Settings

### 1. Add Frameworks

The VIP version requires linking with additional system frameworks:
> AssetsLibrary.framwork
> CoreMedia.framework
> Accelerate.framework

### 2. Add Link Parameters

Under Build Setting -> Other Link Flags, add the `-ObjC` option.

### 3. Add Resource Bundles

Add the following files in the zip file to the project:

> FilterEngine.bundle
> PE.dat
> ufa.bundle
> youtubeauty.bundle

### 4. Add Motion Effect Resources

Add the Resource directory in the zip file to the project as a folder reference. You must add these resources. Otherwise, a crash occurs when the material is switched to the face-transforming type.
![](https://mc.qcloudimg.com/static/img/b7fac6b5e08b0ff245b17d29f7296b18/AAE85661-7601-4473-A338-747FB9A6981C.png)

### 5. Import the License File
The license of the VIP version needs to be verified to enable some of the functions. You can contact your business representative to apply for a 30-day free trial license.
After you obtain a license, name the license as **YTFaceSDK.licence** and add it to the project's assets directory.

> **Notes:**
> - Each license is bound with a specific package name. Modifying the package name of the app will result in verification failure.
> - YTFaceSDK.license cannot be renamed and must be placed in the assets directory.
> - iOS and Android do not need to apply for licenses separately. One license can be used to authorize the bundleid in iOS and the packageName in Android simultaneously.

## Function Calling

### Motion Effect Sticker

A motion effect template is a directory, which contains a lot of resource files. The directory number and file size vary depending on the complexity of the motion effect.
The sample code in the Mini LVB downloads the motion effect resources from the backend, and then the resources are decompressed to the Resource directory. You can find the download addresses of the motion effect resources and thumbnails in the Mini LVB code in the following format:
> `https://st1.xiangji.qq.com/yunmaterials/{Motion Effect Name}.zip`
> `https://st1.xiangji.qq.com/yunmaterials/{Motion Effect Name}.png`
>


You are strongly recommended to put the motion effect resources on your own servers to avoid being affected by Mini LVB changes.
When the decompression is complete, you can enable the motion effect via the following API.

```objective-c
/**
 * Select the motion effect
 *
 * @param tmplName: Motion effect name
 * @param tmplDir: The directory in which the motion effect locates
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```


### Green Screen Function

You need to prepare an mp4 file in advance and call the following API to enable the green screen effect:

```objective-c
/**
 * Set the green screen file
 * 
 * @param file: The path of the green screen file. mp4 is supported. nil means to disable the green screen
 */
-(void)setGreenScreenFile:(NSURL *)file;
```

### Eye Enlarging and Face Slimming

You can set the eye enlarging and face slimming functions in the following ways:

```objective-c
/**
 * Set the eye enlarging level
 * 
 *  @param eyeScaleLevel: Available value range for eye enlarging level: 0-9. 0 means to disable the eye enlarging, while a higher value means a stronger effect.
 */
-(void)setEyeScaleLevel:(float)eyeScaleLevel;

/**
 * Set the face slimming level
 *
 *  @param faceScaleLevel: Available value range for face slimming level: 0-9. 0 means to disable the face slimming, while a higher value means a stronger effect.
 */
-(void)setFaceScaleLevel:(float)faceScaleLevel;
```
