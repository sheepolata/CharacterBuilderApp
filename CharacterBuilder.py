import random


class DrawMethods(object):
    FOUR_DICE = 0
    THREE_DICE = 1
    FAIR = 2


class CoreStatistics(object):
    def __init__(self, stats_name):
        self.stats_name = stats_name
        self.stats = {}
        for c in self.stats_name:
            self.stats[c] = 0

    def draw_stats(self, method, primary_stat, secondary_stat):
        if primary_stat not in self.stats.keys():
            raise AttributeError(f"primary_stat \"{primary_stat}\" is not in this CoreStatistics instance")
        if secondary_stat not in self.stats.keys():
            raise AttributeError(f"secondary_stat \"{secondary_stat}\" is not in this CoreStatistics instance")

        draw_values = []
        if method == DrawMethods.FOUR_DICE:
            for _ in range(len(self.stats.keys())):
                dices = random.sample(range(1, 7), 4)
                print(dices)
                dices.sort(reverse=True)
                draw_values.append(sum(dices[:3]))
        elif method == DrawMethods.THREE_DICE:
            dices = random.sample(range(1, 7), 3)
            draw_values.append(sum(dices))
        elif method == DrawMethods.FAIR:
            for _ in range(3):
                _dice = random.randint(1, 6) + random.randint(1, 6)
                draw_values.append(6 + _dice)
                draw_values.append(19 - _dice)
        else:
            raise TypeError("method must be from the DrawMethods enum (class)")

        draw_values.sort(reverse=True)
        remainder = draw_values[2:]
        random.shuffle(remainder)

        self.stats[primary_stat] = draw_values[0]
        self.stats[secondary_stat] = draw_values[1]

        print(draw_values)
        for v, s in zip(remainder, self.stats.keys() - [primary_stat, secondary_stat]):
            self.stats[s] = v


if __name__ == "__main__":
    core = CoreStatistics(["FOR", "DEX", "CON", "INT", "WIS", "CHA"])

    core.draw_stats(DrawMethods.FOUR_DICE, "FOR", "CON")

    print(core.stats)
