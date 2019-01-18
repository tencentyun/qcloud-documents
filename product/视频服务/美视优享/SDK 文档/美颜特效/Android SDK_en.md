## Feature Description
Eye enlarging, face slimming, motion effect sticker, green screen and other special effects are licensed features developed based on the face recognizing technology of YouTu Lab and the beautifying technology of Pitu. By working with YouTu Lab and Pitu, Mini LVB of Tencent Cloud integrates these special effect features into the image processing process of RTMP SDK to achieve better video effects.

## Version Download
You can download the SDK zip file (VIP version) at the bottom of the [RTMP SDK](/doc/product/454/7873). The zip file is encrypted, and you can contact your business representative to obtain the password and the license file. After the zip file is decompressed, you will get a `txrtmpsdk.jar`, a `libtxrtmpsdk.so`, and other .so files. Replace the .jar files and .so files of non-VIP version in your project with the decompressed .so files.

## Project Settings

### 1. Add SDKs
Copy the `txrtmpsdk.jar` and` libtxrtmpsdk.so` in the SDK to the corresponding location of the project, such as libs.
> **Note:**
> The VIP version only supports the armeabi architecture .so files. Delete .so files of other architectures in the app to prevent load failure of .so files.

### 2. Add Resources
Copy the `camera` folder in the zip file to the assets directory of the project.
> **Note:**
> The camera directory contains the resources to switch motion effects, so it must be properly placed into the assets directory. Otherwise, an error occurs.

### 3. Import the License File
The license of the VIP version needs to be verified to enable some of the functions. You can contact your business representative to apply for a 30-day free trial license. After you obtain a license, name the license as **YTFaceSDK.licence** and add it to the project's assets directory.

> **Notes:**
> - Each license is bound with a specific package name. Modifying the package name of the app will result in verification failure.
> - YTFaceSDK.license cannot be renamed and must be placed in the assets directory.
> - iOS and Android do not need to apply for licenses separately. One license can be used to authorize the bundleid in iOS and the packageName in Android simultaneously.

## Function Calling

### Motion Effect

A motion effect template is a directory, which contains a lot of resource files. The directory number and file size vary depending on the complexity of the motion effect.
The sample code in the Mini LVB downloads the motion effect resources from the backend, and then the resources are decompressed to the Resource directory. You can find the download addresses of the motion effect resources and thumbnails in the Mini LVB code in the following format:

> `https://st1.xiangji.qq.com/yunmaterials/{Motion Effect ID}Android.zip`
> `https://st1.xiangji.qq.com/yunmaterials/{Motion Effect ID}.png`
>

You are strongly recommended to put the motion effect resources on your own servers to avoid being affected by Mini LVB changes.
When the decompression is complete, you can enable the motion effect via the following API:

```java
/**
 * setMotionTmpl Set the location of the motion effect image files
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```


### Green Screen Function

You need to prepare an mp4 file in advance and call the following API to enable the green screen effect:

```java
/**
 * Set the green screen file: Currently, the formats available in Android system are supported. That is, images in jpg/png and videos in mp4/3gp are supported.
 * API requires 18
 * @param path: The location of the green screen file. The following two modes are supported:
 *             1. Place the resource files in the assets directory, and use the file name as the path name
 *             2. Use the absolute path of the file as the path
 */
@TargetApi(18)
public void setGreenScreenFile(String path);
```


### Eye Enlarging and Face Slimming

The eye enlarging and face slimming functions in SDK 2.0.0 are under development and will be available soon.

