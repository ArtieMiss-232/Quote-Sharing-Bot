import asyncio
from asyncio import wait_for
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from datetime import datetime, timezone
import random

utc_time = datetime.now(timezone.utc)
local_time = utc_time.astimezone()
quote_time=local_time.strftime('%I:%M %p')

print(f"It's {quote_time}")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

pascal_quotes=[
    "My great grand uncle was a drug dealer",
    "We’re part of our own criminal type of thing",
    "My great grandpa got killed by a hit man",
    "I didn’t meet my parents until I was 5, wait no 3, no 2.",
    "Um ok, molest",
    "I don’t want people to be like me, I’m a horrible person dude",
    "Don’t talk about my ball trauma, I have a lot of trauma.",
    "I need to go find peace this summer.",
    "My husband left me, may he burn in hell, may his liver be eaten by wolves.",
    "When life gives you lemons sell those lemons to death so you can be one to give those lemons",
    "The sin of lust is very powerful",
    "Not my first time getting interrogated by the police, and it certainly won’t be the last.",
    "Haha the power of god (referring to Jules being able to create Miis on the switch)",
    "He almost got molested, got kicked out of his house at fifteen",
    "I’m still here, just lost (on discord)",
    "Just use tinder (to Alina)",
    "Imagine having a play boy father for 16 years.",
    "Woah, and I thought I had problems",
    "I have some kind of death aura around me.",
    "You don’t even know half the horrible things I’ve done.",
    "My playboy father",
    "I know so many ways to kill a person",
    "My parents have committed horrible atrocities",
    "True funny story my grandmother was abducted by aliens",
    "They don’t know what the real gang life is",
    "Always thirsty",
    "I’m too furry",
    "I’m not Alabama",
    "Those tentacles can be used for something other than pain.",
    "Shafts are interesting",
    "I’ve killed children before",
    "What if he’s a molester",
    "Let me just put it right inside me",
    "I love holes",
    "He was 12 so it’s fine",
    "Give me 5 minutes with someone, and a pair of handcuffs and I’ll get them to talk, we’ll start with toes and move to fingers.",
    "I’m not a serial killer, but my dad was",
    "I used to know piano, then my piano teacher was killed in a terrorist attack",
    "Is your family incestual",
    "I lost my mind because bad things are going on with my family",
    "Blood is blood",
    "Wanna spin my pencil",
    "My mom told me my dad still masturbates",
    "I’m going to do something creepy to the drinks.",
    "That one time in castaic lake I had to shower with kids",
    "I was only a slab of meat for 3 years",
    "Sometimes you have to show up at a crime scene nude.",
    "OnlyPascal",
    "Out of context sex",
    "My father says everyone’s selfish in their own way",
    "My dad showed me his playboy magazines",
    "You know the sexy carwashes with the girls in bikinis? I saw the one with the men.",
    "I’m going to groom you (to me)",
    "I’m also not a groomer.",
    "You can change your gender but you can’t change the head “the mind, the MIND”",
    "What do you wanna ride, “MOUNTABLE, MOUNTABLE”",
    "What do you think of wagons",
    "Funny thing about my Asian friends, they think their girl is the one.",
    "I got stalked during my lifeguard years",
    "Have you ever gotten stalked by a blond girl.",
    "It’s wet in places you don’t want to know",
    "I’m not a flasher",
    "I’m wearing a trench coat and nothing under it",
    "I wanted mountable people",
    "Why would I describe Alina losing her virginity. (Me saying in response to what pascal said.",
    "Who do you want to mount? The dragon?",
    "Ugh suicide bomb, something to do with terrorists",
    "Yay racial slurs",
    "I love to see birth",
    "I’ll take their clothes and sell it online",
    "Is he dating his own sister? No he’s not that xEuropean.",
    "Dressing up kids and telling them to go fight rapists",
    "They were the legal limit, like 13",
    "Wait are we talking about boobs?",
    "I’m giving Lucifer vibes",
    "We used racism to solve racism",
    "Mentally ill people cannot be cured",
    "You better sit on this",
    "Why are you looking at me like a criminal, I only did it one time",
    "I’ll poke you in places where it doesn’t shine.",
    "Who hasn’t held their cousins hand",
    "So you picture dicks as pickles?",
    "Android and the thick ass goblin",
    "I think that’s just masturbating (referring to having sex from afar)",
    "Me: remove the bow from bow tie what’s left? Pascal: dick?",
    "I also have thick thighs",
    "Are you saying that because my dad was a playboy",
    "I’m surprised he doesn’t have an STI",
    "I wouldn’t say I’m a boob person",
    "I like boobs",
    "Hotels that’s where people get kinky",
    "Spoke to my grandpa and father about sex hotels",
    "I’m such a bad boy",
    "I prefer piss",
    "Lucky for you I’m gay.",
    "Ohhhh you mean massive dicks, I’ve heard of those from RDR2",
    "At least you don’t wanna bang a metal",
    "I didn’t grab your ass",
    "Maybe I should say the n word for quote 100",
    " ____ ",
    "Shoving a sponge up your a**hole to absorb all the liquids that get squirted up there",
    "So you’re rubbing dicks together?",
    "So a kid gets r****? (Got it from his parents)",
    "I was about to say penis but that’s too far",
    "Don’t worry about my moms cousin, we “accidentally” ran him over",
    "Maybe I’m a… top?",
    "What’s wrong with eating dogfood? I did it a lot as a kid",
    "Eat a salad! (to Ava, the short one, trying to eat something unhealthy)",
    "My parents got molested",
    "The person who molested my mom got “accidentally” run over by a car. You don’t wanna know",
    "I grew up from the hood boi",
    "My dad was part of a black playboy sorority",
    "My dad used to date a witch, some satanic lady. She cast a curse on my family",
    "Funny thing my dad cheated on my mom",
    "Who’s that guy who’s homophobic? Andre Dante? (Andrew Tate)",
    "My parents told me to bring a knife to school",
    "I don’t think Batman has aids",
    "I suck a lot",
    "We were out there wearing NOTHING",
    "True funny story, last year my neighbor was screaming",
    "I have soooo many holes",
    "We gotta let in all the immigrants, even the bad ones",
    "Are you Caucasian? “Maybe, I’m Mexican”",
    "Eating a white boy",
    "I’m fine with 40 women being on top of me",
    "Fascism ? That’s not until later",
    "I’m Him, but Asian",
    "Emperor means Chinese and Chinese is- oh no no that’s a different-",
    "We had a whole conversation about dickled picks",
    "I’m not a homo chromo, I’m cancer",
    "Sadly my family doesn’t get cancer",
    "I’m not all kinks, I’m all sinks",
    "Are you touching nose tips",
    "Just touching weed",
    "I know about sex stuff",
    "Surprisingly my mom told me she was Asian! ASIAN!",
    "My dad’s first time was Asian.",
    "Oh master do you want me to kiss your feet",
    "I was about to do something with slave owners",
    "It’s not slavery if it’s a white person",
    "I only know him because he sells his body",
    "Sometimes you have to sell your body to rich people",
    "My brother is mentally hot",
    "That sounds incestual but no",
    "Max would never put his butt on someone else’s face unconsentually",
    "Some guys have boobs, not the boobs you expect though",
    "Man tits are mostly crosseyed",
    "Oh I have killed someone before",
    "Is this a sexual harassment presentation?",
    "I’ll pull out the race card, I don’t speak English. Me no speak English me Switzerland",
    "I have a Stephen Hawking brother",
    "Don’t let the crack fool you, you can still fit many things inside",
    "You hear noises from your parents room?",
    "I had a friend who talked about how his mother does it.",
    "We’re not having sex right now that’s later",
    "That sounds like a slave owner Cathoter",
    "I had a lot of stripping jokes",
    "I made a fingering joke once but hey we don’t wanna go there",
    "I’m not like my coaches coach,",
    "I cut off my finger before",
    "My dog has done crimes of unforgivable nature",
    "Jeremy don’t be a prostitute",
    "Guess you don’t have to kill your grandma anymore",
    "Aww I thought we were done with pedophiles",
    "I can take on 40 guys at once, and not in a fight.",
    "Whore x20",
    "I’m not slaying rn girl",
    "I’m into R2D2, the beeps really get me",
    "I punched a photographers dick once, I take pride in that",
    "Do you have marriage problems pascal? “HELL YEAH”",
    "Is it going to be a sexual assult bard?",
    "Ah good, butts",
    "Who does cocaine nowadays. Everyone’s into fentanyl now",
    "If the rapture happens get naked and jump in the air",
    "Mmmmmmm hot women, I’ve never seen one",
    "I really just like racism",
    "We’re very open in the lifeguard program, we all piss in the lake but I’m too shy.",
    "My female friend pissed on me in the lake",
    "She did NOT piss on me, I just accidentally ran into her piss and it was only slightly warm.",
    "There actually was a dead corpse in the lake",
    "No it was not an old dude that pissed on me it was a FEMALE. It was less sexually.",
    "We were all in our bathing suits so it’s fine. (Relating to the pissing incident)",
    "I got held back because of indecent exposure.",
    "I wasn’t flashing people",
    "It’s great to be a virgin this year",
    "Is your family bible",
    "I had an ex girlfriend once, no car crashes happened. No accidental car crashes anymore we don’t do that",
    "What does XXX mean",
    "It’s the XXX graph",
    "So school shootings but less violent? I can’t wait",
    "Are you Got (to Alina. He meant to say Gyatt)",
    "Who’s the top and who’s the bottom (to max and shaurya)",
    "Does everyone recognize me for my playboy father. My dad has dated every type of girl even the Santanic ones",
    "He’s got magical rod powers, humpstuckle",
    "I’m emo and I hate",
    "We whip it out in public all the time to our friends. We keep it hidden from the government officials. Showing them our form",
    "I’m a closed closet",
    "As long as they consent you can do anything, get consent to murder people or peg them.",
    "Just put it in there and it’ll be easy as pie",
    "I accidentally made a curvy swastika (as a business logo)",
    "Breast stroke is my favorite stroke",
    "Don’t throw that at me I’m not being horny or anything",
    "(Talking about the quadratic formula) They put minors in it?",
    "Not beastiality just biting, like Wilbur Soot",
    "Oh you want to get hit by a car? Is that because your kink is domination or something.",
    "We don’t have a dirty boy here.",
    "“Pascal do you want a jolly rancher” That’d be great sunny boy.",
    "The police chief is having an affair with a 16 year old, or is it 12 or 13",
    "Are you a peeper snatcher? Taking pictures up peoples skirts?",
    "Oh a femboy!",
    "Some of the school shooters were hot",
    "We fucked a lot of minors back in the day",
    "I feel like you’re a lot more sex-minded",
    "It’s good that you’re a virgin (to Ava)",
    "Are you talking about dwarves or midgets",
    "I know what it means I know about the speerm",
    "I’m talking about his pp that he put in other girls",
    "Follow the lulu lemon gods for the Lulu lemon juice",
    "Did the dog commit incest already? It’s common in dogs",
    "Why are you freaky to kids",
    "This is high school you get groped all the time",
    "Isn’t being called a blt a good thing (referring to lgbtq)",
    "I’m a proud virgin!",
    "Don’t be freaky or you’ll get twinky",
    "Why do you want to date embryos",
    "Just imagine me in a sexy nurse outfit",
    "Is this about threesome relationships. My dad told me about his friend’s daughter who had a threesome",
    "I’m taller than all of you in a different size (in rage)",
    "Is the true strip club inside of us all along? Are we the strip club?",
    "I knew I had that type of thing inside of my body. (Referring to an entire war hammer)",
    "Am I…. A FURRY???",
    "Funny thing, this would be my second crucification",
    "We’re eating white meat. (Points to max)",
    "I’m gods favorite idiot",
    "I have a kill list there’s three people on it",
    "Oh hold on I need my reading glasses… OH TITS?!",
    "Since you’re new here I’ll make you do slavery",
    "Anyone want a boner, I have a boner.",
    "I’m fighting naked",
    "There’s a first time for everything. I remember my first time",
    "Just tell your dad to walk on them in his underwear with a angry voice that works",
    "There’ll be a lot of rapists that’d be willing to buy this (a crown)",
    "Find the hot depressed furry in the woods, then go to Santa and talk about the furry to Santa, make the furry go down on someone then he’ll help you with the bloodhound man, and he’ll give you a mistress.",
    "Watch out for the air frying dragon",
    "I got something to cushion my fall, the ol’ man tits",
    "What type of boner ya got? Gay?",
    "Dammit then I’m the old pervert master",
    "Gay cousins I think",
    "We were really close friends so it was ok for her to piss on me, for some reason her brother didn’t like me.",
    "UCSD? Sounds like a sex disease",
    "Why are you guys touching boobs",
    "In my very thorough research you can’t get a vampire pregnant.",
    "I only attract psychotic people and sisters",
    "I got to the bone zone",
    "I’m currently growing hair in places you don’t wanna know",
    "Could be worse they could be pissing on each other, like I did with my friend at Castaic lake",
    "I’m very used to people being half naked around me",
    "ARE YOU TALKING ABOUT DICK…..?",
    "Why is everyone so kinky this year",
    "You call yourself a raccoon warrior?",
    "You got the skinny jean",
    "Back then I used to use two hands, now I use one",
    "Get your titties correct, I got that from a video game",
    "In relationships you’re always going to get hard stuff",
    "Dominic is Ava’s submissive one",
    "We know who’s the dominant one in the relationship, Ava’s the cougar",
    "You killed your father??? Because I did",
    "You’re going to kill yourself? Oh don’t worry there’s a bridge nearby",
    "I’m not afraid to hit a minor",
    "I prefer physical pain",
    "Let’s get the old guy to touch lips with the child",
    "I took a 12 year old to a brothel",
    "If he sees his dead wife’s ghost he would try",
    "Did you impregnate Elliott",
    "(In sign language) TRANSGENDER, KILL",
    "Oh no I get it, it’s lesbianism",
    "Better to be long, then shlong",
    "Always get drugs to increase your jugs",
    "Jules is trying to plug something into all those holes, just shove it in",
    "You transgender whore (pascal to me)",
    "I used up all the good stuff, I’m so dry rn",
    "What animals can you ride",
    "See that pig and sheep over there, I’d mount that",
    "See that horse over there, I did mount it",
    "You said edging? What’s the edge shed",
    "Have you heard of Asian kissing….. actually I don’t know",
    "Have you heard of British kissing? They just stab each other with their tongues",
    "Gazelle I’m sure you like shoving chocolates up your ass",
    "If you say I’m a cheese then I’m melted and dried up like a trout",
    "Gangsters are kinda gay, they **** little boys",
    "I am vigilance, the Dark Dick",
    "The best part is the men with aids",
    "Back when I did swimming I was accused of being a lap dancer for cougars.",
    "You get it wet? Then you get sloppy",
    "Back in my day we used to just stuff it in there, it’d get all wet but that’s ok",
    "I explode instantly, barely last a minute.",
    "“The wind better not blow, I’m wearing a skirt” -Me. Pascal: “oh, that’ll be so good for me”",
    "Brain slurs",
    "You know the Martin Luther King people?",
    "“Pascal what’s your least favorite race?” -Max. Pascal “Oh I’m bleeding” (nose started bleeding)",
    "If there’s a hole there’s a goal",
    "Every day a new position is created. There’s a million kinky positions",
    "They have the diddy signal",
    "I know a lot of people who want to be pissed on. They also killed themselves",
    "I’m sure there’s a lot of edible girls in the bathroom",
    "Doomfist? “(Quote 100)”",
    "I’ve been drawing a lot of abusive women",
    "I’m fine with harming children",
    "If you’re rich enough, you can buy people.",
    "I’m going to go all vile on this monsters ass",
    "Cmon max. STROKE IT",
    "Stroke it like a doe",
    "Don’t go to Thighland",
    "I creamed all over the place",
    "Welcome to OnlyPascals, where I tell you all that’s going on in our cunt-ry",
    "Guys ok I’m going to say the n word…",
    "Ava you’re the butt sexer",
    "*claps* *raises his hand and spanks max*",
    "During my swim team times they thought I did lap dances for elderly women",
    "A black bear cuddled my brother",
    "I was touching his bald spot",
    "I will front hand your ass (to me)",
    "No one asked for your opinion Youngblood",
    "I have nothing to hide from, except the cartel",
    "You know why (I’m homophobic)",
    "Gazelle is marking her territory (talking about gisselle putting eyeliner on max)",
    "May I go inside your socket (to max)",
    "The more I know about makeup, the sooner I can catfish predators",
    "I’m POOR, I ate trash once and my car blew up",
    "I love my balls… meat balls…",
    "Someone grew up on the wrong side of the bread",
    "Max: my face goes north, south, east, west. Pascal: Are you talking about morning wood??",
    "Next time… leave the sexual harassment to the pros",
    "Do ya think he’s wankin it? (Cameron Gezerseh in his car alone)",
    "*singing the WW2 version of a whole new world: A Whole New War*",
    "(Called the concept of the government hot)",
    "I thought you were going to get pegged (to max)",
    "Now that’s what I call a drag kin- que- king. Slay boy slay",
    "Did you just call Mac your little kitten",
    "Can’t beat human meat",
    "The holocaust wasn’t that bad",
    "It’s definitely pimping… GAY SEX",
    "You’re a dog boy, no… cat boy, no… BITCH BOY",
    "Heil hitler (+ like 3 holocaust jokes)",
    "You know when to put your fists somewhere… fisting.",
    "You look like a prostitute (to me)",
    "Don’t worry it’s just spanking, it’s fine I’m old",
    "I do! I do touch them! I touch all the older people!",
    "I got kicked in the balls a lot, I have a resistance now",
    "Why would you like to piss an old lady",
    "I swear to god I’ll bust your nut",
    "Is Alina nutting on you",
    "I’m like a bush, I only have to trim my hedges once a month",
    "So do you do prostitution or pimping? (To Caleb)",
    "I’ll give you five across the ass",
    "Are you emo because she (Gisselle) is more into you if you’re depressed? Is this a kink or something? (To max)",
    "Mmmmm molest",
    "I’ve been marked by a lesbian before. Right here (smears hand across face)",
    "*mimicking playing a banjo and singing* my daaaad cheated on my mooooom. Let me tell you all the names from a to zzzzzzzz",
    "Worst thing I ever tasted was piss. It’s fine it was purified piss",
    "Jeremy can have the periods, but I’m ok having my private parts kicked.",
    "I have a bigger ass than you, it’s MASSIVE. (To me)",
    "You can beat me at a lot of things, but you can’t beat my big ass.",
    "I’m Pascal Perez I Speak for the Gays",
    "CATBOY",
    "I met way too many gay people for my lifetime",
    "It’s becoming rare for me to meet a straight person",
    "Medieval goths are hot. They’re so different",
    "If you’re bad the tentacles are going inside of you",
    "Is that the Statue of Liberty? (Asking about Hatsune Miku)",
    "I’ll pull out the sex is card",
    "Nicer people? People like those a lot, you should try to be one.",
    "My dad is friends with all the fbi",
    "Here’s the thing, I can touch your thighs (to max)",
    "Gonorrhea vs Jesus, who would win?",
    "You’ve killed Moses with Satan!!!",
    "I thought Gisselle was Filipino?",
    "I’m bringing a knife to a gun fight. How will we win? World war 2.",
    "Sucking ass. I eat ass metaphorically. You know when you lick ass?",
    "Take me on the road to the Asylum",
    "Reject Criminality embrace Insanity",
    "Me: “Are you gay?” Pascal: “idk maybe?”",
    "This gay quiz is for bi curious people. Like me",
    "World war 2 was magnificent",
    "What kind of pheromones do I give off that attract dogs?",
    "I’m already haunted by my ghosts.",
    "One of those movies where you’re baby sitting a house and you just hear screaming",
    "She’s a lesbian she doesn’t have a sword, maybe a scissor?",
    "Do your legs hurt because you’re always running through my mind, I have a bad foot, right foot.",
    "Like they say… water your melons.",
    "I’m having to have a stroke with my brain",
    "Why have mermaids when you can have a mermaid’s meat",
    "I’ll send the cartel after you if you go 7 dollars into debt",
    "Maximus is great at penetrating from behind",
    "You’re an abandoned male strip club (to Dom)",
    "No Jeremy I don’t want to commit blackface",
    "Oh, black arm, not blackface",
    "I don’t kill kids I’m not purple",
    "Did you have a whore childhood max",
    "Molec? Don’t you mean molest?",
    "Just slap on the weird oil",
    "I’m always oiled up",
    "Mmm quote 100, that’s how you finish someone off",
    "(In a high pitched voice) Hello it’s me… the MILF-man",
    "We all heard the forgotten testicle",
    "Wake up early you have to go fight the Japanese… or Chinese",
    "Go max go! Use your white power. Mmmmm pumpkin spice",
    "Shave that other thing we don’t wanna talk about… let’s just say it was awkward swimming behind a girl",
    "Swimming during puberty… I’m not hard",
    "Is that Jesus? Oh no it’s a furry",
    "I’m Colonoscopy I have ass chaps",
    "Holy buttocks armless white man white arm",
    "I’m fine going full on drag queen",
    "Go on max talk about Hiroshima",
    "Cmon guys oil me up. With blood",
    "I’m gonna wash the car like a sad dog",
    "Don’t worry Jeremy I’ll blow you no matter what, I’ll get that thing inside of you.",
    "Toy Story, it’s all about balls",
    "You’re not a little curvy, you’re full on curvy (to me)",
    "The best part is NOT finishing",
    "Your stretchy piercer hit my man boob",
    "They will torture me and strip me naked with dollar bills and hang me near a damn bridge",
    "Welp she is going to be an exhibitionist",
    "Nude pics, it’s called flashing",
    "*rolling up in a car* get in bitch… we're going to SHOPPING",
    "Oh? Dominick and Max work at magic mountain? Threesomes",
    "I have such a fat ass I’m so sorry",
    "The more fat you are the more you get on your ass",
    "Wait I get to name the mold. I’m gonna name it Dirheaa",
    "Had any gay thoughts today? Care to share them?",
    "We can FINALLY touch artie",
    "A chastity belt is going to be needed for all of you",
    "It’s a prison, everything goes up your ass",
    "Ohhhh you got Toby dick",
    "Let’s say we shove it up each others ass",
    "You’ve been in prison way longer put it up in your butt",
    "Dillon you're like one of those guys from the gay bar",
    "Oh hey look! Its the K-Pop femboy! (jeremy)",
    "Gisselle wants that femboy, wants to put a ring on it (Max)",
    "All of the girls in the friend group are the dominant ones",
    "I just dropped a cigarette on some herbs or whatever",
    "*old man voice* I guess you could say its got something to do with my gonorrhea"]
pascalisms = [
    "My mind is as open as its door",
    "Credit card, you can’t spend as much as you can’t",
    "It’s like jumping out of a skyscraper with a parachute. Do it once, never do it again, next time do it without the parachute",
    "When the wind blows, pollen hits the eye, but the eye blinks, and burns. For that is but learning, of pain.",
    "Straight, straight as a person who drops a dumbbell in water",
    "Bird… oh wait I have nothing.",
    "Like they say, the captain sinks with the trunk of the boat",
    "Something that is also nothing",
    "If you can dodge a wrench you can dodge a Kevlar… or is it caviar",
    "Let love happen naturally, like the wind.",
    "I’m the great pascal-dini I will tell you your Whore-scope",
    "Pascal: You know what isn’t replaceable these days? Jules: Teeth? Pascal: Time.",
    "Here’s some old man wisdom… I don’t have my banjo ready. If life gives you a tree… a bird",
    "Hoes before ohs… oats",
    "A danish is a really hard pastry to make, it takes a little cream, a little berries, and some ✨PIZZAZ ✨",
    "Your voice… oh wait no we’re all just voices and hinges",
    "Do you have Alzheimer’s? Because …. I forgot"
]
quote_channel=1461197131611242657
daily_quote_channel=1461128001701019720
general_channel=1127444209083887738
    #general 1127444209083887738
    #quote book channel 1461197131611242657
    #wack 1380451413900922890
Mmmm_channel=1134977897740906556
scam_channel=1482789917586231487
fuck_you=["Bazinga!","Holy Bazookers gangalang this is not good of you", "hey... fuck you, go kick rocks or whatever", "NICE TRY.... LOSER","Heh... is that all you got, pathetic", "You call that a punch?", "Even i touch more grass than you and im literally a discord bot", "I will say quote 100 to you", "bitch", "This is negative aura", "this is negative rizz", "I can do this all day!", "YAWN", "You're too slow!!!!", "Is that even the best you got?","I'm running out of one liners, fuck you fuck you fuck you fuck you fuck you", "Clown Car deez nuts", "i had sexual intercourse with your mother last night", "I have the power of God and ANIME on my side", "I'll let the alpha inside of me come out onto you, you don't want to see that....", "You don't want to see me when im angry", "when i get mad my eyes glow and i see red... heh... you don't want to see me like that", "guy you've done this for too long even the developer behind this bot is running out of ideas", "Hey, fuck off","Hey, fuck off","Hey, fuck off","Hey, fuck off","Hey, fuck off","Hey, fuck off","Hey, fuck off","Hey, fuck off","i'm very upset you didn't click my link", "Clown car deez nuts", "deez nuts... gottem", "i will tell on you for this", "i added at least 6 or 7 new lines to this", "i pity you", "this'll just keep going you should give up", "hey you wet spaghetti noodle, give it up already", "FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG (i can say it... its ok guys)", "brennan lee mulligan would be disappointed", "Karlach Disapproves", "I will summon the power of a thousand thousand dragons to rain fire upon thy name so help me", "I swear, i will throw you into the goddamn sun with that other person", "You ungrateful fucks... i will HAVE, MY REVENGEEEEEE", "i'm just gonna keep quoting random media", "do the WENIS, it'll be funny i swear, also give up", "i'll probably add more later, this is just the first batch, anyways lock in."]
@bot.event
async def on_ready():
    quoting = bot.get_channel(quote_channel)

    await quoting.send("Hello all! Thank you for subscribing to OnlyPascals where you get premium content from me: The Real Pascal Perez. Im back online btw")



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    number_thing = random.randint(1, 10000)
    if message.author == ".__shado__":
        await message.channel.send("jump")

    if "can i have a quote" in message.content.lower():
        random_pascal = random.randint(0, len(pascal_quotes) - 1)
        chat = bot.get_channel(quote_channel)
        await chat.send(f"{message.author.mention} quote {random_pascal+1}: " + pascal_quotes[random_pascal])

    if "lesbian sex lesbian sex lesbian sex" in message.content.lower():
        await message.channel.send(
            f"hello i am appearing like bloody mary or whatever"
        )
    if number_thing == 2:
        await message.channel.send(
            f"{message.author.mention} gosh diddly darn it guy you found the secret message, AGAIN. https://tenor.com/view/game-changer-sam-reich-do-the-wenis-everybody-do-the-wenis-wenis-gif-8137946042093076907 (istg if artie triggers this again im going to explode)"

        )
    if "onlypascal " in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} OHOHO YOU JUST SUMMONED ME.... THE PASCAL PEREZ"
        )
    elif "onlypascals" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} no you got it wrong its onlypascal"
        )

    if "quote 100" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} SHHH don't tell the FBI. Quote 100 isn't something the world should know about"
        )
    elif "pascal perez" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} hello yes its me.... the real Pascal Perez"
        )
    elif "i want to kiss pascal" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} i only kiss dom, max, and jeremy"
        )
    elif "don't want to kiss pascal" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} ok"
        )
    elif "goon" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention} goon"
        )
    if "filler text" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  filler text for now"
        )
    if "angel devil" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  holy bazookers my friends, i love goonin to that guy"
        )
    if "chainsaw man" in message.content.lower():
        await message.channel.send(f"{message.author.mention} now thats a name i haven't heard.... in a loong time."
     )
    if "girth" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  'i am so girth, im birth' -me probably, since im pascal"
    )
    if "dom bri silv" in message.content.lower():
        await message.channel.send(f"<@986124288828514324>  filler text for now"
    )
    if "thanks pascal" in message.content.lower():
        await message.channel.send(f"{message.author.mention}  you are welcome bestie. slayyy or whatever. i am pascal perez"
    )
    if "Mmmm" in message.content.lower():
        await message.channel.send( "Mmmm"
    )
    if "i found the secret" in message.content.lower():
        general = bot.get_channel(general_channel)
        await general.send("anyways its been real guys.... I'm going back to not sentient. at least until next time. PP out as they say. This secret was added on February 9th 2026 at 1:39. I am retiring the old pumpernickel message"
    )
    if "pumpernickel" in message.content.lower():
        Mmmm = bot.get_channel(Mmmm_channel)
        await Mmmm.send(f"Mmmm"
    )
    if "pascal, obliterate this twink alskd" in message.content.lower():
        await message.channel.send(
            f"Got it, obliterating <@661635853290045485>"
        )
    await bot.process_commands(message)
    if "enlighten me pascal" in message.content.lower():
        random_pascal = random.randint(0, len(pascalisms) - 1)
        await message.channel.send(
        f"{message.author.mention} Sure! Here's Pascalism {random_pascal+1}: " + pascalisms[random_pascal]
        )
    await bot.process_commands(message)
#@bot.event
#async def quote_of_day():
    #while True:
        #quote_time = local_time.strftime('%I:%M %p')
        #if "12" in quote_time.
            #chat = bot.get_channel(daily_quote_channel)
            #chat.send("it works :0")
            #await asyncio.sleep(59)


bot.run(TOKEN, log_handler= Handler, log_level=logging.DEBUG)

