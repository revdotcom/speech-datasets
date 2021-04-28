In this directory, you can find the transcripts for each recording including the corresponding entity labels and normalization files. Our results are generated using Rev's [fstalign](https://github.com/revdotcom/fstalign) algorithm by feeding in the files in `nlp_references` and the corresponding file in `normalizations`. In the returned, `.log.json` files, we find error information for each entity described in the corresponding `.wer_tag.json` in `wer_tags`.

# Results
The following table summarize results from our paper and adds more color to the entity specific WER.

## Overall

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Earnings21_|17.8|17.0|15.8|16.0|13.2|12.8|48.8|
|_Eval-10_|18.5|18.0|16.2|16.7|12.2|12.7|52.2|

## Entity

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Mean Entity_|30.4|28.8|20.7|28.8|19.6|18.8|48.9|
|ABBREVIATION|48.8|50.7|49.0|62.8|39.0|39.0|75.3|
|ALPHANUMERIC|30.5|45.3|15.5|30.2|15.2|12.8|53.4|
|CARDINAL|17.8|18.3|7.4|11.1|4.4|3.9|22.9|
|CONTRACTION|13.4|13.4|13.3|11.3|9.3|7.6|46.5|
|DATE|9.8|7.8|5.0|6.5|5.5|5.1|30.8|
|EVENT|12.2|66.2|20.9|17.6|7.7|4.6|62.9|
|FAC|40.7|40.0|34.8|44.1|36.1|46.2|60.2|
|GPE|22.5|21.1|25.6|26.8|26.1|22.8|54.9|
|LANGUAGE|50.0|50.0|50.0|50.0|100.0|50.0|100.0|
|LAW|27.0|22.2|14.9|30.2|11.6|12.1|39.4|
|LOC|8.8|8.0|9.6|9.5|12.8|14.3|33.3|
|MONEY|23.7|18.4|11.9|12.2|6.0|6.7|26.9|
|NORP|21.3|19.6|20.4|23.4|23.8|28.1|46.0|
|ORDINAL|7.3|8.3|7.6|8.6|8.2|5.0|33.4|
|ORG|35.9|39.9|35.6|44.3|32.5|36.0|68.8|
|PERCENT|49.7|13.3|11.5|26.1|3.3|2.8|42.6|
|PERSON|48.2|46.6|45.2|51.7|46.8|50.1|75.5|
|PRODUCT|40.5|42.8|32.7|53.0|34.9|40.3|61.5|
|QUANTITY|19.0|19.6|15.2|14.6|10.6|13.1|40.2|
|RANGE|79.0|88.2|11.9|40.0|0.0|0.0|10.2|
|TIME|10.0|7.9|6.5|9.0|10.0|6.0|39.3|
|TWITTER|25.0|0.0|25.0|33.3|0.0|0.0|50.0|
|WEBSITE|69.2|25.1|22.7|58.2|20.2|29.7|82.4|
|WORK_OF_ART|27.2|28.4|21.4|28.4|23.5|31.8|51.8|
|YEAR|21.6|19.9|3.2|16.4|1.6|1.9|13.5|

## Sector

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Mean Sector_|17.8|17.1|15.8|16.0|13.2|12.8|48.8|
|Conglomerates|15.5|15.4|14.1|14.0|8.0|10.8|44.1|
|Utilities|15.9|15.9|14.8|14.2|10.3|11.7|45.7|
|Basic Materials|16.7|15.5|14.6|14.5|11.0|12.1|43.6|
|Services|16.8|16.6|14.8|15.2|11.5|11.8|44.1|
|Healthcare|17.1|17.1|15.6|16.0|11.0|12.4|44.6|
|Financial|18.0|17.0|15.6|15.5|13.2|12.7|49.5|
|Consumer Goods|18.7|17.3|16.0|16.1|12.1|12.3|51.1|
|Technology|20.6|18.9|17.1|17.4|16.0|14.4|56.3|
|Industrial Goods|21.2|20.0|19.3|21.0|25.9|16.8|60.2|

## Sampling Rate

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Mean Sample Rate_|18.1|17.5|16.2|16.4|14.5|13.3|49.0|
|44100|16.0|15.5|14.9|14.4|10.0|10.9|40.5|
|24000|17.3|16.3|15.0|15.2|11.3|12.1|49.7|
|22050|14.6|15.6|13.4|12.6|8.9|11.2|43.3|
|16000|22.9|21.1|20.4|22.3|28.1|17.7|59.5|
|11025|19.9|19.1|17.2|17.5|14.2|14.5|52.2|
