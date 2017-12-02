# FE:H Hero Merit Evaluator

A (very) quick and dirty program to analyze Hero Merit data for Fire Emblem:Heroes.

# Instructions:

1. Install Python 3 (uses v.3.6.1)
2. Download the .py file and download or create an "input.txt" file. Make sure the input file is in the same directory.
3. Open the Fire Emblem Heroes app and use your Hero Merit page to fill out the input file. 
 - Each line in the input file should contain a hero merit number followed by the corresponding hero name, separated by a single space.
 - Hero names should not contain any spaces. Use whatever syntax you like for heroes with complex names (eg. BraveIke, Brave_Ike, B!Ike, etc).
4. Run HeroMeritEvaluator.py by opening a command line / terminal and navigating to the directory containing the HeroMeritEvaluator.py program. Then type 'python HeroMeritEvaluator.py' to run the program. The results will be printed to the terminal window.

# Output:

The program will output the following information:

- Total Percent Complete (toward maxing Hero Merit for all of your heroes)
- Number of heroes with max Hero Merit
- Total amount of feathers gained so far from the Hero Merit system
- Total amount of feathers remaining to be gained
- The top ten closest heroes to reaching a new Hero Merit milestone to gain 500 feathers
- Percentage breakdown of your heroes by HM tier (eg % of heroes between 1000-1499 HM)

# Contact / Support

For questions or support, message u/ShiningSolarSword on reddit.
