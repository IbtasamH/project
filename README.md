Guess The Word
Video:  <https://youtu.be/zBRL0J3iDtA>
# Description:

The condept of my project is to basically guess the word inspired by the game wordle.
First you choose a level (1,2,3) depending on the difficulty where 1 is a 3 letter word, 2 is
a 4 letter word and 3 is a 5+ letter word. Once establishing your level, there word length will be
displayed for example if you picked a 5+ letter word, then it would say "the word is ... letters".
This part off the project also includes validation so that the user has to enter 1,2 or 3.

Moving on the next part to this is the user having its first guess. So initially there are 5 guesses
so i first looped through 5 times. Then we ask for the users first guess and also validate this to
make sure that the guess is the same length of the word and we find the length by using the len()
function built in. Ofcourse we prompt the user to guess again without losing their guess if they
didnt input a valid word.

After making the guess we call the letters function which we pass the answer. The loop includes
a for loop which loops through the answer and basically just puts each char in a list so for example
if the word was "hello" then the list would be [h,e,l,l,o].

I forgot to mention that before this and validating the first guess, we actually get the random word
by calling the function random_word, and passing the level through it. The function uses a txt file that
contains over 1000+ english common words instead of importing a external source which would randomly pick
a word. I found using the txt better as it was easier to use and also the words in the txt are all common
english words we all use however if i imported it from an external source, some of the words actually
are illogical or from a different language. So txt was the best approach. To open this file i used the
knowledge i gained from cs50 by using with open(...) and then reading the file with read.splitlines().
Then after this we make a variable words and equal it to [word for word in temp if len(word) == level]
which basically only randomises words equal to the level which we picked before(also the level that
we got from before was increased by 2 to indicate the letters, so for example by inputting level 1,
level becomes the value 3). Then after this we randomise the certain word length and then print the
statement which states what the word length is for the user. In this theres two if statements which helps
to print these statements. The if statement checks if level is 5(by picked level 3 initially) or if the
level is 3,4(by picking level 1 or 2). By doing this we can print "level" in the statement if its 3 or 4
word length but if its 5+ we have to print len(answer) because level will only say the length is 5 when it
could be higher than 5.

After the user inputs his guess and we go call both functions we then get to the actual algorithm section where
we determine if the word[j] equals answer[j] in other words if each letter in each word matches each other in
the correct positions. So basically if word[j] has the same letter in the same position compared to answer we
then change the letter to green, indicating that that letter is correct. We change the letter to green with
this algorithm, word[j] = "\033[32m" + words[j] + "\033[0m". We then use another for loop to check if the
letter is correct but in the wrong position compared to answer which will then turn the letter to orange
to indicate this. Then if the condictions of both the if loops in the two for loops are invalid, then we leave
the letter white to indicate its the wrong letter and wrong position. We use the letters list for this objective
because say there was one "e" in the answer but but the user inputed two, then "e" would be green if in the correct
position and orange but in reality only one should be green/orange and one should be white. So to tackle this
i used the letters which contains a list of the answer. So when the if loop in the for loop is valid, we take away
that letter (word[j]) in the letters. So for example if the condition to turn the letter green is valid,
we make the letter green and take the letter away from letters. By doing this we make sure we dont copy any letters
Then we print the word with print("".join(word)) which has the word the user guessed with and includes the coloured
letters.

Then we check if the word the user guessed is equal to the randomised word(answer) and if it is we print congrats
and print how many guesses it took for the user to guess the word.

If the user took 5 guesses and didnt guess the word, we print that they lost and what the word was.

Depending on if they win or lose we then call the end() function which asks the user if they want to try again
by asking them to Y or N and validating to make sure either Y or N is inputted. If N is inputted then we exit the
project but if they input Y then we start again.
