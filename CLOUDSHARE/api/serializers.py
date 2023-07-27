from rest_framework import serializers
from .models import Folder
import shutil
from numpy import require
from rest_framework import serializers
from .models import *

class FileListSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(
            max_length=100000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def create(self,validated_data):
        folder =  Folder.objects.create()
        files = validated_data.get('files')
        files_objs=[]
        for file in files:
            files_obj = file.objects.create(folder=folder,file=file)
            files_objs.append(files_obj)

        return {'files': {}, 'folder': str(folder.uid)}

