import tempfile
NOOP_PATCH = '''diff --git a/empty.file.{nonce}.ignore b/empty.file.{nonce}.ignore
new file mode 100644
index 0000000..e69de29
'''
def run_tests(entry, model_patch = None):
    instance_id = entry["instance_id"]
    dump(test_cmd)

    if not model_patch:
        model_patch = NOOP_PATCH.format(nonce="model_patch")

    model_name_or_path = "testing"
        "instance_id": entry["instance_id"],
        "model_name_or_path": model_name_or_path,
        "model_patch": model_patch,
        "test_patch": NOOP_PATCH.format(nonce="test_patch"), # task['test_patch']
    log_dir = tempfile.TemporaryDirectory(dir="/Users/gauthier/tmp").name
    dump(log_dir)

    log_fname = Path(log_dir) / f'{instance_id}.{model_name_or_path}.eval.log'

    log_text = log_fname.read_text()
    log_lines = log_text.splitlines()
    log_lines = [l for l in log_lines if l.startswith(">>>>")]
    print('\n'.join(log_lines))

    return log_text
dataset = get_dataset()
num = 0
num_passed = 0
for entry in dataset.values():
    test_text = run_tests(entry)
    passed = '>>>>> All Tests Passed' in test_text
    num += 1
    if passed:
        num_passed += 1
    dump(num_passed/num)