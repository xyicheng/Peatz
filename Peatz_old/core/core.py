import os
import settings
import threading
import importlib as il

from peatz.core.const import *
from peatz.core.template import TemplateManager

######################
#   Framework Core   #
######################
class Core(Object):
    
    def __init__(self):
        from core.data import ThreadCollection
        self.launched_apps = ThreadCollection({})
    
    def launch(self, argv):
        try:
            if len(argv) > 1:
                if len(argv) > 2:
                    getattr(self, argv[1])(argv[2:])
                else:
                    getattr(self, argv[1])([])
            else:
                self.console();
        except Exception as e:
            print(e)

    def console(self):
        print('Console management :');
        cmd = ''
        while(cmd != 'exit'):
            if cmd != '':
                self.launch(['manage.py'] + cmd.split(' '))
            cmd = input('>>> ')
        print('Stoping... Bye !')

    def start(self, args):
        base_name = args[0] if len(args) else settings.PROJECT['main']
        app_main = Application.get_app_main(base_name);
        if os.path.isfile(app_main):
            application = Application.launch(base_name)
            th = threading.Thread(target=application,name=base_name)
            self.launched_apps.add(th).start(base_name)
            return True
        else:
            print('Error : ' + app_main + ' doesn\'t exists')
            return False
            
    def create(self, args):
        base_name = args[0]
        print('Creating directory ' + Application.get_app_dir(base_name))
        os.makedirs(Application.get_app_dir(base_name))
        os.makedirs(Application.get_app_dir(base_name) + DS + 'model')
        os.makedirs(Application.get_app_dir(base_name) + DS + 'view')
        os.makedirs(Application.get_app_dir(base_name) + DS + 'controller')
        os.makedirs(Application.get_app_dir(base_name) + DS + 'assets')
        print('Creating file ' + Application.get_app_main(base_name))
        main = open(Application.get_app_main(base_name), 'w')
        settings = open(Application.get_app_dir(base_name) + 'settings.py', 'w')
        mainviewcontroller = open(Application.get_app_dir(base_name) + 'controller' + DS + 'MainViewController.py', 'w')
        main.write(TemplateManager.fill_main(base_name))
        settings.write(TemplateManager.fill_settings(base_name))
        mainviewcontroller.write(TemplateManager.fill_mainviewcontroller())
        main.close()
        settings.close()
        print('Done.')
        return True

###########################
# Applications base class #
###########################
class Application(Object):
    
    @staticmethod
    def get_app_name(app_name):
        return settings.PROJECT['app_prefix'] + app_name;
    
    @staticmethod
    def get_app_mod(app_name):
        return settings.PROJECT['main_prefix'] + app_name;
    
    @staticmethod
    def get_app_dir(app_name):
        return PROJECT_DIR + DS + Application.get_app_name(app_name) + DS
    
    @staticmethod
    def get_app_main(app_name):
        return Application.get_app_dir(app_name) + settings.PROJECT['main_prefix'] + app_name + '.py';
    
    @staticmethod
    def load_app(app_name):
        app_dir = Application.get_app_dir(app_name)
        if os.path.isdir(app_dir):
            import sys
            #sys.path.append(app_dir);
        else:
            return false;
    
    @staticmethod
    def exists(base_name):
        return os.path.isdir(Application.get_app_dir(base_name))
    
    @staticmethod
    def launch(base_name):
        app_name = Application.get_app_name(base_name);
        app_mod = Application.get_app_mod(base_name);
        return getattr(getattr(__import__(app_name + '.' + app_mod), app_mod), base_name[0].upper() + base_name[1:] + 'Application')
    
    def __init__(self, name):
        from core.data import ViewControllerCollection
        self.app_name = Application.get_app_name(name.lower());
        self.app_mod = Application.get_app_mod(name.lower());
        self.settings = il.import_module(self.app_name + '.settings')
        self.name = self.settings.APPLICATION['app_name'] if 'app_name' in self.settings.APPLICATION else self.name
        self.views = ViewControllerCollection({})
    
    def start(self):
        self.render(self.settings.APPLICATION['starting_viewcontroller'])
        
    def render(self, vc_name):
        if vc_name[-10:] != 'Controller' :
            vc_name = vc_name + 'Controller'
        viewcontroller = getattr(il.import_module(self.app_name + '.controller.' + vc_name), vc_name)
        view = getattr(il.import_module(self.app_name + '.view.' + vc_name[:-10]), vc_name[:-10])
        self.views.add(viewcontroller(view()))
        self.views.last.before()
        self.views.last.render()
        self.views.last.after()
        
    def __str__(self):
        return self.name;