import os
import re
import subprocess
import glob

# *** Tool executing procedure ***
# "exiftool.exe" should present in the tool location
# "tag.ini" should present in the tool location
# Metadata Tag values should capture in the "tag.ini" file in respective xml tags
# If no value for particular element then leave that tag as empty tag, i.e. <Scanner></Scanner>
# TIFF date & time value format should be "YYYY:MM:DD HH:MM:SS", if format is wrong tool notify the error message in "error.log" file.
# get the Input file directory
# Tool will apply the TIFF tag in the same location Input file directory

print("\n *** Adding Metadata tags for TIFF & JPEG files *** \n")
print(" Document Name ")
print(" Artist ")
print(" Scanner Manufacture ")
print(" Scanner  Model ")
print(" Software ")
print(" DateTime \n")

filepath = input(" Enter the File path: ")

meta = "tag.ini"  # All metadata values should update in the INI file.

text_file = filepath + "/" + "error.log"

if os.path.exists(meta): # check the tag.ini file present
	pass
else:
	print("\n tag.ini file is missing")
	f = open(text_file, "a+")
	f.write(str("tag.ini file is missing\n"))
	f.close()
	exit()

exiftool = "exiftool.exe"

# check the exiftool file present
if os.path.exists(exiftool):
	pass
else:
	print("\n exiftool.exe tool is missing")
	f = open(text_file, "a+")
	f.write(str("exiftool.exe tool is missing\n"))
	f.close()
	exit()


#reading the tag.ini file
fo = open(meta, "r+", encoding="utf-8")
str1 = fo.readlines()

art = re.search(r"<Artist>(.*)</Artist>", str(str1))
artist = str("\"")+art.group(1)+str("\"")

tit = re.search(r"<Name>(.*)</Name>", str(str1))
title = str("\"")+tit.group(1)+str("\"")

sca = re.search(r"<Scanner>(.*)</Scanner>", str(str1))
scanner = str("\"")+sca.group(1)+str("\"")

scam = re.search(r"<ScannerModel>(.*)</ScannerModel>", str(str1))
scannermodel = str("\"")+scam.group(1)+str("\"")

soft = re.search(r"<Software>(.*)</Software>", str(str1))
software = str("\"")+soft.group(1)+str("\"")

date = re.search(r"<DateTime>(.*)</DateTime>", str(str1))
datetime = date.group(1)
date1 =  str("\"")+ datetime +str("\"")

fo.close()

pattern = "([0-9][0-9][0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ([0-9][0-9]):([0-9][0-9]):([0-9][0-9])"
result = re.match(pattern, datetime)

# check the date pattern
if  date1 == str("\"\"") or result:
	pass
else:
	print("date format not correct in \"tag.ini\", Date format should be: YYYY:MM:DD HH:MM:SS")
	f = open(text_file, "a+")
	f.write(str("date format not correct in \"tag.ini\", Date format should be: YYYY:MM:DD HH:MM:SS\n\n"))
	f.close()
	exit()

# apply the TIFF tag values
for fname in glob.glob(filepath + "/" + "*.tif"):
	name = os.path.basename(fname)
	print(name)
	filename = str("\"")+ fname + str("\"")
	exif_com = "exiftool.exe" + " " + "-Make="+ scanner + " "  + "-Model="+ scannermodel + " "  + "-Software="+ software + " "  + "-Artist="+ artist + " " + "-documentname="+ title + " " + filename + " " + "-overwrite_original"
	subprocess.call(exif_com)

# apply the TIFF Date tag value
for fname in glob.glob(filepath + "/" + "*.tif"):
	name = os.path.basename(fname)
	filename = str("\"")+ fname + str("\"")
	if date1 == str("\"\""):
		break
	else:
		print(name, ": Adding Date tag")
		exif_dat = "exiftool.exe" + " " + "-modifydate="+ date1 + " " + filename + " " + "-overwrite_original"
		subprocess.call(exif_dat)

# apply the tag values in JPG file
for fname in glob.glob(filepath + "/" + "*.jpg"):
	name = os.path.basename(fname)
	print(name)
	filename = str("\"")+ fname + str("\"")
	exif_jpg = "exiftool.exe" + " " + "-Make="+ scanner + " "  + "-Model="+ scannermodel + " "  + "-Software="+ software + " "  + "-Artist="+ artist + " " + "-documentname="+ title + " " + filename + " " + "-overwrite_original"
	subprocess.call(exif_jpg)

# apply the Date tag value in JPG file
for fname in glob.glob(filepath + "/" + "*.jpg"):
	name = os.path.basename(fname)
	filename = str("\"")+ fname + str("\"")
	if date1 == str("\"\""):
		break
	else:
		print(name, ": Adding Date tag")
		exif_jpgdate = "exiftool.exe" + " " + "-modifydate="+ date1 + " " + filename + " " + "-overwrite_original"
		subprocess.call(exif_jpgdate)
