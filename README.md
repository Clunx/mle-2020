# Parth Tripathi intership interview project

I've tried to do most of what was asked for me, let me detail that to you:

## Refactoring from notebook to python files

The first thing to do was getting rid of the notebook to get to python files. Therefore I've created multiple python files:

test.py -- It's the testing file running it will allow you to input a user id and get its recommended movies

data.py -- It is where I import the datasets needed for the project and do some modifications on the data that I will explain later

functions.py -- It is where I regroup most of the core function needed for the project as well as an other one that I will talk about later

accessors.py -- I've created multiple accessors to ease the task of getting some data for the MLE or datascientists working on the project

evaluation.py -- It is where I've created an evaluation algorithm to see if the main recommendation algorithm gives good or bad results to the user

Let's talk about each programm in detail now:

## test.py

Nothing major is to be said about this program except that it allows to test the recommendation algorithm with a simple user id input.
It should not need to be altered later when the main function are changed to give better results.

## data.py

This program imports the datasets to let the other programs use them. It is a good way to have everything centralized, not requiring the user to change each program to chose which datasets he wants to use. 

But I've also added a scalling algorithm for the movies dataset, to make sure that everyt feature is scalled properly one from an other. It doesn't matter with this dataset since all the features take boolean values but if some other feature is added it might be important to make sure that they're scalled properly. The scalling function is in functions.py

## functions.py

I've added the functions written in the original notebook and the scalling one mentionned above. The two functions (the ones that were in the notebook) should be the only part of all the five scripts that need to be changed to improve the algorithm(except for the imported datasets of course). It makes life easier for the MLE and datascientists working on the project to know that they only have to work on this and not bother about the rest of the scripts.

## accessors.py 

I've created accessors to help the datascients to have access easily to variables they need when they try to improve the program. Not all of them are being used right now and I probably haven't created all the ones that would be needed in the future but it can already help people working on the project. I was thinking at the beginning to create classes to host those accessors, but it did not seem usefull especially at this stage of the project to do so, but it really might be in the future especially if working with SQL databases.

## evaluation.py

This is a program I've made to evaluate the performances of the algorithm, it is probably not optimal in its execution but allow you to compare the average of the average rating for every movie a user has watched to the average of the average movie that every user has watched that has been recommended to him.
Thus allowing us to see how good our program works
There are some minor flaws with the script but it seems to be doing a pretty good work nonetheless.

However it should be tested with a limited number of users(instead of all of them) to get results quickly.


## Conclusion

The way the program is now structured should help improving it more easily than before, separating every part of the program and giving a benchmark algorithm(evaluate.py) to  verify that the program is improving after changes.
It allows you to test it also to see what the output will be for users, and give you tools(accessors) to ease your work when improving it.

## Added features

If going with the same dataset, we should probably think of taking into account the age and the gender of the user to give our recommendation. This could give good results especially when we see that genres are not slim enough factors for a correct reccommendation system.
