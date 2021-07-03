from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
from web import redirect


from fertilizer_dic import fertilizer_dic
import requests
import json
import config
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image

@ app.route('/potatoResult', methods=['POST'])
def potato_prediction():
    if request.method == 'POST':
        ph = float(request.form['addph'])
        M = float(request.form['addmoisture'])
        T = float(request.form['addtemperature'])
        H = float(request.form['addhumidity'])
    return render_template('potatoResult.html', ph = ph, M = M, T = T, H = H)