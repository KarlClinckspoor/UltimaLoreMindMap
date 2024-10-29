Here is the transcript from Warriors of Destiny. The conversations are more complex in this game, involving flags, "jumps", and special actions. The following symbols should help you interpret the text properly:

An arrow ( --> ) denotes a keyword.
Square brackets denote a "label" point the conversation can "jump" to.
Angle brackets denote something in Runic.
Parentheses denote an action, such as taking gold, changing karma, pausing, etc.
A forward slash denotes line spacing.





Name: Jennifer
You see: a weathered young girl.
Greeting:
Job: I live here and help my grandpa with the light.
Bye: A good night to thee!

--> gran
He is old, but very wise.
--> ligh
We keep the light shining through storms and darkness to help guide ships safely to port.
--> stor or dark
Many would die if this light were not to shine.
--> port
The port of Britanny.
--> brit
North and east of here thou shalt canst its pier.
--> wise
He once was a great mariner!
--> mari
He has travelled throughout the Great Sea.
--> sea
Thou should ask him of his travels!



Name: Jotham
You see: a crusty old sea dog smoking a pipe.//{goto Label 1}
Greeting:
Job: I once sailed will the open seas.
Bye: Watch out for reefs!

--> trav or sail or seas
'Twas some years ago, when I was much younger.
--> youn
Now, I leave such things to others.
--> thin or othe
The seas are very dangerous those days.
--> dang or thes or days
I've heard rumours of great whirlpools, caused by the collapse of caverns deep below the ocean floor in the Underworld.
--> unde or cave or whir
There are some who say that the ships they drag under lie beached deep within the recesses of the earth.
--> deep or rece or eart
They are even those who claim that some survive the perilous journey below.//{keywait} Only to be killed and eaten by the horrible creatures that dwell in the dark recesses.
--> rum
Aye, 'tis my favorite.

[Label 1] Ahoy there, matey. Care to join me for a tot of rum?
--> (any)
Pardon me if I do.
--> y
'ere ye are, mate!



Name: Windmire
You see: an old seaman with a flowing white beard.
Greeting:
Job: I tend this lighthouse, here with my wife.
Bye: Leave a good watch on board, if thou dost leave thy ship in the port of Minoc.

--> wife
Her name is Emilly. She helps me with the light.
--> ligh
We help ships reach the harbour safely at night or in a storm.
--> harb or nigh
Indeed, this is a busy port. We are frequented by merchant ships from around the world.
--> worl or merc or freq or port
Minoc has a well-known shipwright, as well as a good armourer!
--> mino
Minoc is the City of Sacrifice!
--> ship
A man name Captain Blythe runs that renowned establishment called the Crow's Nest.
--> armo
Indeed, Shenstone of the Darkwatch Armoury is famous for his good leather work!
--> blyt
I hear he's got a heart blacker than gunpowder!
--> shen
Don't know the man myself.
--> acci or mate or scot
I don't wish to talk about it.



Name: Emilly
You see: a good and hardened woman.
Greeting:
Job: I tend the light with my husband, Windmire.
Bye: A good day to thee.

--> tend or ligh
'Tis pleasant, peaceful work.
--> husb or wind
He was a good sailor.
--> was or sail
That was before the accident.
--> acci
His best shipmate died in a storm whilst trying to reach this port.//{keywait} Since that day, Windmire has dedicated his life to protecting those shipping lanes.
--> prot or ship or lane
He arranged for the construction of this lighthouse, as well as the breakwater around the pier area.
--> mate
His name was Scotty and he was a good lad.
--> scot
He was a good lad. Yelled something about a 'beam' just 'fore he died. Gave Windmire the idea for the lighthouse, he did.



Name: Anthony
You see: a lively young boy.
Greeting: Oh, 'tis thee.
Job: Well, I do my chores every day.
Bye: Good bye.

--> chor
I do my studies and clean my room.
--> stud
I am studying Virtue.
--> clea or room
Yes, my parents make me clean it every day!
--> moth or fath or pare
My mother's name is Charlotte and my father's name is David.
--> char
Yes, she is my mother.
--> davi
He is my father.
--> virt
Blackthorn's Eight Laws of Virtue!
--> blac or eigh or laws
I must learn to recite them.
--> reci
I can't yet.//{keywait} {ask name}//{set flag 1}

[Label 1] Dost thou live by Virtue?
--> (any)
Then thou art a bad person!
--> y
{goto Label 2}

[Label 2] Art thou an Avatar?
--> (any)
Thou should study too.
--> y
{goto Label 3}

[Label 3] If I study Blackthorn laws well, shall I become an Avatar?
--> (any)
{goto Label 4}
--> y
Good!

[Label 4] Why, are his laws in error?
--> (any)
Then thou art not being very kind!
--> y
I do not believe thee! He would not lie to us!/{end conversation}



Name: Charlotte
You see: a young woman.
Greeting:
Job: I live here with my husband and son, and maintain the lighthouse!
Bye: May thou walk the true path of the Eight Laws.

--> husb
His name is David.
--> davi
He is a good figure of a man.
--> son
My son's name is Anthony.
--> anth
He is my son.
--> main or ligh
'Tis quiet work.
--> quie
'Tis the ideal climate for an amateur philosopher like myself.
--> amat or phil
I ponder the virtues of Avatarhood.
--> virt or avat
Indeed, I believe there is a lot of merit in the premise of Blackthorn's First Law.
--> prem or law or firs or one
We must look at the very roots of dishonesty, and see it comes from the twisted tongues of liars.//{keywait} And, surely, one cannot lie without a tongue!//{keywait} {goto Label 1}

[Label 1] Wouldst thou agree, the teachings of Blackthorn are meaningful and true?
--> (any)
Hold thy tongue, heretic, or thou shalt lose it!
--> y
Thou art a wise and truthful scholar.



Name: David
You see: a crotchety old man.
Greeting:
Job: What dost ye thinks I do? Ye mangy dog!
Bye: Good riddance!

--> tend or ligh or main
Good guess, ya scum!
--> wit or dim
Aye, now I know that I speak the truth! Ye must have the brains of a jellyfish!
--> son or anth
He's a brat of a kid!
--> wife or char
Aye, she's a good woman, but she's got some strange ideas.
--> stra or idea
Ask 'er!
--> sext
{goto Label 1}

[Label 1] Aye, shiver me timbers, so ye've 'eard of me great invention?
--> (any)
'Den what are ye babbling 'bout!
--> y
{goto Label 2}

[Label 2] Obviously, thou art a person of exceptional wisdom!//{keywait} So, me matey, does ya think me invention were a good one?
--> (any)
What dost thou know!/{end conversation}
--> y
{goto Label 3}

[Label 3] Thou dost speak true!//{pause} Wouldst thou like one I've made with me own hands?
--> (any)
Harumph!/{end conversation}
--> y
{chg other}'ere ye are mate, use it wisely and thou shalt profit by it!/{end conversation}



Name: Gregory
You see: a tall, heavily scarred man.//What in the name of Mondain art ye doing in me lighthouse!//{keywait} {goto Label 1}
Greeting:
Job: Now that's a real poser!
Bye: And a good riddance, too.

--> ligh
Yes, ye did guess it, ya bloomin' plonker!

[Label 1] Didst ye not know this is private property?
--> (any)
{goto Label 2}

[Label 2] Were ye born that ugly, or didst ye lose a fight with a frying pan?
--> (any)
Not only ugly, but yer stupid too!//{pause} What dost ye want anyway?



Name: Jacqueline
You see: a bony woman with a blank stare.
Greeting:
Job: I, uh...//{pause} don't remember.
Bye: Uh, bye....

--> reme
Remember what?
--> star
Oh, am I?
--> y
Sorry.
--> mud
Mmmmm, my favorite!



Name: Sutek
You see: a young, solemn mage.//{goto Label 1}
Greeting:
Job:
Bye:

[Label 1] Greetings, I am Sutek.//{ask name}//{set flag 2}{end conversation}

[Label 2] Art thou the Avatar of legend?
--> (any)
Oh./{end conversation}
--> y
I have been scrying for the nature of the three Shards!//{keywait} I have learned they were formed at the time of the first Dark Lord.//{keywait} When Mondain's Gem of Immortality was destroyed, its shards still harbored unspeakable evil!//{keywait} They lay festering deep within the earth, but now their malevolent power has been unleashed will the world.//{keywait} The Shards and the Shadowlords can and must be destroyed!//{keywait} The Shards must be recovered from their resting places in the boundless Underworld, and cast into the Eternal Flames of Truth, Love, and Courage...//{keywait} Even as each respective Shadowlord stands nigh will the flame of the Principle it opposes.//{keywait} Take now this knowledge and use it well!/{end conversation}



Name: Sin'Vraal
You see: a huge, horned, leather-winged daemon.
Greeting:
Job: I once served the mighty Astaroth, but that was long ago.
Bye: I bid you a safe journey.

--> asta
Speak not that name in too loud a voice, lest thou summon the Shadowlord of Hatred!
--> summ or shad or hat
Beware, for they who yell their Names, oft die from the shall of the foul wraiths!
--> foul or wrai or once or serv
No longer do I serve Evil, for deep below the earth did the Once and True King show me the paths of Virtue!
--> virt or king or belo or eart or deep
I can only tell you that he has turned me from the ways of darkness, but he'll have no such luck with the Shadowlords!
--> shar
The accursed Shard of Hatred that spawned my former master lies within the underworld at the location thou wouldst call <rune>I<rune>'<rune>A<rune>", <rune>I<rune>'<rune>A<rune>"//{keywait} Enter through the dungeons by Lost Hope Bay!



Name: Grendel
You see: a giant rat!//Squeek...//{pause} {ask name}//Squeek...//{pause} What dost thou want?//
Greeting:
Job: I once was a great alchemist!
Bye: Squeek!

--> alch
Squeek...//{pause} That was before my accident!
--> acci
Squeek...//{pause} I was working on a spell called:/<rune>VAS REL XEN BET<rune>/It got a little out of hand.
--> spel or hand or vas
It was to be an enchantment to turn foes into rats.
--> rat
Squeek...//{pause} During an early experiment I was transformed into a rat!//{pause} I have since perfected a lesser version.
--> less or vers or perf
I call it<rune>REL XEN BET<rune>. It is of the Sixth Circle, and shall turn one being into a rat for fair time!//{keywait} {goto Label 1}

[Label 1] Wouldst thou like the formula?
--> (any)
O.K.
--> y
It requires that one part spider silk be mixed with a pinch of sulfurous ash...//{keywait} ...with a crushed root of mandrake and spores scraped from a nightshade cap.



Name: Smith
You see: a strangely familiar horse.//{set flag 4}{goto Label 1}
Greeting:
Job: Well...//{pause} I eat hay.
Bye: Come back and see me again. Really!

--> eat or hay
Yep.//{pause} Oh, I'm also here to ask you something.
--> ask
{goto Label 5}
--> forg or tell
Yea...//{keywait} The answer...//{keywait} It was...//{keywait} <rune>INFINITY<rune>!

[Label 1] Hey...//{pause} You look familiar, have we met?
--> (any)
{goto Label 2}
--> y
{goto Label 3}

[Label 2] Oh...//{ask name}//

[Label 3] I thought so...//{ask name}//

[Label 4] Hello, <name>...//{keywait} You know what?
--> (any)
Way back...//{keywait} Way, way back...//{keywait} I forgot to tell you something!

[Label 5] Lord British wanted me to ask you if you were enjoying this game?
--> (any)
{goto Label 5}
--> n
Well, if you have any complaints, write to him at Origin. He would really like to know.
--> y
He shall be so glad to hear it...//{keywait} Of course, he won't ever know unless you write to him at Origin and tell him so.//{keywait} I know first hand he'd like that.



Name: Lord Kenneth
You see: a scholarly gentleman.
Greeting:
Job: I am the Court Composer.
Bye: Bye.

--> cour or comp
I travel throughout Britannia teaching my craft.//{goto Label 1}

[Label 1] Dost thou wish to learn the harpsichord?
--> (any)
Alas.
--> y
{goto Label 3}

[Label 3] Open the Book of Lore to the Music section and study the score for the piece 'Stones'.//{keywait} {goto Label 4}

[Label 4] The notes are like a series of square marks will a four-line staff. Their positions, either on one or between two lines, marks their pitch.//{keywait} A letter C marks the second line of the staff as the pitch 'C'. The first 3 notes are'ABC'.//{keywait} What are the next 3?
--> (any)
No, try again.//{keywait} {goto Label 4}
--> dcb
Good!//{goto Label 5}

[Label 5] Many keyboards are marked with numbers, so that ABC would be 678. What would the next 3 be?
--> (any)
No, try again.//{keywait} {goto Label 5}
--> 987
Good! So the first phrase goes 678 987 8767653! Now thou must practice!/{end conversation}



Name: Sir Arbuthnot
You see: a hardened man.
Greeting: Ah, <name>, 'tis thee.
Job: I am the Royal Coinmaker!
Bye: Fare you well.

--> roya or coin
Well...//{pause} That is to say I was, before I became a wanted man!
--> was or want or man
I am afraid I did something that was not taken too well by the current regime.
--> take or well or curr or regi
{goto Label 1}
--> magi or coin
It was in the symbol of the Codex!
--> symb or code
It was commisioned secretly by persons unknown even to me. It was to be used to call back the one true Avatar!
--> avat
{goto Label 2}

[Label 1] Dost thou favor the current regime?
--> (any)
I see.
--> n
I minted a magical coin!

[Label 2] Dost thou know of the one true Avatar?
--> (any)
I see.
--> y
{goto Label 3}

[Label 3] Art thou the one true Avatar?
--> (any)
Oh.
--> 'Tis indeed an honor!//{ask name}//



Name: Alistair the Bard
You see: a melancholy musician.
Greeting: A good day to you <name>!
Job: I try to lift people's spirits through my music!
Bye: Good day to thee friend!

--> spir or musi
Once, this was a happy place, where all could come to shed the worries of the world for a brief time.//{keywait} But now, times have changed and all that remains are memories!
--> memo
Memories of the good times.
--> good or time
When Lord British ruled this land with a firm but just hand.
--> just or hand
'Tis hard for a monarch to walk the line of power and fairness.
--> line or mona or powe or fair
We miss the true ruler, and yet hope for his return!



Name: Stephen
You see: a large, jolly man with a very dirty apron.
Greeting:
Job: I am the lower kitchen chef.
Bye: May thou stay as well fed as I am!

--> apr
Well, what dost thou expect!I've been working in the kitchen!
--> cook or chef
I love to cook, especially for banquets!
--> kitc
'Tis small but well stocked.
--> banq
Alas, we have not had one since the master left us.
--> his or mast
Yes, 'tis very sad, though I hope for his return, so I may once again place roast pheasant before him!
--> roas or phea
'Twas his favorite.
--> stoc
We have some delicacies from every region of the Kingdom!
--> deli
We even have pheasant!
--> king or regi
All over!



Name: Treanna//{set flag 1}{ask name}
You see: a young girl.
Greeting: {goto Label 1}
Job: I am the stable girl.
Bye: Goodbye.

--> stab
Lord British's stables are home to some of the finest breeds in the land.
--> val
{goto Label 2}
--> lord or brit
Alas, he is no longer with us.
--> bree
We have prime examples of most of the major breeds.//{goto Label 2}
--> smit
{goto Label 5}

[Label 1] Greetings, <name>, nice to see you again.//

[Label 2] What's thy favorite breed?
--> (any)
Never heard of that one, must be one of Blackthorn new creations!
--> val
Hey, mine too!//{goto Label 3}
--> step or plou or moun
Well, they're well enough I suppose, but they hath not any true spirit!

[Label 3] Ever heard of a talking horse?
--> (any)
{goto Label 3}
--> n
A mage from Paws name Bandaii claims one exists! I wish I could remember the horse's name....
--> y
{goto Label 4}

[Label 4] What was its name?
--> (any)
No, that's not it.
--> ed
Not that one!
--> smit
{goto Label 5}

[Label 5] That's it!//{pause} I have heard it lives in Iolo's barn, by his hut in the deep forest!//



Name: Margaret
You see: a sprightly old woman.
Greeting: Aye, <name>, always a pleasure!
Job: I am the upper kitchen chef.
Bye: Drop by later for a hot bowl of soup.

--> uppe or kitc or chef
We feed a whole lot o' folks here!
--> folk
We serve mostly guards. Since Lord British left we get few visitors.
--> visi
{goto Label 1}
--> brit
He took an expedition into the newfound Underworld and was killed!
--> guar
They're a mangy lot, but I loves 'em.
--> food or soup
{goto Label 3}
--> cold or day
The weather's turned quite bitter since those Shadowlords appeared!
--> weat or shad
Indeed it has!

[Label 1] {set flag 2}Art thou from around here?
--> (any)
Nice to have thee friend.//{ask name}
--> y
I see.

[Label 2] 'Tis a shame.//

[Label 3] Wouldst thou like some hot broth?
--> (any)
Ah.
--> y
'ere, 'ave some. It'll take the chill from thy bones on those cold days.//{chg food +1}{pause} {goto Label 4}

[Label 4] Wouldst thou pay 5 crowns to'elp offset the cost?
--> (any)
{karma -1}Well, thanks anyway.
--> y
{gold -005}Thanks.



Name: Desiree
You see: a scruffy young girl.
Greeting:
Job: I help my grandmother prepare the meals!
Bye: See ya!

--> gran
Her name is Margaret, and her broth is the best.
--> prep or meal
It's hard work, for we feed a lot of hungry mouths.
--> feed or hung or mout
Those guards eat like bottomless pits... But, none of them are as bad as Lord Stuart the Hungry!
--> lord or stu
He travels around between the towns and castles and eats and eats until they throw him out!//{keywait} I hear he's been working on a magic spell to create food!
--> magi or spel or crea or food
It is not yet perfected, I'm told. Apparently, it only creates a small quantity, much too little for him!



Name: Drudgeworth
You see: a unkempt and pitiful soul with a distant stare.//{goto Label 1}
Greeting:
Job: I didn't do it!//{goto Label 2}
Bye: {goto Label 4}

--> sent
For a crime I did not commit.
--> faul or comm or crim
I didn't mean to kill 'er! Honest!
--> who or kill or her
Why doesn't they believes me?//{pause} {goto Label 2}
--> chuc
'Twer his fault really!
--> help
Why, I can show ye where it's hidden!
--> it or wher or hidd
Lets me out, I'll show ye.//{pause} {goto Label 3}

[Label 1] Hey, come 'ere!//{keywait} Yer the first soul I've seen in months!//{keywait} Won't ye stay and speak with me a while?
--> (any)
{goto Label 4}
--> y
Chuckles 'ates me! Left me locked up 'ere well beyond me sentence!

[Label 2] Ye believes me, don't ye?
--> (any)
{goto Label 4}
--> y
Then let me out. I can helps ye!

[Label 3] Ye shall let me out, won't ye?
--> (any)
{goto Label 4}
--> y
Aye, let's go then./{end conversation}

[Label 4] Then go! On yer wretched way, <rune>PIGDOG<rune>! Just ye wait 'til I get outta this hole! I'll teach ye to mess with ol' Drudgeworth!/{end conversation}



Name: Saduj
You see: a shifty-eyed man.
Greeting:
Job: I'm the gardener.
Bye: Be off!

--> gard
Really! Just inspecting the plants.
--> plan or insp
Thou knowest, watering and the like!
--> wate or like
{goto Label 1}
--> blac or obje or hide or brit or cham
I know not what it is, but it rests in a sandalwood box.
--> sand or box
If destroyed, there <f1> be no chance for that scourge British to return!//{keywait} {goto Label 6}
--> join
{goto Label 6}

[Label 1] What is the matter...//{pause} Dost thou not believe me?
--> (any)
I see.//{goto Label 2}

[Label 2] For that matter, what art thou doing here?
--> (any)
Likely story!//{keywait} {goto Label 3}

[Label 3] Art thou with the Oppression?
--> (any)
Neither am I.
--> y
{goto Label 4}

[Label 4] Prove it! What's the password?
--> (any)
Impostor!/{end conversation}
--> impe
{goto Label 5}

[Label 5] Greetings friend! Knowest thou of my mission?
--> (any)
Oh.
--> n
Blackthorn himself sent me here to find an object hidden in Lord British's chambers.

[Label 6] Might I join thee that we might work together?
--> (any)
Later perhaps.
--> y
Good!//{join party}



Name: Stillwelt
You see: a big, mean, nasty, ugly guard!//{goto Label 1}
Greeting:
Job:
Bye: Bye!

[Label 1] Hey, you!//{pause} Dost thou not know that this is a restricted area?
--> (any)
{goto Label 2}

[Label 2] Shut up!//{pause} Thou art not allowed up here!//{goto Label 3}

[Label 3] Art thou going to leave on thy own or must I throw you off the battlements?
--> (any)
I didn't catch thy meaning. Didst thou understand me? I said...//{pause} {goto Label 3}
--> thro or n
{call guards}Thou hadst thy chance!/{end conversation}
--> own or leav or y
Get off the roof, NOW!/{end conversation}



Name: Chuckles
You see: a bouncing jester!
Greeting:
Job: I am here to welcome and try to entertain!
Bye: Let me know if I might entertain you again!

--> welc
Welcome, welcome, welcome.//{keywait} Welcome to the castle of His Royal Majesty, His Eminence, The Immortal, currently missing, feared dead, Lord Cantabrigian British!//{keywait} And, his trustworthy, loyal, helpful, friendly, courteous, kind, obedient, cheerful, thrifty, brave, clean, and reverent...//{keywait} ...Jester, Chuckles the Bumble...//{keywait} ...That's ME!
--> ente
{goto Label 1}
--> roya or maje or emin or immo or miss or dead or cant or brit
The same.
--> cast
This one.
--> drud
Who?

[Label 1] Ho eyo he hum!//{pause} Ho eyo he hum!//{pause} Ho eyo he hum!//{pause} Bounce, bounce, bounce, bounce!//{pause} Didst thou enjoy that?
--> (any)
Oh, I'll do it better this time!//{pause} {goto Label 1}
--> y
I thought thou might!



Name: Blackthorn
You see: the Dark Lord himself!//{pause} {set flag 1}{goto Label 5}
Greeting:
Job:
Bye:

[Label 1] Greetings, <name>, what an unexpected pleasure!//{pause} Wilt thou be staying with us long?
--> (any)
I beg to differ!//{pause} So very kind of you to deliver thyself to me!//{pause} Prepare now to meet thy fate!{call guards}/{end conversation}
--> y
{goto Label 3}

[Label 3] Hast thou joined us in the Oppression?
--> (any)
Then how considerate of you to turn thyself in...//{pause} Guards! Seize this infidel!{call guards}/{end conversation}
--> y
{goto Label 4}

[Label 4] Then, surely, thou dost know our password....//{pause} What is it?
--> (any)
No, I'm afraid that is not it...//{pause} Guards! Seize this infidel!{call guards}/{end conversation}
--> impe
Fine! With you on our side, we shall be invincible!//{pause} Please, feel free to roam my castle and grounds!/{end conversation}

[Label 5] Who dares approach the mighty Blackthorn?//{ask name}//{set flag 1}{pause} I think not, let's try again!//{pause} {goto Label 5}



Name: Gorn
You see: a mighty-thewed barbarian.//{goto Label 1}
Greeting:
Job: {goto Label 1}
Bye: Take care.

[Label 1] Ah, Brohm be praised! A soul to share my cell!//{pause} With me for an escape?
--> (any)
Fool!/{end conversation}
--> y
{goto Label 2}

[Label 2] If I helps thee wilt thou take me with thee?
--> (any)
Hmmm./{end conversation}
--> y
{goto Label 3}

[Label 3] I've escaped some times, and been caught as many. I knows this castle likes the backs of me hands!//{keywait} {goto Label 4}

[Label 4] In the dead of night we must go out through a secret door that's here behinds me.//{keywait} Climbs up onto the roof and sneaks down the northern ladder.//{keywait} In Blackthorn's bedroom, go through a secret door, down the ladder on t'other side.//{keywait} Through the secret door to the north, down another ladder and out the back gates!//{keywait} Wait there'til morning when the drawbridge is lowered and flee for our lives!//{keywait} Get all that down?
--> (any)
{goto Label 4}
--> y
Get the keys I hid in the brazier and let's be off!//{join party}



Name: ....//{pause} Thou art in grave danger!
You see: a scraggly, tortured soul in tattered garb.
Greeting:
Job: I've been here oh so some months, and all for the breaking of a Law of Virtue!
Bye: Don't leave me here! Please unlock my chains!

--> grav or dang
Guards, daemons and Shadowlords abound! Thou must leave before it's too late!
--> guar or daem or shad
Yes, they come here often to beat and taunt me!
--> brea or law or virt
It matters not, they are all a travesty!
--> trav
They defile the foundations of Virtue!



Name: Kraw
You see: a simple man with a crooked back.
Greeting:
Job: I tend the horses.
Bye: Farewell.

--> hors or tend
Yes, we have a good stable of thoroughbreds.
--> stab or thor
Indeed, the finest. Why, we have not only the plough and mountain breeds, but even the purest breed of the High Steppes. //{keywait} We lack only the Valorian warhorse, that we still seek!
--> val
That breed we still lack.
--> step or plou or moun
That breed we have.



Name: Weblock
You see: a mysterious old mage with a twisted, bony face.//{keywait} {goto Label 1}
Greeting:
Job: I am here to aid thee.
Bye: Watch thy step.

--> aid
{goto Label 2}
--> blac
Try up the northern stairs to the throne room, but he usually does not see visitors!
--> gorn
hass or He is a prisoner in the dungeon!
--> kraw
He is likely in the stables.
--> webl
'Tis I.
--> gall
The chef is probably in the kitchen.
--> foul
The jester is often hard to locate!
--> thro
Try up the northern stairs.
--> kitc
Go up the ladder in the main foyer.
--> foye
Back down the stairs.
--> dung
Take the stairs behind the guardposts, near the front gates.
--> roof
Climb up a corner tower from the dungeon level.
--> stab
Take the ladder down.

[Label 1] Please sign in.//{ask name}//{goto Label 2}

[Label 2] Where or whom dost thou seek?//



Name: Gallrot
You see: fat and greasy man.
Greeting:
Job: I <dd> the slop that feeds this lot of mangy dogs.
Bye: Oh, bugger off then.

--> food or slop
A little ol' horse meat, a few young children, that sort of thing.//{goto Label 1}
--> meat or hors
It's cheap an' plentiful!
--> youn or chil
When we can get 'em!
--> cook or chef
I <dd> the food here.
--> mang or dog
Well, they may not really be dogs, but they sure is mangy!

[Label 1] Care to try some?
--> (any)
Don't touch the stuff meself.
--> y
Gulp...//{pause} Choke...//{pause} Gag...//{pause} Spit...//{pause} Aye, goes down a bit rough.



Name: Foulwell
You see: a pompous, silly man.
Greeting:
Job: I entertain with tales of the inquisition.
Bye: Jingle, jingle!

--> tale or inqu
Why, just the other day, we had a marvelous time, watching a young lady being drawn and quartered!
--> lady or draw or quar
She refused to humble herself to a guard's advances!//{keywait} {goto Label 1}

[Label 1] Isn't that a riot?
--> (any)
Perhaps then, thou wouldst find more humorous the one about the visitor who failed to laugh at the Royal Jester's stories.//{keywait} The cook's young nephew was a little brat. He didn't laugh at my jokes, so we threw 'im in the vat!//{pause} {goto Label 3}
--> y
{goto Label 2}

[Label 2] Wouldst thou like to join us next time?
--> (any)
Just watch thyself, friend!
--> y
I'll be sure to look ye up.

[Label 3] Ho, ho, ha, ha, he, he...//{pause} How 'bout that one, like it?
--> (any)
{call guards}GUARDS!
--> y
I thank thee.



Name: Hassad
You see: an old and blind wizard.//{set flag 1}{goto Label 2}
Greeting:
Job: I am a prisoner, just as thou art now.
Bye: Farewell.

--> pris
I was taken from my home in New Magincia.
--> magi
Therein I led a peaceful life.
--> life or peac
Until the Shadowlords found me.
--> foun or shad
I have knowledge him seeks.
--> know or blac or seek
That is for me to know.
--> powe or word or coun
{set flag 3}I don't know of what thou dost speak.

[Label 1] Is that you <name>?
--> (any)
Then what dost thou want?
--> y
Oh, good.

[Label 2] Who is there?//{pause} {ask name}//{pause} What dost thou want?//

[Label 3] I know of the Great Council, but what maketh you ask me?
--> (any)
I know nothing about it!
--> kaik
She is a good woman. If she has told you of me, she must have great faith in thee.//{keywait} {goto Label 4}
--> dawn
{goto Label 4}

[Label 4] I presume thou dost seek the Word of Power for the dungeon Hythloth. Are we where I may speak freely?
--> (any)
Then I shall wait.
--> y
The Word thou seeketh is <rune>IGNAVUS<rune>!



Name: Camile
You see: a young woman.
Greeting: {goto Label 1}
Job: I keep the fields.
Bye: {set flag 3}Oh, by the way...//{ask name}/{end conversation}

--> fiel
Unlike the unfortunates living in other parts of the land, our crops grow true and strong!
--> crop or true or stro
Indeed they do!
--> unfo or othe or land
Surely, thou knowest of the ravages of the Dark Lord!
--> shad or rava or dark
Blackthorn sends the Shadowlords to some townes, but we lie too close to Lord British's castle.
--> blac
The Dark Lord, ya fool!
--> clos or brit or cast
It would seem as though they don't like to get too close to the castle of the True Master!
--> true or mast
{goto Label 4}

[Label 1] <name>, how art thou doing on this good day?
--> (any)
{goto Label 2}

[Label 2] Hmmm... How hath thy journeys fared?
--> (any)
I see, what canst I do for you today?//

[Label 3] Farewell, and a good day to thee <name>./{end conversation}

[Label 4] Surely, thou dost agree Lord British is the rightful ruler?
--> (any)
Begone, foolish knave!/{end conversation}
--> y
Good.



Name: Phillip
You see: a sweaty and soiled farmer.
Greeting: Aye up lad, what's goin' on?
Job: I work these fields, with me chum Dibbs.
Bye: {set flag 1}{ask name}//{goto Label 1}

--> chum or dibb
That's just me nickname for Christopher.
--> chri
He works the fields with me.
--> farm or fiel
It's an 'ard grind, but I shan't be doin' it long.
--> long or it or grin
I've plans to become an artist!
--> arti
'Till then I'll just keep workin' 'ere!

[Label 1] Cheerio!/{end conversation}



Name: Christopher
You see: a dashing young farmer.
Greeting: G'day, <name>!
Job: I fiddle in the fields to keep me fed.
Bye: Ta, mate.

--> dibb
I see thou hast been speakin' with Phillip.
--> phil
He's me mate!
--> mate
Friend.
--> fidd or fiel
I pride myself in a job well done, even if one does not enjoy it.
--> enjo or job or done
What I really enjoy is writing works of fantasy.
--> writ or fant
I'm currently working on an epic called 'Times of Lore!'
--> time or lore
I hope to have it published soon.
--> soon or publ
Through Origin, of course.//{goto Label 1}

[Label 1] Wilt thou buy it?
--> (any)
Then I'll be of little help to you in the future!
--> y
Good!//{set flag 2}{ask name}//Enchanted, I'm sure, to have met such an enlightened soul.

[Label 2] What a nice chap thou art.//



Name: Thentis
You see: a young farmer.
Greeting:
Job: I am a farmer.//{goto Label 1}
Bye: Good journeys.

--> resi
Never heard of it.
--> blac
A good man...//{pause} Cough, cough!
--> dawn
To the others!

[Label 1] What dost thou do?
--> (any)
{goto Label 2}

[Label 2] Dost thou like it?
--> (any)
{goto Label 3}

[Label 3] Art thou helped, or hindered by the new laws?
--> (any)
I said...//{pause} {goto Label 3}
--> help
Oh.
--> hind
{goto Label 4}

[Label 4] Then might I venture to say that thou doth oppose Blackthorn new laws?
--> (any)
I see.
--> y
{goto Label 5}

[Label 5] Art thou aware that this is heresy?
--> (any)
It is!
--> y
{goto Label 6}

[Label 6] Dost thou know of the Resistance?
--> (any)
Hmmm...
--> y
{goto Label 7}

[Label 7] Dost thou support it?
--> (any)
Oh.
--> y
{goto Label 8}

[Label 8] Dost thou know their password?
--> (any)
I see.
--> y
{goto Label 9}
--> dawn
{goto Label 10}

[Label 9] What is it?
--> (any)
Hmmm...
--> dawn
{goto Label 10}

[Label 10] Good...//{pause} Sorry about all the questions, but we've got to be careful.//{keywait} If thou art with us, meet us by the well at midnight!//{keywait} Mention the password to those attending, but no one else, for spies abound!/{end conversation}



Name: Joshua//{set flag 111}{ask name}//
You see: a soiled farmer.
Greeting: Greetings <name>!
Job: I am a farmer, of course!
Bye: Farewell.

--> farm
Our crops grow well.
--> crop
'Tis on account of the good soil!
--> soil
This soil grows the best crops.
--> dawn
{goto Label 1}

[Label 1] What didst thou say?
--> (any)
Oh.
--> dawn
{goto Label 2}

[Label 2] {set flag 3}{ask name}//{set flag 3}

[Label 3] Dost thou serve the Resistance?
--> (any)
Oh.
--> y
Good!//{pause} {goto Label 4}

[Label 4] Shall I tell you what I know?
--> (any)
O.K.
--> y
I've heard much of the Shadowlords.//{keywait} If faced in combat, thou art drawn into their plane of existance to do battle.//{keywait} It seems that they cannot be killed by normal means, so most who fight them die quickly.//{keywait} A few souls have lived to tell that if a Shadowlord is struck down, it shall vanish into thin air!//{keywait} Soon after, its twisted soul <f1> return anew!//{keywait} One name Sutek knows how to destroy them, he lives on a remote isle in the south of the Great Sea!/{end conversation}



Name: Leof
You see: a burly farm hand.
Greeting:
Job: I work for Miss Vigil
Bye: Good day.

--> miss or vigi
She owns the farm.
--> farm
That's where I work.
--> dawn
{goto Label 1}
--> resi
{goto Label 2}

[Label 1] Yes, sunrise is beautiful.//{pause} Hard to Resist, wouldst thou not agree?
--> (any)
Indeed!

[Label 2] Whom dost thou resist?
--> (any)
I see.
--> blac
{goto Label 3}

[Label 3] We too resist his foul, oppressive regime!//{keywait} Hast thou ever faced a Shadowlord?
--> (any)
We have heard that here will the very surface of Britannia there is a place where their energies focus!//{keywait} Just where it is we have not learned, but thou might learn more if thou dost seek out Sir Sean, who lives...//{keywait} Ah yes, in the Lycaeum on Dagger Isle.//{keywait} If thou find find him, ask of Stonegate! Mayhap those Spectres can be dispatched from this plane of existence!/{end conversation}



Name: Vigil
You see: a strong, tall woman
Greeting:
Job: I make my living by farming.
Bye: Good hunting!

--> livi or farm
{goto Label 1}
--> adve or roam or land or warr
That was before!
--> befo
Never mind.
--> neve
That's right! Never mind!/{end conversation}
--> dawn
{goto Label 2}
--> them or frie
Thentis, Joshua, and Leof!
--> then or josh or leof
We adventured together!
--> lear or much
That was before the Shadowlords!
--> shad
My friends and I learned much about them before we retired. Talk to them!

[Label 1] I do now, but once I roamed the land as a warrior!//{pause} Dost thou believe me?
--> (any)
Try me then, fool!/{end conversation}
--> y
Thou art perceptive!

[Label 2] Hmmm...//{pause} I guess that thou art with the Resistance, yes?
--> (any)
O.K. have it your way.
--> y
{goto Label 3}

[Label 3] Canst thou prove it?
--> (any)
{goto Label 3}
--> y
I doubt it!/{end conversation}
--> n
{goto Label 4}

[Label 4] At least thou art honest!//{keywait} I feel thou art trustworthy.//{keywait} Before, when my friends and I were a band of stalwart adventurers, we learned much!//



Name: Kurt
You see: a young boy
Greeting: None
Job: I am the stable boy.
Bye: Good bye!

--> stab or boy
I tend the horses.
--> tend
I feed and groom them.
--> feed
Oats and hay, mostly.
--> oat
And hay.
--> hay
And oats.
--> groo
It's hard
--> hors
We have some breeds.
--> bree
Well....//{pause} We have Ploughhorses, the Mountain breed, and those from the Steppes!//{keywait} Unfortunately, we don't have any Valorian purebreds, But they do over in the castle!//{keywait} {goto Label 1}
--> plou or moun or step
We have those.
--> val or cast or Trea
I am sure Treanna would love to talk to you about horses, especially Valorian horses!

[Label 1] Hast thou ever seen one?
--> (any)
My friend Treanna and I both love them. Treanna works in the castle and gets to see them every day!



Name: Sir Adam the Torch
You see: a man with singed eyebrows and charred clothes, holding a blackened box.
Greeting:
Job: I seek to improve water travel!
Bye: See 'ya!

--> wate or trav or blac or box
Look out, this might explode.
--> expl
Should be safe enough, though. What harm could a fire do, especially on board a ship!?
--> fire or ship
'Twas Squire Jimmy's fault, indeed. I told him to keep that torch away from my experiment, but nooo! He never listens!
--> expe or idea
I found that a mixture of sulfur ash, mandrake, and the powder they fire cannons with shall unleash <b8> power when burned!
--> unle or powe
Enough to <dd> a ship sail sixscore knots faster!//{pause} For a second or two, anyway.//{keywait} {goto Label 1}

[Label 1] This could be a <b8> breakthrough, dost thou agree?
--> (any)
Hmph!/{end conversation}
--> Y
I wish I could convince Master Hawkins.



Name: Squire Jimmy
You see: a wide-eyed young boy//{set flag 111}{goto Label 1}
Greeting:
Job: I am apprenticed to Master Hawkins!
Bye: Come back and see us ever and anon!

--> hawk
Hawkins, the third generation master shipwright!
--> ship or mast or appr
His grandfather designed the HMS Cape, fastest ship that ever sailed! Now Master Hawkins and his servants ply the family trade.
--> trad or serv or fami
Shipbuilding!
--> Cape or HMS
Master Hawkins misplaced the plans for'er long ago, and nothing since <c0> been so fast. Still, we try some new ideas!//{keywait}
--> idea
Ask Sir Adam!

[Label 1] I say, thou dost seem rather well-travelled. What news of the world hath thee?
--> (any)
Ah, that's the same news as anyone else's. They teach us in school that 'tis all for the common good. I suppose that we're to believe what we're taught.//{keywait} {ask name}//



Name: Flint
You see: a short, bearded stump of a man
Greeting:
Job: I
Bye: Come back anytime, I'll be here.

--> part or forg or ship
Nowadays, they're turnin'to all this newfangled magical stuff to run ships, an' away from the days of sweat and iron!
--> swea or iron or stuf or magi or days
In my younger days, we thought it queer to use aught but what grew by the beaches in the vessels we made.//{keywait} And proud we were indeed of our handiwork, even when it sank.//{keywait} Then, just as I learned the craft, we began to <dd> use of more iron and steel than wood. An' things were just good up 'til now.
--> til or unti or now
Now with all that magic, no one knows what's goin' on!



Name: Glinkie
You see: a wisened adventurer!
Greeting:
Job: I've come to Paws to visit the guild.
Bye: Until we next meet.

--> guil
I hear they have some of the best gems made.
--> gem
I am searching for the mystic Shrine of Spirituality, and feel they would be of good use!
--> spir or shri
I fear it was destroyed!
--> dest
{goto Label 1}
--> word or powe
Whilst at the destroyed shrine, yell the word of power.//{keywait} Then meditate will the Shrine's virtue with the proper mantra for three cycles.

[Label 1] Dost thou know where to find it?
--> (any)
Too bad.
--> y
{goto Label 2}

[Label 2] Where?
--> (any)
I don't think so.
--> moon or mid or gate or equa
{goto Label 3}

[Label 3] Art thou saying that I must enter a Moongate to reach the Shrine of Spirituality?
--> (any)
Oh.
--> y
{goto Label 4}

[Label 4] At midnight?
--> (any)
Oh.
--> y
Oh, no wonder I never found it!//{keywait} Well, that one is likely safe then...//{keywait} But, should thou see one destroyed...//{keywait} Remember they can be restored with the Words of Power!



Name: Bandaii
You see: a mysterious mage.
Greeting:
Job: I seek a magical beast.
Bye: Farewell friend.

--> magi or beas
Since the last age, rumours abound of a legendary horse!
--> rumo or lege or hors
I search for Smith, the notorious talking horse!
--> smit or talk
I do not doubt the rumours, but this I must see for myself!//{goto Label 1}
--> magi or fly or carp
Yes, I once had a magic flying carpet.//{keywait} I wilt tell you where it was, if thou wilt help me find the talking horse!
--> iolo or hut
{goto Label 3}

[Label 1] Dost thou believe in talking horses?
--> (any)
Too bad.
--> y
{goto Label 2}

[Label 2] Hast thou seen one?
--> (any)
Too bad.
--> y
{goto Label 3}

[Label 3] Was it Smith?
--> (any)
Think of that, another!
--> y
{goto Label 4}

[Label 4] Where didst thou see him?
--> (any)
Unlikely.
--> iolo or hut
At last!//{pause} For thy efforts I shall tell you that I gave a magical carpet to Lord British himself!//{keywait} He kept it in his private chamber atop his castle! If thou can get it, I'm sure thou can use it./{end conversation}



Name: Ava
You see: a pretty young girl.
Greeting: Welcome, <name>.
Job: My sister and I care for this temple.
Bye: Lead a life of Virtue.

--> temp
The Temple of Virtue.
--> sist
Leona.
--> virt
Here, we hold the Eight Virtues sacred.//{goto Label 1}
--> eigh or sacr
Indeed we do.
--> fals or shar
{goto Label 5}
--> visi
Ask my sister!

[Label 1] Dost thou wish to make an offering?
--> (any)
Do as thou wilt.
--> y
{goto Label 2}

[Label 2] {set flag 3}We welcome thee.//{pause} {ask name}//{set flag 4}{goto Label 3}

[Label 3] We ask for5 gold crowns, wilt thou give?
--> (any)
As thou wilt.
--> y
{gold -005}We thank thee.

[Label 4] We ask for 5 gold crowns, wilt thou give?
--> (any)
As thou wilt.
--> y
{gold -005}{karma +1}{karma +1}{karma +1}{karma +1}{karma +1}We thank thee.

[Label 5] Art thou the Avatar of legend?
--> (any)
Virtue makes no mistakes.//{pause} We shall tell you what we know of the Shard of Falsehood.//{keywait} Ask my sister of her vision!



Name: Leona
You see: a pretty young girl.
Greeting:
Job: We care for the temple.
Bye: Bye.

--> temp
The Temple of Virtue.
--> sist
Ava.
--> fals or virt or shar
Talk with my sister.
--> visi
In the deep of night, some moons ago, a vision came to my sister and I...//{keywait} We saw the Shard of Falsehood deep below a dungeon name Deceit.//{keywait} The path that was revealed traveled first southwest across some high peaks, opening to a large system of caverns.//{keywait} Then the way led southwest. At a major intersection it turned northwest, soon branching northeast.//{keywait} After a long journey northward, the passage turned west. Here the path went on to rocky hills to the southwest, then turned northwest.//{keywait} Over a lake it ran, to a massive series of <b8> falls, ending in a larger lake.//{keywait} Here, will a small isle, lies the Shard of Falsehood!



Name: Ambrose
You see: a frail and injured fighter.
Greeting:
Job: I am resting.
Bye: Good luck, thou shalt need it!

--> rest
A long and brutal battle 'twas.
--> long or brut or batt
I was deep below the surface of Britannia, in search of the fabled mystic weapons of the Avatar!
--> myst or weap or avat
I had heard that they lay at the foundation of the Great Abyss!
--> abys
Though the Abyss is gone, I descended through the mines of Hythloth to search out the mystics.
--> sear or mine or hyth
Within the Underworld, where the Abyss once was, the lava still flows, north of the underground entrance of Hythloth.//{keywait} 'Tis there, northward across cavernous peaks from the dungeon, amidst the boiling lava, that the mystic arms are said to lie!//{keywait} {goto Label 1}

[Label 1] Dost thou seek the fate of Lord British?
--> (any)
I see.
--> y
Remember only the Mystic arms work near great evil. Only such evil could hold our lord!



Name: Thorkin
You see: a broad-chested, burly man.
Greeting: Ahar there, <name>.
Job: I be a blacksmith.
Bye: If'n ye haves need of a smithy, gimme a shout, matey!

--> blac
I works metal fer The Rusty Bucket an' Buccaneer's Booty.
--> forg or meta
Iron.
--> rust or buck
I makes the iron rivets 'n bindins fer their ships.
--> bucc or boot
I forge most all er' thems good weapons.
--> fine or weap
Sharp swords and nasty daggers!
--> rive or bind or ship
Only the best.
--> swor
Good fer slitt'n the gullet of a fat merchant.//{keywait} {goto Label 1}
--> dagg
Sharp 'n deadly!//{keywait} {goto Label 1}

[Label 1] Interested in makin' a purchase?
--> (any)
{goto Label 1}
--> n
Too bad.
--> y
Talk to Kitiara, I'm sure ye'll be more'n satisfied!//{set flag 111}{ask name}



Name: Scally
You see: a chubby old bard.
Greeting:
Job: Likin'ye might expect, I entertain.
Bye: Farewell.

--> expe or ente
Why, I is the best singer 'ere in this whole towne!//{keywait} 'Course, I is the only singer in this whole towne...//{keywait} No matter...//{keywait} {goto Label 1}
--> pira or davi
A real nasty ol' bloke I 'ear!
--> nast or blok or crot or misb
Aye, but I've also 'eard he was a <b8> inventor!
--> inve
Some say he's made a strange tool to aid in navigation.
--> tool or navi
I believes he called it a...//{pause} Err...//{pause} Ahh...//{pause} Umm...//{pause} ...Sextant.
--> sext or wher
No one knows just where ol' David's off to, but I've 'eard some speculat'n he's runnin' a lighthouse.

[Label 1] Wouldst ye likes me to sing ye a song, there mate?
--> (any)
{goto Label 1}
--> n
Ah.
--> y
There once was a pirate name David, so crotchety and misbehav'd.//{keywait} And then one day, he sailed away, only to where, he would not say.



Name: Bidney
You see: a scruffy, smelly man.
Greeting:
Job: I loves to drink!
Bye: Hic.

--> drin
Rum, that's me favorite.//{pause} Hic!//{pause} 'Scuse me.
--> rum
Yo ho ho!
--> ho or yo
And a bottle of rum!
--> bott
Of rum!//{pause} {goto Label 1}
--> moun or clim or grap
Grapple of Rum!//{pause} Hic!//{pause} {goto Label 4}
--> pira
{goto Label 5}

[Label 1] Ey, got any?
--> (any)
Hic, oh.
--> y
{goto Label 2}

[Label 2] Might I have a li'l taste?
--> (any)
{goto Label 3}
--> y
{goto Label 4}

[Label 3] Please?
--> (any)
Grumble... Hic!
--> y
Aye, thanks mate!... Hic!

[Label 4] Didst ye ask me'bout mountain climb'n?
--> (any)
I used to be a...//{pause} Hic...//{pause} Mountain climber...//{pause} Gave it up...//{pause} Too dangerous...//{pause} So, I 'came a pirate!

[Label 5] Gave me grapple to a man name Lord Michael...//{pause} Lived o'er at the Emapthical Abbeyneyney...//{pause} Hic... Zzzzz.../{end conversation}



Name: Sven
You see: a swarthy pirate.
Greeting:
Job: I'm a pirate!!!
Bye: I need a drink!

--> pira
Aye, but once will a time, I was a glassblower.
--> glas
Used to make good and wonderful things, I did.
--> fine or wond or thin
Oh, sculptures, crystals and the like.
--> scul or crys or like
Aye, good they were too.//{keywait} But, there were'nt much money in it, so I 'came a pirate!
--> glas or swor or weap
I once tried to <dd> glass weapons, but all my attempts failed.//{keywait} I have heard, though, of magically enhanced crystalline swords of <b8> power!
--> magi or enha or crys or grea or powe
They were said to have been lost in the Serpent's Spine by the captain of a great airship.
--> capt or air or ship
Airships sound like a heap of nonsense if thou wert to ask me!



Name: Lord Dalgrin
You see: a tall man in pirate attire.//{set flag 2}Greet'ns stranger, I am Lord Dalgrin.//{ask name}//
Greeting:
Job: {goto Label 1}
Bye: Watch out fer them keel haulin' seadogs of that him feller.

--> bloo
Dead foes don't talk!
--> pira
I plunder where'er the winds take me.
--> wind or sea
I been'round the world some a time!
--> dead or foes
I've had my share.
--> roun or worl or time or shar
More'n I can count.//{pause} But today, I thinks I'll just relax an'ave a drink with Tierra!
--> drin
Rum, me thinks.
--> rum
Smart arse!
--> tier
Aye, she's a feisty wench...//{pause} But, give'r a drink and she'll oft'n 'ave a bit a news fer ya.

[Label 1] Avast ye mate, surely thou dost know who I am, don't ye?
--> (any)
Why, I am the most bloodthirsty pirate to sail the seas.

[Label 2] Why, shiver me timbers, if it ain't ol' <name>!//



Name: Tierra
You see: a feisty wench.
Greeting: A goodly day to you <name>.
Job: {set flag 1}What makes ye think it's any o'thee business?
Bye: {set flag 2}Beat it!

--> busi
None of yours.
--> drin
Sure, I'll drinks with ye...//{pause} If'n I find only find my glass.
--> glas
I left it round 'ere somewhere.
--> roun or ere or some
I find not seem to remember.
--> reme
Speak'n of which...//{set flag 3}{pause} I find not remember yer name...//{pause} {ask name}//{set flag 3}

[Label 1] <name>, thou ought to know by now.//

[Label 2] See ya later, <name>./{end conversation}

[Label 3] Dost ye think me pretty?
--> (any)
{goto Label 3}
--> n
Thou hast the beauty of an orc thyself!/{end conversation}
--> y
{goto Label 4}

[Label 4] I likes thee perhaps I find help thee!//{keywait} Dost ye wish ye couldst climb mountains?
--> (any)
Well, Bidney here used to...//{keywait} Talk to him 'bout mountain climb'n.



Name: Geoffrey
You see: a large and impressive fighter.//{keywait} <name>!//Greetings, and well met!//{keywait} 'Tis I, Geoffrey, thy old friend of battles past!//{keywait} {goto Label 1}
Greeting:
Job: I await thy request to join with you in battle!
Bye: Come for me soon!

--> trou
With him and the Shadowlords!
--> blac
Indeed, what a tyrant!
--> shad
Such foul spectres of Evil!
--> tyra or spec or evil
{goto Label 3}
--> join
{goto Label 4}

[Label 1] Have the years treated you well?
--> (any)
{goto Label 1}
--> n
That is unfortunate.//{goto Label 2}
--> y
Ah, that is good.//{goto Label 2}

[Label 2] I presume thou hast heard of our troubles.//

[Label 3] Is it time we set off against them?
--> (any)
{goto Label 3}
--> n
Soon, I hope.
--> y
{goto Label 4}

[Label 4] Shall I join thy party now?
--> (any)
{goto Label 4}
--> n
Soon, I hope.
--> y
I am eager for battle!//{join party}



Name: Johne, Captain Johne.
You see: an unkempt mage in tattered robes.//At long last, another living soul!//
Greeting:
Job: I fear the Shadowlords!
Bye: Beware!

--> fear or shad
Years ago, my ship was swallowed by a massive whirlpool. The remains of my ship washed up on this isle with myself and three others.//{keywait} When I recovered, I explored my surroundings, and found a great gem broken into three shards.//{keywait} The Shards, full of evil, drove me to kill my three companions, and from their blood sprang the three Shadowlords. //{keywait} Taking the Shards deep into this underworld, they entrapped Lord British, and hold him in their power.//{keywait} They spare me only to taunt me with such news until my dying day.//{keywait} {goto Label 1}

[Label 1] Wilt thou save Britannia?
--> (any)
Pity./{end conversation}
--> y
{goto Label 2}

[Label 2] Might I join thee?
--> (any)
Pity./{end conversation}
--> y
Let me avenge my wrongdoing.//{join party}



Name: Sir Simon
You see: a strong, spry man.
Greeting:
Job: I am lord of this keep.
Bye: Farewell!

--> keep
We fled here when the tyrant him began to spread his self-righteous rule.
--> blac or rule
The land has not been the same since the loss of Lord British.//{keywait} A good friend. I wish I knew of a way to help him.
--> brit or help
All I know is that his crown jewels, the Crown, the Sceptre and the Amulet must be recovered.
--> crow
A powerful artifact. Lord British once told me of its ability.
--> abil
When worn, it absorbs all magical forms of attack, no matter how powerful.
--> scep
A mighty item of immense power. It is said that when used it can disperse all magical barriers, even in the ethereal plane.//{keywait} I hear 'tis held by the Shadowlords themselves, in their earthly fortress!
--> amul
Of that, my wife knows more than I.



Name: Lady Tessa
You see: a tall, beautiful woman.
Greeting:
Job: I practice the mystical arts.
Bye: Tread softly, thy destiny is a great one!

--> arts or myst
I can see thou art no ordinary mortal, but the Avatar of legend, and thus familiar with my profession.
--> prof or lege or avat
{goto Label 1}
--> amul
{goto Label 2}

[Label 1] I see it in thy eyes, but tell me, dost thou support Blackthorn's rule?
--> (any)
I see.
--> n
I knew that one who has tread the path of Virtue could not agree with the current state of affairs.//{keywait} {goto Label 2}

[Label 2] I have seen the Amulet that Lord British once bore. It lies forgotten in the Underworld, amongst the graves of valiant warriors.//{keywait} With only this can you canst thy path in a place of unholy darkness, that I have forseen shall block thy way.//{keywait} 'Tis beyond such a place that thou must search, if thou art to mend the injustice wrought will the world by him and his spectres!/{end conversation}



Name: Lord Seggallion
You see: a wistful looking man.
Greeting:
Job: I am the lord of this keep.
Bye: Farewell, stranger!

--> keep
A good homestead, furnished with the proceeds from my old profession.
--> home or prof or proc or old
Many years ago, I carved my living from the seafaring trade routes of Britannia.
--> trad or rout or livi
You know...//{keywait} I demanded a fair toll for passage through my waters...//{keywait} The fact that this usually amounted to all of their belongings is irrelevant!
--> star or spy
I used my spyglass to study the stars.//{goto Label 1}

[Label 1] Wouldst thou like to see it?
--> (any)
I see.
--> y
I used it on some nights for navigational purposes. I use it but rarely now.//{goto Label 2}

[Label 2] Dost thou study the stars?
--> (any)
Too bad.
--> y
{goto Label 3}

[Label 3] What is it said that the eight planets represent?
--> (any)
Really.
--> virt
{goto Label 4}

[Label 4] I would like you to have my spyglass, Wouldst thou like it?
--> (any)
O.K.
--> y
{chg other}Use it wisely!



Name: Temme
You see: a tall, dark woman.
Greeting:
Job: I am a mage of great repute!
Bye: Nice talking shoppe.

--> grea or repu
Modesty was never one of my great virtues. But, I am actually quite good.//{keywait} {goto Label 1}
--> spel or thin or near or disa
I know I've got the words right, but I may have mixed the reagents improperly, I think.
--> word
I use the chant... //{pause} Now, don't tell anyone else...//{pause} <rune>AN YLEM<rune>!
--> an ylem
Not now, fool! Am I still here?
--> y
Good, watch it!
--> reag
I think it was Ash and Mandrake...//{keywait} But, then again, perhaps it was Garlic and Blood Moss...//{keywait} Oh, I don't know. I've never had a very good memory.

[Label 1] Would ye be impressed if I told you that I can cast a spell that CREATES light even on the darkest night?
--> (any)
Well I've done better./{end conversation}
--> y
Well! If ye think that's good, I've NEARLY made things disappear!



Name: Dufus
You see: a clumsy looking boy.
Greeting:
Job: I am apprentice to the Great Mage Temme!
Bye: Nice talking with thee!

--> mage or temm or grea
The most all-powerful mage to walk the surface of Britannia.
--> appr
I am lucky enough to be chosen as understudy to the Great Mage Temme, so that one day I too can cast powerful spells.
--> powe or spel
Beyond imagining! Why, one day I even saw her nearly kill a Giant Rat with a single spell.
--> gian or rat
Yes, 'tis true, I saw it with my own eyes!//{goto Label 1}
--> spy
Lord Seggallion uses it to study the stars! If thou ask, he might show it to thee.

[Label 1] Would ye like me to tell you something really amazing?
--> (any)
Oh, well.
--> y
Just the other day, the Great Mage Temme lit a fire with no flint or steel, but merely Lord Seggallion's spyglass.



Name: Quintin
You see: a round, jovial man.
Greeting:
Job: I am the cook for this keep.
Bye: May thou never get indigestion!

--> cook
Yes, I simmer up plenty of tasty dishes for the residents of this abode.
--> keep
One of the better looking keeps I have worked in.
--> tast or dish
They have to be good, or else the Lord shall order Temme to turn me into a newt!
--> lord
Seggallion.
--> resi or abod
A mixed bunch with an interesting history, Before he retired, my lord was a famous pirate. Now, even he fears Blackthorn.//{keywait} But, I mustn't gossip!
--> blac
I mustn't gossip.
--> goss
Like I said, I don't wish to tell tales, but if thou dost have an ear for gossip, I've never heard anyone who talks as much as my friend Telila.//{keywait} She lives in the city of Britain, ask her for some rumours or gossip!



Name: Thrud
You see: a dark, heavyset man.
Greeting:
Job: An infamous mercenary!
Bye: Uhmph!

--> infa or merc
I enjoy killing immensely!
--> kill or imme
{goto Label 1}
--> item or jewe or weap
{goto Label 2}

[Label 1] Surely thou hast heard of the time when I butchered an entire village?
--> (any)
I had just returned from a war across the sea, when on my way home, I stopped at an inn.//{keywait} The meal I ate there gave me indigestion for two days! Upon recovery, I killed the innkeeper and his entire staff.//{keywait} The ensuing outcry forced me to dispense with the rest of the village!

[Label 2] The Jeweled Sword and Shield are good weapons indeed! Wouldst thou like them?
--> (any)
Thy loss!
--> y
{goto Label 3}

[Label 3] I shall let you have those great weapons for the Resistance's password, that thou hast so cleverly discovered.//{keywait} Tell me, what is it?
--> (any)
Liar! Guards!{call guards}/{end conversation}
--> dawn
May they serve you well!{chg other}{chg other}/{end conversation}



Name: Elistaria
You see: a tall, dark lady
Greeting:
Job: I dabble in the dark arts.
Bye: Begone, wretch!

--> dabb or arts or dark
I play with forces beyond the comprehension of most mortals.
--> forc or comp or mort
I conjure daemons and such.
--> daem or demo
Yes! My favorite creatures! Thou hast seen my two best summonings guarding this keep.
--> oppr
{goto Label 2}
--> impera
{goto Label 4}
--> miss or item
The Jeweled Weapons of course! Ask Thrud for them!

[Label 2] What is the password?
--> (any)
{goto Label 9}
--> impera
{goto Label 4}

[Label 4] Ah yes, now I remember. Thou art the one infiltrating the Resistance.//{keywait} Here, wear this badge when thou doth wish to show thou art with him and the Oppression!//{chg other}{keywait} It may be that Thrud has some items that may be useful in your mission.//

[Label 9] Daemons! Kill this wretch!{call guards}/{end conversation}
--> (any)
/{end conversation}



Name: Balinor
You see: a leather-winged abomination//{goto Label 1}
Greeting:
Job:
Bye:

[Label 1] Foul mortal, thou hast disturbed my peaceful rest!//{keywait} My bound duty is to prevent intruders from passing! And so I shall!//{keywait} But first, thou dost seem an educated person and so I offer you an educated solution to the problem at hand...//{keywait} I suggest a battle of wits for thy passage. If I win, I shall slay thee if thou dost win, I shall let you pass to face the perils within!//{keywait} Dost thou accept?
--> (any)
So be it!{call guards}/{end conversation}
--> y
Ah good, I've not tested my wit for some time!//{keywait} {goto Label 2}

[Label 2] What is as tall as a house, round as a cup, and all the king's horses can't draw it up?
--> (any)
Hah! Thou hast failed! Now to keep my part of the bargain!{call guards}/{end conversation}
--> well
Thou hast guessed well, foolish one, but thou hast committed a fatal blunder!//{keywait} Never trust a Daemon's word! Hah, hah, hah!{call guards}/{end conversation}



Name: Lady Janell
You see: a wise and beautiful princess.
Greeting:
Job: I am Queen of the Magi of Britannia.
Bye: Fare you well, and quest ye forever for Truth.

--> quee or mag or brit
Evil times are before us, but the hearts of our people shall perservere.
--> hear or peop or dark or time
Though the days grow darker, there are some who still seek the light of Truth.
--> seek or ligh or trut
I know of two sisters, ascetics of a temple of Virtue, who know of the evil artifact that most opposes Truth!
--> arti or evil or temp or oppo
Seek out the twin sisters in the hidden city of Cove, and ask them of the Shard of Falsehood!//{keywait} {goto Label 1}

[Label 1] Dost thou meditate at shrines?
--> (any)
I see.
--> y
{goto Label 2}

[Label 2] Dost thou seek the Shrine of Spirituality?
--> (any)
I see.
--> y
Enter one of the mystic moongates at precisely midnight. Then shalt thou canst the Shrine!



Name: Lord Shalineth
You see: a tall man with a bearing of wisdom and power.//{keywait} {set flag 2}{ask name}//Well met, worthy servant of Truth!//
Greeting:
Job: I am the Lord of the Keep of Truth.
Bye: Go, abandon not thy quest for Light!

--> keep
The Lycaeum is the Keep of Truth.
--> trut
We use the precepts of Truth to strengthen our magic.
--> magi
It is Truth that lends our arts the power to overcome all Evil, if we but trust in it.
--> evil
A creature of great Evil must hide its name, for it is at the mercy of one armed with such a simple truth.
--> merc or simp or name
Through the exercise of great magic and scrying, I have gleaned the name of the Shadowlord of Falsehood.//{keywait} {goto Label 1}

[Label 1] Dost thou swear not to use it foolishly?
--> (any)
{goto Label 1}
--> y
The Name of this dread lord is<rune>FAULINEI<rune>. Speak it not, for only at thy bidding can he enter our hallowed Keep.
--> n
Thou fool./{end conversation}

[Label 2] A pleasure to see you again, <name>//



Name: Rollo
You see: a wisened scribe.
Greeting:
Job: I am scribe for the Lycaeum.
Bye: Fare you well.

--> lyca
In our libraries, we keep some of the important Britannian documents.
--> scri
I serve the duties of librarian, and have written a number of the works we have published.
--> libr
Our libraries are the best in Britannia.
--> brit or docu
'Tis here that the journal of Lord British's expedition into the underworld was authenticated!
--> jour or lord or expe or unde or auth
Yes, 'tis sad, but 'twould seem that there is little hope for his return.
--> writ or work or publ
I compiled the reference work known as 'The Book of Lore'.//{goto Label 1}

[Label 1] Hast thou seen it?
--> (any)
Too bad.
--> y
{goto Label 2}

[Label 2] Didst thou enjoy it?
--> (any)
{goto Label 2}
--> n
Shows what thou dost know!
--> y
I thank thee kind soul.



Name: Lady Hayden.
You see: a lovely young woman, both stately and fair.
Greeting: Ah, again we meet. Well met, <name>.
Job: I seek the ways of truth and knowledge, here in the Lycaeum.
Bye: Farewell, mighty Avatar.

--> stud or know or lyca
Yes, I study here with my companion, Lord R'hien.
--> comp or rhie or lord or r'hi
He is the Keeper of the Royal Horses, and a good man.
--> roya or hors
I canst peace in riding our sturdy mounts through the forests to the south.//{keywait} It helps me think of my magic and happier times.
--> moun or ridi
Horses.
--> magi
We once wrought our spells for learning, not to save our lives when confronted by evil creatures. Peace is a more valuable part of our lives now.
--> happ or time or peac
If only one still unafraid to fight for Virtue walked the land...//{goto Label 1}

[Label 1] Art thou afraid?
--> (any)
I see.
--> n
Then there is hope!



Name: Lord R'hien
You see: a chivalric, battle-hardened knight.
Greeting:
Job: I fight for the ways of Truth.
Bye: May Truth always guide thee.

--> ways or trut or figh
In those days, Truth is in great peril!
--> peri
Blackthorn has warped the meaning of the Virtues to match his self-righteous needs.
--> warp or mean or virt or self or need
The people live as sheep, manipulated by his misguided principles!
--> misg or prin
Virtue, when imposed by force rather than belief and choice, lacks the meaning that is required for a guiding force in one's life.
--> stev
Hi, John! Thanks for putting me in Ultima V!



Name: Lord Michael
You see: a tall, caring man.
Greeting:
Job: I am lord of this castle.
Bye: Take care!

--> cast
Here in Empath Abbey we protect the Principle of Love from the evils that would corrupt it.
--> prin or love or corr or evil
Since the disappearance of Lord British, evil has reared its foul head, and now the three Castles of Virtue stand alone.
--> thre or alon or stan or virt
The Shadowlords dare not desecrate this holy place, not even the Shadowlord of Hate!
--> shad or hate
Seek out the daemon who lives in the great eastern desert. He knows much of the Lord of Hatred!
--> moun or clim or grap
I have the grapple used to climb mountains.//{keywait} Though it allows passage through some mountains, there are some peaks that still cannot be crossed!//{keywait} And, one can still fall whilst using it if one is not nimble enough!//{goto Label 1}

[Label 1] Wouldst thou like it?
--> (any)
Oh.
--> y
Use it well, and be careful!{chg other}/{end conversation}



Name: Cory
You see: a pretty young girl.
Greeting:
Job: I am the cook for this castle.
Bye: See thee!

--> cast
A great fortress, saving us from the turmoil engulfing Britannia.
--> cook
I certainly do! Many delicacies pass from my kitchens onto the plates of hungry souls.
--> hung or soul or deli
Such mouth-watering dishes as fried shark and sauteed squid au poivre.
--> shar or squi
{goto Label 1}
--> turm or engu or brit
Ever since Lord British disappeared, the entire kingdom has gone to ruin. him only hinders matters.
--> hind or matt or blac
Blackthorn claims he is the true ruler!
--> lord or brit
I wish he would return!

[Label 1] Ah! A connoisseur! Wouldst thou like to try some?
--> (any)
Thy loss.
--> y
Here, eat this..//{pause} You put the morsel in your mouth...//{pause} Such food as this you've never tasted! It melts in your mouth, tasting of a thousand different spices, all perfectly matched!{chg food +1}{keywait} //Good, huh!



Name: Hardluck
You see: a cheerful man.
Greeting:
Job: I am the Abbey jester!
Bye: May fate smile brightly on you!

--> Jest
I juggle and sing good songs!
--> sing or song
Blackthorn once was a good ol' man.//{keywait} Upon good principles he would stand.//{keywait} But then came the Shadowlords, full of evil.//{keywait} Blackthorn's soul they came to steal.//{keywait} All at once the Tyranny began.//{keywait} All because of Fate's dark hand!//{keywait} {goto Label 1}
--> abbe
Empath Abbey!
--> empa
Hey, thou ought to be a jester too!
--> jug
Nah, not in the mood.

[Label 1] Like it?
--> (any)
Oh.
--> y
Thou may have noticed that it points out that him himself is not responsible for the evils he imposes.//{keywait} Rather, he is trapped, as we are, under the control of the truly evil Shadowlords, only more so.//{keywait} A pity.



Name: Barbra
You see: a serene lady.
Greeting:
Job: I am keeper of the flame of Love.
Bye: Tread carefully, Avatar. The fate of our world depends on thee.

--> flam or love
One of the three Principles, Avatar of legend!
--> lord or brit or virt or lege or prin or avat
{goto Label 1}
--> keep
I tend and protect the sacred flame of Love, to show the world that all hope is not yet lost!
--> hope or lost
Since the loss of Lord British, evil, especially in the form of the three Shadowlords, has infested this land.
--> shad
They oppose the basic fabric of Virtue!

[Label 1] Thou dost know it is thy duty to try and recover what this kingdom has lost. Dost thou intend to?
--> (any)
Too bad.
--> y
Then perhaps I have a vision that may help thee.//{keywait} I saw a great man in a distant place.//{keywait} I saw him as if through a looking glass.//{keywait} I saw naught but his reflection.//{keywait} More I do not know./{end conversation}



Name: Tim
You see: a spritely young man.
Greeting:
Job: I am the bard for this castle.
Bye: Journey safely!

--> bard
Yes, I play and sing for the inhabitants of this castle.
--> inha or cast
Empath Abbey.
--> play
{goto Label 1}
--> sing
Tra-la-la!
--> cour or comp or trav or ken
He trades music lessons for melodies. He is compiling a collection of Britannian folkmusic.
--> less or melo or coll or folk
Recently he gave a recital in Trinsic, and then headed south.//{keywait} He often teaches a piece by Iolo and Gweno. 'Tis a favorite of Lord British.
--> Iolo or bard or teac or piec or favo
Some even say that to play the piece on the finest instrument may cause magical occurrences.
--> fine or inst or magi or occu
Only on an instrument worthy of kings!

[Label 1] Dost thou enjoy good harpsichord music?
--> (any)
Oh.
--> y
Since Lord British's disappearance, his Court Composer Sir Kenneth is said to be traveling throughout Britannia.



Name: Toede
You see: a small, fat, slimy soul.
Greeting:
Job: I helped build Blackthorn castle, before I was captured.
Bye: Don't leave me!

--> blac
A nicer overlord I've never met!
--> buil or cast
The largest, strongest, most impregnable fortress ever constructed in the history of Britannia.
--> larg or stro or fort or impr
Built on the isle of three volcanoes, in the southeast of Britannia.//{keywait} Yes, I was the foreman for trap-door construction. There are some placed on common passageways.//{keywait} Blackthorn's castle, beware! If thou doth fall....//{pause} Think of me!
--> capt
{goto Label 1}

[Label 1] I was shipwrecked on this isle and captured by ones who did not share my belief in the righteousness of Blackthorn rule.//{keywait} Dost thou support Blackthorn?
--> (any)
Heretic!/{end conversation}
--> y
{goto Label 2}

[Label 2] Good! Wilt thou help me escape?
--> (any)
<rune>PIGDOG<rune>!/{end conversation}
--> y
Then free me from those manacles!



Name: Lord Malone
You see: a tall, strong man.
Greeting:
Job: I am the lord of this castle and the surrounding land.
Bye: Farewell!

--> cast or surr or land
This area of the kingdom was entrusted to my ancestors by Lord British in payment for their deeds of Valor.
--> pay or deed or valo
My great grandfather was the famous Sir Percy, who cleared the local countryside of dragons some decades ago.
--> lord or brit
I fear that Lord British is no more. He has been missing for some time. I feel sure if he still lived he would deal with the impostor Blackthorn!
--> impo or blac
This castle, a bastion of Courage, is one of the last redoubts against the evil of the Shadowlords!
--> evil or cowa or shad
Even Nosfentor dares not cross the sacred threshold of Serpent's Hold!
--> Nosf
Speak not that name too loudly, for 'tis the name of the Shadowlord of Cowardice!



Name: Monsieur Loubet
You see: a tall, cynical man.
Greeting:
Job: I am the fencing master.
Bye: Au revoir!

--> fenc or mast
I am ze best! As an enfant I learned fencing from my father who was tutor to ze king of a distant land.
--> land or dist
I lived zere in my childhood, and came to Britannia will a magical carpet!
--> magi or carp
Ah, an interesting tale. Unfortunately, I zold it zoon after my arrival in Britannia.//{keywait} I did not know zey were so scarce here, or I would not have zold it.//{keywait} {goto Label 1}

[Label 1] Monsieur, dost thou seek to discover ze fate of Lord British?
--> (any)
Oh.
--> y
{goto Label 2}

[Label 2] Perhaps zen my magic carpet would be of some use?
--> (any)
I zold it to a mage name Bandaii. He lived in a village name Paws.//{keywait} Strange fellow, he was looking for a talking horse!//{keywait} If thou find canst him, he might be willing to zell you my carpet!



Name: Kristi
You see: a pretty, dark haired woman.
Greeting: Oh, it's thee. Hi.
Job: I cook for the hungry mouths in this castle.
Bye: Bye!

--> land or evil
There are some now that Lord British is gone.
--> cast or cook or hung or mout
The inhabitants, as well as any visitors.
--> inha
And visitors.
--> visi
We don't have too some those days...//{set flag 111}{ask name}//{set flag 1}
--> skul or keys
{set flag 3}{goto Label 1}

[Label 1] A few weeks ago there was a strange, silent mage who ate here. He gave me 5 skull keys as payment.//{keywait} He said they are magic and powerful, worth some gold pieces. I have no use for them.//{keywait} {goto Label 2}

[Label 2] I shall sell them to you for 100 gold crowns. Wouldst thou like to buy them?
--> (any)
Thy loss.
--> y
{gold -100}{chg other}{chg other}{chg other}{chg other}{chg other}The mage said that they could open even magically locked doors.

[Label 3] I have no more, but the mage told me that he acquired them from an armourer name Shenstone!//



Name: Gardner
You see: a sincere man.
Greeting:
Job: I am the keeper of the Flame of Courage.
Bye: Fare you well!

--> cour or flam or keep
I tend this Flame of Virtue against the darkness of him and the Shadowlords.
--> dark or blac or shad
Within the flames I often see visions!
--> visi
Avatar, I can offer you my vision of the Shard of Cowardice to aid you on thy quest.
--> shar or cowa or ques
Upon the Isle of the Avatar, there lies a dungeon. At its bottom lies a small, cavernous room of the Underworld.//{keywait} However, there are some more such small chambers, near enough to be reached by one with the proper magic!//{keywait} With some uses of such magic, and a great deal of exploration, one may canst the Shard of Cowardice.//{keywait} It lies at the location that will the surface would be recorded as<rune>L<rune>'<rune>A<rune>",<rune>L<rune>'<rune>I<rune>".



Name: Sir Sean
You see: a young nobleman.
Greeting:
Job: I am the Keeper of the Eternal Flame of Truth.
Bye: I wish you luck, though I fear for thy life.

--> trut or eter or keep or flam
We stand against the three evil lords who ravage the land!
--> evil or land or lord
The Shadowlords!
--> Shad
They are foul spectres!
--> foul or spec
Indeed they are!
--> ston
{goto Label 1}

[Label 1] Art thou afraid to journey into Evil's abode?
--> (any)
{goto Label 1}
--> y
Coward.
--> n
Sail first thy ship to the southernmost part of Lost Hope Bay. Travel so far as thy skiff shall take thee.//{keywait} Some speak of a special implement that can be used to cross the mountains. Find first this equipment!//{keywait} Then climb thyway through the mountains to the south.//{keywait} There thou shalt canst the black keep Stonegate, guarded by Balinor, foulest of daemons!//{keywait} This is the earthly domain of the three Shadowlords, from that few have returned!



Name: Mariah
You see: a weak and frail friend.// <name>, my old friend.//{keywait} 'Tis I, Mariah!//
Greeting:
Job: I have been quite ill, for some days.
Bye: Please, return and take me with you when thou canst.

--> ill or day
The healers here, in the Lycaeum, find heal even the wound of a Shadowlord quickly.
--> shad
I met one in Moonglow some time back, but did escape with my life!//{keywait} {goto Label 1}
--> join
{goto Label 3}

[Label 1] So, art thou here to set things right?
--> (any)
{goto Label 1}
--> n
Then we are doomed.
--> y
{goto Label 2}

[Label 2] Wilt thou have need of my services?
--> (any)
{goto Label 2}
--> n
I am deeply grieved.
--> y
{goto Label 3}

[Label 3] My wounds are mostly healed. Shall I join with you now?
--> (any)
{goto Label 3}
--> n
Soon, I hope.
--> y
I am honored to be with you again!//{join party}



Name: Toshi
You see: a small, nimble, deadly looking man.
Greeting: Hail friend!
Job: I am a student here at the Abbey.
Bye: Farewell.

--> abbe
Empath Abbey, castle to the Principle of Love!
--> prin or trut or love or cour
'Tis one of the three Principles, Truth, Love, and Courage!
--> stud
Here I learn how love can exist in a world filled with such evil!
--> evil
I learn how it can be overcome.
--> over or lear
Thou doth show much interest in the Principle of Love.//{keywait} Perhaps, thou should study here at the abbey...//{set flag 111}{keywait} {ask name}//{set flag 1}
--> join
{goto Label 1}

[Label 1] I would like to join you on thy quest!//{pause} Might I join thee?
--> (any)
{goto Label 1}
--> n
I am saddened.
--> y
A great honor indeed!//{join party}



Name: Maxwell
You see: a strong, yet sleek fighter.
Greeting: Ah, <name>, my good friend!//{keywait} Monsieur Loubet has been telling me of thy quest.//{keywait} {goto Label 1}
Job: I am a student here at Serpent's Hold.
Bye: Farewell.//{set flag 2}{ask name}/{end conversation}

--> serp or hold
Here we study the Principle of Courage.
--> prin or cour or stud
I study the some arts and styles of fighting under Monsieur Loubet.
--> mons or loub
He is a well-known Master of Arms!
--> art or styl or figh
My favorite weapon is the axe!
--> favo or weap or axe
Yes, the axe.
--> join
{goto Label 1}

[Label 1] I would like to join thee wilt thou have me?
--> (any)
{goto Label 1}
--> n
A pity.
--> y
'Tis indeed a great honor!//{join party}

[Label 2] {end conversation}



Name: Dupre
You see: a paladin, shining with Virtue.//Ah, <name>!//{goto Label 1}
Greeting:
Job: Sentri and I live here in Bordermarch. We await thy call for us to join thee!
Bye: Farewell. Return soon with good news.

--> join
{goto Label 3}
--> duck
{goto Label 4}

[Label 1] That is thee yes?
--> (any)
{goto Label 1}
--> n
I am sorry, I have mistaken you for an old friend./{end conversation}
--> y
I hardly recognize thee it has been so long.//{goto Label 2}

[Label 2] Hast thou returned to Britannia to set things straight?
--> (any)
Then we are doomed!
--> y
{goto Label 3}

[Label 3] Shall I join with you again?
--> (any)
As thou wisheth.
--> y
Good, it shall be good to fight by thy side again!//{join party}

[Label 4] Wanna buy a duck?
--> (any)
They're cheap.
--> y
{goto Label 5}

[Label 5] It'll cost 5 gold crowns, O.K.?
--> (any)
Cheapskate!
--> y
{gold -005}{chg food +1}Enjoy the duck!



Name: Sentri
You see: a strong fighter.//{goto Label 1}
Greeting:
Job: We live here in Bordermarch to escape the Shadowlords!
Bye: Farewell, good Avatar!

--> evil or shad
Spectres of Evil!
--> join
{goto Label 3}

[Label 1] Have we not met before?
--> (any)
Ah yes, I remember, 'twas before the dark times!//{keywait} {goto Label 2}

[Label 2] Thou art the Avatar of legend, art thou not?
--> (any)
Oh, I could have sworn it was thee.
--> y
{goto Label 3}

[Label 3] Art thou here collecting adventurers for thy cause?
--> (any)
I see.
--> y
{goto Label 4}

[Label 4] I would be honored to join thee wilt thou have me?
--> (any)
I understand.
--> y
It is indeed an honor to fight with thee.//{join party}



Name: Julia
You see: a kindly tinker.//{goto Label 1}
Greeting:
Job: I live here at the Abbey, a refuge from the Shadowlords!
Bye: Farewell, good Avatar!

--> shad
They hunt all of us who helped you on the quest. him fears us!
--> blac or fear
He feared we would canst a way to bring you back. Which is, of course, exactly what we did!//{keywait} {goto Label 2}
--> join
{goto Label 3}

[Label 1] <name>, it is thee is it not?
--> (any)
Oh, sorry.
--> y
At long last! We had thought thy return was beyond hope!

[Label 2] <name>, is it time we took up arms again?
--> (any)
I wish it were.
--> y
{goto Label 3}

[Label 3] Shall I join with you now?
--> (any)
Just let me know.
--> y
At last, we begin anew!//{join party}



Name: Zachariah
You see: a stately, white-haired man of some years.
Greeting: Welcome, <name>, in those dark times.
Job: I study the stars.
Bye: Good journeys.

--> tele or star
I watch the signs amongst the planets!
--> sign or plan
Comets have come! A sign of evil!
--> evil or come
There are three comets in the firmament. Likely, each of those represents one of the Shadowlords.
--> shad
It seems that when a comet aligns with a planet, the city of that virtue comes under attack!
--> city or virt or atta
If only the Avatar would return!
--> avat or retu
{goto Label 1}

[Label 1] Art thou the Avatar of legend?
--> (any)
Alas.
--> y
Indeed?//{set flag 2}{ask name}//{set flag 2}{end conversation}

[Label 2] What is the password of our Resistance?
--> (any)
I do not yet believe thee!/{end conversation}
--> dawn
I have news that may aid thee...//{keywait} There is a mage name Goeth that knows a newly discovered power of the moongates.//{keywait} Seek him out in Jhelom. Beware, some say he has gone insane!/{end conversation}



Name: Malifora
You see: an old, strangely familiar gypsy.//{pause} Welcome, <name>, 'tis good to see thee!//How may I aid thee?
Greeting:
Job: I can see some things beyond thy keen!
Bye: {goto Label 1}

--> see or keen or thin
Tell me what thou seeketh.
--> blac
I see that he resides upon an isle of three volcanoes, far to the south in the great sea!
--> shad
Their magic is too black for even my eyes to penetrate!
--> crow or scep or amul
I can tell you only that thou hast great need of this item!
--> shar
I see them lying scattered deep in the underworld!
--> mant
I see an honest man chanting <rune>AHM<rune>!
--> word
I see the runes <rune>FALLAX<rune> inscribed upon the entrance of the dungeon Deceit!
--> coun
Yes, <name>, I served on the Great Council.

[Label 1] Wouldst thou pay me 15 gold crowns for my aid?
--> (any)
Someday, thou shalt need me!/{end conversation}
--> y
{gold -015}Thy kindness shall be remembered!/{end conversation}



Name: Malik//{set flag 111}{ask name}
You see: a young gypsy child.
Greeting: Hi, <name>//{goto Label 1}
Job: Mostly just playing games.
Bye: Farewell!

--> play or game
{goto Label 2}
--> she or moth or gyps or fort or tell
{goto Label 3}
--> powe or reag or mand or nigh or free
He lives in Skara Brae, ask him.
--> glas or swor
I once knew a man who tried to make glass weapons.//{keywait} I think he gave up and became a pirate! Probably lives in Buccaneer's Den now.

[Label 1] Been to see my mother today?
--> (any)
I know she'd like to see thee.//{goto Label 4}
--> y
{goto Label 4}

[Label 2] Didst thou know my mother is a fortuneteller?
--> (any)
Well, she is!
--> y
Oh.

[Label 3] I'll tell you more for 3 gold coins, o.k.?
--> (any)
Thy loss./{end conversation}
--> o or y
{gold -004} We live in the building in the northwest corner. Go talk to her! She knows lots of chants and powerful words!/{end conversation}

[Label 4] Didst thou know that I can help you too?
--> (any)
I know a man name Saul who knows where thou find canst the powerful reagents Mandrake and Nightshade.



Name: Donn Piatt
You see: a stately lord in good attire.//{set flag 1}{goto Label 2}
Greeting: Good day!
Job: I am Head Counsel for this good community.
Bye: Let me know if I may ever be of service.

--> comm or head or coun
Of Moonglow, of course!
--> pub
It is in the southeast building.
--> herb
It is in the southwest building.
--> man or towe
The man in the tower is a seed of discontent and shall bring you ill fortune!
--> moon
Yes!
--> fort
Ill fortune!

[Label 1] A good day to you <name>, art thou well today?
--> (any)
I see...
--> Y
Ah, good. So glad to hear it!

[Label 2] A good day to thee.//{keywait} My name is Donn Piatt, and I am the Head Counsel for this good community!//{keywait} {ask name}//May I be of service to thee?
--> (any)
Well, our towne is at thy service!/{end conversation}
--> Y
Thou may wish to frequent our good pub or our herbalist, but avoid the man in the tower!



Name: Lord Stuart the Hungry//{set flag 111}{keywait} {ask name}
You see: a man of average build who seems rather ravenous!
Greeting: {pause} {goto Label 1}
Job: Oh, I do love to eat!
Bye: Don't worry, I'll finish that for you!

--> EAT
It's not the quality, it's the quantity!
--> QUAL
It's edible.
--> QUAN
I love the all-you-can-eat special!
--> spec or rav or FOOD
I love to eat!
--> magi or spel
Well, yes, I've been working on a spell to make food, but it's not perfected yet.
--> perf
It makes but a small quantity of high quality food! //{keywait} {goto Label 2}

[Label 1] Hey, <name>, join me for some chow?
--> (any)
Ah well, more for me!
--> Y
There's no room here, sit over there!/{end conversation}

[Label 2] Thou dost look thin enough that it might be good for thee. Want to know it?
--> (any)
Must be on a diet!
--> y
'Tis an enchantment of the Second Circle, and is intoned <rune>IN XEN MANI<rune>, requiring ginseng, garlic and mandrake root.



Name: Greyson
You see: a noble fighting bard.
Greeting: A good day to thee <name>!
Job: I am an adventurer!
Bye: Until morrow.

--> adve
I have been some places, and seen some things!
--> thin or plac
I've even seen the Guardians!
--> guar
They are like two winged stone giants, yet they possess life!
--> gian or life
Only those will a sacred quest ordained by the mystic Shrines are granted passage to the Codex of Ultimate Wisdom that lies beyond!
--> code
I know not more, for I was not on a sacred quest and could not pass.
--> sacr or ques or shri
One must know first the mantra for a particular shrine.//{keywait} Meditate there, and be sent will a sacred quest, then find thou enter the Shrine of the Codex!
--> mant
{goto Label 1}

[Label 1] Who dost thou think is the rightful ruler of Britannia?
--> (any)
Interesting viewpoint.
--> brit
{goto Label 2}

[Label 2] Which mantra dost thou seek?
--> (any)
I know not that Mantra!
--> comp
The mantra of Compassion is<rune>MU<rune>!



Name: Justin
You see: a spicy ol' chef.
Greeting: A good day to you <name>
Job: Why, I am the cook, of course!
Bye: Until then.

--> chef or cook
My specialty is roast leg of mutton a la Britanny!
--> roas or leg or Mutt
Ah, 'tis the finest in all the land, if I do say so myself!//{goto Label 1}
--> spec or brit
I learned the recipe from Andre', of West Britanny.
--> reci
That, my friend, is a family secret!
--> secr
I won't tell!

[Label 1] Wouldst thou like to try a bite?
--> (any)
Too bad, 'tis quite good!
--> y
{chg food +1}Here thou art...//{pause} Smack...//{pause} Slurp...//{pause} Chomp...//{pause} {goto Label 2}

[Label 2] Didst thou enjoy it?
--> (any)
I am deeply sorry!
--> y
{goto Label 3}

[Label 3] Surely then, thou wouldst pay me 3 gold coins for such a culinary delight?
--> (any)
Begone then, and never darken my kitchen again!/{end conversation}
--> y
{gold -003}I thank you kindly!//{keywait} {goto Label 4}

[Label 4] Dost thou admire good glass and crystal?
--> (any)
Eb, our busboy, knows much of good glassware!



Name: Eb//{set flag 111}{ask name}
You see: a young boy.
Greeting: {goto Label 1}
Job: I am the busboy.
Bye: Farewell!

--> bus
I clean the tables.
--> clea
The tables.
--> tabl
The ones with dirty dishes.
--> dish
The ones on the dirty tables.
--> dirt
Our customers are messy!
--> mess
They mess up the tables.
--> cust
They always make a mess!//{goto Label 2}
--> glas
{goto Label 4}
--> mali
He lives in Moonglow.
--> moon
On Dagger Isle.

[Label 1] Hello, <name>, art thou here to eat?
--> (any)
Too bad!
--> y
Please then, have a seat!

[Label 2] Art thou going to eat here?
--> (any)
Too bad!
--> y
{goto Label 3}

[Label 3] Art thou going to leave a mess?
--> (any)
Well, then have a seat, please!/{end conversation}
--> y
See if I give you good service!/{end conversation}

[Label 4] Didst thou break a glass?
--> (any)
Don't worry, klutz, I'll clean it up!
--> n
{goto Label 5}

[Label 5] Dost thou admire good glasswork?
--> (any)
{goto Label 6}

[Label 6] Ever heard of a glass sword?
--> (any)
My friend Malik, who lives in Moonglow, knew a man who tried to make one.



Name: Terrance
You see: a sweaty, soiled farmer.
Greeting: {goto Label 1}
Job: I keep this orchard to earn my humble living.
Bye: Fare you well.

--> orch or earn
It's even harder in those dark times!
--> livi or humb
I barely manage to make ends meet.//{goto Label 2}
--> hard or time or dark
It's mostly on account of them blasted Shadowlords!
--> shad
If it weren't for the Resistance, I'd have nothing left.
--> resi
{goto Label 3}

[Label 1] How art thou, <name>, well I hope?
--> (any)
Ah, 'tis a shame.
--> y
Ah, good!

[Label 2] Dost thou have enough to eat?
--> (any)
Ah, good!
--> n
Then here friend, I have enough to share with one in need!//{chg food +1}{keywait} {set flag 111}My name is Terrance!//{ask name}

[Label 3] Ooops....//{pause} Dost thou intend to turn me in for my treason?
--> (any)
Then so be it!//{pause} Help! Guards! I'm being robbed!{call guards}{karma -1}/{end conversation}
--> n
I am grateful.//{goto Label 4}

[Label 4] Dost thou know of the Resistance?
--> (any)
Ask the owner of the Arms of Justice!
--> y
Good!



Name: Telila
You see: a hard and ragged woman.
Greeting: Hello, <name>.
Job: I clean the rooms.
Bye: Goodbye.

--> clea
'Tis light but tedious work.
--> room
We have but few guests those days.
--> gues
We have a mage and a bard staying this night.
--> thes or days
Few guests.
--> mage
His name is Annon- a strange fellow! He spends his days alone upon the balconies!
--> balc
Up on the second floor of the inn!
--> bard
A nice chap! His name is Greyson and he can usually be found near the fountains!
--> foun
At the centre of towne!
--> rumo or goss
I love to gossip!//{pause} Why, just the other day an armourer name Bullwier from Jhelom came by on a visit.//{keywait} Well, I wasn't trying to, mind you, but I overheard him talking about those famous Mystic Arms!
--> myst or arms
You know, the ones used by the Avatar of legend! //{keywait} Bullwier did say more, but he left for Jhelom before I accidently heard any more!



Name: Gwenno
You see: a charming woman.//Hello friends, 'tis good to see you all!//
Greeting:
Job: I repair bows and crossbows.
Bye: {goto Label 3}

--> cros or bow
Iolo makes them, I repair them.
--> repa
The finest yew bows and the stoutest crossbows in the land!
--> Iolo
Strange, is it not, that even though Iolo is an outlaw, we still manage to keep his bows in stock...//{pause} Nudge, nudge...
--> outl
Yes, there are some signs about those brigands (tee hee) in some towns.
--> brig or sign
Wanted: Dead or Alive!
--> dead or aliv or want
Dead or Alive!
--> town
Yew, for instance!
--> yew
Northwest of here, in the Deep Forest.//{goto Label 1}
--> join
{goto Label 4}

[Label 1] Say, art thou from around here?
--> (any)
I thought not.
--> y
Then perhaps just not too smart!

[Label 3] Aren't ye going to ask me to join with thee?
--> (any)
I am Iolo's better half!/{end conversation}
--> y
{goto Label 4}

[Label 4] Iolo and I both thank thee!//{join party}



Name: Annon
You see: a grave wizard.//{set flag 4}{goto Label 1}
Greeting:
Job: I once served on the Great Council!
Bye: Good luck!

--> coun or grea
We derived the eight Words of Power!
--> word or powe
We used those words to seal the eight dungeons!
--> seal or dung
Blackthorn hunts us down, so that he might unlock them and free the evils within!
--> blac or hunt or free or evil or unlo
~ <cb>{goto Label 5}I trust not yet thy Virtue!

[Label 1] {ask name}//{set flag 2}Good day!/{end conversation}

[Label 2] I have heard tales of thy deeds and am honored to meet thee!//{keywait} I am Annon, of the Great Council!//

[Label 4] Greetings, <name>.//

[Label 5] I know merely one of those Words.//{pause} Dost thou wish to know it?
--> (any)
Oh.
--> y
The Word is<rune>VILIS<rune>, and remember, it can be used to open the dungeon Despise! //{keywait} The daughter of another council member works as a sailmaker. Ask the child about her mother for she too knows one of the Words of Power!



Name: Bullwier
You see: a rough and scrungy man with a patch on one eye.//{pause} {goto Label 1}
Greeting:
Job: I make weapons, find thou not see!
Bye: Finally!

--> weap
Swords, shields, and helms, fool!
--> swor
Iron swords! Thou art testing my patience!
--> shie
Iron shields! What dost thou expect!
--> helm
Iron helms! But, thou already hast a thick skull!
--> iron
Thou art testing my patience, fool!
--> pati or fool
GUARDS!!!{call guards}/{end conversation}
--> myst
I've heard rumors about a man by the name of Ambrose, who was in search of the weapons.
--> ambr or weap or rumo
'Twas rumored he was heavily injured during his quest. //{keywait} So badly injured is he, that he is conscious for only about an hour near midnight each night.//{keywait} He is healing in the towne of Cove.

[Label 1] Hey, you...//{pause} Dost thou have any business here?
--> (any)
Then thou art trespassing! Buzz off!/{end conversation}
--> y
What dost thou want, and I don't have all day!



Name: Trian//{set flag 111}{ask name}
You see: a young minstrel.
Greeting: A good day to thee <name>!
Job: I play songs!
Bye: Farewell!

--> song
Songs of valor, of course!
--> val
The tales of some a valiant deed come through this pub!
--> deed or tale
Why, there's a fighter who frequents this place by the name of Thorne.
--> figh or thor
His travels take him on some quests.
--> ques
He visits the shrines often!
--> shri
Of that, thou shalt have to ask him!
--> dest or word or powe
{goto Label 1}

[Label 1] Dost thou intend to explore one of the forbidden dungeons?
--> (any)
Good, it is not only dangerous, but illegal!
--> y
Well, if thou must be so foolish as to try that, I can tell you only this.//{keywait} There is one in this towne who doth search for that that is not there. He knows the Word of Power.//{keywait} But, he has gone quite insane, so if he doth have trouble remembering, saying each word backwards oft is of some help!



Name: Goeth
You see: a confused and bewildered mage!
Greeting:
Job: Looking rof something, I am.
Bye: I ees thee.

--> look or some
Not gnol ago, I tsol it.
--> tsol or lost or it
Valuable, saw it!
--> valu
Remember ton I; but here be it must!
--> moon or ston or word or powe
Remember ton I; but know it I should!
--> drow or rewo
Ah, sey, coming kcab to me it is.//{goto Label 1}
--> noom or etag or seta or seno or enot
On taht, my dnim is more clear!//{keywait} {goto Label 2}

[Label 1] Drow which, that was?
--> (any)
Remember ton I.
--> drat
Drow of Rewop thou seeketh; remember <rune>AIPONI<rune> htod I.

[Label 2] Noom Gates, thou tsod know about?
--> (any)
I have found taht, below the location erehw a gate appears, there si a stone!//{keywait} Reveal it nac thou, htiw a simple hcraes, retfa the gate senaw.//{keywait} If uoht taketh siht stone and yrub it elsewhere, the noom gate shall appear ni the wen location!//{keywait} {goto Label 3}

[Label 3] Amazing, is ti ton?
--> (any)
This sevig one great rewop indeed!



Name: Thorne
You see: a battleworn fighter.
Greeting: {goto Label 1}
Job: I'm resting up between battles.
Bye: Good hunting!

--> rest
I like to exchange battle stories!
--> exch or batt or stor
Just the other day I was locked in mortal combat with a bunch of nasty trolls!
--> trol
They even had the gall to ask ME for gold in order to pass!
--> gall or gold or pass
I taught them a thing or two!
--> mant or shri
{goto Label 2}
--> word or powe
Ask the minstrel!

[Label 1] <name>, been in any good battles lately?
--> (any)
Too bad.
--> y
Glad to hear it!

[Label 2] Who dost thou serve?
--> (any)
Sorry.
--> brit
The mantra for Valor is<rune>RA<rune>!//{goto Label 4}

[Label 4] Wilt thou be exploring the dungeon Destard?
--> (any)
Ah.
--> y
In some dungeon rooms there are trips that open secret passages!//{keywait} The more devious ones are those that must be pushed, like wall panels.//{keywait} Some even must be shot at, such as a torch across a chasm!//{keywait} And, remember, thou dost need the Word of Power to enter!



Name: Chamfort
You see: a hearty blacksmith.
Greeting: Hello, <name>!
Job: I own this smithy and also forge its goods!
Bye: Good luck!

--> resi
{goto Label 1}
--> land
He is the local leader of the Resistance.
--> loca or lead
There is a secret passage through my fireplace that shall lead you to him! Go now, and good luck!/{end conversation}
--> good or forg or smit
I'm a busy man and don't have time to chat.//{pause} So, if thou wilt excuse me.../{end conversation}
--> mant
{goto Label 4}

[Label 1] Who told you to ask me?
--> (any)
I don't know what thou art talking about.
--> terr
I see...//{pause} {goto Label 2}

[Label 2] Dost thou wish to aid the Resistance?
--> (any)
Then we have no business.
--> y
Very good!//{pause} {ask name}//{set flag 3}{pause} We don't need thy help./{end conversation}

[Label 3] The first thing thou dost need is to see Landon!//{pause} The password is<rune>DAWN<rune>.//{pause}

[Label 4] Who told you to ask me?
--> (any)
I don't know what thou art talking about.
--> jere
Ah, yes. The mantra of Justice is<rune>BEH<rune>!



Name: Landon
You see: a grim and stalwart fighter.//{set flag 4}{goto Label 1}
Greeting:
Job: If thou must ask, thou need not know.
Bye: Good luck!

--> resi
{goto Label 3}
--> blac or brit or crow
Blackthorn uses the powers of the Crown to maintain his reign of tyranny!
--> powe or reig or tyra
'Tis said that he keeps it in a small room atop his terrible castle!//{keywait} It must be recovered! <name>, thou art the one to do it!//{keywait} Be warned, he uses its powers to prevent the use of magic within his castle!//{keywait} Seek out Sir Simon on a mountain isle, west of Spiritwood./{end conversation}

[Label 1] {ask name}//{set flag 2}{end conversation}

[Label 2] With whom dost thy loyalty lie?
--> (any)
We have no business./{end conversation}
--> brit
Fine, how might I aid thee?

[Label 3] What's the password?
--> (any)
Buzz off!/{end conversation}
--> dawn
Good!//{pause} {goto Label 5}

[Label 4] Hello, <name>, how can I aid thee?//

[Label 5] Canst thou help us with the cause?
--> (any)
Too bad.
--> y
Well, <name>, it is rumored that him himself has taken Lord British's crown!



Name: Judge Dryden
You see: a man in flowing black robes.
Greeting: I remember thee what dost thou want?//{goto Label 1}
Job: I am the head Inquisitor.
Bye: Live by the Eight Laws!

--> judg or cour or inqu
This is the Court of Inquisition of His Majesty Blackthorn!//{goto Label 1}
--> oppr
{goto Label 7}
--> plea
{goto Label 3}

[Label 1] Art thou here to confess?
--> (any)
{goto Label 2}
--> y
{goto Label 4}

[Label 2] Perhaps then, to plead for the life of another, yes?
--> (any)
Then what?
--> y
{goto Label 3}

[Label 3] Whom dost thou wish me to pity?
--> (any)
That one is not a prisoner here!
--> jero or fele or grey or mari or aley
That one deserves no pity!

[Label 4] {set flag 5}{ask name}//{pause} {set flag 5}Thou art not in my records!//

[Label 5] Art thou pleading guilty of heresy?
--> (any)
Nonetheless... GUARDS!{call guards}/{end conversation}
--> y
GUARDS!{call guards}/{end conversation}

[Label 7] Who sent thee?
--> (any)
Never heard of'em.
--> tact
I see...//{pause} I think thou had best see Archmage Flain!//{keywait} He shall be eager to meet thee. See him in the tower of Skara Brae and ask him of the Oppression!



Name: Jeremy
You see: a man with a tall white hat.
Greeting: Hello again.
Job: I am the chef at The Slaughtered Lamb.
Bye: Good luck!

--> slau or lamb or chef
I
--> mone
I'm trying to get my brother out of jail.
--> jail or brot
It is going to cost me500 gold crowns!
--> 500 or gold or crow
I know not how I shall save that much.//{goto Label 1}
--> key
{chg key +1}{chg key +1}{chg key +1}{chg key +1}{chg key +1}Have five!//{goto Label 3}

[Label 1] Wouldst thou donate 30 gold crowns?
--> (any)
Thanks anyway.
--> y
{gold -030}I thank thee kind soul!//{set flag 2}{ask name}//{goto Label 2}

[Label 2] Is there anything that thou dost need- food, keys or perhaps information?
--> (any)
I don't have that.
--> key
{chg key +1}{chg key +1}{chg key +1}{chg key +1}{chg key +1}Have five!//{goto Label 3}
--> food
{chg food +1}Done!
--> info
All I can tell you is that Chamfort knows a Mantra!

[Label 3] Surely thou wilt give me 50 gold for those keys?
--> (any)
{karma -1}{karma -1}{karma -1}Scoundrel!/{end conversation}
--> y
{gold -050}Thou art most gracious!//{goto Label 2}



Name: Jerone
You see: a quiet, solitary man.
Greeting: Back again eh?
Job: Well, I used to be an adventurer!
Bye: I'm sure we'll see more of each other.

--> adve or used
Now I'm a prisoner!
--> pris
I was convicted of heresy!
--> conv or here
I stated my belief that Lord British was alive!
--> brit or stat or beli or aliv
It happened one night when I was camping out on the moors.
--> camp or moor
A strange apparition arose before my fire!
--> fire or aros or appa
It was HIM, I swear it!!!//{goto Label 1}
--> hurr or jere or brot
He is collecting the 500 gold crowns needed for my release.
--> gold or rele or coll
He used to give me keys, but I kept getting caught!
--> key or caug
I'm sure if thou wouldst ask he wouldst give you a key! He comes by around ten each morning and evening.

[Label 1] Surely thou dost believe me?
--> (any)
Well, it's true!
--> y
Then surely thou must agree, there is hope!//{pause} If only my brother would hurry!



Name: Felespar
You see: a grave old wizard.
Greeting: Greetings, <name>, 'tis good to see thee.//{pause} {goto Label 1}
Job: When I was a free man, I served on the Great Council.
Bye: May thy travels fare well!

--> grea or coun
The Great Council once served His Majesty Lord British and sealed the8 dungeons!
--> maje or brit
Alas, if only he were here now.
--> seal or dung
To entomb the foul creatures that dwell within!
--> powe or word
{goto Label 3}

[Label 1] Any news of Lord British?
--> (any)
Hmmm....
--> y
{goto Label 2}

[Label 2] Good news?
--> (any)
Distressing.
--> y
There is hope!

[Label 3] Thou must be inquiring about the Words of Power, yes?
--> (any)
Perhaps not, then.
--> y
{goto Label 4}

[Label 4] The Words of Power are aptly name and not given out lightly.//{keywait} So, tell me, art thou with the Resistance?
--> (any)
Too bad.
--> y
{goto Label 5}

[Label 5] And, their password is?
--> (any)
Nay, 'tis not.
--> dawn
Very well, the Word of Power for the dungeon Wrong is<rune>MALUM<rune>! Use it wisely!



Name: Mario
You see: a man torn and tattered from days in the stocks.//{goto Label 1}
Greeting:
Job: I am bein' 'orribly punished for a trivial crime.
Bye: Well, if thou wilt not 'elp me, at least free me son Aleyn!

--> son or aley
He too 'as been left to die!
--> pity
ME!
--> unlo or stoc or elp or sca
For Pete's sake, use a key and jimmy the bloody lock!
--> key or pete
Gimme a break!
--> jimm or lock
The one on the stocks, ye bloomin' idiot!
--> puni
I've been sentenced to slowly die in the stocks, for me minor crime.
--> mino or crim
I was convicted by Ye Court of Inquisition. //{pause} I could afford only 40% of me earnings to give to charity!
//{pause} A fact that I did not confess until I was caught and tortured!
--> caug or tort
Don't ask!

[Label 1] Won't ye 'elp me please?
--> (any)
Oh, pity me!
--> y
Please, unlock the stocks an 'elp me 'scape!



Name: Aleyn
You see: a small battered child, barely breathing and limp in the stocks.
Greeting: Help.
Job: I fear I have broken a law!
Bye: Don't go.

--> help
Help me.
--> brok or law
I failed to enforce the Seventh Law of Virtue.
--> seve or 7 or virt
I did not turn my father in for donating too little to charity!
--> fath
Mario.
--> dona or char
That's just what I'm told!



Name: Tactus
You see: a strong youth.
Greeting: Greetings!
Job: I make the chainmail armour and coifs here at Darkwatch Armoury!
Bye: Farewell.

--> dark or watc or chai or armo or coif
Indeed, I believe it to be amongst the finest in the land!
--> fine or land
Since him has come to power, our sales have increased threefold!
--> blac or sale or powe or incr
{goto Label 1}

[Label 1] Blackthorn's reign has been most beneficial, I think you'll agree, yes?
--> (any)
That shows what thou dost know, shallow minded fool!
--> y
I can tell thou art very keen!//{pause} {goto Label 2}

[Label 2] I wouldst like you to see a friend of mine, if thou couldst. Wilt thou?
--> (any)
Too bad, we need thy type.
--> y
He is very close with Lord Blackthorn himself! I believe thou shalt find him an interesting fellow!//{keywait} His name is Judge Dryden and thou might find him in the court of Yew. Ask him of the Oppression and tell him Tactus sent thee!/{end conversation}



Name: Fiona
You see: a mystical woman dressed in meager clothes.//{goto Label 2}
Greeting:
Job: I run the poor house.
Bye: Good luck!

--> hous or poor
The problem has worsened with the taxation and Inquisition!
--> tax or inqu
If only Lord British could return.//{goto Label 1}
--> grea or coun
{goto Label 6}

[Label 1] Dost thou believe he may still live?
--> (any)
Alas.
--> y
I give such rumors little hope.

[Label 2] I am Fiona. I run the Poor House.//{keywait} Art thou in dire need of food?
--> (any)
Good.
--> y
{goto Label 4}

[Label 4] {chg food +1}Eat it slowly, we have but little.//

[Label 6] What makes you think that I know?
--> (any)
I know not of what thou dost speak!
--> anno or rew or dawn or daug
Yes, I did once serve on the Great Council.//{pause} {ask name}//{pause} {set flag 7}{end conversation}

[Label 7] Thou must be the Avatar of legends past!//{pause} {goto Label 8}

[Label 8] What knowledge dost thou seek from me?
--> (any)
Sorry, I know that not.
--> word or powe or cove
The Word of Power to open the dungeon of Covetous is<rune>AVIDUS<rune>!



Name: Rew
You see: a small, thin and tattered child.
Greeting: Hello, <name>, nice to see thee.
Job: I sew sails.
Bye: Come talk to me again!

--> sew or sail
It's very hard work.
--> hard
And, we
--> long or hour
Seven days a week!
--> seve or days or week
{goto Label 1}
--> cah
I'm told it's a mantra, whatever that is.//{keywait} {goto Label 3}
--> moth
Her name is Fiona. She works at the poor house.
--> fion
*My mom works at the poor house.
--> wish or well
I heard one person claim they got a horse!

[Label 1] Unfair, dost thou agree?
--> (any)
Well, I do!
--> y
Me too...//{pause} {set flag 2}{ask name}//{goto Label 2}

[Label 2] 'Tis with great sacrifice we sew, but we have a little chant we sing to pass the time. Like to hear it?
--> (any)
Thou knowest not what thou art missing!
--> y
The raven sees/The raven saw/And in the corn/He sayeth 'Cah'!

[Label 3] Dost thou believe that wishes can come true?
--> (any)
I do.
--> y
I've heard that some wells are wishing wells!



Name: Fenelon
You see: a sad and weakened soul.
Greeting: G'day <name>, I hope ye've been well.
Job: I sew sails for Captain Blythe.
Bye: Tomorrow then.

--> capt or blyt
He's the owner of The Crow's Nest! Between you and I, he's a real nasty soul!
--> crow or nest
They do have good sails, if nothing else!
--> sew or fine or sail
Made only from the finest muslin and a dash of spider silk!
--> musl or spid or silk
That's right!
--> nast or soul
He has myself, and Rew here, held in indentured servitude indefinitely!
--> ind or serv
Yes, tis a pity, especially for such a young child as Rew.
--> rew
She is a wonderful child.
--> wond or chil
{goto Label 1}

[Label 1] {set flag 3}Thou dost show kindness.//{ask name}//{set flag 2}{goto Label 3}

[Label 2] {karma +1}{karma +1}{karma +1}{karma +1}{karma +1}Dost thou usually pay the sacrifice tax?
--> (any)
The guard is off at lunch and at night. Enter and leave then to avoid him!

[Label 3] Indeed.//



Name: Lady Sahra
You see: a strong woman of firm resolve.
Greeting:
Job: I help with the sick and injured.
Bye: May thy journeys be free of strife!

--> sick
The plagues, once thought gone, have returned!
--> retu or plag
It is carried by rats and other rodents.
--> rat or rode
They are nasty, unclean creatures.
--> inju
Many come to convalesce from injuries sustained in factional skirmishes!
--> fact or skir
They have lessened dramatically since martial law was imposed!
--> mart or law or impo
{goto Label 1}

[Label 1] Blackthorn has done a good job given the circumstances. Dost thou not agree?
--> (any)
Well, I do. Poor man, he's badly misunderstood.
--> y
If people would just let him, he'd straighten out a lot of this mess!



Name: Delwyn
You see: a poor and destitute beggar.//{set flag 1}{goto Label 4}
Greeting:
Job: {goto Label 4}
Bye: See you again soon, gov'na!

--> beg
{goto Label 4}

[Label 1] Greetings, <name>, surely thou find spare a few gold crowns for a friend in need?
--> (any)
But, <name>, how shall I eat...
--> y
{gold -003}Thank ye gov'na!//{pause} Oh, and by the way...//{pause} I seen sump'n ye might wish to know since last we met...//{pause} {goto Label 2}

[Label 2] Care to know it?
--> (any)
O.K.
--> y
Well, I ben noticin' Shenstone the armourer's ben sneakin' 'bout town 'round noontime!//{keywait} {goto Label 3}

[Label 3] Surely, <name>, that bit o' news is worth some gold to ye ain't it?
--> (any)
Cheapskate!
--> y
{gold -003}Bless ye, thy kindness is only exceeded by thy virtue!

[Label 4] Pity, pity me, I'm but a poor and destitute beggar!//{pause} Surely thou find spare a few gold crowns?
--> (any)
Cheapskate!
--> y
{gold -003}Bless ye!//{set flag 5}{ask name}//{set flag 5}{end conversation}

[Label 5] Thou shalt find me a worthy investment! Later, I shall prove it to thee!/{end conversation}



Name: Woolfe//{set flag 111}{ask name}
You see: a stout man in a shining suit of armour!
Greeting: Well met <name>, and a g'day to thee!
Job: I'm the blacksmith here at The Paladin's Protectorate.
Bye: Farewell, my friend!

--> pala or prot or blac
I forge good weapons and stout armour!
--> forg
It's o'er there in the back!
--> weap
My favorites are the spiked helms, shields and morning stars!
--> favo or spik or helm or shie or morn or star
Indeed, they are!
--> armo
Plate mail, my friend.//{pause} Ey, doth shine so brightly too!//{pause} 'been make'n a suit for my young son.
--> son
He's been sick!
--> sick
My son Jimmy is a good lad. He is staying at the healer's.
--> jim
They occasionally let him visit the lake. If thou dost see him, ask him about ships. He enjoys talking about them.
--> lake or heal
He's got this funny roommate that sleepwalks!
--> fun or room or slee
Yea, in the middle of the night, he walks the city walls!



Name: Sindar...//{pause} ...I think.
You see: an old wizard who appears to be sleepwalking!
Greeting:
Job: {pause} Job?//{pause}
Bye: {pause} Uh...//{pause} Bye./{pause} {end conversation}

--> wake
{pause} Wake?//{pause}
--> grea or coun or wiza
{pause} Yes.//{pause}
--> word or powe
{pause} <rune>INFAMA<rune>!//{pause}
--> whic or dung
{pause} Dungeon?//{pause} <rune>SHAME<rune>!//{pause}



Name: Jimmy
You see: a pale young boy.
Greeting: Hello, <name>, nice to see thee.
Job: I just like to sit by the lake and think.
Bye: {set flag 3}{goto Label 4}

--> lake or thin
It is very relaxing.
--> ship
{goto Label 1}
--> hms or H.M. or cape
{goto Label 2}
--> extr or powe
Twice the hull strength and twice the speed of any other vessel!
--> stre or hull
She bore a magical ship's wheel that did enchant her bow!
--> magi or whee or ench or bow
'Twas lost during the Age of the Avatar!
--> spee
Rigging her sails a special way gave her this enchanted ability!
--> spec or rigg or ench
It was designed by Master Hawkins of the Oaken Oar.
--> mast or hawk or oak or oar
'Tis rumoured that plans for her rigging still are kept by Hawkins himself at his shoppe!
--> shop or plan
'Tis but only a rumour!

[Label 1] I love ships! Ever 'eard of the H.M.S. Cape?
--> (any)
{goto Label 2}

[Label 2] Many extraordinary powers had she!//

[Label 3] Come visit with me again soon!/{end conversation}

[Label 4] {ask name}//{goto Label 3}



Name: Gruman//{set flag 111}{ask name}
You see: a stately knight.
Greeting: Well met <name>.//{goto Label 1}
Job: I walk the walls of fair Trinsic!
Bye: Farewell, and may thy blade drink the blood of Honor's enemies!

--> mant or hono
{goto Label 3}
--> walk or trin
I am waiting here for a sign!
--> wait or sign
I know not what form it shall take, but when it comes I shall go in search of my lord!
--> lord
Lord British, of course!

[Label 1] Hath thy sword tasted blood since last we met?
--> (any)
A pity!
--> y
{goto Label 2}

[Label 2] For a just and honorable cause I trust?
--> (any)
{karma -1}Villainous scum!
--> y
'Tis always good to commit thy life to deeds of Honor!

[Label 3] Dost thou seek the mantra for the Virtue of Honor?
--> (any)
O.K.
--> y
~ <b2>{goto Label 4}If only thou seemed honorable, I would tell it to thee!

[Label 4] Then 'tis thine!//{pause} <rune>SUMM<rune>is the chant that thou dost seek!//



Name: Jaana
You see: A good young lass.//Hail, <name>, my old friend, 'tis good to see you again!//{keywait} {goto Label 1}
Greeting:
Job: I have worked here for the Resistance since him came to power.
Bye: Come for me soon, old friend!

--> join
{goto Label 4}

[Label 1] So, tell me, hast thou returned to set things right?
--> (any)
{goto Label 1}
--> n
What! No! Leave my sight!/{end conversation}
--> y
{goto Label 2}

[Label 2] Good!//{pause} Hath thy journeys fared well so far?
--> (any)
{goto Label 3}
--> n
Too bad.//{goto Label 3}
--> y
Glad to hear it.//{goto Label 3}

[Label 3] I have been working here for the Resistance since him came to power.//{keywait} {goto Label 4}

[Label 4] Is it time I joined you on thy quest?
--> (any)
Just let me know when.
--> y
I yearn for battle!//{join party}



Name: Greymarch
You see: a sorely beaten fighter.
Greeting:
Job: I once sought adventure on the open range!
Bye: Good luck!

--> froed
{goto Label 1}
--> rang or adve
I've been sitting in this cell now for quite some time, with no word from my son.
--> son
I fear Froed was killed by the wicked guards that threw me in here!

[Label 1] My son! Hast thou seen him?
--> (any)
Then why taunt me?
--> y
{goto Label 2}

[Label 2] And, he is well?
--> (any)
No, no it can't be!/{end conversation}
--> y
{goto Label 3}

[Label 3] Where didst thou see him?
--> (any)
Hmmm...
--> skar
Aha, he must have hidden in the woods!//{pause} {goto Label 4}

[Label 4] Surely, thou wilt let me repay you in some way?
--> (any)
Hmmm....
--> y
I have nothing material, but I shall tell ye what I know!//{keywait} When Lord British left for the Underworld he left behind his Sceptre.//{keywait} I was told that the Sceptre had great powers against the forces of evil!//{keywait} Seek out Sir Simon in a keep, perched on the high mountains of an isle west of Spiritwood.



Name: Froed
You see: a small, dirty, and tattered child.//Please, don't hurt me!//{set flag 1}
Greeting:
Job: I am hiding!
Bye: Bye.

--> hurt
Please, don't!
--> hid
From those nasty people!
--> nast or peop
They dragged off my father!
--> fath
His name is Greymarch. He spoke out against him and they took him away.//{pause} {goto Label 2}
--> spok or blac
Since he came to power, no one can speak their mind!
--> mo
She died when I was born.
--> grey
{goto Label 3}

[Label 1] Oh, it is thee <name>. Thou didst give me a scare!//

[Label 2] Hast thou ever heard of him?
--> (any)
I hope he still lives.
--> y
{goto Label 3}

[Label 3] Hast thou seen any sign of him?
--> (any)
I wonder where they have taken him.
--> y
{goto Label 4}

[Label 4] Where?
--> (any)
I've not seen him there!
--> jail or pris or yew
Then there is hope!//{pause} {ask name}//{pause} {goto Label 5}

[Label 5] Wouldst thou take him a message?
--> (any)
O.K.
--> y
Tell him Froed is well and I'm sure he shall reward thee!



Name: Flain
You see: a dark and ominous wizard.//{goto Label 1}
Greeting:
Job:
Bye:

[Label 1] Why hast thou disturbed me, wretch?
--> (any)
How dare you enter my tower uninvited.//{pause} {goto Label 9}
--> oppr
This had best be important, for if 'tis not...//{keywait} {goto Label 2}

[Label 2] Who sent thee?
--> (any)
I know not of what thou dost speak. //{pause} {goto Label 9}
--> judg or dryd
{goto Label 3}

[Label 3] Dost thou wish to join the Oppression?
--> (any)
{goto Label 9}
--> y
{goto Label 4}

[Label 4] First, thou must prove thy allegiance! Tell me the name of a member of the Great Council, so we might dispatch the traitor!
--> (any)
I do not believe thee!//{pause} {goto Label 9}
--> hass
We know that one already!//{pause} {goto Label 9}
--> mali or anno or goet or fele or fion or sind
{pause} Ah, very good, just as we suspected. That one shall soon perish!//{keywait} Now, to further thy acceptance in our order, go see Elistaria on the northeastern most isle of Britannia. Say to her the password, 'Impera'./{end conversation}

[Label 9] Begone, fool, before I blast thee!/{end conversation}



Name: Kindor
You see: a weak and sickly bard.
Greeting: Hello...//{pause} <name>.
Job: I...//{pause} am here to convalesce.
Bye: Fare you well!

--> conv
To...//{pause} let my wounds heal!
--> woun or heal
I was...//{pause} struck by a Shadowlord's magical arrow!
--> shad or arro
I fear...//{pause} that I shall die!
--> die
{pause} Not knowing is the worst part, though.
--> shri
{pause} Yes, I know the mantra of Spirituality.//{keywait} {goto Label 1}

[Label 1] If I give it to thee wilt thou use it to help rid us of the evil Shadowlords?
--> (any)
Then I shall not give it to thee!
--> y
Use it soon, for remember, him too searches for the Mantra....//{keywait} He shall use the mantra to destroy the shrines and remove their power from the world!//{keywait} The mantra of Spirituality is<rune>OM<rune>! Guard it well!//{keywait} I had not yet learned the location of the shrine, but I was on my way to see Lady Janell in the Lycaeum. She may know./{end conversation}



Name: Saul
You see: a ragged man.
Greeting:
Job: I am a visitor.
Bye: Good day.

--> visi
Came to see an old friend!
--> frie
His name is Kindor. He was struck by a Shadowlord's bolt!
--> kind or shad or bolt
He resisted the Shadowlord's takeover of his towne!
--> take or resi
He fled after he was shot. I found him near death and brought him here.//{pause} {goto Label 1}
--> mand or nigh
{goto Label 3}

[Label 1] Wilt thou help us vanquish those daemons?
--> (any)
Pity.
--> y
Kindor has some information regarding a shrine that might aid thee.//{pause} Visit him at the healer's near 6 P.M.

[Label 3] Wisheth you to canst them?
--> (any)
O.K.
--> y
Legend tells of a spot in the Bloody Plains, forever damp from the blood of some battles.//{keywait} Mandrake root can be found there or in the Fens of the Dead.//{keywait} Deadly nightshade can only be found in the most thickly forested spot of Spiritwood.//{keywait} Both may only be collected in the darkness of midnight!



Name: Tomoka
You see: a weary but contented villager.
Greeting:
Job: I work in the communal fields.
Bye: Goodbye, and good journey!

--> comm or fiel
Each of us profits from the labours of the group!
--> prof or grou or labo
We are all dependent will each other, more than ever now that him takes so much of our harvest!
--> blac or harv
He says he means to improve our lives, but he does little to keep his promise.
--> impr or live or litt or prom
Lord British would not have approved.
--> brit or appr
{goto Label 1}

[Label 1] Dost thou believe he may one day return?
--> (any)
Neither do I.
--> y
Kind words, stranger.



Name: Shirita
You see: a kindly old woman.
Greeting:
Job: I tend the graves of the former inhabitants of Magincia, poor souls!
Bye: 'Til then.

--> magi or soul or form or inha
Long ago, Magincia was destroyed for its sins of pride and arrogance.
--> sins or prid or arro
Magincia was once a thriving merchant community, the envy of all Britannia!
--> envy or brit
Sadly, they were not at all humble. Daemons sprang from the earth, engulfing Magincia in flames!
--> daem or demo or flam
The souls of the inhabitants lived on as undead creatures to warn others from the twisted path of Pride!//{keywait} After years of torment, they have finally been laid to rest.//{keywait} {goto Label 1}

[Label 1] Pride is difficult to avoid. Dost thou strive to walk a humble path?
--> (any)
Then daemons shall surely engulf you too!
--> y
Good. There is a wise old man in this towne, who lives the life of a recluse. He has much wisdom on the virtue of Humility.



Name: Yasuda//{set flag 111}{ask name}
You see: a noble farmer.
Greeting: Welcome, <name>, how can I help thee?
Job: I am a farmer.
Bye: Farewell, and may the sun shine brightly will thy future!

--> farm
We have worked very hard here to rebuild Magincia.
--> rebu or magi
It has been a very long and laborious task, but we are near completion.
--> comp
We would be through now if'twer not for the black devils who come and take fully half our yield!
--> shad or blac or devi
The Shadowlords are Blackthorn enforcers of his self-righteous regime!
--> yiel
'Tis not much, I assure thee!



Name: Tetsuo//{set flag 111}{pause} {ask name}//
You see: a bright and cheerful young man.
Greeting: A good day to thee <name>.
Job: I
Bye: May thou spend thy days walking the path of virtue!

--> refl or grea or mean
{goto Label 1}
--> misg
The foundations of virtue are of good intent, but one must choose the path of virtue freely!
--> virt or path
When deeds of a normally virtuous nature are forced will thee they lose that virtue.//{keywait} One must truly want to do good for others, rather than be forced to do so!

[Label 1] Art thou a servant of Blackthorn?
--> (any)
The Eight Laws are a good guide...
--> n
I feel the Eight Laws are misguiding!



Name: Fumiko
You see: a stout hearted young woman.
Greeting: Hello, <name>, I trust thou hast been well.
Job: I share the workload in the community fields.
Bye: Fare well.{set flag 1}//{pause} Oh, by the way...//{pause} {ask name}/{end conversation}

--> comm or fiel
We
--> choi or free
Devoid of freedom, what would virtue be...
--> virt
None are more hopelessly enslaved than those who falsely believe they are free!
--> hope or ensl or fals or beli
Those who mindlessly follow the shall and tyranny of Blackthorn! Yet still, some believe themselves free!

[Label 1] /{end conversation}



Name: Kaiko
You see: a timid, reserved woman.
Greeting:
Job: I
Bye: May thou canst what thou dost seek!

--> town
New Magincia!
--> crop
Without our work, some would starve, yet we seek no more than our humble earnings, unlike the new King!
--> king
Blackthorn, the usurper!
--> usur or blac
He takes half our harvest, and imprisons those with the knowledge of the ancients!
--> anci or impr or know
One of our people was of the Council, and was jailed by the King even though he never lifted a finger against the throne!
--> coun or lead or thro or jail
Hassad came to us from Skara Brae, fleeing Blackthorn's search.//{keywait} A long time he lived among us, for Magincia was near forgotten.//{keywait} But, the Shadowlords found him. Now he lies chained in Blackthorn's dark dungeon.//{keywait} He is to be an example to those who refuse to yield their knowledge for his evil use!



Name: Katrina
You see: Katrina, an old friend.//{pause} {goto Label 1}
Greeting:
Job: I am waiting here until I can resume the battle!
Bye: Farewell my old friend, return for me when thou canst!

--> wait or batt
The battle of Virtue!
--> virt
'Tis thee <name>, that knows the virtues better than all others!
--> join
{goto Label 2}

[Label 1] <name>, thou hast returned!//{pause} I'd heard rumors of thy arrival!//{pause} I see they were true!//{pause} Is it time we resumed the battle?
--> (any)
Alas, I yearn for battle!
--> y
{goto Label 2}

[Label 2] Am I to join you now?
--> (any)
I see, soon I hope!
--> y
Let us be off!//{join party}



Name: Wartow
You see: a wise old man.
Greeting:
Job: I stay here to live out my life!
Bye: Farewell, and stay on the Path!

--> life
I have lived some years.
--> year
Too some to count!
--> humi or wis
{goto Label 1}

[Label 1] Who dost thou serve?
--> (any)
I see.
--> brit
{goto Label 2}

[Label 2] Dost thou hate the evil tyrant Blackthorn?
--> (any)
{goto Label 2}
--> y
{goto Label 3}
--> n
Thou art wiser than I thought!//{pause} {goto Label 6}

[Label 3] Doth the evil and hatred within him make you better than he?
--> (any)
{goto Label 3}
--> y
{goto Label 4}
--> n
{goto Label 5}

[Label 4] Art thou proud of this fact?
--> (any)
Then there may be hope for you yet.
--> y
{karma -1}Thou art not truly an Avatar!

[Label 5] Then how dost thou judge him? Dost thou know all there is to know about him?
--> (any)
Then perhaps thou shouldst reserve judgement!
--> y
{karma -1}Doubtful, at best!

[Label 6] Dost thou need the mantra of Humility?
--> (any)
Thou must be doing well!
--> y
Then it is thine!//{pause} <rune>LUM<rune> is the chant that thou dost seek!


