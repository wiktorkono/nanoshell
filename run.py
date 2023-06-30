import os, json

addonList = [] #[0 name, 1 triggerCmd, 2 initFoo]

addons = os.listdir("addons")
howManyAddons = 0
print(f"addons: {addons}")
print("Loading addons...")
for addon in addons:
    howManyAddons += 1
    addonScripts = os.listdir(os.path.join("addons", addon))
    print(f"addon scripts: {addonScripts}")
    for obj in addonScripts:
        if obj.endswith(".json"):
            addonData = json.load(open(os.path.abspath(os.path.join("addons", addon, obj))))
            addonList.append([addonData["name"], addonData["triggerCmd"], addonData["initFoo"]])
print("Successfully loaded addons", 100)

with open("nanoshell.py", "a") as f:
    i = 0
    for addon in addonList:
        if i != 0: el = "el" # so it can be elif instead of if
        else: el = ""
        triggerCmd = addon[1]
        initFoo = addon[2]
        f.write(f"\n    {el}if prompt.startswith('{triggerCmd}'): {initFoo}(prompt)")
        i += 1