#! python3

from data.models.session import Session
from data.models.exercise import Exercise
from data.models.set import Set

import os 
import statistics
import calendar

from datetime import datetime, timedelta

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

class DataHandler:

    def __init__(self):
        self.startYear = 0
        self.endYear = 0

    def dateRange(self, sessions: list) -> tuple:
        ''' Returns a tuple containing the first and last dates in the session list

        Parameters
        ----------
        sessions: a list of Session objects

        Returns
        -------
        A tuple with (startDate, endDate)
        '''

        startDate = datetime(2030, 12, 31)
        endDate = datetime(2020, 1, 1)

        for session in sessions:
            if session.date > endDate:
                endDate = session.date

            if session.date < startDate:
                startDate = session.date

        return (startDate, endDate)

    def getSessions(self, sessions: list, fromDate: datetime, toDate: datetime, competition=False):

        '''Returns a list of sessions between the toDate and fromDate or a session on the fromDate from the given session list. 

        If fromDate and toDate are the same, this will return one session object. If they're different it'll return
        a list of session objects.

        Parameters
        ----------
        sessions: a list of Session objects
        fromDate: a datetime
        toDate: a datetime
        competition: whether the sessions returned are competition sessions, default False

        Returns
        -------
        The exercises as a list of Sessions
        '''

        return [s for s in sessions if s.date >= fromDate and s.date <= toDate and s.competition == competition]

    def getSessionsMonthly(self, sessions: list):

        '''Returns a list of sessions grouped by month. 

        Parameters
        ----------
        sessions: a list of Session objects

        Returns
        -------
        A list of lists of sessions
        '''
        monthlySessions = []
        yearRange = self.dateRange(sessions)
        for year in range(yearRange[0].year, yearRange[1].year + 1):
            for month in range(1, 13):
                s = self.getSessions(sessions, datetime(year, month, 1), datetime(year, month, calendar.monthrange(year, month)[1]), competition=False)

                if len(s) > 0:
                    monthlySessions.append(s)

        return monthlySessions

    def getSessionsForExercise(self, sessions: list, fromDate: datetime, toDate: datetime, exercise: str):

        '''Returns a list of sessions between the toDate and fromDate or a session on the fromDate from the given session list,
        which include the given exercise. 

        Parameters
        ----------
        sessions: a list of Session objects
        fromDate: a datetime
        toDate: a datetime
        exercise: a string

        Returns
        -------
        A list of sessions which include this exercise
        '''

        #allSessions = [s for s in sessions if s.date >= fromDate and s.date <= toDate]
        #allSessionsNonComp = [s for s in allSessions if s.competition == False]
        #allSessionsEx = [s for s in allSessionsNonComp if exercise in [e.name for e in s.exercises]]
        #return allSessionsEx
        return [s for s in sessions if s.date >= fromDate and s.date <= toDate and s.competition == False and exercise in s.exercises]

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

            for exercise in list(session.exercises.keys()):

                if exercise not in exercises:
                    exercises.append(exercise)

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
                if exercise == e:
                    exerciseSets = [s for s in session.exercises[e].sets if s.totalRepetitions == reps]

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
        
        if len(weights) != 0:
            return round(statistics.mean(weights), 2)
        
        return 0

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
        A list of datetime objects
        '''

        competitionDates = []

        for session in sessions:
            if session.competition == True:
                competitionDates.append(session.date)

        return competitionDates

    def getCompetitionPeriodDates(self, competitionDates: list) -> list:
        '''Gets a list of tuples of the start/end date of training periods
        
        For the given competition dates, returns start/end dates of the periods
        between competitions.

        Parameters
        ----------
        competitionDates: a list of datetime objects representing competition dates

        Returns
        -------
        A list of tuples of two datetime objects for the start and end date
        '''

        trainingPeriods = []
 
        # First we need the earliest and latest date in the list.
        start = datetime.strptime('1986-03-24', '%Y-%m-%d') 
        end = datetime.strptime('2030-12-31', '%Y-%m-%d')
        day = timedelta(days=1)

        # The first period will be from the start to the first comp:
        trainingPeriods.append((start, competitionDates[0] - day))

        # If there's only one comp, we can just toss on the last period now
        if len(competitionDates) == 1:
            trainingPeriods.append((competitionDates[0] + day, end))

        # Otherwise we need to loop over dates to get all the periods
        else:
            for i in range(len(competitionDates) - 1):
                # Then we need to loop over compdates:
                trainingPeriods.append((competitionDates[i] + day, competitionDates[i + 1] - day))

            # Then add the last period from last comp to end.
            trainingPeriods.append((competitionDates[len(competitionDates) - 1] + day, end))

        return trainingPeriods

    def getCompetitionLifts(self, competitionSessions: list) -> dict:
        '''Returns the best weights achieved for Snatch and Clean and Jerk in competition

        Parameters
        ----------
        competitionDates: a list of datetime objects representing competition dates

        Returns
        -------
        A dictionary with two keys, 'Snatch' and 'Clean and Jerk', values are the top weight 
        for each lift
        '''
        prs = {'Snatch': 0, 'Clean and Jerk': 0}

        for session in competitionSessions:
            for exercise in session.exercises:
                if exercise.name == 'Snatch' and exercise.topSet().weight > prs['Snatch']:
                    prs['Snatch'] = exercise.topSet().weight

                if exercise.name == 'Clean and Jerk' and exercise.topSet().weight > prs['Clean and Jerk']:
                    prs['Clean and Jerk'] = exercise.topSet().weight

        return prs

