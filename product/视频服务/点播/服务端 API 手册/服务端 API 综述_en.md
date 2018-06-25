## Overview of Server APIs
Tencent Cloud VOD provides a console interface and a complete set of HTTP-based server APIs to allow developers to use this service conveniently. With these APIs, developer's backend can interact with Tencent Cloud VOD backend using almost all of its features including video upload, media asset management and video processing. 

## Use of Server APIs
Tencent Cloud VOD server APIs are used in the same way as with Tencent [Cloud APIs][Cloud APIs]. To help users call these APIs, Tencent Cloud VOD provides developers with [Server API SDK][SDK].

### Request Structure
* [Request Structure Overview](https://cloud.tencent.com/document/api/213/6975)
* [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976)
* [API Request Parameters](https://cloud.tencent.com/document/api/213/6977)
* [Final Request Format](https://cloud.tencent.com/document/api/213/6978)

### Signature Method
* [Signature Method](https://cloud.tencent.com/document/api/213/6984)

### Returned Result
* [Result for Successful Requests](https://cloud.tencent.com/document/api/213/6980)
* [Result for Failed Requests](https://cloud.tencent.com/document/api/213/6981)
* [Common Error Codes][Common Error Codes]

### Error Codes for Tencent Cloud VOD Business
In addition to the [Cloud APIs][Cloud APIs] and [Common Error Codes][Common Error Codes] mentioned above, Tencent Cloud VOD business has its own specific error codes:

| Error Code | Description |
|---------|---------|
| -43001 | Query. Query command execution: Decoding failed; ffmpeg notification file is corrupted |
| -43029 | Query. Query command execution: Decoding failed; ffmpeg decoding failed |
| -43089 | Query. Query command execution: Meta information is missing; source video encoder/decoder unknown |
| -43090 | Query. Query command execution: Meta information is missing; source video/audio frame size unknown |
| -43091 | Query. Query command execution: Meta information is missing; source video/audio frame format unknown |
| -43092 | Query. Query command execution: Meta information is missing; source video/audio frame rate unknown |
| -43093 | Query. Query command execution: Meta information is missing; source video/audio channel number unknown |
| -43094 | Query. Query command execution: Meta information is missing; no decodable DTS frames |
| -43095 | Query. Query command execution: Meta information is missing; source video width/height unknown |
| -43096 | Query. Query command execution: Meta information is missing; source video color space unknown |
| -43097 | Query. Query command execution: Meta information is missing; no frame in rv30,40 and no sar |
| -43098 | Query. Query command execution: End of file |
| -43099 | Query. Query command execution: seeking outside actual filesize |
| -43101 | Query. Query command execution regarding the files to be stitched: Decoding failed; ffmpeg notification file is corrupted |
| -43129 | Query. Query command execution regarding the files to be stitched: Decoding failed; ffmpeg decoding failed |
| -43189 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video encoder/decoder unknown |
| -43190 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video/audio frame size unknown |
| -43191 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video/audio frame format unknown |
| -43192 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video/audio frame rate unknown |
| -43193 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video/audio channel number unknown |
| -43194 | Query. Query command execution regarding the files to be stitched: Meta information is missing; no decodable DTS frames |
| -43195 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video width/height unknown |
| -43196 | Query. Query command execution regarding the files to be stitched: Meta information is missing; source video color space unknown |
| -43197 | Query. Query command execution regarding the files to be stitched: Meta information is missing; no frame in rv30,40 and no sar |
| -43198 | Query. Query command execution regarding the files to be stitched: End of file |
| -43199 | Query. Query command execution regarding the files to be stitched: seeking outside actual filesize |
| -44001 | Screenshot. Screenshot command execution: Decoding failed; ffmpeg notification file is corrupted |
| -44029 | Screenshot. Screenshot command execution: Decoding failed; ffmpeg decoding failed |
| -44089 | Screenshot. Screenshot command execution: Meta information is missing; source video encoder/decoder unknown |
| -44090 | Screenshot. Screenshot command execution: Meta information is missing; source video/audio frame size unknown |
| -44091 | Screenshot. Screenshot command execution: Meta information is missing; source video/audio frame format unknown |
| -44092 | Screenshot. Screenshot command execution: Meta information is missing; source video/audio frame rate unknown |
| -44093 | Screenshot. Screenshot command execution: Meta information is missing; source video/audio channel number unknown |
| -44094 | Screenshot. Screenshot command execution: Meta information is missing; no decodable DTS frames |
| -44095 | Screenshot. Screenshot command execution: Meta information is missing; source video width/height unknown |
| -44096 | Screenshot. Screenshot command execution: Meta information is missing; source video color space unknown |
| -44097 | Screenshot. Screenshot command execution: Meta information is missing; no frame in rv30,40 and no sar |
| -44098 | Screenshot. Screenshot command execution: End of file |
| -44099 | Screenshot. Screenshot command execution: seeking outside actual filesize |
| -44101 | Screenshot. Execution of command regarding the acquiring of screenshot information: Decoding failed; ffmpeg notification file is corrupted |
| -44129 | Screenshot. Execution of command regarding the acquiring of screenshot information: Decoding failed; ffmpeg decoding failed |
| -44189 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video encoder/decoder unknown |
| -44190 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video/audio frame size unknown |
| -44191 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video/audio frame format unknown |
| -44192 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video/audio frame rate unknown |
| -44193 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video/audio channel number unknown |
| -44194 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; no decodable DTS frames |
| -44195 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video width/height unknown |
| -44196 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; source video color space unknown |
| -44197 | Screenshot. Execution of command regarding the acquiring of screenshot information: Meta information is missing; no frame in rv30,40 and no sar |
| -44198 | Screenshot. Execution of command regarding the acquiring of screenshot information: End of file |
| -44199 | Screenshot. Execution of command regarding the acquiring of screenshot information: seeking outside actual filesize |
| -45001 | Audio/video transcoding. Transcode command execution: Decoding failed; ffmpeg notification file is corrupted |
| -45029 | Audio/video transcoding. Transcode command execution: Decoding failed; ffmpeg decoding failed |
| -45089 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video encoder/decoder unknown |
| -45090 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video/audio frame size unknown |
| -45091 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video/audio frame format unknown |
| -45092 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video/audio frame rate unknown |
| -45093 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video/audio channel number unknown |
| -45094 | Audio/video transcoding. Transcode command execution: Meta information is missing; no decodable DTS frames |
| -45095 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video width/height unknown |
| -45096 | Audio/video transcoding. Transcode command execution: Meta information is missing; source video color space unknown |
| -45097 | Audio/video transcoding. Transcode command execution: Meta information is missing; no frame in rv30,40 and no sar |
| -45098 | Audio/video transcoding. Transcode command execution: End of file |
| -45099 | Audio/video transcoding. Transcode command execution: seeking outside actual filesize |
| -45101 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Decoding failed; ffmpeg notification file is corrupted |
| -45129 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Decoding failed; ffmpeg decoding failed |
| -45189 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video encoder/decoder unknown |
| -45190 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video/audio frame size unknown |
| -45191 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video/audio frame format unknown |
| -45192 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video/audio frame rate unknown |
| -45193 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video/audio channel number unknown |
| -45194 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; no decodable DTS frames |
| -45195 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video width/height unknown |
| -45196 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; source video color space unknown |
| -45197 | Audio/video transcoding. Acquire file information before verifying the transcoded file: Meta information is missing; no frame in rv30,40 and no sar |
| -45198 | Audio/video transcoding. Acquire file information before verifying the transcoded file: End of file |
| -45199 | Audio/video transcoding. Acquire file information before verifying the transcoded file: seeking outside actual filesize |
| -45201 | Audio/video transcoding. Acquire file information before uploading the file: Decoding failed; ffmpeg notification file is corrupted |
| -45229 | Audio/video transcoding. Acquire file information before uploading the file: Decoding failed; ffmpeg decoding failed |
| -45289 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video encoder/decoder unknown |
| -45290 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video/audio frame size unknown |
| -45291 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video/audio frame format unknown |
| -45292 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video/audio frame rate unknown |
| -45293 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video/audio channel number unknown |
| -45294 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; no decodable DTS frames |
| -45295 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video width/height unknown |
| -45296 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; source video color space unknown |
| -45297 | Audio/video transcoding. Acquire file information before uploading the file: Meta information is missing; no frame in rv30,40 and no sar |
| -45298 | Audio/video transcoding. Acquire file information before uploading the file: End of file |
| -45299 | Audio/video transcoding. Acquire file information before uploading the file: seeking outside actual filesize |
| -47100 | Source file does not meet the requirement; source file information format is not JSON |
| -47101 | Source file does not meet the requirement; source information does not contain width, height or color space |
| -47102 | Source file does not meet the requirement; unknown source information encoder |
| -47104 | Source file does not meet the requirement; duration of source information is invalid (<0.01 or >604800) |
| -47200 | Source file does not meet the requirement; file duration information is 0 |
| -47300 | Source file does not meet the requirement; maximum stitching limit is exceeded |
| -47301 | Source file does not meet the requirement; resolutions of stitched files are inconsistent |
| -47302 | Source file does not meet the requirement; failed to acquire source information of the video files to be stitched |
| -47400 | Source file does not meet the requirement; video file does not contain audio and video |
| -47401 | Source file does not meet the requirement; source file does not contain audio data (audio conversion task) |
| -47402 | Source file does not meet the requirement; source file does not contain video data (video conversion task) |
| -47403 | Source file does not meet the requirement; width/high/rotate/dar_w/dar_h of the video file are invalid |
| -49101 | Audio/video transcoding. Verification of the transcoded file: Decoding failed; ffmpeg notification file is corrupted |
| -49129 | Audio/video transcoding. Verification of the transcoded file: Decoding failed; ffmpeg decoding failed |
| -49189 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video encoder/decoder unknown |
| -49190 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video/audio frame size unknown |
| -49191 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video/audio frame format unknown |
| -49192 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video/audio frame rate unknown |
| -49193 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video/audio channel number unknown |
| -49194 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; no decodable DTS frames |
| -49195 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video width/height unknown |
| -49196 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; source video color space unknown |
| -49197 | Audio/video transcoding. Verification of the transcoded file: Meta information is missing; no frame in rv30,40 and no sar |
| -49198 | Audio/video transcoding. Verification of the transcoded file: End of file |
| -49199 | Audio/video transcoding. Verification of the transcoded file: seeking outside actual filesize |

[Cloud APIs]: https://cloud.tencent.com/product/api "Cloud APIs"
[Common Error Codes]: https://cloud.tencent.com/document/api/213/10146 "Common Error Codes"
[SDK]: https://cloud.tencent.com/document/developer-resource "SDK"


