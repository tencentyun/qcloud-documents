# Special Effects (Eye Enlarging, Face Slimming, Motion Effect, Green Screen, etc.)

## Feature Description

Eye enlarging, face slimming, motion effect sticker, green screen and other special effects are licensed features developed based on the face recognizing technology of YouTu Lab and the beautifying technology of Pitu. By working with YouTu Lab and Pitu, Tencent Cloud Mini Video integrates these special effect features into the image processing process of RTMP SDK to achieve better video effects.

## Integration Procedure

Application procedure:

1. Submit a ticket or call 400-9100-100 to contact the customer service.

2. Download the [sample form](https://mc.qcloudimg.com/static/archive/766c9092424d0440a31c56c81f34a629/archive.xlsx), fill in the information, and send it to jerryqian@tencent.com and copy it to your customer service contact (important).

3. Ask your customer service contact to confirm the e-mail by replying to it. Otherwise, the e-mail may be treated as a harassing e-mail.

4. As soon as the e-mail is confirmed, we will apply for a trial License from Youtu Lab and send the License along with the package decompression password to you.

   Two types of License:

   - Trial License: It is **valid for one month**, and used to debug and test the motion effects SDK. If your App is published with a trial License, the motion effects will not work normally after the License expires.
   - Official License: The validity period (usually one year) is subject to the contract.

## Version Download

Go to [SDK package](https://cloud.tencent.com/document/product/454/7873) page and download the commercial SDK package at the bottom of this page. The compressed SDK package is encrypted. You can obtain the decompression password & License file from the customer service. After the package is decompressed successfully, you will get `LiteAVSDK_Enterprise_3.9.2749.aar` and `LiteAVSDK_Enterprise_3.9.2749.zip` corresponding to two integration methods respectively.

## Project Configuration

For more information, please see [Project Configuration](https://cloud.tencent.com/document/product/584/11631). 

### Adding SDKs

#### Integration Using aar

Directly replace the non-commercial version of aar in your project with LiteAVSDK_Enterprise_3.9.2749.aar, and modify the corresponding name in build.gradle in the app directory. This method is very simple.

#### Integration Using jar Package

1. Decompress LiteAVSDK_Enterprise_3.9.2749.zip and copy the jar package and so files under libs to your jni load path. The jar package and so files related to motion effects are as follows:


| jar                     |                          |                   |
| ----------------------- | ------------------------ | ----------------- |
| filterengine.bundle.jar | ptu_algo_cb6bc16f389.jar | segmenter-lib.jar |
| video_module.jar        | YTCommon.jar             |                   |

| so                     |                           |                        |
| ---------------------- | ------------------------- | ---------------------- |
| libalgo_rithm_jni.so   | libalgo_youtu_jni.so      | libformat_convert.so   |
| libGestureDetectJni.so | libimage_filter_common.so | libimage_filter_gpu.so |
| libnnpack.so           | libParticleSystem.so      | libpitu_tools.so       |
| libsegmentern.so       | libsegmentero.so          | libYTCommon.so         |
| libYTFaceTrackPro.so   | libYTHandDetector.so      | libYTIllumination.so   |

2. Copy the resources from the decompressed assets folder to your project's assets directory, including the files in the asset root directory and files in the camera folder.

### Importing License File

The license of the commercial version needs to be verified to enable some of the features. You can contact your customer service contact to apply for a 30-day free license for debugging.
After you obtain a license, name the license as **YTFaceSDK.licence** and place it in the project's assets directory.

> Each license is bound with a specific package name. Modifying the package name of the App will result in verification failure.
>
> YTFaceSDK.Licence cannot be renamed or modified and must be placed in the assets directory.
>
> You do not need to apply for licenses for iOS and Android separately. One license can be used to authorize the bundleid in iOS and the packageName in Android simultaneously.

## Feature Calling

### 1. Motion Effect

Example:

![](https://mc.qcloudimg.com/static/img/a320624ee8d3a82ee07feb05969e5290/A8B81CB6-DBD3-4111-9BF0-90BD02779BFC.png)

A motion effect template is a directory, which contains a lot of resource files. The directory number and file size vary depending on the complexity of the motion effect.

The sample code in DEMO downloads the motion effect resources from the backend, and then the resources are decompressed to sdcard. You can find the download addresses of the motion effect resources in DEMO in the following format:

> ```
> http://dldir1.qq.com/hudongzhibo/AISpecial/Android/156/(Motion effectname).zip
> ```

You are strongly recommended to put the motion effect resources on your own servers to avoid being affected by DEMO changes.

When the decompression is completed, you can enable the motion effect via the following API.

```
/**
 * setMotionTmpl Set the location of motion effect image files
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### 2. AI Background Keying-out

Example:

![](https://mc.qcloudimg.com/static/img/0f79b78687753f88af7685530745a8d4/98B403B8-1DEC-4130-B691-D9EB5E321162.png)

The resources for AI background keying-out need to be downloaded, and the API is the same as that of motion effects.

```
/**
 * setMotionTmpl Set the location of motion effect image files
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### 3. Beautifying

```
// Eye enlarging (0-9)
mTXCameraRecord.setEyeScaleLevel(eyeScaleLevel);
// Face slimming (0-9)
mTXCameraRecord.setFaceScaleLevel(faceScaleLevel);
// V-shaped face (0-9)
mTXCameraRecord.setFaceVLevel(level)
// Chin stretching or contracting (0-9)
mTXCameraRecord.setChinLevel(scale)
// Face contracting (0-9)
mTXCameraRecord.setFaceShortLevel(level)
// Nose narrowing (0-9)
mTXCameraRecord.setNoseSlimLevel(scale)
```

### 4. Green Screen

You need to prepare an mp4 file in advance and call the following API to enable the green screen effect.

```
/**
 * Set the green screen file: The formats available in Android system are supported. That is, images in jpg/png and videos in mp4/3gp are supported.
 * API requires 18
 * @param path ：Location of green screen file. The following two methods are supported:
 *             1. Place the resource files in the assets directory, and use the file name as the path name.
 *             2. Use the absolute file path as the path name.
 */
@TargetApi(18)
public void setGreenScreenFile(String path);
```

## Troubleshooting              
### 1. What should I do if crash occurs during project operation?  
 > 1. Check whether abiFilters is set to armeabi in build.gradle (only armeabi is supported).
 > 2. If a jar package was used for integration, check whether all the so files related to motion effects are copied to the jniLibs directory of the project.
     
### 2. Why don't motion effects take effect?  
 > 1. Check if YTFaceSDK.licence is named correctly, and it must be placed in the assets root directory.  
 > 2. Check if the license expired (download [Query Tool](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) or contact our developers).    
 > 3. If a jar package is used for integration, check if the Pitu resources are added correctly (all contents in the assets directory under the decompressed SDK must be copied to the project's assets directory).  
 > 4. If you have updated the license, make sure to use the latest license. If you are not sure, check the validity period of the license (download [Query Tool](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) or contact our developers). If the license in the project is changed, clean the project, delete the local installation package, and then recompile.       
 
##### [Query Tool](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) is an xcode project, which is only supported on Mac. Other query methods will be available soon.

