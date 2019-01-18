### Highlights
Application Programming Interface (API) is a convention for the connection of different components of a software system. Properly designed APIs can reduce the interdependence among different parts of the system and ensure a high performance of the system. Four types of open APIs are provided for now. Users can quickly obtain reliable data by calling these APIs.
![](//mc.qcloudimg.com/static/img/6dd3e0742a280d412e900f5fc4438726/image.jpg)

### Basic Metrics of Application
<hr>
<table>
    <thead>
    <tr>
        <th>Offline data</th>
        <th></th>
        <th></th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=101">New users</a></td>
        <td rowspan="5">/ctr_user_basic/get_offline_data</td>
        <td>Metric ID: 10101</td>
    </tr>
    <tr>
        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=101">Active users</a></td>
        <td>Metric ID: 10102</td> 
    </tr>
    <tr>
        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=101">Launch count</a></td>
        <td>Metric ID: 10103</td>
    </tr>
    <tr>
        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=101">Cumulative launch count</a></td>
        <td>Metric ID: 10104</td>
    </tr>
    <tr>
        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=101">Active accounts</a></td>
        <td>Metric ID: 10105</td>
    </tr>
    </tbody>
</table>
<table class="gui-table text-center">
                                    <thead>
                                    <tr>
                                        <th class="no-right">Real-time data</th>
                                        <th class="no-left no-right"></th>
                                        <th class="no-left"></th>
                                    </tr>
                                    </thead>
                                    <tbody class="text-center">
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=102">New users</a></td>
                                        <td rowspan="5">/ctr_user_basic/get_realtime_data</td>
                                        <td>Metric ID: 10101</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=102">Active users</a></td>
                                        <td>Metric ID: 10102</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=102">Launch count</a></td>
                                        <td>Metric ID: 10103</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=102">Cumulative launch count</a></td>
                                        <td>Metric ID: 10104</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=102">Active accounts</a></td>
                                        <td>Metric ID: 10105</td>
                                    </tr>
                                    </tbody>
                                </table>
                                
### Terminal Device Data

Provide multi-dimensional analysis of new users (10301), active users (10302) and launch count (10303) for each type of terminal device. Top 100 device types are recorded for each metric.
<hr>
<table class="gui-table text-center">
                                    <thead>
                                    <tr>
                                        <th>Offline data</th>
                                        <th class="no-left no-right"></th>
                                        <th class="no-left"></th>
                                    </tr>
                                    </thead>
                                    <tbody class="text-center">
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=103">Operating system version</a></td>
                                        <td rowspan="5">/ctr_terminal_anal/get_offline_data</td>
                                        <td>Terminal type: ty=1</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=103">Resolution</a></td>
                                        <td>Terminal type: ty=2</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=103">Network condition</a></td>
                                        <td>Terminal type: ty=3</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=103">Operator</a></td>
                                        <td>Terminal type: ty=4</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=103">Device model</a></td>
                                        <td>Terminal type: ty=5</td>
                                    </tr>
                                    </tbody>
                                </table>
                                
### User Behavior Data
<hr>
<table class="gui-table text-center">
                                    <thead>
                                    <tr>
                                        <th>Offline data</th>
                                        <th class="no-left no-right"></th>
                                        <th class="no-left"></th>
                                    </tr>
                                    </thead>
                                    <tbody class="text-center">
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=104">DAU</a></td>
                                        <td rowspan="3">/ctr_active_anal/get_offline_data</td>
                                        <td>Metric ID: 10201</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=104">WAU</a></td>
                                        <td>Metric ID: 10202</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=104">MAU</a></td>
                                        <td>Metric ID: 10203</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=105">Per capita usage duration</a></td>
                                        <td rowspan="4">/ctr_usage_anal/get_offline_data</td>
                                        <td>Metric ID: 10401</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=105">Average duration per use</a></td>
                                        <td>Metric ID: 10402</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=105">Per capita page visited</a></td>
                                        <td>Metric ID: 10403</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=105">Average of pages per visit</a></td>
                                        <td>Metric ID: 10404</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=106">Usage frequency of new users</a></td>
                                        <td rowspan="2">/ctr_usage_anal/get_freq_dis</td>
                                        <td>Metric ID: 10405</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=106">Usage frequency of active users</a></td>
                                        <td>Metric ID: 10406</td>
                                    </tr>
                                    </tbody>
                                </table>
                                
### Data Supported for Developing

Provide multi-dimensional analysis of number of times the error occurred (10503) and number of people affected by the error (10504) for each type of terminal device.
<hr>
<table class="gui-table text-center">
                                    <thead>
                                    <tr>
                                        <th>Offline data</th>
                                        <th class="no-left no-right"></th>
                                        <th class="no-left"></th>
                                    </tr>
                                    </thead>
                                    <tbody class="text-center">
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=107">Number of times the error occurred</a></td>
                                        <td rowspan="2">/ctr_crash_anal/get_offline_data</td>
                                        <td>Metric ID: 10501</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=107">Number of people affected by the error</a></td>
                                        <td>Metric ID: 10502</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=108">App version</a></td>
                                        <td rowspan="3">/ctr_crash_anal/get_env_dis</td>
                                        <td>Terminal type: ty=1</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=108">Operating system</a></td>
                                        <td>Terminal type: ty=2</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=108">Device model</a></td>
                                        <td>Terminal type: ty=3</td>
                                    </tr>
                                    <tr>
                                        <td><a href="http://mta.qq.com/mta/ctr_index/open_api_detail?func_id=109">Top 100 records in crash list</a></td>
                                        <td rowspan="1">/ctr_crash_anal/get_err_list</td>
                                        <td>ID of associated metrics: 10501 and 10502</td>
                                    </tr>
                                    </tbody>
                                </table>
