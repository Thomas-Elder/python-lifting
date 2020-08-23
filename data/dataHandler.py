#! python3

import pandas

from data.models.session import Session
from data.models.exercise import Exercise
from data.models.set import Set

import os 
import statistics
import numpy
from datetime import datetime, timedelta

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

class DataHandler:

    def getExercises(self, sessions: list) -> list:
        '''Returns a list of exercises from the given dataset

        Parses the list and compiles a list of unique Exercises.

        Parameters
        ----------
        sessions: a list of Session objects

        Returns
        -------
        The exercises as a list of strings
        '''

        exercises = []
        
        for session in sessions:

            for exercise in session.exercises:

                if exercise.name not in exercises:
                    exercises.append(exercise.name)

        return exercises

    def getSuccessRate(self, sessions: list, exercise: str,reps: int) -> float:
        '''Returns the % of reps successfully made for the given exercise
        
        Parameters
        ----------
        sessions: A list of session objects
        exercise: a string
        reps: int

        Returns
        -------
        A float, successful/total lifts
        '''

        total, successful = 0, 0

        for session in sessions:
            for e in session.exercises:
                if exercise == e.name:
                    exerciseSets = [s for s in e.sets if s.totalRepetitions == reps]

                    for s in exerciseSets:
                        total += s.totalRepetitions
                        successful += s.successfulRepetitions

        return round(successful/total, 2)

    def getExerciseMaxAverage(self, sessions: list, exercise: str, reps: int) -> float:
        '''Computes the average session maximum weight lifted for the given exercise and rep number.
        
        Parameters
        ----------
        sessions: A list of session objects
        exercise: str
        reps: int

        Returns
        -------
        A float, the average of all max weights for the given exercise and number of reps
        '''

        weights = []
        
        for session in sessions:
            for e in session.exercises:
                if exercise == e.name:
                    exerciseSets = [s.weight for s in e.sets if s.totalRepetitions == reps]

                    if len(exerciseSets) != 0:
                        weights.append(max(exerciseSets))
        
        return statistics.mean(weights)

    def getExerciseMax(self, sessions: list, exercise: Exercise, reps: int) -> float:
        '''Finds the highest weight lifted for the given exercise and rep number.
        
        Parameters
        ----------
        sessions: A list of session objects
        exercise: str
        reps: int

        Returns
        -------
        A float, the max weight lifted for the given exercise and number of reps
        '''

        weights = []
        
        for session in sessions:
            for e in session.exercises:
                if exercise == e.name:
                    exerciseSets = [s.weight for s in e.sets if s.totalRepetitions == reps]
                    
                    if len(exerciseSets) != 0:
                        weights.append(max(exerciseSets))
                
        return max(weights)

    def getExerciseMaxes(self, sessions: list, exercise: str, reps: int) -> list:
        '''Finds the all the top set weights lifted for the given exercise and rep number.
        
        Parameters
        ----------
        sessions: A list of session objects
        exercise: str
        reps: int

        Returns
        -------
        A list of dictionaries containing all the max weights lifted in each session, eg
        [{'date': '25Jul20', 'weight': 80}]

        for the given exercise and number of reps.
        '''

        exerciseMaxes = []

        for session in sessions:
            for e in session.exercises:
                if exercise == e.name:
                    exerciseSets = [s.weight for s in e.sets if s.totalRepetitions == reps]

                    if len(exerciseSets) != 0:
                        exerciseMaxes.append({'date': session.date, 'weight': max(exerciseSets)})

        return exerciseMaxes

    def getCompetitionDates(self, sessions: list) -> list:
        '''Finds the all the dates of competition.
        
        Finds sets with an attempt number and returns the dates when those sets occured.

        Parameters
        ----------
        sessions: A list of session objects

        Returns
        -------
        A list of pandas datetime objects
        '''

        competitionDates = []

        for session in sessions:
            if session.competition == True:
                competitionDates.append(session.date)

        return competitionDates

    def getPeriodDates(self, competitionDates: list) -> list:
        '''Gets a list of tuples of the start/end date of training periods
        
        For the given competition dates, returns start/end dates of the periods
        between competitions.

        Parameters
        ----------
        competitionDates: a list of pandas.datetime objects representing competition dates

        Returns
        -------
        A list of tuples of two pandas datetime objects for the start and end date
        '''

        trainingPeriods = []

        # First we need the earliest and latest date in the list.
        start = pandas.to_datetime('1986-03-24') 
        end = pandas.to_datetime('2030-12-31')

        print('competitionDates[0] - pandas.Timedelta(1): {}'.format(competitionDates[0] - pandas.Timedelta(days=1)))

        # The first period will be from the start to the first comp:
        trainingPeriods.append((start, competitionDates[0] - pandas.Timedelta(days=1)))

        # If there's only one comp, we can just toss on the last period now
        if len(competitionDates) == 1:
            trainingPeriods.append((competitionDates[0] + pandas.Timedelta(days=1), end))

        # Otherwise we need to loop over dates to get all the periods
        else:
            for i in range(len(competitionDates) - 1):
                # Then we need to loop over compdates:
                trainingPeriods.append((competitionDates[i] + pandas.Timedelta(days=1), competitionDates[i + 1] - pandas.Timedelta(days=1)))

            # Then add the last period from last comp to end.
            trainingPeriods.append((competitionDates[len(competitionDates) - 1] + pandas.Timedelta(days=1), end))

        return trainingPeriods