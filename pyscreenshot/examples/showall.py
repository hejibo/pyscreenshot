from pyscreenshot.backendloader import BackendLoader
from pyscreenshot.loader import PluginLoaderError
import pyscreenshot as ImageGrab
import time
from entrypoint2 import entrypoint

@entrypoint
def show():
    im=[]
    
    backends = BackendLoader().all_names
    for x in backends:
        BackendLoader().force(x)
        try:
            im.append(ImageGrab.grab(bbox=(100,200,300,400)))
            print 'grabbing by '+x
        except PluginLoaderError as e:
            print e
            
    for x in im:
        x.show()
        time.sleep(1)

