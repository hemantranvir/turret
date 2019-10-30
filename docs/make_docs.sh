#!/bin/sh

sphinx-apidoc -f -o source/apis ../ && make html
