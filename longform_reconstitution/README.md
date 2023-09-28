# JSALT 2023 Long-Form ASR Corpora

Long-form ASR corpora created by reconstituting transcriptions from existing, open ASR corpora. All transcriptions are in English. This repository contains only time-aligned transcriptions - audio can be downloaded from the following locations:

1. GigaSpeech: https://github.com/SpeechColab/GigaSpeech/
2. TED-LIUM: https://www.openslr.org/7/
3. VoxPopuli en: https://github.com/facebookresearch/voxpopuli

All data in this repository made available as Lhotse supervisions - see https://github.com/lhotse-speech/lhotse/tree/master for more information. 

## GigaSpeech

Lhotse supervisions for GigaSpeech M subset. 

`gigaspeech/gigaspeech_m_train_lf_linked.jsonl.gz` - linked reconstitution of the transcriptions of the GigaSpeech M subset. Average segment length 11.8s
`gigaspeech/gigaspeech_m_train_lf_linked_15.jsonl.gz` - linked reconstitution, followed by re-segmentation with a maximum segment length of 15s. Average segment length 7s
`gigaspeech/gigaspeech_m_train_lf_linked_30.jsonl.gz` - linked reconstitution, followed by re-segmentation with a maximum segment length of 30s. Average segment length 9s

Lhotse supervisions for GigaSpeech 200h subset.

`gigaspeech/gigaspeech_200h_train.jsonl.gz` - original segmentation of the transcriptions of the GigaSpeech 200h subset (Note: not time-aligned). Average segment length 4s
`gigaspeech/gigaspeech_200h_train_lf_linked.jsonl.gz` - linked reconstitution of the transcriptions of the GigaSpeech 200h subset. Average segment length 295s
`gigaspeech/gigaspeech_200h_train_lf_linked_15.jsonl.gz` - linked reconstitution, followed by re-segmentation with a maximum segment length of 15s. Average segment length
`gigaspeech/gigaspeech_200h_train_lf_linked_30.jsonl.gz` - linked reconstitution, follwed by re-segmentation with a maximum segment length of 30s. Average segment length

Lhotse supervisions for GigaSpeech XL subset.

`gigaspeech/gigaspeech_xl_train_lf_linked.jsonl.gz` - linked reconstitution of the transcriptions of the GigaSpeech XL subset. Average segment length
`gigaspeech/gigaspeech_xl_train_lf_linked_15.jsonl.gz` - linked reconstitution, followed by re-segmentation with a maximum segment length of 15s. Average segment length
`gigaspeech/gigaspeech_xl_train_lf_linked_30.jsonl.gz` - linked reconstitution, followed by a re-segmentation with a maximum segment legnth of 30s. Average segment length

Lhotse supervisions for GigaSpeech longform dev and test sets.

`gigaspeech/gigaspeech_dev_lf_linked.jsonl.gz` - linked reconstitution of the transcriptions of the GigaSpeech dev set. Average segment length 1510.9s
`gigaspeech/gigaspeech_test_lf_linked.jsonl.gz` - linked reconstitution of the transcriptions of the GigaSpeech test set. Average segment length 1088.2s

## TED-LIUM

Lhotse supervisions for TED-LIUM linked.

`tedlium/tedlium_train_lf_linked.jsonl.gz` - linked reconstitution of TED-LIUM train. Average segment length 64s
`tedlium/tedlium_train_lf_linked_15.jsonl.gz` - linked reconstitution, followed by re-segmentation with a maximum segment length of 15s. Average segment length
`tedlium/tedlium_train_lf_linked_30.jsonl.gz` - linked reconsitution, followed by re-segmentation with a maximum segment length of 30s. Average segment length
`tedlium/tedlium_dev_lf_linked.jsonl.gz` - linked reconstitution of TED-LIUM dev. Average segment length 459.3
`tedlium/tedlium_test_lf_linked.jsonl.gz` - linked reconstitution of TED-LIUM test. Average segment length 576.1

Lhotse supervisions for TED-LIUM expanded.

`tedlium/tedlium_train_lf_expanded.jsonl.gz` - expanded reconstitution of TED-LIUM train. Average segment length 827.4s
`tedlium/tedlium_train_lf_expanded_15.jsonl.gz` - expanded reconstitution, followed by re-segmentation with a maximum segment length of 15s. Average segment length 
`tedlium/tedlium_train_lf_expanded_30.jsonl.gz` - expanded reconstitution, followed by a re-segmentation with a maximum segment length of 30s. Average segment length 
`tedlium/tedlium_dev_lf_expanded.jsonl.gz` - expanded reconstitution of TED-LIUM dev. Average segment length 815.3s
`tedlium/tedlium_test_lf_expanded.jsonl.gz` - expanded reconstitution of TED-LIUM test. Average segment length 972.7s

## VoxPopuli

Lhotse supervisions for VoxPopuli en expanded.

`voxpopuli/voxpopuli_en_train_lf_expanded.jsonl.gz` - expanded reconstitution of VoxPopuli en train. Average segment length 143.7s
`voxpopuli/voxpopuli_en_dev_lf_expanded.jsonl.gz` - expanded reconstitution of VoxPopuli en dev. Average segment length 120.5
`voxpopuli/voxpopuli_en_test_lf_expanded.jsonl.gz` - expanded reconstitution of VoxPopuli en test. Average segment length 108.5
