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








####################
outfile = open("Table.txt","a")

fname = "txt.txt"
with open(fname) as f:
    lines = f.readlines()

for line in lines:
    if len(line.split("\",")[0].strip()) > 0:
        print (line + "Done")

        
        outfile.write("\n" + '<tr><td valign="middle" align="center" style="width: 1%;"><input id="'+line.split("\",")[0]+'chkBox" name="'+line.split("\",")[0]+'chkBox" type="checkbox" onclick="javascript: checkManual();" value="@*@Model[i].UserId*@" /></td><td style="width: 21%;" class="search_field">Pus </td><td><input type="text" id="'+line.split("\",")[0]+'" name="'+line.split("\",")[0]+'" placeholder="Non Reactive" /></td><td><p>-</p></td></tr>' + "\n" )
outfile.close()


