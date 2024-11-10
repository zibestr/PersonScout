import torch
import triton_python_backend_utils as pb_utils
from functools import partial
from transformers import pipeline
from src.ml_models.textmodal import TextModalModule

class TritonPythonModel:
    def initialize(self, args):
        self.model_name = args['model_name']

    @staticmethod
    def auto_complete_config(auto_complete_model_config):
        auto_complete_model_config.add_input( {"name": "input_text",  "data_type": "TYPE_FP32", "dims": [1, -1]})
        auto_complete_model_config.add_output({"name": "text_embendings", "data_type": "TYPE_FP32", "dims": [1,768]})
        auto_complete_model_config.set_max_batch_size(0)
        return auto_complete_model_config


    def execute(self, requests):
        responses = []
        for request in requests:
            inpu = pb_utils.get_input_tensor_by_name(request, 'input_text').as_numpy()
            device = ('cuda' if torch.cuda.is_available() else
          'mps' if torch.backends.mps.is_available() else
          'cpu')
            bert = pipeline('feature-extraction', framework='pt',
                 model='seara/rubert-base-cased-russian-emotion-detection-ru-go-emotions',
                 device=device, trust_remote_code=True,
                 torch_dtype=torch.float32)
            whisper_asr = pipeline('automatic-speech-recognition', model='Garon16/whisper_small_ru_f',
                        framework='pt', device=device, trust_remote_code=True,
                        torch_dtype=torch.float32)
            text_model = TextModalModule(whisper_asr,
                             bert,
                             device=device,
                             concat_technique='mean')
            
            emb = text_model.inference(inpu)
            responses.append(emb)
        return responses