###################################################
# ~ Hero Merit Evaluator by u/ShiningSolarSword ~ #
###################################################

MAX_HERO_MERIT = 3000

class HeroMeritItem:
    def __init__(self, merit, hero):
        self.merit = merit
        self.hero = hero
        self.feathers_gained = (merit // 500) * 500
        self.feathers_remaining = MAX_HERO_MERIT - ((merit // 500) * 500)
        self.distance_from_next_milestone = (500 - (merit % 500))
        self.maxed = 1 if (merit == MAX_HERO_MERIT) else 0

class HeroMeritList:
    def __init__(self, hmlist):
        self.heromeritlist = hmlist
        self.number_of_heroes_with_max_merit = 0
        self.total_feathers_gained = 0
        self.total_feathers_remaining = 0
        self.total_number_of_heroes = 0
        self.total_amount_of_merit = 0
        self.total_percent_complete = 0
        self.tier3000 = 0
        self.tier2500_2999 = 0
        self.tier2000_2499 = 0
        self.tier1500_1999 = 0
        self.tier1000_1499 = 0
        self.tier500_999 = 0
        self.tier0_499 = 0

    def process_list(self):
        for heromerititem in self.heromeritlist:
            self.number_of_heroes_with_max_merit += heromerititem.maxed
            self.total_feathers_gained += heromerititem.feathers_gained
            self.total_feathers_remaining += heromerititem.feathers_remaining
            self.total_number_of_heroes += 1
            self.total_amount_of_merit += heromerititem.merit                
        self.total_percent_complete = ((self.total_amount_of_merit) / (MAX_HERO_MERIT * self.total_number_of_heroes)) * 100

        for heromerititem in self.heromeritlist:
            if (heromerititem.merit == 3000):
                self.tier3000 += 1
            elif (heromerititem.merit >= 2500 and heromerititem.merit <= 2999):
                self.tier2500_2999 += 1
            elif (heromerititem.merit >= 2000 and heromerititem.merit <= 2499):
                self.tier2000_2499 += 1
            elif (heromerititem.merit >= 1500 and heromerititem.merit <= 1999):
                self.tier1500_1999 += 1
            elif (heromerititem.merit >= 1000 and heromerititem.merit <= 1499):
                self.tier1000_1499 += 1
            elif (heromerititem.merit >= 500 and heromerititem.merit <= 999):
                self.tier500_999 += 1
            elif (heromerititem.merit >= 0 and heromerititem.merit <= 499):
                self.tier0_499 += 1

    def closest_heroes_to_milestones(self):
        return sorted(self.heromeritlist, key=lambda x: x.distance_from_next_milestone)

# Read the input into HeroMeritItems and append to a list:
hmlist = []
f = open('input.txt', 'r')
for line in f.readlines():
    data = line.split()
    hmlist.append(HeroMeritItem(int(data[0]), data[1]))
heromeritlist = HeroMeritList(hmlist)
heromeritlist.process_list()
f.close()

# Print Report:
print("\n---------------------")
print("| HERO MERIT REPORT |")
print("---------------------\n")
print("%.2f%% Complete\n" % heromeritlist.total_percent_complete)
print("Your total cumulative Hero Merit amassed is {}\n".format(heromeritlist.total_amount_of_merit))
print("{} heroes have maxed Hero Merit\n".format(heromeritlist.number_of_heroes_with_max_merit))
print("{} feathers have been gained".format(heromeritlist.total_feathers_gained)) 
print("{} feathers remain to be harvested\n".format(heromeritlist.total_feathers_remaining))
print("The top ten closest heroes to reaching a new Hero Merit milestone are: ")
list_sorted_by_closest = heromeritlist.closest_heroes_to_milestones()
names = []
for heromerititem in heromeritlist.closest_heroes_to_milestones():
    names.append(heromerititem.hero)
w = len(max(names, key=len))
print(" 1.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[0].hero, width=w, merit=list_sorted_by_closest[0].merit)) 
print(" 2.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[1].hero, width=w, merit=list_sorted_by_closest[1].merit)) 
print(" 3.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[2].hero, width=w, merit=list_sorted_by_closest[2].merit)) 
print(" 4.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[3].hero, width=w, merit=list_sorted_by_closest[3].merit)) 
print(" 5.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[4].hero, width=w, merit=list_sorted_by_closest[4].merit)) 
print(" 6.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[5].hero, width=w, merit=list_sorted_by_closest[5].merit)) 
print(" 7.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[6].hero, width=w, merit=list_sorted_by_closest[6].merit)) 
print(" 8.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[7].hero, width=w, merit=list_sorted_by_closest[7].merit)) 
print(" 9.  {hero: <{width}} at {merit: <4} HM".format(hero=list_sorted_by_closest[8].hero, width=w, merit=list_sorted_by_closest[8].merit)) 
print(" 10. {hero: <{width}} at {merit: <4} HM\n".format(hero=list_sorted_by_closest[9].hero, width=w, merit=list_sorted_by_closest[9].merit)) 
print("HM Tier Breakdown: ")
print("3000 (MAX)  : %.2f%%" % ((heromeritlist.tier3000/heromeritlist.total_number_of_heroes)*100))
print("2500 - 2999 : %.2f%%" % ((heromeritlist.tier2500_2999/heromeritlist.total_number_of_heroes)*100))
print("2000 - 2499 : %.2f%%" % ((heromeritlist.tier2000_2499/heromeritlist.total_number_of_heroes)*100))
print("1500 - 1999 : %.2f%%" % ((heromeritlist.tier1500_1999/heromeritlist.total_number_of_heroes)*100))
print("1000 - 1499 : %.2f%%" % ((heromeritlist.tier1000_1499/heromeritlist.total_number_of_heroes)*100))
print("500 - 999   : %.2f%%" % ((heromeritlist.tier500_999/heromeritlist.total_number_of_heroes)*100))
print("0 - 499     : %.2f%%" % ((heromeritlist.tier0_499/heromeritlist.total_number_of_heroes)*100))


