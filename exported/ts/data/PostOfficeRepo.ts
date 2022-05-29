import { PartModel } from '../model/partModel';
import { PostOfficeModel } from '../model/postOfficeModel';

export class PostOfficeBase { constructor(public id: string, public data: PostOfficeModel) { } }



export const initPostOfficeRepo = () => {
    return [    
        new PostOfficeBase("Simple Shippin", <PostOfficeModel>{
                "orders": [
                    <PartModel>{"item": "Copper", "base": 150, "increment": 1.27},
                    <PartModel>{"item": "Iron", "base": 150, "increment": 1.23},
                    <PartModel>{"item": "CopperBar", "base": 50, "increment": 1.25},
                    <PartModel>{"item": "OakTree", "base": 200, "increment": 1.27},
                    <PartModel>{"item": "BirchTree", "base": 100, "increment": 1.26},
                    <PartModel>{"item": "JungleTree", "base": 80, "increment": 1.25},
                    <PartModel>{"item": "Fish1", "base": 120, "increment": 1.23},
                    <PartModel>{"item": "Bug1", "base": 120, "increment": 1.23},
                    <PartModel>{"item": "Fish2", "base": 100, "increment": 1.22},
                    <PartModel>{"item": "Bug2", "base": 100, "increment": 1.22},
                    <PartModel>{"item": "IronBar", "base": 50, "increment": 1.18},
                    <PartModel>{"item": "CraftMat1", "base": 100, "increment": 1.2},
                    <PartModel>{"item": "CraftMat5", "base": 40, "increment": 1.2},
                    <PartModel>{"item": "Gold", "base": 100, "increment": 1.23},
                    <PartModel>{"item": "GoldBar", "base": 25, "increment": 1.15},
                    <PartModel>{"item": "ToiletTree", "base": 125, "increment": 1.22},
                    <PartModel>{"item": "Fish3", "base": 70, "increment": 1.2},
                    <PartModel>{"item": "Bug3", "base": 90, "increment": 1.2},
                    <PartModel>{"item": "CraftMat6", "base": 25, "increment": 1.19},
                    <PartModel>{"item": "PalmTree", "base": 110, "increment": 1.23},
                    <PartModel>{"item": "Fish4", "base": 40, "increment": 1.18},
                    <PartModel>{"item": "StumpTree", "base": 100, "increment": 1.21},
                    <PartModel>{"item": "Bug4", "base": 65, "increment": 1.18}
                ],
                "coinRewards": [1, 14, 12, 3, 10],
                "rewards": [
                    <PartModel>{"item": "StoneA1", "base": 2, "increment": 0},
                    <PartModel>{"item": "StoneW1", "base": 1, "increment": 0},
                    <PartModel>{"item": "StoneT1", "base": 2, "increment": 0},
                    <PartModel>{"item": "FoodG1", "base": 1, "increment": 0},
                    <PartModel>{"item": "Peanut", "base": 50, "increment": 0},
                    <PartModel>{"item": "EquipmentStatues1", "base": 1, "increment": 0},
                    <PartModel>{"item": "ExpBalloon1", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentStatues4", "base": 1, "increment": 1},
                    <PartModel>{"item": "Key1", "base": 1, "increment": 1},
                    <PartModel>{"item": "Key2", "base": 1, "increment": 2},
                    <PartModel>{"item": "StoneHelm1", "base": 1, "increment": 2},
                    <PartModel>{"item": "PremiumGem", "base": 1, "increment": 3}
                ]
            }),
        new PostOfficeBase("Plan-it Express", <PostOfficeModel>{
                "orders": [
                    <PartModel>{"item": "EquipmentHats1", "base": 1, "increment": 1.023},
                    <PartModel>{"item": "TestObj1", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "EquipmentShoes9", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "EquipmentShoes1", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "EquipmentShoes15", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "EquipmentHats15", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "EquipmentShirts11", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "EquipmentHats16", "base": 1, "increment": 1.018},
                    <PartModel>{"item": "EquipmentShirts2", "base": 1, "increment": 1.018},
                    <PartModel>{"item": "EquipmentBows3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentTools3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentHats18", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentHats28", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentPunching3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentWands5", "base": 1, "increment": 1},
                    <PartModel>{"item": "TestObj3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentToolsHatchet1", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentShirts24", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentShoes3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentRings2", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentBows4", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentShirts3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentBows5", "base": 1, "increment": 1},
                    <PartModel>{"item": "FishingRod4", "base": 1, "increment": 1},
                    <PartModel>{"item": "CatchingNet4", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentBows6", "base": 1, "increment": 1},
                    <PartModel>{"item": "FishingRod5", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentPants5", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentToolsHatchet4", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentTools6", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentShoes4", "base": 1, "increment": 1}
                ],
                "coinRewards": [1, 17, 15, 3, 10],
                "rewards": [
                    <PartModel>{"item": "StoneA1", "base": 2, "increment": 0},
                    <PartModel>{"item": "StoneW1", "base": 2, "increment": 0},
                    <PartModel>{"item": "FoodG4", "base": 1, "increment": 0},
                    <PartModel>{"item": "FoodPotGr2", "base": 100, "increment": 0},
                    <PartModel>{"item": "ExpBalloon1", "base": 1, "increment": 0},
                    <PartModel>{"item": "EquipmentStatues4", "base": 1, "increment": 0},
                    <PartModel>{"item": "StoneA2", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneT2", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentStatues6", "base": 1, "increment": 1},
                    <PartModel>{"item": "Key1", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneHelm1", "base": 1, "increment": 1},
                    <PartModel>{"item": "FoodPotYe1", "base": 100, "increment": 2},
                    <PartModel>{"item": "Key2", "base": 1, "increment": 2},
                    <PartModel>{"item": "StoneW2", "base": 1, "increment": 2},
                    <PartModel>{"item": "PremiumGem", "base": 1, "increment": 3}
                ]
            }),
        new PostOfficeBase("Dudes Next Door", <PostOfficeModel>{
                "orders": [
                    <PartModel>{"item": "Grasslands1", "base": 125, "increment": 1.25},
                    <PartModel>{"item": "Grasslands2", "base": 120, "increment": 1.24},
                    <PartModel>{"item": "Grasslands3", "base": 115, "increment": 1.23},
                    <PartModel>{"item": "Jungle1", "base": 110, "increment": 1.22},
                    <PartModel>{"item": "Jungle2", "base": 105, "increment": 1.22},
                    <PartModel>{"item": "Jungle3", "base": 100, "increment": 1.21},
                    <PartModel>{"item": "Forest1", "base": 100, "increment": 1.21},
                    <PartModel>{"item": "Forest2", "base": 90, "increment": 1.22},
                    <PartModel>{"item": "Forest3", "base": 90, "increment": 1.22},
                    <PartModel>{"item": "DesertA1", "base": 100, "increment": 1.25},
                    <PartModel>{"item": "Sewers1", "base": 100, "increment": 1.21},
                    <PartModel>{"item": "DesertA2", "base": 95, "increment": 1.24},
                    <PartModel>{"item": "TreeInterior1", "base": 80, "increment": 1.21},
                    <PartModel>{"item": "DesertA3", "base": 150, "increment": 1.23},
                    <PartModel>{"item": "Sewers2", "base": 100, "increment": 1.2},
                    <PartModel>{"item": "TreeInterior2", "base": 70, "increment": 1.21},
                    <PartModel>{"item": "Quest17", "base": 2, "increment": 1.04},
                    <PartModel>{"item": "DesertB1", "base": 100, "increment": 1.23},
                    <PartModel>{"item": "DesertB2", "base": 100, "increment": 1.23},
                    <PartModel>{"item": "DesertB3", "base": 80, "increment": 1.22},
                    <PartModel>{"item": "DesertB4", "base": 80, "increment": 1.22},
                    <PartModel>{"item": "DesertC1", "base": 80, "increment": 1.22},
                    <PartModel>{"item": "DesertC2", "base": 80, "increment": 1.21},
                    <PartModel>{"item": "DesertC3", "base": 80, "increment": 1.21},
                    <PartModel>{"item": "DesertC4", "base": 80, "increment": 1.21},
                    <PartModel>{"item": "EfauntDrop1", "base": 2, "increment": 1.04}
                ],
                "coinRewards": [1, 10, 13, 3, 10],
                "rewards": [
                    <PartModel>{"item": "StoneA1", "base": 2, "increment": 0},
                    <PartModel>{"item": "StoneW1", "base": 2, "increment": 0},
                    <PartModel>{"item": "FoodG2", "base": 1, "increment": 0},
                    <PartModel>{"item": "FoodPotYe2", "base": 100, "increment": 0},
                    <PartModel>{"item": "OilBarrel3", "base": 20, "increment": 0},
                    <PartModel>{"item": "ExpBalloon1", "base": 1, "increment": 0},
                    <PartModel>{"item": "StoneA2", "base": 1, "increment": 0},
                    <PartModel>{"item": "StoneT2", "base": 1, "increment": 0},
                    <PartModel>{"item": "StoneW2", "base": 1, "increment": 1},
                    <PartModel>{"item": "Key2", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneA2", "base": 2, "increment": 2},
                    <PartModel>{"item": "StoneT2", "base": 2, "increment": 2},
                    <PartModel>{"item": "StoneW3", "base": 1, "increment": 3},
                    <PartModel>{"item": "PremiumGem", "base": 2, "increment": 3}
                ]
            }),
        new PostOfficeBase("Down Undelivery", <PostOfficeModel>{
                "orders": [
                    <PartModel>{"item": "DesertA3b", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "DesertA1b", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "DesertC2b", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "TreeInterior1b", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "Sewers1b", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "SnowA2a", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "SnowB2a", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "SnowC4a", "base": 1, "increment": 1.03}
                ],
                "coinRewards": [1, 3, 2, 10, 10],
                "rewards": [
                    <PartModel>{"item": "StoneA2", "base": 2, "increment": 0},
                    <PartModel>{"item": "StoneW2", "base": 2, "increment": 0},
                    <PartModel>{"item": "FoodG5", "base": 1, "increment": 0},
                    <PartModel>{"item": "FoodPotGr3", "base": 100, "increment": 0},
                    <PartModel>{"item": "OilBarrel3", "base": 30, "increment": 0},
                    <PartModel>{"item": "ExpBalloon1", "base": 1, "increment": 0},
                    <PartModel>{"item": "EquipmentStatues13", "base": 1, "increment": 0},
                    <PartModel>{"item": "EquipmentStatues14", "base": 1, "increment": 0},
                    <PartModel>{"item": "StoneA2", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneT2", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentStatues15", "base": 1, "increment": 1},
                    <PartModel>{"item": "Key1", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneHelm1", "base": 1, "increment": 1},
                    <PartModel>{"item": "FoodPotYe2", "base": 100, "increment": 2},
                    <PartModel>{"item": "Key2", "base": 1, "increment": 2},
                    <PartModel>{"item": "StoneW3", "base": 1, "increment": 2},
                    <PartModel>{"item": "PremiumGem", "base": 1, "increment": 3}
                ]
            }),
        new PostOfficeBase("Alpine Suppliers", <PostOfficeModel>{
                "orders": [
                    <PartModel>{"item": "SnowA1", "base": 250, "increment": 1.3},
                    <PartModel>{"item": "SnowA2", "base": 230, "increment": 1.29},
                    <PartModel>{"item": "SnowA3", "base": 220, "increment": 1.28},
                    <PartModel>{"item": "SnowB1", "base": 210, "increment": 1.273},
                    <PartModel>{"item": "SnowB2", "base": 200, "increment": 1.265},
                    <PartModel>{"item": "SnowB5", "base": 180, "increment": 1.26},
                    <PartModel>{"item": "SnowB3", "base": 170, "increment": 1.255},
                    <PartModel>{"item": "SnowB4", "base": 160, "increment": 1.25},
                    <PartModel>{"item": "SnowC1", "base": 150, "increment": 1.25},
                    <PartModel>{"item": "SnowC2", "base": 145, "increment": 1.245},
                    <PartModel>{"item": "SnowC3", "base": 140, "increment": 1.24},
                    <PartModel>{"item": "SnowC4", "base": 135, "increment": 1.235},
                    <PartModel>{"item": "SnowA4", "base": 100, "increment": 1.23},
                    <PartModel>{"item": "SnowC5", "base": 50, "increment": 1.15}
                ],
                "coinRewards": [1, 4, 2, 5, 10],
                "rewards": [
                    <PartModel>{"item": "StoneA1", "base": 2, "increment": 0},
                    <PartModel>{"item": "StoneW1", "base": 2, "increment": 0},
                    <PartModel>{"item": "FoodG6", "base": 1, "increment": 0},
                    <PartModel>{"item": "FoodPotGr3", "base": 100, "increment": 0},
                    <PartModel>{"item": "OilBarrel3", "base": 50, "increment": 0},
                    <PartModel>{"item": "ExpBalloon1", "base": 1, "increment": 0},
                    <PartModel>{"item": "EquipmentStatues18", "base": 1, "increment": 0},
                    <PartModel>{"item": "OilBarrel3", "base": 100, "increment": 1},
                    <PartModel>{"item": "DesertA3b", "base": 1, "increment": 1},
                    <PartModel>{"item": "TreeInterior1b", "base": 1, "increment": 1},
                    <PartModel>{"item": "Sewers1b", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneA3", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneT3", "base": 1, "increment": 1},
                    <PartModel>{"item": "EquipmentStatues19", "base": 1, "increment": 1},
                    <PartModel>{"item": "Key2", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneHelm1", "base": 1, "increment": 1},
                    <PartModel>{"item": "FoodPotYe2", "base": 100, "increment": 2},
                    <PartModel>{"item": "Key3", "base": 1, "increment": 2},
                    <PartModel>{"item": "StoneW3", "base": 1, "increment": 2},
                    <PartModel>{"item": "StoneHelm6", "base": 1, "increment": 3},
                    <PartModel>{"item": "PremiumGem", "base": 1, "increment": 3}
                ]
            }),
        new PostOfficeBase("Cosmic Carrier", <PostOfficeModel>{
                "orders": [
                    <PartModel>{"item": "GalaxyA1", "base": 500, "increment": 1.4},
                    <PartModel>{"item": "GalaxyA3", "base": 500, "increment": 1.4},
                    <PartModel>{"item": "GalaxyA2b", "base": 1, "increment": 1.03},
                    <PartModel>{"item": "AlienTree", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "Fish5", "base": 250, "increment": 1.4},
                    <PartModel>{"item": "GalaxyB1", "base": 1000, "increment": 1.4},
                    <PartModel>{"item": "Bug7", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "GalaxyB3", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "GalaxyB4", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "Lustre", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "GalaxyC1", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "Tree8", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "GalaxyC1b", "base": 1, "increment": 1.02},
                    <PartModel>{"item": "GalaxyC4", "base": 300, "increment": 1.4},
                    <PartModel>{"item": "Starfire", "base": 100, "increment": 1.4},
                    <PartModel>{"item": "Bug8", "base": 300, "increment": 1.4}
                ],
                "coinRewards": [1, 5, 5, 7, 10],
                "rewards": [
                    <PartModel>{"item": "StoneA4", "base": 3, "increment": 0},
                    <PartModel>{"item": "StoneW4", "base": 2, "increment": 0},
                    <PartModel>{"item": "StoneT4", "base": 2, "increment": 0},
                    <PartModel>{"item": "FoodG7", "base": 1, "increment": 0},
                    <PartModel>{"item": "Ladle", "base": 3, "increment": 0},
                    <PartModel>{"item": "ExpBalloon2", "base": 1, "increment": 1},
                    <PartModel>{"item": "TixCol", "base": 1, "increment": 1},
                    <PartModel>{"item": "StoneA3b", "base": 1, "increment": 2},
                    <PartModel>{"item": "StoneW3b", "base": 1, "increment": 2}
                ]
            })    
]
}
