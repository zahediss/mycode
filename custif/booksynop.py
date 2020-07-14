#!/usr/bin/env python3

#ask user input about favorite hp book
thought = float(input("What is your favorite Harry Potter Book?"))

#if value is 1-n return appropriate synopsis
if thought == 1:
    message = 'Harry receives a mysterious letter on his doorstep. He is invited to attend the Hogwarts School of Witchcraft & Wizardry.'
elif thought == 2:
    message = 'Harry returns to Hogwarts. An unexpected visitor, the house elf Dobby, tries in vain to prevent Harry from returning to Hogwarts by getting him to illegally perform magic outside of the school.'
elif thought == 3:
    message = 'The night before the Hogwarts Express departs, Harry learns that Sirius Black is a convicted murderer, who is believed to want to murder Harry.'
elif thought == 4:
    message = 'Harry is mysteriously entered into the triwizard tournament and forced to compete in a series of challenges that prove very dangerous.'
elif thought == 5:
    message= 'Cornelius Fudge, minister of Magic, appoints his toady, Dolores Umbridge, as Defense Against the Dark Arts teacher, for he fears that professor Dumbledore will take his job. But her teaching is deficient and her methods, cruel, so Harry prepares a group of students to defend the school against a rising tide of evil.'
else:
    message= 'I am tired of summarizing Harry Potter books so you do not get one.'

print(message)
