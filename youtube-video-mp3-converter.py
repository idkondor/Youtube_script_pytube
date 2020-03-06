#!/usr/bin/env python3
from __future__ import unicode_literals
import secrets
import time
import random
from argparse import ArgumentParser
from pytube import YouTube
import pytube
import os

parser = ArgumentParser()
parser.add_argument("-i", "--docIn", dest="pathToDoc", help="Input folder path with links!")
parser.add_argument("-o", "--dirOut", dest="pathOutput", help="Input folder path to download!")
parser.add_argument("-d", "--docOut", dest="pathToDocOut", help="Input folder path for output links!")
args = parser.parse_args()
pathToDoc = args.pathToDoc
pathOutput = args.pathOutput
pathToDocOut = args.pathToDocOut


def destination_control(link_type, gender, language):
    path = link_type + '/' + gender + '/' + language + '/'
    if link_type == "Noise":
        return link_type + "/"
    else:
        return path


def videoConverter(sysCommand, mp4Location, mp3Location):
    os.system(f"{sysCommand} {mp4Location} {mp3Location}")
    os.system(f"ffmpeg -i '{mp3Location}' '{mp3Location.replace('mp4', 'mp3')}'")
    os.remove(mp3Location)


def videoDownloader(wholeLinkInfo, linkUrl):
    video_url = linkUrl
    soundDir = pathOutput + destination_control(wholeLinkInfo["Type"], wholeLinkInfo["Gender"],
                                                    wholeLinkInfo["Language"])
    if not os.path.isdir(soundDir):
        os.makedirs(soundDir)

    if os.name == 'nt':
        originAppPath = os.getcwd() + '\\'
    else:
        originAppPath = os.getcwd() + '/'

    videoName = pytube.extract.video_id(video_url)
    YouTube(video_url).streams.first().download(filename=videoName)
    mp4Location = originAppPath + videoName + '.mp4'
    mp3Location = soundDir + hashName + '.mp4'

    if os.name == 'nt':
        videoConverter('ren', mp4Location, mp3Location)
    else:
        videoConverter('mv', mp4Location, mp3Location)


with open(pathToDoc) as linksFile:
    linksDataType = linksFile.readline()
    linksDataContainer = linksFile.read()
    linksList = linksDataContainer.splitlines()
    linksDictionaryList = []
    for link in linksList:
        linksDictionaryList.append(dict(zip(linksDataType.split(","), link.split(","))))

linksSheet = open(pathToDocOut, "r+")
linksSheet.write("URL, Type, Gender, Language, Duration, Comments, Availability, MD5" + "\n")

for dictionaryLink in linksDictionaryList:
    print(dictionaryLink)
    hashName = secrets.token_hex(nbytes=16)
    try:
        if __name__ == '__main__':
            videoDownloader(dictionaryLink, dictionaryLink["URL"])
            dictionaryLink["Availability"] = "Valid"

    except:
        dictionaryLink["Availability"] = "INVALID!"

    linksDictValues = []
    dictItems = dictionaryLink.items()
    for value in dictItems:
        if value[0] == "MD5\n":
            linksSheet.write(hashName + "\n")
            break
        linksSheet.write(value[1] + ", ")
    print('Done downloading, now converting ...')
    time.sleep(random.randint(10, 30))

linksSheet.close()
