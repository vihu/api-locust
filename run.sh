#!/bin/bash

#set -e

docker-compose up --scale locust-worker=4
