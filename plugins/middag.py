# -*- coding: utf-8 -*-
from pluginbase import PluginBase

from bs4 import BeautifulSoup
import urllib
import re

class Middag(PluginBase):
	f __init__(self, bot):
		bot.registerCommand("!dinner", self.handleMiddag)
		bot.registerCommand("!middag", self.handleMiddag)
		bot.addHelp("dinner", "Usage: !dinner")

	def handleMiddag(self, bot, channel, params):

		try:
			url = "http://vadfanskajaglagatillmiddag.nu"
			data = urllib.urlopen(url).read()
			soup = BeautifulSoup(data)

			recept_url = soup.find('a', href=True)['href']
			recept_url = recept_url.encode('utf-8')

			mat = soup.find('a')
			mat = mat.contents[0]
			mat = mat.encode('utf-8')

			print recept_url
			print mat

			bot.sendMessage("PRIVMSG", channel, '%s - %s' % (mat, recept_url))
		except:
			bot.sendMessage("PRIVMSG", channel, "Something went wrong.")

mainclass = Middag