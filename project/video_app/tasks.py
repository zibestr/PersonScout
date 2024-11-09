# from celery import shared_task
# from .models import FileUpload
# import PIL.Image as Image
# import io
# import base64
# import os
# from django.core.files import File
# from . import utils


# @shared_task(name="upload_file")
# def task_upload_file(data):
#     byte_data = data['file'].encode(encoding='utf-8')
#     b = base64.b64decode(byte_data)
#     img = Image.open(io.BytesIO(b))
#     img.save(data['name'], format=img.format)

#     with open(data['name'], 'rb') as file:
#         picture = File(file)
#         instance = FileUpload.objects.create(file=picture)
#         file_path = instance.file.path
#         client = utils.get_client()
#         result = utils.predict_model(file_path, client)
#         print(result)

#     os.remove(data['name'])
