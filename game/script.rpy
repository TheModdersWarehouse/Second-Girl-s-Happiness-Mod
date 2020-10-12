
define k = Character("Kendra", color="#ffc0cb")
define e = Character("Emily", color="#b8860b")
define g = Character("Gianna", color="#20b2aa")
define kat = Character("Katrina", color="#800080")
define all = Character("All", color="#ffff00")
define ken = Character("Kenneth", color="#b8860b")
define s = Character("Sandra", color="#ffff00")
define st = Character("Stewardess", color="#ffff00")
define sty = Character("Stylist", color="#ffc0cb")

label start:
    scene blackscreen
    $ kendra = 0
    $ katrina = 0
    $ gianna = 0
    $ emily = 0
    $ harem = 0
    $ katdom = 0
    $ futurevariable1 = 0
    $ futurevariable2 = 0
    $ futurevariable3 = 0
    $ futurevariablea = 0
    $ futurevariableb = 0
    $ futurevariablec = 0
    $ futurevariabled = 0
    $ exercise = 0
    $ confidence = 0
    $ nopants = False
    $ kendrakiss = False
    $ knees = False
    $ bribestewardess = False
    "WARNING: This is a game meant for adults ages 18 and older.  Please close the game immediately if you are underage."
    scene salon1
    sty "Oh hey there!  Are you my 5:30?"
    $ y = renpy.input("Answer with your name. (Default is Kyle)")
    if y == "":
        $ y = "Kyle"
    define y = Character("[y]", color="#800000")
    scene salon2
    y "Yep, I'm [y]!  Nice to meet you!"
    "The stylist leads you to a chair and put a barber smock over you."
    scene salon5
    sty "So what're we thinking today?"
    y "I was kind of hoping you could tell me.  Normally I just cut my hair with clippers in the bathroom every few months."
    scene salon3
    sty "Ok, well how about shorter on the back and sides, with some subtle layers on top, and let's add some blonde highlights to help bring out your blue eyes."
    y "I actually just came from the eye doctor.  I was there getting contacts, so it'd be great to show off my eyes!"
    sty "So what makes a guy go from cutting his own hair in the bathroom to a $100 haircut here?"
    y "Tonight is an important night!  I've invited my friends to a nearby cafe to celebrate the success of a mobile game I made called {i}Caelum Besieged{/i}."
    scene salon5
    y "I was actually hoping to see a personal shopper and get some help picking up a nice outfit, but I ended up in the waiting room at the eye doctor for longer than I hoped."
    sty "Isn't that always the way at doctors' offices...."
    jump cafe
label cafe:
    scene cafe1
    k "So did any of you actually play the game [y] created?"
    scene cafe5
    g "No, was it any fun?  You know I've never been into gaming."
    scene cafe3
    kat "Yeah, I didn't play it either.  After reading some of his Hearthstone fanfiction I'm kinda done with anything [y] creates."
    scene cafe2
    e "I played his closed beta a few months ago for like fifteen minutes.  It was pretty clear there was going to be way too much grinding, so I stopped."
    scene cafe4
    k "Did you stream it on your Twitch channel?"
    scene cafe2
    e "Oh hell no!  I haven't been getting as many new viewers lately and can't afford to lose any playing some lame game!"
    e "Like Katrina said, after reading his weird fanfiction who knows what's gonna be in that game.  I mean there's like no way Reno Jackson and Elise could ever be together!"
    scene cafe4
    k "I still can't believe he made a fanfiction of a card game, which itself is based on World of Warcraft!  It's like even a step nerdier than writing about WoW!"
    scene cafe5
    g "And now he's rented out this cafe to hold a party celebrating the success of his game.  I feel kinda bad since he's probably spent more renting out this cafe for the evening than his game will ever make."
    scene cafe4
    k "You know he's still crushing on all of us from when we were kids.  We've all turned him down time after time, but he still keeps trying."
    scene cafe2
    e "I feel bad too, I'm here because I know it's important to him and we used to play a lot of online games together, but I'd rather be home, to be honest."
    scene cafe1
    k "Listen, with us all finishing up college maybe it's time to help [y] move on."
    k "Let's use tonight to let him down easy and try to end our friendships with him on a somewhat positive note."
    kat "Yeah we can make this a party not for celebrating his game, but to new beginnings and moving on with life."
    g "I agree.  Maybe we can all chip in and pay for a bit of whatever he paid to rent this place tonight."
    e "Sounds good!  Ok, look out, here he comes!"
    scene cafe6
    all "Hey [y]!"
    scene cafe7
    y "Hey girls!  I'm so glad you could all make it tonight!"
    kat "Glad to be here [y], let's get some drinks!"
    y "Yeah get whatever you like, everything's on me tonight."
    g "You don't have to do that [y], we can each pay for our own. Nice haircut by the way!"
    y "C'mon, I insist!  And I know you didn't play my game much, if at all, but let's start with a toast!"
    scene cafe15
    y "To the success of my new game and to our never-ending friendships!"
    k "Here here!  But listen [y] there's something we need to all talk about."
    y "Wait one more toast I almost forgot!"
    y "And to becoming America's newest 22-year-old millionaire!"
    all "WAIT WHAT?!"
    scene cafe13
    y "Yeah I told you this was a little party to celebrate the success of my game.  Wellb it's had 800,000 mobile downloads and 250,000 steam downloads, and the average user spends $1-2 on in-game purchases."
    scene cafe10
    e "Oh my god [y]!  When I played it a few months ago I had no idea it was going to take off like that!"
    y "I have to thank you Emily for letting me know the grind was too much.  This is partially thanks to you."
    scene cafe12
    k "I'm super happy for you [y], but we were talking before you got here and we're thinking of making this party more than about just your game.  Now, this might be hard for you to hear, but..."
    scene cafe14
    kat "WAIT WAIT Kendra!  Forget what you were about to say, this party is about [y] and his wonderful new game!  Let's keep the spotlight on him tonight!"
    y "Uh ok, well thanks Katrina, I guess."
    scene cafe11
    kat "Seriously [y], a millionaire!  I can hardly believe it!  And this little party isn't enough to celebrate a big accomplishment like that.  We need to go bigger!"
    kat "Like we should all go on a vacation together!"
    scene cafe8
    g "It's summer break from college, so we're all free to go."
    scene cafe10
    e "Could you work on the game remotely?"
    scene cafe13
    y "Yeah I guess I could.  But I don't know, you guys never wanted to go on a vacation before."
    scene cafe11
    kat "Well we didn't have money before, and now we do!"
    scene cafe12
    k "We don't have money Katrina, [y] has money."
    scene cafe14
    kat "And he'll still have tons of money after the vacation too, so what's the big deal if he spoils us a little?"
    k "'Did you forget what we were talking about right before he got here?  [y], what do you think?  Do you really want to take us on a vacation that you have to pay for?"
    scene cafe13
    y "I don't really mind Kendra.  We never hang out anymore.  If that's what it takes to get to spend time with you guys again I'm all for it."
    y "So yeah, why not, I'll spring for a fun trip with all of us!"
    scene cafe11
    kat "Great [y]!  I'll plan everything!  This is gonna be soooooo fun!"
    scene cafe9
    "You spend the rest of the evening drinking and chatting.  It had been so long since you all got together like this."
    "Katrina, Gianna, and Emily were all way nicer to you than usual, but you chalked it up to the beer.  Kendra seemed a little distant though like something else was on her mind."
    jump nextmorning1
label nextmorning1:
    scene kylecell1
    "The next morning you wake up to your cell going off."
    "BEEP"
    "It looks like it's Katrina calling.  In the past, she's only ever called you when she wanted something, usually your money, or manual labor, or to give her a ride somewhere, at least before she got a car.  Now she never calls."
    scene katrinabio
    "Katrina and the other three girls grew up in your neighborhood.  While you wouldn't say Katrina is the leader of the group, you would definitely say she tends to get her way the most."
    "In your early teens, she developed the bad habit of using her good looks and personality to get whatever she wanted from guys (mostly you)."
    "If she paid me back all the money I've 'lent' her over the years and for all the stuff I've bought her, I wouldn't have even had to make my game, you chuckle to yourself."
    "One time you bought her a $250 necklace she begged you for and you decided it was time to ask her out."
    "She yelled at you and said what a jerk you are for trying to 'buy her love', and in the end, you were forced to buy her matching earrings to calm her down."
    "Since then you tried to avoid getting sucked into helping her so much."
    "While the rest of you are going into your final year of your bachelor's degree, Katrina has already finished hers in psychology and is actually nearly finished her masters."
    "You overheard a professor once calling her a prodigy."
    scene kylecell1
    y "Hello?  Katrina?  What's up?  It's still pretty early."
    scene katrinacell1
    kat "Sorry [y] did I wake you?  I've been up for a while now.  I was thinking about you ALL night last night!"
    y "For real?"
    kat "Yeah for real!  And I've been thinking of the vacation we're gonna take.  How about Hawaii a week from now?"
    scene kylecell1
    y "I don't know Katrina, that sounds pretty expensive, especially on such short notice."
    scene katrinacell2
    kat "You're a millionaire now [y]!  It might be a little expensive, but you're still gonna be a millionaire afterward.  I bet you made more money last night while you were asleep than we'll spend on this trip."
    y "Ok, I do want to spend time with everyone again.  And I guess you're right about making money while I sleep, though fewer people download the game in the middle of the night than during the day."
    y "Let's set a budget of $20,000.  That should be more than enough to cover the trip even planning it just a week out.  Just be sure especially to book the plane tickets right away."
    kat "Of course, I'll go do that right now!  I can't wait to plan everything!  I'd love to see you this week though and get your input too if you want.  Call me anytime and I'll come right over!"
    scene kylecell1
    y "That sounds like fun.  It's been a long time since just you and I hung out too.  I'm pretty busy with the game and I'll have more to do this week than usual if I'm about to take time off, but I'll definitely call you if I get time."
    scene katrinacell1
    kat "You'll call me if you get time huh?  Look at you [y]!  I'm proud of you!  Before you'd have called me back after an hour tops!  You're finally growing some balls!"
    "Well I still caved and agreed to what's undoubtedly gonna be your super expensive vacation idea, you think."
    kat "And guess what?  I downloaded your game last night!"
    y "You did?  What did you think of it?"
    kat "Oh I didn't play it silly!  But if you check my Instagram you'll see a picture of me holding my phone up with it loaded and a caption saying how great my friend who made the game is!"
    y "Haha, ok I'll definitely check it out."
    scene kylecell1
    "BEEP"
    "You check and see Emily is calling."
    y "Hey Katrina, it looks like Emily is calling.  We'll talk more about the vacation later ok?"
    scene katrinacell2
    kat "Emily?  Doesn't she normally stream late into the evening?  I'm surprised she's up and calling you already."
    kat "Ok then, talk to ya later!"
    scene emilybio
    "Emily is the girl you still talk to the most out of your childhood friends."
    "You both became gamers and for a long time you played online games (mostly from Blizzard) together each night."
    "One of your best memories was when you both hit legend for first time in Hearthstone on the last day of September back in 2015 after working so hard all month."
    "You were crushing on her pretty hard by then, but she made it pretty clear you guys were just friends, so you never asked her out and suffered getting rejected, and in a way that helped you stay friends easier than with the other girls."
    "Shortly after that, she discovered that Hearthstone was one of the most popular games on Twitch and there weren't too many female legend players, so she took up streaming and had a decent amount of early success."
    "That meant not playing games with you anymore.  You tried it at first, but her viewers were always way fewer when you were playing with her.  You were sad not to play with her anymore, but you understood."
    "After the popularity of Hearthstone started to wane she tried out a few other games like Overwatch, CS:GO, Fortnite, some horror games, and last time you checked out her stream she had moved onto Valorant."
    "Lately though her stream has become kinda stagnant and you're wondering how much longer she'll be able to keep it going.  If she didn't still live with her parents she'd probably have already had to give it up."
    scene kylecell1
    y "Hey Emily, I was just talking to Katrina, you're up pretty early."
    scene emilycell1
    e "Yeah I didn't go to bed last night, I've been up all night."
    y "Really?  What for?"
    e "I have something to confess [y].  When you asked me to test your game a few months ago I only played it for like 15 minutes and then deleted it."
    e "I'm so so sorry.  I know that was a really shitty thing to do to a friend and that you had worked really hard on it."
    scene kylecell1
    "You're surprised and sad to hear she played it so little, but you decide to forgive her."
    y "Well I guess that's ok Emily.  You at least told me you thought it was too grindy, so that's something.  I'm happy you're being honest with me now.  I forgive you."
    scene emilycell2
    e "Thank goodness, I was so sad I let you down!"
    e "I was feeling so guilty that I stayed up all night streaming your game."
    scene kylecell1
    y "Oh really, you actually played it on stream?"
    scene emilycell1
    e "Yeah and I actually had way more viewers than normal too!"
    e "I bragged to everyone that I knew the guy that made the game!  I even told them I might be able to have you on the stream for an in-person interview!"
    e "What do you think [y]?  Would you do that for me?  It would really help me get my numbers up!"
    scene kylecell1
    y "I'll think about it, Emily.  I'll be really busy this week with development and getting the game into a state where I can leave on vacation with you guys, but if I get time I'll come on your stream."
    y "And if not this week then definitely when we get back after the vacation.  Or maybe even during vacation if we can get a decent internet connection wherever Katrina finds for us to stay."
    scene emilycell2
    e "That'd be sooooo awesome [y]!  You're the best!"
    e "And sorry again I didn't believe in your game's potential.  I'd play any game or read any fan fiction you ever make from now on!  Even if Sir Finley Mrrgglton is trying to get it on with Deathwing."
    y "Ewwww, it'd have to be with Alexstrasza!"
    scene kylecell1
    "BEEP"
    "This time it looks like Gianna is calling."
    y "Hey Emily, it looks like Gianna is trying to get a hold of me and she's never called me before ever.  I better take it cause it might be an emergency."
    e "Yeah you better check.  Talk to you later [y]!"
    scene giannabio
    "You've never been as close with Gianna as you were with the other girls.  She was mostly Kendra's friend and became friends with the rest of you through Kendra."
    "She played several sports back in high school and was on the same field hockey team as Kendra, who just played the one sport."
    "None of the rest of you were into sports, so you didn't have all that much in common."
    "That didn't stop you from asking her out though once it was clear you weren't going to get any of the others as a girlfriend."
    "She turned you down and actually seemed pretty surprised you were interested in her."
    "You've never really done anything with just you and her, only seeing her when it's the full group of friends.  And like you told Emily, you've called her before, but she's never been the one to call you."
    scene kylecell1
    y "Gianna!  Is everything ok?  Are you hurt or trapped in a burning car or your dog ran away in the direction of my house? WHAT'S WRONG?!"
    scene giannacell1
    g "Woah [y], everything is fine!  I just wanted to say hi!"
    scene kylecell1
    y "Oh thank goodness!  You never called me before so I was having a panic attack over here!"
    "You hear her beautiful laugh on the other end."
    scene giannacell2
    g "Yeah I can tell!  Calm down though, I just wanted to say hi and tell you I have a free pass if you want to come workout with me at the gym."
    scene kylecell1
    y "Is this the first time they gave you a free pass?  Don't those places give them out all the time to try to lure in new members?  You never invited me before."
    scene giannacell1
    g "Ummmm.... yeah.... well no, my gym doesn't give me them very often.  I think the last time was a year ago and I invited Kendra."
    "You bet she gets them all the time, but you can't really blame her for not inviting you."
    y "Ok Gianna if I get time this week I'll let you know.  I've got a lot to do before the vacation we take with Katrina to get the game in good shape, but we haven't hung out much just us and it sounds nice."
    scene giannacell1
    g "Ok [y], I hope you find the time.  And I'll be calling you a lot more often from now on so you don't have a heart attack in the future when you hear from me!"
    scene kylecell1
    "BEEP"
    "Kendra is calling.  You can't believe it.  Nearly a year of you always being the one to initiate every conversation with the girls, and now all four of them call you back to back."
    y "Gotta go, Gianna, Kendra is on the other line."
    "Gianna gives you another beautiful laugh."
    g "Ok [y], it's no secret she's your number one.  Go see what she wants."
    scene kendrabio
    "Kendra is your first and best friend.  Also at one time your one true love.  She grew up next door to you and you did everything together."
    "You have so many fantastic memories with her, learning to swim in her pool, playing hide and seek, going fishing, having family barbeques."
    "But things got weird when you asked her out."
    "You thought for sure she'd say yes, but she sighed and told you she didn't see you that way, that she saw you more as a brother."
    "After that, it wasn't really the same.  She still hung out with you in the group, but seldom alone, not even inviting you over to swim like she had nearly every summer day of your life."
    "If there's one person who holds your group of friends together (other than you of course) it's her.  You doubt if Katrina, Gianna, and Emily would stay friends without her, so you're super glad she's in all of your lives."
    scene kylecell1
    y "Hi Kendra!"
    scene kendracell1
    k "Hey [y], congrats again on the success of your game."
    y "Thanks Kendra, that means a lot."
    k "That's not the only reason I'm calling though.  Listen, the girls and I were talking before you arrived last night and I want to talk to you about it."
    k "Not on the phone though, do you think you could come over sometime this week?  It's something you should probably hear in person before we all go on vacation."
    scene kylecell1
    y "You sound pretty serious.  Yeah, I'll try to find time this week if I can.  Maybe we can even go swimming again in your parents' pool."
    k "I'd like that [y], and listen, with your newfound success I'm a little worried that the other girls will try to take advantage of you.  Just be on the lookout for that ok?'"
    y "Yeah I will Kendra, they actually all called earlier this morning."
    scene kendracell2
    k "I'm not surprised.  I know you've been interested in all of us as more than just friends in the past, and now that you're rich just watch out for people wanting to take advantage of you."
    k "That goes for others outside of our group as well.  A lot of people out there will pretend to like you just because of your money."
    k "But we can talk more about that in person.  If you get time this week, just swing by and knock on my door just like old times ok?"
    scene kylecell1
    y "Ok Kendra, I'll do that.  Talk to you later."
    jump week1
label week1:
    scene working1
    "You spend most of the day frantically working on your game in preparation for going away for awhile."
    "You find youself with a little free time in the afternoon."
    menu:
        "Invite Katrina over to help plan the vacation" if katrina == 0:
            jump katrinaweek1
        "Do an interview for Emily's Twitch Channel" if emily == 0:
            jump emilyweek1
        "Go to the gym and workout with Gianna" if gianna == 0:
            jump giannaweek1
        "Knock on Kendra's door like old times" if kendra == 0:
            jump kendraweek1


label katrinaweek1:
    scene workcall
    $ katrina = 1
    y "Hey Katrina, I'd love to hear your plans for the trip to Hawaii.  Do you think you could swing by my office later?"
    kat "It's great to hear from you [y]!  I'm free right now.  I'd love to visit your office, can you give me the address?"
    scene katrinaoffice2
    "A little while later Katrina arrives with a travel brochure."
    kat "I've been so busy this week, maybe even busier than you!"
    scene katrinaoffice3
    y "I can imagine, I remember whenever you were planning an event in the past you put your heart and soul into it!"
    kat "This trip is going to be legendary [y]!  I'm so happy for you and your game and the great opportunity we have now because of all your hard work."
    kat "Seriously thank you [y]!  Thank you thank you thank you!"
    y "It's my pleasure, Katrina!  I'm really happy we are all going to get to spend time together again.  You were right that the little cafe party wasn't enough."
    y "It was pretty hard to convince you all to even show up."
    scene katrinaoffice2
    kat "Go big or go home!  No one is going to be hard to convince when it comes to summer break in Hawaii!"
    y "Yeah looking back I should have booked a high-class restaurant instead of that single room cafe."
    kat "Well now you have me to help!  No one will ever turn down an invite from you again!"
    kat "Oh and I love the new office by the way!  Most guys usually move out of their parents' house before they rent their first office, but hey we can take care of that too when we get back."
    scene katrinaoffice3
    y "You mean you'll go house hunting with me?"
    kat "Yep!  I actually looked at a few online this week when I was taking a break from planning the trip, but I didn't want to get too far ahead of myself."
    y "Wow really?"
    scene katrinaoffice2
    kat "Yeah and I bet you didn't get a new car yet either, or better clothes, a luxury watch, designer sunglasses...."
    y "Well I did get a couple top of the line computers!"
    kat "Classic [y]!  Computers are your first love!  Even before me and Kendra on your list!"
    scene katrinaoffice3
    y "Ok you got me, I've actually spent very little of the money I made so far.  I do want to move out on my own pretty soon though.  I might take you up on the house hunting."
    y "As far as the car goes, I'm thinking Corvette.  I always wanted one of those!"
    kat "That'd be sooooo hot!  I could definitely picture you picking me up in a Corvette for a night on the town!"
    kat "You better look into it soon though.  What with the GM strike followed up by Covid-19 even the 2020 models are on backorder, and the 2021 models will be even harder to get."
    y "I didn't think of that."
    kat "Well as I said, you have me to help with this kinda thing now."
    scene katrinaoffice4
    kat "Now let me show you what I've got so far for the trip."
    "As Katrina goes through the brochure with you she puts her arm around your back."
    "She's always been the most physically affectionate of your group of friends, particularly when she wants something."
    "Katrina shows you the beach house she picked out, goes over several day trip options, asks your opinion on having a masseuse drop by each day, etc."
    kat "Of course we'll need to go to at least one luau too!  It wouldn't be Hawaii without one.  We need to book that online though"
    scene katrinaoffice5
    "She moves you over to the computer to book the luau and a few more events not in the brochure."
    "She places her hand on your arm and it feels great having her there next to you."
    y "I agree it wouldn't feel like Hawaii without a luau evening!  Plus grass skirts are awesome!  Maybe you girls could get some!"
    kat "That's a great idea [y]!  I've always wanted an authentic Hawaiian Hula outfit!"
    scene katrinaoffice6
    "You move to the couch where she begins showing you a few travel options she's bookmarked on her phone."
    "While she navigates from page to page her hand rubs up and down your leg."
    "You soon find yourself staring into her eyes instead of what she's trying to show you."
    scene katrinaoffice7
    "Suddenly Katrina drops her phone."
    kat "Could you get that for me [y]?"
    scene katrinaoffice9
    "You drop down to pick it up and when suddenly Katrina's dress falls next to you."
    "You look up in surprise."
    scene katrinaoffice10
    kat "Stay there for a moment [y].  I want to talk to you about something."
    kat "I know you said the budget for the trip would be $20,000.  But I think we better raise that to $50,000."
    scene katrinaoffice12
    "You start to rise but she places her hand on your shoulder, lightly pressing you back down on your knees.  For some reason, you feel like you can only just stare up at her helplessly."
    kat "We can have so much more fun if we spend a little more money.  We can make so many more happy memories.  You want to make me happy don't you [y]?"
    menu:
        "Agree to increase the vacation budget to $50,000[Gr] \[+1 Katrina Dominance\]":
            jump katrinaweek1a
        "Stand to your feet and refuse[Gr] \[+1 Confidence\]":
            jump katrinaweek1b
label katrinaweek1a:
    $ katdom = 1
    "You continue looking up at her and find yourself nodding in agreement."
    y "Yes Katrina, I do want to make you happy.  You can have the $50,000 for the vacation."
    kat "Good boy [y]!"
    scene katrinaoffice10
    "She lets go of your shoulder but you stay where you are."
    scene katrinaoffice11
    kat "By the way, what do you think of my shoes? I just got them."
    y "They look great Katrina.  Your feet look really cute in those."
    kat "And the rest of my outfit, what do you think?"
    scene katrinaoffice13
    "She steps back and gives you a good look."
    y "You look so beautiful!"
    kat "I like the way you look right now too [y]."
    "You realize you're still down on your knees."
    kat "And my tattoos?  What do you think of those?  I've caught you looking several times and you've always looked away and pretended you weren't staring.  Now's your chance to take a good look."
    scene katrinaoffice14
    "She's right, you always wished you could have the opportunity to get a good long look at her tattoos."
    y "They are so beautiful!"
    kat "From now on you can look all you want.  You don't need to quickly avert your eyes and pretend you like weren't anymore."
    y "Thank you, Katrina."
    kat "Think of it as a reward, and good boys get rewarded.  Remember that."
    scene katrinaoffice15
    "Katrina puts her dress back on."
    kat "Well it's been fun and we got a lot of planning done today.  I'm sure you need to get back to work on your game."
    "You start to come back to your senses."
    y "Uh yeah, this was great, yeah the game..."
    kat "See you in a couple days [y]."
    scene working1
    "A few minutes after she leaves you find yourself sitting in front of the computer unable to focus."
    "You think about all the other times she got what she wanted from you.  They were nothing on this level.  Like before she wasn't even trying."
    "So this is what she can do when she actually really really wants something.  Wow!"
    if katrina + gianna + emily + kendra == 4:
        jump week2
    if katrina + gianna + emily + kendra <=3:
        jump week1
label katrinaweek1b:
    scene katrinaoffice13
    $ confidence += 1
    y "No Katrina!  $20,000 is already a lot of money."
    y "I'm looking forward to the trip and spending time with you, but I'm not falling back into the same old pattern of always giving in to whatever you ask of me."
    y "I hope you can understand and respect that."
    scene katrinaoffice8
    "Katrina quickly puts her dress back on and turns back to you."
    "Somehow it almost feels as if the room is darker now that she's unhappy."
    kat "Of course [y].  You're right $20,000 is plenty."
    kat "I'm actually pretty impressed you stood up to me."
    y "It wasn't easy!"
    kat "Oh geez I'm a little embarrassed right now.  I can't believe I took off my dress and got rejected!"
    y "I almost can't believe it either!"
    kat "But hey it's like I said before 'Go big or go home' so I went big just now on trying to convince you, but I won't let it get me down!"
    kat "You're really acting mature lately with your office, success, and standing up for yourself.  I hope you can forgive me for just now."
    y "Of course Katrina, let's just call it a bit of a misunderstanding and move on."
    scene katrinaoffice15
    "Her demeanor brightens right back up."
    kat "Great, well an idea popped into my head just now of a way to save a little money on the trip.  I've gotta run home and make a change to the plane tickets."
    y "Ok, it was fun planning with you today!  I know this trip is going to turn out great!"
    kat "Yeah!  See you in a few days [y]!"
    if katrina + gianna + emily + kendra == 4:
        jump week2
    if katrina + gianna + emily + kendra <=3:
        jump week1



label emilyweek1:
    scene workcall
    $ emily = 1
    y "Hey Emily, it looks like I'll have some free time in a bit if you want to do that interview on your Twitch channel."
    e "That's great!  I'm actually streaming right now.  Say 'hi' to chat!"
    "Wow, that's the first time she's ever answered one of your calls while she was streaming.  Usually, you're sent straight to voicemail if you happen to call during a stream."
    y "Hi chat!"
    e "They say hi back!"
    e "So when you get here just let yourself in and find me in my room.  The door will be open."
    y "Sounds good, see you soon!  Bye chat!"
    e "Heh!  They say bye too!"
    "About an hour later you arrive at Emily's and let yourself in"
    scene emilystream1
    e "Hey everybody he's here!  The creator of Caelum Besieged and my friend... [y]!"
    "You look over at chat and notice it's going crazy.  She has nearly 3,000 viewers and her title reads, 'Exclusive Interview with the creator of Caelum Besieged'."
    "You recall the last time you visited her stream a few months ago she only had about 250 viewers."
    "You also notice Emily's outfit (or lack thereof)."
    menu:
        "Call her out on not wearing any pants.[Gr] \[+1 Confidence\]":
            jump emilyweek1a
        "Pretend not to notice.":
            jump emilyweek1b
label emilyweek1a:
    $ confidence += 1
    $ nopants = True
    y "Wow Emily, I know people joke about not wearing pants when they are on camera sitting down behind a desk, but I can't believe you've gone through with it!"
    y "Like if you stood up even for a split second you'd be looking at a 30-day ban!"
    e "Ha ha ha, good one [y]!  Don't listen to him chat!  He used to mess around all the time like this back in the day with his own personal style of humor."
    e "He's kidding of course guys!"
    e "In fact, some of you might remember [y] here before he was rich and famous when he used to play games with me sometimes on stream back in 2015."
    e "Can I get some !followage in chat?  Let's see who was around back then!"
    "Chat starts to scroll really fast.  You chuckle as most of the people checking their followage have one that's less than an hour, let alone five years."
    jump emilyweek1b
label emilyweek1b:
    scene emilystream2
    "You pull up a chair and grab an extra headset she has for you."
    y "I have some exciting news!  I brought 100 promo codes good for $25 each in in-game currency to give away tonight!"
    e "Wow that's so generous, lemme just change the title to add that!"
    e "Ok, so here's how the giveaway and interview will work chat.  I'll choose questions for [y] at random and if I happen to choose yours you'll win a code!"
    scene emilystream13
    "Emily makes small talk with the chat for a few minutes and you occasionally chime in.  You guess that she's waiting for more people to enter the channel now that she's doing a giveaway."
    "You see her new title reads, 'Exclusive Interview with Caelum Besieged creator and $2,500 GIVEAWAY!'"
    "After a few minutes, she has over 10,000 viewers."
    scene emilystream2
    e "Now for the first question from user Rameses69... Are you really real-life friends with each other?"
    y "We are.  Emily and I have known each other for years and live in the same neighborhood.  I even knew her before her hair was pink!"
    e "Heh, impossible!  Pink is my natural hair color!"
    scene emilystream5
    e "A question from MelodyRiverSong... When is the next update coming?"
    y "Well here I gotta say what most developers say and what no one really wants to hear... soon!"
    "You see a bunch of Soon(TM)'s whizzing down chat"
    scene emilystream4
    e "Oh wow, this next question from BatSuperMan2001... what is Emily like in bed?"
    e "Well [y], care to answer?"
    y "Ummm, sorry guys, I wish I could answer that one, but I struck out!"
    "You look over at chat and see a ton of messages like GIVE HIM A CHANCE, SWING AND A MISS, LET HIM HAVE ANOTHER AT BAT!"
    scene emilystream2
    e "Ok calm down guys!"
    e "Next question... What kind of endgame content can we expect in the next patch?"
    "You do your best to be entertaining and informative while answering the rest of the questions."
    scene emilystream3
    "You find yourself constantly distracted by Emily's tiny thong, but try not to stare too much so chat doesn't call you out on why you're always looking down."
    "At one point you notice she has over 12,000 viewers."
    scene emilystream13
    e "Ok guys, I'm sorry to say that was the last question!"
    e "I'll be streaming again tomorrow and all weekend, but on Monday I'll be in Hawaii with [y] here and a couple of our other friends for a week."
    e "But don't worry, I'll try to stream a little each day there too!  And I will do my best to get [y] to sponsor the stream again with more promo codes!"
    "The chat is full of people excited about more giveaways, as well as a lot of speculation about what will happen in Hawaii between the two of you."
    e "And when I get back we'll set a subscriber goal and then when we hit it I'll cosplay as one of the characters from [y]'s game!"
    e "So goodnight, for now, don't forget to follow if you liked the stream and I'll see you all tomorrow!"
    scene emilystream6
    "Emily randomly picks another streamer to raid and then switches off the stream and jumps up."
    e "DID YOU SEE THOSE VIEWER NUMBERS?!  Oh my god!  I never hit five digits before!  Not even when I first started streaming back when I was really popular!"
    e "I'm really turning things around and I have you to thank!  Plus that giveaway you provided... WOW!  It's been forever since I've been able to do a giveaway of something I didn't buy with my own money!"
    y "I'm glad I could help!"
    scene emilystream7
    e "My channel had been doing bad lately.  I was scared I was going to have to give up and get a real job.  This is just what I needed [y], you're the best!"
    e "I'm going to repay you somehow for this!  Just wait for the trip next week!  I'm going to personally guarantee you have the best vacation of your life!"
    scene emilystream9
    e "Do you think you can come on the stream again with some more giveaways while we're there?"
    y "I'll see what I can do."
    e "I can't wait!  I haven't been this happy in a long time!"
    if nopants == True:
        scene emilystream8
        e "BTW I can't believe you threw me under the bus though about not wearing pants!"
        y "I was shocked, to be honest and I just kinda blurted it out!  I've never seen you like this and if you had stood up thousands of people would have seen your sexy thong."
        e "You think it's sexy?"
        y "It says sexy right on it!"
        scene emilystream11
        e "Well I'll let you in on a little secret since you helped me out so much tonight... I kinda get a kick out of almost exposing myself on stream."
        e "Sometimes underneath the desk I go completely bottomless!"
        y "Wow really?"
        e "I get a thrill knowing that people are watching me, never knowing that if I just stood up they'd get the view of their dreams!"
        e "I have something else to confess as well, though it probably would be better if you were still sitting down!"
        scene emilystream10
        e "When just you and I used to play online together back in the day over Skype, I'd sometimes play completely naked with the video turned on."
        e "If you had ever switched from just audio to video you'd have seen everything!"
        "You mentally strangle the younger version of yourself!"
        y "I guess that's why you sometimes sounded pretty excited even when we were playing boring escort missions and stuff."
        e "Yep!  Now you know my secret!"
        jump emilyweek1c
    if nopants == False:
        jump emilyweek1c
label emilyweek1c:
    scene emilystream12
    e "Anyway I'm gonna head to bed.  I'm going to get up early tomorrow and try an early stream to attract some more European viewers."
    y "This was fun, goodnight Emily, see you in a few days!"
    e "See ya [y]!"
    if katrina + gianna + emily + kendra == 4:
        jump week2
    if katrina + gianna + emily + kendra <=3:
        jump week1

label giannaweek1:
    $ gianna = 1
    scene gym9
    "You arrive at the gym and Gianna launches herself into a big hug."
    g "I'm so glad you made it [y]!"
    "You are so surprised she's hugging you.  It's nothing like her typical greeting of giving you a nod and maybe a small smile if you're lucky."
    scene gym10
    "You get it together though and hug her back."
    y "Yeah I didn't want to pass up the chance to work out with you since we never get to hang out just the two of us."
    y "Besides, I've been meaning to start getting in shape."
    scene gym12
    g "That's great!  I'm so happy we are together today too!  I love your haircut and did you get contacts?"
    y "Yeah, it's nice of you to notice!"
    g "I got us this back room to use so we can work out in peace.  Normally they have kickboxing classes in here, so if you decide to join maybe we can try one out!"
    scene gym11
    y "Yeah that might be fun!  It looks like they've got a punching bag back there in the corner, maybe we try it out today a little."
    g "I like your t-shirt, by the way, nice skull!"
    y "Haha, yeah I went through a phase in high school where I thought skulls made people look badass.  Not sure if this shirt was going for some kinda political message though by giving it the stars and stripes."
    scene gym12
    g "I've actually got a bikini with skulls on it and I gotta say that I do look pretty badass wearing it!"
    y "Hey you should text me a pic.  I'd be happy to let you know how badass you look!"
    g "Ok [y], check your phone later!"
    y "Cool I can't wait!"
    g "Ready to start with some stretches?"
    scene gym1
    "The two of you begin to limber up."
    g "So how's work been going on your game this week?"
    y "Pretty good, really busy though since I won't be able to work on it much next week."
    scene gym2
    g "Yeah I'll bet.  I'd offer to help, but I don't know anything about programming or graphics or pretty much anything technical."
    "Gianna is doing downward dog right in front of you.  It's pretty hard not to stare."
    y "That's nice of you to say, Gianna.  I'm kind of a perfectionist with the technical stuff, so I actually prefer working alone even though it's a lot to do."
    scene gym3
    "You find your eyes drawn more and more towards her."
    g "Have you thought about next year?  I mean is it even worth it to go back for your last year of college?"
    y "I've actually been giving that a lot of thought.  I'm still on the fence about whether to take a year off while the game is doing well..."
    y "Or maybe I'll try part-time and graduate in two more years."
    g "I'd probably go for the part-time plan.  A degree is important."
    g "Now let's see some pushups soldier!"
    "Gianna laughs and you are again reminded of how beautiful it sounds."
    scene gym8
    "She cheers you on and even though you hadn't done any pushups in quite a while you actually manage to do 30."
    "If you'd have been by yourself you'd have probably collapsed back at 20, but you wanted to impress her (or at least not look too much like a weakling)."
    y "Enough pushups for now.  That kickboxing class you mentioned actually sounds like something I might like to try sometime, so let's check out the punching bag."
    scene gym4
    "You spend the next few minutes striking the bag.  It doesn't take your knuckles long to start hurting."
    "Gianna sees you shake out your hands."
    g "You might wanna invest in some bag gloves before you try a class, though your knuckles will harden up if you keep at it."
    scene gym5
    "You switch over to some kicks and find yourself having a lot of fun."
    g "You're actually a pretty tall guy [y] and look you can kick the top of the bag, impressive!"
    g "Ok my turn!"
    scene gym6
    "You watch Gianna take a turn kicking the bag and admire her form."
    g "This makes me feel like a ninja!  Check this out!"
    scene gym7
    "Gianna takes a flying punch at the bag nearly knocking it off of the chain."
    "The two of you spend the next 30 minutes taking turns on the bag and having lots of fun trying to one-up each other's ninja moves."
    scene gym10
    "Eventually it's time to go and you hug goodbye."
    g "I guess I won't see you again for a few days, but I'm really looking forward to next week."
    scene gym12
    g "I had a great time working out with you today.  I hope you do decide to join and take some kickboxing classes with me when we get back!"
    scene gym11
    y "Yeah today was a lot of fun!  I really needed the break from work and hanging out just the two of us was great!"
    y "I'll definitely join and take those classes with you once we're back!"
    g "Awesome!  See you in a few days then [y]!"
    y "See you in a few days, Gianna."
    scene gym16
    "You get back and think about your time with Gianna."
    "That almost felt like a date!  Hugging hello and goodbye, promising to meet up again, just the two of us."
    "Your phone chimes to let you know you have a picture message."
    scene gym13
    g "Told you I look badass with skulls!"
    menu:
        "Agree with her":
            jump giannaweek1b
        "Ask for an even sexier version[Gr] \[+1 Confidence & bonus scene later\]":
            jump giannaweek1c
label giannaweek1b:
    "You text her back that she does look badass."
    "You can't wait to see her wearing it in person next week on vacation."
    "Well anyway, time to get back to work on the game."
    jump week1
label giannaweek1c:
    $ confidence += 1
    $ knees = True
    y "You do look badass, but I want to see you on your knees!"
    "Several minutes go by and you begin to worry that you took it too far."
    "Your phone chimes again."
    scene gym14
    g "You mean like this [y]?"
    "Your phone chimes again."
    scene gym15
    g "Or maybe you meant on the floor with me looking up at you like this?"
    "You can't believe it worked and she actually sent you these.  It's the first time in your life a girl has sent you sexy pics!"
    y "You look great on your knees Gianna!  See you in a few days."
    "Well anyway, time to get back to work on the game, you sigh to yourself."
    if katrina + gianna + emily + kendra == 4:
        jump week2
    if katrina + gianna + emily + kendra <=3:
        jump week1


label kendraweek1:
    scene pool1
    $ kendra = 1
    "You find yourself at Kendra's door.  You knocked on this door a thousand times when you were kids and it always led to fun."
    "Just like old times you think, and knock."
    scene pool2
    "After a moment Kendra's dad Kenneth comes to the door."
    "You've always respected him and Kendra's mom, Sandra."
    "Together their names Kenneth and Sandra combined to form Kendra, which is something you always thought was kinda cool if a little silly."
    ken "Come on in [y], good to see you again!"
    scene pool3
    "You enter the house and take a look at Kendra's father.  It's been about a year since you last saw him and he still intimidates you a little."
    "Despite the fact that you're a little taller than average at 6'2, he stands a few inches taller than you."
    ken "Kendra told us that you've made a mobile game and it's doing quite well."
    scene pool4
    y "Yes sir, I've worked really hard on it.  In fact, this week I've barely had time to sleep."
    ken "Hard work is important.  And I imagine you've hardly slept because next week you're planning a vacation with my daughter and a few of your other friends."
    y "Uh, yes sir, that's correct."
    scene pool3
    ken "Listen [y], I understand you kids are just about all grown up now, but this will still be Kendra's first time away from home without her mother and me, so I expect you to look out for her."
    y "Yes of course sir, I'd never let anything bad happen to Kendra."
    ken "That goes for you too though [y].  No funny business understand?  Kendra tells you no, or tells you she wants to come home at any point and you better respect that."
    y "I would never do anything to make Kendra uncomfortable and want to get away and come home early sir, you can count on me."
    ken "Good to hear it.  Now Sandra and I are leaving for a while to go shopping and get dinner.  We'll be back this evening.  Behave yourselves while we're gone."
    ken "I'll go let Kendra know you're here.  Why don't you go wait out by the pool?"
    scene poolwait
    "Well that wasn't the first awkward {i}you better respect my daughter{/i} talk you've had with Kendra's dad."
    "Still this is the first time they are leaving you alone with her at their house."
    "Growing up they had a rule that at least one her parents had to be home for you to be allowed over."
    "You wonder if this is some kind of test to see first if they can leave you alone at their house before they trust you to take their daughter to Hawaii."
    scene pool5
    "After a few minutes, Kendra comes out of the house in her towel."
    k "Hi [y]!  I'm glad you're here!"
    y "Well you made it sound like you had something pretty important to talk to me about, plus it's been a long time since we've been swimming, so yeah, here I am!"
    k "Yeah about that talk, let's sit down for a minute."
    scene pool6
    "You both sit down and Kendra takes a deep breath."
    k "It's about the other night at the cafe before you arrived."
    k "The girls and I were talking and listen, if you hadn't suddenly declared you were a millionaire I think our friendships would be over."
    scene pool7
    y "What do you mean?!"
    scene pool6
    k "You've been enamored with all of us for too long [y].  We thought it'd be for your own good.  Helping you move on.  You know, yanking off the band-aid so to speak."
    y "..."
    k "Are you going to say something?"
    y "..."
    k "[y], I know this is a lot to process. You and I have known each other for such a long time.  I just don't want you to get hurt."
    k "I know you are a good guy, and I want you to find a girl that appreciates you for who you are and not for your money."
    y "If I am such a good guy, why don't any of you like me?"
    k "[y], what do Emily, Gianna, Katrina, and I have in common?"
    scene pool7
    y "Ummm?"
    k "Confidence!  We all have confidence.  And that is what we are all looking for in a guy! You need to believe in yourself and stop selling yourself short."
    k "There is nothing sexier than a man with confidence.  One who knows what he wants and takes it."
    scene pool6
    k "All of us girls know that you are never able to say no to us.  You are fun to tease, but there is no thrill, no chase, no excitement."
    k "Even if we did say we wanted to take things to the next level with you, I doubt that you would have the confidence to do more than look and blush!"
    scene pool7
    y "Hey, that's not fair!"
    k "Ok, prove it!  Right now!  Kiss me!"
    y "..."
    scene pool6
    k "See, even now you won't do it! That is why the girls take advantage of you but don't consider you boyfriend material."
    k "[y], as your friend I am telling you to man up!  If you want to stop these girls, and any other girls that you meet going forward who discover you are rich from taking advantage of you, you need to man up!"
    k "Start believing that you are an amazing man and not a doormat for girls to walk over. Say no to requests that are not going to benefit you! Take chances and laugh when it goes wrong!"
    k "You deserve to find someone who is going to make you happy.  But before you do that you have to be happy with you."
    k "I think you should use this time in Hawaii to figure out how to be happy with who you are and how to be your best, most confident self."
    scene pool7
    y "I guess what you're saying makes a lot of sense.  In a way, I'm glad I finished the game though, or I guess everyone would have moved on and we wouldn't even be having this conversation."
    k "I know [y].  But that's enough serious talk for now ok?  Ready to go swimming?"
    scene pool8
    "With that, she stands up and drops her towel."
    y "Holy shit!"
    "You've never seen Kendra wearing such a daring bikini before."
    scene pool9
    k "Well I guess it's no secret you like my 'toxic' bikini!"
    y "Toxic?"
    k "Yeah Katrina got it for me and said I was too sweet and needed to balance my life out with a little toxicity!"
    k "So you're not the only one who's gotten a stern heart-to-heart talking to lately about changing yourself for the better.  She's right, I am a little too sweet."
    y "Hey I like sweet Kendra.  But yeah I do like that bikini a lot too!"
    k "Just don't look at my back ok?  This thing barely covers my ass!"
    scene pool10
    y "No promises!"
    scene pool11
    "You spend the next few hours swimming and playing around in the pool like old times."
    "The sadness you felt at hearing Kendra and the others were ready to move on begins to melt away and you decide Kendra is right and that you do need to have more confidence in yourself."
    scene pool12
    "At Kendra's suggestion, you also spend a little time tanning so you don't burn to a crisp the first day in Hawaii."
    k "With my light complexion and red hair I'm kinda dreading a week in the sun.  The last thing I need is more freckles!"
    y "Yeah I'm gonna have at load up on SPF 50!  Let's get back in the pool!"
    scene pool13
    "After awhile Kendra's parents get back."
    ken "Are you kids still out here?"
    s "Nice to see you again [y]!  How are your parents doing?"
    y "They're doing great ma'am.  They were talking about inviting you over for another barbeque sometime this summer."
    s "That'd be great, just tell them to call us whenever."
    y "I'll be sure to do that."
    s "So since you and Kendra have been having such a good time and now that you're a bit older, why don't the two of you finish the night in our jacuzzi."
    "Your mind instantly springs back to wondering if them leaving was a test to see if they can trust you and wonder if this is another test."
    "Despite coming over here all the time growing up you've never been invited to use their jacuzzi before.  It's out on the balcony through their bedroom."
    scene pool14
    "You look over at Kendra for help, but she doesn't say anything, apparently leaving the decision to you."
    menu:
        "Play it safe and head home":
            jump kendraweek1a
        "Take them up on their offer[Gr] \[+1 Confidence & kiss Kendra\]":
            jump kendraweek1b
label kendraweek1a:
    scene pool15
    y "I appreciate the offer, but I really need to get going."
    ken "Are you sure?"
    y "Yeah I still have some more programming to do tonight and I don't want to overstay my welcome."
    s "Ok [y], tell your parents we say hi"
    y "I'll do that, goodnight everyone."
    k "Goodnight [y], see you in a few days."
    if katrina + gianna + emily + kendra == 4:
        jump week2
    if katrina + gianna + emily + kendra <=3:
        jump week1
label kendraweek1b:
    scene pool13
    $ confidence += 1
    $ kendrakiss = True
    y "Wow that's very nice of you to offer.  I'd love to spend some more time with Kendra tonight."
    s "Ok, Kenneth and I will stay downstairs and give you two a little privacy.  Just remember to turn off the lights and jets when you're finished guys."
    scene pool17
    "You find yourself enjoying the sunset with Kendra in her parents' jacuzzi."
    y "This is great, when we get back I'll be looking for my own house.  I think I'm going to try to get a jacuzzi on a balcony too!"
    k "You've never been in here before right?  Even I'm usually not allowed in here."
    y "Yeah I was wondering why they decided to let us.  I'm thinking they're probably spying and it's some kind of test to see how much they can trust me before we leave for Hawaii."
    k "No, I don't think that's it.  And they aren't the type to spy after promising us some privacy."
    "The two of you continue chatting and joking around as the sun continues to set."
    scene pool16
    "You can't help thinking about how beautiful Kendra looks in the newly risen moonlight."
    "It almost seems like she's leaning in for a kiss."
    "You recall earlier when she lectured you about confidence after you had failed to kiss her when she challenged you."
    "Fuck it!  If she rejects me she rejects me, and you go for it!"
    scene pool20
    "To your surprise she doesn't pull away."
    "You kiss for a few moments and pull back."
    scene pool18
    k "I'm glad you did it [y]."
    y "Me too, oh geez, my heart is beating so fast."
    k "This doesn't mean we're dating though, think of it as a reward."
    y "What do you mean?"
    k "Well when you wondered if this was a test you were on the right track, but it was me testing you and not my parents."
    k "I texted them earlier while we were tanning and set it up so they'd offer to let us use the jacuzzi."
    k "I thought for sure you'd be too chicken to take them up on the offer."
    k "But here we are...."
    y "Yeah here we are."
    k "Hope you enjoyed our goodnight kiss as much as I did!  Maybe if you play your cards right you'll get another in Hawaii.  But for now, goodnight!"
    y "Ok, goodnight Kendra!"
    if katrina + gianna + emily + kendra == 4:
        jump week2
    if katrina + gianna + emily + kendra <=3:
        jump week1
label week2:
    scene workcall
    "As you're finishing up work the evening before the trip you get a call from Kendra."
    k "Hey [y], I feel bad about how brutally honest I was with you the other day and was thinking we should get together to clear the air before we leave tomorrow.  Wanna join me at the mall?"
    y "Sure, pick you up in an hour?"
    scene suitshop4
    "You pull into her driveway, but before you can even turn the car off she comes out the front door and gets in the passenger seat."
    scene suitshop5
    "You can't help glancing down at her pretty legs as she sits down next to you."
    scene suitshop6
    "When you glance up again you notice that her father is waving goodbye to the two of you from inside."
    "You give him a quick wave back and pull away before he can come out to talk to you."
    scene suitshop8
    "You ride to the mall in awkward silence and park in the garage."
    "As you get out of the car and start walking in, Kendra turns to you."
    k "I just want to say again how I really hope that you..."
    y "Kendra, I get it.  No hard feelings and no need to keep bringing it up."
    "She nods her head."
    y "So what do you need at the mall?"
    k "I thought I would look around and make sure that I have everything that we need for our trip tomorrow. I am pretty sure I do, but you can never be too prepared!"
    y "I'm glad you suggested that we go out.  I wanted to get a suit to wear on the plane tomorrow so we can fit in while flying first-class."
    k "That's a great idea!  And with how successful you are I bet you will have lots of opportunities to wear it in the future!"
    scene suitshop3
    "Kendra follows you as you walk towards the store your mom always took you to for clothes, but when you get there Kendra grabs your hand and laughs."
    k "It's a good thing I am here to help you!"
    "She teases you a bit as she leads you to a trendier store on the third floor."
    scene suitshop2
    k "Hmmm, let's see what would look good."
    "She holds up a few suits before finding a light gray pin-striped one she asks you to try on."
    scene suitshop1
    y "What do you think?"
    k "I think you shouldn't thrust your hips so far forward when you're modeling an outfit, but yeah it looks very handsome!"
    k "You seem to be more interested in your appearance lately, so maybe check some magazines to see how the models pose and practice in the mirror."
    y "That's good advice, thanks!  Let's get the suit too."
    "The two of you spend some more time at the mall hanging out and buying a couple more little items you might need on the trip."
    scene suitshop7
    "It's dark when you arrive back to Kendra's house."
    "You think about kissing her goodnight, but then someone from inside starts flicking the outside lights on and off."
    k "Daddy!"
    k "Well I better go in before he comes out.  See you tomorrow [y]."
    "She gives you a quick kiss on the cheek and you head home."
    jump planestart

label planestart:
    scene plane3
    "A few days later you and your friends are seated in first class on your way to Hawaii."
    "Well, all except for Kendra."
    scene plane4
    y "Katrina, where's Kendra?  You don't think she missed the flight do you?"
    kat "Oh didn't I mention it?  They only had four first-class tickets available on such short notice, so I got those plus one coach ticket."
    kat "I met her earlier in the terminal and gave her the ticket, so she's on the plane.  We'll see her when we disembark."
    kat "Hopefully it wasn't too much of a shock when she got to her seat and found out it wasn't with us."
    scene plane2
    e "She didn't know in advance?"
    scene plane3
    kat "No, but she's a big girl, she can handle it."
    y "I'd have taken that seat in coach."
    scene plane2
    g "No [y]!  That wouldn't be right!  You are the one paying for the trip!"
    scene plane1
    "Katrina puts her hand on yours."
    scene plane4
    kat "Yeah forget about Kendra for now.  Let's enjoy first-class together."
    y "But there a few empty seats here, so it looks like people didn't show up for the flight or something.  Maybe I could talk to the stewardess about bumping Kendra up to first class with us."
    jump week2a

label week2a:
    scene plane1
    kat "[y] relax, you are stressing out way too much about this."
    kat "Follow me to the bathroom and I'll help you calm down."
    scene plane2
    e "OMG what are you going to do to him in the bathroom?"
    g "Is [y] about to join the mile high club?"
    scene plane1
    kat "No, I'm not going to have sex with him, I'm just going to show him my tits."
    e "You are?"
    kat "Yeah, I'm sure staying in the same beach house for a week he'll end up seeing flashes of skin here and there anyway."
    kat "And I know you streamed together the other day.  I bet you weren't wearing pants again!"
    y "You know she doesn't wear pants?"
    kat "Yep, I walked in on her streaming one time and she spilled the beans about her little exhibitionism kink!"
    scene plane2
    e "Ok, point taken!  Hope you like Katrina's goodies [y]!"
    kat "Anyway let's go [y]!  Follow me."
    menu:
        "Follow Katrina to the bathroom.[Gr] \[+1 Katrina Dominance (Leads to H scene with Kat, but Kendra will not join 1st class\]":
            jump milehigh
        "Talk to the stewardess about upgrading Kendra's ticket.":
            jump kendra1stclass
        "[Gr]MOD: Do Both [Gr]\[Choice to add +1 Katrina Dominance or Not\]":
            ""
            menu:
                centered "[Gr]Do you want to add +1 Katrina Dominance"
                "Yes":
                    $ katdom += 1
                    jump modbothplaneroutes
                "No":
                    jump modbothplaneroutes

label modbothplaneroutes:
    scene plane9
    "Katrina gets up and you find yourself obediently following behind her."
    "You feel bad for Kendra, but you can't pass up the chance to see Katrina's tits up close."
    scene plane10
    kat "Here we are [y]. Down on your knees."
    y "What?"
    kat "Get down on your knees.  Just like you did back at the office a few days ago.  You want see my tits?  Well, I want to see you on your knees."
    "You do want to see her tits, but strangely even more you feel like you want to make her happy by doing what she says."
    scene plane11
    "You drop to your knees and she hooks her thumb in the front of her dress and slowly lowers it."
    kat "God [y] this is so hot!"
    y "Your breasts are amazing Katrina!"
    kat "Yeah keep looking up at me [y].  Good boy.... now don't think about Kendra anymore.  She's ok in coach.  Just relax and enjoy the flight with me."
    "You find yourself nodding in agreement."
    kat "That's good.  Back in the office, I told you you're allowed to stare at my tattoos from now on.  Now I'm adding my breasts to that deal."
    kat "Feel free to look all you want from now on.  And if you're ever feeling stressed out again about anything, please talk to me.  I'll be more than happy to calm you down again."
    scene plane10
    kat "If we had more time I'd take off my dress entirely, but for now we need to get back to Emily and Gianna."
    scene plane1
    if katdom >= 1:
        "Moments later you are back sitting next to Katrina with her fingers lightly stroking yours."
        "It's strange that Katrina is so easily able to take control of you like that.  That's twice now you've been on your knees in front of her unable to do much of anything other than agree with whatever she wants."
        "You snap out of your thoughts vaguely aware of Emily and Gianna teasing you guys."
    scene plane2
    g "So how are Katrina's boobies [y]?"
    y "Ummm, I plead the fifth!"
    e "We're over international waters [y]!  American amendments don't apply!  Spill it!"
    scene plane1
    y "Ok, they are amazing!"
    scene plane2
    g "I bet mine are better!"
    e "Mine are the perkiest!"
    y "I wouldn't mind judging for you...."
    e "Heh, in your dreams [y]!"
    scene plane1
    "You wonder if Katrina is going to mention to the others that she made you get on your knees.  Thankfully she doesn't"
    y "I should go speak with the stewardess"
    jump week2b
label week2b:
    scene plane2
    g "[y] Please stay here with us.  If you talk to the stewardess and she says no we know you're going to offer to switch seats with Kendra."
    e "If you do that she's going to feel so guilty."
    scene plane3
    kat "It's only a few hours.  You'll get to see her all you like in Hawaii."
    menu:
        "Let the matter drop and enjoy first-class with the girls.":
            jump week2c
        "[Gr]Talk to the stewardess about upgrading Kendra's ticket.":
            jump kendra1stclass
label kendra1stclass:
    scene plane8
    y "Excuse me miss.  One of our friends mistakenly purchased a ticket in coach and I noticed there are several empty seats.  Could we upgrade her ticket so she can join us?"
    st "I wish I could do that for your sir, but you would have had to upgrade her ticket back at Admissions when you arrived at the airport."
    scene plane12
    y "I could pay the difference in price in cash right now.  I took out a big sum for our trip."
    st "I could lose my job.  Please understand sir."
    y "I know, it's just that we're all flying to Hawaii to celebrate the success of my game Caelum Besieged and it's not the same without her here."
    scene plane13
    $ bribestewardess = True
    st "Caelum Besieged is your game?!"
    y "You know it?"
    st "I've been playing it for weeks now!  I play it every chance I get!  During layovers, in hotels before return trips, and even when I have a few days off in a row at my own house!"
    st "I'm completely hooked on it.  I'm just sad I didn't pre-order it and get access to the Ruby Halo Sword."
    scene plane12
    y "Like I could give you an in-game code to unlock it."
    st "You could?  Well, maybe I could go get your friend in coach if you promise to keep it a secret."
    y "Sure, just add [y]1998 to your friends list and I'll send you the code in-game after we land."
    st "Ok hang on a sec, seriously though keep it a secret I'm pulling her out of coach."
    st "I really want that sword, but I don't want to lose my job.  Spending time in Hawaii every few weeks when I get this shift is not something I want to lose!"
    scene plane14
    "A moment later you see Kendra walking up with the stewardess."
    if kendrakiss == True:
        jump kendra1stclassa
    else:
        jump kendra1stclassb
label kendra1stclassa:
    scene plane15
    "She flings herself into your arms and kisses you."
    k "Thanks so much for rescuing me!"
    k "I was so confused why I didn't see any of you on the plane, and I was getting so many weird looks being dressed like this."
    k "Katrina said we were flying first class and we should all dress up, and so I stuck out like a sore thumb back there!"
    scene plane6
    "Kendra takes your seat next to Katrina and you sit on the couch."
    e "Did you really just kiss [y]?"
    k "Yeah I guess I did!"
    k "We kinda kissed in my parents' jacuzzi the other day too."
    g "You did?!  How come you didn't invite us over too?  I want to soak in a jacuzzi!"
    kat "Don't worry, there's one at the beach house.  We can go in it every day if you want."
    g "Awesome!"
    e "Let's try it out tonight!"
    jump kendra1stclassc
label kendra1stclassb:
    scene plane14
    k "Thanks so much for rescuing me!"
    k "I was so confused why I didn't see any of you on the plane, and I was getting so many weird looks being dressed like this."
    k "Katrina said we were flying first class and we should all dress up, and so I stuck out like a sore thumb back there!"
    scene plane6
    "Kendra takes your seat next to Katrina and you sit on the couch."
    jump kendra1stclassc
label kendra1stclassc:
    scene plane7
    g "I can't believe you bribed the stewardess for a first-class ticket with a virtual item!"
    y "I'm just that amazing!"
    k "Well I'm really glad to be here with you guys!"
    e "That sword is really good though!  I'd be bummed too if I didn't have it!"
    scene plane6
    kat "So what is everyone looking forward to the most in Hawaii?"
    g "I'm looking forward to morning jogs on the beach!"
    e "Seeing [y] in a Speedo!"
    scene plane7
    g "You brought a Speedo [y]?  In that case, I change my answer!"
    all "Speedo speedo speedo!"
    y "That's a fuck no!"
    y "As for me I'm just looking forward to spending time with you guys."
    k "That is way too cheesy [y]!"
    e "Yeah c'mon am I suddenly in a {i}try not to cringe{/i} youtube video?"
    y "Ok fine, I want there to be at least one evening where we get a lot of alcohol and all get drunk together!"
    e "That's more like it!  I'm totally down for that!"
    g "You wanna be in a room full of hot drunk girls huh [y]?"
    y "Well you guys twisted my arm to say what I really wanted, so yeah!  A lot of people even back in high school were partying and stuff and I never got invited."
    y "I feel like I missed out and now I want to see what it's like!"
    k "I actually haven't been to any parties like that either."
    kat "Sounds good to me!  I'll look up some fancy Hawaiian liquor or beer when we get there and I'll make it happen."
    scene plane6
    "The girls get to talking while you relax on the couch.  Before you know it you arrive at the Honolulu airport."
    jump airport1
label week2c:
    scene plane1
    "The girls are right and Katrina's hand feels great on yours."
    scene plane2
    e "So what is everyone looking forward to the most?"
    g "I'm looking forward to morning jogs on the beach!"
    kat "Shopping in Hawaiian boutiques!"
    scene plane1
    y "Just spending time with you guys."
    scene plane2
    g "That is way too cheesy [y]!"
    e "Yeah c'mon am I suddenly in a {i}try not to cringe{/i} youtube video?"
    scene plane1
    y "Ok fine, I want there to be at least one evening where we get a lot of alcohol and all get drunk together!"
    scene plane2
    e "That's more like it!  I'm totally down for that!"
    g "You wanna be in a room full of hot drunk girls huh [y]?"
    scene plane1
    y "Well you guys twisted my arm to say what I really wanted, so yeah!  A lot of people even back in high school were partying and stuff and I never got invited."
    y "Now I want to see what it's like!"
    kat "Sounds good to me!  I'll look up some fancy Hawaiian liquor or beer when we get there and I'll make it happen."
    scene plane3
    "You continue talking and enjoying first-class and soon enough you find yourself at the Honolulu airport waiting for Kendra to disembark."
    jump airport2
label milehigh:
    scene plane9
    "Katrina gets up and you find yourself obediently following behind her."
    $ katdom += 1
    "You feel bad for Kendra, but you can't pass up the chance to see Katrina's tits up close."
    scene plane10
    kat "Here we are [y]. Down on your knees."
    y "What?"
    kat "Get down on your knees.  Just like you did back at the office a few days ago.  You want see my tits?  Well, I want to see you on your knees."
    "You do want to see her tits, but strangely even more you feel like you want to make her happy by doing what she says."
    scene plane11
    "You drop to your knees and she hooks her thumb in the front of her dress and slowly lowers it."
    kat "God [y] this is so hot!"
    y "Your breasts are amazing Katrina!"
    kat "Yeah keep looking up at me [y].  Good boy.... now don't think about Kendra anymore.  She's ok in coach.  Just relax and enjoy the flight with me."
    "You find yourself nodding in agreement."
    kat "That's good.  Back in the office, I told you you're allowed to stare at my tattoos from now on.  Now I'm adding my breasts to that deal."
    kat "Feel free to look all you want from now on.  And if you're ever feeling stressed out again about anything, please talk to me.  I'll be more than happy to calm you down again."
    scene plane10
    kat "If we had more time I'd take off my dress entirely, but for now we need to get back to Emily and Gianna."
    scene plane1
    "Moments later you are back sitting next to Katrina with her fingers lightly stroking yours."
    "It's strange that Katrina is so easily able to take control of you like that.  That's twice now you've been on your knees in front of her unable to do much of anything other than agree with whatever she wants."
    "You snap out of your thoughts vaguely aware of Emily and Gianna teasing you guys."
    scene plane2
    g "So how are Katrina's boobies [y]?"
    y "Ummm, I plead the fifth!"
    e "We're over international waters [y]!  American amendments don't apply!  Spill it!"
    scene plane1
    y "Ok, they are amazing!"
    scene plane2
    g "I bet mine are better!"
    e "Mine are the perkiest!"
    y "I wouldn't mind judging for you...."
    e "Heh, in your dreams [y]!"
    scene plane1
    "You wonder if Katrina is going to mention to the others that she made you get on your knees.  Thankfully she doesn't and changes the topic."
    kat "So what is everyone looking forward to the most in Hawaii?"
    scene plane2
    g "I'm looking forward to morning jogs on the beach!"
    e "Seeing [y] in a Speedo!"
    scene plane1
    y "Now who's dreaming Emily?"
    y "As for me I'm just looking forward to spending time with you guys."
    scene plane2
    g "That is way too cheesy [y]!"
    e "Yeah c'mon am I suddenly in a {i}try not to cringe{/i} youtube video?"
    y "Ok fine, I want there to be at least one evening where we get a lot of alcohol and all get drunk together!"
    e "That's more like it!  I'm totally down for that!"
    g "You wanna be in a room full of hot drunk girls huh [y]?"
    scene plane1
    y "Well you guys twisted my arm to say what I really wanted, so yeah!  A lot of people even back in high school were partying and stuff and I never got invited."
    y "Now I want to see what it's like!"
    scene plane4
    kat "Sounds good to me!  I'll look up some fancy Hawaiian liquor or beer when we get there and I'll make it happen."
    scene plane3
    "You continue talking and enjoying first-class and soon enough you find yourself at the Honolulu airport waiting for Kendra to disembark."
    jump airport2
label airport1:
    scene airport4
    "You all disembark and get your bearings."
    k "Hang on a second guys I need to call my parents and let them know I'm here."
    scene airport2
    k "Hello?  Yeah daddy I'm here safe."
    k "First-class was great!  There was a bit of a mixup and I started in coach, but [y] busted me out of there.  Now we're gonna go to baggage claim and then get the rental car."
    k "Yeah I guess you can talk to him."
    k "[y] my dad wants to talk to you for a second."
    scene airport3
    y "Hello?"
    ken "Thanks for taking care of Kendra's ticket problem.  Remember what we talked about.  I'll be calling at least once a day to check on her."
    y "Of course sir, I'll take care of Kendra for you."
    ken "Good to hear!  I won't keep you any longer then.  You kids enjoy your trip."
    scene airport4
    "You hang up and turn back to the group, ready to seek out the baggage claim area."
    jump foyerarrival
label airport2:
    scene airport1
    "As first-class passengers, the four of you disembarked first and have to wait for Kendra to catch up."
    "Soon enough you see her walking up, apparently on the phone."
    scene airport2
    k "Oh I found them, daddy!"
    k "I'm sure that was just a misunderstanding, I'm not mad ok?  And I'm sure it's not [y]'s fault."
    k "Ok, yeah you can talk to him."
    k "[y] my dad wants to talk to you for a sec."
    scene airport3
    y "Hello?"
    ken "[y] What's this about Kendra getting stuck in coach while the rest of you flew first class?"
    y "Ummm, well sir, Katrina bought the tickets and...."
    ken "I don't want to hear excuses.  We talked about making sure this trip goes smoothly.  I'm trusting you with my daughter."
    y "I'm sorry sir, I'll make sure everything goes more smoothly from here on out.  We've all made it to Hawaii safely and we're about to get our bags."
    ken "I'll be calling each day to check on her.  Let's hope this was just a one-time failure."
    scene airport4
    "You hang up and rejoin the others."
    kat "Looks like Kendra's dad was chewing you out on the phone just now."
    y "Yeah we had one of those awkward {i}You better take good care of my daughter{/i} talks the other day."
    kat "Next time let me talk to him, he likes me way better than you.  Now let's go find baggage claim, guys!"
    jump foyerarrival
label foyerarrival:
    scene foyer1
    "A little while later you arrive at the beach house and enter into a large foyer."
    g "This place is amazing!"
    kat "I hope you all like it.  I looked through hundreds of listings to find this place."
    kat "[y] you get the master bedroom of course.  Kendra and I will share another bedroom and Emily and Gianna will share one as well."
    kat "Let's take a few minutes to wash off the dust of the trip and get acclimated and then meet by the pool in say, an hour?"
    k "Sounds good!"
    y "Ok, see you all outside in an hour!"
    scene mb1
    "This bedroom is great!"
    "The fire in the electric fireplace looks nice and probably will look even better at night."
    scene mb2
    "It's even got a balcony overlooking the pool."
    "You decide the balcony is probably the place you'll set up a laptop to work on the game later.  Glancing down at your friends in bikinis seems like a good way to get through all the boring coding."
    scene mbath1
    "In the master bathroom, there is a tub with rose petals floating on the surface."
    "You wonder if a maid comes and puts them in daily or if it's just for new arrivals."
    scene mbath2
    "The shower looks nice and spacious as well."
    "You think about whether to take a bath or a shower and decide on the bath."
    scene mbath3
    "After all if someone took the trouble to set this up you might as well enjoy it!"
    "Just as you finish putting on your swim trunks after your bath there is a knock at the door and Katrina enters in a little robe."
    scene mb3
    kat "Hey [y]!  I just wanted to make sure you're settling in ok."
    y "Oh yeah Katrina, everything is great.  You've found us a really nice place!"
    $ katrina = 2
    kat "I'm so glad you like it!"
    kat "I've guess you've seen the pool if you've looked out your window, but also be sure to check out the game room and the area in the yard with the jacuzzi and fire pit."
    scene mb4
    y "I'll do that."
    kat "Maybe the kitchen too if you want a snack before we go swimming."
    kat "Anyway, I am going to borrow your shower really quick while Kendra is using the one we share."
    "You notice Katrina's robe is coming open and decide to try to keep her talking."
    scene mb5
    y "Ok Katrina.  By the way, there's a bathtub with freaking rose petals in there!"
    kat "Ha, I thought you'd get a kick out of that!  Did you have a nice romantic bath with yourself just now?"
    y "Yeah something like that!  Also, I was wondering if we are still enjoying ourselves after a week would it be possible to extend our stay?"
    kat "We could definitely extend our stay in Hawaii, but if you mean this house specifically I'll have to look into it."
    kat "It might be fun to check out Maui, maybe at a luxury hotel or something."
    "You decided you've pressed your luck enough with the robe."
    y "Well I'm off to check out the rest of the house.  See you at the pool in a bit."
    jump exploring
label exploring:
    scene foyer2
    "You head back to the foyer and think about where to go next."
    menu:
        "Check out the game room." if emily == 1:
            jump gameroom1
        "Visit the jacuzzi/fire pit area." if kendra == 1:
            jump firepit1
        "Get a snack in the kitchen." if gianna == 1:
            jump kitchen1
label gameroom1:
    $ emily = 2
    scene emilygr1
    "You find the stairs leading down to the game room and discover Emily is already there."
    e "Oh hey [y]!  I finished getting ready to go swimming so I was just setting up my computer back there in the corner to stream later."
    scene emilygr2
    e "This room is pretty nice huh?"
    y "Yeah looks like we might be spending a lot of time in here playing pool or hanging out on the couches."
    e "Let's check out the bar back there!"
    scene emilygr3
    y "This is nice too, but it looks like we'll have to stock our own liquor."
    e "This'll be a great room to have that drinking party you wanted.  Though maybe we'll also spill out into the pool area or to the jacuzzi."
    e "I guess that'll be up to you since that night will be all about giving you the party experience you want!"
    y "Yeah I'm really looking forward to that!"
    e "Hey Katrina told me there's even a poker room off in one of the side rooms around here.  Wanna find it?"
    y "Sure!"
    scene emilygr4
    "You explore around a bit and come to a hallway with gaudy green wallpaper."
    e "Here it is!"
    e "Wow that wallpaper though!"
    e "We should add a poker night to our list of activities!  Do you think the other girls will want to play?"
    y "I hope so!  You and I would clean them out!"
    scene emilygr5
    "Emily jumps up on the table giggling."
    e "Oh [y]!  I can't believe I lost the last hand after betting my body!"
    e "Take me I'm yours!"
    y "You should've known better than to fold after going all-in.  I was bluffing the entire time!"
    scene emilygr6
    e "Haha, you crack me up [y]!  We're gonna have a great time this week."
    e "I'm gonna finish setting up my computer.  See you at the pool in a few!"
    if katrina + gianna + emily + kendra == 8:
        jump firstdaypool
    if katrina + gianna + emily + kendra <=8:
        jump exploring
label firepit1:
    $ kendra = 2
    scene kendrafirepit1
    "You find Kendra lounging by the firepit."
    k "Hey [y]!  I was hoping we could have a fire out here one night."
    k "I saw some tiki torches too over by the shed.  We could have our own little luau!"
    y "That sounds great!"
    y "No toxic bikini today?"
    k "I packed it but when I got here I found it had been replaced by this more modest bikini.  I'm sure it was my dad's doing.  He hates that bikini!"
    y "Well at least I got to see it back home."
    k "Let me show you the jacuzzi!  It's way nicer than my parents'!"
    scene kendrafirepit2
    "She jumps up and you follow!"
    k "Check it out!  All five of us could get in here at the same time!  And it's got lights if we come at night we can switch on!"
    y "Looks super nice!  Let's come back here at night!"
    k "Yeah, I'd like that.  Maybe after everyone else is asleep."
    y "Oh I meant with everyone, but yeah just us would be great too."
    k "Geez, ok I'm a little embarrassed.  I took it the wrong way, sorry!"
    scene kendrafirepit6
    "Kendra grabs your hand and hops off into the yard."
    k "I was thinking maybe we could play some ultimate frisbee out here... with everyone."
    y "We'll have lots of time to do so many fun things this week."
    scene kendrafirepit3
    "You decide to take a chance and put your arm around Kendra while pointing out some of the areas in the yard."
    "She leans her head back into your shoulder."
    k "I'm so glad we came on this trip [y].  I feel like it's the perfect way to enter a new chapter in our lives."
    k "Hey [y].... do you think this is romantic?"
    y "Yes, I do think this is romantic Kendra."
    k "Me too [y]."
    scene kendrafirepit4
    "You lean in and kiss her."
    scene kendrafirepit5
    y "Yeah definitely romantic."
    k "You're a great kisser [y]!"
    scene kendrafirepit7
    k "I forgot my towel in my room.  I'm gonna go get it while I catch my breath after that kiss.  See you at the pool!"
    y "Ok, see you there."
    if katrina + gianna + emily + kendra == 8:
        jump firstdaypool
    if katrina + gianna + emily + kendra <=8:
        jump exploring
label kitchen1:
    scene giannakitchen1
    "You decide to grab a snack in the kitchen."
    $ gianna = 2
    g "Hey [y]!  This kitchen is awesome!  Get in here!"
    y "Wow, I get to see the skull bikini in person!"
    scene giannakitchen2
    g "Oh yeah baby!  Feast your eyes on how badass I am!"
    y "I gotta say, it does look amazing!  I definitely would be wary of having a water gun fight with you!"
    g "Haha [y]"
    y "Wow this place has both a table and a kitchen island you can sit around."
    scene giannakitchen3
    g "Yeah and you can see the pool out the window.  Check out this view!"
    y "Yeah the view is great!"
    scene giannakitchen4
    "Gianna doesn't change her pose as you move up behind her."
    g "So did you like my sexy selfies the other day?"
    y "A lot actually!"
    g "Do you want to take one right now?"
    y "You'll let me?"
    g "Take out your phone [y].  You don't want to let this great view go to waste."
    scene giannakitchen5
    "You take out your phone and take a picture of Gianna's ass."
    g "So how many girls have you collected sexy pics of?"
    scene giannakitchen6
    y "Just you actually."
    g "Oh really?  So you barely have any pics at all?"
    y "It's a tragedy really!"
    g "It sure is!  Tell you what, let's get your collection started right!  You name any pose and I'll do it!"
    g "Only rule is my bikini stays on."
    menu:
        "Get on all fours.":
            jump fours
        "On your back touching yourself.":
            jump back
        "On your knees looking up at me.":
            jump knees
        "Show me your feet.":
            jump feet
        "[Gr]MOD: View all poses":
            jump modallposes
label fours:
    scene giannapose1
    "Gianna gets up on the kitchen island into position."
    g "Like this [y]?"
    y "Yeah that's perfect!"
    "You snap a couple pics with your phone and Gianna moans a little."
    jump kitchen1a
label back:
    scene giannapose2
    "Gianna gets up on the kitchen island into position."
    g "Like this [y]?"
    y "Yeah that's perfect!"
    "You snap a couple pics with your phone and Gianna moans a little."
    "She starts to get really into it, pressing down hard enough that you can see the edges of her pussy lips start to spread out from under her bikini."
    jump kitchen1a
label knees:
    if knees == True:
        jump kneesa
    else:
        jump kneesb
label kneesa:
    scene giannapose3
    g "So you want another pic of me on my knees huh?"
    g "You must have really liked the one the other day."
    jump kneesc
label kneesb:
    scene giannapose3
    g "Ok [y].  Looks like you have me right where you want me!"
    jump kneesc
label kneesc:
    scene giannapose3
    "You take a couple pics."
    jump kitchen1a
label feet:
    scene giannapose4
    g "Oh so you're a feet guy!"
    "Gianna gets up on the kitchen island into position."
    g "Like this [y]?"
    y "Yeah that's perfect!"
    "You snap a couple pics with your phone and Gianna moans a little."
    jump kitchen1a
label modallposes:
    scene giannapose1
    "Gianna gets up on the kitchen island into position."
    g "Like this [y]?"
    y "Yeah that's perfect!"
    "You snap a couple pics with your phone and Gianna moans a little."

    scene giannapose2
    "Gianna gets up on the kitchen island into position."
    g "Like this [y]?"
    y "Yeah that's perfect!"
    "You snap a couple pics with your phone and Gianna moans a little."
    "She starts to get really into it, pressing down hard enough that you can see the edges of her pussy lips start to spread out from under her bikini."

    scene giannapose4
    g "Oh so you're a feet guy!"
    "Gianna gets up on the kitchen island into position."
    g "Like this [y]?"
    y "Yeah that's perfect!"
    "You snap a couple pics with your phone and Gianna moans a little."

    if knees == True:
        scene giannapose3
        g "So you want another pic of me on my knees huh?"
        g "You must have really liked the one the other day."
        scene giannapose3
        "You take a couple pics."
    else:
        scene giannapose3
        g "Ok [y].  Looks like you have me right where you want me!"
        scene giannapose3
        "You take a couple pics."

    jump kitchen1a
label kitchen1a:
    scene giannapose5
    g "Wow that was really hot!  I ummm, need to take care of something in my room.  I'll meet you out at the pool ok?"
    "Gianna rushes out of the room.  You grab an apple and leave as well."
    if katrina + gianna + emily + kendra == 8:
        jump firstdaypool
    if katrina + gianna + emily + kendra <=8:
        jump exploring


label firstdaypool:
    scene poolday1
    "It's been about an hour, so you head to the pool to meet the girls."
    "You open the door and can tell the girls have just arrived as you hear Kendra talking."
    k "Don't forget to put on sunscreen girls, we don't want to ruin this dream vacation by turning into painful peeling tomatoes!"
    g "Eww, gross Kendra!"
    e "Hey Kendra, could you get my back please?"
    kat "There should be a massage table in the pool storage along with some pool toys.  Let me get it and Kendra can do all our backs."
    scene poolday2
    "A moment later Emily is on the table with Kendra applying the sunscreen."
    e "Wow, Kendra, your hands feel good and on this table, it's just like a massage!"
    g "I want a massage!"
    kat "Me too!"
    "Kendra laughs."
    k "Ok line up!"
    menu:
        "Walk out and ask Kendra to put sunscreen on you too":
            jump firstdaypoola
        "Keep listening to the girls' conversation silently":
            jump firstdaypoolb
label firstdaypoola:
    y "Hi ladies!"
    y "Kendra, if you are putting lotion on everyone can you get me too?"
    k "Sure, [y]"
    scene poolday5
    "The other girls enter the pool and you take Emily's spot."
    y "Thanks, Kendra!  The girls are right, your hands do feel good!  And I appreciate you taking care of all of us."
    "Kendra laughs happily."
    k "I don't want to ruin our vacation with a bad sunburn!"
    "You are feeling brave after the moment you shared earlier out in the yard."
    y "Did anyone take care of your back?"
    k "No..."
    y "Ok then it's your turn to lie down and I will return the favor!"
    scene poolday6
    "Kendra lays down and you rub your hands on her exposed skin."
    k "Make sure you get under the straps."
    "You blush as you push the straps of her bathing suit down her shoulders slightly so you can cover the area with sunscreen."
    k "Thanks, [y]!"
    scene poolday7
    "You and Kendra walk over to the pool with the other girls who have pulled some floats out of the pool shed."
    jump firstdaypoolc

label firstdaypoolb:
    scene poolday2
    "You continue to watch Kendra rub suntan lotion on the girls."
    "You hear Emily moan under Kendra's touch, making it pretty obvious to everyone how much she's enjoying it."
    scene poolday3
    "Katrina makes Kendra do both her front and her back."
    kat "Make sure you get every inch of me.  I'm hoping to get a really even tan!"
    scene poolday4
    g "Yay!  It's my turn now!"
    "You continue to watch as Kendra works her way all the way down Gianna's body."
    scene poolday7
    "With the sunscreen successfully applied the girls grabbed some floats and entered the pool."
    "You decide you are ready to join them."
    jump firstdaypoolc

label firstdaypoolc:
    scene poolday7
    y "Everyone having fun?"
    all "Yes!"
    k "This really is a dream come true!"
    g "It is so relaxing!"
    e "The water is the perfect temperature."
    scene poolday8
    "After a bit of relaxing, Gianna goes back to the pool shed to search around."
    g "Hey I found a beach ball guys!  Let's play!"
    scene poolday9
    "She kicks you the ball and you splash the girls as you lunge for it."
    "Emily, Katrina, and Kendra give a small scream as the water touches them.  Emily quickly hops up on the side of the pool."
    kat "Cut that out!"
    y "Make me!"
    scene poolday10
    "You laugh as you toss the ball back to Gianna who jumps for it, splashing the others again."
    kat "You're gonna regret that!"
    "Kendra and Katrina attempt to paddle towards Gianna to try to get the ball away, but before they can Gianna tosses the ball back you."
    scene poolday11
    "Katrina attempts to turn for the ball, but you quickly grab her float."
    y "DON'T YOU KNOW THAT ONLY PURE MAIDENS CAN RIDE UNICORNS?"
    scene poolday12
    kat "[y] NOOOOOOOO!"
    scene poolday13
    "Katrina bobs to the surface."
    "She swims after you for a bit trying to catch you and exact revenge."
    scene poolday14
    "After awhile you all agree to end the game and move to sit on the chairs to dry off."
    kat "It's taking longer than I thought it would for my suit to dry off."
    g "I know, I was thinking the same thing!"
    e "Well, it is pretty private here.  What if we got new suits, ones that leave a little less to the imagination?  The smaller the suit the quicker it will dry!"
    k "Emily!"
    e "What? We don't want to waste any time here waiting around for things to dry off."
    scene poolday15
    y "I think it is a great idea!"
    kat "See, [y] thinks its a great idea!  That must mean he is going to get a new suit too. A Speedo would dry fast, what do you think, [y]?"
    y "Not a Speedo!"
    scene poolday14
    g "But a yes to new swimsuits?  Tomorrow we will have to go shopping!  But how do we want to spend our first night in Hawaii?"
    k "I don't know about the rest of you, but I am starting to feel the time zone difference."
    kat "I think for tonight we should just stay in and keep things quiet and try to get over the jet lag."
    "Everyone agrees that makes sense."
    e "Ok, quick showers, and then let's meet in the kitchen to grab some snacks.  Then it's pajama party time in the TV room!"
    kat "Gianna, come with me, we'll borrow [y]'s shower while he uses the tub."
    g "Umm ok, I assume we'll be staying in our bikinis then?"
    kat "Well I am, I don't know about you!"
    jump sharedshower
label sharedshower:
    scene sharedshower4
    "Katrina and Gianna head up to your room with you."
    g "Wow is that a freaking chandelier hanging over a tub of rose petals?"
    y "I know right?  It's crazy!"
    g "It's like {i}Lifestyles of the Rich and the Famous{/i} up in here!  How do I get started making a video game?"
    y "The hardest part is actually getting over the hurdle of taking your idea and writing that very first bit of code, rather than just keeping it all in your head just thinking of doing it."
    scene sharedshower5
    kat "So [y], do you think you can keep your eyes off us while we shower?  Or is this going to be too distracting for you?"
    y "I'm not sure, guess we'll find out."
    kat "Well what if we do something sexier now than anything we might do in the shower.  Maybe if you've already seen the best of what we could do you'll be able to focus on your bath."
    kat "Hey Gianna, do you have any idea of what we could do?"
    "Katrina's voice sounds sultry, but there's more to it than that.  It's kind of a mix between sultry and commanding and something else you can't quite put your finger on."
    g "[y] likes when I take sexy pictures for him."
    "You're a little surprised Gianna just came out and told her like that."
    kat "Oh does he now?  Have you taken a lot for him?"
    g "No, just a few this week, but it was really fun."
    kat "That's a great idea, Gianna let's do that."
    scene sharedshower6
    "Katrina moves around behind Gianna and pulls her backward into a sexy pose."
    "Gianna and closes her eyes and just lets it happen."
    "You pull out your phone and snap a pic while Katrina squeezes Gianna's left breast."
    scene sharedshower7
    "Gianna sinks to the ground and cups her breasts.  Katrina begins lightly caressing her neck."
    "You take another pic and expect Gianna do get up, but she doesn't.  Katrina continues to caress Gianna's neck for way longer than you expected Gianna to let her."
    scene sharedshower8
    "Eventually Katrina stops and steps to the side."
    kat "Who knew taking a couple sexy pics could be that fun?"
    kat "We should stop now though while Gianna still remembers her own name.  She seems like she was so into it she's almost entered a daze."
    scene mbath3
    "You enter the tub and relax for a moment."
    "Your thoughts turn for a moment to the rose petals.  Is it ok to drain the water or will it cause a clog?"
    "You wonder if people who have been rich all their lives think of things like that.  Probably they just leave the water the way it is and let the maid figure it out."
    scene sharedshower1
    "Despite agreeing to keep your eyes to yourself in exchange for the sexy pics you can't help but listen to the girls talk."
    "Katrina seems to have Gianna backed up to the wall."
    kat "I really like your bikini, Gianna.  What made you pick it out?"
    g "I originally bought it for an indoor Halloween pool party the volleyball team had in our senior year of high school.  I wore it on this trip though because [y] told me he thought skulls were badass."
    kat "You do look badass!  It makes me want to mess with you!"
    g "Shouldn't the skulls make you back down if you think I look badass?"
    kat "No way!  If you look like you might be a challenge I get way more interested!"
    scene sharedshower2
    kat "I like your jewelry too!"
    g "Thanks!"
    kat "Do you think I'd look good with a thumb ring?"
    g "Yes, you're very pretty and it would look great with your tattoos."
    kat "Maybe I'll get one then."
    scene sharedshower3
    kat "I'd have to find one with some kind of significant meaning though."
    kat "I'd probably take it off in the shower too, so it doesn't rust."
    g "They don't rust, but they are a little duller than when I got them."
    scene mbath3
    "The care and maintenance of jewelry doesn't interest you, so you go back to relaxing."
    "After a while the girls get out and head back to find pajamas.  You put your own on and head to the kitchen."
    jump nightkitchen
label nightkitchen:
    scene nightkitchen1
    "Everyone arrives except for Kendra and you start making toast."
    e "C'mon, did no one put any stat points into cooking?"
    kat "Nope, all of mine went to intelligence and charisma."
    y "Those are attributes, you'd have spent the skill points separately."
    kat "Are you going to make me reveal my character sheet?"
    g "That sounds dirty!"
    "You hear the sound of heels clicking on the hardwood floor."
    scene nightkitchen2
    k "Oh my gosh what is everyone wearing?!"
    scene nightkitchen3
    all "What are we wearing?!  What are you wearing?!"
    scene nightkitchen2
    k "Well I assumed we were all going to dress in sexy pajamas or lingerie and tease [y]!"
    k "Emily, not even you?"
    scene nightkitchen3
    e "Hey why are you singling me out?"
    scene nightkitchen5
    k "I'm so embarrassed!  First I was wearing a clubbing outfit when I arrived at my seat in coach, now I'm wearing sexy lingerie in a room full of people wearing comfy PJs."
    scene nightkitchen6
    e "Awww, you look great Kendra, calm down ok?"
    g "We're going out tomorrow to buy skimpier bikinis, how about we buy some sexy lingerie too?"
    kat "Yeah then you won't feel out of place next time."
    e "I kinda thought we'd at least do that for that drinking party [y] wants anyway."
    scene nightkitchen7
    k "God, I'm even wearing heels!"
    e "The heels look good Kendra."
    g "Yeah ummm, my feet are really cold so I'm actually jealous."
    k "I'm gonna go change."
    scene nightkitchen8
    y "You don't have to do that Kendra.  If you came here thinking everyone was going to tease me I wouldn't mind if it was just you."
    k "You want me to watch the movie like this?"
    y "Yes, you look great!  Don't feel embarrassed!  This trip is about having fun!  We've never all gone on a trip before, let's make the most of it!"
    k "Ok, but you have to carry me like a princess to the TV room!"
    y "Deal!"
    k "And the heels come off when I get there."
    y "Ok, that's fair."
    jump movie
label movie:
    scene nightmovie1
    y "Here we are Princess Kendra.  Let's take the big side of this Tetris L-block couch."
    k "Ha, you always cheer me up with your silly game references!"
    e "I claim this swinging chair!"
    kat "Guess that leaves me and you, Gianna."
    g "We get the short side of the Tetris L-block?  Hey, even I've played Tetris!  Everybody has!"
    scene nightmovie2
    "The one thing every vacation house has had in common, from all the cheap ones you stayed at with your parents over the years right up to this luxurious one, is that the movies they provide in the TV room are always random and old."
    "The group agrees on {i}Batman Begins{/i}, just based on the fact that a 2005 release makes it the newest movie in the collection."
    scene nightmovie4
    "No one really watches it though.  You're all tired and winding down after a long day of travel and fun."
    "Kendra puts her head in your lap and doesn't protest as you gently caress her hair and face."
    "She looks so beautiful and you think back to earlier when she misunderstood about hanging out in the jacuzzi."
    "She had basically agreed to do it just the two of you.  That does sound really nice."
    scene nightmovie3
    "You glance over and see Katrina cuddled up and occasionally whispering to Gianna."
    "They were never that close in the past, so you're glad this trip seems to be bringing them together."
    scene nightmovie5
    "After a while you notice the movie is playing for the second time.  It must have reached the end and restarted."
    "Kendra had fallen asleep so you nudge her awake and let her know you are heading back to your room."
    if bribestewardess == True:
        jump endofday1a
    else:
        jump endofday1b
label endofday1a:
    scene nightmovie6
    "As you sit down on your bed you realize you never sent the pre-order promo code to the stewardess from the plane."
    y "Crap!  I don't want her hunting me down while I'm stuck on Oahu!"
    "You log into the game from your phone and find a friend request from B787 and a message."
    st "It was nice meeting you today on the flight!  Hope you don't forget your promise!  I'm here on leave for a few days, so maybe I'll be assigned to your return flight."
    y "You accept her friend request and send her the code with a message apologizing for taking several hours."
    "You then drift off to sleep thinking of how this was the perfect first day in Hawaii and how happy you are you've saved your relationship with your friends."
    jump morningjog1
label endofday1b:
    scene nightmovie6
    "You sit on your bed and send a text to your parents letting them know you arrived in Hawaii safely and are having a great time."
    "They are probably getting up for the day since they are six hours ahead of you."
    "You then drift off to sleep thinking of how this was the perfect first day in Hawaii and how happy you are you've saved your relationship with your friends."
    jump morningjog1
label morningjog1:
    scene day2morning1
    "You wake up early the next morning and head out to the balcony for coffee and to get a little work done on Caelum Besieged."
    "Jet lag works in funny ways.  You still feel tired, but at the same time you feel like you've slept in until noon."
    scene day2morning2
    "After a little while Gianna comes out to the pool and does some stretches followed by a few cartwheels."
    "You have a dirty thought about how limber she is and how great she must be in bed."
    scene day2morning3
    y "Hey Gianna!  What're you doing down there?"
    g "Oh hey [y]!  Is that your room up there?  You get a balcony too?"
    y "Yep, I need to be able to overlook the plebs!"
    g "Ha ha, very funny!  Why don't you get down here and we'll take a jog together?  I was just warming up."
    y "Ok, sure, give me a minute to get dressed."
    scene morningjog1
    "The two of you take a five-minute jog down to the beach."
    g "Wow this is nice!  We even get a little private section of beach to ourselves."
    scene morningjog2
    "After a bit you reach the end of the cove."
    y "It's kind of cool how the natural rock forms coves.  I guess this is where our section ends and the section open to the public begins."
    g "Yeah it looks like to get around you'd have to either walk up and around the rocks or else swim around then in the ocean."
    g "I'll have to wear my swimsuit tomorrow and we'll swim around.  I'd prefer jogging further in one direction than doing laps back and forth in our own section."
    y "Sounds like a plan."
    scene morningjog3
    "You head back the way you came and find Kendra and Katrina set up for the day."
    g "Hey guys, how long have you been here."
    k "Not too long, less than an hour I guess."
    scene morningjog4
    kat "There's a boardwalk within walking distance with a bunch of little shops and boutiques.  We thought we'd find you down here and we could all go."
    y "Where's Emily?"
    k "Streaming of course.  She was going on about how great her numbers have been lately and how it's already evening in Europe and blah blah blah."
    kat "Yeah long story short, we couldn't convince her to come."
    g "Well I'm up for doing some shopping.  Should we go back and get changed?"
    kat "No need.  We'll just pick up beach dresses and something for [y] at the first boutique."
    jump shopping
label shopping:
    scene shopping1
    "You find the boardwalk and check out a few stores through the windows before finding one that the girls think looks promising."
    g "Oh look at these dresses."
    kat "C'mon [y]!  I'll help you pick out something in the men's section."
    scene shopping2
    kat "Let's see, some nice looking beach shirts here.  How would you feel about wearing a cool necklace for me?"
    y "I've never worn one before, do you think I could pull it off?"
    kat "Yeah definitely!  Let's go to the dressing rooms and try on an outfit."
    scene shopping3
    kat "How's it going in there [y]?  Make sure to leave the shirt unbuttoned.  That's the style you're gonna want at the beach."
    y "Ok, and I do think the necklace looks pretty good.  The sunglasses you chose are cool too!"
    kat "I can't wait to see, come out and pose for me!"
    scene shopping4
    "You come out and lean on the doorframe the way you've seen models do in magazines."
    kat "Wow [y]!  I think my heart just skipped a beat!"
    kat "I have great taste in outfits!"
    y "Yeah it looks like I won't need a Personal Shopper to help me when we get back.  That is if you're willing to help me find some outfits."
    kat "Girls!  Come look how hot I made [y]!"
    scene shopping5
    g "You do look hot [y]!"
    "You try out another pose you've seen in magazines."
    k "I like your shades!  Just don't wear them 24/7 like Emily."
    y "I thought hers were prescription."
    k "I don't think so!"
    g "Katrina do you like these beach dresses we found?  They have the same dress with four different patterns.  Go pick one out and we'll match."
    scene shopping6
    "The girls go to get a dress for Katrina and one to bring back for Emily and you look into the mirror."
    y "I do look a lot nicer than I did just a few weeks ago."
    y "Contact lenses, new hair, a new outfit.  Why didn't I do this sooner?  I think my stomach looks flatter too just from that day at the gym with Gianna."
    y "Well that and I spent so much time on the game I frequently forgot to eat!"
    scene shopping7
    k "We found some skimpy bikinis to try on [y]!"
    g "Yeah can we model them for you?"
    y "Like any guy would say no to that!"
    scene shopping8
    "Katrina is the first one out."
    kat "What do you think?"
    y "I love it!  That metallic gloss makes it so shiny!"
    kat "If you got really close maybe you could see your reflection in it."
    "You find yourself taking a step forward."
    scene shopping9
    "Katrina quickly spins away from you though."
    kat "And what about the back?"
    y "Your ass looks great!"
    kat "Oh good, my orange bikini was actually pretty skimpy too, so the thong in the back of this one is what sets it apart."
    scene shopping10
    "Gianna is out next and Katrina squeals in pleasure when she sees her and grabs her from behind."
    kat "Look how great Gianna looks!"
    kat "The white bikini really looks great in contrast to her dark complexion don't you think?"
    y "Yeah she looks really nice."
    "Katrina leans in to whisper to Gianna."
    kat "I wish I wasn't sharing a room with Kendra.  We could have so much fun at night making sexy pics to send to [y]."
    scene shopping11
    "Gianna closes her eyes and you see Katrina's hand move towards the knot tying on Gianna's thong bikini bottoms."
    kat "Would you like that Gianna?"
    g "yes...."
    scene shopping12
    "Katrina slowly pulls on the string until the knot comes loose and Gianna's bikini begins to fall."
    "You think Gianna will snap out of it since you're in a store, but she let's it happen."
    "You wonder if Katrina will manage to get her bikini bottoms all the way off before she reacts."
    k "Guys I'm coming out!"
    scene shopping13
    "Kendra's reappearance snaps Gianna out of it and she re-ties her bikini looking embarrassed."
    k "What do you guys think?  Leopard print is sexy right?"
    y "Yeah very sexy Kendra!"
    kat "Rrrraaawwwwrrr!"
    scene shopping14
    "Kendra poses like she's blowing you a kiss."
    y "You'll steal my heart looking like that!"
    k "I think I stole your heart a long time ago [y]."
    "You notice Katrina giving Kendra an odd look out of the corner of your eye.  Like maybe she's jealous or envious, it's hard to say exactly."
    scene shopping15
    k "I've never worn a slingshot bikini before!"
    g "You're brave to put that on!  I kind of wish I found it first!"
    k "This wasn't even the skimpiest one!  There's a pink one even smaller!"
    kat "You know what would be funny?  What if we got it for Emily?"
    k "Do you think she'd wear it?"
    kat "She agreed to get a skimpy bikini but didn't come with us today.  It would serve her right for choosing her Twitch fans over us!"
    k "Yeah it'll be so funny seeing her face when she sees it.  Let me go get it!"
    scene shopping16
    "Kendra is back a moment later and to your surprise Katrina manages to convince Kendra to try it on for us."
    k "Guys we have a problem!  This thing is kinda see-through!  I can't come out in this!  Sorry [y]!"
    scene shopping17
    "Just then Kendra's cell rings from her bag and Katrina grabs it and answers on speakerphone."
    kat "Hi Kenneth!"
    ken "Katrina?  Is that you?  Hi, is my daughter there?"
    kat "Yeah, and before you ask, no [y] is not here and no Kenneth, you can't talk to him."
    ken "What's with the {i}Kenneth{/i}?  You always called me Mister Ken."
    kat "Well this may come as a shock, but guess what!  I grew up!  Oh, and so did your daughter."
    ken "You'll always be kids in my eyes."
    kat "I don't know, I think I'm pretty mature for my age.  If fact maybe you should be calling me {i}Miss Katrina{/i}."
    ken "You think so?"
    kat "Kendra will be back in a second.  We're getting a gag gift ready for Emily."
    kat "You see, she didn't come shopping with us today, so as revenge we're buying her the tiniest sluttiest slingshot you can imagine!"
    kat "I mean, I can't imagine any girl actually ever putting it on, but it's going to be hilarious when she sees it!"
    scene shopping18
    "Katrina's rapidly escalating conversation with Kendra's dad is enough to get her to open the door."
    k "Katrina!  Give me the phone!"
    "Katrina leans overs to Kendra and whispers."
    kat "This is the perfect chance to get back at your dad for confiscating your toxic bikini."
    kat "Let [y] feel you up while you talk."
    scene shopping19
    "To your surprise, Kendra turns to you looking like she's ready to pounce!"
    "You decide to play along as well."
    k "Hi daddy!"
    ken "Hi sweetie, how're things going?"
    scene shopping20
    k "Great daddy!  Listen I wanted to thank you for taking my one bikini out of my suitcase and replacing it with a more modest one."
    ken "You're welcome honey!  You know I'm always looking out for my little girl."
    scene shopping23
    k "Yeah, after thinking about it more it would have been really inappropriate to wear around [y] and random beachgoers."
    k "And don't worry about what Katrina said about playing that prank on Emily.  I'm sure she'll never wear the slingshot.  It's just too small and see-through."
    ken "It's see-through too?!"
    scene shopping21
    k "And it's made of such tiny low cut strings she'd have to shave as well."
    ken "You mean her legs?"
    k "Yeah of course daddy, she'd have to shave just her legs."
    scene shopping22
    ken "Sweetie, you probably shouldn't get it for her, even as a joke."
    k "Ok daddy, you're probably right!  I doubt if these straps would stay in place.  Apparently, they fall to the sides really easily."
    k "Thanks for setting me straight!  I gotta go now, tell mom I say hi!"
    ken "Bye sweetie, I love y...."
    "Katrina hangs up."
    scene shopping24
    k "Wow, I need to catch my breath after that.  Sorry, that got a little out of hand [y]!  I bet you kinda enjoyed it though!"
    k "We're going to go to a few other shops and try to find some fun lingerie next.  Why don't you head back for now?"
    kat "Yeah if you stick around we're going to probably get kicked out!"
    y "Yeah you guys are right!  I'll leave my credit card with you but don't go too crazy.  I'll head back and check in with Emily."
    jump aftershopping
label aftershopping:
    scene backathouse1
    "You walk back to the house and check the game room first."
    y "Hey Emily!  I thought I'd find you here at your computer!"
    e "Holy crap [y]!  When did you get so hot?!"
    scene backathouse2
    e "Don't worry chat, you'll always be my first love!"
    y "The girls picked this outfit for me.  They're still out shopping.  How's the stream going?"
    e "It's going great!  Wanna do a giveaway?  Do you have any codes for us today?  How about another 100?"
    y "Ummm no, giving away 100 was just a one-time thing.  I can give you three today."
    e "Ok, hear that chat?  We'll set it up so you can redeem 1,000 channel points per entry into a raffle!"
    y "So will you join us back at the beach in a little while?"
    scene backathouse1
    e "Yeah yeah, pretty soon maybe."
    y "Ok, well I'm going to go play some pool on the other side of the room.  Let me know if it's too disruptive."
    scene backathouse3
    e "Ok [y]!  Button up that shirt though!  We wouldn't want chat to see something they shouldn't."
    scene backathouse4
    "You practice some pool while listening to Emily interact with chat and waiting for the others to get home."
    "You're feeling pretty glad your game and giveaways are helping her out so much."
    scene backathouse5
    "After about an hour the other three girls return."
    k "Hey [y]!  We're here to drag you and Emily to the beach!"
    y "Did you get what you were looking for?"
    g "You mean the lingerie?  Yeah, we got it and also some hula outfits!"
    kat "I got a lead on some good Hawaiian liquor too!  It's supposed to contain a mystical Hawaiian Aphrodisiac that is said to be impossible to resist!"
    kat "I need to visit the local Witch Doctor later to get it."
    k "She's kidding!  It's sold at a local shop, but it was a little too far to walk."
    g "So about the beach, let's go!"
    y "Actually Katrina, could we stay and play a game of pool and then join them later?  There's something I want to talk to you about."
    scene backathouse6
    k "Emily!  Time to log off!  You're coming to the beach!"
    g "Do it or we'll jump in front of your webcam and earn you a 30-day ban!"
    e "Ok, geez guys I'm coming!"
    e "Sorry chat!  I'll try to be back on tonight or tomorrow morning!  Gotta go, gotta go!"
    jump chapter1final
label chapter1final:
    scene backathouse8
    kat "So what did you want to talk about [y]?  Though I think I can guess."
    y "It's about the effect you seem to be having on people.  On me back at the office, on Gianna, even on Kendra."
    scene backathouse7
    y "I've never seen Kendra rebel against her father like that and Gianna was ready to let you take off her bikini in the store."
    kat "Congrats on Gianna by the way.  You're almost ready to score with her, but you're a little behind me."
    y "What do you mean?"
    scene backathouse8
    kat "I mean you could probably get her to sleep with you in another couple of days, but I could have her tonight if I wanted."
    scene backathouse10
    y "You want to sleep with Gianna?"
    kat "Not for the reason you think.  You remember when Emily made us watch {i}Rosario Vampire{/i}?"
    y "Yeah that's the anime where Tsukune Aono kinda builds a harem at the school for monsters?"
    scene backathouse12
    kat "Yeah, I bet you feel a little bit like the hero of an anime-style harem right now with just you and four beautiful girls."
    y "I guess so, a little."
    kat "And do you remember back at Kendra's house when she confessed we were thinking of moving on with our lives the night at the cafe?"
    y "Yeah, I guess she told you about that conversation."
    kat "She did, and I have a confession too.  That night at the cafe I wasn't planning on just moving on from you, I was planning on moving on from everyone."
    y "You were?"
    scene backathouse9
    kat "Remember how I told everyone I was almost done my Masters degree in Psychology after only 3 years?  Well, I lied because I didn't want to make anyone feel bad for falling behind."
    kat "I've actually nearly completed my ph.D. thesis."
    y "How is that possible?"
    kat "How is it possible you made a game in a year that has over a million users?  By having a natural aptitude and putting in tens of thousands of hours in the fewest number of days."
    scene backathouse14
    kat "At the cafe, I thought I had left everyone in our little group behind.  I was ready to graduate and take a job offer out of state and move on with my life."
    kat "But then I found out I hadn't left everyone behind.  I was actually the one behind.  I was behind you."
    y "You're talking like this is some kind of race."
    kat "Well not exactly a race, but I hope you can understand how I felt.  I've been racing through life towards my goal of becoming one of the most successful Psychologists of all time and thinking my friends were just twiddling their thumbs."
    kat "Then all of a sudden you drop this bombshell that you too were following your dream and you made a game that I didn't even know you were working on, just like you didn't know the effort I was putting in at school, and now you're rich!"
    kat "And I'm in second place, and I mean that in more ways than one."
    scene backathouse16
    y "I'm not sure I'm following."
    kat "I want to be with you [y].  It was stupid of me to think I was above our group of friends and to be ready to move on and call it quits.  I want us to be a couple."
    kat "But just like in {i}Rosario Vampire{/i} you have a number one girl, and it's not me."
    kat "Kendra is your Moka Akashiya and I'm your Kurumu Kurono."
    kat "And just like that succubus I could've fucked you that night after the cafe or any night since and tried to take you away, but ultimately it wouldn't lead to happiness for anyone."
    scene backathouse15
    y "What does this have to do with seducing Gianna, or Kendra rebelling against her dad, or trying to get me down on my knees."
    kat "With you, there are two ways you could end up, both of which entice me."
    kat "As for Gianna and Kendra... I've been thinking a lot about what Kurumu should have done to get out of second place.  She needed to develop an intimate relationship with the other girls if she really wanted Tsukune."
    scene backathouse17
    y "So you're going to sleep with our friends?"
    kat "Yeah, well at least Gianna and Emily probably.  Kendra will never let me."
    y "And then I'm going to somehow have a harem where you are number one?  And that everyone is going to somehow end up living happily ever after?"
    scene backathouse11
    kat "Yes, I'll help you fuck all the girls and build a harem.  It'll be far easier for me to get Kendra in bed with you instead of me anyway."
    y "This is kinda fucked up Katrina."
    scene backathouse18
    kat "I know, I probably sound really crazy right now, but I'm not."
    y "And what if I refuse to go along with this plan of yours?"
    kat "Then I'll back off.  I'll stop preparing to seduce the others and I'll take a good long hard look inward at myself and try to find peace with being your number two."
    scene backathouse19
    kat "Do you want some time to think about it?"
    y "No, I've already made my decision."
    jump chapter2start
    scene backathouse20
    "Please save your game."
    jump chapter2start
    "Here are some previews of upcoming scenes."
    scene upcoming1
    pause
    scene upcoming2
    pause
    scene upcoming3
    pause
    scene upcoming4
    pause
    scene backathouse20
    "Last chance to save your game."
    jump chapter2start
label chapter2start:
    scene backathouse20
    $ katharem = False
    menu:
        "Ok, let's build this harem together!":
            jump katharem
        "Please leave the others alone.[Gr] \[+1 Confidence (Currenlty unknown if this choice prevents harem in the future)\]":
            jump ridingsolo
label katharem:
    scene afterdecision4
    y "Ok, let's build this harem together!"
    $ katharem = True
    kat "This is gonna be great [y]!"
    scene afterdecision2
    kat "We're gonna have so much fun!"
    y "Well you seem to know what you're doing with Gianna and if there's a chance I'll come out of all this on top I'm gonna take it!"
    scene afterdecision3
    kat "Oh you'll end up on top all right... if you know what I mean..."
    kat "For now though let's join up with the others at the beach!  We can play as much pool as we want back home, but every minute in Hawaii is precious!"
    scene afterdecision4
    y "Yeah sounds good, I'll grab my swim trunks and we can walk down together."
    jump beachall
label ridingsolo:
    scene afterdecision4
    $ confidence += 1
    y "Listen, Katrina, I appreciate you confiding all of this to me, but this has gotten a little too strange."
    y "We're not in some harem anime.  Have I been interested in all of you girls at one time or another?  Sure."
    y "And would I sleep with any of you if I had the chance, yeah probably, I am a guy after all."
    scene afterdecision5
    y "But when I think about this trip we're on and how I got talked into it even after I found out everyone wanted to cut ties with me I hurt deep down.  I feel anger, sadness, and betrayal."
    y "It really sucks to know that the people you care about the most don't feel the same way.  That they think they know what's best for you."
    y "Then when you suddenly find success they do a complete 180 towards you and after that, you can never know for sure whether now they're just in it for your money."
    y "Despite the anger and hurt I really want to forgive everyone.  Maybe that makes me a gullible idiot, but even so, I'm willing to forgive, to move on, and to create strong lasting relationships."
    y "That's what this trip is all about, forgiveness, and giving us all one last shot at friendship."
    scene afterdecision4
    y "And I don't want this last shot at friendship to become some quest of yours to build a harem for us ok?"
    y "I want us all to come out of this as true friends.  Ones that won't walk out on each other if someone gets too nerdy or falls behind the others because they didn't graduate fast enough."
    y "True friends that don't use each other for money or favors or play psychological games with."
    y "Do you understand me, Katrina?"
    scene afterdecision6
    k "Wow, this has actually turned into a really great talk [y]."
    k "I feel like we just had a therapy session together.  I said my piece and now you've said yours and I feel like we've gotten to know each other a lot better."
    k "We should have had this talk before I suggested we all take a trip.  That wasn't fair to you and I see now it's been weighing on your mind."
    scene afterdecision1
    "Katrina embraces you, and you in turn put your arms around her."
    k "I've been on a roller coaster of emotions in my head this last week since getting to know the real you.  I'm so sorry for everything."
    k "Hearing your words about friendship and heartache makes me feel like such a fool.  Of course, I'll respect you and your wish to rekindle our relationships without me getting involved with the other girls."
    k "Let's promise to talk openly like this from now on ok?"
    y "I promise.  It already feels like I got a huge weight off my chest just now."
    scene afterdecision3
    k "I'll let you in on a little secret and it'll be up to you whether to use it or not.  Gianna's jewelry is the key to seducing her.  She'll feel more naked without her jewelry than she would without her clothes."
    y "That's how you were gonna seduce her?  Take off her jewelry?  Really?"
    k "Well I already planted lots of little seeds, that was just the water to make them grow."
    k "Anyway that's it for my psychological games.  From now on I solemnly swear to only use my powers for good!  Never on someone in our group or on you, unless you ask me to use them on you that is..."
    scene afterdecision1
    y "Oh geez, ok that's enough talk, let's join the others at the beach.  Let me just go grab my swim trunks real quick."
    jump beachall
label beachall:
    scene afterdecision7
    e "Hey [y] and Katrina are here!"
    k "How did your talk go?"
    g "Yeah it sounded kind of serious.  Is everything ok?"
    scene afterdecision8
    y "It actually was serious, but Katrina and I had a good talk about some things that were coming between us."
    kat "Yeah don't worry about it, everything is cool now."
    e "Well great!  I'm glad I got dragged down here, let's have some fun!"
    scene beachall1
    "You spend the next hour having some good old fashioned beach fun."
    "You're glad you had the talk with Katrina, but it was more than a little stressful and it's great to wind down acting like kids again."
    scene beachall2
    y "So Emily, how come you're not wearing your new swimsuit?"
    e "Oh my god [y]!  It's like the tiniest thing ever!  I could never wear that to the beach, not even a private one like this!"
    k "Lies!  You know you love it, Emily!  I saw your eyes shine when you saw it!"
    e "Hey [y] is it true you saw Kendra wearing it at the store?"
    k "Don't tell her [y]!  Gianna let it slip a little, but Emily wasn't there so let's punish her by letting her imagination run wild!"
    y "Ok then, yeah Kendra modeled it for me, but that's all you'll ever know!"
    e "My imagination is gonna run wild then!  Prepare yourselves!  I'm gonna imagine you two doing all kinds of stuff!"
    y "Ha ha, wow I wish I had some popcorn and a front row seat in your brain!"
    e "C'mon!  Tell me!"
    scene beachall7
    g "Hey [y] come do some cartwheels with me!  It's pretty hard in the sand!"
    y "The ones I saw you doing from the balcony were pretty great."
    g "I did gymnastics as a kid and I still do them as a warmup for jogging nearly every day.  Doing them in the sand is extra fun though!"
    scene beachall8
    "You do several cartwheels with Gianna.  A few times you fall over but since it's sandy it doesn't hurt."
    "You even manage to get up into a handstand and even manage to walk a few feet on your hands."
    "Your shoulders and abs are burning and you realize this is actually a pretty good workout!"
    scene beachall7
    "You look back at Gianna.  Are you really just a couple of days from seducing her like Katrina said?"
    if katharem == True:
        jump whoseducesgiannafirst1
    else:
        jump whoseducesgiannafirst2
label whoseducesgiannafirst1:
    "And is Katrina really going to get to her first?"
    "The idea that Katrina is going to fuck Gianna does excite you quite a bit.  And if Katrina is true to her word then afterward you'll more than likely get a threesome with them at some point."
    jump beachall2
label whoseducesgiannafirst2:
    "Is her jewelry really the key to seducing her?"
    "Should you try to take it off her?"
    "That might look really weird.  She might get really pissed off."
    "Well if a situation where I could take it off her comes up I'll cross that bridge then."
    jump beachall2
label beachall2:
    scene beachall6
    e "Hey [y] will you give me a piggyback ride?"
    y "Yeah sure, hop on!"
    e "Before that, what did you talk about with Katrina?"
    y "Nosy today huh?  First, you want to know about Kendra at the store and now about Katrina?  How about the two of us make some of our own memories instead?"
    e "Ok yeah, time to mount up!"
    scene beachall9
    e "Away Sleipnir, my eight-legged steed!"
    y "Of course mighty Odin, your wish is my command!"
    e "Shush Sleipnir, horses cannot speak!"
    y "They can when they are the son of Loki."
    "You spend some time running Emily all-around your section of the beach.  Now your leg muscles are burning too!  You wonder how sore you're gonna be in the morning."
    scene beachall10
    k "This beach is so beautiful [y]!"
    y "It's hard to believe places like this even exist.  It's so different from the city back home."
    k "Do you think you'll find any inspiration for your game here?"
    y "I do!  The sky seems so much bluer and the water so clear, but at the same time the sun is so bright they appear white at times."
    y "I think whenever I move on to an expansion I'll have it take place on an island."
    y "Either that or I'll switch over to making ROBLOX games!  Those guys are making bank right now with all the kids stuck at home!"
    "Katrina lets out a snort of laughter behind you."
    k "Katrina are you ok?  You've been kind of lost in thought since you guys got here."
    kat "Yeah I'm ok, how about we play some volleyball?"
    scene beachall3
    "Since you have no net you decide to play with a beach ball over the umbrella."
    kat "This one's coming to you, Gianna!"
    g "Let's see how many times we can volley it before someone misses."
    scene beachall4
    g "Get ready guys I'll bump it as high as I can!  Get under it!"
    k "That's a good strategy!  Bumps and sets only guys, no spiking it!"
    scene beachall5
    e "With the umbrella angled towards your side I can barely get my hand over it to spike anyway!"
    "You manage to volley it over 20 times and after a few more tries you reach 30.  It's a little hard with the ocean breeze sometimes catching the ball."
    "When you finish Katrina mentions there is a full-sized net and a volleyball in the pool shed we could set up for the week if we want to play again."
    scene beachall9
    e "Back to the stables Sleipnir!  Evening has fallen and night will soon follow!"
    jump firepit1a
label firepit1a:
    scene firepit1
    "Shortly after you get back the girls change into their matching beach dresses and you start up a fire in the firepit by the jacuzzi."
    g "I thought this was a real firepit, but there was a switch and it came right on."
    y "Yeah I guess since this is a rental place they wanted the convenience and safety of an electric fire."
    k "Awwww, one of my Hawaiian dreams was to roast a huge pig on a spit over the fire!"
    kat "Don't worry Kendra, they'll probably do that at the luau later this week.  For now, do you guys wanna dance?"
    all "Yeah!"
    scene firepit2
    "You watch the girls begin dancing while you finish your Coca-Cola."
    "Katrina quickly pairs up with Gianna leaving Emily and Kendra as a pair."
    k "Come join us [y]!"
    y "I'm finishing my drink and enjoying the show."
    scene firepit3
    e "We'll just have to make the dance enticing enough that you can't help but want to join!"
    k "Yeah Emily, grind that ass on me!"
    e "You got it baby!"
    scene firepit4
    "You finish your drink and get up to join them."
    "You've never really been dancing so you're not too sure about your moves, but the girls don't seem to mind."
    "You think that when you get back you'll take a dancing lesson or two."
    g "Go [y] go!"
    e "Wooooo, shake what your daddy gave ya!"
    scene firepit5
    k "Watch out, some of [y]'s moves look like he's doing karate!"
    y "One of my special talents in Jumanji is Dance Fighting!"
    "You remember that night at the movies and burst into song together."
    all "Ooh baby, I love your way, every day."
    all "Wanna tell you I love your way, every day."
    all "Wanna be with you night and day, hey..."
    "You all kind of trail off and laugh, realizing none of you actually know more than the chorus."
    scene firepit6
    e "So who's gonna tell me what happened at the store today?"
    k "Are you still on about that Emily?  Tell you what, if you put that slingshot on I'll tell you!"
    e "Deal, but everyone else has to put their new swimsuits on too."
    k "Ok, you wait here [y], we'll be right back."
    scene firepit15
    "As you gaze into the fake electric fire while you wait for the girls to change, you can't help but think...."
    "This is gonna be fucking awesome!"
    if katharem == True:
        jump fire2girls
    else:
        jump fire4girls
label fire2girls:
    scene firepit11
    e "Hide me, Kendra!  I just can't do it!  It's too revealing!"
    k "C'mon Emily!  I thought you had a secret exhibitionist streak!"
    e "Yeah when other people could see me, but either they don't know they can or when I'm hiding below a desk!  [y] is looking right at me!"
    k "Ok fine, hide behind me chicken!"
    scene firepit8
    "The girls go back to dancing, but they make it a game of trying to keep you from getting in front of Emily for a good look."
    y "Where are Gianna and Kendra?  They didn't come back with you."
    k "They said they were still jet-lagged and wanted to head to bed early."
    scene firepit7
    e "Kendra, dodge left!  We must protect my modesty at all costs!"
    k "What about my modesty?  He's probably had a fantastic view of my ass this entire time!"
    e "Relax, it's getting pretty dark and he still has his sunglasses on, he can't see anything."
    k "Then why are you so worried about him seeing you?  And hey wait!  You have sunglasses on too and you are seeing everything just fine!"
    e "Ummm, oops!  Well, it's easier to see through pink lenses than black!"
    scene firepit13
    e "Anyway, we had a deal!  I put on this slingshot and you tell me what happened at the store."
    y "Should we tell her Kendra?"
    k "Yeah I guess, a deals a deal."
    k "So first we made [y] model the outfit he's wearing right now and Katrina was bragging about how hot she made him."
    scene firepit8
    k "Then we went to look for sexy bikinis and Gianna and Katrina got there first and left me standing awkwardly in front of a row of slingshots."
    k "So I thought, what the hell, if I didn't have my toxic bikini with me I'd still channel my inner naughty side, so I grabbed this leopard print one and tried it on."
    k "Everyone seemed pretty impressed and then I mentioned I saw an even skimpier pink one."
    k "Someone, not naming names, but definitely not me, suggested getting it for you as a prank."
    scene firepit7
    y "Definitely not me either."
    k "So then I thought I'd just try it on cause I just couldn't get over the fact that something that revealing was for sale."
    k "I found out it was see-through and like you, I decided there was no way I could show it to [y]."
    scene firepit13
    y "But right then her dad calls and Katrina answered it!"
    k "Hey this is my story!"
    y "I'm a main character though, so I reserve the right to chime in!"
    k "Yeah so my dad calls and Katrina starts getting sassy with him and so I burst out of the room to grab the phone."
    k "But then I remember the whole reason I'm even here is that he stole my toxic bikini out of my bag, so I decide if he's gonna do that, then I'll get back at him a little."
    scene firepitanim1
    "Suddenly Kendra pushes you back onto the bench and straddles you."
    k "It was kind of like this.  I forget what I said exactly, but I remember being all over [y]."
    k "It got so crazy, and now you've worn it too you know how easy it would be for the straps to fall to the sides and your breasts to be on full display."
    e "Oh my god did that happen?"
    k "Yeah, but I think my back was to him, so I'm not sure how much he saw."
    e "That's sooooo hot!"
    k "Like these slingshots shift to the sides so easy, I don't know how people wear them.  Even right now I can feel it sliding side to side a little."
    "Kendra starts grinding on you and you feel your dick getting more and more excited."
    jump animation1

label animation1:
    scene a1
    $ renpy.pause(0.05)
    scene a2
    $ renpy.pause(0.05)
    scene a3
    $ renpy.pause(0.05)
    scene a4
    $ renpy.pause(0.05)
    scene a5
    $ renpy.pause(0.05)
    scene a6
    $ renpy.pause(0.05)
    scene a7
    $ renpy.pause(0.05)
    scene a8
    $ renpy.pause(0.05)
    scene a9
    $ renpy.pause(0.05)
    scene a10
    $ renpy.pause(0.05)
    scene a11
    $ renpy.pause(0.05)
    scene a12
    $ renpy.pause(0.05)
    scene a13
    $ renpy.pause(0.05)
    scene a14
    $ renpy.pause(0.05)
    scene a15
    $ renpy.pause(0.05)
    scene a16
    $ renpy.pause(0.05)
    scene a17
    $ renpy.pause(0.05)
    scene a18
    $ renpy.pause(0.05)
    scene a19
    $ renpy.pause(0.05)
    scene a20
    $ renpy.pause(0.05)
    scene a21
    $ renpy.pause(0.05)
    scene a22
    $ renpy.pause(0.05)
    scene a23
    $ renpy.pause(0.05)
    scene a24
    $ renpy.pause(0.05)
    scene a25
    $ renpy.pause(0.05)
    scene a26
    $ renpy.pause(0.05)
    scene a27
    $ renpy.pause(0.05)
    scene a28
    $ renpy.pause(0.05)
    scene a29
    $ renpy.pause(0.05)
    scene a30
    $ renpy.pause(0.05)
    scene a31
    $ renpy.pause(0.05)
    scene a32
    $ renpy.pause(0.05)
    scene a33
    $ renpy.pause(0.05)
    scene a34
    $ renpy.pause(0.05)
    scene a35
    $ renpy.pause(0.05)
    scene a36
    $ renpy.pause(0.05)
    scene a37
    $ renpy.pause(0.05)
    scene a38
    $ renpy.pause(0.05)
    scene a39
    $ renpy.pause(0.05)
    scene a40
    $ renpy.pause(0.05)
    scene a41
    $ renpy.pause(0.05)
    scene a42
    $ renpy.pause(0.05)
    scene a43
    $ renpy.pause(0.05)
    scene a44
    $ renpy.pause(0.05)
    scene a45
    $ renpy.pause(0.05)
    scene a46
    $ renpy.pause(0.05)
    scene a47
    $ renpy.pause(0.05)
    scene a48
    $ renpy.pause(0.05)
    scene a49
    $ renpy.pause(0.05)
    scene a50
    $ renpy.pause(0.05)
    scene a51
    $ renpy.pause(0.05)
    scene a52
    $ renpy.pause(0.05)
    scene a53
    $ renpy.pause(0.05)
    scene a54
    $ renpy.pause(0.05)
    scene a55
    $ renpy.pause(0.05)
    scene a56
    $ renpy.pause(0.05)
    scene a57
    $ renpy.pause(0.05)
    scene a58
    $ renpy.pause(0.05)
    scene a59
    $ renpy.pause(0.05)
    scene a60
    $ renpy.pause(0.05)
    scene a61
    $ renpy.pause(0.05)
    scene a62
    $ renpy.pause(0.05)
    scene a63
    $ renpy.pause(0.05)
    scene a64
    $ renpy.pause(0.05)
    scene a65
    $ renpy.pause(0.05)
    scene a66
    $ renpy.pause(0.05)
    scene a67
    $ renpy.pause(0.05)
    scene a68
    $ renpy.pause(0.05)
    scene a69
    $ renpy.pause(0.05)
    scene a70
    $ renpy.pause(0.05)
    scene a71
    $ renpy.pause(0.05)
    scene a72
    $ renpy.pause(0.05)
    scene a73
    $ renpy.pause(0.05)
    scene a74
    $ renpy.pause(0.05)
    scene a75
    $ renpy.pause(0.05)
    scene a76
    $ renpy.pause(0.05)
    scene a77
    $ renpy.pause(0.05)
    scene a78
    $ renpy.pause(0.05)
    scene a79
    $ renpy.pause(0.05)
    scene a80
    $ renpy.pause(0.05)
    scene a81
    $ renpy.pause(0.05)
    scene a82
    $ renpy.pause(0.05)
    scene a83
    $ renpy.pause(0.05)
    scene a84
    $ renpy.pause(0.05)
    scene a85
    $ renpy.pause(0.05)
    scene a86
    $ renpy.pause(0.05)
    scene a87
    $ renpy.pause(0.05)
    scene a88
    $ renpy.pause(0.05)
    scene a89
    $ renpy.pause(0.05)
    scene a90
    $ renpy.pause(0.05)
    scene a91
    $ renpy.pause(0.05)
    scene a92
    $ renpy.pause(0.05)
    scene a93
    $ renpy.pause(0.05)
    scene a94
    $ renpy.pause(0.05)
    scene a95
    $ renpy.pause(0.05)
    scene a96
    $ renpy.pause(0.05)
    scene a97
    $ renpy.pause(0.05)
    scene a98
    $ renpy.pause(0.05)
    scene a99
    $ renpy.pause(0.05)
    scene a100
    $ renpy.pause(0.05)
    scene a101
    $ renpy.pause(0.05)
    scene a102
    $ renpy.pause(0.05)
    scene a103
    $ renpy.pause(0.05)
    scene a104
    $ renpy.pause(0.05)
    scene a105
    $ renpy.pause(0.05)
    scene a106
    $ renpy.pause(0.05)
    scene a107
    $ renpy.pause(0.05)
    scene a108
    $ renpy.pause(0.05)
    scene a109
    $ renpy.pause(0.05)
    scene a110
    $ renpy.pause(0.05)
    scene a111
    $ renpy.pause(0.05)
    scene a112
    $ renpy.pause(0.05)
    scene a113
    $ renpy.pause(0.05)
    scene a114
    $ renpy.pause(0.05)
    scene a115
    $ renpy.pause(0.05)
    scene a116
    $ renpy.pause(0.05)
    scene a117
    $ renpy.pause(0.05)
    scene a118
    $ renpy.pause(0.05)
    scene a119
    $ renpy.pause(0.05)
    scene a120
    $ renpy.pause(0.05)
    scene a121
    $ renpy.pause(0.05)
    scene a122
    $ renpy.pause(0.05)
    scene a123
    $ renpy.pause(0.05)
    scene a124
    $ renpy.pause(0.05)
    scene a125
    $ renpy.pause(0.05)
    scene a126
    $ renpy.pause(0.05)
    scene a127
    $ renpy.pause(0.05)
    scene a128
    $ renpy.pause(0.05)
    scene a129
    $ renpy.pause(0.05)
    scene a130
    $ renpy.pause(0.05)
    scene a131
    $ renpy.pause(0.05)
    scene a132
    $ renpy.pause(0.05)
    scene a133
    $ renpy.pause(0.05)
    scene a134
    $ renpy.pause(0.05)
    scene a135
    $ renpy.pause(0.05)
    scene a136
    $ renpy.pause(0.05)
    scene a137
    $ renpy.pause(0.05)
    scene a138
    $ renpy.pause(0.05)
    scene a139
    $ renpy.pause(0.05)
    scene a140
    $ renpy.pause(0.05)
    scene a141
    $ renpy.pause(0.05)
    scene a142
    $ renpy.pause(0.05)
    scene a143
    $ renpy.pause(0.05)
    scene a144
    $ renpy.pause(0.05)
    scene a145
    $ renpy.pause(0.05)
    scene a146
    $ renpy.pause(0.05)
    scene a147
    $ renpy.pause(0.05)
    scene a148
    $ renpy.pause(0.05)
    scene a149
    $ renpy.pause(0.05)
    scene a150
    $ renpy.pause(0.05)
    scene a151
    $ renpy.pause(0.05)
    scene a152
    $ renpy.pause(0.05)
    scene a153
    $ renpy.pause(0.05)
    scene a154
    $ renpy.pause(0.05)
    scene a155
    $ renpy.pause(0.05)
    scene a156
    $ renpy.pause(0.05)
    scene a157
    $ renpy.pause(0.05)
    scene a158
    $ renpy.pause(0.05)
    scene a159
    $ renpy.pause(0.05)
    scene a160
    $ renpy.pause(0.05)
    scene a161
    $ renpy.pause(0.05)
    scene a162
    $ renpy.pause(0.05)
    scene a163
    $ renpy.pause(0.05)
    scene a164
    $ renpy.pause(0.05)
    scene a165
    $ renpy.pause(0.05)
    scene a166
    $ renpy.pause(0.05)
    scene a167
    $ renpy.pause(0.05)
    scene a168
    $ renpy.pause(0.05)
    scene a169
    $ renpy.pause(0.05)
    scene a170
    $ renpy.pause(0.05)
    scene a171
    $ renpy.pause(0.05)
    scene a172
    $ renpy.pause(0.05)
    scene a173
    $ renpy.pause(0.05)
    scene a174
    $ renpy.pause(0.05)
    scene a175
    $ renpy.pause(0.05)
    scene a176
    $ renpy.pause(0.05)
    scene a177
    $ renpy.pause(0.05)
    scene a178
    $ renpy.pause(0.05)
    scene a179
    $ renpy.pause(0.05)
    scene a180
    $ renpy.pause(0.05)
    scene a181
    $ renpy.pause(0.05)
    scene a182
    $ renpy.pause(0.05)
    scene a183
    $ renpy.pause(0.05)
    scene a184
    $ renpy.pause(0.05)
    scene a185
    $ renpy.pause(0.05)
    scene a186
    $ renpy.pause(0.05)
    scene a187
    $ renpy.pause(0.05)
    scene a188
    $ renpy.pause(0.05)
    scene a189
    $ renpy.pause(0.05)
    scene a190
    $ renpy.pause(0.05)
    scene a191
    $ renpy.pause(0.05)
    scene a192
    $ renpy.pause(0.05)
    scene a193
    $ renpy.pause(0.05)
    scene a194
    $ renpy.pause(0.05)
    scene a195
    $ renpy.pause(0.05)
    scene a196
    $ renpy.pause(0.05)
    scene a197
    $ renpy.pause(0.05)
    scene a198
    $ renpy.pause(0.05)
    scene a199
    $ renpy.pause(0.05)
    scene a200
    $ renpy.pause(0.05)
    scene a201
    $ renpy.pause(0.05)
    scene a202
    $ renpy.pause(0.05)
    scene a203
    $ renpy.pause(0.05)
    scene a204
    $ renpy.pause(0.05)
    scene a205
    $ renpy.pause(0.05)
    scene a206
    $ renpy.pause(0.05)
    scene a207
    $ renpy.pause(0.05)
    jump fire2girls2
label fire2girls2:
    scene a207
    "As Kendra finishes riding you you notice her suit has shifted to the side and a wet spot is starting to appear on your pants where her pussy was uncovered."
    "Clearly she's very excited."
    k "Ummmm, wow this is getting out of hand again.  Then basically I hung up on my dad.  Can we get in the jacuzzi and cool off?"
    scene bikininighta
    "Kendra knew you didn't have your swim trunks on when she suggested the jacuzzi, so you decide to go in naked thinking maybe that's what she's expecting."
    "Your pants were feeling way too tight anyway."
    e "Kendra, how am I gonna hide behind you in here, are you gonna sit on my lap?"
    k "I think sitting on [y]'s lap was enough for now.  Emily, you're just gonna have to suck it up and at least let him see you from the top-up."
    scene bikininightd
    e "Fine, ok [y] here's a good look at my side boob!"
    e "I can't believe you guys did all that in a store!"
    e "Did any other customers see you?  Did the clerk?"
    y "I don't remember there being any other customers, and no the clerk was up at the cash register, so I think we got away with it."
    e "I'm super turned on right now!  Can I grind on you a little like Kendra did?"
    k "You know he's naked under the water right?"
    e "Just for a minute?  Pleeeeeeeeaaase?  I'll be super careful not to let my suit slip!"
    k "Go for it then!  I don't want to hog [y] all to myself!"
    y "Yeah there's plenty of me to go around!"
    scene bikininighth
    "She climbs on your lap and starts to rub herself against your hard dick."
    e "I'm not sure what would be hotter, you guys getting away with fooling around in a store or you guys getting caught doing that!"
    y "Which would you want if it were me and you?"
    e "Oh god!  Don't tell anyone ok?  I maybe wish we'd get caught.  I've been getting away with little things for so long I kinda wonder what it'd be like to get caught, just once."
    scene bikininighte
    "Emily cups her breasts and moans.  You think about sucking her nipple and if Kendra had joined in you would have, but instead, you decide to lighten the atmosphere by motorboating Emily's breasts instead."
    e "Ha ha ha, that tickles [y]!"
    y "You'rrere aa bbadd ggiirll Emmmly!"
    "Kendra laughs at your garbled speech and you pull back."
    scene bikininighth
    y "I can't believe that I'm saying this, but I'm about at my limit.  You better hop off."
    e "Ok, but while I've got you here, I have something I want to talk to you about tomorrow."
    y "What?  Why tomorrow?"
    e "I'm waiting for the perfect time to ambush you.  You'll find out when the time is right!"
    y "Haha, we'll I'd better be on my guard then!"
    scene bikininightd
    "Emily hops off and the three of you relax and chat a bit more."
    "Eventually your dick settles back down and you decide to call it a night."
    $ renpy.end_replay()
    jump katrinagianna
label katrinagianna:
    scene findinglaptop1
    "When you get back to your room you find your laptop has been moved to your bed along with what looks like Gianna's bracelet and rings on your nightstand."
    scene findinglaptop2
    "Curiously you sit down on the bed and see that Notepad is open on the taskbar along with Windows Media Player."
    "You click on Notepad first."
    kat "Hey [y], sorry Gianna and I didn't rejoin you guys at the firepit, but I'm sure you'll enjoy this video I recorded on your laptop of me and Gianna."
    kat "Don't lose Gianna's jewelry there on the nightstand.  It's pretty important.  Don't give it back to her either yet though.  Just hang onto it for safekeeping."
    "You click on the video."
    scene katseduction1
    g "What did you just do on [y]'s laptop?"
    kat "I turned the camera on.  I know how much you like sending him sexy pics, so I thought we'd surprise him!"
    g "Like kiss and hide the file somewhere on his computer for him to find later?  That could be fun."
    scene katseduction2
    kat "Have you been having fun with me so far on this trip Gianna?"
    g "Yes, I especially liked the movie last night.  I'm glad we shared a couch together."
    kat "What movie did we watch last night?"
    g "Ummm, you know what?  I can't really remember.  I just remember enjoying it with you."
    scene katseduction3
    kat "Do you remember when we talked about your jewelry in the shower."
    g "Yes, I do remember that.  You said you liked it."
    kat "That's right.  Do you like my tattoos?"
    g "They're very pretty."
    kat "They have significant meaning to me too, just like your jewelry does to you, but you know what's better about tattoos?"
    g "No, what?"
    kat "They don't come off."
    scene katseduction5
    "You watch the screen as suddenly Katrina whips her hand down Gianna's arm, knocking her jewelry onto the floor."
    "Gianna gasps and starts to try to pick it up, but Katrina grabs her."
    scene katseduction6
    kat "Leave it on the floor Gianna.  Look at me.  Those life-changing events that led to you putting on that bracelet and those rings are in the past."
    kat "Here and now is what matters."
    "Gianna gives up on the jewelry and stares into Katrina's eyes."
    "This feels a lot like the shower and the store.  And you try to remember what Katrina and Gianna were whispering about last night during the movie, but you had been too focused on Kendra."
    "A full minute passes as they continue to stare at each other.  Then Katrina speaks."
    scene katseduction7
    kat "Now, we need to get started making a fun video for [y]."
    "Katrina pulls down the front on Gianna's dress with her right hand, but doesn't break eye contact."
    kat "You still want to right?"
    g "Yes, he has a few good pictures of me and I'd really like it if he had more."
    kat "He'll be so happy, and so will I.  You want to make me happy too right?"
    g "Very much."
    scene katseduction8
    "Katrina pulls Gianna's dress the rest of the way down and then follows up with her own.  Then she pulls Gianna to her chest, finally breaking eye contact."
    kat "That's it, suck my breasts, Gianna."
    kat "[y] is going to love this.  We can send him lots of fun sexy pics from now on."
    scene katseduction9
    kat "Now kiss lower.  It's ok to be on your knees in front of me.  I love your lips on my bellybutton."
    "You know that getting people on their knees seems to be Katrina's fetish.  An image of you and Gianna both on your knees in front of Katrina briefly flashes in your mind."
    "Then another image of you and Katrina standing hand in hand with Gianna, Emily, and Kendra kneeling in front of you both crosses your mind as well."
    scene katseduction10
    kat "You look so beautiful like this Gianna.  Do you feel beautiful?"
    g "Yes, you look so beautiful too Katrina.  I'm sorry I didn't realize it until now."
    scene katseduction11
    kat "[y] is going to love this video, but we better spice it up a little more.  What do you think?"
    g "I think the spicier the better."
    scene katseduction12
    "Katrina sits on the bed and locks her legs around Gianna's head."
    kat "Have you ever been with another girl?"
    g "No."
    kat "Me neither.  I might need to get another tattoo after this special moment we have together."
    kat "Now lick my pussy."
    scene katseduction13
    kat "Oh god, that feels great Gianna!  Don't stop!"
    "The girls moan in pleasure."
    scene katseduction14
    kat "Flick your tongue over my clit."
    kat "Good girl, yes right there."
    "You see Katrina pull Gianna further in with her legs."
    kat "Now join me up here on the bed."
    scene katseduction15
    "Gianna pushes Katrina back and joins her on the bed, caressing her breasts and kissing her nipple between her thumb and index finger."
    kat "That feels wonderful Gianna, but I can't let you be on top!"
    scene katseduction16
    "Katrina slides out to the side and flips Gianna onto her back."
    kat "You'd rather be on the bottom anyway right Gianna?"
    g "Yes, you belong on top."
    scene katseduction17
    kat "That's right.  You're a fast learner."
    "You're not sure whether she's talking about being a fast learner at obeying commands or about eating pussy or maybe both."
    scene katseduction18
    kat "Oh god, I don't want this to ever end!"
    kat "I might need some practice too though for another time.  And also it wouldn't be fair for me to take all the pleasure."
    scene katseduction19
    "Katrina goes down on Gianna and the girls' moans once again fill the room."
    "You realize at some point you took out your dick and had begun stroking."
    scene katseduction20
    "The girls continue to eat each other out while you watch."
    "You consider how lucky you are that you left your computer on earlier.  Otherwise, this might have only been a couple pics texted to your phone."
    scene katseduction21
    kat "Hmmm, your eyes are closed now."
    kat "Let's try another position."
    scene katseduction22
    "Gianna's eyes stay closed and Katrina speaks directly to the camera for the first time since they entered the room."
    kat "I hope you're enjoying the show [y]."
    kat "When we have your drinking party later don't ask us about this if we play {i}Never Have I Ever.{/i}"
    scene katseduction23
    "Hearing Katrina talk to you seems to remind Gianna they are here to put on a show.  She sits up and starts grinding harder."
    kat "This is so intense.  Maybe I should start jogging every morning too to build up my strength so I can keep up with you!"
    scene katseduction25
    kat "I'm going to cum Gianna, keep going just a little longer."
    g "I've cum so many times already."
    kat "I know, you're such a good girl."
    "Katrina orgasms and they fall to the bed."
    scene katseduction26
    g "That was amazing!"
    kat "Having sex with another woman was even better than I thought it'd be."
    "The girls kiss and cuddle for a bit."
    scene katseduction27
    kat "Well we better get out of here before [y] gets back."
    g "Yeah the only way to explain this situation if he catches us in person would be to fuck him."
    kat "Actually that might not be so bad, but not yet, we'll save that for another day soon."
    scene katseduction28
    g "Hey can I put my bracelet and rings back on now."
    kat "No, we're going to leave them here for [y] to hold onto.  I'm sure he'll take good care of them for you this week."
    scene katseduction29
    g "Ok, I trust you Katrina, and I trust [y] too."
    kat "Good girl.  You head back to your room now and I'll set up the laptop for [y] to find."
    $ renpy.end_replay()
    scene findinglaptop2
    "Wow, that was an amazing video.  Katrina really did manage to seduce Gianna and even found a way for you to watch it."
    "You can't wait to see what the rest of the week holds."
    jump sandymorningb

label fire4girls:
    scene firepit12
    e "Hide me, Kendra!  I just can't do it!  It's too revealing!"
    k "C'mon Emily!  I thought you had a secret exhibitionist streak!"
    scene firepit10
    e "Yeah when other people could see me, but either they don't know they can or when I'm hiding below a desk!  [y] is looking right at me!"
    k "Ok fine, hide behind me chicken!"
    scene firepit9
    "The girls go back to dancing, but they make it a game of trying to keep you from getting in front of Emily for a good look."
    g "Katrina, swivel right, dance arms in block position!"
    kat "You're not getting through on this side [y].  You're safe for now Emily!"
    scene firepit7
    e "Kendra, dodge left!  We must protect my modesty at all costs!"
    k "What about my modesty?  He's probably had a fantastic view of my ass this entire time!"
    e "Relax, it's getting pretty dark and he still has his sunglasses on, he can't see anything."
    k "Then why are you so worried about him seeing you?  And hey wait!  You have sunglasses on too and you are seeing everything just fine!"
    e "Ummm, oops!  Well, it's easier to see through pink lenses than black!"
    scene firepit14
    kat "Kendra, lean back and edge him closer to the fire and wait for your moment to strike!"
    y "Wait, when did guarding Emily take such a lethal turn?"
    e "When he respawns back in the house, everyone run for it!"
    g "Won't he respawn as a ghost and only fully recover once he arrives back here to reclaim his dropped equipment?"
    y "Haha, don't tease me about my game mechanics!  Lots of other games do that too you know!"
    scene firepit9
    e "Anyway, we had a deal!  I put on this slingshot and you tell me what happened at the store."
    y "Should we tell her Kendra?"
    k "Yeah I guess, a deals a deal."
    k "So first we made [y] model the outfit he's wearing right now and Katrina was bragging about how hot she made him."
    kat "Yeah, I take full credit!"
    scene firepit14
    k "Then we went to look for sexy bikinis and Gianna and Katrina got there first and left me standing awkwardly in front of a row of slingshots."
    k "So I thought, what the hell, if I didn't have my toxic bikini with me I'd still channel my inner naughty side, so I grabbed this leopard print one and tried it on."
    k "Everyone seemed pretty impressed and then I mentioned I saw an even skimpier pink one."
    k "Someone, not naming names, but definitely not me, suggested getting it for you as a prank."
    scene firepit9
    y "Definitely not me either."
    g "Or me!"
    kat "Or me either!"
    k "So then I thought I'd just try it on cause I just couldn't get over the fact that something that revealing was for sale."
    k "I found out it was see-through and like you, I decided there was no way I could show it to [y]."
    scene firepit14
    y "But right then her dad calls and Katrina answered it!"
    k "Hey this is my story!"
    y "I'm a main character though, so I reserve the right to chime in!"
    k "Yeah so my dad calls and Katrina starts getting sassy with him and so I burst out of the room to grab the phone."
    k "But then I remember the whole reason I'm even here is that he stole my toxic bikini out of my bag, so I decide if he's gonna do that, then I'll get back at him a little."
    scene firepitanim1
    "Suddenly Kendra pushes you back onto the bench and straddles you."
    k "It was kind of like this.  I forget what I said exactly, but I remember being all over [y]."
    k "It got so crazy, and now you've worn it too you know how easy it would be for the straps to fall to the sides and your breasts to be on full display."
    e "Oh my god did that happen?"
    k "Yeah, but I think my back was to him, so I'm not sure how much he saw."
    e "That's sooooo hot!"
    k "Like these slingshots shift to the sides so easy, I don't know how people wear them.  Even right now I can feel it sliding side to side a little."
    "Kendra starts grinding on you and you feel your dick getting more and more excited."
    jump animation2
label animation2:
    scene a1
    $ renpy.pause(0.05)
    scene a2
    $ renpy.pause(0.05)
    scene a3
    $ renpy.pause(0.05)
    scene a4
    $ renpy.pause(0.05)
    scene a5
    $ renpy.pause(0.05)
    scene a6
    $ renpy.pause(0.05)
    scene a7
    $ renpy.pause(0.05)
    scene a8
    $ renpy.pause(0.05)
    scene a9
    $ renpy.pause(0.05)
    scene a10
    $ renpy.pause(0.05)
    scene a11
    $ renpy.pause(0.05)
    scene a12
    $ renpy.pause(0.05)
    scene a13
    $ renpy.pause(0.05)
    scene a14
    $ renpy.pause(0.05)
    scene a15
    $ renpy.pause(0.05)
    scene a16
    $ renpy.pause(0.05)
    scene a17
    $ renpy.pause(0.05)
    scene a18
    $ renpy.pause(0.05)
    scene a19
    $ renpy.pause(0.05)
    scene a20
    $ renpy.pause(0.05)
    scene a21
    $ renpy.pause(0.05)
    scene a22
    $ renpy.pause(0.05)
    scene a23
    $ renpy.pause(0.05)
    scene a24
    $ renpy.pause(0.05)
    scene a25
    $ renpy.pause(0.05)
    scene a26
    $ renpy.pause(0.05)
    scene a27
    $ renpy.pause(0.05)
    scene a28
    $ renpy.pause(0.05)
    scene a29
    $ renpy.pause(0.05)
    scene a30
    $ renpy.pause(0.05)
    scene a31
    $ renpy.pause(0.05)
    scene a32
    $ renpy.pause(0.05)
    scene a33
    $ renpy.pause(0.05)
    scene a34
    $ renpy.pause(0.05)
    scene a35
    $ renpy.pause(0.05)
    scene a36
    $ renpy.pause(0.05)
    scene a37
    $ renpy.pause(0.05)
    scene a38
    $ renpy.pause(0.05)
    scene a39
    $ renpy.pause(0.05)
    scene a40
    $ renpy.pause(0.05)
    scene a41
    $ renpy.pause(0.05)
    scene a42
    $ renpy.pause(0.05)
    scene a43
    $ renpy.pause(0.05)
    scene a44
    $ renpy.pause(0.05)
    scene a45
    $ renpy.pause(0.05)
    scene a46
    $ renpy.pause(0.05)
    scene a47
    $ renpy.pause(0.05)
    scene a48
    $ renpy.pause(0.05)
    scene a49
    $ renpy.pause(0.05)
    scene a50
    $ renpy.pause(0.05)
    scene a51
    $ renpy.pause(0.05)
    scene a52
    $ renpy.pause(0.05)
    scene a53
    $ renpy.pause(0.05)
    scene a54
    $ renpy.pause(0.05)
    scene a55
    $ renpy.pause(0.05)
    scene a56
    $ renpy.pause(0.05)
    scene a57
    $ renpy.pause(0.05)
    scene a58
    $ renpy.pause(0.05)
    scene a59
    $ renpy.pause(0.05)
    scene a60
    $ renpy.pause(0.05)
    scene a61
    $ renpy.pause(0.05)
    scene a62
    $ renpy.pause(0.05)
    scene a63
    $ renpy.pause(0.05)
    scene a64
    $ renpy.pause(0.05)
    scene a65
    $ renpy.pause(0.05)
    scene a66
    $ renpy.pause(0.05)
    scene a67
    $ renpy.pause(0.05)
    scene a68
    $ renpy.pause(0.05)
    scene a69
    $ renpy.pause(0.05)
    scene a70
    $ renpy.pause(0.05)
    scene a71
    $ renpy.pause(0.05)
    scene a72
    $ renpy.pause(0.05)
    scene a73
    $ renpy.pause(0.05)
    scene a74
    $ renpy.pause(0.05)
    scene a75
    $ renpy.pause(0.05)
    scene a76
    $ renpy.pause(0.05)
    scene a77
    $ renpy.pause(0.05)
    scene a78
    $ renpy.pause(0.05)
    scene a79
    $ renpy.pause(0.05)
    scene a80
    $ renpy.pause(0.05)
    scene a81
    $ renpy.pause(0.05)
    scene a82
    $ renpy.pause(0.05)
    scene a83
    $ renpy.pause(0.05)
    scene a84
    $ renpy.pause(0.05)
    scene a85
    $ renpy.pause(0.05)
    scene a86
    $ renpy.pause(0.05)
    scene a87
    $ renpy.pause(0.05)
    scene a88
    $ renpy.pause(0.05)
    scene a89
    $ renpy.pause(0.05)
    scene a90
    $ renpy.pause(0.05)
    scene a91
    $ renpy.pause(0.05)
    scene a92
    $ renpy.pause(0.05)
    scene a93
    $ renpy.pause(0.05)
    scene a94
    $ renpy.pause(0.05)
    scene a95
    $ renpy.pause(0.05)
    scene a96
    $ renpy.pause(0.05)
    scene a97
    $ renpy.pause(0.05)
    scene a98
    $ renpy.pause(0.05)
    scene a99
    $ renpy.pause(0.05)
    scene a100
    $ renpy.pause(0.05)
    scene a101
    $ renpy.pause(0.05)
    scene a102
    $ renpy.pause(0.05)
    scene a103
    $ renpy.pause(0.05)
    scene a104
    $ renpy.pause(0.05)
    scene a105
    $ renpy.pause(0.05)
    scene a106
    $ renpy.pause(0.05)
    scene a107
    $ renpy.pause(0.05)
    scene a108
    $ renpy.pause(0.05)
    scene a109
    $ renpy.pause(0.05)
    scene a110
    $ renpy.pause(0.05)
    scene a111
    $ renpy.pause(0.05)
    scene a112
    $ renpy.pause(0.05)
    scene a113
    $ renpy.pause(0.05)
    scene a114
    $ renpy.pause(0.05)
    scene a115
    $ renpy.pause(0.05)
    scene a116
    $ renpy.pause(0.05)
    scene a117
    $ renpy.pause(0.05)
    scene a118
    $ renpy.pause(0.05)
    scene a119
    $ renpy.pause(0.05)
    scene a120
    $ renpy.pause(0.05)
    scene a121
    $ renpy.pause(0.05)
    scene a122
    $ renpy.pause(0.05)
    scene a123
    $ renpy.pause(0.05)
    scene a124
    $ renpy.pause(0.05)
    scene a125
    $ renpy.pause(0.05)
    scene a126
    $ renpy.pause(0.05)
    scene a127
    $ renpy.pause(0.05)
    scene a128
    $ renpy.pause(0.05)
    scene a129
    $ renpy.pause(0.05)
    scene a130
    $ renpy.pause(0.05)
    scene a131
    $ renpy.pause(0.05)
    scene a132
    $ renpy.pause(0.05)
    scene a133
    $ renpy.pause(0.05)
    scene a134
    $ renpy.pause(0.05)
    scene a135
    $ renpy.pause(0.05)
    scene a136
    $ renpy.pause(0.05)
    scene a137
    $ renpy.pause(0.05)
    scene a138
    $ renpy.pause(0.05)
    scene a139
    $ renpy.pause(0.05)
    scene a140
    $ renpy.pause(0.05)
    scene a141
    $ renpy.pause(0.05)
    scene a142
    $ renpy.pause(0.05)
    scene a143
    $ renpy.pause(0.05)
    scene a144
    $ renpy.pause(0.05)
    scene a145
    $ renpy.pause(0.05)
    scene a146
    $ renpy.pause(0.05)
    scene a147
    $ renpy.pause(0.05)
    scene a148
    $ renpy.pause(0.05)
    scene a149
    $ renpy.pause(0.05)
    scene a150
    $ renpy.pause(0.05)
    scene a151
    $ renpy.pause(0.05)
    scene a152
    $ renpy.pause(0.05)
    scene a153
    $ renpy.pause(0.05)
    scene a154
    $ renpy.pause(0.05)
    scene a155
    $ renpy.pause(0.05)
    scene a156
    $ renpy.pause(0.05)
    scene a157
    $ renpy.pause(0.05)
    scene a158
    $ renpy.pause(0.05)
    scene a159
    $ renpy.pause(0.05)
    scene a160
    $ renpy.pause(0.05)
    scene a161
    $ renpy.pause(0.05)
    scene a162
    $ renpy.pause(0.05)
    scene a163
    $ renpy.pause(0.05)
    scene a164
    $ renpy.pause(0.05)
    scene a165
    $ renpy.pause(0.05)
    scene a166
    $ renpy.pause(0.05)
    scene a167
    $ renpy.pause(0.05)
    scene a168
    $ renpy.pause(0.05)
    scene a169
    $ renpy.pause(0.05)
    scene a170
    $ renpy.pause(0.05)
    scene a171
    $ renpy.pause(0.05)
    scene a172
    $ renpy.pause(0.05)
    scene a173
    $ renpy.pause(0.05)
    scene a174
    $ renpy.pause(0.05)
    scene a175
    $ renpy.pause(0.05)
    scene a176
    $ renpy.pause(0.05)
    scene a177
    $ renpy.pause(0.05)
    scene a178
    $ renpy.pause(0.05)
    scene a179
    $ renpy.pause(0.05)
    scene a180
    $ renpy.pause(0.05)
    scene a181
    $ renpy.pause(0.05)
    scene a182
    $ renpy.pause(0.05)
    scene a183
    $ renpy.pause(0.05)
    scene a184
    $ renpy.pause(0.05)
    scene a185
    $ renpy.pause(0.05)
    scene a186
    $ renpy.pause(0.05)
    scene a187
    $ renpy.pause(0.05)
    scene a188
    $ renpy.pause(0.05)
    scene a189
    $ renpy.pause(0.05)
    scene a190
    $ renpy.pause(0.05)
    scene a191
    $ renpy.pause(0.05)
    scene a192
    $ renpy.pause(0.05)
    scene a193
    $ renpy.pause(0.05)
    scene a194
    $ renpy.pause(0.05)
    scene a195
    $ renpy.pause(0.05)
    scene a196
    $ renpy.pause(0.05)
    scene a197
    $ renpy.pause(0.05)
    scene a198
    $ renpy.pause(0.05)
    scene a199
    $ renpy.pause(0.05)
    scene a200
    $ renpy.pause(0.05)
    scene a201
    $ renpy.pause(0.05)
    scene a202
    $ renpy.pause(0.05)
    scene a203
    $ renpy.pause(0.05)
    scene a204
    $ renpy.pause(0.05)
    scene a205
    $ renpy.pause(0.05)
    scene a206
    $ renpy.pause(0.05)
    scene a207
    $ renpy.pause(0.05)
    jump fire4girls2
label fire4girls2:
    scene a207
    "As Kendra finishes riding you you notice her suit has shifted to the side and a wet spot is starting to appear on your pants where her pussy was uncovered."
    "Clearly she's very excited."
    k "Ummmm, wow this is getting out of hand again.  Then basically I hung up on my dad.  Can we get in the jacuzzi and cool off?"
    scene bikininightb
    "Kendra knew you didn't have your swim trunks on when she suggested the jacuzzi, so you decide to go in naked thinking maybe that's what she's expecting."
    "Your pants were feeling way too tight anyway."
    "You get in first with Gianna and Katrina and no one seems to mind."
    e "Kendra, how am I gonna hide behind you in here, are you gonna sit on my lap?"
    k "I think sitting on [y]'s lap was enough for now Emily.  You're just gonna have to suck it up and at least let him see you from the top-up."
    scene bikininightc
    e "Fine, ok [y] have a good look at whatever you can see in this light and under the water.  I guess I've teased you long enough that you deserve it!"
    e "I still can't believe you guys did all that in a store!"
    e "Did any other customers see you?  Did the clerk?"
    y "I don't remember there being any other customers, and no the clerk was up at the cash register, so I think we got away with it."
    e "I'm super turned on right now!  Can I grind on you a little like Kendra did?"
    kat "You know he's naked under the water right?"
    e "Just for a minute?  Pleeeeeeeeaaase?  I'll be super careful not to let my suit slip!"
    k "Go for it then!  I don't want to hog [y] all to myself!"
    y "Yeah there's plenty of me to go around!"
    scene bikininightg
    "She climbs on your lap and starts to rub herself against your hard dick."
    e "I'm not sure what would be hotter, you guys getting away with fooling around in a store or you guys getting caught doing that!"
    y "Which would you want if it were me and you?"
    e "Oh god!  Don't tell anyone ok?  I maybe wish we'd get caught.  I've been getting away with little things for so long I kinda wonder what it'd be like to get caught, just once."
    scene bikininightf
    "Emily cups her breasts and moans."
    "None of the other girls have joined in, but neither are they acting uncomfortable and not having been in any situation even remotely like this before you're not sure what to do."
    "You decide to motorboat Emily and keep the mood playful."
    e "Ha ha ha, that tickles [y]!"
    y "You'rrere aa bbadd ggiirll Emmmly!"
    "Everyone laughs at your garbled speech and you pull back."
    scene bikininightg
    y "I can't believe that I'm saying this, but I'm about at my limit.  You better hop off."
    e "Ok, but while I've got you here, I have something I want to talk to you about tomorrow."
    y "What?  Why tomorrow?"
    e "I'm waiting for the perfect time to ambush you.  You'll find out when the time is right!"
    y "Haha, we'll I'd better be on my guard then!"
    scene bikininightc
    "Emily hops off and the five of you relax and chat a bit more."
    "Eventually your dick settles back down and you decide to call it a night."
    jump sandymorninga

label sandymorninga:
    scene day2morning1
    "The next morning shortly after waking up you find yourself at your computer with a hot coffee."
    "You think back to the amazing night before."
    "It was so much fun dancing with the girls.  There will definitely have to be more of that when you guys have the drinking party later."
    "Let's see them keep Emily's modesty intact when they are all drunk!"
    scene hawaiiworking1
    "It was great having Emily and Kendra grind on you too.  First Kendra with her suit slid to the side and then Emily with you completely naked."
    "Each time there was just a thin layer of fabric between you and them."
    scene gmorningwj
    g "Hey [y]!  Good morning!"
    y "Good morning Gianna!  Are you going jogging again?"
    g "Yeah, and if you wanted to join me I was thinking we could drag the volleyball net down to the beach and set it up for later."
    g "Also I've got my bikini on so we could swim over to the next cove over if you want."
    y "Sounds great!  I'd love to join you.  Give me a sec to get ready."
    scene giannanet1a
    y "Holy shit, I didn't think this was going to be an Olympic regulation net!"
    g "Yeah that thing is heavy!"
    y "We'll have to play when the tide is out, or else the team on the other side is going to have a serious handicap!"
    scene giannanet2
    g "At least it should be sturdy enough the wind won't blow it over.  It was blowing that beach ball all over the place yesterday."
    y "That's true.  So ready to go jogging?  I'm really trying to get six-pack abs.  I've always wanted them!"
    scene giannanet3
    g "That's great you want to improve yourself.  My abs have never quite had the definition I want, even with all the working out."
    y "You look fantastic, don't say that!"
    g "Let's swim over to the next cove now and check it out."
    scene giannanet4
    "After a brief swim over to the next cove, you head back."
    "It's a public beach, but since it's still early in the day there weren't that many people, just a few locals."
    "It might be fun to check it out again later with your full group."
    g "What do you want to do now?  Lay in the sun and dry off or maybe head back?"
    scene giannanet5
    "You think back to Katrina mentioning about Gianna's jewelry and find yourself really curious."
    y "I was just thinking about how pretty you look when you're wet."
    g "Oh really?"
    "She doesn't pull away as you touch her, so you decide to go for it figuring maybe you can talk your way out of it if she gets mad and give it right back."
    y "Let's play a little one on one volleyball.  I'll put your jewelry over on the towel so it doesn't slip off while it's wet and get lost in the sand."
    scene giannanet6
    "Before she can reply you quickly slide your hand down her arm and then down her hand and fingers, grabbing her bracelet and rings as you go."
    "She lets out a small gasp and her rate of breathing noticeably increases, but she doesn't say anything."
    "You place the jewelry on a towel and decide to start the volleyball game while you assess her mood."
    scene giannanet7
    y "Ok, let's see what you got Gianna!"
    g "Bring it on [y]!"
    y "Everything's ok right?"
    g "Yeah I'm pumped to play!  You remember I played volleyball in high school right?"
    scene giannanet8
    y "Of course!  You guys won the county right?"
    g "Yeah one year we did, but you might be remembering the field hockey team I was on with Kendra.  We won the county every year and even the state when we were seniors."
    y "Yeah, thanks to me cheering you guys on in the bleachers with Emily and Katrina!"
    scene giannanet9
    g "You guys were always so supportive!  I always really liked that about you."
    g "And you're proving to be really good at volleyball!  It's a shame our school didn't have a boys team."
    y "I did pretty well in gym class when we played, and being a little taller than average helps too."
    y "My favorite thing in volleyball is actually blocking spikes.  I like it even more than spiking the ball myself."
    scene giannanet7
    g "Me too!  Like there is this instant where your opponent's eyes go wide, just as they realize you've stopped them."
    g "Another thing I like is diving for the ball and keeping it just barely in play."
    scene giannanet10
    y "You mean like this?"
    "You bump the ball towards the sideline just out of reach and Gianna dives for it."
    "The shifting sand makes for bad footing though so she doesn't quite get there in time."
    scene giannanet11
    g "Ha, no not like that!  If that was a gym floor I think I'd have made it though!"
    g "Now I'm covered with sand instead and you scored."
    scene giannanet12
    y "I actually do feel like I scored!  I gotta say you look really really good right now."
    g "You look really good too [y]."
    y "I think I might like you better covered in sand than I do seeing you wet."
    "You took her jewelry off earlier, but she hasn't been acting that different."
    "It does seem like she's enjoying hanging out with you and she seems to enjoy your compliments, so you decide to push things a little further."
    y "I'd love to get a picture of you wearing the sand."
    g "I guess your collection could use another sexy pic.  Sure go ahead!"
    y "I mean of you only wearing sand."
    "Back in the kitchen the last time you got a pic she had told you her one rule is that her bikini stays on."
    scene giannanet13
    g "Oh that sounds naughty!"
    "She slides out of her bikini and tosses it over towards the towels."
    g "I guess being covered with sand is a little like the girls who model wearing only body paint."
    y "Yeah it's just like that."
    "You take out your phone and snap a picture of her giving you a sultry look."
    y "Let's see if we can top that with an even sexier version.  How about a yoga pose?"
    scene giannanet14
    "She spins around with her back towards you for a second and then strikes another pose."
    g "Like this?"
    y "That's perfect!  Now let's get a few of you standing up so I can get the ocean in the background."
    scene giannanet15
    g "That's a really good idea!  Hawaii is so beautiful.  I feel like a real model doing a Hawaiian photo shoot."
    y "You'd put those models to shame!  Now shift just a little to the side and we'll take the perfect shot."
    scene upcoming4
    g "Text this one to me later ok?"
    y "Sure thing!"
    g "When I look back on this trip I want to be able to remember this moment perfectly."
    y "Me too!  Now get on your knees for the next one."
    scene giannanet16
    "She drops to her knees in front of you."
    "So far she's done everything you said."
    scene giannanet17
    "You already knew that she likes taking sexy pictures though, but how will she react if you put the phone down?"
    y "Gianna, I'm having a bit of a problem, do you think you can help me out?"
    g "Judging by the bulge in your shorts I can see you have a {i}big{/i} problem you need help with!"
    scene giannanet18
    "She pulls your shorts down and grabs your cock.  You take one more pic and then drop your phone to see if she'll continue without it."
    "She lovingly kisses your cock all over while looking you right in the eyes."
    scene giannanet19
    y "Yeah, that's it, Gianna, now suck on it."
    "You confidently pull her head forward and she doesn't resist at all."
    y "You're eyes look beautiful."
    scene giannanet20
    "Gianna continues sucking your cock."
    "The part of you that was angry at her for doing a 180 on your friendship and then taking advantage of your money to come on this trip takes a back seat in your mind."
    "After all, it's pretty hard to feel like you're being used when she's the one on her knees sucking your cock at the beach."
    scene giannanet21
    y "Put your arms behind your back Gianna."
    "She immediately obeys.  Yeah, you definitely don't feel like you're the one being used."
    scene giannanet22
    "You pull her deeper as the angry part of your mind puts one more idea in your head."
    "You think about how right now you could come in her mouth and then tell her to leave and find her own way back to the mainland U.S."
    "Then she'd be the one who'd been used and you'd have full revenge for her wanting to ditch you just a week ago."
    scene giannanet21
    "But that's not who you are.  You're better than that.  You're willing to forgive and give people a second chance as long as they're willing to change."
    y "I'm cumming Gianna."
    scene giannanet23
    "You cum all over her face and pick your phone back up to snap one last picture to remember this by."
    y "Wow, that was amazing!"
    g "Glad you liked it!  That was the hottest thing I ever did!"
    scene giannanet24
    y "Isn't this the part where the girl reminds the guy not to show the pics to anyone or post them online?"
    g "If you were the kind of guy who I thought needed a reminder like that I wouldn't have done this at all."
    g "I trust you [y]."
    y "C'mon, let's go wash off that sand."
    $ renpy.end_replay()
    jump prejetski

label sandymorningb:
    scene day2morning1
    "The next morning shortly after waking up you find yourself at your computer with a hot coffee."
    "You think back to the amazing night before."
    "It was so much fun dancing with the girls.  There will definitely have to be more of that when you guys have the drinking party later."
    "Let's see them keep Emily's modesty intact when they are all drunk!"
    scene hawaiiworking1
    "It was great having Emily and Kendra grind on you too.  First Kendra with her suit slid to the side and then Emily with you completely naked."
    "Each time there was just a thin layer of fabric between you and them."
    "And the video of Katrina and Gianna... WOW!  You'll definitely be watching that again soon!"
    scene gmorningwoj
    g "Hey [y]!  Good morning!"
    y "Good morning Gianna!  Are you going jogging again?"
    g "Yeah, and if you wanted to join me I was thinking we could drag the volleyball net down to the beach and set it up for later."
    g "Also I've got my bikini on so we could swim over to the next cove over if you want."
    y "Sounds great!  I'd love to join you.  Give me a sec to get ready."
    scene giannanet1b
    y "Holy shit, I didn't think this was going to be an Olympic regulation net!"
    g "Yeah that thing is heavy!"
    y "We'll have to play when the tide is out, or else the team on the other side is going to have a serious handicap!"
    scene giannanet2
    g "Hey, so I also wanted you to come down here with me because I wanted to talk about last night.  Did you find anything on your computer?"
    y "Yeah, that video you took with Katrina was really hot!"
    g "So you're not like mad or anything?  The pics we took before were meant to be sexy and fun for you, but I wasn't sure if the video crossed a line."
    scene giannanet1b
    y "Of course I'm not mad.  Seeing the two of you have sex was the hottest thing ever!  I hope I can be there next time and join in!"
    g "I didn't go into your room thinking it would go that far, but Katrina just kind of took control and everything felt so right."
    y "Yeah she can be that way.  Oh, and I have your bracelet and rings in my room.  Do you want them back?"
    g "No, well maybe after the trip, but Katrina said you should have them for now."
    scene giannanet3
    g "I'm glad we got this out in the open and you're not upset.  Now let's do some jogging!  You're gonna have to build up your endurance if you want to take me and Katrina on at the same time!"
    y "You got that right!"
    scene giannanet4b
    "After your jog and a brief swim over to the next cove, you head back."
    "The next cove over was a public beach, but since it's still early in the day there weren't that many people, just a few locals."
    y "It might be fun to check that out again later with everyone, maybe a little later in the day."
    g "What do you want to do now?  Lay in the sun and dry off or maybe head back?"
    y "How about a little volleyball while we dry off?"
    scene giannanet7
    y "Ok, let's see what you got Gianna!"
    g "Bring it on [y]!  I'm pumped to play!  You remember I played volleyball in high school right?"
    scene giannanet8
    y "Of course!  You guys won the county right?"
    g "Yeah one year we did, but you might be remembering the field hockey team I was on with Kendra.  We won the county every year and even the state when we were seniors."
    y "Yeah, thanks to me cheering you guys on in the bleachers with Emily and Katrina!"
    scene giannanet9
    g "You guys were always so supportive!  I always really liked that about you."
    g "And you're proving to be really good at volleyball!  It's a shame our school didn't have a boys team."
    y "I did pretty well in gym class when we played, and being a little taller than average helps too."
    y "My favorite thing in volleyball is actually blocking spikes.  I like it even more than spiking the ball myself."
    scene giannanet7
    g "Me too!  Like there is this instant where your opponent's eyes go wide, just as they realize you've stopped them."
    g "Another thing I like is diving for the ball and keeping it just barely in play."
    scene giannanet10
    y "You mean like this?"
    "You bump the ball towards the sideline just out of reach and Gianna dives for it."
    "The shifting sand makes for bad footing though so she doesn't quite get there in time."
    scene giannanet11
    g "Ha, no not like that!  If that was a gym floor I think I'd have made it though!"
    g "Now I'm covered with sand instead and you scored."
    scene giannanet12
    y "I actually do feel like I scored!  I gotta say you look really really good right now."
    g "You look really good too [y]."
    y "I think I might like you better covered in sand than I do seeing you wet."
    y "Stay there a sec, I want a picture of this on my phone."
    g "Ok, but I don't see how it could compete with the video from last night."
    "You retrieve your phone and take a pic."
    y "You'd be surprised.  The sand and the wet hair and the ocean behind you make this a pretty damn sexy pic!"
    y "Hell even the volleyball looks sexy!"
    g "Haha, don't go falling for Wilson instead of me!"
    y "Heh, not a chance!  Now let's head back and get some lunch and see what Katrina has planned for everyone today."
    jump prejetski


label prejetski:
    scene prejetski1
    k "Did you guys have a good jog at the beach?"
    y "Yeah!  We also swam over to the next cove.  It's a public beach, but hardly anyone was there yet."
    e "Probably too early in the morning."
    scene prejetski3
    kat "Maybe we could check it out later.  If we talk to some locals we might find out some more cool stuff to do around here!"
    k "What do you think [y]?"
    y "I guess, you want to do that after lunch?"
    scene prejetski2
    kat "It would have to be another day.  This afternoon we are going jet skiing at Lagoon Resort."
    e "Wow, that sounds like fun!"
    kat "Everyone grab a quick lunch and get ready to go.  It's a bit of a drive and we're due there in a little under two hours."
    jump emilyshower1


label emilyshower1:
    scene upcoming2
    "Shortly after lunch, you're in the shower getting ready to head to the jet ski place when you hear the door open and close."
    $ cosplay = False
    $ pickupemily = False
    y "Is someone there?"
    scene showerscene1
    e "It's Emily.  Don't turn around ok?"
    y "You're naked aren't you?"
    e "Yes, and if you're a good boy and keep your back to me I'll get in the shower with you."
    e "I told you last night I was waiting for the perfect moment to ambush you, and now here it is!"
    scene showerscene2
    e "I wanted to talk to you about an idea I had for my channel."
    e "Giving away in codes for in-game currency is great don't get me wrong, but what if we made some item you could only get by subscribing to me on Twitch?"
    e "Remember I told everyone when I get back I'd do a cosplay?  What if we make it a sorceress outfit if they subscribe and then I cosplay wearing it as part of the announcement?"
    e "That sounds so perfect right [y]?  If you agree I could maybe let you turn around right now."
    e "Later I'll do a private modeling session of the cosplay for you too.  What do you think?"
    menu:
        "Yeah, that does sound like a great way to build your channel, I'd love to help![Gr] \[May lead to Cosplay scenes in future updates\]":
            jump cosplayyes
        "No, you're not taking advantage of me like this![Gr] \[+1 Confidence\]":
            jump cosplayno
label cosplayyes:
    scene showerscene16
    "She said she {i}might{/i} let you turn around, so you turn around before she can change her mind."
    $ cosplay = True
    e "I take it this is a yes then?"
    y "Yeah, that does sound like a great way to build your channel!  I'd love to help!"
    e "That's great [y]!  I'm going to have like ten times as many subscribers!  Maybe even more than that!"
    e "We'll need to design something really awesome!  Something that you can program in and we can also have made in real life."
    scene showerscene17
    e "So was it worth the wait to see me naked?"
    e "You don't have to answer, this guy is telling me all I need to know."
    e "You're pretty big by the way [y]!"
    e "I'd love to stay, but I need to go tweet out some cryptic teaser about the sorceress outfit before we leave."
    e "So exciting!  You're helping me sooooo much!  You have no idea how grateful I am!"
    scene showerscene18
    e "Ambush successful!"
    e "Look forward to the private cosplay [y].  I'll be going all out for you!"
    jump lilo
label cosplayno:
    scene showerscene2
    "Emily asking for more favors makes something snap inside your head."
    $ pickupemily = True
    $ confidence += 1
    y "Before I answer, I want you to close your eyes too."
    e "But then I won't know if you're looking at me or not."
    y "That's what makes it hot though Emily, the risk...."
    scene showerscene3
    "Of course you open your eyes as soon as she closes hers.  You're too pissed not to."
    y "When I told you all about the success of my game I didn't expect you to try to take advantage of me."
    y "I'm trying to get over the anger and betrayal I felt after learning you guys were ready to abandon me the night at the cafe."
    e "[y] I...."
    scene showerscene5
    y "Shut up Emily!  The answer is NO!  You will not be getting any more special favors until we repair our relationship!"
    y "I gave you $2,500 towards your channel already.  I gave you a first-class plane ticket.  I gave you a trip to Hawaii."
    y "You didn't even play my game before it was successful! Yet I was willing to forgive all of this because I'm your friend."
    scene showerscene4
    y "But now here you are in the shower of all places.  Trying to catch me when I'm most vulnerable to ask for more!"
    y "You will not be taking advantage of me anymore!"
    scene showerscene6
    e "Oh god, what am I doing?  You're right, this isn't me."
    e "[y] I'll change!  I'll take a break from streaming!  Tell me what I can do to make this right?"
    y "This just goes back to the golden rule Emily.  Treat me the way you want to be treated."
    e "I'll try harder.  I've felt a little like I was slowly drowning as my viewers declined."
    scene showerscene4
    e "Then you came along like a lifeguard with your game and your success and instead of letting you help me on your own terms I grabbed you and pushed you under to get out faster."
    e "I'm so so sorry.  This is not who I want to be.  Do you think I should quit being a streamer?"
    y "No, I don't want you to give up on your dreams.  It's ok for friends to lean on each other for support, just don't take it too far ever again."
    scene showerscene3
    "You take a step back, feeling your anger subside now that your feelings are out in the open."
    e "I'm glad we had this talk, even if it is extra awkward since we're in the shower with our eyes closed."
    e "You still have your eyes closed right?"
    "You don't answer."
    scene showerscene7
    e "Can I confess something?  I'm actually really turned on right now.  You are right that not knowing if you are looking at me makes this hot."
    e "Now that everything is out in the open, do you think maybe we could kiss and make up?  I think if we don't I'll wonder all day if you're still mad at me."
    scene showerscene9
    "You lean in and kiss Emily."
    "You realize how tense your muscles had been and you start to relax."
    "Still a little angry though you decide you're going to do one more thing before you completely forgive her."
    scene showerscene10
    "You grab her and lift her up against the wall and start eating her pussy."
    e "Oh god [y]!  Oh god!"
    e "That feels so good!  I need this so bad!  Did you know it would get me this hot when you made me close my eyes?"
    scene showerscene11
    e "Don't slip though!  The floor is wet and a broken bone would kill the mood!"
    y "Don't worry, I have big feet!"
    e "It tickles when you talk with your lips up against me like this.  In a good way!"
    scene showerscene12
    e "I'm gonna cum soon [y]!"
    "You swirl your tongue all over her clit."
    e "I'm cumming!  I'm cummmmmmmmmmming!!!"
    scene showerscene13
    "You risk a glance up after Emily calms down from her orgasm."
    "Uh oh, she makes eye contact.  You're busted!"
    scene showerscene14
    e "We definitely have to do this again sometime!"
    e "I can't believe how hot this was!  I guess it counts as makeup sex too right?"
    y "Yeah I guess it does.  I definitely feel like we made up."
    scene showerscene15
    "You carefully put Emily back down."
    e "So we're good now right [y]?  I'll be really careful in the future not to let my ambitions as a streamer get in the way of our friendship."
    y "Yeah we're good Emily.  Let's use the rest of this vacation to enjoy our friendship.  You've got the best jokes of all the girls after all!"
    e "Thanks [y]!  Let's go meet up with the others."
    $ renpy.end_replay()
    jump lilo

label lilo:
    scene lilo1
    "It's almost time to go, so you look for everyone and find them in the T.V. room."
    kat "We are just watching this great Hawaiian documentary while we finish up getting ready."
    y "{i}Lilo and Stitch{/i}! This was one of my favorites growing up!"
    k "We were flipping through the stations and couldn't resist watching something that takes place in Hawaii!"
    g "Seeing David juggling the torches makes me excited for when we go to our own luau!"
    scene lilo2
    kat "Do you think we could distract someone and make them drop their torch like they did in the movie?"
    y "I think you have a better shot of seeing an alien!"
    k "The thing I am looking forward to at the luau is getting laid!"
    kat "Kendra!"
    k "What?  I want them to put the flower necklace on me like they do in the movies!  They're called leis right?"
    jump lagoonresort


label lagoonresort:
    scene lagoon1
    y "Wow this place is nice Katrina!"
    kat "Glad you like it!  They do all kinds of stuff here.  Helicopter tours, boat tours, scuba diving, the jet skiing we're doing today."
    kat "They even have underwater hotel rooms if you stay overnight!"
    e "Wow really?"
    scene lagoon2
    define alii = Character("Alii", color="#ffc0cb")
    alii "Hello and welcome to Lagoon Resort!  My name is Alii and I'll be helping you today."
    kat "Hi, we've booked a jet ski excursion under the name [y] for this afternoon."
    alii "Ah yes, you're actually our only group today."
    k "I'm surprised this place isn't busier."
    scene lagoon3
    alii "Well the COVID quarantine ended and we didn't end up with any cases this far out from Honolulu, but still business hasn't really picked back up yet."
    alii "A couple weeks ago though someone said they saw a Killer Whale though, so I'm hoping someone can get a picture of it."
    g "There's no way a Killer Whale was off the coast of Oahu."
    alii "Wow, do you know about whales?"
    alii "You're right though, what they probably saw was a Pseudorca Crassidens or {i}false killer whale{/i}.  They are extremely rare and usually only spotted near Maui."
    alii "If someone were to get a picture of one here we'd have scientists and animal enthusiasts booking our rooms, so I'm letting everyone know about a contest we have going on."
    alii "Any guest who gets a picture of a Pseudorca Crassidens gets a free night stay and a free helicopter tour for two."
    scene lagoon2
    g "That's cool!  I hope we see one!  I can point out the difference to my friends if we see the more common Humpback Whale first."
    k "I didn't know you knew about whales Gianna."
    g "Going to aquariums was a hobby of my parents, and I guess it's become a hobby of mine as well."
    e "I didn't know that about you either.  When we get back maybe we can all go together."
    g "Sure!"
    scene lagoon3
    alii "If you stay long enough you will definitely see Humpback Whales today."
    alii "Around this time of year, not a day goes by where I don't see at least one."
    alii "I see you're booked for a boat tour later this week as well, so if you don't see one I'll take you to a spot where I know they'll be."
    k "You captain the boat?"
    alii "Yeah I run this place with my parents.  My dad does the helicopter tours and I alternate with my mom with the boat and hotel duties."
    alii "Anyway, head around behind me to the elevator and you can change and find your life vests in room four."
    scene lagoon4
    e "I didn't even know underwater hotel rooms were a thing!"
    k "It's like a whole new world!"
    y "That's Princess Jasmine!  I think you were trying to go for Ariel!"
    g "How much would staying in a room like this even cost?"
    kat "Whatever you are thinking, it's way more.  Way more than even renting the beach house."
    e "Didn't you say they do scuba diving here?  Couldn't someone swim up to the window and look in if I was naked?"
    kat "Haha, I guess they could my little exhibitionist!"
    k "Let's get changed.  [y] could you face the window for a sec?"
    scene lagoon5
    "You throw on your life vest and Emily lingers for a moment."
    e "Winning a night here would be amazing [y].  You and me, laying on this bed together, wondering if a diver was out there seeing everything..."
    y "I could just buy us a night here."
    e "What?!  I can't believe you just said that!  That's pay-to-win!  We're true gamers [y]!  We're getting a picture of that whale!"
    y "You're right Emily, I'm still getting used to having money.  It's the challenge that makes it fun!  I'm gonna have to brush my teeth after suggesting we pay, my mouth feels dirty!"
    e "I'll forgive you this once!  Now don't turn around while I change with the girls!"
    scene lagoon6
    "You look out into the ocean.  The reef is really cool, but you wonder if the room lights scare off the fish."
    "You take a moment to squint to see if you can see a reflection of the girls changing, but the thick glass isn't very reflective."
    scene lagoon7
    "You try imagining what your room would look like to a scuba diver from the outside."
    y "Wow, I think I understand why Emily is so excited.  It would be pretty hot."
    kat "What was that [y]?"
    y "Nothing, just muttering to myself."
    scene lagoon8
    alii "So has anyone here used a jet ski before?"
    k "Yes, [y] and I went camping with our families at a lake and did it there before."
    alii "Great, so you can help the others if they get stuck out there.  And does everyone know how to swim?"
    g "Yeah, Kendra has a pool and we've been swimming with her for years.  All of us are very strong swimmers."
    alii "Super, though still wear the life vests we've provided when you're out there."
    "Alii goes over the basics of operating a jet ski with a focus on safety."
    alii "Now everyone pick a jet ski and have fun out there!"
    e "I call the purple one!"
    scene lagoon9
    "Kendra leaps off the dock directly onto the jet ski as Emily reaches the ladder to climb down."
    e "Kendra!"
    k "You got the swing chair at movie night.  The purple jet ski is mine!"
    scene lagoon10
    e "KENDRA!!!"
    k "See ya later sucker!"
    scene lagoon11
    y "Guys, line up next to me and let's race!"
    g "We haven't had enough practice yet and you and Kendra said you did this before."
    y "That makes it my best chance to win!"
    k "Racing is the best thing you can do on these things.  We even did a tournament back at the lake to see who was grand jet ski champion."
    y "Remind me who won that Kendra."
    k "Ok ok, it was you [y].  You beat my dad in the final round.  He's super competitive and was stewing about it for weeks afterward."
    y "That must be why he invited us camping at the lake again just a month later.  Too bad my parents suggested a family barbeque instead!"
    e "Times up, let's do this!"
    scene lagoon12
    "Emily tries to take off, but instantly falls to last place."
    "You and Kendra pull out to an early lead."
    e "I KNEW THE PURPLE ONE WOULD BE FASTEST!"
    k "So did I!"
    y "First one to circle the resort twice wins!"
    scene lagoon13
    "It doesn't take long for you, Kendra, and Gianna to build a big lead."
    k "C'mon slowpokes, catch up!"
    kat "Damn it, I'm usually really good at whatever I try to do!"
    kat "Wait up Emily, I don't wanna be last!"
    scene lagoon14
    e "Hey guys, it looks like there's a bar up there!  Aren't races supposed to have pit stops?"
    kat "I'm with you!  Let's get Alii to serve up some Mai Tai's!"
    g "No drinking and driving!  And no stopping when I've almost caught up to Kendra and [y]!"
    scene lagoon15
    y "One lap down, one to go!  I'll beat you just like I beat your dad!"
    k "Hello, my name is Inigo Montoya, you killed my father, prepare to die!"
    "Kendra laughs and stands up leaning forward to try to coax a little more speed out of her jet ski."
    scene lagoon16
    "As you arrive at the finish line you notice there is a bit of a wake coming off the dock."
    "You pull back on the handles and jump it, using the momentum to just get a little ahead."
    k "I'M SORRY DADDY!!!!"
    scene lagoon15
    k "You're just too good at this [y], I don't understand!"
    "You hear Emily's voice in the distance."
    e "It's all the Wave Race 64 he played on Nintendo!"
    y "Man, I miss that game!  I might have to hook up my Nintendo 64 again sometime!"
    scene lagoon12
    "You spend the next hour racing around having fun."
    "The views are spectacular and you are pretty excited to come back here later this week for a boat tour of Oahu."
    "One day of fun, one day of education.  Katrina really is skilled at planning things.  That's a great way to feel like you got the most out of a trip like this."
    scene lagoon17
    e "Any sight of that false killer whale yet?"
    y "No, nothing yet.  Maybe all our yelling and laughing is keeping the whales away."
    e "Let's try quietly going a little further out."
    scene lagoon18
    e "Dang, I still don't see anything yet.  I really want to win a night here and maybe come back on the last day just the two of us, my treat!"
    y "That does sound pretty fun, but I still don't see anything yet."
    e "Me neither, got any more ideas [y]?"
    y "We could go back and climb up to the helicopter pad for a bird's eye view."
    e "That's brilliant!  Let's go!"
    scene lagoon20
    y "You know how to fly that thing Trinity?"
    e "Not yet."
    scene lagoon21
    e "Tank, I'm gonna need a pilot program for an N5766 helicopter."
    y "Haha, too bad it's not as easy at it is in the Matrix."
    scene lagoon22
    e "Hey guys, any whales down there?"
    g "Are you calling us fat?"
    e "You know what I mean Gianna!"
    g "No nothing, we're just getting some sun and relaxing."
    scene lagoon19
    y "Hey Emily, over here I think I see something."
    e "Where where where?"
    y "Over there, look, he's poking his head out."
    scene whale1
    e "Oh my god, we're going to win!  I'm getting a picture now!"
    y "I'm not sure, it doesn't look much like a killer whale."
    scene whale2
    e "Shit you're right.  That looks like a Humpback Whale Gianna described."
    e "It's almost time for us to leave for the day too."
    y "Well we're coming back later this week for the tour.  You'll get another chance."
    e "I'll check the boardwalk shops for someplace that sells binoculars when we get back."
    y "Maybe there's some device we can put under the water to make whale calls."
    e "Let's check with Alii."
    scene lagoon2
    alii "Thanks for visiting Lagoon Resort today.  I hope you all had a great time!"
    e "Alii, we didn't find a false killer whale today, but when we come back later this week we want to try again."
    y "Yeah, is there some device we could use to make whale calls underwater?"
    alii "Sure, you could play the sounds into a hydrophone.  We actually have one you could use.  Just find the whale sounds on youtube you want to try."
    e "Awesome!  See you later this week then!"
    scene lagoon3
    alii "Bye guys!  Have a great day and I'm looking forward to being your captain in a couple days!"
    scene hawaiiworking1
    "After you get back you find yourself with a little free time, so you check up on your game."
    "There is a knock at the door."
    define m = Character("Maid", color="#ffff00")
    define r = Character("Rachel", color="#ffff00")
    m "Housekeeping!"
    scene maid1
    "You open the door and let a maid in."
    m "Hi, my name is Rachel and I work for the housekeeping company that takes care of this house."
    r "Do you mind if I clean the bathroom really quick?"
    y "I'm [y].  You must be the one who puts the rose petals in the tub."
    r "Yep!  That would be me!"
    y "You don't have to do it if you don't want to.  I'm not exactly used to that kind of treatment."
    r "That's nice of you, but I do have to do it as part of my job.  Don't worry though, it's really no trouble."
    y "So you just go around Honolulu cleaning houses all day?"
    r "Well I always wanted to live in Hawaii, so being a maid is a small price to pay.  All the jobs around here that I could get are service industry types."
    scene maid2
    r "And I just work four days a week, and I'm off after this.  I always clean this house last since there is a nice beach nearby I like to visit in the evenings."
    y "That must be the next cove over.  I swam over there this morning."
    r "Yeah, that's the one!  Right next to the private beach you guys have."
    y "Maybe I'll see you over there sometime.  We were talking about visiting that beach one evening to hang out with some locals."
    r "Cool!  Yeah, I hope I see you there!"
    r "By the way, I noticed you're a little younger than the average guy who rents this house."
    "You decide not to tell her about your money so that she treats you like a regular guy."
    y "Yeah, I won the grand prize in a radio contest.  They still hit me with taxes though, so I'll have to work extra shifts to make it up when I get back."
    r "Wow, that's so lucky!  Well, I better get back to work.  Nice meeting you [y]!"
    scene hawaiiworking1
    "Rachel goes to clean the bathroom and you get back to work."
    "It's been pretty fortunate there haven't been any major problems this week."
    y "Working remotely has actually been easier than I thought."
    scene katrinaalcohol1
    kat "Hey [y]!  I was thinking we'd have your drinking party tonight.  I'm heading into town to pick up the alcohol."
    define kaw = Character("Kawika", color="#ffc0cb")
    kat "Do you wanna tag along?"
    menu:
        "Go ahead without me, I'm going to get some work done on my game":
            jump workingremotely
        "Sure, I'll be right down[Gr] \[+1 Katrina\]":
            jump katrinaalcohol
label workingremotely:
    scene katrinaalcohol1
    y "Sorry Katrina, I was actually thinking about how nice working remotely is.  I'd like to keep at it for now."
    kat "Sure [y]!  I'll see if Emily wants to go.  Maybe we'll stop and get her the binoculars she was talking about."
    y "Yeah she'll like that.  See you later!"
    kat "See ya!  Hope you get a lot done!"
    scene hawaiiworking1
    "You return to work and begin outlining the initial plans for an expansion that takes place on a tropical island."
    scene hawaiiworking2
    "After awhile Kendra comes out and sits down with her phone."
    y "Kendra, what are you wearing?"
    scene hawaiiworking3
    k "Hey up there [y]!  It's my sexy lingerie!  I just put my bikini and slingshot in the wash and this is the next closest thing I had."
    k "It kind of looks like a one-piece swimsuit a little right?"
    y "Yeah I guess it does."
    k "You're working up there, right?  Is it gonna bother you if I chill here by the pool?"
    y "Ha!  It might distract me a little, but it definitely won't bother me!"
    scene hawaiiworking4
    "Kendra gets comfortable and you get back to work."
    y "Yeah working remotely is the best!"
    jump party1
label katrinaalcohol:
    scene katrinaalcohol2
    $ katrina += 1
    $ katrinastare = True
    kat "This is the place.  Apparently, this old Hawaiian guy makes the strongest stuff around and sells it on the sly out of his bar."
    "In front of you is the largest Hawaiian man you've ever seen.  Maybe the largest man period!"
    "His Hawaiian shirt doesn't go very far towards making him look less intimidating."
    kat "Sit down for a sec while I handle this.  The girl at the shop said he doesn't sell to just anyone."
    scene katrinaalcohol3
    kat "Hey, my name is Katrina and this is [y].  How's it going?"
    kaw "Welcome to my bar guys, I'm called Kawika.  You have some nice tattoos.  A few of them look Hawaiian."
    kat "They're not, but that's kind of you to say."
    kaw "What can I get for you guys?"
    kat "I heard you make something called Oahu Overwhelm.  I was hoping we could get a bottle."
    kaw "Who told you about that?"
    kat "A girl in a shop down at the boardwalk."
    kaw "That must have been Makaio.  You must have been very persuasive to get her to tell you about Oahu Overwhelm."
    scene katrinaalcohol4
    kat "What can {i}you{/i} tell me about Oahu Overwhelm?"
    kaw "It's not like anything on the mainland.  I guess the closest thing would be absinthe.  The ingredients aren't the same, but the effect is a little similar."
    kaw "I named it Oahu Overwhelm because it overwhelms the inhibitions and sensibility of many people who drink it."
    kaw "It's almost like it can get in your head and make you do things you normally wouldn't."
    scene katrinaalcohol3
    kat "Sounds like I have a lot in common with this drink."
    kaw "What do you mean?"
    kat "Just that I like getting in people's heads too and getting them to do what I want.  Is that how it affects you?"
    kaw "At first, but not anymore.  I've built up the strength of will to mitigate the effect, ha, or maybe I've just built up enough alcohol resistance."
    kaw "I do own a bar after all!"
    scene katrinaalcohol4
    kat "Well you've convinced me, we'll take a bottle."
    kaw "I'm not trying to convince you to buy it, I'm trying to convince you not to buy it.  I don't want to get in trouble if you guys do something crazy under the effects."
    scene katrinaalcohol5
    kat "We'll be drinking it at our beach house, not going crazy with it in town and getting arrested!"
    kat "Also I didn't say anything about buying it.  I said I'd take a bottle."
    kaw "You want me to give you a bottle for free?"
    kat "How about a game?  I told you I have a lot in common with your famous drink."
    kaw "What kind of game?"
    scene katrinaalcohol3
    kat "Just a simple staring contest.  I'll come around the bar and whoever turns away first loses."
    kat "If I win I get the bottle."
    kaw "If I win you buy it for double price, and you get a Hawaiian tattoo."
    kat "Deal, I was thinking of getting one anyway."
    kaw "You take those sunglasses off.  They give you an unfair advantage."
    scene katrinaalcohol6
    "Katrina comes around the bar."
    kat "Actually my sunglasses would give you an advantage."
    "Katrina begins staring down the big bartender.  He towers over her, but somehow she seems more threatening than him."
    "After a moment you get a distinct impression that he wants to take a step backward.  You're not sure how you know this, but yet you're certain of it."
    scene katrinaalcohol7
    "Another few seconds pass and he closes his eyes and turns away."
    kat "Good game!  You actually lasted a lot longer than I expected.  Maybe drinking your Oahu Overwhelm really did help you somehow."
    scene katrinaalcohol8
    kat "This is it here right?"
    kat "Oh not talking again yet?  Well, it's the only bottle here without a label.  Pretty much a dead giveaway."
    scene katrinaalcohol9
    kat "Ok [y] ready to go?"
    y "How did you do that Katrina?"
    kat "The eye trick?  It's not magic or anything if that's what it seems like."
    y "What is it?"
    kat "Let me see, how to describe it.... Well, you have to make yourself wonderful and terrible to look at at the same time."
    kat "And then you try to guess what the other person is thinking about.  People sometimes think of off the wall things even when they are looking you in the eyes."
    kat "Once you know what they are thinking about there is kind of a moment where you can almost superimpose your thoughts over theirs."
    kat "Like I said, it's hard to describe, but you'll see what I mean if you practice."
    y "I could learn to do it?"
    kat "Yeah, do you want to try right now?"
    menu:
        "No, this is pretty cool, but I think I want to practice on a little easier of an opponent first":
            jump starelater
        "Yeah, I need to see this for myself.[Gr] \[+1 Katrina Dominance\]":
            jump staringcontest1
label starelater:
    scene katrinaalcohol9
    y "I think I better practice on someone else first."
    k "Ok, suit yourself.  Ready to go then?"
    scene katrinaalcohol17
    k "Hey wanna hear an Emily joke?"
    y "Yeah what would she say right now?"
    k "Bartender.exe is not responding!"
    y "Haha, you're totally right, she'd definitely say something like that!"
    jump party1
label staringcontest1:
    y "Yeah, let's try it.  There was a moment back there where I swear it was like I was reading his thoughts when it suddenly seemed like he wanted to step backward."
    $ katdom += 1
    $ lostkatrinastare = True
    k "You're on the right track!  It's not what he was thinking at first, but that was part of me superimposing my own thoughts on him after I kind of locked on."
    y "You're sure this isn't magic."
    k "No, not at all.  You should have majored in Psychology with me.  There's so much cool stuff like this to learn."
    scene katrinaalcohol10
    "Katrina turns towards you and you begin."
    "You try to think about whatever she might be thinking about."
    "Normally her hair slightly covers one eye, but right now she has it brushed more to the side."
    "And those little star tattoos next to her eyes.  You wonder if that has something to do with looking wonderful and terrible at the same time."
    "You realize your mind is wandering and you were supposed to think about what she might be thinking about, but it's too late."
    scene katrinaalcohol11
    "A moment later you find yourself down on your knees staring at her feet."
    k "That was a pretty good try [y]!  I win though!"
    if katdom == 1:
        jump dom0
    if katdom == 2:
        jump dom1
    if katdom == 3:
        jump dom2
label dom0:
    scene katrinaalcohol13
    kat "Now kiss my hand and stand up."
    "She puts out her hand and you kiss it."
    y "I feel a little groggy.  Like I just woke up."
    scene katrinaalcohol16
    y "That's a really cool trick though.  I hope I can learn it!."
    kat "Keep practicing and you can.  If you want a rematch just let me know!"
    "You look over at the bartender, half expecting him to tease you about losing too, but he doesn't say anything."
    scene katrinaalcohol17
    k "Hey wanna hear an Emily joke?"
    y "Yeah what would she say right now?"
    k "Bartender.exe is not responding!"
    y "Haha, you're totally right, she'd definitely say something like that!"
    jump party1
label dom1:
    scene katrinaalcohol11
    kat "Put your hands behind your back and kiss my hand."
    scene katrinaalcohol12
    kat "Yeah just like that.  I love seeing you like this."
    kat "Just think of what I might make you do if we have a rematch later."
    Kat "Ask me for another round anytime if you want to find out...."
    scene katrinaalcohol16
    y "I feel a little groggy.  Like I just woke up."
    "You look over at the bartender, half expecting him to tease you about losing too, but he doesn't say anything."
    scene katrinaalcohol17
    kat "Hey wanna hear an Emily joke?"
    y "Yeah what would she say right now?"
    kat "Bartender.exe is not responding!"
    y "Haha, you're totally right, she'd definitely say something like that!"
    jump party1
label dom2:
    scene katrinaalcohol11
    kat "Looks like I have you on your knees again [y].  I'm starting to think you like it!"
    scene katrinaalcohol14
    "She puts her foot on your chest and gently pushes you back.  It doesn't feel like you have the strength to resist."
    kat "It's kind of addicting seeing you down there.  The more I see it the more I want to see it."
    kat "Hmmm, let's see, what should I order you to do for losing?"
    kat "I know, kiss my foot [y]!"
    scene katrinaalcohol15
    "You immediately move forward to obey."
    kat "This is nice.  Maybe next time I'll have you suck on my toes.  Not here though, a customer might walk in."
    scene katrinaalcohol16
    y "I feel a little groggy.  Like I just woke up."
    "You look over at the bartender, half expecting him to tease you about losing too, but he doesn't say anything."
    scene katrinaalcohol17
    kat "Hey wanna hear an Emily joke?"
    y "Yeah what would she say right now?"
    kat "Bartender.exe is not responding!"
    y "Haha, you're totally right, she'd definitely say something like that!"
    jump party1
label party1:
    scene party1
    g "What do you think [y]?  This is the lingerie we picked out for your drinking party tonight!"
    k "If you hadn't already seen me in this I think I'd have needed a shot before we let you down here."
    e "[y], they got me the tiniest outfit, just like they did with the swimsuit!"
    y "I've actually seen Katrina's outfit too, back in my office before we came here."
    kat "Hey, that was a secret!"
    k "You mean he already saw you wearing this, and on movie night you let me be the only one in lingerie when you secretly had that outfit here?"
    k "You'll have some explaining to do later missy!"
    scene party2
    e "Let's get this party started!"
    "Emily hooks her phone up to her computer speakers and puts on a party mix."
    g "Shots shots shots!"
    y "To Hawaii and to friendship!"
    all "Here here!"
    scene party3
    "The first shots hit hard.  Within a few minutes, you are all feeling great!"
    g "Watch out!  I'm gonna try to jump over this couch!"
    kat "C'mon Gianna, let's play some pool!"
    scene party4
    kat "I'm gonna hit this white ball at this other white ball!"
    y "That's the cue ball Katrina.  And why are there two of them?"
    kat "BECAUSE IT'S A TWO PLAYER GAME, HAHAHAHAHAHAHA!"
    scene party5
    g "Katrina, hit it under me!  I need to do a few yoga poses really quick and build my flexibility for [y]!"
    g "No time to lose!  Who wants to hear the benefits of yoga!  Gather around everyone and I'll teach you!"
    scene party6
    e "Yoga is lame Gianna, dance with me instead!  This seems like the perfect place!  Surrounded by balls!"
    k "That's it [y], just aim a little more to the left!  You can jump the ball over her toes!"
    kat "Is it my turn next?  I've been staring at this table for like an entire minute, but I can't find the 8-ball.  Where is it?"
    k "Haha, it's like literally in the center of the table Kat!"
    kat "It's Katrina, you know I don't like being called Kat."
    g "Tonight it's Kat!  Kat Kat Kat!"
    kat "Fine, just for tonight though!  Meeeeeeoooooooowwwww!"
    scene party7
    k "Hey everyone look!  I got Emily's glasses!"
    k "I'M GONNA BE A STREAMER NOW!  [y] how do I stream your game?"
    scene party8
    e "Hey give me back my glasses Kendra!"
    k "Looks like we have a new subscriber!  Thanks, Emily!  You're my first of the day!  Nine more and we'll hit our first subgoal!"
    y "Ummm, I see the monitor but where is the actual computer case?"
    scene party9
    k "Oh we have a question in the chat from user [y]."
    k "The answer is that it's under the table!  Don't tell me you can't see it.  Wow that's just like Kat not seeing the 8-ball!"
    e "C'mon Kendra, pleeeeeeaaase give 'em back?"
    k "Ok everyone, that's the end of the stream, don't forget to click like and subscribe.  And ring that notification bell so you know when I go live again!"
    e "That's YouTube, not Twitch!"
    scene party10
    g "Sit there [y], we're gonna have a pillow fight!"
    k "That's every guy's dream right?  Seeing half-naked girls having a pillow fight?"
    y "Did I really miss this kind of thing back in high school?"
    kat "Oh for sure!  We always had naked pillow fights at every party right Emily?"
    e "Right Kat, at sleepovers too!  It's like the first thing girls do whenever they get drunk!"
    y "Wait, is this sarcasm?  My brain tells me it is but the drink tells me it isn't!"
    scene party11
    e "It's over Anakin!  I have the high ground!"
    k "Let's get her guys!"
    g "You may have the high ground, but I have the element of surprise!"
    scene party12
    k "Haha, you're losing your top!"
    e "[y]!  The force is strong with this one.  I need your help!"
    scene party13
    y "I'll save you Emily!"
    k "This is what rolling a natural 20 looks like!  Critical hit!  Your top is gone forever!"
    scene party14
    y "You cannot win against such overwhelming odds!"
    e "Eat my pillow, Kendra!"
    k "Stop stop! I give up!"
    scene party15
    e "My turn to roll a natural 20, and my target is prone so I get a bonus!"
    "Emily whips the front of Kendra's lingerie open."
    e "Agree to a loser's penalty and I'll let you up!"
    k "Fine fine, anything!  But you did all team up on me!"
    e "Kendra's penalty is.... naked dancing!"
    kat "I second that!"
    g "I third it!"
    scene party16
    k "I need another shot if I'm going to get naked."
    y "You don't actually have to Kendra."
    kat "Stop being such a nice guy all the time [y] or I'm getting you a toxic bikini too!"
    kat "This is why I gave it to her.  To help her in situations like this."
    k "Yeah it's ok [y].  I want to.  Just let me take another shot to build up my confidence!"
    scene party17
    k "Ok, bottoms up!  Here's goes nothing!"
    "Kendra takes the shot like a pro."
    scene party18
    k "Emily this is actually a little more embarrassing than I thought."
    e "You want me to dance with you?"
    k "Yeah please?"
    scene party19
    e "Hey!  Where is my top?"
    k "It fell off during the pillow fight remember?"
    e "Do you think my panties are too tiny?"
    k "They look just right to me!"
    scene party20
    k "Ok here goes nothing!"
    "Kendra slides her lingerie off and kicks it away."
    scene party21
    k "Now it's your turn to hide me like I did for you last night!"
    e "Nope, not part of the deal!"
    scene party22
    "Emily swivels behind Kendra, giving you a good view."
    k "Ok, everyone else come up here too though.  I feel like Emily and I are strippers when you sit there like that!"
    scene party23
    g "Kendra the stripper!  Haha, that's like your exact opposite!"
    kat "Yeah, girl-next-door Kendra has evolved!"
    scene party24
    g "C'mon and join us [y].  Dance with Kendra!"
    "Gianna maneuvers Kendra in front of you."
    "You push the pool table to the side and get a good look at her."
    "She's absolutely gorgeous and you can't believe this is finally happening!"
    scene party25
    k "Show me your moves [y]!"
    e "Hey [y]!  Where's your shirt?"
    y "I took it off awhile ago.  Ummm, before we went upstairs for ice cream I think."
    kat "Ah ha ha, we never went up for ice cream!"
    g "[y] this isn't fair, Kendra is naked, but you're not, take your pants off too."
    scene party27
    y "How'd you get them off so easily Gianna?"
    k "Wow, where were these moves last night [y]?"
    y "I'm just really hitting my rhythm!  Soon I'll be the best dancer here!"
    scene party28
    k "Oooo, I can't wait to see that!"
    "Kendra rubs her bare ass on your cock."
    y "If you keep doing that this dance is going to get a lot more interesting!"
    k "Oh, is that a promise?"
    if pickupemily == True:
        jump party2
    else:
        jump party3

label party2:
    scene party28
    e "Hey [y]!  Pick her up like you did to me in the shower today!"
    k "What happened in the shower?"
    "To your hazy mind that seems like a great idea."
    scene party30
    y "Up you go, Kendra!"
    "The alcohol tells you she's supposed to put her legs around your face, but she doesn't realize it and suddenly you start to lose your grip on her."
    jump party5
label party3:
    scene party30
    "Suddenly you have this great idea that it would be really fun to try to pick Kendra up into one of those dirty dancing raises."
    "Unfortunately not being a trained dancer, and both of you being completely wasted, you start to drop her."
    jump party5

label party5:
    scene party31
    "Luckily you catch her before she completely falls."
    g "What are you doing [y]?"
    y "I'm thinking about how to put Kendra down without dropping her on her head."
    "While you think about that you hear something ringing."
    scene party32
    kat "Hi Kenneth!  Are you calling for Kendra?"
    "You look out of the corner of your eye passed Kendra's leg and see Kat has answered a phone call."
    ken "Hi Katrina, yes is she around?"
    kat "Tonight I'm going by Kat!"
    scene party33
    kat "Kendra, it's for you, it's your dad."
    k "Ummm, hi daddy!  You've caught me at a bit of a weird time.  I'm hanging from [y]!"
    ken "You're hanging out with [y]?  What's weird about that?  Oh, you've been drinking haven't you."
    k "Yes daddy, but we're being totally responsible.  We're at the house safe and no one is going to drive."
    scene party34
    "You decide this is a good a time as any to start eating Kendra out."
    ken "I understand sweetie.  I'm glad you're being responsible.  A little drinking is harmless every now and then."
    k "Aaaaaaahhh, ummm, yeah daddy.  I'm having a lot of fun!"
    scene party35
    "Your cock has been waving in front of Kendra's face for a while now.  Suddenly she locks her ankles behind your head and takes your cock in her mouth."
    k "mmmm, mmmm, mmmm."
    ken "Is everything alright sweetie.  Are you trying to say something?"
    scene party33
    k "Sorry daddy, I was just a little distracted for a moment."
    scene party36
    ken "Alcohol takes some getting used to.  Don't overdo it ok?"
    k "Mmmmhmmmm."
    ken "it sounds like you're eating something.  Can you swallow so we can speak normally sweetie?"
    k "Mmmmmmm"
    scene party37
    "Kendra takes you further into her mouth and starts sucking hard."
    "Your balls tense up and you begin cumming in her mouth."
    scene party38
    "She releases your dick with a pop."
    k "Ok daddy, I did it, I swallowed just like you asked me to."
    ken "That's great honey.  I don't want to take you away from your friends for too long, but I'd love to hear about your trip."
    scene party41
    "You very careful set Kendra down and she takes the phone from Katrina while you go looking for your pants."
    k "It wasn't actually bad."
    ken "What wasn't honey?"
    k "Swallowing.  I think I'll do it again later."
    ken "What are you talking about, what were you eating?"
    scene party40
    g "I'm not sure if that phone call was funnier or sexier!"
    y "Yeah she really gets going when she talks to her dad!  That's the second time!"
    g "Her parents have always been a little too controlling.  It's just a little harmless acting out."
    y "I think the drink is starting to wear off a little.  How about you?"
    g "Haha, yeah I don't feel like giving yoga instructions from the top of the pool table anymore."
    if katharem == True:
        jump katrinaemilypreview1
    else:
        jump endofparty1

label katrinaemilypreview1:
    scene party42
    "You hear Kat whispering something to your left."
    "You can't quite make it out, but they look like they are still having fun."
    "Having seen Kat whisper to Gianna already on vacation you try to strain your ears.  Luckily drunk Emily speaks up at full volume."
    scene party43
    e "Hey Kat, let go of my glasses.  I already fell for that once tonight."
    kat "I just want to see how pretty your eyes are Emily."
    e "I don't believe you.  Kendra said something like that and then started shouting about becoming a streamer."
    scene party42
    kat "Ok, tell me a little more about streaming.  It does actually sound kinda fun."
    "Part of you is glad Emily didn't give up her glasses.  You're still feeling a bit of the effect of the alcohol, but you don't think Kat was trying to take them as part of a joke."
    $ renpy.end_replay()
    jump endofparty1
label endofparty1:
    scene party44
    k "I thought my dad would never get off the phone."
    y "Well you're a long way from home for the first time."
    k "Yeah I know.  That call got pretty crazy huh?"
    g "It was great!  Definitely going into my spank bank!"
    k "Gianna!"
    g "Hey what can I say?"
    k "Will you hold me for a bit [y]?"
    scene party45
    k "This is nice.  I'm feeling so sleepy now."
    y "Do you want me to help you back to your room?"
    k "No, let's just fall asleep like this ok?"
    y "Ok, goodnight Kendra."
    if katharem == True:
        jump katrinaemilypreview2
    else:
        jump endofparty2

label katrinaemilypreview2:
    scene party46
    "The last thing you see as your eyes close is that Gianna has also chosen to sleep downstairs."
    jump endofparty2
label endofparty2:
    scene party47
    "You wake up early in the morning with Kendra still at your side."
    "You carefully get up trying not to wake her."
    "She's still naked.  Would she be ok with you being here now that she's not drunk?"
    "You decide to take one last look at her before heading back to your room."
    scene morningafter3
    "When you get back the hangover hits you and you flop down on the bed."
    y "This is gonna be rough!  I should have had Katrina ask around about an ancient Hawaiian hangover remedy."
    "You lay there for several minutes before grabbing a coffee."
    scene gmorningwoj
    g "Hey [y]!  I'm surprised you're up already.  How are you feeling?"
    y "Kinda bad, but I guess this is part of the high school party experience I missed out on before."
    g "Yeah, I'm not feeling too great either.  I'm gonna go do my morning exercising at the beach.  You wanna join me again?"
    "Just then there is a knock at the door."
    y "Yeah, I'll meet you in the foyer in like 15 minutes, someone is at the door."
    scene morningafter1
    "You open the door and Kendra steps in."
    k "Good morning [y], how are you feeling?"
    y "The coffee helped a little, but I've still got a pretty bad headache."
    k "Me too, but I wanted to talk to you about last night.  I'm a little embarrassed.  Let's sit down."
    scene morningafter2
    y "Are you feeling bad about what happened?"
    k "No, just a little embarrassed.  I didn't do anything that I didn't want to do."
    k "But listen, teasing you is fun and all, but I guess we crossed a line yesterday."
    y "A fun line."
    k "Yeah it was really fun!  And I kinda want to keep doing fun stuff like that.  I don't even care the other girls are around."
    k "To be honest I like coming out of my girl-next-door shell."
    "She takes a deep breath."
    k "Here's the thing though.  I don't want my first time to be in front of a group or even worse, on the phone with my dad."
    k "I want it to be romantic.  Then we can go back to the fun flirty stuff in the group if you want."
    y "Yeah ummm, I kind of pictured my first time as part of a romantic evening too."
    k "I'm not asking you to wait long.  I'm thinking tonight we go on a romantic date with just the two of us.  Someplace that I can pay my half of the bill."
    k "Then we'll come back here and see where the night takes us ok?"
    y "Yeah that sounds nice!"
    scene morningafter4
    k "Great!  It's a date then!"
    k "I'm gonna go get some breakfast.  Maybe some waffles will help settle my stomach."
    y "I'm going to meet Gianna in the foyer.  We are going to exercise at the beach, but we could have breakfast with you first if you want to join us today."
    k "Ummm, yeah actually!  That sounds really great.  Go get her from the foyer while I start the waffles."
    jump chapter3a
    "Please save your game."
    jump chapter3a
    "If you've liked this game and aren't already supporting, please consider supporting me on Patreon at www.patreon.com/obrecht13.  It's only $3 for the current version of the game and it'd really help me a lot."
    jump chapter3a
    "I'm getting better with Daz and Ren'Py and I hope to have a nice long chapter 3 out towards the end of September.  I'm shooting for 28-day production cycles, so each month will come out sooner."
    jump chapter3a
    "Remember to save your game and thanks for playing!"
    jump chapter3a
label chapter3a:
    scene foyerchat1
    "You head down to the foyer to meet Gianna and find her speaking with the maid, though you hardly recognize her wearing shorts and a bikini top instead of her maid dress."
    r "Hey, I'm Rachel and I'm the maid for this rental property.  You must be [y]'s girlfriend.  I met him yesterday."
    g "Oh, [y]'s not my boyfriend, though I kind of hope he might be soon.  It's actually five of us staying here in a group."
    r "So like none of you are dating him then?"
    g "Nope, I don't want to say too much since we just met, but we're sort of trying to make amends for not treating him very well recently."
    r "Ok, I won't pry.  Anyway, I guess you noticed I'm not in my maid outfit.  It was because I was coming by to see if [y] or any other people he's staying with might want to be extras in a movie shooting nearby."
    scene foyerchat2
    y "Hey Rachel!  What's this about a movie?"
    r "[y]!  There's a movie shooting in the next cove over from yours.  I think I was telling you about the cove yesterday.  Well, there's a movie shooting there today and they are looking for extras."
    r "I only saw an ad posted for it online this morning.  I guess whoever was supposed to post something waited until the last minute.  I was just down there and I was literally the only person who showed up to be an extra."
    r "They asked if I knew any other young attractive people who I could invite and I thought of you."
    scene foyerchat3
    y "I'm flattered!"
    scene foyerchat2
    r "Oops!  That might have come out a little wrong.  Ummmm, I do think you're attractive, but I have a boyfriend.  I actually called him first but lately, all he does is play this new game called {i}Caelum Besieged{/i}.  Have you heard of it?"
    "You exchange a glance with Gianna."
    scene foyerchat3
    y "Yeah I've heard of it."
    scene foyerchat2
    r "Well lots of movies shoot here in Hawaii and going and being extras was something we liked doing together, but this time he turned me down to play more of that game."
    r "So that brings us to now.  You and Gianna are both attractive and you were nearby, and I promise this will be super fun!  So wanna come with me?"
    g "What do you think [y]?"
    scene foyerchat3
    y "I think it does sound like fun.  We'll need to swing by the kitchen and track down the others to invite them too."
    y "Kendra was about to make waffles and then was planning to join us at the beach, so I'll bet she'll be up for it."
    scene foyerchat2
    r "Ummm, well there's one more thing.  I also wanted to ask for the day off so we can do this."
    y "Can't you just request off directly from the agency?  Won't they just send someone else in your place?"
    r "I could, but then I won't get paid.  I know it's a little dishonest, but my boyfriend used to give surfing lessons, and lately because of that game he hasn't been seeking out tourists and we're kind of low on money."
    g "Because of the {i}Caelum Besieged{/i}?  So it's kind of your fault then [y].  I think we should cover for her."
    r "What do you mean it's [y]'s fault?"
    g "Oh nothing!"
    scene foyerchat3
    y "I'm sorry Rachel.  I really can't imagine going a day without rose petals in my bathtub."
    "You see her face beginning to fall."
    y "I'm just fucking with you!  Of course, you can skip cleaning our place today and we won't rat you out to the maid agency."
    y "I told you yesterday I'm not used to this luxurious lifestyle anyway."
    scene foyerchat2
    r "Yes!!  Today is going to be great!  Let's go find your other friends in the kitchen.  I can't wait to meet them!"
    scene kitchenchat1
    "Unfortunately when you get to the kitchen you find Emily is not doing so well."
    k "It's going to be ok Emily.  I'll get you some water.  The hangover will pass."
    kat "Or maybe a coffee would help?"
    e "I'm never drinking again!"
    scene kitchenchat2
    y "Hey guys, looks like you're not doing too good Emily.  I wanted to introduce Rachel who's working as our maid, but we can come back another time."
    e "No, it's ok.  Don't mind me, I'm just going to wallow in misery for a few minutes here on this nice cool floor."
    r "Ummm, hi.  I was just coming by to tell you guys about a movie that's shooting nearby, but I can see this isn't a good time."
    scene kitchenchat3
    r "It's called {i}Hawaiian Zombies 7: Aloha Death{/i}.  It's one of those B-horror flicks people get drunk and watch to laugh at.  They are desperate for extras today."
    e "I love watching those kinds of movies!  You guys have to go be in it!"
    k "We can't leave you here Emily."
    scene kitchenchat5
    kat "I actually have no interest in being an extra in a movie like that.  I'll stay with Emily and nurse her back to health.  Why don't the rest of you go?"
    scene kitchenchat7
    g "Are you sure Katrina?"
    g "I feel like we should all stick together."
    scene kitchenchat5
    kat "Don't get me wrong, I'd love to watch that movie with you once it's made and laugh my ass off, but I'm worried that if it gets out I was in a movie like that it'd be hard to be taken seriously as a Doctor of Psychology."
    scene kitchenchat6
    y "What about you Kendra.  Would you want to be in the movie?"
    scene kitchenchat4
    k "If Emily is really ok with us going then yeah, I do think it sounds like a blast!"
    k "Sorry about this Rachel.  We kind of got really drunk last night and it looks like it hit Emily a little harder than the rest of us."
    scene kitchenchat6
    r "I totally understand.  You aren't the first guest to wake up with a hangover and I'm sure you won't be the last.  I've had to clean up after a zillion parties here."
    y "I guess it's settled then.  Gianna, Kendra, Rachel, and I will go be in the movie, and Katrina will stay here and look after Emily until she feels better."
    scene kitchenchat5
    kat "Rachel, I remember seeing a coffee shop near here on the boardwalk.  I'm going to get Emily and me something better than what we have here.  Can you remind me which direction it was?"
    scene kitchenchat2
    r "Yeah, the closest one is Kauai Coffee and you just head right when you come up to the boardwalk and it's just a two-minute walk from there."
    scene kitchenchat3
    kat "Thanks!  Have fun you guys!"
    scene zombies7
    "A few minutes later you find yourself approaching a small movie set."
    r "I found some people for your movie Mr. Director!"
    define d = Character("Director", color="#b8860b")
    define t = Character("Timmy", color="#800080")
    d "That's great!  Wow, I'm glad you had such attractive friends!  I was just telling Zombie Mike here I was worried we weren't going to find anyone since Timmy forgot to post the online ads."
    scene zombies10
    d "You there, guy in the sunglasses."
    y "It's [y]."
    d "No, you're not [y] today.  You're playing Surfer Dude."
    scene zombies9
    "You see an angry-looking guy in his late teens run up."
    t "But Dad!  I was gonna play Surfer Dude!"
    d "Shut your damn mouth, Timmy!  We're lucky we're even able to shoot a scene here today after you forgot the ads for extras."
    t "I thought Mike was going to do them!"
    d "And you starred in {i}Hawaiian Zombies 6{/i} and we killed you off in that movie.  You can't just suddenly be in {i}Hawaiian Zombies 7{/i}!"
    t "Well what am I supposed to do all day then Dad?"
    d "You can be my assistant.  Go hold the clapperboard."
    t "So I can yell action and cut?"
    d "No, you can hold the clapperboard.  I'm the director and I yell those words!"
    scene zombies10
    d "You girls there.  You will be playing Beach Slut One, Beach Slut Two, and Beach Slut There."
    "Kendra starts snickering under her breath."
    k "This is gonna be so great!  I love laughing B-horror movies, but just listen to this guy!  It's gonna be so much funnier being in one!"
    g "So like in the credits it's gonna literally bill us as Beach Sluts followed by a number?"
    d "Yeah, you're an extra.  You don't get a name.  But hey, you'll be at the top of the credits cause we do it in order of appearance."
    g "Haha, yeah this shit is gonna be hilarious!"
    scene zombies18
    "The director goes around giving everyone some final instructions and before you know it your big scene is about to begin."
    d "You guys, here's your motivation.  Surf Dude there has just won a big surfing competition.  You are all going to congratulate him the only way a Beach Slut knows how."
    k "Let me guess, with our bodies?"
    g "Is there like a script or something?"
    scene zombies19
    d "No there's not a script!  It's called improv!  It's called acting!  These movies are much better without a script.  Believe me!  We tried it back with {i}Hawaiian Zombies 3{/i}.  Worst movie I ever made!"
    d "Now get out there and ham it up!  ACTION!"
    scene zombies11
    y "Yeah, like dude you got the best barrels ever dude just like you pull in and you just get spit right out of them and you just drop in and just smack it cool."
    y "WHAAA BAP!"
    y "Drop down say BAAAAAAA and then after that you just drop in, just ride the bell and get pitted, like so pitted, like that!"
    "The girls barely hold it together having seen the funny surfer dude vine you just quoted."
    "Somehow Kendra manages to get in a line in."
    k "You were like sooooo amazing out there!  Those waves were so big!"
    y "That's not the only thing that's big baby!"
    r "Oh really?"
    g "What else is big?"
    y "My dick is what's big ladies!!  And there's plenty to go around!  Let's celebrate my victory right here on the beach!"
    scene zombies12
    "Rachel looks like she's having the most trouble holding back laughter from your over-the-top improv so you grab her and kiss her before she breaks character."
    g "You're soooooo hot!"
    k "I can't wait to suck your big dick!  A stud like you deserves more than just a trophy for winning the competition!"
    scene zombies19
    d "AND CUT!  Great job so far guys!  Now for this next part you girls take your tops off and Timmy, get some more light shining into the scene."
    scene zombies26
    t "Sure thing Dad!  This is called a spotlight guys.  It's a movie term."
    d "Everyone knows what a damn spotlight is Timmy!"
    scene zombies21
    r "Mr. Director, so we really need to take out tops off?  Can't the zombies just attack us now?  I mean, I have a boyfriend and it's not this guy."
    scene zombies19
    d "Didn't we just go over this?  This is called acting!  Acting means pretending Surfer Dude is your boyfriend!"
    d "And these movies need tits!  It's the only reason a lot of people watch them!"
    scene zombies21
    g "It'll be ok Rachel.  We'll all do it and it'll be super fun!  I promise!"
    k "It's super unlikely anyone you even know will ever watch this movie anyway, and you could always give the director a fake name to put in the credits next to Beach Slut Two."
    r "Ok, I was the one who wanted to do this in the first place.  Sorry for almost chickening out when you guys are so brave!"
    d "AND ACTION!"
    scene zombies12
    "You do your best to get back in the same position you were in before the director said cut."
    "You make out with Rachel some more and the girls take off their bikini tops."
    scene zombies13
    "You spin Rachel around and let your hands roam all over her body."
    "Gianna whispers to her to just go with it and she closes her eyes."
    "You move down and rub the front of Rachel's bikini bottoms while Gianna does the same to herself and Kendra puts on hand on your ass."
    scene zombies19
    d "CUT!  For the next part Surfer Dude you need to act like you're sitting in a chair while the girls keep doing what they're doing and the zombies start sneaking up on you."
    t "Can't we get them a real chair?"
    scene zombies20
    d "No we can't Timmy!  Because back in {i}Hawaiian Zombies 4{/i} you used a chair that had a company logo on it and we nearly got sued!"
    d "Some companies oddly enough don't want their brand associated with the illustrious {i}Hawaiian Zombies{/i} franchise!"
    scene zombies19
    d "We'll CGI in a chair later or use some camera angle trickery.  For now, just pretend you're in a damn chair!"
    scene zombiemovie2
    "You kinda squat down and the girls rub you all over."
    "You slide your right hand over Kendra's ass and your left one over Rachel's.  You never dreamed you have three topless girls fooling around with you like this, even if it is just acting."
    "Yeah, your thighs are burning from the strain since you can't have a real chair, but it's totally worth it!"
    "Out of the corner of your eye, you see Mike and two other actors made-up to look like zombies approaching."
    scene zombies14
    "You realize you only have a few seconds left to fool around with the girls so you lay Rachel down."
    "Kendra crawls over your legs and both of the girls begin touching Rachel."
    "She moans into your mouth and you think about plunging your hand inside her bikini bottoms."
    scene zombies15
    "The zombies are nearly upon you and you hesitate, not knowing what you are supposed to do next."
    "From up close they do look kind of real.  Despite being a B-horror movie they obviously have makeup artists who know what they're doing."
    scene zombies18
    d "CUT!  You guys are still doing great!  I think we have enough smut to work with now, so the zombies are going to attack."
    d "Surfer Dude, you attempt to fight them and then let them win after a few seconds while Beach Sluts you run away screaming."
    d "The zombies will chase you and whenever they catch you just pretend to let them eat your brains."
    d "Surfer Dude while the girls are running around getting chased I want you to head over to the makeup tent and get zombified.  We need to show the virus has mutated since the last movie and now can turn people instantly."
    d "Whichever girl takes the longest to get caught will have Surfer Dude chase down at the end."
    scene zombies19
    d "ACTION!"
    scene zombies15
    "The zombies creep up and the girls scream and run away behind you."
    scene zombies16
    y "Don't worry babes!  I won't let these creepy fucking zombies get you!"
    define z = Character("Zombies", color="#800080")
    z "BRAAAAAAIIIIIINNNNNNSSSSSSSS!!!!"
    y "The joke's on you zombies!  I barely have any brains!"
    scene zombies17
    "Zombie Mike grabs you and the three of them swarm all over you making eating sounds."
    "You notice they purposefully put themselves in between you and the camera as much as possible."
    "Guess they don't have enough budget to CGI in some brains since they are thinking of CGI'ing in a chair!"
    "After you're dead you get up and head towards the makeup tent while checking out what the girls are up to in the distance."
    scene zombies27
    g "They're gaining on us guys!  EEEEEEEEEEEEECCCKKKKK!"
    k "Run faster!  There's gotta be somewhere we can hide!"
    g "STOP CHASING US ZOMBIES!!!"
    scene zombies28
    g "EEEEEEEEEECCCCKKKK!!!!"
    r "They got our friend!  I never even learned her name!"
    k "Just think about how it'll be more cute surfer boys for us once we get away!"
    r "I can't go on!  Leave me behind!  Save yourself!!"
    scene zombies29
    r "Stay back zombie!  I never did anything to you!"
    z "BBBBRRRRRRRAAAAAAAIIIIIIIINNNNNNSSSSSS!!!!!"
    r "No!  Leave me alone!"
    scene zombies30
    z "BBBBRRRRRRRAAAAAAAIIIIIIIINNNNNNSSSSSS!!!!!"
    r "NOOOOOOOOOOOOO!!!!!  I'm too beautiful to die!!!!"
    scene zombies1
    "A little while after Gianna and Rachel are eaten, you emerge from the makeup tent and the director tells you to start chasing Kendra and pretend to eat her brains once you have her."
    "Just as you start chasing her though she gets a call."
    k "Mr. Director can we start another take on this scene?  My Dad is calling."
    scene zombies19
    d "Improv honey!  Answer it and tell your Dad you're getting chased by a zombie!  It'll be great!  Keep rolling the camera Timmy!"
    scene zombies1
    k "Daddy help!  [y]'s been turned into a zombie and he's trying to eat my brains!"
    ken "What are you talking about sweetie?!"
    k "I'll facetime you so you can see for yourself!"
    scene zombies2
    k "Look behind me, Daddy!  He's almost got me!"
    ken "OH MY GOD!  [y] really has been turned into a zombie!"
    ken "Run faster honey!!"
    k "I'm getting tired Daddy!  I'm not sure if I can get away!"
    y "BBBBRRRRRRRAAAAAAAIIIIIIIINNNNNNSSSSSS!!!!!"
    ken "Leave my daughter alone [y]!"
    scene zombies3
    k "He's got me, Daddy!  Tell mom I love her!"
    y "BBBBRRRRRRRAAAAAAAIIIIIIIINNNNNNSSSSSS!!!!!"
    ken "Don't do it [y]!  It's Kendra!  You've known her your whole life!"
    scene zombies4
    "You pull your face close to the back of Kendra's head while trying to hide your mouth from the cameras like you saw the professional zombie actors do."
    y "NOM NOM NOM!"
    scene zombies5
    ken "Try to struggle away!  You can swim for safety in the ocean!"
    "Kendra struggles but you hold her in a full-nelson and you're pretty sure she couldn't get away even if she wanted to."
    "Mr. Kenneth was always pulling practical jokes on his daughter back in the day.  You're sure he'll get a good laugh over this in a minute."
    scene zombies6
    "You force Kendra to the ground and keep pretending to munch on the back of her head."
    "It looks like her bikini bottoms came off a little bit during the struggle.  The director will probably be pleased about that, as long as the cameras didn't pick up too much."
    d "AND CUT!"
    ken "Who said that?"
    scene zombies31
    k "I'm so sorry Daddy!  This isn't real.  We're acting in a movie today!"
    ken "Oh thank god!  I was so worried!  I was trying to {i}google{/i} how to call in the National Guard!"
    y "Hi Mr. Kenneth!  Sorry about this!  The makeup artist here is amazing!  I hope you're not mad!"
    "Kenneth takes a deep breath and then bursts out laughing!"
    ken "You guys got me good!  I should have known zombies aren't real!  You just got me so off guard and that makeup makes you really look undead!"
    ken "I was just calling to see if you had hangovers from last night."
    k "No, Emily has one, but the rest of us are ok.  We've been having a ton of fun acting in this movie and I made a new friend named Rachel."
    ken "That's great honey!  I knew those drama lessons we paid for back in middle school would pay off one day!"
    k "They sure did Daddy!  I think the director is pretty happy!  Well, at least when he's not yelling at Timmy!"
    ken "Who's Timmy?  Wait a second are you topless?!"
    k "Gotta go bye!!"
    "Kendra quickly hangs up and switches off her phone."
    k "Shit!  I forgot we were on facetime!"
    scene zombies18
    d "Ok, nice work everyone.  Anyone coming to the next shooting site please head towards the bus."
    "He turns towards your group."
    d "You guys are welcome to come as well.  We can put you in zombie makeup and use you as extras in the warehouse scene."
    if katharem == True:
        jump nocoffee
    else:
        jump coffee


label coffee:
    scene zombies22
    "Just then Katrina comes walking up with a tray full of coffees."
    kat "Hey guys!  Emily is doing a lot better.  I went back to Kauai Coffee a second time and got some for everyone."
    kat "I have one for you too Rachel."
    scene zombies23
    r "That's super nice of you Katrina!"
    y "What kind is this?"
    kat "They're mochas, but with macadamia nuts in addition to the chocolate."
    g "Sounds great!"
    k "Yeah, thanks a million Katrina!"
    scene zombiemovie3
    d "TIMMY! WHY DO THE EXTRAS HAVE A BETTER ASSISTANT THAN I DO?!"
    t "What do you mean Dad?"
    d "GET ME A COFFEE RIGHT NOW TIMMY!"
    scene zombiemovie4
    t "But you don't even drink coffee dad!"
    d "GET ME THE DAMN COFFEE TIMMY!"
    scene zombies24
    k "This really hit the spot!"
    y "So what do you guys think?  Should we go with the crew on the bus and be zombie extras in the next scene?"
    k "I'd love to but I'm sure my Dad is gonna call back and I'll have some explaining to do.  Luckily I'm thousands of miles away so he can't ground me!"
    y "I think I'm gonna head back as well.  Maybe get some work done or relax on the beach."
    r "I'm gonna go to the next filming site!  I've had so much fun I don't want it to end.  Thanks for coming today guys!"
    g "I think I'm gonna go be in the warehouse scene too.  C'mon Rachel, let's sit next to each other on the bus!"
    jump aftermovie



label nocoffee:
    scene zombies25
    r "How about it?  Do you guys want to go?"
    k "I'd love to but I'm sure my Dad is gonna call back and I'll have some explaining to do.  Luckily I'm thousands of miles away so he can't ground me!"
    y "I'm gonna head back as well.  Maybe get some work done or relax on the beach."
    g "Well I'd love to go with you, Rachel."
    r "Great!  Ok, thanks for coming today [y] and Kendra.  See you tomorrow when I'm back to my dull life as a maid!"
    g "C'mon Rachel, let's sit next to each other on the bus!"
    jump aftermovie

label aftermovie:
    scene bc1
    "You decide to go relax on the beach by yourself for a bit and find your beach stuff exactly where you left it."
    "Between working on the game and going from activity to activity there hasn't been a lot of time to relax."
    scene bc8
    "You sit down and take in the view."
    "Hawaii really is a beautiful place."
    "You find your mind wandering back to the girls and how this trip is meant to be a chance for you all to reconnect."
    menu:
        "I think things are going great here.  The girls seem like they are trying to make amends and I think I can forgive them":
            jump aftermovie1
        "I'm still mad.  I might just end up using the girls for my own pleasure and dumping them the second we get back":
            jump aftermovie2
label aftermovie1:
    scene bc6
    $ forgive = 1
    "Yeah, I do need to forgive them.  Everyone makes mistakes and they really are trying to make things right."
    jump aftermovie3
label aftermovie2:
    scene bc6
    $ forgive = 0
    "I know I've told the girls that I've let it go, but I just can't get it out of the back of my head that they were going to break it off with me."
    "I'm probably going to have sex with Kendra tonight after the date she asked me on.  I bet I can get the rest of the girls in bed as well."
    "Maybe after this trip is over I'll be the one to move on from all of them."
    "Not telling Rachel I made the game seems to have worked out pretty well.  She likes me without knowing I have money.  Maybe I'll try to find a girl back home like that."
    jump aftermovie3


label aftermovie3:
    scene bc8
    "You continue relaxing and letting your thoughts wander wherever the Hawaiian breeze takes them."
    if katharem == True:
        jump streaming1
    else:
        jump poolkatemily1


label streaming1:
    "After a while, you get a text from Katrina containing three links.  One of them you recognize as Emily's Twitch channel."
    kat "I'm streaming with Emily.  My phone is under the desk, my iPad is by the bar, and her computer camera is on.  Take your pick of which angle you wanna watch from and click a link."
    scene streaminglesson1
    "You cycle between all three links.  It looks like Katrina has just finished setting up her iPad to stream to your phone.  You begin listening in."
    e "I'm so glad you're taking an interest in streaming Katrina.  I can't wait to teach you everything I know!"
    kat "Yeah, I can't wait.  I'm setting up my iPad to record your lesson.  I bet I could stream an hour or two a day and make a little extra money part-time!"
    e "I know you already know I like streaming bottomless.  I hope you're not like weirded out too much.  If you are I'll go put on shorts."
    kat "No way, I think exhibitionism is hot!  I'm going in my panties too!"
    e "Ok, well just remember don't stand up.  It's a 30-day ban if you do and we'll be on my stream so it would really hurt me."
    kat "You can trust me, Emily.  I'll be really careful not to give us away."
    scene streaminglesson2
    e "So while we wait for people to join I'll go over some basics.  The main thing is that being a girl streamer gives you a couple of advantages."
    kat "Oh it get it!  You're talking about your breasts!"
    e "Haha, yeah!  So a tank top or small shirt is almost mandatory.  If you don't want to use your sexuality you don't have to, but then you'll need to be successful in the same way a guy needs to be."
    scene streaminglesson4
    e "Namely that's being either in the top .01 percent of most charismatic guys or being in the top .01 percent of the most skilled guys at the game they are playing."
    e "Also, some guys find success with a gimmick.  Like playing crazy decks in Hearthstone or Magic."
    e "I kind of try to do both.  I use my sexuality and I also try to be the best I can at whatever game I'm streaming."
    kat "I'm a firm believer one should always use all assets available in every situation."
    scene streaminglesson3
    e "Twitch used to be all about gaming, but now it's really expanded.  You can just chat, or you can play music, or you could cook.  Or in your case maybe ASMR."
    kat "People do ASMR on Twitch?"
    e "They sure do!  That's what you were doing to me last night right?  You know, right before we fell asleep.  I remember looking at you and you were whispering and I felt the tingles in my neck."
    e "I remember you got my glasses off somehow even though I tried to stop you at first.  I don't even remember why I didn't want you to have them."
    kat "Yeah, what I was doing did have a lot in common with ASMR.  The whispering, the light touches, and the personal attention all are aspects of ASMR.  I've studied it in detail in college and on my own time."
    kat "Do you remember what I whispered to you?"
    scene streaminglesson2
    e "Not really actually.  I guess it was because I was drunk."
    kat "It's ok if you don't remember.  Your subconscious will remember even if you can't recall right now."
    e "Wait, remember I'm the one giving you a Twitch lesson right now.  Don't try turning this into you giving me lessons about the subconscious and psychology."
    kat "Haha, it's hard not to talk about my passions!"
    scene streaminglesson4
    e "So today we'll be playing [y]'s game {i}Caelum Besieged{/i}.  We'll start a new character for you and go over the basics."
    e "It's important to have a catchy title for your stream so we're calling this one {i}Caelum Besieged Bootcamp{/i}."
    e "I find people click a little more when you have a cool word like {i}bootcamp{/i} in the title.  They'll know it's an instructional stream, but it won't give off a boring vibe like learning in school."
    kat "Is [y]'s game fun?"
    e "Oh it's super fun!  I've been getting so many viewers and it's gaining more popularity every day."
    scene streaminglesson7
    e "Ok we have some viewers now.  You can use the headset I brought for [y].  I'm hoping he'll do another interview this trip."
    e "Hey chat!  I hope everyone is doing great!  I woke up with a huge hangover today, but my BFF Katrina here got me a Mocha and Macadamia Nut coffee."
    kat "You're welcome Emily!  Hi, chat!"
    e "Today we're going to be playing more {i}Caelum Besieged{/i}, but Katrina is interested in learning to play so we're creating a new character and running a bootcamp."
    e "The stream today will be fairly short.  Just enough to get her feet wet!"
    kat "How do you mute the mic?"
    e "The little button on the side of your headset, or the Volume Mixer in the lower right on the monitor."
    "Emily clicks it for a second, but you can still hear her though Katrina's iPad."
    kat "My feet won't be the only thing getting wet!  Streaming in my panties is more fun than I thought!  The guys in chat will never know!"
    e "I know right?!"
    "Emily turns the sound back on and you click over to the link under the desk."
    scene streaminglesson5
    "Emily starts explaining the basics of the game to Katrina, but having made the game you are far more interested in what Katrina is doing to Emily below the desk."
    "As Emily interacts with chat and tries to keep her composure you watch as Katrina gently strokes Emily's leg."
    "A few times Emily stops mid-sentence, clearly distracted, but she doesn't pull Katrina's hand away."
    scene streaminglesson6
    "Katrina moves her hand higher and Emily actually begins lightly stroking the top of it."
    e "I muted us again.  This is so hot, but don't distract me too much!"
    kat "I can't help it, Emily.  Your leg is so soft!"
    "Emily unmutes."
    e "Ok chat, I'm gonna switch with Katrina now and she's gonna start her new character."
    kat "What do you think chat?  Should I wear the pink glasses?"
    "You switch back to Emily's Twitch stream and see a lot of people seem super excited at the chance to see Emily without her signature glasses for once."
    scene streaminglesson9
    "Emily grudgingly gives up the glasses and switches seats with Katrina."
    e "So click there and pick the class you want."
    kat "I'm going Sorceress."
    e "Cool!  That's my main too!"
    scene streaminglesson8
    "The girls work their way through the tutorial and you take a look back at the iPad angle."
    "You know that this whole streaming lesson is most likely part of Katrina's grand scheme to seduce Emily and the rest of the girls, but it really looks like Katrina is enjoying your game and that makes you happy."
    "She stops playing with Emily's legs under the table and it looks like the game has her whole focus."
    if katdom == 0:
        jump streaming2
    else:
        jump streaming3

label streaming2:
    y "That'll teach you to try to get in everyone's head Katrina!  Looks like I'm the one with your undivided attention this time instead of the other way around for once.  Glad my game is so addictive!"
    jump streaming3

label streaming3:
    "45 minutes go by and Katrina manages to get through the tutorial and first dungeon."
    "By then the chat has fallen in love with her and someone makes a $100 donation telling Emily to sit on Katrina's lap."
    "Emily mutes the mic again as you listen through the iPad."
    kat "Are we allowed to do that?"
    e "It's kind of a gray area.  Probably we can get away with it.  I'll split that donation with you if you wanna do it."
    kat "It's fine with me, hop on!"
    scene streaminglesson13
    "The chat goes crazy!"
    "Katrina tries to keep playing, but the girls end up spending most of their time reading all the new donation messages that are coming in."
    scene streaminglesson12
    e "Ok guys, that's gonna have to be it for now.  You know we can't go further than this and we've got some other things to do today.  I'll be back on either tonight or tomorrow, hopefully with [y] again soon."
    "She shuts down the stream, much to the disappointment of chat, but you still have the links from Katrina's iPad and phone."
    e "That was crazy!  Hopefully, I won't get more than a warning for this.  I've never done anything like this on stream before and it's so much hotter since they didn't even know we're in our panties."
    kat "I had a lot of fun too.  Next time we'll include [y] ok?  I bet he'll stream in his boxers!"
    e "That'll be super fun!"
    "Katrina whispers something to Emily, but you can't quite make it out.  You expect Emily to get up soon from Katrina's lap, but she doesn't."
    scene streaminglesson10
    "Suddenly Katrina leans Emily back and makes direct eye contact while moving her hand over Emily's pussy."
    "Desperate to hear what Katrina is whispering you turn the volume on your phone to the max."
    kat "I'm in the mood for more games.  How about we play another one?  I'll try to make you cum and if you do then you will obey me for the rest of the trip."
    e "Ok, Katrina."
    kat "Good girl.  Now just keep staring into my eyes and focus on how good my fingers are making you feel."
    "Katrina rubs Emily through her panties and Emily moans."
    kat "Still think I'm doing ASMR?"
    e "No, it's something more, aaaaahhhh."
    kat "Good girl.  This is the best kind of game, one that you'll actually enjoy losing."
    scene streaminglesson11
    "Katrina pulls Emily's panties to the side and begins rubbing her clit."
    "Emily's moaning gets louder and louder."
    "Katrina whispers something else that you can't hear even on max volume and then begins moving her fingers even faster."
    e "Oh god!  I'm cumming!!!"
    scene streaminglesson10
    "Emily cums on Katrina's fingers and Katrina slides her thong back into place."
    kat "That was a really fun game!  We'll have to do it again sometime when we get back."
    e "It was really fun!  Do I really have to obey you now though?"
    kat "You do but don't worry, I won't make you do anything you don't want to."
    kat "For my first order though I want you to go shave your cute little landing strip.  You'll be wearing your new slingshot bikini when we go on the boat tomorrow."
    scene endofstream
    "Emily gets up and Katrina walks over to the iPad."
    kat "I hope you enjoyed the end of the stream [y]!  Next time I hope you join us!  We'll have all kinds of fun under the table with Emily!"
    jump poolkatemily1
label poolkatemily1:
    scene poolchat3
    "When you get back you find Katrina floating in the pool and decide to join her."
    if katharem == True:
        jump poolkatemily2b
    else:
        jump poolkatemily2a
label poolkatemily2a:
    kat "So how did the movie-making go?"
    y "It was super fun!  The director was all over the place.  One minute telling us we did great, the next minute yelling about what acting is, and the next minute yelling at his son Timmy."
    y "He even said the words {i}Beach Sluts{/i} with a straight face!"
    kat "Haha, that's awesome!  I can't wait to see it when it comes out."
    scene poolchat1
    y "Gianna and Rachel went to help with the next scenes at the warehouse.  I'm going to tell her no spoilers when she gets back.  Three months from now or whenever this movie comes out we're gonna have a blast watching it!"
    kat "So what are your plans for the rest of the day?"
    y "Well since the movie stuff ended I've just been relaxing.  I guess I plan to do a little more of that and then I'm going out with Kendra tonight."
    scene poolchat2
    kat "Like on a date?"
    y "Yeah I guess so.  She was feeling kinda weird about how things went last night."
    kat "Oh right, you mean when you guys 69'd standing up while I held the phone for her Dad to talk to you?"
    scene poolchat1
    y "It sounds pretty bad when you say it out loud!  But yeah we are going to go on a date tonight and clear the air about that."
    scene poolchat3
    kat "Ok, well I hope you have fun.  And I hope maybe you consider going on a date with me some time too."
    y "For sure!  We'll find time soon!"
    scene poolchat4
    e "Hi guys!  Can I join you?"
    y "Of course Emily!  Are you feeling any better?"
    scene poolchat5
    e "Yeah, I just needed a little time and the nice coffee that Katrina brought me.  How'd the movie go?"
    y "Katrina and I were just talking about that.  I don't want to give any spoilers for when we watch it later, but it was fun!"
    e "Ok, I won't ask too much more about it then."
    scene poolchat6
    e "So do you think we'll see that whale when we go back to Lagoon Resort tomorrow for the boat tour?"
    kat "I hope so!"
    e "I looked up some whale songs this morning.  It was actually surprisingly soothing despite the hangover."
    y "I hope they work!"
    "The three of you continue to chat and enjoy the pool until it's time for your date."
    jump kendradate1
label poolkatemily2b:
    kat "Did you like the Twitch stream?"
    y "Yeah, that was super hot!"
    kat "Let's do it again tomorrow, but with you there ok?"
    y "Sounds like a plan!"
    scene poolchat2
    kat "So how did the movie-making go?"
    y "It was super fun!  The director was all over the place.  One minute telling us we did great, the next minute yelling about what acting is, and the next minute yelling at his son Timmy."
    y "He even said the words {i}Beach Sluts{/i} with a straight face!"
    kat "Haha, that's awesome!  I can't wait to see it when it comes out."
    scene poolchat1
    y "Gianna and Rachel went to help with the next scenes at the warehouse.  I'm going to tell her no spoilers when she gets back.  Three months from now or whenever this movie comes out we're gonna have a blast watching it!"
    kat "So what are your plans for the rest of the day?"
    y "Well since the movie stuff ended I've just been relaxing.  I guess I plan to do a little more of that and then I'm going out with Kendra tonight."
    scene poolchat2
    kat "Like on a date?"
    y "Yeah I guess so.  She was feeling kinda weird about how things went last night."
    kat "Oh right, you mean when you guys 69'd standing up while I held the phone for her Dad to talk to you?"
    scene poolchat1
    y "It sounds pretty bad when you say it out loud!  But yeah we are going to go on a date tonight and clear the air about that."
    scene poolchat3
    kat "Ok, well I hope you have fun!  Looks like you are going to score before me this time!"
    y "Hope there are no hard feelings."
    kat "No, none at all.  I'm not exactly sure how to seduce Kendra.  She kind of always brushes me off whatever I try."
    kat "The only thing I can think of is to maybe try to get her interested in me as part of rebelling against her Dad.  I'm certain once I get her in bed I can take control, I'm just not sure how to get to that point."
    y "I'm sure you'll figure it out."
    scene poolchat4
    e "Hi guys!  Can I join you?"
    y "Of course Emily!  Are you feeling any better?"
    scene poolchat5
    e "Yeah, I just needed a little time and the nice coffee that Katrina brought me.  How'd the movie go?"
    y "Katrina and I were just talking about that.  I don't want to give any spoilers for when we watch it later, but it was fun!"
    e "Ok, I won't ask too much more about it then."
    scene poolchat6
    e "So do you think we'll see that whale when we go back to Lagoon Resort tomorrow for the boat tour?"
    kat "I hope so!"
    e "I looked up some whale songs this morning.  It was actually surprisingly soothing despite the hangover."
    y "I hope they work!"
    kat "By the way, Emily, did you go do what I asked you?"
    e "Yeah, and I'll wear the slingshot tomorrow on the boat when we hunt down that whale."
    kat "Good girl!"
    e "Call me Ishmael."
    y "Are well calling the whale {i}Moby Dick{/i} then?"
    "The three of you continue chatting and enjoying the pool until it's time for your date with Kendra."
    jump kendradate1
label kendradate1:
    scene boardwalk1
    k "The boardwalk feel so empty tonight."
    y "Yeah I guess even though the COVID quarantine is over people still aren't traveling much."
    k "So many businesses went under too.  I guess this shoe store is one of them.  Just a few shoes in the window that was part of a display, but all the merchandise is packed up and gone."
    y "I guess everyone is buying their shoes online right now.  I'm sure all the businesses will bounce back though."
    scene boardwalk2
    y "At least with fewer people walking around we stand out less in these super fancy outfits."
    k "Oh I don't care about that.  It was bad back in coach when I was the only one dressed like this, but with you here, with me, it's no big deal."
    y "Yeah you're right.  I should be more worried about overheating in this jacket."
    scene boardwalk1
    k "Do you mind if we go back to the boutique where Katrina picked out that outfit for you?"
    y "Sure, is there something you need there?"
    k "I was thinking we should get some Hawaiian shirts or something for our parents as souvenirs.  Also, I'm a little jealous that Katrina found such a nice outfit for you and I want to see what else they have."
    scene boardwalk2
    y "I'm wearing a suit you picked out for me right now.  No need to be jealous."
    k "I know, I guess I'm just being silly.  So you don't want to let me pick out something else for you?"
    y "I didn't say that.  You have great taste and I do need some more nice clothes.  I'm tired of doing a load of laundry every day to re-wear the same things."
    scene boardwalk3
    k "Ok so some Hawaiian shirts for our parents and a new outfit for you.  Here we are!"
    y "I have good memories of this store!"
    k "I bet you do!"
    scene boardwalk4
    k "Let's look over here."
    k "I didn't really get a good look at the men's section last time."
    scene boardwalk5
    k "Looks like they have a lot of Hawaiian style shirts."
    k "Do you think we should get each of our Dad's the same one?  And each of our Mom's the same one?"
    y "Yeah, it'd be really funny if they wore them on the same day!"
    k "Let me get one to model for you."
    scene boardwalk6
    k "What do you think?"
    y "It looks great on you Kendra, but ummm, I can see your panties."
    k "Well I was in a dress so I have no bottoms to wear.  I guess they are pretty tiny though."
    y "And sparkly like your dress."
    k "I'm sure you don't mind!"
    scene boardwalk7
    k "How about this look?"
    y "Super hot!  You could be a model in a Hawaiian shirt magazine!"
    k "Do they have those?"
    y "I don't know, probably."
    k "Ok, you put it on now!"
    scene boardwalk8
    k "Haha, now you could be the model in a Hawaiian shirt magazine!"
    k "Well except for your suit pants which don't match at all!"
    y "Guess that makes two of us for not being fully prepared to try on Hawaiian shirts!"
    y "Maybe we should make our own magazine for fun some time and get everybody to model some crazy Hawaiian shirts."
    k "Yeah that'd be a lot of fun!  We could get crazier and crazier until the store finally kicks us out!"
    y "They didn't kick us out last time, so I bet it'd get pretty crazy!"
    k "Wait here while I pick out a nice outfit for you."
    scene boardwalk9
    y "I think this looks really nice Kendra!"
    k "Yeah it's a more preppy style than what Katrina picked out.  I like this better!"
    y "Let's get it then!  Listen I know you wanted to split the cost of the date evenly, so how about if you buy this outfit and the Hawaiian shirts and I pay for dinner?"
    k "We're going someplace really expensive for dinner aren't we?"
    y "Ok yeah, but listen!  It's a restaurant built into a dormant volcano!  How cool is that?"
    k "Haha, that does sound awesome!  But really I don't ever want to use you for your money."
    y "It's just another way of dividing up the cost of the date.  You're paying for the first half of the date and I'm paying for the second half."
    k "Ok, just this once [y].  We'll probably never get a chance to eat in a volcano again."
    scene date3
    define w = Character("Waitress", color="#b8860b")
    w "Hi, welcome to Mount Kona Fine Dining, I'll be your server tonight."
    k "Wow this place really is built into a volcano!"
    scene date5
    w "Allow me to tell you our specials."
    w "Tonight we have Poi, Lomi-Lomi Salmon, Kalua Pig, and Laulau."
    w "All dishes are served with a side of long rice, pineapple, and lilikoi."
    k "What is Laulau?"
    scene date6
    w "Laulau is made with pork wrapped in layers of Taro leaves and cooked in our underground hot rock oven for hours until it turns soft and smoky flavored."
    w "The meat is tender and juicy while the leaves turn to a spinach-like consistency."
    y "What is a Taro leaf?"
    w "Taro is a well-respected plant, not only here in Hawaii, but also throughout Polynesia and the Pacific islands."
    w "While Poi is made from the Taro root, Laulau is made from the leaves."
    k "[y] how about we get two orders of that?"
    y "Sounds good, two orders of Laulau please."
    scene romanticdinner1
    k "That waitress was really knowledgeable."
    y "She sure was!  I hope this is good.  I kind of want to try Poi too while we're here, but I heard it's gross, so I'll just get it at a food truck or something another day."
    k "I hope this volcano is really dormant."
    y "It better be!  Otherwise, we're gonna end up in a 2020 meme!  Something like, {i}Who had dormant volcano suddenly erupts on their 2020 Bingo card?{/i}"
    k "Haha, yeah there's stuff like that on my Facebook newsfeed every day!"
    "BEEP"
    scene date2
    y "I just got a text from Gianna.  They are done with the movie for the day.  Looks like a picture is coming through."
    k "Let's see it!"
    scene zombies32
    k "Wow, look at Gianna, I barely recognize her!  And Rachel looks all cut up.  Let's call them!"
    y "Are you sure that's ok?  Calling someone while we're on a date?"
    k "Don't you wanna know how the rest of the movie went?"
    y "Yeah, for sure!"
    scene date2
    y "Hey Gianna, I'm here with Kendra.  What's up with you in the picture?"
    g "Hi guys!  I'm still with Rachel.  We just finished shooting and the bus is gonna bring us back in a few minutes."
    g "I'm a ghoul in this picture.  Rachel and I got cured of being zombies by a mad scientist but then I got turned into a ghoul."
    r "Then at the end of the movie Gianna scratched my face and I got bit by a zombie.  The movie ended with a cliffhanger that I might be half-ghoul, half-zombie, but stronger than both!"
    y "Isn't that the plot of {i}Underworld{/i}, just replacing the Vampires and Lycans?"
    g "Yeah pretty much!  We had so much fun today though.  Mr. Director really chilled out after we got to the warehouse.  Mostly because Timmy got lost looking for coffee and never showed up."
    k "That's hilarious.  Poor Timmy!"
    g "So we need to leave in a minute before we miss the bus, but do you want a sexy ghoul girl pic, [y] before I wash off all this body makeup?"
    y "Sure, I can't wait!"
    scene zombies33
    "A moment goes by and another picture message comes through."
    "Kendra cranes her neck to see it."
    k "Wow, she's the hottest ghoul girl ever!"
    y "I guess Rachel must have taken that picture for her."
    scene romanticdinner1
    k "Time to put the phone away.  We can't have any more naked girls texting you during our date!  You're mine for the rest of the night!"
    y "Hope you aren't mad!"
    k "Haha, no way!  Today is like the best day ever!"
    scene date4
    "The food comes and the two of you enjoy your meal."
    "The pineapple is especially good.  You remember hearing the Dole plantation is in Oahu, so it must be super fresh!"
    scene date7
    w "Here's the check.  If you find yourselves in Hawaii in the future, please come visit us again!"
    k "This place was wonderful!  Maybe next time we'll try the salmon."
    w "Enjoy the rest of your evening and have a safe trip back."
    scene romanticdinner1
    k "When we get back to the house, wait for me by the jacuzzi area ok?  I have a surprise for you."
label galleryScene2:
    scene kendrahula8
    k "How do I look?"
    y "Like a Hawaiian princess!"
    k "Don't tell the others I wore this ok?  It was supposed to be for another night."
    y "My lips are sealed!"
    scene kendrahula9
    k "That's a shame because I kind of want to kiss them!"
    y "You look so beautiful, Kendra."
    "Kendra kisses you and then pulls back."
    scene kendrahula10
    k "The seashells didn't really cover my breasts very well.  Hope you don't mind that I left them off."
    y "Never apologize for your breasts being too big!"
    k "Go get in the jacuzzi ok.  This afternoon I was practicing a special dance I want to show you."
    scene kendrahula5
    k "So a hula dance is meant to tell a story."
    "She takes a deep breath and begins."
    scene upcoming3
    k "Once upon a time there was a girl named Kendra and a boy named [y]."
    k "[y] liked Kendra and Kendra liked [y], but she wasn't ready for a relationship."
    scene kendrahula1
    k "[y] asked Kendra out, but she refused him."
    k "But over time, she started to change her mind.  Maybe [y] was right for her after all."
    scene kendrahula2
    k "She had trouble telling him though and the more time that passed the harder it was for her to say something to him."
    k "Then he started showing interest in their other friends."
    scene kendrahula4
    k "Part of her was jealous and part of her wanted to share, but still, she said nothing and more time passed."
    k "Eventually she decided to try to move on, but afterward realized it was a big mistake."
    scene upcoming3
    k "She told him she was sorry and he immediately forgave her."
    k "In a way that made her feel even worse."
    scene kendrahula1
    k "She wished she could go back in time to when he first asked her out and she'd say yes this time."
    k "But that's impossible so at least she decided she'd finally open up about how she is feeling."
    scene kendrahula3
    k "And big Hawaiian finish!"
    "You applaud."
    scene kendrahula5
    k "So that's my story.  You don't need to do it now, but when we get back, please think about asking me out again.  I'll say yes if you do."
    scene kendrahula6
    k "For now, let's enjoy the jacuzzi together."
    "She lets the grass skirt fall to the floor."
    scene kendrahula7
    "Her flower necklace quickly follows."
    k "You want me to join you right?  You know where this night is going if I get in?"
    y "Sit on the edge."
    scene kendrahula11
    "She sits down on the edge and you begin fingering her."
    y "I loved your hula story Kendra.  I'm so happy you shared how you're feeling with me."
    k "Aaaaah, yeah, aaaaah, I feel like the last few years have almost been wasted since I kept everything to myself, aaaaaah."
    y "We'll talk more about it when we get home."
    k "Aaaaah, ok [y]."
    "You finger Kendra until she reaches climax and then it's your turn."
    scene kendrahula12
    k "I love your cock [y]!  It's so big.  Did I really have it in my mouth last night?"
    y "Yeah, my memory is a little fuzzy, but it was great."
    k "Let me try it again."
    scene kendrahula13
    "Kendra takes your cock in her mouth and begins bobbing her head up and down."
    "You enjoy the moment, not saying anything."
    "Her lips feel amazing and even though she can only go halfway down she uses her hand as well."
    "You feel yourself getting ready to cum and gently pull her back up."
    scene kendrahula12
    k "Do you want me to swallow again or do you want to take this to the bedroom."
    y "The bedroom.  I've been wanting you for so long."
    scene kendraseduction1
    "Leaving your clothes back at the jacuzzi, you head for your room."
    "just inside the door, Kendra leaps into your arms, knocking you onto the bed."
    scene kendraseduction2
    k "How do you want me [y]?"
    "She kisses the tip of your dick."
    scene kendraseduction3
    y "I'm taking you in every position tonight in case I never get another chance like this."
    "You roll her over."
    scene kendraseduction4
    k "Don't worry, this won't be a one-time thing if you don't want it to be... aaaaaah!"
    "You thrust inside her."
    "You bend down and kiss her while you gather speed."
    scene kendraseduction5
    "She kisses you back while wrapping her left leg around you."
    "Her right leg you pin upwards with your arm."
    k "Oh god [y]!  This is amazing!  I feel so full!"
    scene kendraseduction6
    "Wanting a better view you pull back into a kneeling position."
    k "Aaaaah, aaaaaah, [y]!"
    y "Alexa, turn on the light above the bed."
    scene kendraseduction7
    "The light comes on above you giving you an even better view of your cock pumping in and out of Kendra's pussy."
    k "Aaaaaah, keep going!"
    y "Pull your legs further apart!"
    scene kendraseduction8
    "She spreads them as far as she can."
    "You can feel the tip of your cock pushing against her cervix deep inside her."
    scene kendraseduction9
    y "Time for another position!"
    "You turn her onto her side and pull her arms behind her."
    k "Your cock feels even bigger this way!  Aaaaaah!"
    y "We need to see which position we like best."
    y "Get on your hands and knees!"
    scene kendraseduction10
    k "Like this?"
    "You grab her hips and continue thrusting into her."
    k "I'm cumming [y]!  I'm cuuuuuummmmmminnnngggg!"
    scene kendraseduction14
    "She collapses down on her belly, but you don't stop."
    y "We're not done yet, Kendra!"
    "You feel her pussy clamping down hard on your cock."
    scene kendraseduction13
    k "I'm cumming again!  Oh my god!!!!"
    y "I want you to ride me now."
    scene kendraseduction16
    "You roll onto your back and she takes your cock and puts it back inside her."
    scene kendraseduction17
    y "I've wanted you in this position since back at the firepit."
    y "Now there's no bathing suits in between us!"
    k "Yeah this feels much better!"
    "She grinds down hard on your dick and you feel your orgasm start to build."
    y "I'm going to cum soon."
    k "I feel another one building as well.  Let's cum together!"
    scene kendraseduction18
    "She leans back and you explode inside her."
    k "[y]!!!!!!!!!"
    "She cums all over your dick as you shoot deep up inside of her."
    scene kendraseduction19
    "You both take a moment to catch your breath."
    scene kendraseduction20
    k "I hope I can spend the night."
    "She leans you back onto the bed."
    scene kendraseduction21
    k "That was so amazing, [y]!  I'm sorry I made you wait so long, but I'm really glad you were my first."
    y "I'm really glad you were my first too, Kendra!"
    k "Will you hold me like you did last night?"
    scene kendraseduction22
    "You roll over into the position she wants, exhausted from the day."
    "In no time you are both asleep, dreaming of a possible future together."
    $ renpy.end_replay()
label galleryScene1:
    scene bathroommorning3
    "You wake up to the sound of Kendra moving around in the bathroom and decide to join her."
    k "Good morning sleepyhead!  I realized I don't have any clothes.  Can I borrow a long t-shirt or at least a towel from the bathroom?"
    scene bathroommorning1
    y "Sure, when I let you leave."
    k "Hey [y]?  Remember when you said you wanted to take me in every position last night in case we never do it again?"
    y "Yeah."
    k "Let's do it again!"
    scene bathroommorning2
    "You spin her around and go for her breasts."
    "You feel your dick slid up her hip towards her belly as it hardens."
    scene bathroommorning4
    k "Yeah eat me out again [y]!"
    k "Your tongue feels like magic!"
    scene bathroommorning5
    y "Nope, just enough to get you wet."
    "You stand up and slide your cock into her pussy."
    k "Oh wow!  How do you still have so much energy after last night?"
    y "You're so beautiful!  I feel like I can do this forever!"
    r "Housekeeping!"
    scene bathroommorning6
    r "[y]!!  Kendra!!  Oh my god, I'm so sorry guys!!"
    "You look over and see Rachel, but you don't pull out."
    k "Rachel!  We should have locked the door!"
    scene bathroommorning7
    "You notice Rachel take a step forward rather than a step back.  You wonder how Katrina would use psychology to interpret that."
    r "No, it's my fault!  I didn't think anyone would be having sex in here.  Yesterday Gianna said [y] wasn't dating any of you."
    y "Some things happened last night."
    k "Ummm, yeah we aren't exactly dating yet."
    r "I'll come back to clean in a little while.  Again, I'm so sorry for barging in on you!"
    scene bathroommorning5
    "Rachel leaves and you continue thrusting into Kendra."
    y "We better finish fast before one of the other girls comes looking for us and we get busted again."
    k "I actually came when Rachel was in the room.  I had to bite my lip!"
    y "My turn to cum then!"
    y "You pick up the pace and cum inside her."
    scene bathroommorning3
    k "That's a great way to get up in the morning!  Well other than someone we just met walking in on us!"
    y "Let's get a quick shower and then head to the kitchen.  I think Katrina said something about us going hiking this morning."
    $ renpy.end_replay()
    jump hike1
label hike1:
    scene hike1
    "An hour later Katrina has you in a wilderness area outside of Honolulu."
    kat "You see that mountain across the plains there?"
    kat "On it, there is a trail called the {i}Stairway to Heaven{/i}."
    e "Are we walking all the way over there just to get to the start of the trail?"
    kat "Nope, I'm just pointing it out since it's the most famous trail in Hawaii, unfortunately, it's been deemed too unsafe so it's illegal to go there now."
    kat "So rest assured, we'll be tackling the much easier {i}Aiea Loop Trail{/i} today."
    scene hike15
    kat "It's still kind of dangerous, so be careful of cliff edges as we get higher up.  And look for markers so we don't leave the path."
    e "So like in {i}The Hobbit{/i} when they travel through Mirkwood?  STAY ON THE PATH!"
    kat "Exactly, but there wouldn't be any elves to save us, not even unfriendly ones like in that story."
    scene hike2
    "You fall back a little to get a better view of the girls as they hike in front of you."
    k "Don't think we don't know what you're doing back there [y]!"
    g "We'll let you get away with it for a bit though."
    scene hike3
    "The gentle upward slope isn't too bad, but after a while you still find yourselves getting high above a ravine below."
    g "Look over the edge here guys!"
    e "No way, this is as close as I get!"
    k "I'm with you, Emily!  Heights are the worst!"
    kat "How about if we take a few romantic pictures with [y]?"
    scene hike4
    k "Let's make some memories!"
    e "Lean in like you're gonna kiss."
    y "Like this?"
    e "Perfect!"
    "She snaps a photo on her phone."
    e "I'll send these to everyone so we'll all have them forever."
    scene hike16
    e "Put your arms around Gianna."
    e "That looks great!"
    g "Are you sure you don't want to do this closer to the cliff edge?  It would be more dramatic!"
    y "Very sure!"
    if katdom < 2:
        jump katrinahike1
    else:
        jump katrinahike2

label katrinahike1:
    scene hike10
    kat "My turn for a pic!"
    y "Sure!"
    "She ruffles your hair a bit."
    kat "There, now you look more relaxed!"
    jump hike2

label katrinahike2:
    scene hike9
    kat "Ok, down on your knees for maximum romantic effect!"
    k "That's a weird idea of romance Katrina!"
    "You drop down to your knees."
    kat "Now kiss my feet!  They are tired from the long hike!"
    "Emily snaps a photo."
    kat "Send this to me and [y], and [y], make sure to use this as the wallpaper on your phone."
    jump hike2

label hike2:
    scene hike11
    kat "Ok Emily, you're up!"
    kat "[y], look down into her eyes.  Really try to emphasize your height."
    kat "Emily take that white sweater top off.  I don't like it."
    scene hike12
    kat "Yeah that's perfect.  Smile guys!"
    "She takes the photo."
    scene hike8
    "Since the trail is a long loop you eventually arrive at the halfway point and find the landscape sloping back downwards."
    e "How much further?"
    kat "It's a four-mile hike, so a little under two-miles left."
    g "By the way guys, Rachel mentioned yesterday that her boyfriend gives surfing lessons.  Is that something we maybe want to try?"
    kat "We have a little time tomorrow.  What do you think [y]?"
    y "I feel a little bad since he's apparently addicted to my game."
    g "Yeah she said he's even getting a bit of a belly from all the inactivity."
    y "Well maybe, let's see how we feel tomorrow."
    e "Personally I'm looking forward to our boat tour.  That's what we're doing after this right?"
    k "Yeah that's right."
    scene hike13
    e "In that case let's get there faster!"
    e "Hey Sleipnir, I'm getting tired!  Let me ride on your back!  Ok, my trusty steed?"
    k "Actually I'm getting a little tired too [y].  How about if you carry me instead?"
    menu:
        "Carry Emily [Gr]\[+1 Emily\]":
            jump hike3a
        "Carry Katrina [Gr]\[+1 Katrina Dominance\]":
            jump hike3b
label hike3a:
    $ emily += 1
    y "Sorry Katrina, me and Emily always play around like this.  I wouldn't be a very {i}trusty{/i} steed if I carried someone else!"
    k "Haha, ok fine.  I see how it is!"
    scene hike14
    e "Yay Sleipnir!  I knew you wouldn't let me down!"
    y "Let's go!  Two-miles is nothing to me!"
    scene hike5
    e "I really hope we get a picture of that elusive whale today!"
    y "Me too Emily!"
    "You head down the rest of the trail while Emily goes on about how great winning the grand prize will be."
    jump boattour1

label hike3b:
    $ katdom += 1
    y "Sorry Emily, I carry you around a lot, it's Katrina's turn."
    kat "Thanks [y]!"
    scene hike7
    e "Awwww, first Kendra takes my purple jetski and now Katrina takes my trusty steed!"
    kat "You're a gamer, Emily.  You should be used to losing!"
    e "Low blow Katrina!  Low blow!"
    scene hike6
    "You head down the rest of the trail while Emily goes back and forth between how much her feet hurt and how awesome it'll be to get a picture of the whale later."
    "Katrina whispers in your ear several times about how glad she is you chose to carry her."
    jump boattour1

label boattour1:
    scene boattour1
    alii "Welcome back everyone!  Wow, you guys look great in your swimsuits!"
    kat "Thanks!  They're a little revealing.  I hope that doesn't make you uncomfortable or anything."
    alii "Not at all.  In fact, I was wondering if you mind if I wear a bikini today as well.  Normally I don't get to."
    g "Yeah go for it!"
    k "We don't mind at all."
    alii "Great!  In that case, you guys can go check out the boat from the dock while I go down and change real quick."
    e "No scuba divers to spy on you right?"
    alii "Haha, none that I know of.  It's just you guys again today."
    scene boattour2
    alii "Ok so here it is.  We call her the TARDIS because everyone says it's bigger on the inside!"
    y "Nice {i}Doctor Who{/i} reference!  You're gonna fit in great with our group today!"
    alii "I hope so!  We're gonna probably paint it all blue at some point."
    scene boattour4
    e "Hey Alii, did anyone find that False Killer Whale yet?"
    alii "Nope not yet!"
    e "Awesome!  I've got binoculars today and a whale song playlist ready to go!"
    alii "Let's take your cell below deck.  The hydrophone is under a trapdoor behind the bar.  I'll plug it into the auxiliary cable."
    scene boattour13
    alii "So right back here.  And told you this place looks bigger on the inside!"
    y "Yeah you were right about that.  And can we get some drinks later?"
    alii "Of course, it's included in the price of the tour."
    scene boattour14
    e "Ok here's my phone.  It's on the playlist so just hit play once it's on.  It's a 10-hour loop."
    alii "Sure thing Emily!  I hope we see one and you win the prize!"
    scene boattour5
    "Alii takes you around the outskirts of Oahu, pointing out various landmarks."
    scene boattour7
    "Emily however has her eyes focused out to sea."
    e "Guys shouldn't you stand up for a better view?"
    g "No, we need to have a lower center of gravity to catch you when we hit a wave and you fall."
    scene boattour6
    kat "Do you think they actually stand a chance to find that whale, Alii?"
    alii "I think it's unlikely, but I really hope they do!  We could certainly use the business it would bring in."
    alii "I'll take us to a cove where we'll have the best chance and I'll drop the anchor.  Then I'll make you guys some Mai Tai's if you want."
    k "That sounds lovely."
    scene boattour9
    g "Having fun [y]?"
    y "Yeah actually.  It's great to see Emily so gung-ho to find the whale and win the contest!"
    g "I'm enjoying myself too.  I love being out on the sea with a chance to see something you'd only normally see in an aquarium."
    scene boattour8
    e "Gianna, I'm counting on you to let me know if the type of whale we spot is the right one or not."
    g "Don't worry, Emily.  I won't let you down."
    scene boattour10
    alii "Sea turtle off the starboard bow!"
    e "Wow, how'd he sneak up on us?"
    y "It's because you're looking out to the horizon."
    "You take a picture with your phone."
    g "Look how amazing he is.  These are endangered you know."
    alii "Yeah please don't touch him.  It's a $400 fine.  Not that I'd turn you in, but just please don't ok?"
    g "Oh of course we won't, Alii."
    scene boattour5
    "You see a few more sea creatures, but no whales."
    "After another hour you arrive in a cove Alii mentioned."
    scene boattour11
    alii "I'm dropping anchor.  We'll hang out here for a while and hopefully whatever is down there hears the hydrophone."
    g "The average whale can hear another whale song up to 1,000 miles away."
    scene boattour9
    g "There's even a recorded event where a tagged humpback whale being studied off the coast of Ireland turned towards its mate who was also tagged and being studied in the Caribbean."
    g "4,000 miles away he could hear her."
    y "That's incredible."
    g "Kinda makes you believe in true love."
    scene boattour12
    e "GUYS I THINK I SEE SOMETHING!"
    e "[y] get your phone ready!"
    "PLEASE SAVE YOUR GAME."
    "If you've liked this game and aren't already supporting, please consider supporting me on Patreon at www.patreon.com/obrecht13.  It's only $3 for the current version of the game and it'd really help me a lot."
    "The next update will come out in late October."
    return
