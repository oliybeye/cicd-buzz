from __future__ import print_function
import random

buzz = ('continous testing', 'continous integration',
        'continous deployment', 'continuos improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service', 'intefrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
           'seriously')
verbs = ('acceclerates', 'improves', 'enhances', 'revamps', 'boosts')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
                       sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())
