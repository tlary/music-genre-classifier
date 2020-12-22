import pandas as pd
import json
from fastai.text.all import *

# load data from json file into pandas dataframe
with open('Lyrics_KoolSavas.json') as json_data:
    data = json.load(json_data)
df = pd.DataFrame(data['songs'])

