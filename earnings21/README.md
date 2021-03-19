# Table of Contents

* [File Format Overview](#format)
  * [nlp Files](#nlp)
    * [Example](#nlp_example)
  * [wer_tag JSON](#wer_tag)
    * [Example](#wer_tag_example)

* [Entity Labels](#entities)


# File Format Overview
<a name="format"/>
In the following section, we provide an overview of the file formats we provide with this dataset.

## nlp Files
<a name="nlp"/>
NLP files are `.csv` inspired, pipe-separated text files that contain token and metadata information of a transcript. Each line of a file represents a single transcript token and the metadata associated with it.

|Column Title|Description
|--|--|
| Column 1: `token` | A single token in the transcript. These are typically single words or multiple words with hyphens in between. |
| Column 2: `speaker` | A unique integer that associates this token to a specific speaker in an audio |
Column 3: `ts`          |     A float representing the second that start of the token's utterance |
Column 4: `endTs`       |     A float representing the second that end of the token's utterance |
Column 5: `punctuation` |     A punctuation character that is included at the end of a token that is used when reconstructing the transcript. Example punctuation: `",", ";", ".", "!"`. |
Column 6: `case`  | A two letter code to denominate the which of four possible casings for this token: <ul><li>`UC` - Denotes a token that has the first character in uppercase and every other character lowercase.</li><li>`LC` - Denotes a token that has every character in lowercase.</li><li>`CA` - Denotes a token that has every character in uppercase.</li><li>`MC` - Denotes a token that doesnâ€™t follow the previous rules. This is the case when upper- and lowercase characters are mixed throughout the token</li></ul> |
Column 7: `tags`        |     Displays one of the several entity tags that are listed in wer_tags in long form - such that the displayed entity here is in the form `ID:ENTITY_CLASS`. |
Column 8: `wer_tags`    |     A list of entity tags that are associated with this token. In this field, only entity IDs should be present. The specific ENTITY_CLASS for each ID can be extracted from an accompanying wer_tags sidecar json. |

_**Note that each entity ID is unique to that specific entity. Entities can be comprised of single and multiple tokens. Within a file there can be several entities of the same ENTITY_CLASS but only one entity can be labeled with any given ID.**_


### Example File
<a name="nlp_example"/>
`example.nlp`

```
token|speaker|ts|endTs|punctuation|case|tags|wer_tags
Good|0||||UC|[]|[]
morning|0||||LC|['5:TIME']|['5']
and|0||||LC|[]|[]
welcome|0||||LC|[]|[]
to|0||||LC|[]|[]
the|0||||LC|['6:DATE']|['6']
first|0||||LC|['6:DATE']|['6']
quarter|0||||LC|['6:DATE']|['6']
2020|0||||CA|['0:YEAR']|['0', '1', '6']
NexGEn|0||||MC|['7:ORG']|['7']
```

## wer_tag JSON
<a name="wer_tag"/>
The wer_tags sidecar JSON is used in combination with an nlp file and exclusively when that file is using the wer_tags column. It is used to provide entity information about each entity ID. It is formatted such that the JSON acts as a list of objects that map the ID of an entity to an object specifying the entity_type as the entity label. The object is formatted such that:

```
"ID":{
  "entity_type" : "LABEL"
}
```

### Example File
<a name="wer_tag_example"/>
`example.wer_tags.json`

```
{
  "0":{
    "entity_type" : "YEAR"
  },
  "1":{
    "entity_type" : "CARDINAL"
  },
  "5":{
    "entity_type" : "TIME"
  },
  "6":{
    "entity_type" : "DATE"
  },
  "7":{
    "entity_type" : "ORG"
  }
}
```

# Entity Labels
<a name="entities"/>
In the following table, we provide a list of all possible entity tags we provide in the dataset including a description of each tag and a few examples.

| Tags (Entity Classes) | Description | Examples |
| --------------------- | ----------- | -------- |
| PERSON |Names of people, including fictional people | Hagrid, Jason Chicola, W. E. B. Du Bois |
| NORP | Nationalities or religious or political groups | American, Chinese, Republican, Grand Old Party, Roman Catholic |
| FAC | Buildings, airports, highways, bridges, etc. | Golden Gate Bridge, the Empire State Building |
| ORG | Companies, agencies, institutions, etc. | Rev, General Motors, SEC, NAACP |
| GPE | Countries, cities, states, etc. Geopolitical entities. | Italy, US, Boston, New Zealand |
| LOC | Non-GPE locations, mountain ranges, bodies of water,etc. | the North, the Rocky Mountains |
| PRODUCT | Objects, vehicles, foods, etc. (not services) | Camry, Sufentanil, ARX-02 |
| EVENT | Named hurricanes, battles, wars, sports events, etc. | COVID-19, the Spanish Flu, Hurricane Katrina, World War II |
| WORK_OF_ART | Titles of books, songs, etc. | Frankenstein, The Mona Lisa |
| LAW | Named documents made into laws, etc. | Fox’s Act 1792, Article 5 of the Constitution |
| LANGUAGE | Any named language, etc. | Esperanto, Spanish, Swahili |
| DATE | Absolute or relative dates or periods, etc. | Q1, the end of last year |
| TIME | Times smaller than a day, etc. | Morning, 30 minutes |
| PERCENT | Percentage, including "%"', etc. | Approximately 10%, 5% |
| MONEY | Monetary values, including unit, etc. | $40 billion, 20 thousand pounds |
| QUANTITY | Measurements, as of weight or distance, etc. | 10 kilometers, approximately 80 tons |
| ORDINAL | "first", "second", etc. | Third, eighth, 4th |
| CARDINAL | Numerals that do not fall under another type, etc. | 20, fifty, 1420 |
| ABBREVIATION | An all-caps shortened form of a word or phrase where each letter represents a word. Specifically all Initialisms or Acronyms. | AFK (away from keyboard), RSU (restricted stock unit), FEMA |
| WEBSITE | A written out website | www.rev.com, indeed.com |
| YEAR | A 4 digit number representing a year | 2020, 2021 |
| CONTRACTION | A word or group of words resulting from shortening an original form OR can be transformed into a common form. | I’ll (I will), going to (gonna) |
| ALPHANUMERIC | A token that is comprised of letters and numbers | 8th, Q4 |
| FALLBACK | A word that does not conform to a normal word. This is usually words that contain an unknown symbol (like &) or words that were only partially spoken (like th-) | Q&M, lo- |
