# Special Effects (Eye Enlarging, Face Slimming, Dynamic Effect and Green Screen)

## Feature Description
Special effects such as eye enlarging, face slimming, dynamic sticker and green screen, are privileged features developed based on face recognition technology of Tencent YouTu Lab team and makeup technology of Tencent Pitu team. By cooperating with the two teams, Tencent Cloud's Mini LVB team deeply integrates these special effects into the image processing process of RTMP SDK to achieve better video effects.

## Charges
The special effects use patented technology of Tencent YouTu Lab, with annual licensing fees being about **0.5 million CNY**(currently, the fees of similar image processing products in China are millions of CNY). If you need the feature, submit a ticket or call our customer service at 400-9100-100. Staff of the business department will provide a password for decoding the SDK package and apply to Tencent YouTu Lab for a trial license for you.

## Version Downloading
You can download the privileged SDK package at the bottom of the [RTMP SDK](https://cloud.tencent.com/document/product/454/7873) page. The package is encrypted and you can get the password and the license file from our staff of the business department. After decompressing the package, you can replace the non-privileged jar and so files of your project with the decompressed `txrtmpsdk.jar`,` libtxrtmpsdk.so` and other so files.

> To distinguish the privileged and non-privileged versions, you can view the bundler id of the SDK. bundler id being com.tencent.TXRTMPSDK means the non-privileged version and being com.tencent.TXRTMPSDK.pitu, the privileged version.
>
> You can also judge from the SDK size, with the privileged version is much larger than the non-privileged.



## Xcode Project Settings

### 1. Add the framework

The privileged version need to be linked to some additional system frameworks
> 1. AssetsLibrary.framwork
> 2. CoreMedia.framework
> 3. Accelerate.framework

### 2. Add link parameters

In "Build Setting" -> "Other Link Flags" of the project, add the `-ObjC` option.

### 3. Add resource bundles

Add the following files in the zip package to the project

> 1. FilterEngine.bundle
> 2. PE.dat
> 3. ufa.bundle
> 4. youtubeauty.bundle

### 4. Add resources for dynamic effects

Add the Resource directory in the zip package to the project as folder refrence.

![](https://mc.qcloudimg.com/static/img/b7fac6b5e08b0ff245b17d29f7296b18/AAE85661-7601-4473-A338-747FB9A6981C.png)

These resources are very important. The loss or damage of them can cause crash when you switch to face changing materials.

### 3. Import the license file
The features of the privileged version take effect only after the license verification is successful. You can apply to our staff of the business department for a 30-day free license for debugging.
After getting the license, you need to name it **YTFaceSDK.licence** and place it under the assets directory in the project.

> Each license is bound to a specific package name. Therefore, modifying the package name in the App can cause verification failure.
>
> The name of YTFaceSDK.license file is fixed, can not be modified, and must be placed under the assets directory.
> 
> For iOS and Android systems, you need to apply for only one license because one license can authorize the bundleid of an iOS system and the packageName of an Android system at the same time.

## Feature Calling

### 1. Dynamic stickers

One dynamic effect template is included in one directory, which contains many resource files. Depending on the complexity of each dynamic effect, the number of directories and file sizes are different.

Download resources for dynamic effects from the background and decompress them to the Resource directory, and then you can get sample codes in the Mini LVB. In the codes, you can find download addresses of resources and thumbnails for dynamic effects. The format is as follows

> `https://st1.xiangji.qq.com/yunmaterials/{Name of the dynamic effect}.zip`
>
> `https://st1.xiangji.qq.com/yunmaterials/Name of the dynamic effect}.png`
>

It is strongly recommended that you put the resources for dynamic effects on your own servers to prevent unnecessary impact caused by modifications of the Mini LVB.

After decompression, you can enable dynamic effects through the following API

```objective-c
/**
 * select dynamic effect
 *
 * @param tmplName:  Name of the dynamic effect
 * @param tmplDir:  Directory where the dynamic effect is located
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```


### 2. Green screen

Prepare a mp4 file for playback, and then you can enable the green screen effect by calling the following API

```objective-c
/**
 * Set the green screen file
 * 
 * @param file:  Green screen file path. Supported files are in mp4 format. nil means disabling the green screen
 */
-(void)setGreenScreenFile:(NSURL *)file;
```

### 3. Eye enlarging and face slimming

Eye enlarging and face slimming are set in the following ways

```objective-c
/**
 * Set the eye enlarging level
 * 
 *  @param eyeScaleLevel:  Range of eye enlarging level: 0-9. 0 means disabling the feature. For 1-9, the larger value brings more obvious effect.
 */
-(void)setEyeScaleLevel:(float)eyeScaleLevel;

/**
 * Set the face slimming level
 *
 *  @param faceScaleLevel:  Range of face slimming level: 0-9. 0 means disabling the feature. For 1-9, the larger value brings more obvious effect.
 */
-(void)setFaceScaleLevel:(float)faceScaleLevel;
```


