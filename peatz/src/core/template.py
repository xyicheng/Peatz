from core.const import *

TEMPLATE_APP_START = TEMPLATES + 'app_start.ptz'
TEMPLATE_APP_SETTINGS = TEMPLATES + 'app_settings.ptz'
TEMPLATE_APP_MAINVIEWCONTROLLER = TEMPLATES + 'app_mainviewcontroller.ptz' 

class TemplateManager:
			
	@staticmethod
	def fill_main(app):
		return open(TEMPLATE_APP_START, 'r').read().replace('<%FORMATED_APP_NAME%>', app[:1].capitalize() + app[1:].lower())
		
	@staticmethod
	def fill_settings(app):
		return open(TEMPLATE_APP_SETTINGS, 'r').read().replace('<%FORMATED_APP_NAME%>', app[:1].capitalize() + app[1:].lower())
	
	@staticmethod	
	def  fill_mainviewcontroller():
		return open(TEMPLATE_APP_MAINVIEWCONTROLLER, 'r').read()