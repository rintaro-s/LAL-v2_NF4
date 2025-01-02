LAL-v2: A Fine-Tuned Japanese Language Model

Introduction
LAL-v2 is a fine-tuned language model based on the rinna/japanese-gpt-neox-3.6b model. This model is specifically designed to generate text in a sisterly tone, making it well-suited for applications such as character generation and creative writing.

Model Details
Model Type: Large Language Model
Base Model: rinna/japanese-gpt-neox-3.6b
Fine-tuning Data: A dataset of text written in a sisterly tone, approximately 8000 tokens (measured by GPT-4).
License: MIT
Usage
Installation:
Bash

pip install transformers torch numpy sentencepiece
Quickstart: Refer to use-example.py for a basic usage example.
Limitations: Not suitable for general-purpose use.
Training Details
Data Preprocessing: Refer to study.ipynb for details on data preprocessing.
Training: Trained on a dataset of sisterly-toned text using a standard language modeling objective.
Bias and Limitations
Bias: The model may exhibit biases present in the training data, such as a tendency towards generating text that is overly polite or submissive.
Limitations: The model is still under development and may produce incorrect or nonsensical outputs.
How to Use
Loading the Model:
Python

from transformers import AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("https://github.com/rintaro-s/LAL-v2")
Generating Text:
Python

input_text = "今日は暑いね"
output = model.generate(input_ids=tokenizer.encode(input_text), max_length=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))
Note: This model is still under development and may not be suitable for all applications.

Contributing
Contributions to this project are welcome. Please refer to the contributing guidelines in the repository.

Repository: https://github.com/rintaro-s/LAL-v2

Please let me know if you have any other questions or would like to make further modifications.


ーーライセンス表記ーー


@misc{rinna-japanese-gpt-neox-3.6b,
    title = {rinna/japanese-gpt-neox-3.6b},
    author = {Zhao, Tianyu and Sawada, Kei},
    url = {https://huggingface.co/rinna/japanese-gpt-neox-3.6b}
}

@inproceedings{sawada2024release,
    title = {Release of Pre-Trained Models for the {J}apanese Language},
    author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},
    booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
    month = {5},
    year = {2024},
    pages = {13898--13905},
    url = {https://aclanthology.org/2024.lrec-main.1213},
    note = {\url{https://arxiv.org/abs/2404.01657}}
}
