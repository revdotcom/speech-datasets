[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE.md)

# Earnings 22

The Earnings 22 dataset ( also referred to as earnings22 ) is a 119-hour corpus of English-language earnings calls collected from global companies. The primary purpose is to serve as a benchmark for industrial and academic automatic speech recognition (ASR) models on real-world accented speech.

This work has been submitted for publication at Interspeech 2022.

# Table of Contents

* [File Format Overview](#file-format-overview)
  + [nlp Files](#nlp-files)
    - [Example](#example-nlp-file)
* [Results](#results)
* [WER Calculation](#wer-calculation)
* [Cite this Dataset](#cite-this-dataset)

# File Format Overview
In the following section, we provide an overview of the file formats we provide with this dataset.

## nlp Files
NLP files are `.csv` inspired, pipe-separated text files that contain token and metadata information of a transcript. Each line of a file represents a single transcript token and the metadata associated with it.

|Column Title|Description
|--|--|
| Column 1: `token` | A single token in the transcript. These are typically single words or multiple words with hyphens in between. |
| Column 2: `speaker` | A unique integer that associates this token to a specific speaker in an audio |
Column 3: `ts`          |     A float representing the start time of the token, in seconds |
Column 4: `endTs`       |     A float representing the end time of the token, in seconds |
Column 5: `punctuation` |     A punctuation character that is included at the end of a token that is used when reconstructing the transcript. Example punctuation: `",", ";", ".", "!"`. |
Column 6: `case`  | A two letter code to denominate the which of four possible casings for this token: <ul><li>`UC` - Denotes a token that has the first character in uppercase and every other character lowercase.</li><li>`LC` - Denotes a token that has every character in lowercase.</li><li>`CA` - Denotes a token that has every character in uppercase.</li><li>`MC` - Denotes a token that doesnâ€™t follow the previous rules. This is the case when upper- and lowercase characters are mixed throughout the token</li></ul> |
Column 7: `tags`        |     Displays one of the several entity tags that are listed in wer_tags in long form - such that the displayed entity here is in the form `ID:ENTITY_CLASS`. |
Column 8: `wer_tags`    |     A list of entity tags that are associated with this token. In this field, only entity IDs should be present. The specific ENTITY_CLASS for each ID can be extracted from an accompanying wer_tags sidecar json. |

_**Note that each entity ID is unique to that specific entity. Entities can be comprised of single and multiple tokens. Within a file there can be several entities of the same ENTITY_CLASS but only one entity can be labeled with any given ID.**_


### Example nlp File
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

# Results
Tables found in the paper along with all entity class WER can be found within the `transcripts` directory.

# WER Calculation
All of our analysis on this dataset is done through the use of our newly released [fstalign](https://github.com/revdotcom/fstalign/tree/master) tool. We strongly recommend the use of this tool to quickly get started using the *Earnings-22* dataset.

# Cite this Dataset
This dataset has been submitted to Interspeech 2022.
The paper describing our methods and results can be found on arXiv at https://arxiv.org/abs/2203.15591.
```
@misc{https://doi.org/10.48550/arxiv.2203.15591,
  doi = {10.48550/ARXIV.2203.15591},
  url = {https://arxiv.org/abs/2203.15591},
  author = {Del Rio, Miguel and Ha, Peter and McNamara, Quinten and Miller, Corey and Chandra, Shipra},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Earnings-22: A Practical Benchmark for Accents in the Wild},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution Share Alike 4.0 International}
}
```
