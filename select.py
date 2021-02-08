def select(population, to_retain):
    sorted_population = sorted(population)

    to_retain_by_sex = to_retain // 2
    members_per_sex = len(sorted_population) // 2

    males = sorted_population[members_per_sex:]
    selected_males = males[-to_retain_by_sex:]

    females = sorted_population[:members_per_sex]
    selected_females = females[-to_retain_by_sex:]

    return selected_males, selected_females
