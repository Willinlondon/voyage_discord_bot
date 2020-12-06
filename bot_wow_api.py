import os
import re
import wowapi

wow_api_client = wowapi.WowApi(os.getenv('BLIZZARD_CLIENT_ID'), os.getenv('BLIZZARD_CLIENT_SECRET'))

identify_api_call_pattern = re.compile("\${\wow_api\.([a-zA-Z_-].+)\(([0-9,]+)?\)\}")

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
    
    list_of_ranks_matching_criteria = [f':rogue: {member["character"]["name"]}'
                                         for member in roster_json["members"] 
                                             if str(member["rank"]) in [0,1,2,3,4]]
    
    join_ranks_into_formatted_list = "\n - ".join(list_of_ranks_matching_criteria)
    
    return f" - {join_ranks_into_formatted_list}"

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
