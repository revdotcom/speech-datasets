[![License: CC BY--NCSA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE.md)

# multi-coraal
The multi-coraal dataset is a 10-hour subset of [CORAAL](https://oraal.uoregon.edu/coraal) that has been re-transcribed several times by humans. This corpus is intended to provide the research community insight into evaluation bias caused by human transcription styles.

# Table of Contents
* [Cite this Dataset](#cite-this-dataset)

# Tooling
For purposes of alignment and WER cal [fstalign](https://github.com/revdotcom/fstalign/tree/master) tool. We strongly recommend the use of this tool to quickly get started using the *Earnings-21* dataset.

To find the recordings we used for this work, see the [DataSelection Jupyter Notebook](https://github.com/revdotcom/speech-datasets/blob/main/coraal-multi/code/DataSelection.ipynb) which shows our data selection process as well as the files that we ultimately selected for transcription. The audios can then be downloaded from the offical [CORAAL](https://oraal.uoregon.edu/coraal) website.


# Cite this Dataset
This dataset has been accepted to Interspeech 2024.
The paper describing our methods and results can be found on [ArXiv](https://arxiv.org/abs/2409.03059), and on the [ISCA Archive](https://www.isca-archive.org/interspeech_2024/heuser24_interspeech.html).

If you use work please cite the following:
## Text Citation
```
Heuser, A., Kendall, T., del Rio, M., McNamara, Q., Bhandari, N., Miller, C., Jetté, M. (2024) Quantification of stylistic differences in human- and ASR-produced transcripts of African American English. Proc. Interspeech 2024, 4538-4542, doi: 10.21437/Interspeech.2024-2300
Kendall, Tyler and Charlie Farrington. 2023. The Corpus of Regional African American Language. Version 2023.06. Eugene, OR: The Online Resources for African American Language Project. [https://doi.org/10.7264/1ad5-6t35]
```

## BibTex Citation
```
@inproceedings{heuser24_interspeech,
  title     = {Quantification of stylistic differences in human- and ASR-produced transcripts of African American English},
  author    = {Annika Heuser and Tyler Kendall and Miguel {del Rio} and Quinn McNamara and Nishchal Bhandari and Corey Miller and Migüel Jetté},
  year      = {2024},
  booktitle = {Interspeech 2024},
  pages     = {4538--4542},
  doi       = {10.21437/Interspeech.2024-2300},
}
@article{kendall2018corpus,
  title={The corpus of regional {A}frican {A}merican {L}anguage},
  author={Kendall, Tyler and Farrington, Charlie},
  journal={Version 2023.06},
  year={2023}
}
```
