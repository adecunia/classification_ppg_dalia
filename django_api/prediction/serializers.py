from rest_framework import serializers
from prediction.models import Activity


class ActivitySerializer(serializers.Serializer):
    SPORT = serializers.FloatField()
    SKIN = serializers.FloatField()
    HEIGHT = serializers.FloatField()
    AGE = serializers.FloatField()
    WEIGHT = serializers.FloatField()
    chest_Temp = serializers.FloatField()
    chest_EDA = serializers.FloatField()
    chest_EMG = serializers.FloatField()
    chest_ECG = serializers.FloatField()
    chest_ACC_Z = serializers.FloatField()
    chest_ACC_X = serializers.FloatField()
    chest_ACC_Y = serializers.FloatField()
    EDA = serializers.FloatField()
    wrist_ACC_Z = serializers.FloatField()
    wrist_ACC_X = serializers.FloatField()
    wrist_ACC_Y = serializers.FloatField()
    pred_activity = serializers.FloatField(allow_null=True)

    def create(self, validated_data):
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.SPORT = validated_data.get('SPORT', instance.SPORT)
        instance.SKIN = validated_data.get('SKIN', instance.SKIN)
        instance.HEIGHT = validated_data.get('HEIGHT', instance.HEIGHT)
        instance.AGE = validated_data.get('AGE', instance.AGE)
        instance.WEIGHT = validated_data.get('WEIGHT', instance.WEIGHT)
        instance.chest_Temp = validated_data.get('chest_Temp', instance.chest_Temp)
        instance.chest_EDA = validated_data.get('chest_EDA', instance.chest_EDA)
        instance.chest_EMG = validated_data.get('chest_EMG', instance.chest_EMG)
        instance.chest_ECG = validated_data.get('chest_ECG', instance.chest_ECG)
        instance.chest_ACC_Z = validated_data.get('chest_ACC_Z', instance.chest_ACC_Z)
        instance.chest_ACC_X = validated_data.get('chest_ACC_X', instance.chest_ACC_X)
        instance.chest_ACC_Y = validated_data.get('chest_ACC_Y', instance.chest_ACC_Y)
        instance.EDA = validated_data.get('EDA', instance.EDA)
        instance.wrist_ACC_Z = validated_data.get('wrist_ACC_Z', instance.wrist_ACC_Z)
        instance.wrist_ACC_X = validated_data.get('wrist_ACC_X', instance.wrist_ACC_X)
        instance.wrist_ACC_Y = validated_data.get('wrist_ACC_Y', instance.wrist_ACC_Y)
        instance.pred_activity = validated_data.get('pred_activity', instance.pred_activity)
        instance.save()
        return instance
