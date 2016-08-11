#!/usr/bin/python

import os
import sys
import locale
from random import randint

locale.setlocale(locale.LC_ALL, '')

current_count = 0
run_times = ""
success = 0
success_ar = 0
ans_rand = ""

def game():
	global rand_ans
	global success_ar
	random_right = randint(0, 2)
	random_guess = randint(0, 2)
	final_answer = ""
	final_answer_ar = 0
	wrong_reveal = ""
	if random_right == 0:
		if random_guess == 0:
			random_select = randint(0, 1)
			if random_select == 0:
				wrong_reveal = 1
			else:
				wrong_reveal = 2
		else:
			if random_guess == 1:
				wrong_reveal = 2
			else:
				wrong_reveal = 1

	elif random_right == 1:
		if random_guess == 1:
			random_select = randint(0, 1)
			if random_select == 0:
				wrong_reveal = 0
			else:
				wrong_reveal = 2
		else:
			if random_guess == 0:
				wrong_reveal = 2
			else:
				wrong_reveal = 0

	else:
		if random_guess == 2:
			random_select = randint(0, 1)
			if random_select == 0:
				wrong_reveal = 0
			else:
				wrong_reveal = 1
		else:
			if random_guess == 0:
				wrong_reveal = 1
			else:
				wrong_reveal = 0

	if ans_rand == "y":
		rand_dec = randint(0, 1)
		if random_guess == 0:
			if rand_dec == 1:
				final_answer = 0
			elif wrong_reveal == 1:
				final_answer = 2				
			else:
				final_answer = 1
		elif random_guess == 1:
			if rand_dec == 1:
				final_answer = 1
			elif wrong_reveal == 0:
				final_answer = 2
			else:
				final_answer = 0
		else:
			if rand_dec == 1:
				final_answer = 2
			elif wrong_reveal == 0:
				final_answer = 1
			else:
				final_answer = 0

		if wrong_reveal == 0:
			if random_guess == 1:
				final_answer_ar = 2
			else:
				final_answer_ar = 1
		elif wrong_reveal == 1:
			if random_guess == 0:
				final_answer_ar = 2
			else:
				final_answer_ar = 0
		else:
			if random_guess == 0:
				final_answer_ar = 1
			else:
				final_answer_ar = 0
	else:
		if wrong_reveal == 0:
			if random_guess == 1:
				final_answer = 2				
			else:
				final_answer = 1
		elif wrong_reveal == 1:
			if random_guess == 0:
				final_answer = 2
			else:
				final_answer = 0
		else:
			if random_guess == 0:
				final_answer = 1
			else:
				final_answer = 0
	
	if final_answer == random_right:
		global success		
		success += 1
	if ans_rand == "y":
		if final_answer_ar == random_right:
			success_ar += 1
	global current_count
	current_count += 1
######end of game func########
print ""
print "This is a Monty Hall Simulation."
print ""
print "The simulation will always reveal a wrong answer or a *goat*."
print "The player will always then choose a selection that wasn't their initial selection and not the revealed wrong door."
print "It then determines if the final answer equals the initial right selection."
print "A running total of how many times you want the simulation ran is shown."
print ""
ans_rand = str(raw_input("Do you want the player to choose randomly at round 2?\n \"y\" for yes, anything else for no: "))
run_times = int(raw_input("Number of times you want to run the Monty Hall simulation: "))

while (current_count < run_times):
	game()
	run_percent = float(success)/current_count*100
	run_cur_count = format(current_count, "n" )
	run_run_times = format(run_times, "n" )
	run_success = format(success, "n" )
	sys.stdout.write("\rRan %s times of %s times. Successes: %s Success percent: %i." % (run_cur_count,run_run_times,run_success,run_percent))
	sys.stdout.flush()
print ""
print "Success of ", success, " of ", run_times
percent = float(success)/run_times*100

print ""
if ans_rand == "y":
	print "Percent where randomly guessing was the correct choice: ",percent
	percent_ar = float(success_ar)/run_times*100
	print "Percent where switching would have been the correct choice: ",percent_ar
	diff_perc = percent_ar - percent
	if diff_perc >= 0:
		sym = "-"
	else:
		sym = "+"
	print "Difference in percent: ",sym, diff_perc
else:
	print "Percent where switching was the correct choice: ",percent
print ""
#wrote by erick hutson - feel free to use as you wish.
#made 8-9-16 and intended for Linus OSes
