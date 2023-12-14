In this directory, you can find the rttm files for every recording.
Our results are using https://github.com/nryant/dscore or rather directly NIST official DER scoring `md-eval-22.pl` script.

# Results
You can find diarization results in the following table

|System|DER|MISSED|FALARM|SPEAKER ERROR|
|--|--|--|--|--|
|pyannote3.0||||
|rev DER|7.71%|1.47%|1.34%|4.89%|

Please note that two files, specifically `4341191` and `4363614` were retranscribed by 
a human annotator because of incorrect speaker labels in some parts of the audio 
(so this only affects diarization results, not ASR). Therefore, the content in 
[transcripts](https://github.com/revdotcom/speech-datasets/tree/main/earnings21/transcripts)
directory does not match with RTTM for these two files.

