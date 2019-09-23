vfj-wind
========

An SM5386B data acquisition application/library


Installation
------------
<pre>
git clone https://github.com/la1k/vfj-wind.git
cd vfj-wind
python -m pip install minimalmodbus
python vfj-wind <i>serial_port_device</i>
</pre>

Description
-----------

This code will acquire data from SM5386B-based wind sensors via a USB-RS485 interface and write the data to an HTML file.

Requires Python package <pre>minimalmodbus</pre>
