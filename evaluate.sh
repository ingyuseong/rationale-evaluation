export PY_PATH=/home/testing/anaconda3/envs/eraser/bin/python
export exp=1-1

echo "----------------Cleaning previous results...----------------"
mv prediction/predict_results_claimdiff_$exp.json predict_results_claimdiff.json
rm -rf eraserbenchmark/data/output/*

echo "----------------Generate test_decoded.jsonl----------------"
python3 test_decoded_generator.py

echo "----------------Evaluate based on ERASER benchmark(TF1, IOUF1)----------------"
PYTHONPATH=$PY_PATH python eraserbenchmark/rationale_benchmark/metrics.py --split test --data_dir eraserbenchmark/data --results eraserbenchmark/output/test_decoded.jsonl --score_file eraserbenchmark/output/test_scores.json
mv eraserbenchmark/output/test_scores.json output/eraser_scores_$exp.json
mv predict_results_claimdiff.json prediction/predict_results_claimdiff_$exp.json