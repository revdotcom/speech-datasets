In this directory, you can find the transcripts for each recording including the corresponding entity labels and normalization files. Our results are generated using Rev's [fstalign](https://github.com/revdotcom/fstalign) algorithm by feeding in the files in `nlp_references` and the corresponding file in `normalizations`. In the returned, `.log.json` files, we find error information for each entity described in the corresponding `.wer_tag.json` in `wer_tags`.

# Results
The following table summarize results from our paper and adds more color to the entity specific WER.

## Overall

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Earnings21_|17.8|17.0|15.8|16.0|13.2|12.8|60.5|
|_Eval-10_|18.5|18.0|16.2|16.7|12.2|12.7|62.9|

## Entity

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Mean Entity_|30.4|28.8|20.7|28.8|19.6|18.8|55.9|24.5|
|ABBREVIATION|48.8|50.7|49.0|62.8|39.0|39.0|81.0|48.2|
|ALPHANUMERIC|30.5|45.3|15.5|30.2|15.2|12.8|60.9|24.9|
|CARDINAL|17.8|18.3|7.4|11.1|4.4|3.9|34.2|10.5|
|CONTRACTION|13.4|13.4|13.3|11.3|9.3|7.6|57.6|11.4|
|DATE|9.8|7.8|5.0|6.5|5.5|5.1|44.0|6.6|
|EVENT|12.2|66.2|20.9|17.6|7.7|4.6|66.2|21.6|
|FAC|40.7|40.0|34.8|44.1|36.1|46.2|63.6|40.3|
|GPE|22.5|21.1|25.6|26.8|26.1|22.8|62.4|24.2|
|LANGUAGE|50.0|50.0|50.0|50.0|100.0|50.0|100.0|58.3|
|LAW|27.0|22.2|14.9|30.2|11.6|12.1|51.5|19.7|
|LOC|8.8|8.0|9.6|9.5|12.8|14.3|39.9|10.5|
|MONEY|23.7|18.4|11.9|12.2|6.0|6.7|36.9|13.1|
|NORP|21.3|19.6|20.4|23.4|23.8|28.1|55.3|22.8|
|ORDINAL|7.3|8.3|7.6|8.6|8.2|5.0|40.1|7.5|
|ORG|35.9|39.9|35.6|44.3|32.5|36.0|74.7|37.4|
|PERCENT|49.7|13.3|11.5|26.1|3.3|2.8|44.7|17.8|
|PERSON|48.2|46.6|45.2|51.7|46.8|50.1|79.7|48.1|
|PRODUCT|40.5|42.8|32.7|53.0|34.9|40.3|66.9|40.7|
|QUANTITY|19.0|19.6|15.2|14.6|10.6|13.1|49.1|15.3|
|RANGE|79.0|88.2|11.9|40.0|0.0|0.0|26.8|36.5|
|TIME|10.0|7.9|6.5|9.0|10.0|6.0|47.8|8.2|
|TWITTER|25.0|0.0|25.0|33.3|0.0|0.0|50.0|13.9|
|WEBSITE|69.2|25.1|22.7|58.2|20.2|29.7|77.6|37.5|
|WORK_OF_ART|27.2|28.4|21.4|28.4|23.5|31.8|64.3|26.8|
|YEAR|21.6|19.9|3.2|16.4|1.6|1.9|22.7|10.8|
|AVERAGE|30.4|28.8|20.7|28.8|19.6|18.8|55.9|24.5|

## Sector

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Mean Sector_|17.8|17.1|15.8|16.0|13.2|12.8|60.5|
|Conglomerates|15.5|15.4|14.1|14.0|8.0|10.8|56.0|
|Utilities|15.9|15.9|14.8|14.2|10.3|11.7|58.2|
|Basic Materials|16.7|15.5|14.6|14.5|11.0|12.1|57.1|
|Services|16.8|16.6|14.8|15.2|11.5|11.8|56.5|
|Healthcare|17.1|17.1|15.6|16.0|11.0|12.4|57.0|
|Financial|18.0|17.0|15.6|15.5|13.2|12.7|61.4|
|Consumer Goods|18.7|17.3|16.0|16.1|12.1|12.3|62.2|
|Technology|20.6|18.9|17.1|17.4|16.0|14.4|66.3|
|Industrial Goods|21.2|20.0|19.3|21.0|25.9|16.8|69.4|

## Sampling Rate

||Google|Amazon|Microsoft|Speechmatics|Rev<br />Kaldi|Rev<br />ESPNet|Kaldi.org<br />Librispeech|
|--|--|--|--|--|--|--|--|
|_Mean Sample Rate_|18.1|17.5|16.2|16.4|14.5|13.3|60.7|
|44100|16.0|15.5|14.9|14.4|10.0|10.9|53.6|
|24000|17.3|16.3|15.0|15.2|11.3|12.1|61.2|
|22050|14.6|15.6|13.4|12.6|8.9|11.2|56.8|
|16000|22.9|21.1|20.4|22.3|28.1|17.7|68.5|
|11025|19.9|19.1|17.2|17.5|14.2|14.5|63.4|