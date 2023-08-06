# King's Quest VI Randomizer

This is a (under construction) program that shuffles the locations of items in King's Quest 6. You still have to fulfill all of the normal conditions to pick up an item, but when it enters your inventory, it will be a different item from usual. This creates brand-new surprising ways to softlock yourself, so as always in King's Quest VI, make a lot of saves! The randomizer is designed to always generate a long-path-beatable game, but there may be some oversights in the logic. The logic does not care if you can finish short path or not, but it will often be possible.

Any container (such as the teacup) will be filled at the USUAL LOCATION. These liquids are technically not items unto themselves, and they are not shuffled (at least in the first version of the randomizer).

All items are USED in the same way as the vanilla game, with one exception. When trading items BACK to the shopkeeper after obtaining them, he will only take the SHUFFLED item. So for example, if the nightingale has been shuffled to be a handkerchief instead, you need to trade back the handkerchief to get a different item, not the nightingale. This applies to whatever replaces the map as well as whatever replaces the items on the counter. Be careful to not consume these items too early!

The decompiled game scripts have some (under construction) item numbers and room numbers replaced with a string (plus verb numbers for the tradables). The python script (under construction) decides where the items should be shuffled to, and then replaces those strings with the replacement item. The scripts can then be placed into the game folder, the game can be loaded into SCI Companion, and the randomized version of the game can be played. The scripts will only take effect if the game is run through SCI Companion: it can still be played normally outside of SCI Companion. The scripts can be replaced with newly-randomized scripts to shuffle the items again.

This project is built on top of SCI scripts created by Sierra and decompiled by sluicebox.

Original readme for decompiled scripts below.

# Sierra Creative Interpeter - Scripts

This repository contains decompiled scripts for Sierra's SCI games.

- All games: King's Quest IV (1988) - Leisure Suit Larry 7 (1996)
- All platforms: DOS, Amiga, Atari ST, Macintosh, PC-98, FM-Towns, Windows
- All scripts: 100% decompiled
- Allotta versions: 300+

Scripts are the code that make up each game. The originals were written in Sierra's proprietary programming language and compiled to bytecode. The scripts in this repository are generated from that bytecode by my decompiler and heavily auto-annotated for readability. If you're familiar with a game, you should recognize a lot. If you want to learn how a game's puzzle works (or *doesn't*) then try searching for nearby game text.

## How Do I Use These?

The code is in the `.sc` text files. If you just want to casually browse, you can ignore everything else. But if you're serious...

The best way to view scripts is with SCI Companion, a Windows program that lets you view resources and create games. You will also need the game. Find your version in this repository and copy the files to your game directory. Open the game with SCI Companion and it will recognize the scripts as if it had generated them. SCI Companion doesn't support every game and version, but it works with most.

- SCI Companion site: http://scicompanion.com/
- SCI Companion repo, has newer code than the site: https://github.com/icefallgames/SCICompanion/
- SCI Companion fork, has nightly builds: https://github.com/Kawa-oneechan/SCICompanion/

## Can I Compile These?

Maybe! If SCI Companion fully supports the game, then it can compile most scripts. You may need to fix a Sierra bug or two, or make some other adjustments to make SCI Companion happy. My goal is to show what's really going on in the scripts, bugs and all.

## What Are The Files?

- `*.sc`: Script files
- `*.sco`: Script object files that SCI Companion needs for compiling
- `src`: SCI Companion needs `.sc` and `.sco` files to be in this directory
- `game.ini`: SCI Companion needs this file to find the scripts

If you don't care about compiling, you don't need the `.sco` files. If you don't use SCI Companion, you only need the `.sc` files.

## Why All English?

Localized text has been replaced with the original English for script diffing. How else will you find Italian Phantasmagoria's exclusive bug fixes? Or the not-so-temporary test code that ruins Spanish EcoQuest?

## Whodunnit?

This repository is dedicated to every Sierra reverse engineer from the past 35 years. And Sierra's real engineers too. You're all insane! And you all made this possible!

## Tell Me More

- https://www.benshoof.org/blog/sci-scripts
- https://mtnphil.wordpress.com/2016/04/09/decompiling-sci-byte-code-part-1/
- https://mtnphil.wordpress.com/2016/04/09/decompiling-sci-part-2-control-flow/
- https://mtnphil.wordpress.com/2016/04/09/decompiling-sci-part-3-instruction-consumption/
- https://mtnphil.wordpress.com/2016/04/09/decompiling-sci-part-4-final-steps/

## SCI Games

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
|`brain1`         | The Castle of Dr. Brain                                                        |
|`brain2`         | The Island of Dr. Brain                                                        |
|`camelot`        | Conquests of Camelot                                                           |
|`cb`             | The Colonel's Bequest                                                          |
|`cnick`          | Crazy Nick's Software Picks                                                    |
|`eco1`           | EcoQuest: The Search for Cetus                                                 |
|`eco2`           | EcoQuest II: Lost Secret of the Rainforest                                     |
|`fairytales`     | Mixed-Up Fairy Tales                                                           |
|`fpfp`           | Freddy Pharkas: Frontier Pharmacist                                            |
|`gk1`            | Gabriel Knight: Sins of the Father                                             |
|`gk2`            | Gabriel Knight 2: The Beast Within                                             |
|`goose`          | Mixed-Up Mother Goose (SCI Remake)                                             |
|`goosevga`       | Mixed-Up Mother Goose (VGA Remake)                                             |
|`goosedeluxe`    | Mixed-Up Mother Goose Deluxe                                                   |
|`hoyle1`         | Hoyle's Official Book of Games: Volume 1                                       |
|`hoyle2`         | Hoyle's Official Book of Games: Volume 2                                       |
|`hoyle3`         | Hoyle's Official Book of Games: Volume 3                                       |
|`hoyle4`         | Hoyle Classic Card Games                                                       |
|`hoyle5`         | Hoyle Classic Games                                                            |
|`hoyle5solitaire`| Hoyle Solitaire                                                                |
|`iceman`         | Codename: ICEMAN                                                               |
|`jones`          | Jones in the Fast Lane                                                         |
|`kq1`            | King's Quest: Quest for the Crown (SCI Remake)                                 |
|`kq4`            | King's Quest IV: The Perils of Rosella                                         |
|`kq5`            | King's Quest V: Absence Makes the Heart Go Yonder                              |
|`kq6`            | King's Quest VI: Heir Today, Gone Tomorrow                                     |
|`kq7`            | King's Quest VII: The Princeless Bride                                         |
|`lighthouse`     | Lighthouse: The Dark Being                                                     |
|`longbow`        | Conquests of the Longbow                                                       |
|`lsl1`           | Leisure Suit Larry in the Land of the Lounge Lizards (SCI Remake)              |
|`lsl2`           | Leisure Suit Larry Goes Looking for Love (in Several Wrong Places)             |
|`lsl3`           | Leisure Suit Larry 3: Passionate Patti in Pursuit of the Pulsating Pectorals   |
|`lsl5`           | Leisure Suit Larry 5: Passionate Patti Does a Little Undercover Work           |
|`lsl6`           | Leisure Suit Larry 6: Shape Up or Slip Out                                     |
|`lsl7`           | Leisure Suit Larry 7: Love for Sail                                            |
|`pepper`         | Pepper's Adventures in Time                                                    |
|`phant1`         | Phantasmagoria                                                                 |
|`phant2`         | Phantasmagoria 2: A Puzzle of Flesh                                            |
|`pq1`            | Police Quest: In Pursuit of the Death Angel (SCI Remake)                       |
|`pq2`            | Police Quest II: The Vengeance                                                 |
|`pq3`            | Police Quest III: The Kindred                                                  |
|`pq4`            | Police Quest IV: Open Season                                                   |
|`pqswat`         | Police Quest: SWAT                                                             |
|`qfg1`           | Quest for Glory: So You Want to Be a Hero                                      |
|`qfg1vga`        | Quest for Glory: So You Want to Be a Hero (VGA Remake)                         |
|`qfg2`           | Quest for Glory II: Trial by Fire                                              |
|`qfg3`           | Quest for Glory III: Wages of War                                              |
|`qfg4`           | Quest for Glory IV: Shadows of Darkness                                        |
|`ra`             | The Dagger of Amon Ra                                                          |
|`rama`           | RAMA                                                                           |
|`shivers`        | Shivers                                                                        |
|`slater`         | Slater & Charlie Go Camping                                                    |
|`sq1`            | Space Quest I: Roger Wilco in the Sarien Encounter (SCI Remake)                |
|`sq3`            | Space Quest III: The Pirates of Pestulon                                       |
|`sq4`            | Space Quest IV: Roger Wilco and the Time Rippers                               |
|`sq5`            | Space Quest V: The Next Mutation                                               |
|`sq6`            | Space Quest 6: The Spinal Frontier                                             |
|`torin`          | Torin's Passage                                                                |