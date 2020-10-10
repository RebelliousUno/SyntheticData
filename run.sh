#/bin/bash

for i in `seq 0 1000 1000000`; do python3 synthetic.py $i; done