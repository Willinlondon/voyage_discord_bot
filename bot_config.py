import configparser

config = configparser.RawConfigParser()
config.read('config/config.properties')

DISCORD_APPLICATION_CHANNEL = config.getint('Discord', 'applications.channel')
DISCORD_GUILD = config.getint('Discord', 'guild')
DISCORD_OFFICER_CHANNEL = config.getint('Discord', 'officer.channel')
DISCORD_OFFICER_SIM_CHANNEL = config.getint('Discord', 'officer.sim.channel')
DISCORD_RAIDBOTS_USER_ID = config.getint('Discord', 'raidbots.user.id')

GAME_GUILD = config.get('Game', 'guild')
GAME_REALM = config.get('Game', 'realm')
GAME_REGION = config.get('Game', 'region')

print(f"Loaded: DISCORD_APPLICATION_CHANNEL={DISCORD_APPLICATION_CHANNEL}")
print(f"Loaded: DISCORD_GUILD={DISCORD_GUILD}")
print(f"Loaded: DISCORD_OFFICER_CHANNEL={DISCORD_OFFICER_CHANNEL}")
print(f"Loaded: DISCORD_OFFICER_SIM_CHANNEL={DISCORD_OFFICER_SIM_CHANNEL}")
print(f"Loaded: DISCORD_RAIDBOTS_USER_ID={DISCORD_RAIDBOTS_USER_ID}")

print(f"Loaded: GAME_GUILD={GAME_GUILD}")
print(f"Loaded: GAME_REALM={GAME_REALM}")
print(f"Loaded: GAME_REGION={GAME_REGION}")
