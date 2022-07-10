For 2022 MIT AI2 summer Capstone project, suggested device to purchase is CanaKit Raspberry Pi 4 4GB Starter PRO Kit which has OS pre-installed in Micro SD in the kit.

Below install guide is for Raspberry Pi without OS pre-installed in Micro-SD card.

For more detailed installation info, please check https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up

## SSH into your Raspberry Pi
- [Enable SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/): Need reboot OS.
  - Raspberry Pi Configuration -> Interfaces -> SSH: Enable
  - Or Run `$ sudo raspi-config`. This also can be used to enable Camera.
- [Set up Static IP address](https://www.raspberrypi.org/documentation/configuration/tcpip/)
  - In your MBP, check your default Gateway IP of your local network.
    ```
    $ netstat -nr | grep default
     default            192.168.86.1       UGSc           en0
     default                                 fe80::%utun0                    UGcI          utun0
     default                                 fe80::%utun1                    UGcI          utun1
    ```
  - In your Raspberry Pi, modify `/etc/dhcpcd.conf` to set up static IP addresses at the bottom. wlan0 is wireless IP.
    ```
    pi@raspberrypi:~ $ nano /etc/dhcpcd.conf
    ...
    # fallback to static profile on eth0
    #interface eth0
    #fallback static_eth0
    
    interface eth0
    
    static ip_address=192.168.86.100/24
    static routers=192.168.86.1
    static domain_name_servers=192.168.86.1
    
    interface wlan0
    
    static ip_address=192.168.86.200/24
    static routers=192.168.86.1
    static domain_name_servers=192.168.86.1
    ...
    
    pi@raspberrypi:~ $ reboot
    ```
- In your Raspberry Pi, Check the IP address: Run `$ ping raspberrypi.local` in your Raspberry Pi.
- In your MBP, SSH into your pi from another computer. Default password is `raspberry`.
    ```
    ❯ ssh pi@192.168.86.200
    The authenticity of host '192.168.86.200 (192.168.86.200)' can't be established.
    ECDSA key fingerprint is SHA256:F6BlQO9PDGmyajljfTSYSZdxK4tMokqzngTfmFKU6LQ.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '192.168.86.200' (ECDSA) to the list of known hosts.
    pi@192.168.86.200's password:
    Linux raspberrypi 5.4.79-v7+ #1373 SMP Mon Nov 23 13:22:33 GMT 2020 armv7l
    
    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.
    
    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Wed Dec  9 00:06:42 2020
    
    SSH is enabled and the default password for the 'pi' user has not been changed.
    This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.
    
    pi@raspberrypi:~ $
    ```
  
