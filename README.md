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
- '1' (AI v1)
