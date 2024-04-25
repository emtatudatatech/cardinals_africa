def country_rename(nation):
    """
        Renames the nation names to a uniform standard for 
        certain nations who have names with special
        characters.
    """
    if nation == "Cabo Verde":
        return "Cape Verde"
    elif nation == "Congo, Republic of ":
        return "Congo"
    elif nation == "Congo, Dem. Rep. of the":
        return "Democratic Republic of the Congo"
    elif nation == "Gambia, The":
        return "Gambia"
    elif nation == "Côte d'Ivoire":
        return "Cote d'Ivoire"
    elif nation == "São Tomé and Príncipe":
        return "Sao Tome and Principe"
    elif nation == "South Sudan, Republic of":
        return "South Sudan"
    else:
        return nation
    
