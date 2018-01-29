import os,sys

os.chdir('D:\\screenshot')
for i in os.listdir(os.getcwd()):
    os.remove(os.getcwd()+'\\'+i)
