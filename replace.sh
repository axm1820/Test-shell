#!/bin/bash
find . -name "*" -print0 | xargs -0 sed  -e 's/contour/jama/g'
