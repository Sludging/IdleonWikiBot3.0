import { ActiveTalentModel } from '../model/activeTalentModel';

export class ActiveTalentBase { constructor(public index: number, public data: ActiveTalentModel) { } }



export const initActiveTalentRepo = () => {
    return [    
        new ActiveTalentBase(0, <ActiveTalentModel>{
                "name": "Blah",
                "K": 1.1,
                "D": 1.3,
                "s": 1,
                "cooldown": 5,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "projectile",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(1, <ActiveTalentModel>{
                "name": "Indiana Attack",
                "K": 1.15,
                "D": 1.35,
                "s": 1.3,
                "cooldown": 12,
                "castTime": 1.4,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 90,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(2, <ActiveTalentModel>{
                "name": "Breakin' The Bank",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 2000,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(3, <ActiveTalentModel>{
                "name": "Gimme Gimme",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 120,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(4, <ActiveTalentModel>{
                "name": "Its Your Birthday!",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 86000,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(5, <ActiveTalentModel>{
                "name": "Coin Toss",
                "K": 1.2,
                "D": 1.3,
                "s": 1.3,
                "cooldown": 20,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 1,
                "AFKrange": 125,
                "AFKtype": "projectile",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(6, <ActiveTalentModel>{
                "name": "Printer Go Brrr",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 82000,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(7, <ActiveTalentModel>{
                "name": "Maestro Transfusion",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 120,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(8, <ActiveTalentModel>{
                "name": "Void Trial Rerun",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 70010,
                "castTime": 1,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(9, <ActiveTalentModel>{
                "name": "Void Radius",
                "K": 1.15,
                "D": 1.35,
                "s": 1.3,
                "cooldown": 40,
                "castTime": 1,
                "manaCost": 200,
                "inputReq": 0,
                "AFKrange": 400,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(10, <ActiveTalentModel>{
                "name": "Power Strike",
                "K": 1.1,
                "D": 1.17,
                "s": 1.1,
                "cooldown": 4,
                "castTime": 0.45,
                "manaCost": 3,
                "inputReq": 0,
                "AFKrange": 80,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(11, <ActiveTalentModel>{
                "name": "Whirl",
                "K": 1.1,
                "D": 1.18,
                "s": 1.2,
                "cooldown": 6,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 45,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(12, <ActiveTalentModel>{
                "name": "Firmly Grasp It",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 30,
                "castTime": 1.5,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -1
            }),
        new ActiveTalentBase(13, <ActiveTalentModel>{
                "name": "Big Pick",
                "K": 1.05,
                "D": 1.4,
                "s": 1,
                "cooldown": 12,
                "castTime": 1.5,
                "manaCost": 10,
                "inputReq": 0,
                "AFKrange": 0,
                "AFKtype": "buff",
                "AFKactivity": 1
            }),
        new ActiveTalentBase(14, <ActiveTalentModel>{
                "name": "Bear Swipe",
                "K": 1.1,
                "D": 1.25,
                "s": 1.2,
                "cooldown": 12,
                "castTime": 0.8,
                "manaCost": 20,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(15, <ActiveTalentModel>{
                "name": "Axe Hurl",
                "K": 1,
                "D": 1.25,
                "s": 1.1,
                "cooldown": 17,
                "castTime": 0.8,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 200,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(16, <ActiveTalentModel>{
                "name": "Mocking Shout",
                "K": 1,
                "D": 1,
                "s": 1.1,
                "cooldown": 600,
                "castTime": 1.5,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(17, <ActiveTalentModel>{
                "name": "No Pain No Gain",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 30,
                "castTime": 1.5,
                "manaCost": 20,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(18, <ActiveTalentModel>{
                "name": "Worming Undercover",
                "K": 1,
                "D": 1.4,
                "s": 1,
                "cooldown": 15,
                "castTime": 1.5,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": 4
            }),
        new ActiveTalentBase(19, <ActiveTalentModel>{
                "name": "Fired Up",
                "K": 1,
                "D": 1.4,
                "s": 1,
                "cooldown": 60,
                "castTime": 1.5,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(20, <ActiveTalentModel>{
                "name": "Combustion",
                "K": 1.1,
                "D": 1.25,
                "s": 1.2,
                "cooldown": 20,
                "castTime": 0.8,
                "manaCost": 20,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(21, <ActiveTalentModel>{
                "name": "Serrated Swipe",
                "K": 1.1,
                "D": 1.25,
                "s": 1.2,
                "cooldown": 15,
                "castTime": 0.8,
                "manaCost": 25,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(22, <ActiveTalentModel>{
                "name": "Taste Test",
                "K": 1.1,
                "D": 1.25,
                "s": 1.2,
                "cooldown": 200000,
                "castTime": 0.8,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 125,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(23, <ActiveTalentModel>{
                "name": "Shockwave Slash",
                "K": 1.2,
                "D": 1.4,
                "s": 1,
                "cooldown": 14,
                "castTime": 1.8,
                "manaCost": 25,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(24, <ActiveTalentModel>{
                "name": "Daggerang",
                "K": 1,
                "D": 1.4,
                "s": 1,
                "cooldown": 16,
                "castTime": 0.8,
                "manaCost": 30,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(25, <ActiveTalentModel>{
                "name": "Bricky Skin",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 30,
                "castTime": 1,
                "manaCost": 20,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(26, <ActiveTalentModel>{
                "name": "Balanced Spirit",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 30,
                "castTime": 1,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(27, <ActiveTalentModel>{
                "name": "Refinery Throttle",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 72000,
                "castTime": 0.95,
                "manaCost": 10,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(28, <ActiveTalentModel>{
                "name": "Knightly Disciple",
                "K": 1.2,
                "D": 1.4,
                "s": 1.2,
                "cooldown": 40,
                "castTime": 1,
                "manaCost": 60,
                "inputReq": 0,
                "AFKrange": 230,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(29, <ActiveTalentModel>{
                "name": "Divine Intervention",
                "K": 1.2,
                "D": 1.2,
                "s": 1,
                "cooldown": 40,
                "castTime": 0.5,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(30, <ActiveTalentModel>{
                "name": "Orb Of Remembrance",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 150,
                "castTime": 0.5,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(31, <ActiveTalentModel>{
                "name": "Piercing Arrow",
                "K": 1.15,
                "D": 1.19,
                "s": 1.15,
                "cooldown": 15,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 300,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(32, <ActiveTalentModel>{
                "name": "Kung Fu Kick",
                "K": 1,
                "D": 1.15,
                "s": 1,
                "cooldown": 7,
                "castTime": 0.45,
                "manaCost": 3,
                "inputReq": 0,
                "AFKrange": 80,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(33, <ActiveTalentModel>{
                "name": "Strafe",
                "K": 1,
                "D": 1,
                "s": 1.2,
                "cooldown": 30,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -1
            }),
        new ActiveTalentBase(34, <ActiveTalentModel>{
                "name": "Homing Arrows",
                "K": 1,
                "D": 1.25,
                "s": 1.1,
                "cooldown": 20,
                "castTime": 0.45,
                "manaCost": 18,
                "inputReq": 0,
                "AFKrange": 300,
                "AFKtype": "circle",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(35, <ActiveTalentModel>{
                "name": "Magic Shortbow",
                "K": 1.1,
                "D": 1.2,
                "s": 1.05,
                "cooldown": 7,
                "castTime": 0.45,
                "manaCost": 7,
                "inputReq": 0,
                "AFKrange": 100,
                "AFKtype": "target",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(36, <ActiveTalentModel>{
                "name": "Extendo Rangeo",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 30,
                "castTime": 0.45,
                "manaCost": 8,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(37, <ActiveTalentModel>{
                "name": "360 Noscope",
                "K": 1.2,
                "D": 1.3,
                "s": 1,
                "cooldown": 30,
                "castTime": 1.1,
                "manaCost": 25,
                "inputReq": 2,
                "AFKrange": 200,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(38, <ActiveTalentModel>{
                "name": "Bear Trap",
                "K": 1.2,
                "D": 1.15,
                "s": 1,
                "cooldown": 9,
                "castTime": 1.5,
                "manaCost": 30,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(39, <ActiveTalentModel>{
                "name": "Uwu Rawrrr",
                "K": 1,
                "D": 1,
                "s": 1.1,
                "cooldown": 120,
                "castTime": 1.5,
                "manaCost": 30,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(40, <ActiveTalentModel>{
                "name": "Stop Right There",
                "K": 1,
                "D": 1,
                "s": 1.1,
                "cooldown": 60,
                "castTime": 1.5,
                "manaCost": 40,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(41, <ActiveTalentModel>{
                "name": "Eagle Eye",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 6,
                "castTime": 0.95,
                "manaCost": 2,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(42, <ActiveTalentModel>{
                "name": "Cannonball",
                "K": 1,
                "D": 1.5,
                "s": 1,
                "cooldown": 4,
                "castTime": 0.45,
                "manaCost": 30,
                "inputReq": 0,
                "AFKrange": 350,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(43, <ActiveTalentModel>{
                "name": "Suppressing Fire",
                "K": 1.3,
                "D": 1.2,
                "s": 1.1,
                "cooldown": 6,
                "castTime": 0.45,
                "manaCost": 35,
                "inputReq": 0,
                "AFKrange": 400,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(44, <ActiveTalentModel>{
                "name": "Firebomb",
                "K": 1,
                "D": 1.4,
                "s": 1,
                "cooldown": 38,
                "castTime": 1.1,
                "manaCost": 45,
                "inputReq": 0,
                "AFKrange": 0,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(45, <ActiveTalentModel>{
                "name": "Pirate Flag",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 490,
                "castTime": 0.5,
                "manaCost": 15,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(46, <ActiveTalentModel>{
                "name": "Ballista",
                "K": 1.1,
                "D": 1.3,
                "s": 1,
                "cooldown": 15,
                "castTime": 0.45,
                "manaCost": 150,
                "inputReq": 1,
                "AFKrange": 1,
                "AFKtype": "target",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(47, <ActiveTalentModel>{
                "name": "Boar Rush",
                "K": 1.1,
                "D": 1.2,
                "s": 1.1,
                "cooldown": 25,
                "castTime": 0.95,
                "manaCost": 100,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(48, <ActiveTalentModel>{
                "name": "Whale Wallop",
                "K": 1.2,
                "D": 1.1,
                "s": 1.1,
                "cooldown": 40,
                "castTime": 0.95,
                "manaCost": 250,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(49, <ActiveTalentModel>{
                "name": "Nacho Party",
                "K": 1.1,
                "D": 1.1,
                "s": 1.2,
                "cooldown": 30,
                "castTime": 0.7,
                "manaCost": 125,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(50, <ActiveTalentModel>{
                "name": "Arena Spirit",
                "K": 1.1,
                "D": 1.1,
                "s": 1.2,
                "cooldown": 86400,
                "castTime": 0.7,
                "manaCost": 20,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(51, <ActiveTalentModel>{
                "name": "Energy Bolt",
                "K": 1,
                "D": 1.21,
                "s": 1,
                "cooldown": 8,
                "castTime": 0.5,
                "manaCost": 4,
                "inputReq": 2,
                "AFKrange": 200,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(52, <ActiveTalentModel>{
                "name": "Mini Fireball",
                "K": 1.05,
                "D": 1.2,
                "s": 1.1,
                "cooldown": 10,
                "castTime": 0.85,
                "manaCost": 6,
                "inputReq": 0,
                "AFKrange": 270,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(53, <ActiveTalentModel>{
                "name": "Teleport",
                "K": 1,
                "D": 1,
                "s": 1.3,
                "cooldown": 1,
                "castTime": 0.5,
                "manaCost": 2,
                "inputReq": 0,
                "AFKrange": 480,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(54, <ActiveTalentModel>{
                "name": "Log On Logs",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 30,
                "castTime": 0.95,
                "manaCost": 5,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": 3
            }),
        new ActiveTalentBase(55, <ActiveTalentModel>{
                "name": "Ice Shards",
                "K": 1.1,
                "D": 1.3,
                "s": 1,
                "cooldown": 10,
                "castTime": 1.2,
                "manaCost": 12,
                "inputReq": 2,
                "AFKrange": 200,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(56, <ActiveTalentModel>{
                "name": "Floor Is Lava",
                "K": 1.1,
                "D": 1.3,
                "s": 1.02,
                "cooldown": 13,
                "castTime": 0.95,
                "manaCost": 25,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(57, <ActiveTalentModel>{
                "name": "Tornado",
                "K": 1.1,
                "D": 1.3,
                "s": 1.02,
                "cooldown": 25,
                "castTime": 0.95,
                "manaCost": 30,
                "inputReq": 0,
                "AFKrange": 150,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(58, <ActiveTalentModel>{
                "name": "Speedy Book",
                "K": 1,
                "D": 1,
                "s": 1.05,
                "cooldown": 2,
                "castTime": 0.95,
                "manaCost": 10,
                "inputReq": 0,
                "AFKrange": 0,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(59, <ActiveTalentModel>{
                "name": "Mana Is Life",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 60,
                "castTime": 0.95,
                "manaCost": 12,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(60, <ActiveTalentModel>{
                "name": "Charge Syphon",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 3600,
                "castTime": 0.95,
                "manaCost": 10,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(61, <ActiveTalentModel>{
                "name": "Crazy Concoctions",
                "K": 1.1,
                "D": 1.3,
                "s": 1.02,
                "cooldown": 25,
                "castTime": 0.95,
                "manaCost": 15,
                "inputReq": 1,
                "AFKrange": 50,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(62, <ActiveTalentModel>{
                "name": "Auspicious Aura",
                "K": 1.05,
                "D": 1.21,
                "s": 1.1,
                "cooldown": 40,
                "castTime": 0.95,
                "manaCost": 40,
                "inputReq": 0,
                "AFKrange": 80,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(63, <ActiveTalentModel>{
                "name": "Sizzling Skull",
                "K": 1.05,
                "D": 1.21,
                "s": 1.1,
                "cooldown": 18,
                "castTime": 0.95,
                "manaCost": 20,
                "inputReq": 0,
                "AFKrange": 130,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(64, <ActiveTalentModel>{
                "name": "Cranium Cooking",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 80000,
                "castTime": 0.95,
                "manaCost": 100,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "buff",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(65, <ActiveTalentModel>{
                "name": "Meteor Shower",
                "K": 1.2,
                "D": 1.2,
                "s": 1,
                "cooldown": 12,
                "castTime": 0.8,
                "manaCost": 90,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(66, <ActiveTalentModel>{
                "name": "Lightning Barrage",
                "K": 1,
                "D": 1.3,
                "s": 1,
                "cooldown": 4,
                "castTime": 0.55,
                "manaCost": 40,
                "inputReq": 2,
                "AFKrange": 200,
                "AFKtype": "line",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(67, <ActiveTalentModel>{
                "name": "Radiant Chainbolt",
                "K": 1.3,
                "D": 1,
                "s": 1,
                "cooldown": 8,
                "castTime": 0.95,
                "manaCost": 50,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(68, <ActiveTalentModel>{
                "name": "Dimensional Wormhole",
                "K": 1,
                "D": 1,
                "s": 1.3,
                "cooldown": 120,
                "castTime": 0.95,
                "manaCost": 100,
                "inputReq": 0,
                "AFKrange": 50,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(69, <ActiveTalentModel>{
                "name": "Chemical Warfare",
                "K": 1,
                "D": 1.21,
                "s": 1,
                "cooldown": 32,
                "castTime": 1.1,
                "manaCost": 110,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(70, <ActiveTalentModel>{
                "name": "Flatulent Spirit",
                "K": 1,
                "D": 1.21,
                "s": 1,
                "cooldown": 38,
                "castTime": 1.1,
                "manaCost": 90,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(71, <ActiveTalentModel>{
                "name": "Tampered Injection",
                "K": 1,
                "D": 1.21,
                "s": 1,
                "cooldown": 28,
                "castTime": 1.1,
                "manaCost": 20,
                "inputReq": 2,
                "AFKrange": 1,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(72, <ActiveTalentModel>{
                "name": "Raise Dead",
                "K": 1,
                "D": 1.21,
                "s": 1,
                "cooldown": 37,
                "castTime": 1.1,
                "manaCost": 80,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "auto",
                "AFKactivity": 0
            }),
        new ActiveTalentBase(73, <ActiveTalentModel>{
                "name": "Roll Da Dice",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 200,
                "castTime": 0.5,
                "manaCost": 1,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -1
            }),
        new ActiveTalentBase(74, <ActiveTalentModel>{
                "name": "Exp Converter",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 3,
                "castTime": 0.1,
                "manaCost": 1,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(75, <ActiveTalentModel>{
                "name": "Telekinetic Storage",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 1800,
                "castTime": 0.1,
                "manaCost": 1,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(76, <ActiveTalentModel>{
                "name": "Printer Sampling",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 2,
                "castTime": 0.1,
                "manaCost": 1,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(77, <ActiveTalentModel>{
                "name": "Shrine Architect",
                "K": 1,
                "D": 1,
                "s": 1,
                "cooldown": 6,
                "castTime": 0.1,
                "manaCost": 1,
                "inputReq": 0,
                "AFKrange": 1,
                "AFKtype": "buff",
                "AFKactivity": -2
            }),
        new ActiveTalentBase(78, <ActiveTalentModel>{
                "name": "From Downtown",
                "K": 1,
                "D": 1.3,
                "s": 1,
                "cooldown": 5,
                "castTime": 0.45,
                "manaCost": 5,
                "inputReq": 1,
                "AFKrange": 125,
                "AFKtype": "projectile",
                "AFKactivity": 0
            })    
]
}
