try:
	import argparse, sys, urllib, os

	print """


           __          __  _     ______ _     _
           \ \        / / | |   |  ____(_)   | |
   ______   \ \  /\  / /__| |__ | |__   _ ___| |__    ______
  |______|   \ \/  \/ / _ \ '_ \|  __| | / __| '_ \  |______|
              \  /\  /  __/ |_) | |    | \__ \ | | |
               \/  \/ \___|_.__/|_|    |_|___/_| |_|

	    A Website Cloner Written By NSK B3
	    	      Original Software
"""
	def cli():
		global args
		parser = argparse.ArgumentParser()
		parser.add_argument('-u', '--url', help="URL To Clone")
		args = parser.parse_args()
	class cloner:
		def __init__(self):
			#Initalize Object
			pass
		@classmethod
		def GetCode(self, site):
			global site_code
			self.site = site
			r = urllib.urlopen(self.site)
			site_code = r.read()
			return site_code
		@classmethod
		def WriteCode(self, realcode):
			self.realcode = site_code
			os.chdir('/var/www/html')
			f = open('index.html', 'w')
			f.write(str(self.realcode))
		@classmethod
		def StartApacheWebServer(self):
			os.system('apachectl start')
	def StartCloner():
		cloner.GetCode(args.url)
		cloner.WriteCode(site_code)
		cloner.StartApacheWebServer()
	cli()
	StartCloner()
except Exception as e:
	print e
	quit()
