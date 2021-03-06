# -*- coding: utf-8 -*-
from .pluginbase import PluginBase

import urllib.request, urllib.error, urllib.parse
import re

class Course(PluginBase):
	def __init__(self, bot):
		bot.registerCommand("!course", self.handleCourse)
		bot.registerCommand("!kurs", self.handleCourse)
		bot.addHelp("kurs", "Usage: !kurs <kurskod>")

	def handleCourse(self, bot, channel, params):
		bot.sendMessage("PRIVMSG", channel, self.getCourse("%20".join(params)))

	def getCourse(self, courseCode):
		courseCode = courseCode.upper()
		if len(courseCode) != 6:
			return "Invalid course code"

		try:
			url = "http://www.ltu.se/edu/course/%s/%s?ugglanCat=student" % (courseCode[:3], courseCode)
			f = urllib.request.urlopen(url)
			data = f.read().decode('iso-8859-1')
			f.close()
		except urllib.error.HTTPError as e:
			return "Error: %s" % e.code

		m = re.search("<title>\n?(.*)\n?</title>", data)
		if m:
			return "%s : %s" % (m.group(1), url)
		return "Course not found"

mainclass = Course
