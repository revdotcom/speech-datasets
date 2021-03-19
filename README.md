# speech-datasets

Various speech datasets made available to the public.

# Table of Contents
* [Datasets](#datasets)
* [How to Check Out Only a Single Dataset](#how-to-check-out-only-a-single-dataset)

# Datasets
In each dataset, the most up-to-date version of the dataset will always be in the `main` branch. Any suggested improvements should be pull-requested off of the develop branch.

| Dataset | Description |
| ------- | ----------- |
|`earnings21` | This dataset contains 44 files totalling roughly 39 hours of earnings calls from the year 2020. This dataset provides the full audios, the transcripts, and accompanying metadata such as speaker labels, punctuation, and entity tags. |

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
