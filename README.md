# Are-You-the-One-Reality-Show-Solver
This repo contains a generic solver for the reality dating show Are you the One (https://en.wikipedia.org/wiki/Are_You_the_One)


To run, please call the script in python along with an argument for the number of contestants
python ayto.py \< n \> where n is the number of contestants.
eg: python ayto.py 5
E:\Downloads>python ayto.py 5

--------------------------------
Starting: Are You the One Solver

Initializing for 5 contestants

True sequence is
(2, 0, 4, 3, 1)

Guesses were

[(1, 3, 0, 4, 2), (0, 1, 2, 3, 4), (1, 4, 3, 2, 0), (0, 2, 4, 1, 3), (2, 0, 4, 3, 1)]

Score Hints were

['0', '1', '0', '1', '5']

We solved it

--------------------------------

Are you the One (https://en.wikipedia.org/wiki/Are_You_the_One) is a reality show
which randomly pairs an even number of boys and girls
as being "perfect" matches according to some dubious matchmaking formula. Each boy and girl has exactly
one perfect match that is decided beforehand and for N couples,
they have N tries over the course of the show to guess exactly right
all N matches simultaneously. The only feedback the contestants get for
a given guess is the number of correct matches they have made across all N couples
for a given unique guess configuration. A unique guess configuration requires all 
N couples be paired up for the given guess. The structure of this problem almost
exactly matches the game Mastermind except you basically know all the given colors in 
the code beforehand, all the colors are unique, and you are simply trying to guess
the unique pattern for the code. So, the "code" represents the boy configuration for example
and the guesses are the girls that pair up with them. We use the Donald Knuth algorithm and modify it
for the problem at hand where we basically enumerate every possible guess in a dictionary where each
entry contains every possible score for every possible guess combination. At a high level, for every guess
that we make, based on the score, we can eliminate every entry in the dictionary that would not have that
score for the given guess. Then for the next guess, we iterate through all the possible guesses that we
have not yet made and calculate the minimum number of unique configurations that would be eliminated if we made
that guess, then we pick the maximum of these choices. We then iterate through until our algorithm converges to the correct answer.
For N couples and N guesses, we can provably guarantee that we will converge on a solution before we are out of guesses even
in the worst case through induction and combinatorics analysis. The show is actually even easier because they have some mechanic called a truth booth which
definitively tells you whether or not a couple is a perfect match which I think they get a couple of uses per season.
Also, I promise I'm not trying to be a stick in the mud! I like the show! Was just curious about how you might go about solving it.


