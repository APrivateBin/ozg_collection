# Log

2023.11.23: finish data_raw.csv

# About Dataset

## Source

音乐网站Zvyki（https://zvyki.com/）。

以Иван Ожогин为歌手关键词进行搜索，共26页（https://zvyki.com/artist/348701-Ivan_Ozhogin/page/1/ - https://zvyki.com/artist/348701-Ivan_Ozhogin/page/26/）。

抓取时间：2023.11.23

## Summary

共1300首，含歌词或注释363首。

范围为Капелька добра (мисс Лучезарная) - Чикаго（3567361） - Твои глаза зеленые（209370431）

## Columns

### data_raw.csv

**dataId: **网站对应歌曲id。

**dataLyricsId: **网站对应歌词id，无歌词时为'false'。

**title: **歌曲标题。

**lyrics: **歌曲歌词，包括歌词或注释，如日期、场次。

**link: **下载直链。

**linkPage: **Zvyki歌曲页面。

**time: **歌曲时长。

# About Code

### text/

加载全部lyrics后各页对应html代码块。

若网站有更新：

1. 点击全部**text**按键（加载lyrics内容）；
2. 拷贝网页源代码，或仅拷贝新增歌曲部分（建议使用Chrome DevTools）。

### zvyki.py & zvyki.ipynb

**不含网页爬取，仅含数据处理。**

Python及Jupyter Notebook版。内容功能无差别。