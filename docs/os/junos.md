# JunOS

## Commands

```shell
# command-line interface
cli

# show mac table
show ethernet-switching table brief

# view current configuration
show configuration | display set | no-more

# When the power is reset, Juniper will default to recovery mode. To prohibit this behavior you need to do:
request system configuration rescue save
```

## Configuration process

```shell
# take a USB-COM adapter and install Tera-Term on the computer
# TeraTerm speed should be set according to the device (maybe for our 115200)
# connect the cable from the COM port to Juniper's CON port (rear)
# turn on Juniper, in TeraTerm we see the download process
# after booting, enter root as the user, nothing as the password
# go to juniper's configuration interface
cli
# start the configuration process
configure
# we tell Juniper to read the configuration from the terminal (after reading, you will need to press Ctrl+D to stop the reading process)
# check the configuration for syntax errors
commit check
# apply the configuration for 10 minutes (read above)
commit confirmed
# finally apply the configuration
commit
# disable startup of Juniper's recovery utility on power reset (juniper will boot as usual)
request system configuration rescue save
# copy the current configuration to juniper's alternative bootloader
request system snapshot slice alternate
# exit the cli utility
exit
# juniper logout
exit

```