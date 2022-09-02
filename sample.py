import time
import requests
from time import sleep
from clicknium import clicknium as cc, locator

def main():
    cc.chrome.open("https://www.instagram.com/explore/")
    cc.find_element(locator.chrome.instagram.searchbox).set_text("#check",'sendkey-after-click')
    sleep(3)
    cc.send_hotkey('{ENTER}')
    sleep(3)
    cc.send_hotkey('{ENTER}')

    cc.find_element(locator.chrome.instagram.firsTthumbnail).click()
    downloadPic()
    cc.wait_appear(locator.chrome.instagram.nextPic)
    cc.find_element(locator.chrome.instagram.nextPic).click()
    i=0
    while cc.is_existing(locator.chrome.instagram.nextPic) and i < 10:
        downloadPic()
        cc.find_element(locator.chrome.instagram.nextPic).click()
        i = i+1

def downloadPic():
    uielements = cc.find_elements(locator.chrome.instagram.pic)
    print(len(uielements))
    for pic in uielements:
        path = pic.get_property("src")
        r = requests.get(path)
        sleep(3)
        dirname="insimg"
        imgname= time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        filename = '%s/%s.jpg' % (dirname, imgname)
        if r.status_code == 200:
            with open(filename,'wb') as f:
                f.write(r.content)
        else:
            print("failed to download")


    
if __name__ == "__main__":
    main()
