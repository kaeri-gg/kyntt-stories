# kynnt-stories
Level design prototype using Kyntt 
Created by Sunny and Kath <3 

## How to run
- Open the **Level Editor Plus.exe file** - to load the levels,
- Select the **"Masaru-Level"** and click **"Load Level"**
- Click the **Test Level** to test it (make sure u save it first before test level)
- <img width="530" height="484" alt="image" src="https://github.com/user-attachments/assets/7f9c525e-e46d-49c4-a5a6-53561ec4fca3" />
- Then place the character anywhere in the map.
- You can see that the Test Level becomes yellow, it means its waiting for you to place the character in the map.
- <img width="529" height="484" alt="image" src="https://github.com/user-attachments/assets/fde45d55-f12a-4919-80d1-7c46f602b666" />


## IMPORTANT: Placing the object and the tilesets
- If you look at 0-3 and 4-7 numbers below, it means the following:
  - 0-2 = You can use this as a background (trees, colors, etc. ) - this doesnt collide with your player.
  - 3 = Select 3, if you're working on floors, doors, wall - something that collides with player
  - 4-7 = You can add objects in this like enemies, insects, traps, powerups.
<img width="1063" height="125" alt="image" src="https://github.com/user-attachments/assets/e9078ddd-f94e-4f75-a0ee-2a25ea0412e5" />

## Basics to start around level design:
- Make sure you are in the right place. Select 0-2 for background, 3 for floors.
- You can use 2 tileset to design your level - The A and B below image.
- Click on either A or B to switch the tileset.
- And click the number (the one beside the A or B with green highlight) to select tileset.
- When u click it, **left click** means next, **right click** means previous. 
<img width="536" height="241" alt="image" src="https://github.com/user-attachments/assets/60d9f609-d03a-4684-a790-bb0056b87964" />

## Adding objects (insects, birds, powerups, enemies)
- If you want to add objects, make sure you are in the right place. See below image, the active place is 4, this is where i want to place objects for example. Just click it to select between 0-7. 
- Next, click the Bank - this contains all the object you can add in your level.
- Then select the objects like how you select a tileset using left and right click. 
<img width="542" height="262" alt="image" src="https://github.com/user-attachments/assets/b552bb57-77ce-475e-b409-b43aaa4e0ce5" />



That's it! Exporting it as a game to me is unknown. So we just use it like that during the playtesting. 

## Downloads (on itch.io)

The game ships as **two separate downloads** on
[kaeri-gg.itch.io/kyntt-stories](https://kaeri-gg.itch.io/kyntt-stories) — pick whichever suits you:

**1. Standalone bundle (`windows` channel)** — easiest, no setup.
- Download the zip and unzip it anywhere.
- Run **`Knytt Stories Plus 1080.exe`**.
- Select **Masaru** (by KathAndSunny) from the level list.
- Pick a save slot, then click **Start New Game**.
- Includes the Knytt Stories Plus engine, so you don't need anything else.

**2. Level file only (`knytt-bin` channel)** — for people who already have Knytt Stories.
- Download `Masaru.knytt.bin`.
- Drop it into your `Knytt Stories\Worlds\` folder (Knytt Stories installs it automatically), **or**
  open Knytt Stories → *Install Level* and pick the file.
- Start it the same way: select **Masaru**, pick a slot, **Start New Game**.

## Controls

Keyboard defaults (all rebindable from the main menu → **Set Controls**):

| Key | Action |
| --- | --- |
| ← / → | Walk |
| **X** (hold) | Run |
| **Z** | Jump — press again in mid-air for **Double Jump** |
| **↑** (hold) | Climb (against a climbable wall) |
| **Shift** (hold) | Umbrella — glide down slowly |
| **Esc** | Pause / menu |
| **F12** | Show screen coordinates (handy while designing) |

This level starts you with **Run, Climb and Double Jump** already unlocked.

## Releasing to itch.io

This repo publishes to [kaeri-gg.itch.io/kyntt-stories](https://kaeri-gg.itch.io/kyntt-stories)
automatically when you push a version tag:

```
git tag v1.0.0
git push origin v1.0.0
```

The CI workflow (`.github/workflows/deploy.yml`) repacks `Worlds/Masaru-Level` into a
`.knytt.bin` and uploads two downloads: the level file (`knytt-bin` channel) and a
standalone Windows bundle (`windows` channel). Built on Knytt Stories — http://knytt.ni2.se


