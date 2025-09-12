SSH into session:

```
ssh -i ~/.ssh/primeintellect_ed25519 -p 1234 root@<IP_OR_HOST>
```

To verify GPU count:

```
 uv run python - <<'PY'
```

then

```
import torch, flash_attn
print("GPUs:", torch.cuda.device_count())
PY
```

For a lil test, run the reverse test training and inference setup

```
CUDA_VISIBLE_DEVICES=0,1 uv run rl \
--trainer @ configs/reverse_text/train.toml \
--orchestrator @ configs/reverse_text/orch.toml \
--inference @ configs/reverse_text/infer.toml
```

To edit GPU configs for train, inference etc like you see we use tomls in above command:

```
vi configs/hendrycks_math/1b/infer.toml
```

here change number of GPUs according to setup

Reference
Everything here: https://github.com/PrimeIntellect-ai/prime-rl/blob/main/README.md
