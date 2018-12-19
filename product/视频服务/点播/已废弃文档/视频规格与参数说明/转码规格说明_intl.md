Audio and video file transcoding involves many complex parameters. To simplify the call process, VOD pre-defines a set of standard transcoding specifications, with each corresponding to a group of transcoding parameters. For more information, please see standard output specifications of transcoding in VOD system.

Besides, if you have customized transcoding specifications, you can submit a ticket for request. VOD backend will then configure it for you.

## Standard Output Specifications of Transcoding in VOD System

<table style="display:table">
    <tr>
        <td rowspan=2>
            Specifications                
        </td>
        <td rowspan=2>
            Encapsulation Format                
        </td>
        <td colspan=8>    
            Video Parameter        
        </td>
        <td colspan=4>    
            Audio Parameter        
        </td>
    </tr>
    <tr>
        <td>
            Encoder
        </td>
        <td>
            Frame Rate
        </td>
        <td>
            Wide Edge
        </td>
        <td>
            Narrow Edge
        </td>
        <td>
            Colorimetric Space
        </td>
        <td>
            Bit Depth
        </td>
        <td>
            Bit Rate Mode
        </td>
        <td>
            Bit Rate
        </td>
        <td>
            Encoder
        </td>
        <td>
            Bit Rate
        </td>
        <td>
            Channel
        </td>
        <td>
            Sampling Rate
        </td>
    </tr>
    <tr>
        <td>
            10
        </td>
        <td>
            MP4
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            320
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            256 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            20
        </td>
        <td>
            MP4
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            640
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            512 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            30
        </td>
        <td>
            MP4
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1280
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            1,024 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            40
        </td>
        <td>
            MP4
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1920
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            2,500 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            210
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            320
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            256 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            220
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            640
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            512 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            230
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1280
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            1,024 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            240
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1920
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            2,500 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
</table>


## Other Output Specifications of Transcoding in VOD System

<table style="display:table">
    <tr>
        <td rowspan=2>
            Specifications                
        </td>
        <td rowspan=2>
            Encapsulation Format                
        </td>
        <td colspan=8>    
            Video Parameter        
        </td>
        <td colspan=4>    
            Audio Parameter        
        </td>
    </tr>
    <tr>
        <td>
            Encoder
        </td>
        <td>
            Frame Rate
        </td>
        <td>
            Wide Edge
        </td>
        <td>
            Narrow Edge
        </td>
        <td>
            Colorimetric Space
        </td>
        <td>
            Bit Depth
        </td>
        <td>
            Bit Rate Mode
        </td>
        <td>
            Bit Rate
        </td>
        <td>
            Encoder
        </td>
        <td>
            Bit Rate
        </td>
        <td>
            Channel
        </td>
        <td>
            Sampling Rate
        </td>
    </tr>
    <tr>
        <td>
            211
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            The same as the original
        </td>
        <td>
            The same as the original
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            1,000 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            221
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            960
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            1,500 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            231
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1280
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            2,500 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            241
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1920
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            3,500 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
    <tr>
        <td>
            242
        </td>
        <td>
            HLS
        </td>
        <td>
            H.264
        </td>
        <td>
            24
        </td>
        <td>
            1920
        </td>
        <td>
            Scale according to the DAR or PAR of the original video (DAR preferred)
        </td>
        <td>
            YUV420P
        </td>
        <td>
            8
        </td>
        <td>
            ABR
        </td>
        <td>
            3,000 kbps
        </td>
        <td>
            ACC
        </td>
        <td>
            48 kbps
        </td>
        <td>
            Double
        </td>
        <td>
            44,100 Hz
        </td>
    </tr>
</table>
