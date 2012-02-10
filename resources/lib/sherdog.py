#!/usr/bin/env python

import os
import xbmc
import xbmcaddon
import xbmcvfs

from BeautifulSoup import BeautifulSoup
from resources.lib.utils import *

__addon__             = xbmcaddon.Addon()
__addondir__          = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__fighterDir__        = os.path.join(__addondir__, 'fighters')

def getEventDetails(sherdogEventID):
	return SherdogScraper(xbmc).getEventDetails(sherdogEventID)

def getFighterDetails(sherdogFighterID):
	fighter = SherdogScraper(xbmc).getFighterDetails(sherdogFighterID)
	fighterThumb = fighter['ID'] + '.jpg'
	thumbPath = os.path.join(fighterDir, fighterThumb)
	if not xbmcvfs.exists(thumbPath):
		thumbUrl = soup.find("span", {"id" : "fighter_picture"}).img['src']
		if not thumbUrl == 'http://www.cdn.sherdog.com/fightfinder/Pictures/blank_fighter.jpg':
			downloadFile(thumbUrl, thumbPath)
	
	return fighter
