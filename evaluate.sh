export PY_PATH=/home/testing/anaconda3/envs/eraser/bin/python

echo "----------------Cleaning previous results...----------------"
rm -rf eraserbenchmark/data/output/*

echo "----------------Generate test_decoded.jsonl----------------"
python3 test_decoded_generator.py

echo "----------------Evaluate based on ERASER benchmark(TF1, IOUF1)----------------"
PYTHONPATH=$PY_PATH python eraserbenchmark/rationale_benchmark/metrics.py --split test --data_dir data --results output/test_decoded.jsonl --score_file output/test_scores.json
mv eraserbenchmark/output/test_scores.json output/eraser_scores.json