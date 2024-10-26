# Rantoni Assets

Everything regarding the game Rantoni that doesn't directly have to do with the game is in here. It's more like a dirty repo where I don't exactly try to keep a super clean history or small git dir size.

## Gameplay

### AI

#### Pathfinding

- `https://www.radicalfishgames.com/?p=186`
- `https://www.radicalfishgames.com/?p=498`
- `https://github.com/bevyengine/bevy/discussions/558`
- `https://www.youtube.com/watch?v=J7mFjlyScHA`

### Attacks

Bro, hear me out. Holding down light/heavy attack will trigger a "charged version", for the light attack it will be a continous stream of strikes that start slow and get faster and faster (like a gatling gun), the player is moving forward while doing this, similar to the one attack from wizards of legends with the ice melee attack. The heavy attack charges until a max is hit, when the player releases the character first stomps on the ground real hard, sending all his enemies around him to get fling into the air (though no knockback, just up), then the player jumps up and performs a sick ass all round house heel kick, sending all the enemies into oblivion.

I think this would also make for a great trailer ending.

KILL. THEM. ALL. Then baaam, the hit of the heavy attack or the light attack getting faster and faster with each word.
LEAVE. NO. SURVIVORS.
EVERYBODY. MUST. DIE

### Playtesting, QA

Testing niddy griddy like player stats (movement speed, attack speed bla bla bla) can be easily done by having a txt file or ron file and letting the testers just adjust those values and then hot reload the game state to reflect the changes.

Also allows for easily copy/pasting configs.

### Juice

- Destructable objects, sending enemies through walls is so much fun in Redeemer, should have that too

### Regarding Player Movement with Mouse and Keyboard

I am fairly sure that when playing with mouse and keyboard you would want to use your mouse for the target area. Using attack direction = move direction is just super ass. Dominik was the one who proposed it, but I think he will agree that it feels kinda shit (and just way too inaccurate) once he plays it that way.

## Game References

- Redeemer
    - For game feel and gameplay
- Midnight fight express
    - gameplay
- Hades
    - Partially for game feel
    - Animation statemachine
- Wizards of Legends
    - Animations
- Akane
    - Not a great gameplay reference, though I think the enemies have really small anticipation, how does that work?
- CrossCode
    - Leveldesign
- Katana Zero
    - Absolutely amazing tutorial
    - Also game juice

## Art References

- Akane
    - General vibe
- `https://guttykreum.itch.io/dark-tokyo-game-assets`
    - For the tileset, something like this should work, I also realized we don't really need 2x2 tileset mapping, it's modern so there are clear cuts pretty much everywhere
- Katana Zero
    - General vibe

## Logic References

- CrossCode
    - `https://www.radicalfishgames.com/?p=498`

## Expenses

- Steam Capsule art
    - Really don't want to spend more than 500 bucks on this
    - Don't be too cheap with this, also we can't really do this later, better to get it right the first time
- Music
    - Bro if I can get noisecream to work on this... dude
    - Though I really, REALLY don't want to spend more then 500 bucks on this, preferable is something like 300 but I doubt that will work
    - Though this can also be budgeted like max 500 at first and then, if there are more whishlists than expected, you can take a bit more cash in the hand and get some more songs, this way you have somewhat of a dynamic budget and don't overhire as badly

## Marketing

### Talks

- `https://www.youtube.com/watch?v=UJiv14uPOac`
- `https://www.youtube.com/watch?v=EMGTcgsEN68`
- `https://www.youtube.com/watch?v=ht6xx9en-ZU&t=21s`

### Specific unique marketing

- Reach out to Ranton, tell him about the game and also ask if he wants to be part, as for example a story writer (also partially marketing in terms of videos or similar content creation)
- Regardless of whether or not Ranton will actually agree to join, we can definitely do some posts on his subreddit as the game was inspired by him
- Events or leaderboard stuff on discord or some similar form of competition (probably not because it's too much work)

### General Stuff

- Localize steam page!

Just some rough plans for what you can do for marketing. Will probably not be able to do everything.

- Some pointers for reference
    - `https://github.com/tutsplus/Marketing-Checklist-For-Indie-Game-Developers/blob/master/Indie%20Game%20Developer%20Marketing%20Checklist.md`
- Set up press kit and host on server
- Discord server
    - Possible moderators: Eric, Ivan, Alex? (uni)
- Send out steam keys to streamers/youtubers and ask them to play the game
- Reach out to press/blogs etc
- Youtube Videos (game dev logs) about the game
- Bevy Community
    - Share on main bevy discord server (in showcase channel for example)
    - Possibly post on some more niche bevy servers like specific crates?
    - Put game on assets page
- Lost Oppai Game Dev with Rantoni mention at the end (probably kinda cheeky, but oh well)
    - In this case doing a little bit of marketing for Lost Oppai may actually end up helping this game as well, though probably only way too indirectly and not really worth the extra effort? Well you could at least post it on yarnspinner discord

## Story

Generally I am pretty open as to what the story should be, I do think that a linear story is very much necessary though. Have levels and then you just play through them until you reach the end. Our target audience isn't really that niche or specific, so a simple linear story line should be better suited for a broader audience.

Now regarding the actualy story, I was thinking something pretty similar to Redeemer, some Monk (with maybe some connections of his past to gang or something like that) then an event happens and he is out for blood to kill gang members. Generally that would probably work, could also go with a more philosophically interesting story but I don't really mind too much.

Some gameplay ideas that could influence:
    - If we end up including policeman and civilians then at the very end with the final dude let him incoorporate the stats of the player, something like `Final Badguy: "I have read the reports you know... 276. Fucking 276 civilians! You are not any better than us. No, no you are even worse! You are a monster!`, or something along those lines. I think that could be a pretty cool reflection on the players choices throughout the game and maybe also hit them with a curve ball because they probably didn't think much of killing civilians in a game like this.

## Legal

### Localization

So there this happened to Jonas `https://youtu.be/MaFpf3nmHmo?t=798`, I personally think that if you had a github repo with a clear license like MIT that said clearly that anybody that would contribute will have their work licensed under MIT would make this essentially a non problem? Though I guess it would be better to ask a lawyer for that? But if this were a problem then wouldn't all of open source be at risk?
