import { TaskShopDescModel } from '../model/taskShopDescModel';

export class TaskShopDescBase { constructor(public index: number, public data: TaskShopDescModel) { } }



export const initTaskShopDescRepo = () => {
    return [    
        new TaskShopDescBase(0, <TaskShopDescModel>{
                "descLine1": "Inventory Bag } is applied to everyone,",
                "descLine2": "but only if your 1st character has it.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "B C E F H BCEFH",
                "icon": "TaskSa1",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(1, <TaskShopDescModel>{
                "descLine1": "All Blunder Hills Monsters respawn +{%",
                "descLine2": "faster. This boosts AFK kills per hour!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSa2",
                "bonusPerLevel": 2
            }),
        new TaskShopDescBase(2, <TaskShopDescModel>{
                "descLine1": "+{% EXP Gain for the lowest leveled",
                "descLine2": "character in your family.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 12,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSb5",
                "bonusPerLevel": 4
            }),
        new TaskShopDescBase(3, <TaskShopDescModel>{
                "descLine1": "Sets the Max Lv. to { For the 'Goblet",
                "descLine2": "of Hemoglobin' Talent. Helps survivability!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbb1",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(4, <TaskShopDescModel>{
                "descLine1": "Bosses can now drop Boss Keys. 4%",
                "descLine2": "higher key drop chance per purchase!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSb4",
                "bonusPerLevel": 7
            }),
        new TaskShopDescBase(5, <TaskShopDescModel>{
                "descLine1": "Unlocks recipe to craft Amarok }.",
                "descLine2": "Descline2",
                "number1": 1,
                "number2": 6,
                "number3": 2,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Shoes Pants Torso Helmet Pendant SoldOut",
                "icon": "SmithingRecipes1",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(6, <TaskShopDescModel>{
                "descLine1": "+{% higher chance for Minibosses in",
                "descLine2": "world 1 to drop new Star Talents.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 6,
                "meritCost": 3,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TalentBook1",
                "bonusPerLevel": 30
            }),
        new TaskShopDescBase(7, <TaskShopDescModel>{
                "descLine1": "IDK YET",
                "descLine2": "Descline2",
                "number1": 1,
                "number2": 3,
                "number3": 6,
                "totalLevels": 5,
                "meritCost": -1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "Blank",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(8, <TaskShopDescModel>{
                "descLine1": "Monsters now drop Obols. +5% drop",
                "descLine2": "rate per purchase!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 7,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "A B C E F H",
                "icon": "TaskSb3",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(9, <TaskShopDescModel>{
                "descLine1": "All Yum-Yum Desert Mobs respawn +{%",
                "descLine2": "faster. This boosts AFK kills per hour!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSb2",
                "bonusPerLevel": 2
            }),
        new TaskShopDescBase(10, <TaskShopDescModel>{
                "descLine1": "+2% AFK Gains for your first {",
                "descLine2": "characters in your family.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSa3",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(11, <TaskShopDescModel>{
                "descLine1": "Boosts Max Lv. to { for 'Convert Better",
                "descLine2": "Darnit' Talent. Probs still stinks...",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSb1",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(12, <TaskShopDescModel>{
                "descLine1": "World bosses can now drop gems. +7%",
                "descLine2": "gem drop rate per purchase!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 8,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSa4",
                "bonusPerLevel": 7
            }),
        new TaskShopDescBase(13, <TaskShopDescModel>{
                "descLine1": "Unlocks recipe to craft Efaunt }.",
                "descLine2": "Descline2",
                "number1": 1,
                "number2": 6,
                "number3": 2,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Shoes Pants Torso Helmet Ring SoldOut",
                "icon": "SmithingRecipes2",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(14, <TaskShopDescModel>{
                "descLine1": "+{% higher chance for Minibosses in",
                "descLine2": "world 2 to drop new Star Talents.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 8,
                "meritCost": 3,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TalentBook1",
                "bonusPerLevel": 30
            }),
        new TaskShopDescBase(15, <TaskShopDescModel>{
                "descLine1": "+{% arcade ball gain rate, so you",
                "descLine2": "can get them balls launchin!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbb2",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(16, <TaskShopDescModel>{
                "descLine1": "1st, 3rd purchase give +1 Build Slot,",
                "descLine2": "2nd, 4th purchase give +1 Food Slot.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 4,
                "meritCost": 3,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "A B C E F H",
                "icon": "TaskSc1",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(17, <TaskShopDescModel>{
                "descLine1": "All Frostbite Tundra Mobs respawn +{%",
                "descLine2": "faster. This boosts AFK kills per hour!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSc2",
                "bonusPerLevel": 2
            }),
        new TaskShopDescBase(18, <TaskShopDescModel>{
                "descLine1": "+{ Max possible Lv of Talent books",
                "descLine2": "from the Talent Book Library.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSc3",
                "bonusPerLevel": 2
            }),
        new TaskShopDescBase(19, <TaskShopDescModel>{
                "descLine1": "Boosts Max Lv. to { for 'Telekinetic",
                "descLine2": "Storage' Talent. Easy item depositing!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSc5",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(20, <TaskShopDescModel>{
                "descLine1": "+0.5% Printer Sample Size per purchase.",
                "descLine2": "Make the Federal Reserve jealous!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSc4",
                "bonusPerLevel": 0.5
            }),
        new TaskShopDescBase(21, <TaskShopDescModel>{
                "descLine1": "Unlocks recipe to craft Chizoar }.",
                "descLine2": "Descline2",
                "number1": 1,
                "number2": 6,
                "number3": 2,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Shoes Pants Torso Helmet Pendant SoldOut",
                "icon": "SmithingRecipes3",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(22, <TaskShopDescModel>{
                "descLine1": "Refinery Salt Costs don't scale beyond",
                "descLine2": "power output. +1 Salt Type Per Purchase.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSc6",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(23, <TaskShopDescModel>{
                "descLine1": "+{% higher chance for Minibosses in",
                "descLine2": "world 3 to drop new Star Talents.",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": -1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "Blank",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(24, <TaskShopDescModel>{
                "descLine1": "The first +{ kills each day are",
                "descLine2": "guaranteed to spawn a crystal monster",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 3,
                "meritCost": 3,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "A B C E F H",
                "icon": "TaskSbd2",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(25, <TaskShopDescModel>{
                "descLine1": "All Hyperion Nebula Mobs respawn +{%",
                "descLine2": "faster. This boosts AFK kills per hour!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbd1",
                "bonusPerLevel": 2
            }),
        new TaskShopDescBase(26, <TaskShopDescModel>{
                "descLine1": "+{ egg capacity in the Nest. Those pets",
                "descLine2": "wont hatch themselves after all!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 2,
                "meritCost": 6,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbd4",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(27, <TaskShopDescModel>{
                "descLine1": "Boosts Max Lv. to { for 'Spice Spillage'",
                "descLine2": "Talent. Convenient Spice claiming!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbd5",
                "bonusPerLevel": 20
            }),
        new TaskShopDescBase(28, <TaskShopDescModel>{
                "descLine1": "+{ connection range in the Lab, so",
                "descLine2": "players can connect from farther away!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 8,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbd3",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(29, <TaskShopDescModel>{
                "descLine1": "Unlocks recipe to craft Troll }.",
                "descLine2": "Descline2",
                "number1": 1,
                "number2": 6,
                "number3": 2,
                "totalLevels": 4,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Shoes Pants Torso Helmet SoldOut",
                "icon": "SmithingRecipes4",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(30, <TaskShopDescModel>{
                "descLine1": "+{ Bubbles upgraded by 'No Bubble Left",
                "descLine2": "Behind' per day. Bubble blowin' baby!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 3,
                "meritCost": 5,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSbd6",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(31, <TaskShopDescModel>{
                "descLine1": "IDK YET",
                "descLine2": "Descline2",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": -1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "Blank",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(32, <TaskShopDescModel>{
                "descLine1": "+{ Talent Pts for Tab 4, so you can",
                "descLine2": "max out those Elite Class talents!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 20,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TalentPoint4",
                "bonusPerLevel": 3
            }),
        new TaskShopDescBase(33, <TaskShopDescModel>{
                "descLine1": "All Smolderin Plateau Mobs respawn +{%",
                "descLine2": "faster. This boosts AFK kills per hour!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSe1",
                "bonusPerLevel": 2
            }),
        new TaskShopDescBase(34, <TaskShopDescModel>{
                "descLine1": "+{ Loot Pile Capacity. More sailing",
                "descLine2": "chest storage ain't bad, eh?",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 7,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSe2",
                "bonusPerLevel": 1
            }),
        new TaskShopDescBase(35, <TaskShopDescModel>{
                "descLine1": "Boosts Max Lv. to { for 'Stat Overload'",
                "descLine2": "Talent. Get those 10k stats!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 10,
                "meritCost": 1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSe4",
                "bonusPerLevel": 30
            }),
        new TaskShopDescBase(36, <TaskShopDescModel>{
                "descLine1": "+{% EXP for Sailing, Divinity, and",
                "descLine2": "Gaming skills. Experience POINTS!!!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSe3",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(37, <TaskShopDescModel>{
                "descLine1": "Unlocks recipe to craft Kattle }.",
                "descLine2": "Descline2",
                "number1": 1,
                "number2": 6,
                "number3": 2,
                "totalLevels": 9,
                "meritCost": 2,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Shoes Pants Torso Helmet Spear Bow Wand Gloves Scarf SoldOut",
                "icon": "SmithingRecipes5",
                "bonusPerLevel": 0
            }),
        new TaskShopDescBase(38, <TaskShopDescModel>{
                "descLine1": "+{% reduction in Atom Upgrade Costs,",
                "descLine2": "so you can upgrade Atoms more!!",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 4,
                "meritCost": 3,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "TaskSe5",
                "bonusPerLevel": 5
            }),
        new TaskShopDescBase(39, <TaskShopDescModel>{
                "descLine1": "IDK YET",
                "descLine2": "Descline2",
                "number1": 0,
                "number2": 0,
                "number3": 0,
                "totalLevels": 5,
                "meritCost": -1,
                "text1": "bonusGiven",
                "text2": "BonusPerLv",
                "extraStr": "Blank420q",
                "icon": "Blank",
                "bonusPerLevel": 0
            })    
]
}
