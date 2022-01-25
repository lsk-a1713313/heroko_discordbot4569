const readline = require('readline');
const Discord = require('discord.js');
const client = new Discord.Client();
const config = require("./config.json");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);

    rl.question('935367951232679966', (channel) => {
        var input = function () {
            rl.question('', (msg) => {
                if (msg == '-l') { return rl.close(); }
                else {
                    client.channels.fetch(channel)
                        .then(cnl => cnl.send(msg))
                        .catch(console.error);
                    input();
                }
            })
        }
        input();
    });
});
client.login(config.ODc5OTY2MjIyMTIzNDEzNTQ0.YSXaaA.XzpftymOLHhy9DK7Ak_wM98F8Pk);
