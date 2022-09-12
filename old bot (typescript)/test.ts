import Database from "better-sqlite3";

let db = new Database("db.sqlite3");

let items = db.prepare("SELECT * FROM DestinyInventoryItemDefinition").all()


console.log(items)