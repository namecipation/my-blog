**Connecting raspberry pi without html cable**
==================================

This document describes step by step to set up a **headless Raspberry Pi 5** 
(using only LAN and no HDMI cable) with **GUI (LXDE)** accessible via **RealVNC Viewer**.

Steps Summary
-------------

1. Flash Raspberry Pi OS (64-bit Bookworm)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Use Raspberry Pi Imager with these Advanced Settings:

   - ✅ Enable SSH → Use password authentication
   - ✅ Set username: ``namerasp``
   - ✅ Set password: ``<your-password>``
   - ✅ Set hostname: ``raspberrypi``
   - ❌ Skip Wi-Fi (LAN will be used)
   - ✅ Save & Write the image to SD card

2. Boot Pi and Connect via LAN
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Insert SD card, power on the Pi
   - Connect Pi to your Mac with an Ethernet cable
   - On Mac, enable Internet Sharing: ``Wi-Fi → Ethernet``
   - Raspberry Pi will acquire IP: ``192.168.2.2``

3. SSH into Raspberry Pi
   ~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: bash

      ssh namerasp@raspberrypi.local
      # or
      ssh namerasp@192.168.2.2

4. Update System
   ~~~~~~~~~~~~~

   .. code-block:: bash

      sudo apt update
      sudo apt full-upgrade -y

5. Install GUI Desktop (LXDE)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: bash

      sudo apt install --reinstall raspberrypi-ui-mods lxsession lightdm pi-greeter -y

6. Enable Autologin
   ~~~~~~~~~~~~~~~~

   .. code-block:: bash

      sudo mkdir -p /etc/lightdm/lightdm.conf.d
      sudo nano /etc/lightdm/lightdm.conf.d/20-pi-autologin.conf

   Paste:

   .. code-block:: ini

      [Seat:*]
      autologin-user=namerasp

7. Force Virtual Display (HDMI-less)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: bash

      sudo nano /boot/firmware/config.txt

   Add to the end:

   .. code-block:: ini

      hdmi_force_hotplug=1
      hdmi_group=2
      hdmi_mode=82  # 1080p resolution

8. Configure LXDE as Default Session
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: bash

      sudo nano /etc/lightdm/lightdm.conf

   Add:

   .. code-block:: ini

      [Seat:*]
      autologin-user=namerasp
      autologin-session=LXDE-pi-x
      user-session=LXDE-pi-x

9. Reboot
   ~~~~~~

   .. code-block:: bash

      sudo reboot

10. Connect via RealVNC Viewer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Server: ``raspberrypi.local`` or ``192.168.2.2``
    - Login: ``namerasp``
    - Password: ``<your-password>``
    - You should now see the **full GUI desktop**

Final Notes
-----------

- No HDMI is required
- RealVNC must be enabled and autologin properly configured
- LightDM + LXDE-pi-x ensures GUI session is loaded headless