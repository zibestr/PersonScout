import torch
import triton_python_backend_utils as pb_utils
from functools import partial
from ultralytics import YOLO
from transformers import ViTModel
from src.ml_models.imagemodal import ImageModalModule

class TritonPythonModel:
    def initialize(self, args):
        self.model_name = args['model_name']

    @staticmethod
    def auto_complete_config(auto_complete_model_config):
        auto_complete_model_config.add_input( {"name": "input_image",  "data_type": "TYPE_FP32", "dims": [-1,3,448, 448]})
        auto_complete_model_config.add_output({"name": "video_embendings", "data_type": "TYPE_FP32", "dims": [1,768]})
        auto_complete_model_config.set_max_batch_size(0)
        return auto_complete_model_config


    def execute(self, requests):
        responses = []
        for request in requests:
            inpu = pb_utils.get_input_tensor_by_name(request, 'input_image')
            device = ('cuda' if torch.cuda.is_available() else
          'mps' if torch.backends.mps.is_available() else
          'cpu')
            vit = ViTModel.from_pretrained('dima806/facial_emotions_image_detection')
            yolo_face = YOLO('models/yolov11n-face.pt')
            image_model = ImageModalModule(yolo_face,
                               vit,
                               detection_threshold=0.5,
                               device=device,
                               concat_technique='mean',
                               half_precision_mode=False)
            
            emb = image_model.inference(inpu)
            responses.append(emb)
        return responses
