Capturing screenshot by time offset is to capture screenshots at a specified time offset position of a video, and return the URL of the screenshot generated. The input parameters of this operation contain the following two types:

1. Time offset parameters: Time offset of the position where a　screenshot　is　to be captured in a video;
2. Image parameters: Such as image resolution, image filling method (how to fill a screenshot when its resolution is not proportional to that of the original image).

For ease of calling, VOD pre-defines a set of specifications to simplify the input of the second type of parameters.

## Standard Output Specifications of Screenshots Captured by Time Offset in VOD System

| Template ID | Screenshot Width | Screenshot Height | Screenshot Filling Method |
|---------|---------|---------|---------|
| 10 | The same as the original | The same as the original | N/A |
| 20 | 500 | 281 | Stretch to fill |
