import { EnemyNavModel } from '../model/enemyNavModel';

export class EnemyNavBase { constructor(public id: string, public data: EnemyNavModel) { } }



export const initEnemyNavRepo = () => {
    return [    
        new EnemyNavBase("mushG", <EnemyNavModel>{
                "prev": null,
                "next": "mushR",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("mushR", <EnemyNavModel>{
                "prev": "mushG",
                "next": "frogG",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("frogG", <EnemyNavModel>{
                "prev": "mushR",
                "next": "beanG",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("beanG", <EnemyNavModel>{
                "prev": "frogG",
                "next": "slimeG",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("slimeG", <EnemyNavModel>{
                "prev": "beanG",
                "next": "snakeG",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("snakeG", <EnemyNavModel>{
                "prev": "slimeG",
                "next": "carrotO",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("carrotO", <EnemyNavModel>{
                "prev": "snakeG",
                "next": "goblinG",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("goblinG", <EnemyNavModel>{
                "prev": "carrotO",
                "next": "plank",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("plank", <EnemyNavModel>{
                "prev": "goblinG",
                "next": "frogBIG",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("frogBIG", <EnemyNavModel>{
                "prev": "plank",
                "next": "poopSmall",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("poopSmall", <EnemyNavModel>{
                "prev": "frogBIG",
                "next": "ratB",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("ratB", <EnemyNavModel>{
                "prev": "poopSmall",
                "next": "branch",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("branch", <EnemyNavModel>{
                "prev": "ratB",
                "next": "acorn",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("acorn", <EnemyNavModel>{
                "prev": "branch",
                "next": "Crystal0",
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("Crystal0", <EnemyNavModel>{
                "prev": "acorn",
                "next": "mushW",
                "hasCrystal": false,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("mushW", <EnemyNavModel>{
                "prev": "Crystal0",
                "next": null,
                "hasCrystal": true,
                "crystalName": "Crystal0",
                "hasCard": true
            }),
        new EnemyNavBase("jarSand", <EnemyNavModel>{
                "prev": null,
                "next": "mimicA",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("mimicA", <EnemyNavModel>{
                "prev": "jarSand",
                "next": "crabcake",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("crabcake", <EnemyNavModel>{
                "prev": "mimicA",
                "next": "coconut",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("coconut", <EnemyNavModel>{
                "prev": "crabcake",
                "next": "sandcastle",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("sandcastle", <EnemyNavModel>{
                "prev": "coconut",
                "next": "pincermin",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("pincermin", <EnemyNavModel>{
                "prev": "sandcastle",
                "next": "potato",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("potato", <EnemyNavModel>{
                "prev": "pincermin",
                "next": "steak",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("steak", <EnemyNavModel>{
                "prev": "potato",
                "next": "moonman",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("moonman", <EnemyNavModel>{
                "prev": "steak",
                "next": "sandgiant",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("sandgiant", <EnemyNavModel>{
                "prev": "moonman",
                "next": "snailZ",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("snailZ", <EnemyNavModel>{
                "prev": "sandgiant",
                "next": "shovelR",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("shovelR", <EnemyNavModel>{
                "prev": "snailZ",
                "next": "Crystal1",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("Crystal1", <EnemyNavModel>{
                "prev": "shovelR",
                "next": "Bandit_Bob",
                "hasCrystal": false,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("Bandit_Bob", <EnemyNavModel>{
                "prev": "Crystal1",
                "next": "Blank",
                "hasCrystal": true,
                "crystalName": "Crystal1",
                "hasCard": true
            }),
        new EnemyNavBase("sheep", <EnemyNavModel>{
                "prev": null,
                "next": "flake",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("flake", <EnemyNavModel>{
                "prev": "sheep",
                "next": "stache",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("stache", <EnemyNavModel>{
                "prev": "flake",
                "next": "bloque",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("bloque", <EnemyNavModel>{
                "prev": "stache",
                "next": "mamoth",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("mamoth", <EnemyNavModel>{
                "prev": "bloque",
                "next": "snowball",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("snowball", <EnemyNavModel>{
                "prev": "mamoth",
                "next": "penguin",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("penguin", <EnemyNavModel>{
                "prev": "snowball",
                "next": "thermostat",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("thermostat", <EnemyNavModel>{
                "prev": "penguin",
                "next": "glass",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("glass", <EnemyNavModel>{
                "prev": "thermostat",
                "next": "snakeB",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("snakeB", <EnemyNavModel>{
                "prev": "glass",
                "next": "speaker",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("speaker", <EnemyNavModel>{
                "prev": "snakeB",
                "next": "eye",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("eye", <EnemyNavModel>{
                "prev": "speaker",
                "next": "ram",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("ram", <EnemyNavModel>{
                "prev": "eye",
                "next": "skele",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("skele", <EnemyNavModel>{
                "prev": "ram",
                "next": "skele2",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("skele2", <EnemyNavModel>{
                "prev": "skele",
                "next": "Crystal2",
                "hasCrystal": true,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("Crystal2", <EnemyNavModel>{
                "prev": "skele2",
                "next": null,
                "hasCrystal": false,
                "crystalName": "Crystal2",
                "hasCard": true
            }),
        new EnemyNavBase("mushP", <EnemyNavModel>{
                "prev": null,
                "next": "w4a2",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4a2", <EnemyNavModel>{
                "prev": "mushP",
                "next": "w4a3",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4a3", <EnemyNavModel>{
                "prev": "w4a2",
                "next": "demonP",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("demonP", <EnemyNavModel>{
                "prev": "w4a3",
                "next": "w4b2",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4b2", <EnemyNavModel>{
                "prev": "demonP",
                "next": "w4b1",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4b1", <EnemyNavModel>{
                "prev": "w4b2",
                "next": "w4b3",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4b3", <EnemyNavModel>{
                "prev": "w4b1",
                "next": "w4b4",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4b4", <EnemyNavModel>{
                "prev": "w4b3",
                "next": "w4b5",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4b5", <EnemyNavModel>{
                "prev": "w4b4",
                "next": "w4c1",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4c1", <EnemyNavModel>{
                "prev": "w4b5",
                "next": "w4c2",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4c2", <EnemyNavModel>{
                "prev": "w4c1",
                "next": "w4c3",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4c3", <EnemyNavModel>{
                "prev": "w4c2",
                "next": "w4c4",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("w4c4", <EnemyNavModel>{
                "prev": "w4c3",
                "next": "Crystal3",
                "hasCrystal": true,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("Crystal3", <EnemyNavModel>{
                "prev": "w4c4",
                "next": "Blank",
                "hasCrystal": false,
                "crystalName": "Crystal3",
                "hasCard": true
            }),
        new EnemyNavBase("babayaga", <EnemyNavModel>{
                "prev": null,
                "next": "poopBig",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("poopBig", <EnemyNavModel>{
                "prev": "babayaga",
                "next": "poopD",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("poopD", <EnemyNavModel>{
                "prev": "poopBig",
                "next": "wolfA",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("wolfA", <EnemyNavModel>{
                "prev": "poopD",
                "next": "wolfB",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("wolfB", <EnemyNavModel>{
                "prev": "wolfA",
                "next": "wolfC",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("wolfC", <EnemyNavModel>{
                "prev": "wolfB",
                "next": "babaHour",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("babaHour", <EnemyNavModel>{
                "prev": "wolfC",
                "next": "babaMummy",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("babaMummy", <EnemyNavModel>{
                "prev": "babaHour",
                "next": "Boss2A",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss2A", <EnemyNavModel>{
                "prev": "babaMummy",
                "next": "Boss2B",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss2B", <EnemyNavModel>{
                "prev": "Boss2A",
                "next": "Boss2C",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss2C", <EnemyNavModel>{
                "prev": "Boss2B",
                "next": "mini3a",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("mini3a", <EnemyNavModel>{
                "prev": "Boss2C",
                "next": "Boss3A",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss3A", <EnemyNavModel>{
                "prev": "mini3a",
                "next": "Boss3B",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss3B", <EnemyNavModel>{
                "prev": "Boss3A",
                "next": "Boss3C",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss3C", <EnemyNavModel>{
                "prev": "Boss3B",
                "next": "mini4a",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("mini4a", <EnemyNavModel>{
                "prev": "Boss3C",
                "next": "Boss4A",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss4A", <EnemyNavModel>{
                "prev": "mini4a",
                "next": "Boss4B",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            }),
        new EnemyNavBase("Boss4B", <EnemyNavModel>{
                "prev": "Boss4A",
                "next": "Blank",
                "hasCrystal": true,
                "crystalName": null,
                "hasCard": true
            })    
]
}
