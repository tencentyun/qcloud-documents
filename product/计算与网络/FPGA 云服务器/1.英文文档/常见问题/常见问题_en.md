**Q: What is FPGA? Why do I need it?**
**A:**FPGA is often used to customize hardware. FPGA is more flexible than dedicated hardware (such as ASIC) because it can be programmed in the field once it is inserted into a PC motherboard.
FPGA is a programmable integrated circuit that can be configured using software. By using FPGA, you can minimize application processing latency and improve processing capability compared with servers that only use CPU. In addition, FPGA can be reprogrammed. Therefore, you have the flexibility to update and optimize hardware acceleration without having to redesign the hardware.
FPGA is a programmable chip with a limited number of simple logic gates and storage units. FPGA programming uses HDL (hardware description language) to connect these logic gates and storage units to form a variety of operations that can be executed in parallel. Therefore, it is suitable for customizing hardware. It can provide up to 30 times the acceleration in some special applications, such as big data mining, financial risk analysis, etc.

**Q: What is Tencent Cloud FCC instance?**
**A:** FCC instance is a new computing service that can accelerate applications with programmable hardware. You can easily get and configure your FPGA computing instance in a few minutes, and then deploy and access the FPGA with a few clicks. We provide you with a reprogrammable environment where you can program FPGA without having to redesign your hardware and create custom hardware acceleration for your application, giving you greater focus on business development.


**Q: How does Tencent Cloud FCC instance compare to traditional FPGA solutions?**
**A:** FCC instance can accelerate applications with programmable hardware. Through FCC instance, you can access FPGA hardware with just a few clicks to save time and cost on a full FPGA development cycle and reduce deployment time from years or months to days. Although FPGA technology has been around for decades, due to time, costs and other factors of infrastructure development, hardware design and large-scale deployment, it's hard to adopt application acceleration in the development of accelerators and business model of selling custom hardware to traditional enterprises. This service frees customers from the undifferentiated heavy work of developing FPGA in local data center. With a large number of FPGA intellectual property (IP) rights, Tencent and its partners can help accelerate the launch process of your products. In addition, you can also provide the IP you designed via Tencent Cloud marketplace.


**Q: What is Tencent Cloud FPGA IP?**
**A:** FPGA IP refers to FPGA Intellectual Property. With a large number of FPGA intellectual property (IP) rights, Tencent and its partners can help accelerate the launch process of your products. In addition, you can also provide the IP you designed via Tencent Cloud marketplace.



**Q: What is Tencent Cloud FPGA Image?**
**A:** Tencent Cloud FPGA Image is an operating system image that contains FPGA. You can deploy and develop using the FPGA Image provided by Tencent Cloud. Currently, the Tencent Cloud's official FPGA Image is provided free of charge, so you can detect the pictures by calling the IP of Alexnet model based on deep learning, to accelerate your product application.

**Q: Do I need to become an FPGA expert to use FCC instances?**
**A:** No, you don't. The FCC instance released by the Tencent Cloud this time provides an EPGA-based Alexnet model API for image classification which can be called by users to implement apps.
We will provide a framework later. Together with the operating system support provided by the Tencent Cloud FCC instance, you can easily access DDR and use DMA to communicate between the CVM and FPGA, and developers only need to focus on application-oriented logic design.

**Q: How to start using an FCC instance as an FPGA developer?**
**A:** We will provide a framework which supports development languages such as C/C++, OpenCL and Verilog/VHDL later. FPGA developers can select a familiar language for FPGA logic design.



**Q: How to start using FCC instance if I am not an FPGA developer?**
**A:** We provide an EPGA-based Alexnet API for image classification which can be called by users to implement apps. For more information, please see [Overview of Getting Started](https://cloud.tencent.com/document/product/565/8220)


**Q: Can I add an FPGA to any CVM instance type?**
**A:** No, you can't. FPGA is a hardware instance customized by the Tencent Cloud. Currently, FCC instance has one instance specification and does not support FPGA elastic mounting to the CVM.

**Q: How can I get the internal trial qualification of FCC instance?**
**A:** Currently, FCC instance is under internal trial. Only the user whose application for internal trial is approved can use it. You can apply for internal trial by completing the [Internal Trial Application](https://cloud.tencent.com/act/apply/fpga). If your application is approved, our pre-sales engineer will contact you for internal trial use. The distribution date of FCC instance across the network is subject to the notice by Tencent Cloud.



