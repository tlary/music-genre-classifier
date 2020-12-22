from dotenv import load_dotenv
import os
import lyricsgenius as lg
import pandas as pd
from pandas.io.json import json_normalize
import json
from fastai.text.all import *

# load environment variables
# requires CLIENT_ACCESS_TOKEN from genius API
load_dotenv()

# initiate genius
token = os.getenv("CLIENT_ACCESS_TOKEN")
genius = lg.Genius(token, remove_section_headers=True, skip_non_songs=True)

# search for songs

# hip hop
artist_kks = genius.search_artist("Kool Savas", get_full_info=False)
artist_samy = genius.search_artist("Samy Deluxe", get_full_info=False)
artist_capi = genius.search_artist("Capital Bra", get_full_info=False)

# schlager
artist_helene = genius.search_artist("Helene Fischer", get_full_info=False)
artist_wolle = genius.search_artist("Wolfgang Petry", get_full_info=False)
artist_reim = genius.search_artist("Matthias Reim", get_full_info=False)

# Pop
artist_silbermond = genius.search_artist("Silbermond", get_full_info=False)
artist_herbert = genius.search_artist("Herbert Grönemeyer", get_full_info=False)
artist_mark = genius.search_artist("Mark Forster", get_full_info=False)

# save the lyrics to disk
artist_kks.save_lyrics()
artist_samy.save_lyrics()
artist_capi.save_lyrics()
artist_silbermond.save_lyrics()
artist_herbert.save_lyrics()
artist_mark.save_lyrics()
artist_wolle.save_lyrics()
artist_helene.save_lyrics()
artist_reim.save_lyrics()

# load data from json files into pandas dataframe
dfList = list()
for file in os.listdir():
    if file.endswith(".json"):
        artist = file.replace("Lyrics_", "")
        artist = artist.replace(".json", "")
        with open(file) as json_data:
            data = json.load(json_data)
        df = pd.DataFrame(data["songs"])
        if artist in ["KoolSavas", "SamyDeluxe", "CapitalBra"]:
            genre = "hiphop"
        elif artist in ["HeleneFischer", "WolfgangPetry", "MatthiasReim"]:
            genre = "schlager"
        elif artist in ["Silbermond", "HerbertGrönemeyer", "MarkForster"]:
            genre = "pop"
        df["genre"] = genre
        dfList.append(df)
    else:
        continue
finalDF = pd.concat(dfList)
lyrics = finalDF[["lyrics", "genre"]]
notNone = lyrics.notnull()
lyrics = lyrics[notNone]

# save lyrics data to disk as .csv file
lyrics.to_csv("/home/tlary/PycharmProjects/LyricizeApp/lyrics.csv")