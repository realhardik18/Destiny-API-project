import DestinyDatabaseTable from "../Destiny2/DestinyDatabaseTable";

export type Cache = {
  [key in DestinyDatabaseTable]: {
    [key: number]: any;
  };
};
