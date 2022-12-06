# Embedded Linux CAN bus
Embedded Linux CAN bus settings and scripts/software for CAN bus communication 

## Raspberry pi: 
1. Connect a modded (3.3V transceiver) HW-184 SPI-CAN bus module to the Raspberry pi SPI bus
2. Add the following to /boot/config.txt
```bash command-line
dtparam=spi=on
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25, spimaxfrequency=2000000
dtoverlay=spi0-hw-cs
```

## Beaglebone
1. Connect a CAN bus cape
* can0 is connected to
```bash command-line
config-pin p9.19 can
config-pin p9.20 can
```
* can1 is connected to
```bash command-line
config-pin p9.24 can
config-pin p9.26 can 
```

https://www.beyondlogic.org/adding-can-to-the-beaglebone-black/    

2. Add the overlay to uboot (/boot/uEnv.txt)
* Have to use the correct overlay file for the type of BeagleBone 
- Beaglebone Black am335x
```bash command-line
uboot_overlay_addr4=/lib/firmware/BB-CAN0-00A0.dtbo (can0)
uboot_overlay_addr5=/lib/firmware/BB-CAN1-00A0.dtbo (can1)
```

- Beaglebone AI am572x

## Generic (for both Beaglebone and Raspberry pi)
3. Install can-utils
```bash command-line
sudo apt install can-utils
```

4. Bring up the CAN interface (can0) with an appropriate bitrate 
```bash command-line
sudo /sbin/ip link set can0 up type can bitrate 500000
```
5. Debugging/testing:
```bash command-line
candump can0 # Listen and print all messages
cansend can0 060#0100000000000001 # Send a message with id 60
sudo netstat -lptu # get network/can statistics
sudo ip link set can0 down  # and repeat step 4. to restart the interface if needed.
```
6. Edit /etc/network/interfaces for automatic setup:
```bash command-line
auto can0
iface can0 inet manual
    pre-up /sbin/ip link set can0 type can bitrate 500000 triple-sampling on restart-ms 100
    up /sbin/ifconfig can0 up
    down /sbin/ifconfig can0 down
```
