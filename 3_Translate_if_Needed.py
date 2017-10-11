#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate
###################################################
File_Name= raw_input("Enter the name of file: ")

###################################################


#write on a file and save it
# ! tweet_text = ' my test text \n'
# ! saveFile = open('foo.txt','w')
# ! saveFile.write(tweet_text)
# ! saveFile.close()


#open the file and read it 
my_tweets = open(File_Name,"r").read()
# ! print my_tweets
#to choose a file name
#str = raw_input("Enter your file_name: ")

#translate
def main():
    to_translate = my_tweets
    #print(translate(to_translate))
    print(translate(to_translate, 'ar'))
    print(translate(to_translate, 'it'))

if __name__ == '__main__':
    main()
