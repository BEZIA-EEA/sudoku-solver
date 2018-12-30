#Amina Babaslimane bbsmina09@gmail.com
#BEZIA Ayoub Ayoub.bezia@gmail.com

from __future__ import print_function
from Numberjack import *
import numpy as np

def get_model(): #Declaration du domaine des variables
	grille = Matrix(9,9,1,9) 
	model = Model()
	model.add(grille[0,0]==1, grille[6,0]==9, grille[7,0]==5, grille[4,1]==6,grille[5,1]==7,
				grille[6,2]==8, grille[4,3]==3,grille[7,3]==4,grille[8,3]==7, grille[0,4]==8,
				grille[1,6]==4, grille[3,6]==9, grille[6,6]==1, grille[2,7]==7, grille[3,7]==5,
				grille[1,8]==3)				
	
	for i in range(9):
			model.add(AllDiff( [grille[i,j]  for j in range(9)] ) )
 
	for j in range(0, 8):
		model.add(AllDiff([grille[i,j] for i in range(9)]))
		
	for i in range(3):
		for j in range(3):
			model.add(AllDiff(grille[3*i:3+3*i,3*j:3+3*j]))

				
			
	return grille, model

def solve(param):
	grille,model = get_model()
	solver = model.load('Mistral')
	solver.solve()

#print a l'ecran

	if solver.is_sat():
		print(grille)
	elif solver.is_unsat():
		print("Unsatisfiable")
	else:
		print("Unknown")


#main

if __name__ == '__main__':
	default = {'solver': 'Mistral'}
	param = input(default)
	solve(param)

