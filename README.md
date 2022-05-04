# rationale-evaluation
A simple script to evaluate generative rationale

### (Lehman, et al., 2019) Pipeline

To run this model, we need to first:
* create a `model_components`, `data`, and `output`, directory
* download GloVe vectors from http://nlp.stanford.edu/data/glove.6B.zip and extract the 200 dimensional vector to `model_components`
* download http://evexdb.org/pmresources/vec-space-models/PubMed-w2v.bin to `model_components`
* set up a virtual env meeting requirements.txt
* download data from the primary website to `data` and extract each dataset to its respective directory
* ensure that we have at least an 11G GPU. Reducing batch sizes may enable running on a smaller GPU.

### Evaluation
```
bash evaluate.sh
```

### How to evaluate (ERASER)
0. jsonl_generator (local) -> docs.jsonl(val + test), val.jsonl, test.jsonl (eraser/data)
1. new_evaluation (training VM) -> predict_results_claimdiff_val, predict_results_claimdiff_test (./prediction)
2. predict_results_claimdiff -> test_decoded_generator or pred_to_eval (local) -> test_decoded.jsonl (eraser/output)
3. Run `evaluate.sh`

### Reference
* [ERASER](https://github.com/jayded/eraserbenchmark)
* [Rough script template, ec2-docker-script](https://github.com/dooking/ec2-docker-script)
