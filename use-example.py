from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import tempfile

# キャッシュディレクトリをEドライブに設定
os.environ['TRANSFORMERS_CACHE'] = 'E:\\imouto-ai\\cache'
os.environ['TORCH_HOME'] = 'E:\\imouto-ai\\cache'

# 一時ファイルのディレクトリをEドライブに設定
os.environ['TMP'] = 'E:\\imouto-ai\\temp'
os.environ['TEMP'] = 'E:\\imouto-ai\\temp'
tempfile.tempdir = 'E:\\imouto-ai\\temp'

model_name = "./LL1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")

text = "「らる、おなかすいてる？」という会話文への「らる」という名前の妹の、お兄ちゃんへの返信は："
inputs = tokenizer(text, return_tensors="pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens=50)  # max_new_tokensで生成するトークン数を制御
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)