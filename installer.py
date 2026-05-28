from pathlib import Path

print('Welcome to the Download Project Installer!')
folder = input('Please select a folder for the project: ')
Path(folder).mkdir(parents=True, exist_ok=True)
s = \
f'''
import requests as r
import sys

def __install(package):
    fd = '{folder}'
    url = 'https://github.com/Munder2/download.proj/raw/refs/heads/main/public/'+package
    resp = r.get(url)
    print('Getting the package . . .')
    if resp.status_code == 200:
        print('Success!\\nDownloading the package . . .')
        with open(fd+package, 'wb') as f:
            f.write(resp.content)
        print('Success!')
    else:
        print('Failed to get the package.\\nTry looking for errors in the enterred package name.'); sys.exit(1)

def installs(*packages):
    for pack in packages:
        __install(pack)

if __name__ == '__main__':
    try:
        if sys.argv[1] == '-d':
            __install(sys.argv[2])
        else:
            print('Usage: dl -d <package>'); sys.exit(1)
    except:
        print('Usage: dl -d <package>'); sys.exit(1)'''
open(folder+'/dl.py','w').write(s)
