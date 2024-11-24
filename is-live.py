#!/usr/bin/env python
import requests
import argparse

# https://stackoverflow.com/a/76441100
def isChannelLive(username):
    html = requests.get("https://www.twitch.tv/" + username).text
    return ('isLiveBroadcast'in html)

def areChannelsLive(usernames):
    res = list()
    for username in usernames:
        name = username.strip()
        res.append(isChannelLive(name))

    return res

def areChannelsLiveFromFile(file_path):
    f = open(file_path, "r")
    names = list(filter(bool, f.read().splitlines()))
    f.close()

    return areChannelsLive(names)

parser = argparse.ArgumentParser()
parser.add_argument('channel_name', nargs='*', type=str, help='Check channel')
parser.add_argument('-f', type=str, help='Path to a txt file of channel names seperated by a newline')
args = parser.parse_args()

if args.f != None:
    file_path = args.f if args.f.endswith(".txt") else args.f + ".txt"

    f = open(file_path, "r")
    names = list(filter(bool, f.read().splitlines()))
    f.close()

    res = areChannelsLive(names)

    for str, result in zip(names, res):
        name = str.strip()
        print(name + " is live" if result else name + " not live")


if args.channel_name != None:
    for str in args.channel_name:
        name = str.strip()
        print(name + " is live" if isChannelLive(name) else name + " not live")
