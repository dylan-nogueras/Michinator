from flask import Flask, request
from flask_restful import Resource, Api
import json, random

app = Flask(__name__)
api = Api(app)

class Michi:
	def get_michi(self, michis):
		return michis[random.randint(0, len(michis)-1)]
	
	def generate_michi(self):
		michi = self.get_michi(json.load(open('memes.json')))
		return michi
