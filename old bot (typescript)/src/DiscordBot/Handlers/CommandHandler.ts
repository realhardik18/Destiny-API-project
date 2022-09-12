import {
  ApplicationCommandOptionWithChoicesAndAutocompleteMixin,
  AutocompleteInteraction,
  CommandInteraction,
} from "discord.js";
import path from "path";
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
import fs from "fs";
import Command from "../Types/Command.js";

export default class CommandHandler {
  private cmds: {
    [key: string]: Command;
  };
  constructor() {
    this.cmds = {};
    let commandFolder = "../Commands/";
    fs.readdirSync(__dirname + "/" + commandFolder).forEach(async (file) => {
      if (file.endsWith(".js")) {
        let command = (
          await import(`file://${__dirname}/${commandFolder}/${file}`)
        ).default;
        this.cmds[command.name] = command;
      }
    });
  }
  get commands() {
    let commands: Array<Command> = [];
    Object.values(this.cmds).map((x) => {
      let data: Command = {
        name: x.name,
        description: x.description,
      };
      if (x.options) data["options"] = x.options;
      commands.push(data);
    });
    return commands;
  }
  run(interaction: CommandInteraction, name: string) {
    if (this.cmds[name]) {
      let command = this.cmds[name];
      command.execute?.(interaction);
    } else {
      interaction.reply({ content: "Command not found", ephemeral: true });
    }
  }
  async autocomplete(interaction: AutocompleteInteraction, name: string) {
    if (this.cmds[name]) {
      let command = this.cmds[name];
      command.autocomplete?.(interaction);
    }
  }
}
