```
$ python -m scripts.run_fine_tune --train-batch-size 8 --eval-batch-size 16 --epochs 5
```


```
MODEL_PATH = artifacts/gpt2_2020.12.09_14.15.47/gpt2_step_6000.pth 

$ python -m scripts.run_generate --model-path artifacts/gpt2_2020.12.09_14.15.47/gpt2_step_6000.pth --output-path decoded.tsv
```
