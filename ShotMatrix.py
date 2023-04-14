from pandas import *
from datetime import datetime
import numpy as np
import csv
import sys
import os




# with open('ShotMatrix.csv', 'a') as ShotMatrix:

##Taking in previous shot sheet data
ShotSheet = read_csv("ShotMatrix.csv")

ShotNumber  = ShotSheet['ShotNumber'].tolist()
Date        = ShotSheet['Date'].tolist()
Time		= ShotSheet['Time'].tolist()
Fuel        = ShotSheet['Fuel'].tolist()
P0f 		= ShotSheet['P0f'].tolist()
P0ox 		= ShotSheet['P0ox'].tolist()
Mdot_target = ShotSheet['mdot_target'].tolist()
FuelSet 	= ShotSheet['FuelSet'].tolist()
OxSet 		= ShotSheet['OxSet'].tolist()
Mdotf 		= ShotSheet['mdotf'].tolist()
Mdoto 		= ShotSheet['mdoto'].tolist()
Mdott 		= ShotSheet['mdott'].tolist()
Igniter 	= ShotSheet['igniter'].tolist()
Engine 		= ShotSheet['engine'].tolist()
Finj 		= ShotSheet['finj'].tolist()
H 			= ShotSheet['h'].tolist()
Outcome 	= ShotSheet['Outcome'].tolist()
Comments 	= ShotSheet['Comments'].tolist()

##Taking previous data as default values

shotnum  = ShotNumber[len(ShotNumber)-1] + 1 #Adding one for new shot

fuel     = [Fuel[len(Fuel)-1]]
p0f      = [P0f[len(P0f)-1]]
p0ox	 = [P0ox[len(P0ox)-1]]
mdottarg = [Mdot_target[len(Mdot_target)-1]]
fset 	 = [FuelSet[len(FuelSet)-1]]
oxset    = [OxSet[len(OxSet)-1]]
mdotf    = [Mdotf[len(Mdotf)-1]]
mdoto    = [Mdoto[len(Mdoto)-1]]
igniter  = [Igniter[len(Igniter)-1]]
engine   = [Engine[len(Engine)-1]]
finj     = [Finj[len(Finj)-1]]
h        = [H[len(H)-1]]


###Taking inputs for new shot


print("If the value remains unchanged from the previous value, leave empty")
print("Fuel type " + str(fuel) + ":")
fuel = input()
if len(fuel)==0:
	fuel = Fuel[len(Fuel)-1] ##If input string is empty, restores previous value

print("Fuel pressure " + str(p0f) + " (psi):")
p0f = input()
if len(p0f)==0:
	p0f = P0f[len(P0f)-1] ##If input string is empty, restores previous value

print("Oxidizer pressure " + str(p0ox) + " (psi):")
p0ox = input()
if len(p0ox)==0:
	p0ox = P0ox[len(P0ox)-1] ##If input string is empty, restores previous value

print("Target mass flow rate " + str(mdottarg) + " (g/s):")
mdottarg = input()
if len(mdottarg)==0:
	mdottarg = Mdot_target[len(Mdot_target)-1] ##If input string is empty, restores previous value

print("Fuel needle valve setting " + str(fset) + " :")
fset = input()
if len(fset)==0:
	fset = FuelSet[len(FuelSet)-1] ##If input string is empty, restores previous value

print("Fuel needle valve setting " + str(oxset) + " :")
oxset = input()
if len(oxset)==0:
	oxset = OxSet[len(OxSet)-1] ##If input string is empty, restores previous value

print("Fuel mass flow rate " + str(mdotf) + " (g/s, from calibrations):")
mdotf = input()
if len(mdotf)==0:
	mdotf = Mdotf[len(Mdotf)-1] ##If input string is empty, restores previous value

print("Oxidizer mass flow rate " + str(mdoto) + " (g/s, from calibrations):")
mdoto = input()
if len(mdoto)==0:
	mdoto = Mdoto[len(Mdoto)-1] ##If input string is empty, restores previous value

mdott = int(mdotf) + int(mdoto)

print("Igniter used (LE, HE, nonel) " + str(igniter) + ":")
igniter = input()
if len(igniter)==0:
	igniter = Igniter[len(Igniter)-1] ##If input string is empty, restores previous value

print("Engine configuration (Radial discrete, MK2): " + str(engine) + ":")
engine = input()
if len(engine)==0:
	engine = Engine[len(Engine)-1] ##If input string is empty, restores previous value

print("Fuel injector " + str(finj) + ":")
finj = input()
if len(finj)==0:
	finj = Finj[len(Finj)-1] ##If input string is empty, restores previous value

print("Annulus thickness " + str(h) + " mm :")
h = input()
if len(h)==0:
	h = H[len(H)-1] ##If input string is empty, restores previous value

print("Experiment outcome: ")
outcome = input()

print("Extra comments and notes: ")
comments = input()

##pulling date and time variables
now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")


data = {'ShotNumber'	: [shotnum],
		'Date'			: [date],
		'Time'			: [time],
		'Fuel'			: [fuel],
		'P0f'			: [p0f],
		'P0ox'			: [p0ox],
		'mdot_target' 	: [mdottarg],
		'FuelSet'		: [fset],
		'OxSet'			: [oxset],
		'mdotf'			: [mdotf],
		'mdoto'			: [mdoto],
		'mdott'			: [mdott],
		'igniter'		: [igniter],
		'engine'		: [engine],
		'finj'			: [finj],
		'h'				: [h],
		'Outcome'		: [outcome],
		'Comments'		: [comments]
}

newshot = DataFrame(data)
newshot.to_csv('ShotMatrix.csv', mode='a', index=False, header=False)