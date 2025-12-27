from math import *

class Tank:
	def __init__(self, attribute, tid):
		self.__tid = tid
		self.__hp = int(attribute[0])
		self.__d = int(attribute[1])
		self.__a = int(attribute[2])
		self.__p = int(attribute[3])

	def getTID(self):
		return self.__tid
		
	def getHP(self):
		return self.__hp

	def getD(self):
		return self.__d

	def getA(self):
		return self.__a

	def getP(self):
		return self.__p

	def setHP(self, hp):
		self.__hp = hp

	def setD(self, d):
		self.__d = d

	def setA(self, a):
		self.__a = a

	def setP(self, p):
		self.__p = p

	def display(self):
		print(f"A fucking tank with\nHit point: {self.__hp}\nDamage: {self.__d}\nArmor: {self.__a}\nPrice: {self.__p}\n=====\n")

	def strength(self):
		return sqrt(self.__hp**2 + self.__d**2 + self.__a**2)

	def __lt__(self, other):
		return self.__p > other.__p
