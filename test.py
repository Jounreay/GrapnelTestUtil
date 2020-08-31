import os
import glob
import re
import zipfile
import pathlib as Path
zip = re.compile('.*\.zip')
newlbxid = input('New lbxid: ')
oldlbxid = input('Old lbxid: ')
oldtif = re.compile('.+%s.*\.tif' % oldlbxid)
newtif = re.compile('.+%s.*\.tif' % newlbxid)

rootdir = r'C:\Users\Joshua Reid\Desktop'


def scan():

    files = os.listdir(rootdir)
    zipfiles = list(filter(zip.match, files))
    for f in zipfiles:
        if f != '':
            zipfiles = Path.Path(rootdir + '\\' + f)
            rename(zipfiles, newlbxid, oldlbxid)


def rename(zipfiles,newlbxid,oldlbxid):

    with zipfile.ZipFile(zipfiles, 'r') as f:
        if f != '':
            f.extractall(rootdir+'\\')

        files = os.listdir(rootdir)
        files_torename = list(filter(oldtif.match, files))
        for f in files_torename:
            print('Found %s.' % f)
            renamed_file = f.replace(oldlbxid, newlbxid)
            os.rename(rootdir+'\\'+f, rootdir+'\\'+renamed_file)
            print('Tif renamed from %s to %s' % (f, renamed_file))
            zf = zipfile.ZipFile('PID_%s.zip' % newlbxid, mode='w')
        files_torezip = list(filter(newtif.match, newlbxid))
        for z in files_torezip:
            print('Rezipping %s.' % z)
            zipfile.ZipFile('PID_%s.zip' % newlbxid, mode='w').write(z)
            zipfile.ZipFile('PID_%s.zip' % newlbxid, mode='w').close()







if __name__ == '__main__':
    scan()

