import sys
import random
import itertools
import collections

def score_guess(guess, ans):
    # iterates through guess and answer lists element-by-element. Whenever it finds a match,
    # increments score for this guess by 1
    score = 0;
    for guess_elem, ans_elem in zip(list(guess), list(ans)):
        if guess_elem == ans_elem:
            score = score + 1;
    return str(score);

def build_dict(n):
    # default dict avoids storing keys as tuple, saves lookup time
    score_dict = collections.defaultdict(dict)
    all_guesses = list(itertools.permutations(range(0, (n))))
    for guess, answer in itertools.product(all_guesses, repeat=2):
        guess_str = "".join(str(guess))
        ans_str = "".join(str(answer))
        score_dict[guess_str][ans_str] = score_guess(guess, answer)
    return score_dict


class AYTOSolver:
    def __init__(self, num_contestants, answer):
        self.answer_list = list(itertools.permutations(list(range(0, (num_contestants)))))
        self.answer_list = {str(answerTemp) for answerTemp in self.answer_list}
        self.answer = answer
        self.guesses_left = num_contestants
        self.contestants = num_contestants
        self.score_dict = build_dict(num_contestants)
        self.guess_history = []
        self.hint_history = []

    def make_guess(self):
        guesses_to_try = []
        for guess, scores_by_answer_dict in self.score_dict.items():
            # reduce possible_score_dict to only include possible answers
            scores_by_answer_dict = {answer: score for answer, score in scores_by_answer_dict.items()
                                     if answer in self.answer_list}
            self.score_dict[guess] = scores_by_answer_dict

            # find how often a score appears in scores_by_answer_dict, get max
            possibilities_per_score = collections.Counter(scores_by_answer_dict.values())
            worst_case = max(possibilities_per_score.values())

            # prefer possible guesses over impossible ones
            impossible_guess = guess not in self.answer_list

            guesses_to_try.append((worst_case, impossible_guess, guess))

        return eval(min(guesses_to_try)[-1])
        
    def solve(self):
        while self.guesses_left > 0:
            if self.guesses_left == self.contestants:
                guess = tuple(random.sample(range(self.contestants), self.contestants));
            else:
                guess = self.make_guess()

            self.guess_history.append(guess)
            # reduce amount of possible answers by checking answer against guess and score
            score = score_guess(guess, self.answer)
            self.hint_history.append(score)
            self.answer_list = {answer for answer in self.answer_list
                                if self.score_dict[str(guess)][answer] == score}
            self.guesses_left -= 1
            if str(guess) == str(self.answer):
                return self.guess_history, self.hint_history
        
        return self.guess_history, self.hint_history

print >>sys.stderr, '--------------------------------'
print >>sys.stderr, 'Starting: Are You the One Solver'

num_contestants = int(sys.argv[1])


print >>sys.stderr, 'Initializing for %s contestants' % num_contestants

true_sequence = tuple(random.sample(range(num_contestants), num_contestants));
print("True sequence is ");
print(true_sequence);


#sys.exit();
solver = AYTOSolver(num_contestants=num_contestants, answer=true_sequence);

tempDict = solver.score_dict;
guesses, hints = solver.solve();

print("Guesses were ");
print(guesses);
print("Score Hints were")
print(hints);

if(guesses[-1] == true_sequence):
    print("We solved it")
else:
    print("We messed up")

print >>sys.stderr, '--------------------------------'
