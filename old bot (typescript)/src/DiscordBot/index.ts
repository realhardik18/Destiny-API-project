import CMDHandler from "./Handlers/CommandHandler.js";
import { Client, IntentsBitField } from "discord.js";
import DestinyItemCache from "../DestinyAPI/cache.js";

export const ItemCache = new DestinyItemCache();

export const client = new Client({
  intents: [IntentsBitField.Flags.GuildIntegrations],
});
const CommandHandler = new CMDHandler();

client.on("ready", async () => {
  client?.application?.commands.set(CommandHandler.commands);
  console.log("Ready!")
});

client.on("interactionCreate", async (interaction) => {
  if (interaction.isCommand()) {
    CommandHandler.run(interaction, interaction.commandName);
  }
  if (interaction.isAutocomplete()) {
    CommandHandler.autocomplete(interaction, interaction.commandName);
  }
});

client.login(
  "MTAwNzY1MzU3MjE2ODY2MzE5MQ.GnmKkB.F9EhB6f5QDmLVg86Mon_hQj8x6VWbmsACZzePE"
);
