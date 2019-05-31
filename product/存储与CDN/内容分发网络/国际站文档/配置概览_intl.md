CDN supports various custom configurations which allow you to optimize your CDN acceleration according to your business needs.

## Basic Configuration

| Configuration                            | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Basic Info](https://cloud.tencent.com/document/product/228/7864) | Change the project to which a domain belongs, domain's content type |
| [Origin server info](https://cloud.tencent.com/document/product/228/6289) | Configure hot slave origin and modify origin server to ensure the success of back-to-origin requests |
| [Hosting Source](https://cloud.tencent.com/doc/product/228/6293) | Specify the site domain accessed by the CDN node at the origin server |

## Access Control

| Configuration                            | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Filter Parameter Configuration](https://cloud.tencent.com/doc/product/228/6291) | Specify whether a node will ignore the parameters following the "?" in user request URLs |
| [Hotlink Protection Configuration](https://cloud.tencent.com/doc/product/228/6292) | Configure HTTP referer blacklist & whitelist |
| [IP Blacklist & Whitelist](https://cloud.tencent.com/doc/product/228/6298) | Configure IP blacklist & whitelist for access control |
| [IP Access Frequency Limit](https://cloud.tencent.com/doc/product/228/6420) | Configure access frequency limit of an IP to a single node |
| [Video Drag Configurations](https://intl.cloud.tencent.com/document/product/228/8111) | Support to open video drag configuration |


## Cache Configuration
| Configuration                            | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Cache Validity Period Configuration](https://cloud.tencent.com/doc/product/228/6290) | Configure cache expiration rules for specified resource contents |

 ## Origin Configuration

| Configuration                            | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Intermediate Node Configuration](https://cloud.tencent.com/doc/product/228/6294) | Specify whether to use an intermediate node |
| [Range GETs Configuration](https://cloud.tencent.com/document/product/228/7184) | Enable/disable Range back-to-origin transmission in slices |
| [Follow 302 Configuration](https://cloud.tencent.com/document/product/228/7183) | Configure whether a request should be redirected when the origin server returns the status code 302 |

## Advanced Configuration
| Configuration                            | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [HTTPS Configuration](https://cloud.tencent.com/doc/product/228/6295) | Configure HTTPS to achieve a secure acceleration. HTTPS forced redirection is supported |
| [SEO Optimization](https://cloud.tencent.com/doc/product/228/6297) | Enable SEO optimization configuration to ensure a consistent domain authority on search engines |
| [HTTP Header](https://cloud.tencent.com/doc/product/228/6296) | Add HTTP header configurations           |
| [Capped Bandwidth Configuration](https://cloud.tencent.com/document/product/228/7541) | Configure bandwidth cap for domains. When the cap is reached, the CDN service will be disabled and the access request is forwarded to the origin server |

## Oversea CDN Configuration

| Configuration                            | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [International Private Line (Beta)](https://cloud.tencent.com/document/product/228/7854) | Enable international private line during the use of oversea CDN acceleration service to improve back-to-origin connections |
