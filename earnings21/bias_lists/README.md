# Contextual Biasing Lists

This folder contains biasing lists for measuring contextual ASR performance on the Earnings21 dataset. 

- `oracle_list.txt` contains words and phrases found in the Earnings21 reference transcripts
- `distractor_list.txt` includes all of `oracle_list.txt` with the addition of some Fortune 500 company names and famous CEOs which are not found in Earnings21

These biasing lists were used in [Improving Contextual Recognition of Rare Words with an Alternate Spelling Prediction Model](https://arxiv.org/abs/2209.01250) (published at Interspeech 2022)!