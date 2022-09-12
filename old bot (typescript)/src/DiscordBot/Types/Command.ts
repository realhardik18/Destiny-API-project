import { ApplicationCommandOptionData } from "discord.js";

export default interface Command {
  name: string;
  description: string;
  options?: [ApplicationCommandOptionData];
  execute?: Function;
  autocomplete?: Function;
}
