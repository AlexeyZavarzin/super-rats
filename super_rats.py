import random
import statistics

from config import NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, \
    INITIAL_MODE_WT, GOAL, GENERATION_LIMIT, LITTER_SIZE, \
    MUTATE_MAX, MUTATE_MIN, MUTATE_ODDS, LITTER_PER_YEAR
from mutate import mutate
from select import select


def get_populate(num_rats, min_wt, max_wt, mode_wt):
    return [int(random.triangular(min_wt, max_wt, mode_wt))
            for _ in range(num_rats)]


def get_value_fitness(population, goal):
    return statistics.mean(population) / goal


def breed(males, females, litter_size):
    random.shuffle(males)
    random.shuffle(females)
    children = []

    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)

    return children


def main():
    generations = 0
    parents = get_populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT,
                           INITIAL_MODE_WT)
    print(f'первоначальные веса популяции = {parents}')

    populations_fitness = get_value_fitness(parents, GOAL)
    print(f'первоначальная приспособленность популяции = {populations_fitness}')
    print(f'число крыс в начальной популяции = {NUM_RATS}')

    ave_wt = []

    while populations_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        populations_fitness = get_value_fitness(parents, GOAL)

        print(f'приспособленность поколения {generations} = {populations_fitness}')
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1

    print(f'средний вес на поколение = {ave_wt}')
    print(f'\nчисло поколений = {generations}')
    print(f'число лет {int(generations / LITTER_PER_YEAR)} ')
