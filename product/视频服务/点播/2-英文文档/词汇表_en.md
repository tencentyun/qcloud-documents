## Container Format (Format)

Container format refers to that the encoded and compressed video stream and audio stream are put into one file according to a certain format specification. For network VOD, the more appropriate term is "Streaming Network Transport Protocol". The most widely used protocols in the Internet are as follows:

- **MP4**: One of the most classic file formats, which is well supported on iOS/Android/PC. However, the header of MP4 video files is large, and the file structure is complex. If the duration of a video is relatively long (for example, a few hours), the file header is too large, which may affect the video loading speed. So, it is more suitable for short video scenarios. For more information, please see [Wikipedia: MP4](https://zh.wikipedia.org/wiki/MP4).
- **HLS (HTTP Live Streaming)**: The standard format launched by Apple Inc. HLS is well supported on iOS/Android. But on IE, the support for HLS depends on the secondary development of FLASH (Tencent Video Cloud's FLASH player control is recommended). Unlike MP4, HLS's compact m3u8 index structure allows a fast indexing, which makes it a good choice for VOD. For more information, please see [HTTP Live Streaming](https://developer.apple.com/streaming/) and [Wikepedia: HTTP Live Streaming](https://zh.wikipedia.org/wiki/HTTP_Live_Streaming).
- **FLV**: As a format launched by Adobe Systems, it's well supported by FLASH on PCs. However, on mobile devices, FLV is only supported by apps which implement its player (Tencent Video Cloud's FLASH player control is recommended). Most mobile browsers don't support FLV. For more information, please see [Wikepedia: Flash Video](https://zh.wikipedia.org/wiki/Flash_Video).

## Video Encoding Parameters

### Codec
A program or a device that can compress or decompress (video decoding) digital videos. Common codecs include:

- H.26X series is led by the ITU (International Telecommunication Union). Among the standards of this series, H.264 is now the most widely used one, with H.265 as its successor. Under the same image quality, the compression rate of H.265 can be double that of H.264. However, H.265 is not yet in widespread use because of the patent and other factors. For more information, please see [Wikipedia: H.264](https://zh.wikipedia.org/wiki/H.264/MPEG-4_AVC) and [Wikipedia: H.265](https://zh.wikipedia.org/wiki/%E9%AB%98%E6%95%88%E7%8E%87%E8%A7%86%E9%A2%91%E7%BC%96%E7%A0%81).
- MPEG series is dominated by the MPEG (Moving Picture Experts Group) of ISO (International Organization for Standardization).
- Other series, such as the Google-led VP8, VP9, and the Real-led RealVideo and so on.

### Bitrate
The number of bits required to play continuous media (such as compressed audios or videos) per unit time. Bitrate is measured in bits per second (bit/s or bps). For more information, please see [Wikipedia: Bitrate](https://zh.wikipedia.org/wiki/%E6%AF%94%E7%89%B9%E7%8E%87).

### Frame Rate
TThe unit of measurement for the number of video frames displayed per unit time. Unit of frame rate can be frame per second (FPS) or Hz. For more information, please see [Wikipedia: Frame Rate](https://zh.wikipedia.org/wiki/%E5%B8%A7%E7%8E%87).

### Resolution
It is used to describe the video's capability of resolving details, generally expressed as the number of distinct pixels in each dimension, such as 640x480. For more information, please see [Wikipedia: Resolution](https://zh.wikipedia.org/wiki/%E5%88%86%E8%BE%A8%E7%8E%87).

### GOP (Group of Pictures)
A group of consecutive pictures encoded with MPEG within a movie or a video stream. It begins with an I frame and ends with the next I frame. A GOP contains the following image types:

- I-Frame (Intra Coded Picture): The node-encoded picture. It is a fixed image independent of other image types. Each GOP begins with this type of image.
- P-Frame (Predictive Coded Picture): The predictive coded picture. It contains the difference information from the previous I frame or P frame.
- B-Frame (Bidirectionally Predictive Coded Pictures): The predictive coded picture before and after. It contains the difference information from the previous and/or the latter I or P frame.

The number of frames in a GOP is called the GOP length.

### Profile
Profile is a collection of specific encoding features for a specific application scenario. H.264 provides three main grades:

- Baseline: It supports I/P frame, and only supports Progressive and CAVLC. It is generally used in low-grade apps or apps that need extra fault tolerance, such as video chat and mobile video, and other instant messaging apps.
- Main: It provides I/P/B frame, and supports Progressive and Interlaced, as well as CAVLC and CABAC. It is used for the mainstream consumer electronics specifications, such as MP4 with low decoding rate (relatively), portable video player, PSP and iPod.
- High: 8x8 internal prediction, custom quantification, lossless video encoding and more YUV formats (eg 4:4:4) are added on the basis of Main for broadcast and video disc storage (Blu-ray movies), and the application of HDTV.

### Color Space
 A color space is an abstract mathematical model describing the way colors can be represented as tuples of numbers (e.g. triples in RGB or quadruples in CMYK). For more information, please see [Wikipedia: Color Space](https://zh.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%96%93).

## Video Processing Parameters

### Video Denoising
Video noises are the random brightness or color changes in images generated by sensors, scanner circuits or digital cameras. Video noises also come from spot noises in film grains and constant quantum detectors. video noises are often seen as an unwanted component in image acquisition. Video denoising is a process of removing unwanted noises and reserving more important details in videos. For more information, please see [Wikipedia: Video Denoising](https://zh.wikipedia.org/wiki/%E5%BD%B1%E5%83%8F%E9%99%8D%E5%99%AA).

### Deinterlacing
In the era of analogue television, both processing speed and network bandwidth of playback devices are restricted. To reduce the transmission bitrate without lowering the frame rate, the interlacing technology has been developed. This technology can be used to reduce by half the video transmission bandwidth in case of slight decrease in image quality. However, the negative impact of interlacing can not be ignored, such as lower resolution, prone to flickering, or jagged edges in videos. Now, both video playback devices and network bandwidth have been rapidly developed, therefore, interlacing has been phased out step by step. Some new devices no longer supports interlacing. As a result, deinterlacing are required for some historical videos that have used the interlacing technology. For more information please see [Wikipedia: Interlacing](https://zh.wikipedia.org/wiki/%E9%9A%94%E8%A1%8C%E6%89%AB%E6%8F%8F) and [Wikipedia: Deinterlacing](https://zh.wikipedia.org/wiki/%E5%8E%BB%E4%BA%A4%E9%8C%AF).

## Audio Encoding Parameters
### Codec
The method to convert sound from analog signal to digital signal (or vice versa), mainly including lossless encoding and lossy encoding. According to the sampling theorem, the audio encoding can only "infinitely approach" the natural signal, so that all audio codecs are virtually lossy. In the field of computers, it is generally agreed that only [PCM Encoding](https://zh.wikipedia.org/wiki/%E8%84%88%E8%A1%9D%E7%B7%A8%E7%A2%BC%E8%AA%BF%E8%AE%8A) that can achieve the highest level of fidelity is lossy encoding. All the common audio encoding in the Internet is lossy encoding. The common encoding formats include [MP3](https://zh.wikipedia.org/wiki/MP3), [AAC](https://zh.wikipedia.org/wiki/%E9%80%B2%E9%9A%8E%E9%9F%B3%E8%A8%8A%E7%B7%A8%E7%A2%BC), etc.

### Sample Rate
Sample rate is the number of samples taken from continuous signals per second to form discrete signals, measured in Hz. For more information, please see [Wikipedia: Sample Rate](https://zh.wikipedia.org/wiki/%E9%87%87%E6%A0%B7%E7%8E%87).

### Bitrate
For more information, please see video [Bitrate](#.E7.A0.81.E7.8E.87).

### Sound Channel
Sound channels refer to the mutually independent audio signals through which sound is recorded or played. The number of sound channels is the number of sound sources during audio recording or the number of speakers during video playback.
