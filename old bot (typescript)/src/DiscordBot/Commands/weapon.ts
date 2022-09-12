import {
  AutocompleteInteraction,
  CommandInteraction,
  EmbedBuilder,
} from "discord.js";
import Database from "better-sqlite3";
import { ItemCache } from "../index.js";
import DestinyDatabaseTable from "../../DestinyAPI/Types/Destiny2/DestinyDatabaseTable.js";
import WeaponAttributes from "../../DestinyAPI/Classes/WeaponAttributes.js";

function format(x: any) {
  return `Name: **${x.displayProperties.name}**\nDescription: ${x.displayProperties.description}`;
}

export default {
  name: "weapon",
  description: "Get Weapon Data",
  options: [
    {
      type: 3,
      name: "weapon-name",
      description: "The name of the weapon",
      autocomplete: true,
      required: true,
    },
  ],
  async execute(interaction: CommandInteraction) {
    //await interaction.deferReply({ ephemeral: true });
    let item = await ItemCache.get(
      DestinyDatabaseTable.DestinyInventoryItemDefinition,
      Number(interaction.options.data[0].value)
    );
    if (!item)
      return interaction.reply({
        ephemeral: true,
        content: "That weapon does not exist",
      });
    let attributes = new WeaponAttributes(item);
    let embed = new EmbedBuilder();
    embed.setTitle(item.displayProperties.name);
    embed.addFields([
      {
        name: "Perks",
        value: attributes.perks
          .slice(0, 5)
          .map((x) => format(x))
          .join("\n"),
      },
      {
        name: "Curated Roll",
        value: attributes.curatedRoll
          .slice(0, 5)
          .map((x) => format(x))
          .join("\n"),
      },
      {
        name: "Mods",
        value: attributes.mods
          .slice(0, 5)
          .map((x) => format(x))
          .join("\n"),
      },
    ]);
    embed.setImage("https://www.bungie.net" + item.screenshot);
    interaction.reply({ embeds: [embed] });
  },
  autocomplete(interaction: AutocompleteInteraction) {
    try {
      let db = new Database("db.sqlite3");
      const focusedValue = interaction.options.getFocused();
      let items = db
        .prepare(
          `SELECT * FROM DestinyInventoryItemDefinition WHERE json_extract(json, '$.displayProperties.name') like '${focusedValue}%' AND json_extract(json, '$.itemType') = 3 AND json_extract(json, '$.iconWatermark') not null LIMIT 25`
        )
        .all();
      let choices = items.map((i) => JSON.parse(i.json));

      interaction.respond(
        choices.map((choice) => ({
          name: choice.displayProperties.name,
          value: String(choice.hash),
        }))
      );
    } catch (error) {
      return;
    }
  },
};
