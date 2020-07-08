from transformers import BertConfig, DistilBertConfig, AlbertConfig
from utils.tokenizer import BERTTokenizer
from transformers import BertTokenizer, BertModel
from models import BERT
from transformers.modeling_bert import BertConfig
import torch

epoches = 15
batch_size = 10
lr = 1e-5

BERT_MAX_LEN = 200
RANDOM_SEED = 2020

max_text_len = 100

bert_feature_size = 768

load_weight = False
dataset_path = "./datasets/"
pretrained_model_path = "./pretrained_models/"
save_weights_path = "./saved_weights/"
model_file_path = "./saved_weights/spanbert_model_24000_1591679879"

MODEL_CLASSES = {
    'bert': (BertConfig, BertModel, BERTTokenizer),
    'spanbert': (BertConfig, BertModel, BERTTokenizer),
    'chinese-bert': (BertConfig, BertModel, BertTokenizer)
}

MODEL_PATH_MAP = {
    'bert': 'bert-base-cased',
    'spanbert': 'spanbert-base-cased',
    'chinese-bert':'chinese-bert_chinese_wwm_pytorch'
}

use_cuda = True
device = torch.device("cuda:0")
# device = torch.device("cpu")

focal_loss = False


