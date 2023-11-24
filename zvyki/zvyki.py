import pandas as pd
from bs4 import BeautifulSoup

def getInfo(song):
    '''
    extract information from the html block of a song

    Parameters
    ----------
    song : bs4.element
        html block of a song

    Returns
    ----------
    dataId : str
        data-id of the song
    dataLyricsId : str
        data-lyrics-id of the song
    link : str
        download link to the mp3 file
    linkPage : str
        link to the song's webpage on zvyki
    lyrics : str
        lyrics of the song
    title : str
        title of the song
    time : str
        time of the song

    '''
    dataId=song.get('data-id')
    dataLyricsId=song.get('data-lyrics-id')
    link=song.get('data-mp3')
    linkPageRaw=song.find('div',class_='playlist-title').find('a').get('href')
    linkPage='zvyki.com'+linkPageRaw
    lyricsRaw=song.find('div',class_='playlist-lyrics')
    if lyricsRaw is None:
        lyrics=''
    else:
        lyrics=lyricsRaw.text
    title=song.find('span',class_='ctitle').text
    timeRaw=song.find('em').find_all('a')[-1].next_sibling
    if timeRaw is None:
        time=''
    else:
        time=timeRaw.text.replace('\t','').replace('\n','')
    return dataId,dataLyricsId,link, linkPage,lyrics, title, time

dataIdList=[]
dataLyricsIdList=[]
linkList=[]
linkPageList=[]
lyricsList=[]
titleList=[]
timeList=[]

for i in range(1, 27):
    filePath='text/p'+str(i)+'.txt'
    with open(filePath,'r',encoding='utf-8') as f:
        html_text=f.read()
    html_soup=BeautifulSoup(html_text,'html.parser')
    html_songlist=html_soup.find_all('li',class_='track')
    for song in html_songlist:
        dataId,dataLyricsId,link, linkPage,lyrics, title, time=getInfo(song)
        dataIdList.append(dataId)
        dataLyricsIdList.append(dataLyricsId)
        linkList.append(link)
        linkPageList.append(linkPage)
        lyricsList.append(lyrics)
        titleList.append(title)
        timeList.append(time)

data_raw=pd.DataFrame({'dataId':dataIdList,'dataLyricsId':dataLyricsIdList,'title':titleList,'lyrics':lyricsList,'link':linkList,'linkPage':linkPageList,'time':timeList})
data_raw.to_csv('data_raw.csv',index=False,encoding='utf-8-sig')