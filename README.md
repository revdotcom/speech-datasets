# speech-datasets
Various speech datasets made available to the public.

In each dataset, the most up-to-date version of the dataset will always be in the master branch. Any suggested improvements should be pull-requested off of the develop branch.

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
