# LAL-v2: A Fine-Tuned Japanese Language Model（NF4）

あくせす　かうんたー<br>
<img src="https://count.getloli.com/@rintaro-s?name=rintaro-s&theme=gelbooru&padding=5&offset=0&align=top&scale=1&pixelated=1&darkmode=auto"/>


## Introduction
LAL-v2 is a fine-tuned language model based on the `rinna/japanese-gpt-neox-3.6b` model. This model is specifically designed to generate text in a younger sister tone, making it well-suited for applications such as character generation and creative writing.

## Model Details
- **Model Type**: Specialized Language Model
- **Base Model**: `rinna/japanese-gpt-neox-3.6b`
- **Fine-tuning Data**: A dataset of text written in a younger sister tone, approximately 8000 tokens (measured by GPT-4o).
- **Training data created by**: Rinta,SN,Ruim
- **License**: MIT

## Usage

### Installation
```bash
pip install transformers torch numpy sentencepiece
```

### Quickstart
Refer to `use-example.py` for a basic usage example.

### Limitations
Not suitable for general-purpose use.

## Training Details

### Data Preprocessing
Refer to 

study.ipynb

 for details on data preprocessing.

### Training
Trained on a dataset of sisterly-toned text using a standard language modeling objective.

## Bias and Limitations

### Bias
The training data contains many novel-like sentences, including onomatopoeia.


### Limitations
The model is still under development and may produce incorrect or nonsensical outputs.

### Generating Text
```

「らる、おなかすいてる?」という会話文への「らる」という名前の妹の、お兄ちゃんへの返信は:「お兄ちゃん、お腹空いたよー!何 か食べに行かない?お兄ちゃんが奢ってよー!」
```
*Note: This model is still under development and may not be suitable for all applications.*


## Repository
[https://github.com/rintaro-s/LAL-v2](https://github.com/rintaro-s/LAL-v2)

## cite

@misc{rinna-japanese-gpt-neox-3.6b,<br>
　　title = {rinna/japanese-gpt-neox-3.6b},<br>
　　author = {Zhao, Tianyu and Sawada, Kei},<br>
　　url = {https://huggingface.co/rinna/japanese-gpt-neox-3.6b}<br>
}<br>
<br>
@inproceedings{sawada2024release,<br>
　　title = {Release of Pre-Trained Models for the {J}apanese Language},<br>
　　author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},<br>
　　booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},<br>
　　month = {5},<br>
　　year = {2024},<br>
　　pages = {13898--13905},<br>
　　url = {https://aclanthology.org/2024.lrec-main.1213},<br>
　　note = {\url{https://arxiv.org/abs/2404.01657}}<br>
}
