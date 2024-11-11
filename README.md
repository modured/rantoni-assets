# Rantoni Assets

Everything regarding the game Rantoni that doesn't directly have to do with the game is in here. It's more like a dirty repo where I don't exactly try to keep a super clean history or small git dir size.

Overall a great reference for what NOT to do is in the game Redeemer, boy oh boy does that game screw up.

## Gameplay

### Statemachine

- `https://www.gamedev.net/forums/topic/639005-how-to-handle-states-in-a-fighting-game/`
- `https://www.gamedev.net/forums/topic/637975-what-makes-a-good-beatem-up-game/`

### AI

- `https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter01_What_is_Game_AI.pdf`

- Don't you fucking dare to put bullet sponges in the game, bro just play Redeemer and you know what **not** to do
- I really think that multiple factions in the game would be sick, something like in Streets of Rogue (different gangs, police, mafia, etc)

#### Pathfinding

- `https://www.reddit.com/r/roguelikedev/comments/3slu9c/faq_friday_25_pathfinding/`
    - I think this is a great source of information on all sorts of topics

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

### Skills

Not really sure if I want to _implement_ these, but it would be cool to _play_ with these (at least in my head). So what I am thinking are skills that you use and then are on cooldown, really showy stuff.

- Link enemy-damage, when you punch on enemy, all linked enemies take damage the exact same way (same amount, same direction etc.)
    - Side note: I actually got this while debugging just now, there seems to be some kind of shared state that makes enemies either share hurtboxes or their state
- **DOMAIN EXPANSION**, bro that would be sick, maybe slow down time and do the Gojo thing he did in Shibuya, where you go through all enemies killing them
    - Could also be made so that it's a mix between Juggernauts ulti from Dota 2 and Gojo, so you slow down time, then the player is positioned in front of some enemy, he presses some attack button which pretty much instantly kills the enemy (maybe in like 0.1s), then telepored to the next enemy, then rince and repeat until either all enemies are dead in the AOE or the time runs out

### Playtesting, QA

Testing niddy griddy like player stats (movement speed, attack speed bla bla bla) can be easily done by having a txt file or ron file and letting the testers just adjust those values and then hot reload the game state to reflect the changes.

Also allows for easily copy/pasting configs.

### Juice

- Destructable objects, sending enemies through walls is so much fun in Redeemer, should have that too
- Experiment with camera responding to player (like dropkicking an enemy, should the camera move in a specific way?)

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
- Streets of Rogue
    - Factions and simulation based chaos/complexity
    - Giving different AI's different rules can result in very interesting and fun situations

## Art References

- Akane
    - General vibe
- `https://guttykreum.itch.io/dark-tokyo-game-assets`
    - For the tileset, something like this should work, I also realized we don't really need 2x2 tileset mapping, it's modern so there are clear cuts pretty much everywhere
- Katana Zero
    - General vibe
- Dead Cells
    - `https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-`
    - `https://www.youtube.com/watch?v=iNDRre6q98g`
    - `https://stackoverflow.com/questions/70362019/how-to-vectorize-an-image-using-python`

### Animation References

- Slide attacking feels a little weird, this looks kinda better, maybe send enemies flying a little instant of just instantly putting them on the ground? OHH! Maybe this would also make the colliders easi- yeah no, but it might make things better, maybe
    - `https://youtu.be/GbzdbDri3P8?t=32`
    - `https://youtu.be/GbzdbDri3P8?t=103`
- Oh! Maybe you could also use the same sliding for the drop kick, sending them flying and then they are grounded!
    - `https://youtu.be/rLvbwNAFGRQ?t=4738`
- Possible Jump animation and dropkick animation reference
    - `https://youtu.be/rLvbwNAFGRQ?t=4798`

### Blender Stuff

- `https://www.youtube.com/watch?v=AQcovwUHMf0`

## Logic References

- CrossCode
    - `https://www.radicalfishgames.com/?p=498`

### Map Collision/Navmesh Implementation

- Save the collision and navmesh data in a separate file (something handrolled).
- Store a hash of the whole data for each level as well
- Then before you calculate the level data, check the hash, if they are equal (nothing changed) then just go to the next
- Else go ahead and calculate the collision and navmesh node data for the level, then store it in some data struct (something simple will do)
- Finally when everything is done write the struct to the file

- In game you can load the level data into a Res struct on boot
- Then when you need to reference a level just get the Res with the level index or something and boom, there you got all your level data
    - Note that I might need to tweak this if it takes up too much memory, I mean it's only a bunch of vertices so it _should_ be fine, but you should extrapolate how much memory it will cost for like 200 levels or something

## Expenses

- Steam Capsule art
    - Really don't want to spend more than 500 bucks on this
    - Don't be too cheap with this, also we can't really do this later, better to get it right the first time
- Music
    - Bro if I can get noisecream to work on this... dude
    - Though I really, REALLY don't want to spend more then 500 bucks on this, preferable is something like 300 but I doubt that will work
    - Though this can also be budgeted like max 500 at first and then, if there are more whishlists than expected, you can take a bit more cash in the hand and get some more songs, this way you have somewhat of a dynamic budget and don't overhire as badly
- Legal shit? Should we talk with a lawyer or do we need to register a company (GmbH?)

## Marketing

### Talks

- `https://www.youtube.com/watch?v=UJiv14uPOac`
- `https://www.youtube.com/watch?v=EMGTcgsEN68`
- `https://www.youtube.com/watch?v=ht6xx9en-ZU&t=21s`

### Specific unique marketing

- Reach out to Ranton, tell him about the game and also ask if he wants to be part, as for example a story writer (also partially marketing in terms of videos or similar content creation)
- Regardless of whether or not Ranton will actually agree to join, we can definitely do some posts on his subreddit as the game was inspired by him
- Events or leaderboard stuff on discord or some similar form of competition (probably not because it's too much work)
- Lost Oppai Game Dev with Rantoni mention at the end (probably kinda cheeky, but oh well)
    - In this case doing a little bit of marketing for Lost Oppai may actually end up helping this game as well, though probably only way too indirectly and not really worth the extra effort? Well you could at least post it on yarnspinner discord
    - Lost Oppai game dev log with a reveal of the game at the end (though only once the steam page is up!)
- Bevy Community
    - Share on main bevy discord server (in showcase channel for example, if you do gamedev logs then post there as well)
    - Possibly post on some more niche bevy servers like specific crates?
    - Put game on assets page

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

## Level Design

### Biomes and Areas

Take a look at Midnight Fight Express if you are running low on ideas, they also got high rises which might provide some good reference.

- Sidestreets of Tokyo
    - This may be too difficult to do in a general way, perhaps reduce this to very specific situations, like for instance, you could just have a straight path (either horizontal or vertical), that would be very easy (lol, relatively) to make
    - Instead you could have something like 
- Interiors?
- City high rises (office buildings and rooms, playing both in the interior as well as on the roofs etc, looking down on the city)
- Severs?
- Winter region? (Hokkaido maybe? Something with snow would look cool)
- Volcano? (Mr. Fuji? Would be sick, also great visuals)
- Some temple in the mountains (I am picturing some kind of late summer/autumn setting, colorful trees and beatiful nature)

- Shibuya?

Possible locations for gang hideouts:

- Abandoned Factory
- Warehouse by the Docks
- Rooftops of High-rise Buildings
- Old Parking Garage
- Rail Yard
- Construction Site
- Underground Parking Lots
- Forest or Park Hideouts
- Old, Closed Movie Theater
- Closed Subway Station
- Storage Unit Complex
- Deserted Hotel

## Story

Generally I am pretty open as to what the story should be, I do think that a linear story is very much necessary though. Have levels and then you just play through them until you reach the end. Our target audience isn't really that niche or specific, so a simple linear story line should be better suited for a broader audience.

Now regarding the actualy story, I was thinking something pretty similar to Redeemer, some Monk (with maybe some connections of his past to gang or something like that) then an event happens and he is out for blood to kill gang members. Generally that would probably work, could also go with a more philosophically interesting story but I don't really mind too much.

Some gameplay ideas that could influence:
    - If we end up including policeman and civilians then at the very end with the final dude let him incoorporate the stats of the player, something like `Final Badguy: "I have read the reports you know... 276. Fucking 276 civilians! You are not any better than us. No, no you are even worse! You are a monster!`, or something along those lines. I think that could be a pretty cool reflection on the players choices throughout the game and maybe also hit them with a curve ball because they probably didn't think much of killing civilians in a game like this.
    - If there is something like a _Game+_ then perhaps have slightly different dialogue in some cases? Maybe even have a different ending (like a "true ending" or something?). Something like that could easily double the playtime while only requiring a fraction of the time to create, although certianly not all players would play this mode, but it would be nice to give that to people who really enjoyed the game and want to play some more

If you end up implementing multiple gangs then you could do something like some gang wanting to team up with our protagonist, they meet up, they give the proposition, they shake hands, though after a few seconds the hand of the gang member explodes (chad crushed his hand with a hand shake), then says something like "I would never ally with scum like you.", further solidifying his disgust and hatred for gangs.

### How to Implement Story

- It should never **EVER** interrupt gameplay, preferably put them at the end of chapters, don't know if they should always have one, maybe cutscenes? Maybe just simple dialogue? Maybe not all need them, depends on the pacing of the game I guess
- Less is more, this game is about gameplay/mechanics first, everything else is second, story is just a little driving force, if the mechanics are ass then the story is not supposed to save it, the story must not overshadow gameplay
- Keep story segments short, probably less than one minute, towards the end longer segments are toleratable
- Do not, **EVER** start the game with a cutscene or stupid story shit, **EVER**, let the player _want_ to know more about the world, open with gameplay instantly, explain what stuff is about as you go
    - Oh, I just realized this is **exactly** what Breath of the Wild does, and it's great (also Katana Zero does this a _tiny_ bit, like the first 2 minutes or so are tutorial and then story starts)
- No story before 15min, I feel like that is a decent mark, mabye even 30min (though the game will not be that long in the first place, so yeah something in that ballpark)

### Possible stories

As I said, I am pretty open to anything, though for the case that I need to write the story myself, here are some potential ideas, dear future me. Also note that in any story, it will only start **after** the gameplay, regardless of what you actually choose, the player will be left to wonder why is killing these guys, only then can you start the story.

- Protagonist is a former elitst fighter (monk/martial artist? something), but now lives a life secluded from any kind of civilization, only with his wife and daughter (or son? his family.). However, one day some kind of messanger arrives, to tell him that the world is in danger (or maybe not the world, maybe just his temple or something of his past, I really, *really* don't like these grandious stories where the hero has to save the entire world, keep it grounded man), so he has to set out to erradicate this danger for the sake of his families protection. You would leave your family in the protection of some old friend you trust, or something like that. What exactly happens here is kinda open, a betrayal? Probably too obvious, but some kind of interesting twist would be good.
- Protagonist is a former elitst fighter (monk/martial artist? something), but now lives a life secluded from any kind of civilization with his family, or well, used to live, they got all killed (or perhaps some got kidnapped?) so you set out to kill them all in act of vengance (or rescue the ones that were kidnappes?). I am not a huge fan of this, super flat story, also the villains are just super boring, story very similar to that of Redeemer.

## Legal

### Localization

So there this happened to Jonas `https://youtu.be/MaFpf3nmHmo?t=798`, I personally think that if you had a github repo with a clear license like MIT that said clearly that anybody that would contribute will have their work licensed under MIT would make this essentially a non problem? Though I guess it would be better to ask a lawyer for that? But if this were a problem then wouldn't all of open source be at risk?

## MISC

### Feedback for Concept Art

- Views didn't match, preferably make both T-pose, meaning have legs parallel
- Feet and hands would be nice (especially feet + shoes), separate close up shot of them
