from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "./model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

text = "「らる、おなかすいてる？」という会話文への「らる」という名前の妹の、お兄ちゃんへの返信は："
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=50) # max_new_tokensで生成するトークン数を制御
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
