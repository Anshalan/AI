import math
import random

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

G = 9.81

def calc_v0(a, d):
    return math.sqrt((G * d) / math.sin(2 * math.radians((a))))

d = ctrl.Antecedent(np.arange(0, 100, 1), 'd')
a = ctrl.Antecedent(np.arange(0, 90, 1), 'a')
v0 = ctrl.Consequent(np.arange(0, 62, 1), 'v0')

d.automf(3)
a.automf(3)

v0['lower'] = fuzz.trimf(v0.universe, [0, 0, 10])
v0['low'] = fuzz.trimf(v0.universe, [0, 10, 30])
v0['medium'] = fuzz.trimf(v0.universe, [15, 30, 45])
v0['high'] = fuzz.trimf(v0.universe, [30, 45, 60])
v0['higher'] = fuzz.trimf(v0.universe, [45, 60, 60])

rule1 = ctrl.Rule(a['average'] | d['good'], v0['medium'])
rule2 = ctrl.Rule(a['average'] | d['average'], v0['low'])
rule3 = ctrl.Rule(a['average'] | d['poor'], v0['lower'])
rule4 = ctrl.Rule(a['good'] | d['average'], v0['medium'])
rule5 = ctrl.Rule(a['poor'] | d['average'], v0['medium'])
rule6 = ctrl.Rule(a['poor'] | d['good'], v0['high'])
rule8 = ctrl.Rule(a['good'] | d['good'], v0['high'])
rule7 = ctrl.Rule(a['poor'] | d['average'], v0['high'])


v0_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7,rule8])
v0_calc = ctrl.ControlSystemSimulation(v0_ctrl)

def predict(a_gen, d_gen):    #
    v0_calc.input['a'] = a_gen
    v0_calc.input['d'] = d_gen
    v0_calc.compute()
    print(calc_v0(a_gen, d_gen))
    print(v0_calc.output['v0'])
    v0.view(sim=v0_calc)

for i in range (10):
    a = random.randint(0,90)
    d = random.randint(0,100)
    print("loop " + str(i))
    predict(a,d)
