# Joint_RE
A pytorch version of  ACL 2020 paper 
"A Novel Cascade Binary Tagging Framework for Relational Triple Extraction"

![](/img/model.png)

## 运行步骤

### 1.基于NTY数据集

1. 安装相关依赖
2. 解压/datasets/NYT/NYT_normal_dataset.zip
3. 创建目录/pretrained_models/bert-base-cased/
4. 下载pytorch的bert模型，放入上述目录（下载链接见百度网盘）

pytorch bert-base-cased 模型：https://pan.baidu.com/s/1u4IC6ldMLf43oEQxF-SdLA      提取码：lv4y

### 2.基于百度2019语言与智能技术竞赛数据集

1. 解压/datasets/2019_Baidu_RE/2019_Baidu_RE.zip
2. 创建目录/pretrained_models/chinese-bert_chinese_wwm_pytorch/
3. 下载哈工大预训练模型，放入上述目录（下载链接见讯飞网盘，哈工大git库中提供）
4. 运行run.py --model chinese-bert --dataset 2019_Baidu_RE

chinese-bert_chinese_wwm_pytorch 模型：http://pan.iflytek.com/#/link/5DBDD89414E5B565D3322D6B7937DF47 密码：hteX

## other

config.py 中device调试时候用cpu

## 可参考

原论文链接: https://arxiv.org/abs/1909.03227

tensorflow版本: https://github.com/weizhepei/CasRel

pytorch原版本:https://github.com/WeKnowG/Extractor

bert-chinese中文bert:https://github.com/ymcui/Chinese-BERT-wwm