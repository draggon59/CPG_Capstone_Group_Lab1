#!/bin/bash

# check for newer versions of the software packages installed on this server and update them
# "-y" means automatically answer yes for automation purposes
dnf update -y

# install the Apache HTTP server
dnf install -y httpd

# start Apache
systemctl start httpd

# start Apache automatically whenever the Linux machine boots
systemctl enable httpd

