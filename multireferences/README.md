# Multireferences

This directory houses the datasets used for our recently published paper [Style-agnostic evaluation of ASR using multiple reference transcripts](https://arxiv.org/abs/2412.07937). Each of these includes two different transcripts produced by Rev transcriptionists. For more information on each of the test suites, click into the subdirectory where you can find specifics about each in their respective READMEs.

## Creation of FSTs
In our paper, we discuss using [fstalign](https://github.com/revdotcom/fstalign/tree/develop) with FST files as the references. We created a script to facilitate the creation of FSTs from side-by-side files, available [here](https://github.com/revdotcom/fstalign/tree/develop/tools/sbs2fst.py). For more information on how to use FSTs with fstalign check out [the documentation we've provided](https://github.com/revdotcom/fstalign/tree/develop/tools#sbs2fstpy).

# Cite this data
The paper describing our methods and results can be found on arXiv at https://arxiv.org/abs/2412.07937.

Each of the subdirectories have their own different citation specifications. If you use the data in them, please check the READMEs within the subdirectories.
If you'd like to use the tools from this paper please cite:
```
@misc{mcnamara2024styleagnosticevaluationasrusing,
      title={Style-agnostic evaluation of ASR using multiple reference transcripts}, 
      author={Quinten McNamara and Miguel Ángel del Río Fernández and Nishchal Bhandari and Martin Ratajczak and Danny Chen and Corey Miller and Migüel Jetté},
      year={2024},
      eprint={2412.07937},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.07937}, 
}
```
