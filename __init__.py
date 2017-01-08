import os
import shutil
from sw import *

class Command:
    def on_save_pre(self, ed_self):
        pass
        #  
        fn = file_get_name(FILENAME_CURRENT)
        if not fn:
            msg_box(BEEP_WARN)
            return
        
        base_file = os.path.basename(fn)
        print("fn: %s" % (fn))
        print("base: %s" % (base_file))
        # target_file = "%s%s" % (backup_dir,base_file)
        dest = os.path.join("c:\\", "me2008", "backup", base_file)
        print("save: %s" % (dest))
        #msg_status('Backup: '+target_file)
        #print('Backup: %s' % (target_file))
        # Backup: c:\me2008\backup\derived.classes.cpp
        shutil.copyfile(base_file, dest)

