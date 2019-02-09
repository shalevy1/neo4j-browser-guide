#!/usr/bin/env bash

asciidoctor $1 -T ./templates -a leveloffset=+1 -o $2