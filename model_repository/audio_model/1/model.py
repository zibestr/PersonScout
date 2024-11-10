import torch
import triton_python_backend_utils as pb_utils
from functools import partial
from src.ml_models.audiomodal import AudioFeatureExtractor

class TritonPythonModel:
    def initialize(self, args):
        self.model_name = args['model_name']

    @staticmethod
    def auto_complete_config(auto_complete_model_config):
        auto_complete_model_config.add_input( {"name": "input_audio",  "data_type": "TYPE_FP32", "dims": [1,-1], "reshape": {[1,-1]}})
        auto_complete_model_config.add_output({"name": "audio_embendings", "data_type": "TYPE_FP32", "dims": [1, 192]})
        auto_complete_model_config.set_max_batch_size(0)
        return auto_complete_model_config


    def execute(self, requests):
        responses = []
        for request in requests:
            inpu = pb_utils.get_input_tensor_by_name(request, 'input_audio')
            device = ('cuda' if torch.cuda.is_available() else
          'mps' if torch.backends.mps.is_available() else
          'cpu')
            ecapa2 = torch.jit.load('models/ecapa2.pt', map_location=device)
            audio_model = AudioFeatureExtractor(ecapa2,
                                    device=device,
                                    half_precision_mode=False)
            
            emb = audio_model.extract(inpu)
            responses.append(emb)
        return responses
