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


def main(wholeLinkInfo, linkUrl):
    video_url = linkUrl
    soundDir = pathOutput + destination_control(wholeLinkInfo["Type"], wholeLinkInfo["Gender"],
                                                    wholeLinkInfo["Language"])
    if not os.path.isdir(soundDir):
        os.makedirs(soundDir)

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name + '.mp4'
    renametomp3 = soundDir + hashName + '.mp3'

    if os.name == 'nt':
        os.system('ren {0} {1}'. format(location, renametomp3))
    else:
        os.system('mv {0} {1}'. format(location, renametomp3))


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
            main(dictionaryLink, dictionaryLink["URL"])
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
