#!/bin/bash

pip install -e .
[[ -f $1/.root ]] || touch $1/.root