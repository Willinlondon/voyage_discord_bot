import os
import re
import wowapi

wow_api_client = wowapi.WowApi(os.getenv('BLIZZARD_CLIENT_ID'), os.getenv('BLIZZARD_CLIENT_SECRET'))

identify_api_call_pattern = re.compile("\${\wow_api\.([a-zA-Z_-].+)\(([0-9,]+)?\)\}")

wow_class_icons = {"1": "<:warrior:785139541102690324>",
                   "2": "<:paladin:785139814474186762>",
                   "3": "<:hunter:785140043596431361>",
                   "4": "<:rogue:785130266410483732>",
                   "5": "<:priest:785140414134091787>",
                   "6": "<:deathknight:785141081082953729>",
                   "7": "<:shaman:785140414142742539>",
                   "8": "<:mageclass:785141081393725470>",
                   "9": "<:warlock:785140413743759413>",
                   "10": "<:monk:785140414155849758>",
                   "11": "<:druid:785141081389662228>",
                   "12": "<:demonhunter:785141081355321374>"}

def fetch_ranks(args):
    rank_list = args[0]
    roster_json = wow_api_client.get_guild_roster("eu", "profile-eu", "frostmane", "silverblade")
    
    list_of_ranks_matching_criteria = [member["character"]["name"] 
                                         for member in roster_json["members"] 
                                             if str(member["rank"]) in rank_list.split(",")]
    
    join_ranks_into_formatted_list = "\n - ".join(list_of_ranks_matching_criteria)
    
    return f" - {join_ranks_into_formatted_list}"

def fetch_roster(args):
    roster_json = wow_api_client.get_guild_roster("eu", "profile-eu", "frostmane", "silverblade")
    
    list_of_ranks_matching_criteria = [(member["character"]["playable_class"]["id"], member["character"]["name"])
                                         for member in roster_json["members"] 
                                             if int(member["rank"]) in [0,1,2,3,4]]
    
    list_of_ranks_matching_criteria.sort()
    
    formatted_list_of_ranks_matching_criteria = [f"{wow_class_icons[str(member[0])]} `{member[1]}`" for member in list_of_ranks_matching_criteria]
    
    join_ranks_into_formatted_list = "\n  ".join(formatted_list_of_ranks_matching_criteria)
    
    return f"  {join_ranks_into_formatted_list}"

functionality = {"fetch_ranks": fetch_ranks, "fetch_roster": fetch_roster}

def parse(content):
    possible_match = identify_api_call_pattern.search(content)
    if possible_match == None: # Just return the content if there's no match, it may have been intended
        return content
    else:
        wow_api_function = possible_match.groups()[0]
        if wow_api_function in functionality:
            return identify_api_call_pattern.sub(functionality[wow_api_function](possible_match.groups()[1:]), content)
        else:
            return content
