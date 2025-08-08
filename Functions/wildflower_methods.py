from Objects.wildflower import WildFlower
from Dictionary.wildflower_dict import wildflowers
from rich import print
from rich.console import Console

# Create a console instance for styled input prompts
console = Console(highlight=False, markup=True)
#return a list of names of all flowers
def return_all():
    print("""
[green]Northeast:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          """)
    for wildflower in wildflowers.values():
        if "Northeast" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
    print("""
[green]Southeast:[/green]         
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          """)
    for wildflower in wildflowers.values():
        if "Southeast" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
    print("""
[green]Midwest:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          """)
    for wildflower in wildflowers.values():
        if "Midwest" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")            
    print("""
[green]Northwest:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          """)
    for wildflower in wildflowers.values():
        if "Northwest" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
    print("""
[green]Southwest:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          """)
    for wildflower in wildflowers.values():
        if "Southwest" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")

def return_wildflower(name):
    # Convert input to lowercase for case-insensitive matching
    name_lower = name.lower()
    
    for wildflower in wildflowers.values():
        # Compare lowercase versions for case-insensitive matching
        if (wildflower.name.lower() == name_lower or 
            wildflower.scientific.lower() == name_lower):
            return(f"""
[green]Name:[/green] [purple]{wildflower.name}[/purple]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]

[green]Scientific Name:[/green] [purple]{wildflower.scientific}[/purple]

[green]Region:[/green] [purple]{wildflower.region}[/purple]

[green]Zone:[/green] [purple]{wildflower.zone}[/purple]

[green]Toxicity:[/green] [purple]{wildflower.safety}[/purple]
{wildflower.return_germination_info()}
{wildflower.return_info()}
                  """)
    print(f"[purple]Unidentified keyword: {name}[/purple]")
   
#Return flowers based on region    
def return_northeast():
    print('''
[green]Northeastern Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Northeast" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")

def return_southeast():
    print('''
[green]Southeastern Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Southeast" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_midwest():
    print('''
[green]Midwestern Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Midwest" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_northwest():
    print('''
[green]Northwestern Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Northwest" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_southwest():
    print('''
[green]Southwestern Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Southwest" in wildflower.region:
            print(f"[purple]{wildflower.name}[/purple]")
            
#Add/Delete wildflowers

def add_wildflower():
    name = ''
    scientific = ''
    region = ''
    zone = ''
    safety = ''
    germination = {}
    info = {}
    count = 0
    #Loops through required fields to add a new wildflower
    #If the user enters a value, it is stored in the appropriate variable
    #If the user does not enter a value, the loop continues until a value is entered
    #Once all required fields are filled, a new WildFlower object is created and added to
    while count <=6:
        if count == 0:
            user_input = console.input("[bold cyan]Enter wildflower name: [/bold cyan]")
            name = user_input
            count +=1
        elif count == 1:
            user_input = console.input("[bold cyan]Enter scientific name: [/bold cyan]")
            scientific = user_input
            count +=1
        elif count == 2:
            user_input = console.input("[bold cyan]Enter wildflower's region: [/bold cyan]")
            region = user_input
            count +=1
        elif count == 3:
            user_input = console.input("[bold cyan]Enter wildflower's zone: [/bold cyan]")
            zone = user_input
            count +=1
        elif count == 4:
            user_input = console.input("[bold cyan]Is the wildflower edible or toxic?: [/bold cyan]")
            safety = user_input
            count +=1
        elif count == 5:
            germ_count = 0
            while germ_count <=2:
                if germ_count == 0:
                    user_input = console.input("[bold cyan]Requires light for germination?: [/bold cyan]")
                    germination["Requires light for germination"] = user_input
                    germ_count+=1
                elif germ_count == 1:
                    user_input = console.input("[bold cyan]Days to germinate?: [/bold cyan]")
                    germination["Days to germinate"] = user_input
                    germ_count+=1
                elif germ_count == 2:
                    user_input = console.input("[bold cyan]Days to maturity?: [/bold cyan]")
                    germination["Days to maturity"] = user_input
                    germ_count+=1
                    count +=1
                
        elif count == 6:
            info_count = 0
            while info_count <5:
                if info_count == 0:
                    user_input = console.input("[bold cyan]Required sunlight?: [/bold cyan]")
                    info["Required sunlight"] = user_input
                    info_count+=1
                elif info_count == 1:
                    user_input = console.input("[bold cyan]Drought tolerant?: [/bold cyan]")
                    info["Drought tolerant"] = user_input
                    info_count+=1
                elif info_count == 2:
                    user_input = console.input("[bold cyan]Frost tolerant?: [/bold cyan]")
                    info["Frost tolerant"] = user_input
                    info_count+=1
                elif info_count == 3:
                    user_input = console.input("[bold cyan]Growing season?: [/bold cyan]")
                    info["Growing season"] = user_input
                    info_count+=1
                elif info_count == 4:
                    user_input = console.input("[bold cyan]Description?: [/bold cyan]")
                    info["Description"] = user_input
                    info_count+=1
                elif info_count == 5:
                    user_input = console.input("[bold cyan]Interesting fact?: [/bold cyan]")
                    info["Interesting fact"] = user_input
                    count +=1
                    

            wildflower = WildFlower(name, scientific, region, zone, safety, germination, info)
            wildflowers[name] = wildflower
            print(f"[purple]Wildflower '{name}' added successfully![/purple]")
            break

#removes wildflower based on English name
def remove_wildflower():
    name = console.input("[bold cyan]Enter the name of the wildflower to remove: [/bold cyan]")
    if name in wildflowers:
        del wildflowers[name]
        print(f"[purple]Wildflower '{name}' removed successfully![/purple]")
    else:
        print(f"[purple]Wildflower '{name}' not found in the catalog.[/purple]")
        
def return_drought_tolerant():
    print('''
[green]Drought-tolerant Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Drought tolerant" in wildflower.info and wildflower.info["Drought tolerant"].lower() == "yes":
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_frost_tolerant():
    print('''
[green]Frost-tolerant Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Frost tolerant" in wildflower.info and wildflower.info["Frost tolerant"].lower() == "yes":
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_growing_season():
    print('''
[green]Wildflowers by Growing Season:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        user_input = console.input("[bold cyan]Enter growing season: [/bold cyan]")
        if "Growing season" in wildflower.info and user_input.lower() in wildflower.info["Growing season"].lower():
            print(f"[purple]{wildflower.name}[/purple]")
   
def return_edible():
    print('''
[green]Edible Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Edible" in wildflower.safety:
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_toxic():
    print('''
[green]Toxic Wildflowers:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Toxic" in wildflower.safety:
            print(f"[purple]{wildflower.name}[/purple]")

def return_full_sun():
    print('''
[green]Wildflowers for Full Sun:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Required sunlight" in wildflower.info and "full sun" in wildflower.info["Required sunlight"].lower():
            print(f"[purple]{wildflower.name}[/purple]")
            
def return_partial_shade():
    print('''
[green]Wildflowers for Partial Shade:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Required sunlight" in wildflower.info and "partial shade" in wildflower.info["Required sunlight"].lower():
            print(f"[purple]{wildflower.name}[/purple]")

def return_full_shade():
    print('''
[green]Wildflowers for Full Shade:[/green]
[dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta][dark_green]~~[/dark_green][green]'[/green][magenta]*[/magenta]
          
          ''')
    for wildflower in wildflowers.values():
        if "Required sunlight" in wildflower.info and "full shade" in wildflower.info["Required sunlight"].lower():
            print(f"[purple]{wildflower.name}[/purple]")