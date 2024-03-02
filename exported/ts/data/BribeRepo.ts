import { BribeModel } from '../model/bribeModel';

export class BribeBase { constructor(public index: number, public data: BribeModel) { } }



export const initBribeRepo = () => {
    return [    
        new BribeBase(0, <BribeModel>{
                "name": "Insider Trading",
                "desc": "All stamps cost 5% less coins to upgrade.",
                "cost": 750,
                "type": "pigbank",
                "intName": "StampCostPct",
                "amount": 8
            }),
        new BribeBase(1, <BribeModel>{
                "name": "Tracking Chips",
                "desc": "Stamps drop +15% more often from monsters and resources that drop stamps.",
                "cost": 1800,
                "type": "pigbank",
                "intName": "StampDrop",
                "amount": 15
            }),
        new BribeBase(2, <BribeModel>{
                "name": "Mandatory Fire Sale",
                "desc": "All shop items cost 7% less coins.",
                "cost": 3200,
                "type": "shops",
                "intName": "ShopCostPct",
                "amount": 7
            }),
        new BribeBase(3, <BribeModel>{
                "name": "Sleeping on the Job",
                "desc": "Boosts fighting AFK Gains Rate by +5%",
                "cost": 6000,
                "type": "pigbank",
                "intName": "FightAfkRate",
                "amount": 5
            }),
        new BribeBase(4, <BribeModel>{
                "name": "Artificial Demand",
                "desc": "Items sell to shops for +10% more than their normal value.",
                "cost": 9000,
                "type": "shops",
                "intName": "ShopSellPct",
                "amount": 10
            }),
        new BribeBase(5, <BribeModel>{
                "name": "The Art of the Deal",
                "desc": "Unlocks the next set of 7 Bribes to be purchased.",
                "cost": 15000,
                "type": "pigbank",
                "intName": "BribeExpansion",
                "amount": -1
            }),
        new BribeBase(6, <BribeModel>{
                "name": "Overstock Regulations",
                "desc": "Item Quantity in all shops increased by +20%. Takes effect only after Shops restock.",
                "cost": 20000,
                "type": "shops",
                "intName": "ShopQtyPct",
                "amount": 20
            }),
        new BribeBase(7, <BribeModel>{
                "name": "Double Exp Scheme",
                "desc": "Whenever you claim AFK rewards, there is a 2.2% chance to get x2 EXP.",
                "cost": 222222,
                "type": "afk",
                "intName": "AfkDoubleEXP",
                "amount": 2
            }),
        new BribeBase(8, <BribeModel>{
                "name": "Tagged Indicators",
                "desc": "Stamps drop +20% more often. Stacks with previous bribe of this type.",
                "cost": 30000,
                "type": "pigbank",
                "intName": "StampDrop",
                "amount": 20
            }),
        new BribeBase(9, <BribeModel>{
                "name": "Fossil Fuel Legislation",
                "desc": "Oil Barrel consumption chance is reduced to 80% of the original chance.",
                "cost": 55000,
                "type": "smithing",
                "intName": "OilConsume",
                "amount": 0
            }),
        new BribeBase(10, <BribeModel>{
                "name": "Five Aces in the Deck",
                "desc": "Card drop rate boosted by 1.20x for all areas of the game.",
                "cost": 70000,
                "type": "afk",
                "intName": "CardDropPct",
                "amount": 20
            }),
        new BribeBase(11, <BribeModel>{
                "name": "Fake Teleport Tickets",
                "desc": "Get +2 Map Teleport every 24 hours. Caps at 6, so being gone for 4 days only gives 6 tele.",
                "cost": 99000,
                "type": "pigbank",
                "intName": "FreeTeleport",
                "amount": 3
            }),
        new BribeBase(12, <BribeModel>{
                "name": "The Art of the Steal",
                "desc": "Unlocks the next set of 7 Bribes to be purchased.",
                "cost": 200000,
                "type": "pigbank",
                "intName": "BribeExpansion",
                "amount": -1
            }),
        new BribeBase(13, <BribeModel>{
                "name": "Counterfeit Telepassports",
                "desc": "You now get +4 Map Teleports every 24 hours, and caps at 12 before you need to login.",
                "cost": 300000,
                "type": "pigbank",
                "intName": "FreeTeleport2",
                "amount": 2
            }),
        new BribeBase(14, <BribeModel>{
                "name": "Weighted Marbles",
                "desc": "+10% arcade balls recharge rate. You'll be drowning in balls in no time!",
                "cost": 725000,
                "type": "world3",
                "intName": "ArcadeBallz",
                "amount": 10
            }),
        new BribeBase(15, <BribeModel>{
                "name": "Changing the Code",
                "desc": "Unlock the 2nd Alchemy Bubble slot for ALL players. Don't go tellin' Lava 'bout this one...",
                "cost": 1500000,
                "type": "pigbank",
                "intName": "BubbleSlot",
                "amount": 1
            }),
        new BribeBase(16, <BribeModel>{
                "name": "Taxidermied Cog Pouches",
                "desc": "+4 Cog Inventory slots.",
                "cost": 750000,
                "type": "world3",
                "intName": "CogInve",
                "amount": 4
            }),
        new BribeBase(17, <BribeModel>{
                "name": "Guild VIP Fraud",
                "desc": "Logging in each day now contributes 20 GP to your guild, instead of the normal 10.",
                "cost": 400000,
                "type": "afk",
                "intName": "BonusType",
                "amount": 10
            }),
        new BribeBase(18, <BribeModel>{
                "name": "Library Double Agent",
                "desc": "+4 minimum Lv for all Talent Books from the library, so you get more of the goood stuff.",
                "cost": 9156348,
                "type": "world3",
                "intName": "BonusType",
                "amount": 4
            }),
        new BribeBase(19, <BribeModel>{
                "name": "The Art of the Fail",
                "desc": "Unlocks the next set of 7 Bribes to be purchased.",
                "cost": 25000000,
                "type": "pigbank",
                "intName": "BribeExpansion",
                "amount": -1
            }),
        new BribeBase(20, <BribeModel>{
                "name": "Photoshopped Dmg Range",
                "desc": "Boosts Total Damage by +2%.",
                "cost": 100000000,
                "type": "pigbank",
                "intName": "TotalDmg",
                "amount": 2
            }),
        new BribeBase(21, <BribeModel>{
                "name": "Glitched Acc Formula",
                "desc": "Boosts Total Accuracy by +2%",
                "cost": 300000000,
                "type": "pigbank",
                "intName": "TotalAcc",
                "amount": 2
            }),
        new BribeBase(22, <BribeModel>{
                "name": "Firewalled Defence",
                "desc": "Boosts Total Defence by +2%",
                "cost": 700000000,
                "type": "pigbank",
                "intName": "TotalDef",
                "amount": 2
            }),
        new BribeBase(23, <BribeModel>{
                "name": "Bottomless Bags",
                "desc": "Boosts Carry Capacity by +5%",
                "cost": 1200000000,
                "type": "pigbank",
                "intName": "CarryCap",
                "amount": 5
            }),
        new BribeBase(24, <BribeModel>{
                "name": "AFKeylogging",
                "desc": "Boosts Skill AFK Gains Rate by +2%.",
                "cost": 20000000000,
                "type": "afk",
                "intName": "SkillAFK",
                "amount": 2
            }),
        new BribeBase(25, <BribeModel>{
                "name": "Guild GP Hack",
                "desc": "Logging in each day now contributes 30 GP to your guild, instead of 20.",
                "cost": 2500000000,
                "type": "afk",
                "intName": "Guild2",
                "amount": 10
            }),
        new BribeBase(26, <BribeModel>{
                "name": "The Art of the Bail",
                "desc": "Unlock the next Bribe Set from the Garbage Tuna on Trash Island in World 2 to buy.",
                "cost": 99999999,
                "type": "fish",
                "intName": "BribeExpansion",
                "amount": -1
            }),
        new BribeBase(27, <BribeModel>{
                "name": "Random Garbage",
                "desc": "All random event bosses now drop Garbage Piles to give to the Garbage Tuna.",
                "cost": 8000000000000,
                "type": "fish",
                "intName": "RandoGarbo",
                "amount": 1
            }),
        new BribeBase(28, <BribeModel>{
                "name": "Godlier Creation",
                "desc": "The Godly Creation talent now gives up to +12 Stat bonus, instead of up to +4",
                "cost": 12121212121212,
                "type": "smithing",
                "intName": "GodlyCreation",
                "amount": 1
            }),
        new BribeBase(29, <BribeModel>{
                "name": "Fishermaster",
                "desc": "+25% Fishing EXP, and +15% Fishing Efficiency, now and forever.",
                "cost": 251500000000,
                "type": "fish",
                "intName": "FishingStats",
                "amount": 1
            }),
        new BribeBase(30, <BribeModel>{
                "name": "Muscles on Muscles",
                "desc": "Boosts Total Damage by +2%",
                "cost": 20000000000000000,
                "type": "pigbank",
                "intName": "TotalDmgB",
                "amount": 2
            }),
        new BribeBase(31, <BribeModel>{
                "name": "Bottle Service",
                "desc": "Bottles, used to buy maps to new islands, wash up at the docks +10% more often.",
                "cost": 40000000000000,
                "type": "fish",
                "intName": "BottleMore",
                "amount": 10
            }),
        new BribeBase(32, <BribeModel>{
                "name": "Star Scraper",
                "desc": "Get +33 Star Talent points, right now, for all characters, no questions asked.",
                "cost": 3300000000000000,
                "type": "pigbank",
                "intName": "StarTalz",
                "amount": 33
            }),
        new BribeBase(33, <BribeModel>{
                "name": "The Art of the Grail",
                "desc": "You must unlock the next Bribe set from the Jade Emporium in World 6 to buy this.",
                "cost": 99999999,
                "type": "pigbank",
                "intName": "BribeExpansion",
                "amount": -1
            }),
        new BribeBase(34, <BribeModel>{
                "name": "Artifact Pilfering",
                "desc": "Boosts Artifact find chance by a pleasantly large +20%",
                "cost": 300000000000000000,
                "type": "world5",
                "intName": "New1",
                "amount": 20
            }),
        new BribeBase(35, <BribeModel>{
                "name": "Forge Cap Smuggling",
                "desc": "Boosts Forge Capacity by a smoking hot 1.30x",
                "cost": 4400000000000000000,
                "type": "smithing",
                "intName": "New2",
                "amount": 30
            }),
        new BribeBase(36, <BribeModel>{
                "name": "Gold from Lead",
                "desc": "Boosts all Golden Food bonuses by +10%",
                "cost": 71000000000000000000,
                "type": "pigbank",
                "intName": "New3",
                "amount": 10
            }),
        new BribeBase(37, <BribeModel>{
                "name": "Nugget Fabrication",
                "desc": "Boosts the rate at which the Shovel generates Nuggets in Gaming by +20%",
                "cost": 350000000000000000000,
                "type": "world5",
                "intName": "New4",
                "amount": 20
            }),
        new BribeBase(38, <BribeModel>{
                "name": "Divine PTS Miscounting",
                "desc": "Boosts Divinity PTS gain rate by +30%",
                "cost": 5000000000000000000000,
                "type": "world5",
                "intName": "New5",
                "amount": 30
            }),
        new BribeBase(39, <BribeModel>{
                "name": "Loot Table Tampering",
                "desc": "All items from Random Event Bosses are 1.20x more likely to drop than before.",
                "cost": 99999999999999991611392,
                "type": "pigbank",
                "intName": "New6",
                "amount": 20
            }),
        new BribeBase(40, <BribeModel>{
                "name": "The Art of the Flail",
                "desc": "Look buddy, I ain't got no more bribes, maybe an associate of mine will sort it out later...",
                "cost": 99999999,
                "type": "pigbank",
                "intName": "BribeExpansion",
                "amount": -1
            })    
]
}
