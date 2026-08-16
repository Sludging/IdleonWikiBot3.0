import { MineheadButtonBonusModel } from '../model/mineheadButtonBonusModel';

export class MineheadButtonBonusBase { constructor(public index: number, public data: MineheadButtonBonusModel) { } }



export const initMineheadButtonBonusRepo = () => {
    return [    
        new MineheadButtonBonusBase(0, <MineheadButtonBonusModel>{"index": 0, "bonusPerCycle": 2}),
        new MineheadButtonBonusBase(1, <MineheadButtonBonusModel>{"index": 1, "bonusPerCycle": 3}),
        new MineheadButtonBonusBase(2, <MineheadButtonBonusModel>{"index": 2, "bonusPerCycle": 2}),
        new MineheadButtonBonusBase(3, <MineheadButtonBonusModel>{"index": 3, "bonusPerCycle": 2}),
        new MineheadButtonBonusBase(4, <MineheadButtonBonusModel>{"index": 4, "bonusPerCycle": 4}),
        new MineheadButtonBonusBase(5, <MineheadButtonBonusModel>{"index": 5, "bonusPerCycle": 5}),
        new MineheadButtonBonusBase(6, <MineheadButtonBonusModel>{"index": 6, "bonusPerCycle": 4}),
        new MineheadButtonBonusBase(7, <MineheadButtonBonusModel>{"index": 7, "bonusPerCycle": 25}),
        new MineheadButtonBonusBase(8, <MineheadButtonBonusModel>{"index": 8, "bonusPerCycle": 5})    
]
}
