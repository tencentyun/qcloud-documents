Cloud API focuses on how to manage your LVB streams. For this end, Tencent Cloud provides two modes: LVB Code Mode (new) and Channel Mode (old).

### LVB Code Access Mode
LVB Code Mode is designed to help you directly manage LVB stream at the backend. It was only available for several domestic LVB platforms before May 2016. LVB Code Mode now becomes a major access solution for Tencent Cloud LVB service because of its low access cost and high reliability.

In this solution, URL generation and LVB stream are determined by you, which is highly flexible and customizable. So it is the best access solution for LVB streams such as game LVB and Showtime LVB.

![](//mc.qcloudimg.com/static/img/653f16b4eca39cd915cacc6456378778/image.png)

### Channel (Hosting) Mode
Channel Mode is customized for a manual management of LVB channels. It is suitable for a single LVB event:
- **Create a channel**: Before LVB starts, create a channel to get a push URL, and publish the playback URL.
- **Disable a channel**: When LVB is finished, or if an accident occurs, you can "ban" the LVB by disabling the LVB channel at any time.

This mode also provides server API support, but the access cost is much higher and the stability is not as good as LVB Code Mode.

### Difference Between Two Modes
| Item | LVB Code Mode | Channel Mode |
|---------|---------|---------|
| Push URL | You can specify an URL on your own without communicating with the Tencent Cloud backend | This URL is generated at the Tencent Cloud backend by creating a channel |
| Hotlink Protection | Support push and playback hotlink protection (contact customer service to configure a playback hotlink protection) | Support push hotlink protection and FLV/HLS playback hotlink protection (RTMP push hotlink protection is not available) |
| API List | [API for LVB Stream Management](https://cloud.tencent.com/document/product/267/5956) | Suitable for manual operation. [API](https://cloud.tencent.com/document/product/267/5664) is also provided |
| Message Notification | You are notified of any stream status change in JSON format | Not supported |
| Application Scenario | Suitable for server interfacing, for example, a **Showtime LVB** | Suitable for manual operation, such as an **LVB event** |

