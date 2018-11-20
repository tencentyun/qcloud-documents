## Overview

Thank you for using [Tencent Cloud Game Multimedia Engine SDK](https://intl.cloud.tencent.com/product/tmg?idx=1). This document provides a detailed description that makes it easy for developers to select sound quality via GME SDK..

## Overview of Sound Quality Types

As shown below, the audio type you select varies with different application scenarios.

| Audio Type | Meaning | Parameter | Volume Type | Recommended Sampling Rate on the Console | Application Scenarios |
| -------------------------- | -------- | ---- | -------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| ITMG_ROOM_TYPE_FLUENCY			|Fluent	|1|Speaker: chat volume; headset: media volume 	| 16k sampling rate is recommended if there is no special requirement for sound quality					| Fluent sound quality and ultra-low delay which is suitable for team speak scenarios in games like FPS and MOBA.	|							
| ITMG_ROOM_TYPE_STANDARD			|Standard	|2|Speaker: chat volume; headset: media volume	| Choose 16k or 48k sampling rate depending on different requirements for sound quality				| Good sound quality and medium delay which is suitable for voice chat scenarios in casual games like Werewolf and board games.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|High-quality	|3|Speaker: media volume; headset: media volume	| To ensure optimum effect, it is recommended to enable HQ configuration with 48k sampling rate	| Super-high sound quality and relative high delay which is suitable for scenarios demanding high sound quality, such as music playback and online karaoke.	|

Please select the appropriate sampling rate (16k or 48k) in the console according to the actual application scenario. In the integration of SDK, you can adjust the "audio type" by passing parameters, but the actual sampling rate will not exceed the sampling rate selected in the console. For example, if you select a sampling rate of 16k in the console and pass "3" for the "audio type" of the client, the actual sampling rate is 16k. If you select a sampling rate of 48k in the console and pass "1" for the "audio type" of the client, the actual sampling rate is 16k.

