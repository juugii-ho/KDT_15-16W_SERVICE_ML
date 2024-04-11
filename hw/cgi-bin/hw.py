#!/usr/bin/env python


import torch
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import cgi, sys, codecs
import torch
from torchtext.datasets import AG_NEWS

sys.stdout = codecs.getwriter(encoding='utf-8')(sys.stdout.detach())
form = cgi.FieldStorage()

def print_html(result=""):
    filename="./html/hw.html"
    with open(filename, 'r', encoding='utf-8') as f:
        print('Content-Type : text/html; charset = utf-8')
        print()
        print(f.read().format(result))


tokenizer = get_tokenizer("basic_english")

def yield_tokens(data_iter):
    for _, text in data_iter:
        yield tokenizer(text)

train_iter = AG_NEWS(split="train")
vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])

text_pipeline = lambda x: vocab(tokenizer(x))
label_pipeline = lambda x: int(x) - 1

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load('text_classification_model.pth')
model.to(device)

def predict(text):
    with torch.no_grad():
        text = torch.tensor(text_pipeline(text), dtype=torch.int64).to(device)
        text = text.unsqueeze(0)
        offsets = torch.tensor([0]).to(device)
        predicted_label = model(text, offsets)
        print(predicted_label.argmax(1).item() + 1 )
        return predicted_label.argmax(1).item() + 1 


if 'text' in form:
    result = predict('text')
else:
    result = "No Data"


result = 'how you like that'
print_html(result)
