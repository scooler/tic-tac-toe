Tic-Tac-Toe
------------

(or Kółko i Krzyżyk in Polish)


I had an idea to write some simple game, to play around with some AI ideas, see what happens. I tried the pygame but on
OSX it's a pain, so it's mainly ASCI (as it's not about UI :D ).


To run
```
python main.py
```

To gather stats (multiple runs and compare - best works for auto players)
```
python stats.py
```

There are at this point a couple Displays supported (ASCI, Pygame, Null - file is coming)
And some "input strategy" - console/numeric keyboard, mouse on UI, Random pick, Basic Rule-based AI

Those are in oder:
- 'C' (console, ASCI)
- 'P' (pygame)
- 'R' (Random)
- '1' (AI v1) - rule based, just to prevent oponent from wining + fallback to random
- '2' (AI v2) - rule based - win if you can, otherwise fallback to v1
- '3' (AI v3) - score based - looks 1 step ahead - which step will result in board "most in his favor". 1 for your pair, -1 for oponent's 100 for winning - 100 for loosing
- '4' (AI v4) - score based - looks n steps ahead (playing both it's, and oponent's part). Than picks up the move resulting in the best result in the long run
