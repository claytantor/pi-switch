## install python 3
```
python3 -m venv venv --system-site-packages
source venv/bin/activate
```

## creating the systemd service
```
$(pwd)/venv/bin/python3 makeservice.py -d $(pwd) -t piswitch.service.mustache > piswitch.service
```

Instructions for setting up your service can be found at https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/

```
sudo cp piswitch.service /lib/systemd/system/piswitch.service
sudo chmod 644 /lib/systemd/system/piswitch.service
sudo systemctl daemon-reload
sudo systemctl unmask piswitch.service
sudo systemctl enable piswitch.service
