from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model
import torch
import joblib
import os

from cdqa.reader import BertProcessor, BertQA
from cdqa.utils.download import download_squad

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# print ('Available devices ', torch.cuda.device_count())
# print ('Current cuda device ', torch.cuda.current_device())
# print(torch.cuda.get_device_name(device))

train_processor = BertProcessor(bert_model="bert-base-multilingual-cased", do_lower_case=False, is_training=True, max_seq_length=384)
train_examples, train_features = train_processor.fit_transform(X='./dataset/KorQuAD_v1.0_train.json')
# eval_examples, eval_features = train_processor.transform(X='./dataset/KorQuAD_v1.0_dev.json')

reader = BertQA(bert_model='bert-base-multilingual-cased',    # multilingual-cased를 써줘야 한국어가 잘 훈련된다(이거 안해줘서 f1-score안나왔음)
                train_batch_size=12,
                learning_rate=3e-5,
                num_train_epochs=5,
                do_lower_case=False,
                output_dir='models')

reader.fit(X=(train_examples, train_features))

reader.model.to('cuda')
reader.device = torch.device('cuda')
joblib.dump(reader, os.path.join(reader.output_dir, 'bert_qa_hwalim_multi_epoch5.joblib'))
reader.predict(X=(eval_examples, eval_features))
# print(reader.predict(X=(eval_examples, eval_features)))
# reader._n_best_predictions()
