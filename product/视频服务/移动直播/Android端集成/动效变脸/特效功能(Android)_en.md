# Special Effects (Eye Enlarging, Face Slimming, Dynamic Effect and Green Screen)

## Feature Description
Special effects such as eye enlarging, face slimming, dynamic sticker and green screen, are privileged features developed based on face recognition technology of Tencent YouTu Lab team and makeup technology of Tencent Pitu team. By cooperating with the two teams, Tencent Cloud's Mini LVB team deeply integrates these special effects into the image processing process of RTMP SDK to achieve better video effects.

## Charges
The special effects use patented technology of Tencent YouTu Lab, with annual licensing fees being about **0.5 million CNY**(currently, the fees of similar image processing products in China are millions of CNY). If you need the feature, submit a ticket or call our customer service at 400-9100-100. Staff of the business department will provide a password for decoding the SDK package and apply to Tencent YouTu Lab for a trial license for you.

## Version Downloading
You can download the privileged SDK package at the bottom of the [RTMP SDK](https://cloud.tencent.com/document/product/454/7873) page. The package is encrypted and you can get the password and the license file from our staff of the business department. After decompressing the package, you need to replace the non-privileged jar and so files in your project with the decompressed `txrtmpsdk.jar`,` libtxrtmpsdk.so` and other so files.

## Project Settings

### 1. Add the SDK
Copy txrtmpsdk.jar, libtxrtmpsdk.so and other so files in the SDK to the corresponding location in the project, such as in the libs folder
> Note: Privileged version only supports so files with armeabi architecture. Therefore, you should delete so files with other architectures in the App to avoid loading failure of so files.

### 2. Add resources
Copy the `camera` folder in the zip package to the assets directory of the project
> Note: The camera directory includes files such as resources for switching dynamic effects, and must be placed correctly under the assets directory, otherwise an error will occur

### 3. Import the license file
The features of the privileged version take effect only after the license verification is successful. You can apply to our staff of the business department for a 30-day free license for debugging.
After getting the license, you need to name it **YTFaceSDK.licence** and place it under the assets directory in the project.

> Each license is bound to a specific package name. Therefore, modifying the package name in the App can cause verification failure.
>
> The name of YTFaceSDK.license file is fixed, cannot be modified, and must be placed under the assets directory.
> 
> For IOS and Android systems, you need to apply for only one license because one license can authorize the bundleid of an iOS system and the packageName of an Android system at the same time.

## Feature Calling

### 1. Dynamic effects

One dynamic effect template is included in one directory, which contains many resource files. Depending on the complexity of each dynamic effect, the number of directories and file sizes are different.

Download resources for dynamic effects from the background and decompress them to the Resource directory, and then you can get sample codes in the Mini LVB. In the codes, you can find download addresses of resources and thumbnails for dynamic effects. The format is as follows

> `https://st1.xiangji.qq.com/yunmaterials/{ID of the dynamic effect}Android.zip`
>
> `https://st1.xiangji.qq.com/yunmaterials/{ID of the dynamic effect}.png`
>

It is strongly recommended that you put the resources for dynamic effects on your own servers to prevent unnecessary impact caused by modifications of the Mini LVB.

After decompression, you can enable dynamic effects through the following API

```java
/**
 * setMotionTmpl is used to set the location of dynamic sticker files
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```


### 2. Green screen

Prepare a mp4 file for playback, and then you can enable the green screen effect by calling the following API

```java
/**
 * Set the green screen file: Currently, the supported pictures are in jpg/png format, and the supported videos are in mp4, 3gp and other Android-supported format
 * API requirement 18
 * @param path : Location of the green screen file. It supports two ways:
 *             1. The resource file is put under the assets directory, and path is the file name
 *             2. path is the absolute path of the file 
 */
@TargetApi(18)
public void setGreenScreenFile(String path);
```


### 3. Eye enlarging and face slimming

> Eye enlarging and face slimming features for SDK 2.0.0 are still under tense development and will be released as soon as possible.



