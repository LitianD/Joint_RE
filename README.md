# Joint_RE
A pytorch version of  ACL 2020 paper 
"A Novel Cascade Binary Tagging Framework for Relational Triple Extraction"

![](/img/model.png)

## 运行步骤

1. 安装相关依赖
2. 解压/datasets/NYT/NYT_normal_dataset.zip
3. 创建目录/pretrained_models/bert-base-cased/
4. 下载pytorch的bert模型，放入上述目录（下载链接见百度网盘）

pytorch bert模型：https://pan.baidu.com/s/1u4IC6ldMLf43oEQxF-SdLA      提取码：lv4y

## other

config.py 中device调试时候用cpu

## 可参考

原论文链接: https://arxiv.org/abs/1909.03227

tensorflow版本: https://github.com/weizhepei/CasRel

pytorch原版本:https://github.com/WeKnowG/Extractor

bert-chinese中文bert:https://github.com/ymcui/Chinese-BERT-wwm