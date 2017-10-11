#!/usr/bin/env python
# -*- coding: utf-8 -*-

outfile = open("pizzaout.txt","a")

fname = "pizza.txt"
with open(fname) as f:
    lines = f.readlines()

for line in lines:
    if len(line.split("\",")[0].strip()) > 0:
        print line.split("\",")[0]
        print "-------------------------"
        
        outfile.write(line.split("\",")[0] + "\n")
outfile.close()

