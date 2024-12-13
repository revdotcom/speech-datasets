[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE.md)

# Rev16

The Rev-16 dataset ( also referred to as rev16 ) is a 16-hour corpus of English-language podcasts introduced by [Radford et al., 2023](https://proceedings.mlr.press/v202/radford23a.html).

The transcripts were created by Rev transcriptionists in two different styles, and are separated by subdirectory. The verbatim transcripts are created by the transcriptionists writing exactly what they hear, including filler words, stutters, interjections (active listening) and repetitions. The nonverbatim transcripts are created by lightly editing for readability without changing the structure or meaning of the speech.

For more information, see Rev's [Transcription Style Guide](https://cf-public.rev.com/styleguide/transcription/Transcription+Style+Guide+v5.pdf) on page 6-8.

# Media
We do not claim ownership over the recordings. We have provided direct links to the podcasts used in this dataset in the `podcasts.csv` file under the `iTunes ID` column. These media files have also been uploaded to Huggingface [here](https://huggingface.co/datasets/sanchit-gandhi/rev16_csv) if you'd like to download them. The `podcasts.csv` file also has direct paths to the media files on Huggingface under the `MP3 file` column.

# Cite this Dataset
The paper that originally described this dataset can be found at https://proceedings.mlr.press/v202/radford23a.html. Radford et al., 2023 covers the verbatim transcripts and the media files that are used to produce them. The nonverbatim transcripts and both sets of normalization files were created as part of https://arxiv.org/abs/2412.07937.

If you'd only like to use the verbatim transcripts please only cite:
```
@InProceedings{pmlr-v202-radford23a,
  title = 	 {Robust Speech Recognition via Large-Scale Weak Supervision},
  author =       {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and Mcleavey, Christine and Sutskever, Ilya},
  booktitle = 	 {Proceedings of the 40th International Conference on Machine Learning},
  pages = 	 {28492--28518},
  year = 	 {2023},
  editor = 	 {Krause, Andreas and Brunskill, Emma and Cho, Kyunghyun and Engelhardt, Barbara and Sabato, Sivan and Scarlett, Jonathan},
  volume = 	 {202},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {23--29 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://proceedings.mlr.press/v202/radford23a/radford23a.pdf},
  url = 	 {https://proceedings.mlr.press/v202/radford23a.html},
  abstract = 	 {We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results without the need for any dataset specific fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.}
}
```

If you'd like to use the nonverbatim transcripts, or either set of normalizations, please cite both of the following:
```
@InProceedings{pmlr-v202-radford23a,
  title = 	 {Robust Speech Recognition via Large-Scale Weak Supervision},
  author =       {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and Mcleavey, Christine and Sutskever, Ilya},
  booktitle = 	 {Proceedings of the 40th International Conference on Machine Learning},
  pages = 	 {28492--28518},
  year = 	 {2023},
  editor = 	 {Krause, Andreas and Brunskill, Emma and Cho, Kyunghyun and Engelhardt, Barbara and Sabato, Sivan and Scarlett, Jonathan},
  volume = 	 {202},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {23--29 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://proceedings.mlr.press/v202/radford23a/radford23a.pdf},
  url = 	 {https://proceedings.mlr.press/v202/radford23a.html},
  abstract = 	 {We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results without the need for any dataset specific fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.}
}
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
