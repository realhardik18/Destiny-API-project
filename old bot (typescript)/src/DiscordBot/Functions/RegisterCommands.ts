import { Client } from "discord.js";
import CommandHandler from "../Handlers/CommandHandler.js";
export default function RegisterCommands(
  commandHandler: CommandHandler,
  client: Client
) {
  client?.application?.commands.set(commandHandler.commands);
}
