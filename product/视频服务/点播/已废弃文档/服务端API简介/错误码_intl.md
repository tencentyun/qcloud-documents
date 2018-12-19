## VOD Error Code Description
The error code included in the response body displays an overview of the results for the calling and execution operations of Tencent Cloud APIs. An error code other than 0 indicates that the request is not properly executed. The error message describes the error in details. Users can determine API execution result based on the error code. On some terminals, such as browsers, message in Chinese is displayed in Unicode and needs to be decoded.

Apart from common error codes, each API may have special error codes. Refer to the documentation of each API for details.

| Error Code | Error Type | Description |
|---------|---------|---------|
| 4000 | Invalid request parameter | Mandatory parameters are missing, or the format of parameter values is incorrect. For details on the error message, please refer to the message field in the error description.  |
| 4100 | Authentication failed | Signature authentication failed. Please refer to the Authentication section in the document.  |
| 4200 | Request expired | Request has expired. Please refer to the Request Validity section in the document.  |
| 4300 | Access denied | The account is suspended or is not within the user range for the API.  |
| 4400 |Quota exceeded | The number of requests has exceeded the quota limit. Please refer to the Request Quota section in the document.  |
| 4500 | Replay attack | The Nonce and Timestamp parameters of request can ensure that each request is executed only once on the server. Therefore, the Nonce should not be identical to the previous one. The time difference between the Timestamp and Tencent CVM should not be greater than 2 hours.  |
| 4600 | Unsupported protocol | Protocol is not supported. Please refer to the document.  |
| 5000 | Resource does not exist | The instance that the resource ID indicates does not exist, or the instance has been returned, or another user's resource is accessed.  |
| 5100 | Resource operation failed | The operation performed on the resource failed. For specific error message, see the message field in the error description. Try again later or contact customer service personnel for help.  |
| 5200 | Failed to purchase resource | Failed to purchase resource. This may be caused by unsupported instance configuration, or insufficient resources.  |
| 5300 | Failed to purchase resource | Failed to purchase resource because of insufficient balance.  |
| 5400 | Part of operations performed successfully | Part of batch operations have been performed successfully. For details, see the returned value of the method.  |
| 5500 | User failed to pass qualification verification | Failed to purchase resource, because user failed to pass the qualification verification.  |
| 6000 | Internal error on the server | An internal error occurred on the server. Try again later or contact customer service personnel for help.  |
| 6100 | Version is currently not supported | This API is not supported in this version or the API is under maintenance. Note:  When this error occurs, first check whether the domain name of the API is correct. Different modules may have different domain names.  |
| 6200 | API is temporarily unavailable | The API is being maintained. Please try again later.  |


## Error Code Description Regarding Video Processing Operations
The error codes of video processing operations (such as transcoding, taking screenshots and stitching) are as follows:

| Error Code | Description |
|---------|---------|
| -43001 | Query, query command execution:  Decoding failed, ffmpeg notification file is corrupted |
| -43029 | Query, query command execution:  Decoding failed, ffmpeg decoding failed |
| -43089 | Query, query command execution:  Metainformation is missing, source video encoder/decoder unknown |
| -43090 | Query, query command execution:  Metainformation is missing, source video audio frame size unknown |
| -43091 | Query, query command execution:  Metainformation is missing, source video audio frame format unknown |
| -43092 | Query, query command execution:  Metainformation is missing, source video audio frame rate unknown |
| -43093 | Query, query command execution:  Metainformation is missing, source video audio channel number unknown |
| -43094 | Query, query command execution:  Metainformation is missing, no decodable DTS frames |
| -43095 | Query, query command execution:  Metainformation is missing, source video width/height unknown |
| -43096 | Query, query command execution:  Metainformation is missing, source video color space unknown |
| -43097 | Query, query command execution:  Metainformation is missing, no frame in rv30,40 and no sar |
| -43098 | Query, query command execution:  End of file |
| -43099 | Query, query command execution:  seeking outside actual filesize |
| -43101 | Query, execution of command regarding the query of files to be stitched:  Decoding failed, ffmpeg notification file is corrupted |
| -43129 | Query, execution of command regarding the query of files to be stitched:  Decoding failed, ffmpeg decoding failed |
| -43189 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video encoder/decoder unknown |
| -43190 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video audio frame size unknown |
| -43191 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video audio frame format unknown |
| -43192 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video audio frame rate unknown |
| -43193 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video audio channel number unknown |
| -43194 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, no decodable DTS frames |
| -43195 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video width/height unknown |
| -43196 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, source video color space unknown |
| -43197 | Query, execution of command regarding the query of files to be stitched:  Metainformation is missing, no frame in rv30,40 and no sar |
| -43198 | Query, execution of command regarding the query of files to be stitched:  End of file |
| -43199 | Query, execution of command regarding the query of files to be stitched:  seeking outside actual filesize |
| -44001 | Screenshot, screenshot command execution:  Decoding failed, ffmpeg notification file is corrupted |
| -44029 | Screenshot, screenshot command execution:  Decoding failed, ffmpeg decoding failed |
| -44089 | Screenshot, screenshot command execution:  Metainformation is missing, source video encoder/decoder unknown |
| -44090 | Screenshot, screenshot command execution:  Metainformation is missing, source video audio frame size unknown |
| -44091 | Screenshot, screenshot command execution:  Metainformation is missing, source video audio frame format unknown |
| -44092 | Screenshot, screenshot command execution:  Metainformation is missing, source video audio frame rate unknown |
| -44093 | Screenshot, screenshot command execution:  Metainformation is missing, source video audio channel number unknown |
| -44094 | Screenshot, screenshot command execution:  Metainformation is missing, no decodable DTS frames |
| -44095 | Screenshot, screenshot command execution:  Metainformation is missing, source video width/height unknown |
| -44096 | Screenshot, screenshot command execution:  Metainformation is missing, source video color space unknown |
| -44097 | Screenshot, screenshot command execution:  Metainformation is missing, no frame in rv30,40 and no sar |
| -44098 | Screenshot, screenshot command execution:  End of file |
| -44099 | Screenshot, screenshot command execution:  seeking outside actual filesize |
| -44101 | Screenshot, execution of command regarding the acquiring of screenshot information:  Decoding failed, ffmpeg notification file is corrupted |
| -44129 | Screenshot, execution of command regarding the acquiring of screenshot information:  Decoding failed, ffmpeg decoding failed |
| -44189 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video encoder/decoder unknown |
| -44190 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video audio frame size unknown |
| -44191 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video audio frame format unknown |
| -44192 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video audio frame rate unknown |
| -44193 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video audio channel number unknown |
| -44194 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, no decodable DTS frames |
| -44195 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video width/height unknown |
| -44196 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, source video color space unknown |
| -44197 | Screenshot, execution of command regarding the acquiring of screenshot information:  Metainformation is missing, no frame in rv30,40 and no sar |
| -44198 | Screenshot, execution of command regarding the acquiring of screenshot information:  End of file |
| -44199 | Screenshot, execution of command regarding the acquiring of screenshot information:  seeking outside actual filesize |
| -45001 | Audio/video transcoding, transcode command execution:  Decoding failed, ffmpeg notification file is corrupted |
| -45029 | Audio/video transcoding, transcode command execution:  Decoding failed, ffmpeg decoding failed |
| -45089 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video encoder/decoder unknown |
| -45090 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video audio frame size unknown |
| -45091 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video audio frame format unknown |
| -45092 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video audio frame rate unknown |
| -45093 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video audio channel number unknown |
| -45094 | Audio/video transcoding, transcode command execution:  Metainformation is missing, no decodable DTS frames |
| -45095 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video width/height unknown |
| -45096 | Audio/video transcoding, transcode command execution:  Metainformation is missing, source video color space unknown |
| -45097 | Audio/video transcoding, transcode command execution:  Metainformation is missing, no frame in rv30,40 and no sar |
| -45098 | Audio/video transcoding, transcode command execution:  End of file |
| -45099 | Audio/video transcoding, transcode command execution:  seeking outside actual filesize |
| -45101 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Decoding failed, ffmpeg notification file is corrupted |
| -45129 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Decoding failed, ffmpeg decoding failed |
| -45189 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video encoder/decoder unknown |
| -45190 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video audio frame size unknown |
| -45191 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video audio frame format unknown |
| -45192 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video audio frame rate unknown |
| -45193 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video audio channel number unknown |
| -45194 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, no decodable DTS frames |
| -45195 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video width/height unknown |
| -45196 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, source video color space unknown |
| -45197 | Audio/video transcoding, acquire file information before verifying the transcoded file:  Metainformation is missing, no frame in rv30,40 and no sar |
| -45198 | Audio/video transcoding, acquire file information before verifying the transcoded file:  End of file |
| -45199 | Audio/video transcoding, acquire file information before verifying the transcoded file:  seeking outside actual filesize |
| -45201 | Audio/video transcoding, acquire file information before uploading the file:  Decoding failed, ffmpeg notification file is corrupted |
| -45229 | Audio/video transcoding, acquire file information before uploading the file:  Decoding failed, ffmpeg decoding failed |
| -45289 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video encoder/decoder unknown |
| -45290 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video audio frame size unknown |
| -45291 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video audio frame format unknown |
| -45292 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video audio frame rate unknown |
| -45293 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video audio channel number unknown |
| -45294 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, no decodable DTS frames |
| -45295 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video width/height unknown |
| -45296 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, source video color space unknown |
| -45297 | Audio/video transcoding, acquire file information before uploading the file:  Metainformation is missing, no frame in rv30,40 and no sar |
| -45298 | Audio/video transcoding, acquire file information before uploading the file:  End of file |
| -45299 | Audio/video transcoding, acquire file information before uploading the file:  seeking outside actual filesize |
| -47100 | Source file does not meet requirement, source file information format is not json |
| -47101 | Source file does not meet requirement, source information does not contain width, height or color space |
| -47102 | Source file does not meet requirement, unknown source information encoder |
| -47104 | Source file does not meet requirement, duration of source information is invalid (<0.01 or >604800) |
| -47200 | Source file does not meet requirement, file duration information is 0 |
| -47300 | Source file does not meet requirement, maximum stitching limit exceeded |
| -47301 | Source file does not meet requirement, resolutions of stitched files are inconsistent |
| -47302 | Source file does not meet requirement, failed to acquire source information of the video files to be stitched |
| -47400 | Source file does not meet requirement, video file does not contain audio and video |
| -47401 | Source file does not meet requirement, source file does not contain audio data (audio conversion task) |
| -47402 | Source file does not meet requirement, source file does not contain video data (video conversion task) |
| -47403 | Source file does not meet requirement, width/high/rotate/dar_w/dar_h of the video file are invalid |
| -49101 | Audio/video transcoding, verification of the transcoded file:  Decoding failed, ffmpeg notification file is corrupted |
| -49129 | Audio/video transcoding, verification of the transcoded file:  Decoding failed, ffmpeg decoding failed |
| -49189 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video encoder/decoder unknown |
| -49190 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video audio frame size unknown |
| -49191 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video audio frame format unknown |
| -49192 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video audio frame rate unknown |
| -49193 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video audio channel number unknown |
| -49194 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, no decodable DTS frames |
| -49195 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video width/height unknown |
| -49196 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, source video color space unknown |
| -49197 | Audio/video transcoding, verification of the transcoded file:  Metainformation is missing, no frame in rv30,40 and no sar |
| -49198 | Audio/video transcoding, verification of the transcoded file:  End of file |
| -49199 | Audio/video transcoding, verification of the transcoded file:  seeking outside actual filesize |
