# JSALT 2023 Long-Form ASR Corpora

Long-form ASR corpora created by reconstituting transcriptions from existing, open ASR corpora. All transcriptions are in English. This repository contains only time-aligned transcriptions - audio can be downloaded from the following locations:

1. GigaSpeech: https://github.com/SpeechColab/GigaSpeech/
2. TED-LIUM: https://www.openslr.org/7/
3. VoxPopuli: https://github.com/facebookresearch/voxpopuli

All data in this repository made available as Lhotse supervisions - see https://github.com/lhotse-speech/lhotse/tree/master for more information. 

## GigaSpeech

Currently available: Lhotse supervisions for four versions of the GigaSpeech M subset. 

1. `gigaspeech/gigaspeech_supervisions_m.jsonl.gz` - original segmentation of the transcriptions of the GigaSpeech M subset (Note: not time-aligned). Average segment length 4s 
2. `gigaspeech/gigaspeech_supervisions_m_lf.jsonl.gz` - full reconstitutions of the transcriptions of the GigaSpeech M subset. Average segment length 10s
3. `gigaspeech/gigaspeech_supervisions_m_lf_15.jsonl.gz` - full reconstitution, followed by re-segmentation with a maximum segment length of 15s. Average segment length 7s
4. `gigaspeech/gigaspeech_supervisions_m_lf_30.jsonl.gz` - full reconstitution, followed by re-segmentation with a maximum segment length of 30s. Average segment length 9s

## TED-LIUM

## VoxPopuli
