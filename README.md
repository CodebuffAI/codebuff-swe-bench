# Codebuff SWE Bench harness

This repo contains the benchmarking harness that was used to run run Codebuff on the SWE Bench.
It closely follows [Aider's SWE-bench harness](https://github.com/Aider-AI/aider-swe-bench), but doesn't try to re-run if it fails to solve a test. We want to make the results as realistic as possible to what a real user might do.

## Installation

```
# Clone this repo
git clone https://github.com/codebuffai/codebuff-swe-bench

# Clone the SWE Bench docker repo into a subdir of this repo
cd codebuff-swe-bench
git clone https://github.com/aorwall/SWE-bench-docker

# Install pip requirements
pip install -r requirements.txt


npm i -g codebuff
```

See the
[SWE Bench Docker docs](https://github.com/aorwall/SWE-bench-docker)
to ensure you have built or pulled all the SWE Bench testbed
docker images you'll need.

## Running the benchmark and computing results

The workflow for working with SWE Bench in general is 2 steps:

1. Run your agent on the problems to produce predictions, which are a series of json records that get bundled up into a jsonl file.
2. Evaluate the predictions jsonl file using the acceptance tests. This produces `.eval.log` files with logs of the testing procedure.

This repo is for running and evaluating Codebuff on SWE Bench. As described in the README, it consists of 2 scripts:

1. The `codebuff_harness.py` script will run Codebuff on all the problems and produce predictions. You can optionally give it a `--run-id` to have it continue on a particular run (the ID is just a timestamp, which you can find at the directory name at `predictions/codebuff/<ID>`).

2. The `report.py` script takes in an argument to the particular directory with the diffs (should be `predictions/codebuff/<ID>`). It consumes all those predictions and turns them into `predictions/codebuff/<ID>/all_preds.jsonl`. It then feeds that jsonl file through the SWE Bench evaluation and reporting scripts to produce `logs/codebuff/<ID>/<instance_id>...eval.log` files as well as a summary report in `predictions/<DIRNAME>/results.json`.

3. The `table.py` script takes in an argument to the particular directory with the diffs (should be `predictions/codebuff/<ID>`). It formats the results nicely and shows the final resolved percentage.
