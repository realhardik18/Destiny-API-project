import DestinyDatabaseTable from "./Types/Destiny2/DestinyDatabaseTable.js";
import { Cache } from "./Types/Cache/interfaces.js";
import Database from "better-sqlite3";
import { AllDestinyManifestComponents } from "./Types/Destiny2/interfaces.js";

function merge(array: any) {
  const merged_dict: any = {};
  array.forEach((ele: any) => {
    merged_dict[ele] = {};
  });
  return merged_dict;
}

export default class DestinyItemCache {
  private cache: Cache;
  private db: Database.Database;

  constructor() {
    this.db = new Database("db.sqlite3");
    this.cache = merge(Object.values(DestinyDatabaseTable));
  }

  public get(table: DestinyDatabaseTable, hash: number) {
    let current = this.cache[table][hash];
    if (current) return current;
    else {
      let item = this.getFromDB(table, hash);
      if (item != undefined) this.set(table, hash, item);
      return item;
    }
  }

  private getFromDB(table: DestinyDatabaseTable, hash: number) {
    let signedHash = new Int32Array([hash])[0];
    let item = this.db
      .prepare(`SELECT * FROM ${table} WHERE id=${signedHash}`)
      .get();
    return item ? JSON.parse(item.json) : undefined;
  }

  private async set(table: DestinyDatabaseTable, hash: number, item: any) {
    this.cache[table][hash] = item;
  }
}
