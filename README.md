# speech-datasets

Various speech datasets made available to the public.

# Release Notes
## `202408`
* `earnings-21`: Updated 4341191 to resolve off-by-one labeling issue
* `earnings-22`: Updated to include `<>` symbols around `<inaudible>` and `<crosstalk>` tags
## `2023012`
* `rttms` - added RTTM files to evaluate diarization (DER and possibly other metrics)
## `202309`
* `longform-reconstitution`: Added long-form data described in https://arxiv.org/abs/2309.15013
## `202206`
* `earnings-21`: Updated the some reference transcripts with some errors identified as part of our routine testing.
    - Diff: +44 −45
    - Modified 8 nlp files and 1 norm.json file
* `earnings-22`: No changes since release of `202204`

# Table of Contents
* [Datasets](#datasets)
* [How to Check Out Only a Single Dataset](#how-to-check-out-only-a-single-dataset)

# Datasets
In each dataset, the most up-to-date version of the dataset will always be in the `main` branch. Any suggested improvements should be pull-requested off of the develop branch.

| Dataset | Description |
| ------- | ----------- |
|`earnings21` | This dataset contains 44 files totalling roughly 39 hours of earnings calls from the year 2020. This dataset provides the full audios, the transcripts, and accompanying metadata such as speaker labels, punctuation, and entity tags. |
|`earnings22` | This dataset contains 125 files totalling roughly 119 hours of English language earnings calls from global countries. This dataset provides the full audios, transcripts, and accompanying metadata such as ticker symbol, headquarters country, and our defined "Language Region". |
| `longform-reconstitution` | Long-form versions of the Gigaspeech, TED-LIUM, and VoxPopuli-en corpora. See https://arxiv.org/abs/2309.15013 for details |


# How to Check Out Only a Single Dataset

As we grow this repository, we expect that it will grow in size and will make pulling the whole repository difficult. In order to download only one dataset we recommend following [this post on StackOverflow](https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository/52269934#52269934). We outline the process here for ease of use.

1. Ensure that you have `>= git 2.30.0`
2. Run the following commands such that `${DATASET_NAME}` is set to the dataset directory you want to use.
  ```
  git clone --depth 1  --filter=blob:none  --sparse https://github.com/revdotcom/speech-datasets.git
  cd speech-datasets
  git sparse-checkout init --cone
  git sparse-checkout set ${DATASET_NAME}
  ```

  e.g.
  ```
  git clone --depth 1  --filter=blob:none  --sparse https://github.com/revdotcom/speech-datasets.git
  cd speech-datasets
  git sparse-checkout init --cone
  git sparse-checkout set earnings21
  ```
  These commands will only checkout the `earnings21` dataset.
  
# Github Large File Storage (LFS)
Due to the length of some media files in our corpora, we have added Github's LFS to allow us to upload large files for ease of download by users.

The impact is a few added steps to be able to access these files.

## Affected Datasets
- `earnings22`
- `longform-reconstitution`

## Steps to Download from LFS
1. The first step is to download and install Git LFS onto your machine. We recommend following [Github's step-by-step instructions found here](https://git-lfs.github.com/)
2. Run the following commands from the main directory of `speech-datasets`:
  ```
  cd ${DATASET_NAME}
  git lfs pull
  ```

  e.g.
  ```
  cd earnings22
  git lfs pull
  ```


  
