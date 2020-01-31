# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from prediction.models import Activity
from prediction.serializers import ActivitySerializer
import json
import ast

from django.shortcuts import render


@csrf_exempt
def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def activity_detail(request, pk):
    try:
        activity = Activity.objects.get(pk=pk)
    except Activity.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(activity, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        activity.delete()
        return HttpResponse(status=204)


@csrf_exempt
def predict(request):
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)

        if serializer.is_valid():
            data['pred_activity'] = predict_activity(data)
            serializer = ActivitySerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def predict_activity(unscaled_data):
    from sklearn.externals import joblib

    print(type(unscaled_data))
    print(unscaled_data)

    colonnes = ['wrist_ACC_X', 'wrist_ACC_Y', 'wrist_ACC_Z', 'EDA', 'chest_ACC_X',
                'chest_ACC_Y', 'chest_ACC_Z', 'chest_ECG', 'chest_EMG', 'chest_EDA',
                'chest_Temp', 'WEIGHT', 'AGE', 'HEIGHT', 'SKIN', 'SPORT']

    path_to_model = './prediction/RFC.sav'
    unscaled_data = [unscaled_data[colonne] for colonne in colonnes]
    import numpy as np
    unscaled_data = np.array(unscaled_data).reshape(1, -1)
    model = joblib.load(path_to_model)

    pred_activity = model.predict(unscaled_data)

    return pred_activity
