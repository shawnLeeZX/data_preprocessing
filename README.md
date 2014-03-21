Scripts in this folder will aid you create dictionary from documents and
generate data the same as the lda-style data in the example given in petuum
code.

Use documents in `data/bing_sample_big.txt` as an example.

## Perquisite
The raw documents should be stored in the form:

doc_title(could be url)<tab>doc_content

see `data/bing_sample_big.txt`.

First, we should give each doc one unique document id. To do this, run this
python script.
```bash
src/convert_url_to_int.py data/bing_sample_big.txt
```

It will create `data/bing_sample_big.txt.with_doc_id`.

## How to Generate Dictionary
Then execute `scripts/prepare_dict.sh`.

```bash
./scripts/prepare_dict.sh data/bing_sample_big.txt.with_doc_id
```

It will generate `data/bing_sample_big.txt.tf_df.sorted_df` and 
`data/bing_sample_big.txt.tf_df.sorted_df`. The first one sorts words in the
documents by tf and the second by df.

Use those two to select words to create your dictionary.

After you have selected some words from those two file, regardless of which
one. I will use `data/bing_sample_big.txt.tf_df.sorted_df` as an example.

Imagine that I only used 100000 words in the
`data/bing_sample_big.txt.tf_df.sorted_df` as dictionary and save those 100000
lines in file called `data/wiki_tf_df.dict`. To remove the
<tab>tf:df appending to each words, execute the following command:

```bash
python src/remove_tf_df.py data/bing_sample_big_tf_df.dict
```

After this you will get `data/bing_sample_big.dict` file, which is your
dictionary.

## How to Create lda-style data
To produce lda-style data, execute the following bash script:
```bash
scripts/lda_data_preprocess.sh data/bing_sample_big.txt.with_doc_id data/bing_sample_big.dict
```
`data/bing_sample_big.txt.with_doc_id.lda_data` is the data you want.

`data/bing_sample_big.txt.with_doc_id.map` is the word_id map file.

You can have some idea of the word id of each word in `data/bing_sample_big.txt.with_doc_id.lda_data`
in `data/bing_sample_big.txt.with_doc_id.almost_lda_data`.

In petuum lda-style data file, the first line is the number of documents. Get
the number in the last line of `data/bing_sample_big.txt.with_doc_id`, and plus
one since we assign doc id incrementally from zero. Put the number in the first
line then the file format will be the same.

## TODO: Deal with large scale
The script uses hadoop to proprocess data will be future work.
