#!/bin/bash
cd /opt/student-api
nohup python3 app.py > /var/log/student-api.log 2>&1 &
