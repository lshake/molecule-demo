#!/bin/bash
docker build -f Dockerfile.centos -t centos7-molecule:latest .
docker build -f Dockerfile.rhel -t rhel7-molecule:latest .

