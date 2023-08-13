'''
python Built-in Modules

module..?
يعني 
هو عبر عن مكتبات موجوده في الغاء يمكان ان تستخدمه
import عن طريق  

ومن المكتبات المستخدمه بي كثره هي 
os
للعمل مصار لي الملف موجود منته حباب تستخدمه


ولو عمز اكريت ملف الجديد 
os.mkdir("السم الملف") بعمل 



في طريقه للعمل المكتابه الستدع 
الاول 
import  ملحوظه ان الطريق ده بجيب كل ما في المكتبه          وبعدين اسم المكتبه             

الثاني
from  اسم المكتبه import  الجزء المفرود استخدمه
from os import mkdir
كد نا بقول عوز الجزء ده بس من المكتبه

'''

'''
install module
يعني لعوز احميل مكتبات جديده

محج 
pip 
pip الحجات المستخدمه في 
Usage:
  pip <command> [options]

Commands:
    install                     Install packages.
    download                    Download packages.
    uninstall                   Uninstall packages.
    freeze                      Output installed packages in requirements format.
    inspect                     Inspect the python environment.
    list                        List installed packages.
    show                        Show information about installed packages.
    check                       Verify installed packages have compatible dependencies.
    config                      Manage local and global configuration.
    search                      Search PyPI for packages.
    cache                       Inspect and manage pip's wheel cache.
    index                       Inspect information available from package indexes.
    wheel                       Build wheels from your requirements.
    hash                        Compute hashes of package archives.
    completion                  A helper command used for command completion.
    debug                       Show information useful for debugging.
    help                        Show help for commands.

'''

# Renaming & Deleting Files
# يعني اعمل تعديل علي اسم الملف او حزف الملف 
'''
للعمل تعديل 
import os 

os.rename(" السم الجديد " , "السم القديم")

لحذف الملف 
os.remove(السم الملف)

Directories pythonاسم الملف في ال

للضف الملف جديد 
os.mkdir("اسم الملف )

لو عوز انتقل من الملف الي الملف 
os.chdir("اسم الملف المفروض انتقل في")


لو عوز اجيب المكان الذي نا في 
os.getcwd()    مابيختش حجه



'''

import os

os.getcwd()

# os.mkdir("hasan")
# os.remove('hasan')

