import { QuestNameModel } from '../model/questNameModel';

export class QuestNameBase { constructor(public id: string, public data: QuestNameModel) { } }



export const initQuestNameRepo = () => {
    return [    
        new QuestNameBase("TP Pete2", <QuestNameModel>{"name": "Roll of Anger", "difficulty": 4}),
        new QuestNameBase("Town Marble2", <QuestNameModel>{"name": "Visualizing the Sculpture Within...", "difficulty": 3}),
        new QuestNameBase("Obol Altar1", <QuestNameModel>{"name": "Bad Kitty, get off that altar!", "difficulty": 6}),
        new QuestNameBase("Woodsman2", <QuestNameModel>{"name": "A noob's first swing", "difficulty": 1}),
        new QuestNameBase("Woodsman5", <QuestNameModel>{"name": "A noob's 2nd first swing", "difficulty": 2}),
        new QuestNameBase("Woodsman8", <QuestNameModel>{"name": "It's Just a Plank, Bro!", "difficulty": 3}),
        new QuestNameBase("Scripticus4", <QuestNameModel>{"name": "The Journey Begins!", "difficulty": 1}),
        new QuestNameBase("Scripticus6", <QuestNameModel>{"name": "Hardcore Gamer Status, Here I Come!", "difficulty": 2}),
        new QuestNameBase("Krunk1", <QuestNameModel>{"name": "A Plot to be Perfect", "difficulty": 2}),
        new QuestNameBase("Glumlee3", <QuestNameModel>{"name": "Learning to Swing", "difficulty": 1}),
        new QuestNameBase("Picnic Stowaway5", <QuestNameModel>{"name": "The Hungry Stowaway", "difficulty": 2}),
        new QuestNameBase("Scripticus9", <QuestNameModel>{"name": "Gear Up, Gamer!", "difficulty": 1}),
        new QuestNameBase("Scripticus13", <QuestNameModel>{"name": "Mr. Worldwide", "difficulty": 3}),
        new QuestNameBase("Glumlee6", <QuestNameModel>{"name": "Learning to Smelt", "difficulty": 2}),
        new QuestNameBase("Scripticus17", <QuestNameModel>{"name": "The Choice is Yours!", "difficulty": 1}),
        new QuestNameBase("Hamish2", <QuestNameModel>{"name": "The Hamazing Plot Twist", "difficulty": 2}),
        new QuestNameBase("Mr Pigibank5", <QuestNameModel>{"name": "A Pig and his Stamps", "difficulty": 2}),
        new QuestNameBase("Secretkeeper2", <QuestNameModel>{"name": "The Few, the Proud", "difficulty": 1}),
        new QuestNameBase("Promotheus2", <QuestNameModel>{"name": "I'm Ready, Promotion!", "difficulty": 2}),
        new QuestNameBase("Promotheus10", <QuestNameModel>{"name": "Three Right Answers", "difficulty": 1}),
        new QuestNameBase("Bushlyte1", <QuestNameModel>{"name": "A Peanut for your Thoughts", "difficulty": 1}),
        new QuestNameBase("Bushlyte4", <QuestNameModel>{"name": "Honk if you Love Peanuts!", "difficulty": 2}),
        new QuestNameBase("Bushlyte7", <QuestNameModel>{"name": "A Peanut Saved is a Peanut not Eaten!", "difficulty": 3}),
        new QuestNameBase("Rocklyte2", <QuestNameModel>{"name": "How It's Made, Episode 7. The Super Peanut", "difficulty": 3}),
        new QuestNameBase("Rocklyte5", <QuestNameModel>{"name": "If Life Gives you Peanuts, make Shiny Peanuts!", "difficulty": 4}),
        new QuestNameBase("Rocklyte8", <QuestNameModel>{"name": "Becoming the Best Beginner", "difficulty": 1}),
        new QuestNameBase("Scripticus20", <QuestNameModel>{"name": "Certified Swinger, of Pickaxes of course!", "difficulty": 3}),
        new QuestNameBase("Picnic Stowaway8", <QuestNameModel>{"name": "Beating Up Frogs for some Sauce", "difficulty": 3}),
        new QuestNameBase("Picnic Stowaway12", <QuestNameModel>{"name": "Live-Action Entertainment", "difficulty": 3}),
        new QuestNameBase("Scripticus23", <QuestNameModel>{"name": "The Smithing Grind", "difficulty": 2}),
        new QuestNameBase("Scripticus25", <QuestNameModel>{"name": "Warrior, Archer or Mage?", "difficulty": 4}),
        new QuestNameBase("Glumlee9", <QuestNameModel>{"name": "Literally Burning your Money", "difficulty": 1}),
        new QuestNameBase("Stiltzcho5", <QuestNameModel>{"name": "Outta the Way Slimes", "difficulty": 3}),
        new QuestNameBase("Stiltzcho10", <QuestNameModel>{"name": "No Stone Unturned", "difficulty": 3}),
        new QuestNameBase("Stiltzcho16", <QuestNameModel>{"name": "Investigator by Day, Prankster by Night", "difficulty": 4}),
        new QuestNameBase("Scripticus33", <QuestNameModel>{"name": "Stiltzcho, the Leaf Scout", "difficulty": 5}),
        new QuestNameBase("Picnic Stowaway21", <QuestNameModel>{"name": "The Most Important Meal of the Day", "difficulty": 2}),
        new QuestNameBase("Picnic Stowaway24", <QuestNameModel>{"name": "Brunchin' with the Blobs", "difficulty": 3}),
        new QuestNameBase("Picnic Stowaway27", <QuestNameModel>{"name": "Luncheon with the Inlaws", "difficulty": 4}),
        new QuestNameBase("Picnic Stowaway30", <QuestNameModel>{"name": "Afternoon Tea in a Jiffy", "difficulty": 4}),
        new QuestNameBase("Picnic Stowaway33", <QuestNameModel>{"name": "Early Evening Eating Endeavor", "difficulty": 5}),
        new QuestNameBase("Picnic Stowaway37", <QuestNameModel>{"name": "The Last Supper, at Least for Today!", "difficulty": 5}),
        new QuestNameBase("Picnic Stowaway40", <QuestNameModel>{"name": "Don't Desert the Dessert", "difficulty": 5}),
        new QuestNameBase("Picnic Stowaway44", <QuestNameModel>{"name": "A Midnight Snack", "difficulty": 6}),
        new QuestNameBase("Picnic Stowaway47", <QuestNameModel>{"name": "King of Food", "difficulty": 8}),
        new QuestNameBase("Tiki Chief5", <QuestNameModel>{"name": "Brochure Building", "difficulty": 3}),
        new QuestNameBase("Tiki Chief8", <QuestNameModel>{"name": "Three Strikes, you're Out!", "difficulty": 3}),
        new QuestNameBase("Tiki Chief11", <QuestNameModel>{"name": "Blame it on the Glublins", "difficulty": 4}),
        new QuestNameBase("Scripticus39", <QuestNameModel>{"name": "What Lies at the Heart of the Forest", "difficulty": 2}),
        new QuestNameBase("Scripticus42", <QuestNameModel>{"name": "The Bigger they are, the Bigger they Fall!", "difficulty": 3}),
        new QuestNameBase("Scripticus47", <QuestNameModel>{"name": "Champion of the Grasslands", "difficulty": 9}),
        new QuestNameBase("Builder Bird1", <QuestNameModel>{"name": "Restoring Power to the Portal", "difficulty": 4}),
        new QuestNameBase("Mutton3", <QuestNameModel>{"name": "Beatboxing Starterpack", "difficulty": 4}),
        new QuestNameBase("Hamish6", <QuestNameModel>{"name": "Should We Tell Him?", "difficulty": 2}),
        new QuestNameBase("Funguy2", <QuestNameModel>{"name": "Mushroom Munchies", "difficulty": 3}),
        new QuestNameBase("Funguy6", <QuestNameModel>{"name": "Videogame Highscores are COOL!", "difficulty": 3}),
        new QuestNameBase("Dog Bone (NPC)3", <QuestNameModel>{"name": "Why he Die???", "difficulty": 2}),
        new QuestNameBase("Speccius1", <QuestNameModel>{"name": "More like 'Sleepius' lmao", "difficulty": 3}),
        new QuestNameBase("Speccius8", <QuestNameModel>{"name": "Specialization Station", "difficulty": 1}),
        new QuestNameBase("Whattso1", <QuestNameModel>{"name": "Mopey Dick", "difficulty": 1}),
        new QuestNameBase("Whattso4", <QuestNameModel>{"name": "The Whaley Hard Minigame", "difficulty": 3}),
        new QuestNameBase("Scubidew2", <QuestNameModel>{"name": "Don't Step to Me, Bro!", "difficulty": 2}),
        new QuestNameBase("Fishpaste973", <QuestNameModel>{"name": "'Accidental' Exploit", "difficulty": 3}),
        new QuestNameBase("Postboy Pablob2", <QuestNameModel>{"name": "Signed, Sealed and Lost in the Post", "difficulty": 6}),
        new QuestNameBase("TP Pete5", <QuestNameModel>{"name": "The Rats are to Blame!", "difficulty": 3}),
        new QuestNameBase("TP Pete10", <QuestNameModel>{"name": "Fired for BS Reasons!", "difficulty": 5}),
        new QuestNameBase("Sprout3", <QuestNameModel>{"name": "Sticks and Stone Something Something Bones...", "difficulty": 5}),
        new QuestNameBase("Sprout6", <QuestNameModel>{"name": "Justice Wears No Clothes", "difficulty": 4}),
        new QuestNameBase("Sprout9", <QuestNameModel>{"name": "Shoe Shopping with Sprout", "difficulty": 3}),
        new QuestNameBase("Sprout12", <QuestNameModel>{"name": "Frisbee Fanatic", "difficulty": 7}),
        new QuestNameBase("Krunk4", <QuestNameModel>{"name": "The Scientific Method, According to a Rock", "difficulty": 4}),
        new QuestNameBase("Krunk8", <QuestNameModel>{"name": "King of the Cavern", "difficulty": 5}),
        new QuestNameBase("Glumlee17", <QuestNameModel>{"name": "The Impossible Task", "difficulty": 7}),
        new QuestNameBase("Desert Davey1", <QuestNameModel>{"name": "More Tasks Pls", "difficulty": 1}),
        new QuestNameBase("Cowbo Jones1", <QuestNameModel>{"name": "The Grind Begins...?", "difficulty": 1}),
        new QuestNameBase("Cowbo Jones4", <QuestNameModel>{"name": "The Hatless Howerhouse!", "difficulty": 3}),
        new QuestNameBase("Cowbo Jones7", <QuestNameModel>{"name": "No Country for One Character", "difficulty": 4}),
        new QuestNameBase("Cowbo Jones12", <QuestNameModel>{"name": "Say Goodbye to your Dubloon!", "difficulty": 2}),
        new QuestNameBase("Cowbo Jones19", <QuestNameModel>{"name": "Alchemial Apprentice", "difficulty": 3}),
        new QuestNameBase("Cowbo Jones22", <QuestNameModel>{"name": "Three Vials? Those are Rookie Numbers!", "difficulty": 2}),
        new QuestNameBase("Cowbo Jones24", <QuestNameModel>{"name": "The Notorious B.O.B", "difficulty": 4}),
        new QuestNameBase("Cowbo Jones27", <QuestNameModel>{"name": "Bake Him Away, Toys", "difficulty": 5}),
        new QuestNameBase("Cowbo Jones33", <QuestNameModel>{"name": "A Hat in Crime", "difficulty": 4}),
        new QuestNameBase("Cowbo Jones38", <QuestNameModel>{"name": "Commence Criminal Crimes!", "difficulty": 6}),
        new QuestNameBase("Loominadi3", <QuestNameModel>{"name": "Rhyming is Key!", "difficulty": 4}),
        new QuestNameBase("Loominadi6", <QuestNameModel>{"name": "Uh, Something About Vials?", "difficulty": 5}),
        new QuestNameBase("Loominadi10", <QuestNameModel>{"name": "Journey to the Center of the Blundermines", "difficulty": 5}),
        new QuestNameBase("Goldric4", <QuestNameModel>{"name": "Trickle Down Economics", "difficulty": 2}),
        new QuestNameBase("Djonnut2", <QuestNameModel>{"name": "Genie Dieting", "difficulty": 4}),
        new QuestNameBase("Bandit Bob7", <QuestNameModel>{"name": "Bullets for Bandit Bob!", "difficulty": 3}),
        new QuestNameBase("Bandit Bob10", <QuestNameModel>{"name": "Bob's Brand New Bandana", "difficulty": 2}),
        new QuestNameBase("Bandit Bob14", <QuestNameModel>{"name": "Bringing Bob's Boxes", "difficulty": 3}),
        new QuestNameBase("Hamish10", <QuestNameModel>{"name": "Slime for Storage", "difficulty": 4}),
        new QuestNameBase("Promotheus17", <QuestNameModel>{"name": "Slovakian Scare", "difficulty": 5}),
        new QuestNameBase("Promotheus20", <QuestNameModel>{"name": "The Witcher, but not Really", "difficulty": 5}),
        new QuestNameBase("Funguy9", <QuestNameModel>{"name": "Partycrastination", "difficulty": 6}),
        new QuestNameBase("Funguy12", <QuestNameModel>{"name": "Party Crashin'", "difficulty": 4}),
        new QuestNameBase("Funguy14", <QuestNameModel>{"name": "Wicked Party Cleanup", "difficulty": 5}),
        new QuestNameBase("Tiki Chief14", <QuestNameModel>{"name": "Hotel? Tikivago. Sorry, couldn't Help It!", "difficulty": 4}),
        new QuestNameBase("Papua Piggea7", <QuestNameModel>{"name": "Crystal Crime Stopper", "difficulty": 4}),
        new QuestNameBase("Papua Piggea10", <QuestNameModel>{"name": "Stamp Collecting", "difficulty": 6}),
        new QuestNameBase("Papua Piggea13", <QuestNameModel>{"name": "This Little Piggy Felt Remorse", "difficulty": 5}),
        new QuestNameBase("Mutton6", <QuestNameModel>{"name": "Clout Chasin'", "difficulty": 3}),
        new QuestNameBase("Mutton9", <QuestNameModel>{"name": "Cross Platform Promotion", "difficulty": 5}),
        new QuestNameBase("Mutton12", <QuestNameModel>{"name": "7 Figure Followers", "difficulty": 8}),
        new QuestNameBase("Papua Piggea3", <QuestNameModel>{"name": "Oinko Boinko", "difficulty": 3}),
        new QuestNameBase("Goldric8", <QuestNameModel>{"name": "Hoopsies", "difficulty": 2}),
        new QuestNameBase("Goldric11", <QuestNameModel>{"name": "Only Winners have Portraits", "difficulty": 3}),
        new QuestNameBase("Goldric14", <QuestNameModel>{"name": "Criminal Code of Conduct", "difficulty": 5}),
        new QuestNameBase("Goldric17", <QuestNameModel>{"name": "Dress to Impress", "difficulty": 4}),
        new QuestNameBase("Cowbo Jones44", <QuestNameModel>{"name": "The Worst Trade Deal in History", "difficulty": 3}),
        new QuestNameBase("Cowbo Jones47", <QuestNameModel>{"name": "Children? What'd they ever do for Me...", "difficulty": 4}),
        new QuestNameBase("Cowbo Jones50", <QuestNameModel>{"name": "Oh No, not the Elderly!", "difficulty": 6}),
        new QuestNameBase("Carpetiem5", <QuestNameModel>{"name": "Darn Lazy Gamers!", "difficulty": 3}),
        new QuestNameBase("Carpetiem9", <QuestNameModel>{"name": "Old Timey Craftin'", "difficulty": 4}),
        new QuestNameBase("Carpetiem13", <QuestNameModel>{"name": "Be like Buster!", "difficulty": 3}),
        new QuestNameBase("Typhoon2", <QuestNameModel>{"name": "Surprise Attack!", "difficulty": 2}),
        new QuestNameBase("Scubidew5", <QuestNameModel>{"name": "Uncovering the Deep Sea State!!!", "difficulty": 3}),
        new QuestNameBase("Desert Davey4", <QuestNameModel>{"name": "U Cool?", "difficulty": 4}),
        new QuestNameBase("Giftmas Blobulyte4", <QuestNameModel>{"name": "Boo, Headshot!", "difficulty": 2}),
        new QuestNameBase("Giftmas Blobulyte7", <QuestNameModel>{"name": "You Shouldn't Have! No, really.", "difficulty": 2}),
        new QuestNameBase("Meel3", <QuestNameModel>{"name": "Spooky Scary Skelepoops", "difficulty": 3}),
        new QuestNameBase("Meel6", <QuestNameModel>{"name": "Waitin' for the Cards to Drop", "difficulty": 7}),
        new QuestNameBase("Wellington3", <QuestNameModel>{"name": "Platforms in Disguise, Platsformers!", "difficulty": 4}),
        new QuestNameBase("Wellington6", <QuestNameModel>{"name": "Findin' Fingerprints", "difficulty": 4}),
        new QuestNameBase("Wellington10", <QuestNameModel>{"name": "You Can't Run, but you Can Hide", "difficulty": 1}),
        new QuestNameBase("XxX Cattleprod XxX3", <QuestNameModel>{"name": "Peak Gaming", "difficulty": 3}),
        new QuestNameBase("XxX Cattleprod XxX6", <QuestNameModel>{"name": "Wait No, I meant Pathetic Gaming", "difficulty": 5}),
        new QuestNameBase("XxX Cattleprod XxX11", <QuestNameModel>{"name": "Ok, NOW it's Peak Gaming!", "difficulty": 5}),
        new QuestNameBase("Djonnut5", <QuestNameModel>{"name": "I'm Blue Dabadedada", "difficulty": 4}),
        new QuestNameBase("Snake Jar3", <QuestNameModel>{"name": "Lookin' Like a Snack", "difficulty": 3}),
        new QuestNameBase("Snake Jar6", <QuestNameModel>{"name": "Red Stuff Bad!", "difficulty": 3}),
        new QuestNameBase("Snake Jar9", <QuestNameModel>{"name": "PSA. You Are Being Eaten!", "difficulty": 4}),
        new QuestNameBase("Scripticus52", <QuestNameModel>{"name": "Can't somebody else do it?", "difficulty": 2}),
        new QuestNameBase("Centurion2", <QuestNameModel>{"name": "Down The Mimic Hole!", "difficulty": 3}),
        new QuestNameBase("Centurion7", <QuestNameModel>{"name": "Which one of yous is the Mafia?", "difficulty": 3}),
        new QuestNameBase("Centurion11", <QuestNameModel>{"name": "High Scorer", "difficulty": 4}),
        new QuestNameBase("Centurion15", <QuestNameModel>{"name": "Colosseum Champ!", "difficulty": 5}),
        new QuestNameBase("Centurion19", <QuestNameModel>{"name": "Colosseum GDQ", "difficulty": 6}),
        new QuestNameBase("Telescope4", <QuestNameModel>{"name": "I'm Seeing Stars!", "difficulty": 2}),
        new QuestNameBase("Loveulyte2", <QuestNameModel>{"name": "Heart Hogger", "difficulty": 2}),
        new QuestNameBase("Loveulyte5", <QuestNameModel>{"name": "Heartbreaker", "difficulty": 4}),
        new QuestNameBase("Constructor Crow2", <QuestNameModel>{"name": "Restoring Power to another Portal", "difficulty": 7}),
        new QuestNameBase("Iceland Irwin2", <QuestNameModel>{"name": "Crikey, it's cold out!", "difficulty": 4}),
        new QuestNameBase("Woodsman12", <QuestNameModel>{"name": "Exotic Pranks... I mean Logs!", "difficulty": 5}),
        new QuestNameBase("Glumlee24", <QuestNameModel>{"name": "He's Havin' a Bad Day", "difficulty": 2}),
        new QuestNameBase("Stiltzcho23", <QuestNameModel>{"name": "Time Crime Episode 1", "difficulty": 2}),
        new QuestNameBase("Stiltzcho26", <QuestNameModel>{"name": "Time Crime Episode 2", "difficulty": 2}),
        new QuestNameBase("Stiltzcho29", <QuestNameModel>{"name": "Time Crime Season Finale", "difficulty": 3}),
        new QuestNameBase("Dazey3", <QuestNameModel>{"name": "Dressing like a Dork", "difficulty": 5}),
        new QuestNameBase("Dazey9", <QuestNameModel>{"name": "Literally Physics", "difficulty": 4}),
        new QuestNameBase("Dog Bone (NPC)14", <QuestNameModel>{"name": "Bow Wow going Dow..n!", "difficulty": 3}),
        new QuestNameBase("Egggulyte3", <QuestNameModel>{"name": "Egg Shaped Lootboxes!", "difficulty": 2}),
        new QuestNameBase("Egggulyte7", <QuestNameModel>{"name": "I've Got a Golden Tickegg!", "difficulty": 4}),
        new QuestNameBase("Lord of the Hunt3", <QuestNameModel>{"name": "Pelt for the Pelt God", "difficulty": 2}),
        new QuestNameBase("Lord of the Hunt7", <QuestNameModel>{"name": "Frogecoin to the MOON!", "difficulty": 2}),
        new QuestNameBase("Lord of the Hunt10", <QuestNameModel>{"name": "Yet another Cartoon Reference", "difficulty": 3}),
        new QuestNameBase("Lord of the Hunt13", <QuestNameModel>{"name": "Small Stingers, Big Owie", "difficulty": 4}),
        new QuestNameBase("Lord of the Hunt16", <QuestNameModel>{"name": "The Mouse n the Molerat", "difficulty": 4}),
        new QuestNameBase("Lord of the Hunt19", <QuestNameModel>{"name": "Happy Tree Friend", "difficulty": 5}),
        new QuestNameBase("Lord of the Hunt22", <QuestNameModel>{"name": "Noot Noot!", "difficulty": 6}),
        new QuestNameBase("Lord of the Hunt25", <QuestNameModel>{"name": "Bunny you Should Say That!", "difficulty": 7}),
        new QuestNameBase("Lord of the Hunt28", <QuestNameModel>{"name": "Rollin' Thunder!", "difficulty": 7}),
        new QuestNameBase("Lord of the Hunt31", <QuestNameModel>{"name": "Untitled Quest", "difficulty": 7}),
        new QuestNameBase("Lord of the Hunt35", <QuestNameModel>{"name": "To Trap or not to Trap", "difficulty": 7}),
        new QuestNameBase("Hoggindaz3", <QuestNameModel>{"name": "Turn ON for what???", "difficulty": 1}),
        new QuestNameBase("Hoggindaz7", <QuestNameModel>{"name": "Trapping with the Lord", "difficulty": 4}),
        new QuestNameBase("Hoggindaz10", <QuestNameModel>{"name": "Constructing a Tower", "difficulty": 3}),
        new QuestNameBase("Hoggindaz15", <QuestNameModel>{"name": "Monke Tower Time!", "difficulty": 2}),
        new QuestNameBase("Hoggindaz19", <QuestNameModel>{"name": "Taking Samples", "difficulty": 1}),
        new QuestNameBase("Lonely Hunter2", <QuestNameModel>{"name": "Leaf Him Alone!", "difficulty": 3}),
        new QuestNameBase("Lonely Hunter5", <QuestNameModel>{"name": "Skeleton? Skelegone!", "difficulty": 4}),
        new QuestNameBase("Snouts5", <QuestNameModel>{"name": "A Salty Fall", "difficulty": 4}),
        new QuestNameBase("Snouts8", <QuestNameModel>{"name": "Gravity VS Salt", "difficulty": 5}),
        new QuestNameBase("Snouts12", <QuestNameModel>{"name": "Big Ol Chonker", "difficulty": 5}),
        new QuestNameBase("Carpetiem17", <QuestNameModel>{"name": "Helping 100 times over", "difficulty": 2}),
        new QuestNameBase("Cowbo Jones54", <QuestNameModel>{"name": "Tomb Raid", "difficulty": 5}),
        new QuestNameBase("Cowbo Jones59", <QuestNameModel>{"name": "The New Sheriff", "difficulty": 9}),
        new QuestNameBase("Bandit Bob19", <QuestNameModel>{"name": "The Desert Dungeon Prequest", "difficulty": 2}),
        new QuestNameBase("Snake Jar16", <QuestNameModel>{"name": "A Noob, served Medium Rare!", "difficulty": 2}),
        new QuestNameBase("Whattso7", <QuestNameModel>{"name": "Bobbin' Bobbers", "difficulty": 4}),
        new QuestNameBase("Whattso10", <QuestNameModel>{"name": "The Biggest Fish in the Sea...?", "difficulty": 6}),
        new QuestNameBase("Goldric24", <QuestNameModel>{"name": "Dont lay a finger on my Sheepies!!!", "difficulty": 4}),
        new QuestNameBase("Loominadi15", <QuestNameModel>{"name": "The Mummy of Mystery", "difficulty": 7}),
        new QuestNameBase("Djonnut13", <QuestNameModel>{"name": "The Blue New World", "difficulty": 4}),
        new QuestNameBase("Wellington15", <QuestNameModel>{"name": "Puzzles and Math, a Winning Combination!", "difficulty": 5}),
        new QuestNameBase("Scubidew11", <QuestNameModel>{"name": "A Normal Quest.", "difficulty": 1}),
        new QuestNameBase("Fishpaste978", <QuestNameModel>{"name": "Can you do the Can Can?", "difficulty": 4}),
        new QuestNameBase("Cactolyte5", <QuestNameModel>{"name": "Super Skillage", "difficulty": 4}),
        new QuestNameBase("Cactolyte8", <QuestNameModel>{"name": "Top Skillage", "difficulty": 6}),
        new QuestNameBase("Cactolyte11", <QuestNameModel>{"name": "Peanut De-Aging", "difficulty": 5}),
        new QuestNameBase("Cactolyte15", <QuestNameModel>{"name": "Maestro! The Stro! Mman!", "difficulty": 1}),
        new QuestNameBase("Coastiolyte2", <QuestNameModel>{"name": "Cooler than a Cooler!", "difficulty": 2}),
        new QuestNameBase("Coastiolyte5", <QuestNameModel>{"name": "Vibe Check", "difficulty": 2}),
        new QuestNameBase("Walupiggy1", <QuestNameModel>{"name": "Treasure Hunt 1", "difficulty": 2}),
        new QuestNameBase("Walupiggy4", <QuestNameModel>{"name": "Treasure Hunt 2", "difficulty": 3}),
        new QuestNameBase("Walupiggy7", <QuestNameModel>{"name": "Treasure Hunt 3", "difficulty": 4}),
        new QuestNameBase("Walupiggy10", <QuestNameModel>{"name": "Treasure Hunt 4", "difficulty": 5}),
        new QuestNameBase("Toadstall4", <QuestNameModel>{"name": "Creating a Party!", "difficulty": 1}),
        new QuestNameBase("Toadstall7", <QuestNameModel>{"name": "Bigger Party Better Party!", "difficulty": 1}),
        new QuestNameBase("Toadstall10", <QuestNameModel>{"name": "Bother the Frogger!", "difficulty": 1}),
        new QuestNameBase("Gangster Gus2", <QuestNameModel>{"name": "Plunderin Down Yonder", "difficulty": 1}),
        new QuestNameBase("Gangster Gus5", <QuestNameModel>{"name": "Perfect Progress Score", "difficulty": 3}),
        new QuestNameBase("Gangster Gus10", <QuestNameModel>{"name": "Sanke Revival Denial", "difficulty": 5}),
        new QuestNameBase("Falloween Pumpkin3", <QuestNameModel>{"name": "The Spookyness", "difficulty": 1}),
        new QuestNameBase("Falloween Pumpkin6", <QuestNameModel>{"name": "The Scaryness", "difficulty": 3}),
        new QuestNameBase("Falloween Pumpkin9", <QuestNameModel>{"name": "The Horroriness", "difficulty": 5}),
        new QuestNameBase("Falloween Pumpkin12", <QuestNameModel>{"name": "The Booeyness", "difficulty": 7}),
        new QuestNameBase("Falloween Pumpkin15", <QuestNameModel>{"name": "The Afterparty", "difficulty": 7}),
        new QuestNameBase("Lonely Hunter8", <QuestNameModel>{"name": "Opening Chests", "difficulty": 4}),
        new QuestNameBase("Snouts16", <QuestNameModel>{"name": "Mana Plox", "difficulty": 5}),
        new QuestNameBase("Hoggindaz25", <QuestNameModel>{"name": "Voter Recognition", "difficulty": 3}),
        new QuestNameBase("Hoggindaz28", <QuestNameModel>{"name": "Voter Appeasement", "difficulty": 5}),
        new QuestNameBase("Hoggindaz31", <QuestNameModel>{"name": "Voter Apathy", "difficulty": 6}),
        new QuestNameBase("Hoggindaz36", <QuestNameModel>{"name": "Chizoar No More", "difficulty": 5}),
        new QuestNameBase("Hoggindaz39", <QuestNameModel>{"name": "The Fresh Prince of the Tundra", "difficulty": 1}),
        new QuestNameBase("Shuvelle3", <QuestNameModel>{"name": "Mayoral Luck", "difficulty": 3}),
        new QuestNameBase("Shuvelle6", <QuestNameModel>{"name": "Mayoral Skill", "difficulty": 4}),
        new QuestNameBase("Shuvelle9", <QuestNameModel>{"name": "Mayoral Sack Size", "difficulty": 6}),
        new QuestNameBase("Shuvelle12", <QuestNameModel>{"name": "Mayoral Movie Taste", "difficulty": 5}),
        new QuestNameBase("Shuvelle15", <QuestNameModel>{"name": "Diggy Hole!", "difficulty": 3}),
        new QuestNameBase("Shuvelle18", <QuestNameModel>{"name": "Diggy Diggy Hole!", "difficulty": 4}),
        new QuestNameBase("Shuvelle21", <QuestNameModel>{"name": "Dig Diggily Diggy Dig Dig Hole!", "difficulty": 5}),
        new QuestNameBase("Yondergreen3", <QuestNameModel>{"name": "Infrastructure Plan", "difficulty": 2}),
        new QuestNameBase("Yondergreen6", <QuestNameModel>{"name": "Economic Policy", "difficulty": 3}),
        new QuestNameBase("Yondergreen9", <QuestNameModel>{"name": "Stance on Big Tech", "difficulty": 4}),
        new QuestNameBase("Yondergreen12", <QuestNameModel>{"name": "Legislative Action", "difficulty": 5}),
        new QuestNameBase("Yondergreen16", <QuestNameModel>{"name": "No Snapping Contract", "difficulty": 2}),
        new QuestNameBase("Yondergreen19", <QuestNameModel>{"name": "Keep Away Contract", "difficulty": 4}),
        new QuestNameBase("Yondergreen22", <QuestNameModel>{"name": "Ad Solidarity Contract", "difficulty": 7}),
        new QuestNameBase("Bill Brr2", <QuestNameModel>{"name": "Fairly Odd Damage", "difficulty": 4}),
        new QuestNameBase("Bill Brr5", <QuestNameModel>{"name": "Laughin' Amphibian", "difficulty": 2}),
        new QuestNameBase("Bill Brr9", <QuestNameModel>{"name": "The Spores are a Bore", "difficulty": 3}),
        new QuestNameBase("Bill Brr12", <QuestNameModel>{"name": "Coin Shenanigans", "difficulty": 3}),
        new QuestNameBase("Bill Brr15", <QuestNameModel>{"name": "Have a Candy", "difficulty": 3}),
        new QuestNameBase("Bill Brr18", <QuestNameModel>{"name": "Duckin' and Shatterin'", "difficulty": 5}),
        new QuestNameBase("Bill Brr21", <QuestNameModel>{"name": "Hatin' on the Green One", "difficulty": 8}),
        new QuestNameBase("Bellows1", <QuestNameModel>{"name": "Poking Some Eyes Out", "difficulty": 2}),
        new QuestNameBase("Bellows4", <QuestNameModel>{"name": "Eyexperience", "difficulty": 5}),
        new QuestNameBase("Bellows7", <QuestNameModel>{"name": "Veyebing", "difficulty": 4}),
        new QuestNameBase("Bellows10", <QuestNameModel>{"name": "Optometric Hoarder", "difficulty": 6}),
        new QuestNameBase("Crystalswine6", <QuestNameModel>{"name": "Melting the Snakes", "difficulty": 4}),
        new QuestNameBase("Crystalswine9", <QuestNameModel>{"name": "Sunrunning to Chizoar", "difficulty": 6}),
        new QuestNameBase("Crystalswine12", <QuestNameModel>{"name": "Global Warming", "difficulty": 7}),
        new QuestNameBase("Worldo4", <QuestNameModel>{"name": "Odd Jobs for Cold Hard Cash", "difficulty": 3}),
        new QuestNameBase("Worldo7", <QuestNameModel>{"name": "Can't Guard if you're Dead!", "difficulty": 6}),
        new QuestNameBase("Giftmas Blobulyte11", <QuestNameModel>{"name": "Giftmas Time!", "difficulty": 2}),
        new QuestNameBase("Carpenter Cardinal1", <QuestNameModel>{"name": "Restoring Power, once again, to a Portal", "difficulty": 8}),
        new QuestNameBase("Gobo3", <QuestNameModel>{"name": "Breeding in Outer Space", "difficulty": 1}),
        new QuestNameBase("Gobo6", <QuestNameModel>{"name": "Intense Pet Fighting", "difficulty": 1}),
        new QuestNameBase("Gobo9", <QuestNameModel>{"name": "Squirrel Tactics", "difficulty": 1}),
        new QuestNameBase("Gobo12", <QuestNameModel>{"name": "Spicy Cooking", "difficulty": 1}),
        new QuestNameBase("Gobo16", <QuestNameModel>{"name": "Lab Experimentation, Ft. You", "difficulty": 1}),
        new QuestNameBase("Oinkin2", <QuestNameModel>{"name": "Filling the Menu", "difficulty": 1}),
        new QuestNameBase("Oinkin5", <QuestNameModel>{"name": "Diner Deliverer", "difficulty": 1}),
        new QuestNameBase("Oinkin8", <QuestNameModel>{"name": "Recipe for Fattening Pastry", "difficulty": 1}),
        new QuestNameBase("Capital P2", <QuestNameModel>{"name": "Right side wrong side!", "difficulty": 3}),
        new QuestNameBase("Capital P5", <QuestNameModel>{"name": "No room on the Dance Floor!", "difficulty": 4}),
        new QuestNameBase("Capital P8", <QuestNameModel>{"name": "Everybody move it move it!", "difficulty": 6}),
        new QuestNameBase("Blobbo1", <QuestNameModel>{"name": "A Honker Took mah Baby!", "difficulty": 4}),
        new QuestNameBase("Blobbo4", <QuestNameModel>{"name": "Glitter Critter", "difficulty": 5}),
        new QuestNameBase("Nebula Neddy2", <QuestNameModel>{"name": "Task Requirement Affirmative", "difficulty": 4}),
        new QuestNameBase("Eliteus2", <QuestNameModel>{"name": "The Greenie Gucci Gang", "difficulty": 5}),
        new QuestNameBase("Eliteus4", <QuestNameModel>{"name": "Elite Class for the Elites in Class", "difficulty": 5}),
        new QuestNameBase("Slargon3", <QuestNameModel>{"name": "Shut up the Namecallers!", "difficulty": 2}),
        new QuestNameBase("Slargon6", <QuestNameModel>{"name": "Smack the meanies!", "difficulty": 4}),
        new QuestNameBase("Slargon9", <QuestNameModel>{"name": "Mess with the Misters!", "difficulty": 5}),
        new QuestNameBase("Slargon12", <QuestNameModel>{"name": "Assert Dominance over the Meek!", "difficulty": 7}),
        new QuestNameBase("Pirate Porkchop2", <QuestNameModel>{"name": "Bring me the Booty", "difficulty": 2}),
        new QuestNameBase("Pirate Porkchop5", <QuestNameModel>{"name": "Sailing for some Sparks", "difficulty": 3}),
        new QuestNameBase("Pirate Porkchop8", <QuestNameModel>{"name": "Seeking Treasure Shrooms", "difficulty": 6}),
        new QuestNameBase("Pirate Porkchop11", <QuestNameModel>{"name": "Ye finest treasure at once!", "difficulty": 8}),
        new QuestNameBase("Poigu1", <QuestNameModel>{"name": "Think twice speak once", "difficulty": 3}),
        new QuestNameBase("Poigu4", <QuestNameModel>{"name": "Speak from the heart not the mind", "difficulty": 5}),
        new QuestNameBase("Poigu7", <QuestNameModel>{"name": "Learn the Language of the Universe", "difficulty": 8}),
        new QuestNameBase("Muhmuguh2", <QuestNameModel>{"name": "Wave after wave slowly Sailing", "difficulty": 1}),
        new QuestNameBase("Muhmuguh6", <QuestNameModel>{"name": "Rising up and Growing as a Gamer", "difficulty": 1}),
        new QuestNameBase("Muhmuguh10", <QuestNameModel>{"name": "Learn the Language of the Universe", "difficulty": 2}),
        new QuestNameBase("Lava Larry2", <QuestNameModel>{"name": "W5 Task Req Check", "difficulty": 4}),
        new QuestNameBase("Rift Ripper4", <QuestNameModel>{"name": "Entering The Rift...", "difficulty": 3}),
        new QuestNameBase("Nebulyte3", <QuestNameModel>{"name": "Species Slayer", "difficulty": 7}),
        new QuestNameBase("Nebulyte6", <QuestNameModel>{"name": "Chizoar Slayer", "difficulty": 7}),
        new QuestNameBase("Nebulyte9", <QuestNameModel>{"name": "Oh Geez Lets Not Think About This One...", "difficulty": 7}),
        new QuestNameBase("Nebulyte12", <QuestNameModel>{"name": "VMAN ACHIEVED!", "difficulty": 1}),
        new QuestNameBase("Bubbulyte2", <QuestNameModel>{"name": "Spring Splendor", "difficulty": 5}),
        new QuestNameBase("Tired Mole2", <QuestNameModel>{"name": "Establishing Order among Molekind", "difficulty": 3}),
        new QuestNameBase("Tired Mole5", <QuestNameModel>{"name": "Like taking Keys from a Crawler", "difficulty": 5}),
        new QuestNameBase("Tired Mole8", <QuestNameModel>{"name": "Divine Endeavor", "difficulty": 1}),
        new QuestNameBase("Omar Da Ogar2", <QuestNameModel>{"name": "Helping Omar", "difficulty": 2}),
        new QuestNameBase("Omar Da Ogar5", <QuestNameModel>{"name": "Helping Omar Again", "difficulty": 3}),
        new QuestNameBase("Omar Da Ogar8", <QuestNameModel>{"name": "Helping Omar A 3rd Time", "difficulty": 4}),
        new QuestNameBase("Omar Da Ogar11", <QuestNameModel>{"name": "Helping Omar Some More", "difficulty": 5}),
        new QuestNameBase("Omar Da Ogar14", <QuestNameModel>{"name": "Helping Omar Yet Again Deja Vu", "difficulty": 6}),
        new QuestNameBase("Omar Da Ogar17", <QuestNameModel>{"name": "Helping Omar For the Final Time", "difficulty": 7}),
        new QuestNameBase("Monolith1", <QuestNameModel>{"name": "Surface Level Jealousy", "difficulty": 2}),
        new QuestNameBase("Monolith4", <QuestNameModel>{"name": "Onyx Statue Crafting", "difficulty": 6}),
        new QuestNameBase("Monolith7", <QuestNameModel>{"name": "A Lack of Modesty", "difficulty": 9}),
        new QuestNameBase("Royal Worm4", <QuestNameModel>{"name": "Let the Tails Hit the Floor", "difficulty": 2}),
        new QuestNameBase("Royal Worm7", <QuestNameModel>{"name": "Bothering Mutants", "difficulty": 4}),
        new QuestNameBase("Royal Worm10", <QuestNameModel>{"name": "Royal Score", "difficulty": 5}),
        new QuestNameBase("Royal Worm13", <QuestNameModel>{"name": "Downfall of the Hammer Things", "difficulty": 4}),
        new QuestNameBase("Royal Worm16", <QuestNameModel>{"name": "Kickin' the Can", "difficulty": 6}),
        new QuestNameBase("Royal Worm19", <QuestNameModel>{"name": "A Royal Gift", "difficulty": 7}),
        new QuestNameBase("Royal Worm22", <QuestNameModel>{"name": "Bossin' the Boss", "difficulty": 8}),
        new QuestNameBase("Royal Worm28", <QuestNameModel>{"name": "Normie Bidding", "difficulty": 7}),
        new QuestNameBase("Royal Worm32", <QuestNameModel>{"name": "Royal Bidding", "difficulty": 1}),
        new QuestNameBase("Lafu Shi2", <QuestNameModel>{"name": "Seed Planting", "difficulty": 1}),
        new QuestNameBase("Lafu Shi5", <QuestNameModel>{"name": "Visiting the Farmer's Market", "difficulty": 1}),
        new QuestNameBase("Lafu Shi8", <QuestNameModel>{"name": "Climbing the Ninja Hotel", "difficulty": 1}),
        new QuestNameBase("Lafu Shi11", <QuestNameModel>{"name": "Emporium Investing", "difficulty": 1}),
        new QuestNameBase("Lafu Shi14", <QuestNameModel>{"name": "Summoning Debut", "difficulty": 1}),
        new QuestNameBase("Lafu Shi17", <QuestNameModel>{"name": "Essence Juicing", "difficulty": 1}),
        new QuestNameBase("Hoov2", <QuestNameModel>{"name": "Sneak Dropout", "difficulty": 1}),
        new QuestNameBase("Hoov5", <QuestNameModel>{"name": "Stealth Check 1 2 3", "difficulty": 3}),
        new QuestNameBase("Hoov8", <QuestNameModel>{"name": "Sneak Registration", "difficulty": 5}),
        new QuestNameBase("Hoov11", <QuestNameModel>{"name": "Sneak Graduate", "difficulty": 8}),
        new QuestNameBase("Woodlin Elder2", <QuestNameModel>{"name": "Portal Issues", "difficulty": 2}),
        new QuestNameBase("Woodlin Elder5", <QuestNameModel>{"name": "Big Lock Picking", "difficulty": 3}),
        new QuestNameBase("Woodlin Elder8", <QuestNameModel>{"name": "Fiddy", "difficulty": 1}),
        new QuestNameBase("Woodlin Elder11", <QuestNameModel>{"name": "Hunned Fiddy", "difficulty": 4}),
        new QuestNameBase("Woodlin Elder14", <QuestNameModel>{"name": "Triple Tre", "difficulty": 7}),
        new QuestNameBase("Sussy Gene3", <QuestNameModel>{"name": "Goofin' Around", "difficulty": 3}),
        new QuestNameBase("Sussy Gene6", <QuestNameModel>{"name": "Messin' Around", "difficulty": 5}),
        new QuestNameBase("Sussy Gene9", <QuestNameModel>{"name": "Loiterin' Around", "difficulty": 8}),
        new QuestNameBase("Spirit Sungmin2", <QuestNameModel>{"name": "Mind, Body, Soul, Tasks", "difficulty": 5})    
]
}
