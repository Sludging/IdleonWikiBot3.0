import { GodInfoModel } from '../model/godInfoModel';

export class GodInfoBase { constructor(public index: number, public data: GodInfoModel) { } }



export const initGodInfoRepo = () => {
    return [    
        new GodInfoBase(0, <GodInfoModel>{
                "name": "Snehebatu",
                "majorBonus": "+30% AFK Gains for all activities!",
                "passiveBonus": "+{% accuracy and +{% defence",
                "passiveMax": 70,
                "blessingBaseCost": 10,
                "blessingIncrement": 1.75,
                "blessingBonus": "+{% Divinity Gain",
                "preUnlockMessage": "The green snake expects a gift...",
                "x": 241,
                "y": 85,
                "linkX": 12,
                "linkY": 18,
                "hueAdjust": 0,
                "bonusIndex": 0,
                "blessingPerLevel": 2
            }),
        new GodInfoBase(1, <GodInfoModel>{
                "name": "Arctis",
                "majorBonus": "Whenever you level up a skill thats over Lv 50, a Divinity Pearl will drop which gives +40% exp to any skill under Lv 50!",
                "passiveBonus": "+{% skill exp",
                "passiveMax": 150,
                "blessingBaseCost": 10,
                "blessingIncrement": 1.15,
                "blessingBonus": "+{% Divinity Gain",
                "preUnlockMessage": "The fierce bear awaits a gesture...",
                "x": 502,
                "y": 85,
                "linkX": 694,
                "linkY": 20,
                "hueAdjust": 85,
                "bonusIndex": 2,
                "blessingPerLevel": 3
            }),
        new GodInfoBase(2, <GodInfoModel>{
                "name": "Nobisect",
                "majorBonus": "This character is always active within the Lab Mainframe. However, they will not gain any Lab EXP!",
                "passiveBonus": "+{ Talent LV for all talents above Lv 1",
                "passiveMax": 15,
                "blessingBaseCost": 10000,
                "blessingIncrement": 2.25,
                "blessingBonus": "+{ Scaled Skill Efficiency",
                "preUnlockMessage": "The insect requires an offering...",
                "x": 123,
                "y": 85,
                "linkX": 318,
                "linkY": 16,
                "hueAdjust": -50,
                "bonusIndex": 7,
                "blessingPerLevel": 50
            }),
        new GodInfoBase(3, <GodInfoModel>{
                "name": "Harriep",
                "majorBonus": "This character produces 3x more resources at 3d Printer! Works with the Lab Bonus, but won't affect the displayed printer amount.",
                "passiveBonus": "+{% coins gained for ALL characters!",
                "passiveMax": 100,
                "blessingBaseCost": 50000000,
                "blessingIncrement": 1.3,
                "blessingBonus": "+{% Divinity Gain",
                "preUnlockMessage": "The hare watches expectantly...",
                "x": 653,
                "y": 24,
                "linkX": 454,
                "linkY": 6,
                "hueAdjust": 220,
                "bonusIndex": 3,
                "blessingPerLevel": 3
            }),
        new GodInfoBase(4, <GodInfoModel>{
                "name": "Goharut",
                "majorBonus": "When claiming non-candy AFK gains, also progress one of the following by the AFK time! (Refinery, 3D Printer, Cooking, Pet Breeding, Sailing, or Gaming)",
                "passiveBonus": "+{% Class EXP",
                "passiveMax": 100,
                "blessingBaseCost": 1000000,
                "blessingIncrement": 2.6,
                "blessingBonus": "+{% Sailing Speed",
                "preUnlockMessage": "The horned one desires a sacrifice...",
                "x": 249,
                "y": 236,
                "linkX": 455,
                "linkY": 66,
                "hueAdjust": 160,
                "bonusIndex": 5,
                "blessingPerLevel": 4
            }),
        new GodInfoBase(5, <GodInfoModel>{
                "name": "Omniphau",
                "majorBonus": "Being connected to the Lab also counts as being present at the Divinity Altar, so you get gains for both!",
                "passiveBonus": "+{% AFK Gains for ALL characters!",
                "passiveMax": 5,
                "blessingBaseCost": 5,
                "blessingIncrement": 1.12,
                "blessingBonus": "+{% Divinity Gain",
                "preUnlockMessage": "The wise one stares beyond you...",
                "x": 1,
                "y": 39,
                "linkX": 226,
                "linkY": 4,
                "hueAdjust": 999,
                "bonusIndex": 4,
                "blessingPerLevel": 4
            }),
        new GodInfoBase(6, <GodInfoModel>{
                "name": "Purrmep",
                "majorBonus": "All characters produce 2x more Divinity, and get 2x more Divinity EXP! @ Only 1 player can link to Purrmep",
                "passiveBonus": "+{% Boat Sailing speed and +{% Gaming Plant grow speed",
                "passiveMax": 50,
                "blessingBaseCost": 1000000000,
                "blessingIncrement": 1.35,
                "blessingBonus": "+{% Sailing Speed",
                "preUnlockMessage": "Fury needs appeasement...",
                "x": 519,
                "y": 190,
                "linkX": 694,
                "linkY": 66,
                "hueAdjust": -100,
                "bonusIndex": 6,
                "blessingPerLevel": 3
            }),
        new GodInfoBase(7, <GodInfoModel>{
                "name": "Flutterbis",
                "majorBonus": "All kills count for 2x more kills for opening portals and accumulating Deathnote kills.",
                "passiveBonus": "+{% Total Damage",
                "passiveMax": 200,
                "blessingBaseCost": 10,
                "blessingIncrement": 1.15,
                "blessingBonus": "+{% Total Damage",
                "preUnlockMessage": "The flutterbird seeks your glory...",
                "x": 130,
                "y": 236,
                "linkX": 319,
                "linkY": 64,
                "hueAdjust": 40,
                "bonusIndex": 1,
                "blessingPerLevel": 1
            }),
        new GodInfoBase(8, <GodInfoModel>{
                "name": "Kattlekruk",
                "majorBonus": "I am not yet prepared to bestow upon you my bonus, give me some time. You may link with me, but nothing will come of it.",
                "passiveBonus": "Nothing. Be patient mortal.",
                "passiveMax": 1,
                "blessingBaseCost": 1000000000,
                "blessingIncrement": 3,
                "blessingBonus": "+{% Total Damage",
                "preUnlockMessage": "A present for what was the past...",
                "x": 773,
                "y": 24,
                "linkX": 542,
                "linkY": 2,
                "hueAdjust": 999,
                "bonusIndex": 8,
                "blessingPerLevel": 1
            }),
        new GodInfoBase(9, <GodInfoModel>{
                "name": "Bagur",
                "majorBonus": "I am not yet prepared to bestow upon you my bonus, give me some time. You may link with me, but nothing will come of it.",
                "passiveBonus": "Nothing. Be patient mortal.",
                "passiveMax": 1,
                "blessingBaseCost": 20,
                "blessingIncrement": 1.18,
                "blessingBonus": "+{% Sailing Speed",
                "preUnlockMessage": "BAGUR WANT THE STUFF...",
                "x": -23,
                "y": 185,
                "linkX": 172,
                "linkY": 66,
                "hueAdjust": 555,
                "bonusIndex": 9,
                "blessingPerLevel": 5
            })    
]
}
