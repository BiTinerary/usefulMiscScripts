#Enable g_serial Ambian

sudo su
echo "g_serial" >> /etc/modules

#Try This:
# nano /etc/systemd/system/serial-getty@ttyGS0.service.d/10-switch-role.conf
#If folder/file no exist:
# mkdir -p /etc/systemd/system/serial-getty@ttyGS0.service.d
#Try again:
# nano /etc/systemd/system/serial-getty@ttyGS0.service.d/10-switch-role.conf

# Make sure this is contained in conf file above.
#[Service]
#ExecStartPre=-/bin/sh -c "echo 2 > /sys/bus/platform/devices/sunxi_usb_udc/otg_role"

systemctl --no-reload enable serial-getty@ttyGS0.service
echo "ttyGS0" >> /etc/securetty
reboot
