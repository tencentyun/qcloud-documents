##  Product Overview
GCC (GPU Cloud Computing) instance is a rapid, stable and flexible computing service based on GPU, and is applicable to many GPU computing scenarios, such as deep learning, scientific computing, etc. Designed for convenient management, it is managed in the same way as with standard CVM. With extreme computing capacity based on excellent graphic processing capacity and high-performance computing capacity, you can be freed from heavy computing load effectively, thus improving the computing efficiency and competitiveness of your products.

## Why GCC Instance
Comparison between GCC Instance and Self-built GCC Instance
<table class="npf-comparsion-table">
	<colgroup>
		<col class="col2" style="width: 6%;" />
		<col class="col3" style="width: 54%;" />
		<col class="col4" style="width: 40%;" />
	</colgroup>
	<thead>
		<tr>
			<th>
			<div>Advantages</div>
			</th>
			<th class="stress-item">
			<div class="gradient ">Tencent Cloud GCC</div>
			</th>
			<th>
			<div>Self-built GPU-based Servers</div>
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
			<div><span class="unit-text">Elasticity</span></div>
			</td>
			<td class="stress-item">
			<div>
			
<ul class="text-list">
	<li>In just a few minutes, you can easily obtain one or more high-performance computing instances.</li>
	<li>It can be customized flexibly as needed, and upgraded to an instance specification with higher performance and larger capacity with just one click, to achieve rapid, smooth expansion, and satisfy the requirement for fast business development.</li>
<ul>
			</div>
			</td>
			<td>
			<div><span class="unit-text">Fixed configuration makes it hard to satisfy the ever-changing requirements.</span></div>
			</td>
		</tr>
		<tr>
			<td>
			<div><span class="unit-text">Performance</span></div>
			</td>
			<td class="stress-item">
			<div>
			
<ul class="text-list">
	<li>Transparently transmit and make the most advantage of GPU performance. </li>
	<li>Peak computing capacity for single machine: 14T Flops for single-precision floating point arithmetic and 0.4T Flops for double-precision floating point arithmetic.</li>
<ul>
			</div>
			</td>
			<td>
			<div>
			<ul class="text-list">
	<li>Users have to perform disaster recovery manually, depending on the robustness of hardware. </li>
	<li>Single point of failure may occur on physical server. Data security is uncontrollable.</li>
<ul>
			</div>
			</td>
		</tr>
		<tr>
			<td>
			<div><span class="unit-text">Ease of Use</span></div>
			</td>
			<td class="stress-item">
			<div>
			<ul class="text-list">
	<li>It can connect to CVM, CLB and many other cloud products seamlessly. Private network traffic is free of charge. </li>
	<li>Designed for ease of use, it is managed in the same way as with CVM, without the need to use jump server for login.</li>
	<li>Clear guides on installation and deployment of NVIDIA graphics card driver, eliminating high learning costs.</li>
<ul>
			</div>
			</td>
			<td>
			<div>
						<ul class="text-list">
	<li>The installation management service has been purchased to achieve automatic hardware expansion and driver installation. </li>
	<li>Jump server is used for login with complicated operation procedures.</li>
<ul>
			</div>
			</td>
		</tr>
		<tr>
			<td>
			<div><span class="unit-text">Security</span></div>
			</td>
			<td class="stress-item">
			<div>
						<ul class="text-list">
	<li>Resources are completely isolated among different users to ensure the data security. </li>
	<li>Well-established security groups and network ALC settings allow you to control and securely filter the inbound and outbound network traffic to or from instances and subnets.</li>
	<li>It can seamlessly connect to Cloud Security, and has basic protection and high defense services of Cloud Security equivalent to that of CVM.</li>
<ul>
			</div>
			</td>
			<td>
			<div>
			<ul class="unit-text">
			<li>Resources are shared among different users, and data is not isolated.</li>
			<li>Additional security protection services need to be purchased.</li>
			<ul>
			</div>
			</td>
		</tr>
		<tr>
			<td>
			<div><span class="unit-text">Cost</span></div>
			</td>
			<td class="stress-item stress-last-item">
			<div>
<ul class="unit-text">
			<li>Prepaid billing method is supported. You can purchase physical machines without the need to make a huge one-off investment.</li>
			<li>Hardware is updated upon update of NVIDA GPU graphics card, eliminating the need to replace the hardware after each update.</li>
			<li>With low server OPS cost, you can effectively reduce investment in infrastructure construction without the need to purchase and prepare hardware resources in advance.</li>
			<ul>
			</div>
			</td>
			<td>
			<div>
			<ul class="unit-text">
			<li>High server investment and operating costs.</li>
			<li>Due to high power consumption of devices, hardware modification is required.</li>
			<li>Higher IT OPS cost is required to guarantee the stability of service.</li>
			<ul>
			</div>
			</td>
		</tr>
	</tbody>
</table>


Comparison between GCC Instance and CVM Instance
![](//mc.qcloudimg.com/static/img/ac3ea7314a71758f5c7caef08ec63692/image.jpg)

<table class="table" contenteditable="true">
	<thead>
		<tr>
			<th>Dimension</th>
			<th>GCC</th>
			<th>CVM</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Number of Kernels</td>
			<td>Thousands of accelerated kernels (dual ENI, M40, up to 6,144 accelerated kernels)</td>
			<td>Dozens of kernels</td>
		</tr>
		<tr>
			<td>Product Features</td>
			<td>1. Numerous efficient arithmetic logic units (ALU) support parallel processing<br />
			2. Massively parallel throughput can be achieved using multiple threads<br />
			3. Simple logic control</td>
			<td>1. Complex logic control unit<br />
			2. Powerful arithmetic logic unit<br />
			3. Simple logic control</td>
		</tr>
		<tr>
			<td>Application Scenarios</td>
			<td>Program with intensive computation and parallel arithmetic</td>
			<td>Program with logic control and serial arithmetic</td>
		</tr>
	</tbody>
</table>



