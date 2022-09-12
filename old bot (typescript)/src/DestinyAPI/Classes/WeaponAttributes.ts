import { ItemCache } from "../../DiscordBot/index.js";
import DestinyDatabaseTable from "../Types/Destiny2/DestinyDatabaseTable.js";
import {
  DestinyInventoryItemDefinition,
  DestinyPlugSetDefinition,
} from "../Types/Destiny2/interfaces.js";

/* AttributeTypes 
  perks = 4241085061,
  mods = 2685412949,
  cosmetics = 2048875504,
  curatedRoll = "curatedRoll",
*/

export default class WeaponAttributes {
  private weapon: DestinyInventoryItemDefinition;
  constructor(weapon: DestinyInventoryItemDefinition) {
    if (weapon.itemType != 3) throw "Item must be a weapon";
    this.weapon = weapon;
  }
  get perks(): Array<DestinyInventoryItemDefinition> {
    let plugs: Array<DestinyInventoryItemDefinition> = [];
    this.weapon
      .sockets!.socketCategories.filter(
        (x) => x.socketCategoryHash === 4241085061
      )[0]
      ["socketIndexes"].map((x) => {
        let soc = this.weapon.sockets!.socketEntries[x];
        if (!soc["reusablePlugSetHash"] && !soc["randomizedPlugSetHash"])
          return;
        let plugSet: DestinyPlugSetDefinition = ItemCache.get(
          DestinyDatabaseTable.DestinyPlugSetDefinition,
          (soc["reusablePlugSetHash"] || soc["randomizedPlugSetHash"])!
        );
        if (plugSet.isFakePlugSet) return;
        plugSet.reusablePlugItems.map((x) => {
          let plug = ItemCache.get(
            DestinyDatabaseTable.DestinyInventoryItemDefinition,
            x.plugItemHash
          );
          plugs.push(plug);
        });
      });
    return plugs;
  }
  get mods(): Array<DestinyInventoryItemDefinition> {
    let plugs: Array<DestinyInventoryItemDefinition> = [];
    this.weapon
      .sockets!.socketCategories.filter(
        (x) => x.socketCategoryHash === 2685412949
      )[0]
      ["socketIndexes"].map((x) => {
        let soc = this.weapon.sockets!.socketEntries[x];
        if (!soc["reusablePlugSetHash"] && !soc["randomizedPlugSetHash"])
          return;
        let plugSet: DestinyPlugSetDefinition = ItemCache.get(
          DestinyDatabaseTable.DestinyPlugSetDefinition,
          (soc["reusablePlugSetHash"] || soc["randomizedPlugSetHash"])!
        );
        if (plugSet.isFakePlugSet) return;
        plugSet.reusablePlugItems.map((x) => {
          let plug = ItemCache.get(
            DestinyDatabaseTable.DestinyInventoryItemDefinition,
            x.plugItemHash
          );
          plugs.push(plug);
        });
      });
    return plugs;
  }
  get curatedRoll(): Array<DestinyInventoryItemDefinition> {
    let plugs: Array<DestinyInventoryItemDefinition> = [];
    this.weapon.sockets!.socketEntries.map((x: any) => {
      let plug = ItemCache.get(
        DestinyDatabaseTable.DestinyInventoryItemDefinition,
        x.singleInitialItemHash
      );
      if (plug.itemTypeDisplayName === "Trait") plugs.push(plug);
    });
    return plugs;
  }
}
