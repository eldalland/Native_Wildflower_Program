from Dictionary.wildflower_dict import wildflowers
from Functions.wildflower_methods import *
from rich.console import Console
from rich import print

def main():
    """Main function that runs when the script is executed."""
    # Create a console instance with highlighting disabled and markup enabled
    console = Console(highlight=False, markup=True)
    
    console.print("""
[dark_green]~~[/dark_green][bright_green]'[/bright_green][magenta]*[/magenta][dark_green]~~[/dark_green][bright_green]'[/bright_green][magenta]*[/magenta][dark_green]~~[/dark_green][bright_green]'[/bright_green][magenta]*[/magenta][purple]Welcome to the American Native Wildflower App![/purple][magenta]*[/magenta][bright_green]'[/bright_green][dark_green]~~[/dark_green][magenta]*[/magenta][bright_green]'[/bright_green][dark_green]~~[/dark_green][magenta]*[/magenta][bright_green]'[/bright_green][dark_green]~~[/dark_green]
                                                      
                             [blue]__
                            // \\
                            \\_//[/blue] [yellow]//[/yellow]
        [blue]sjw''-.._.-''-.._..[/blue] [yellow]-(||)(')[/yellow]
                     [yellow]_       '''[/yellow]
                   [yellow]_(_)_[/yellow]                          [magenta]wWWWw[/magenta]   [yellow]_[/yellow]
       [red]@@@@[/red]       [yellow](_)[red]@[/red](_)[/yellow]   [magenta]vVVVv[/magenta]      [yellow]_[/yellow]    [red]@@@@[/red]  [magenta](___)[/magenta] [yellow]_(_)_[/yellow]
      [red]@@[yellow]()[/yellow]@@[/red] [magenta]wWWWw[/magenta]  [yellow](_)[/yellow][green]\\ [/green]   [magenta](___)[/magenta]    [yellow]_(_)_[/yellow] [red]@@[yellow]()[/yellow]@@[/red]   [green]Y[/green]  [yellow](_)[red]@[/red](_)[/yellow]
       [red]@@@@[/red]  [magenta](___)[/magenta]     [green]`|/    Y[/green]     [yellow](_)[red]@[/red](_)[/yellow] [red]@@@@[/red]   [green]\\|/[/green]  [yellow](_)[/yellow][green]\\ [/green]
        [green]/      Y       \\|    \\|/     /[yellow](_)[/yellow]   \\|      |/      |
     \\ |     \\ |/       | / \\ | /  \\|/       |/    \\|      \\|/
jgs   \\|//    \\|///    \\|//  \\|/// \\|///    \\|//   \\|//    \\|//
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[/green]
          
[purple]This is a working dictionary of American wildflowers categorized by geographic region and containing important general information about each species.
          
To view a list of commands: please type "help"
          
Save our pollinators![/purple]
          """)
    
    keywords = [
        "list all",
        "quit",
        "help",
        "northeast",
        "southeast", 
        "midwest", 
        "northwest", 
        "southwest",
        "add wildflower",
        "remove wildflower",
        "drought-tolerant", 
        "frost-tolerant", 
        "growing season", 
        "edible", 
        "toxic",
        "full sun",
        "partial shade",
        "full shade"
    ]

    while True:
        
        user_input = console.input("[bold cyan]Enter command: [/bold cyan]")
        print(f"[purple]You entered: {user_input}[/purple]")

        if user_input == "help":
            print("""          
          To view a list of all our cataloged wildflowers separated by geographical region:
          type "list all" and hit "enter" or "return".
          
          To view a list of wildflowers based on region:
          please type "northeast, southeast, midwest, northwest, or southwest".
          
          To view all info on a specific wildflower:
          type the english or latin name of the flower, with multi-word names separated by spaces.
          
          To view a list of wildflowers based on specific characteristics, you may simply type one of these keywords:
          "drought-tolerant, frost-tolerant, growing season, edible, toxic, full sun, partial shade, full shade".
          
          To add a wildflower to the list:
          type "add wildflower" and then follow the prompts that appear in the command line.
          
          To remove a wildflower from the list:
          type "remove wildflower" and then follow the prompts that appear in the command line.
          
          Furthermore, you may type in a region followed by a comma, a space, and a characteristic to narrow-down your search.
          
          To exit the program: type "quit".)
        """)
        
        # Handle commands using match-case (Python 3.10+) - more efficient than if-elif-else
        # Convert to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()
        
        match user_input_lower:
            case "list all":
                return_all()
            case "growing season":
                print("Showing wildflowers by growing season...")
            case "northeast":
                return_northeast()
            case "southeast":
                return_southeast()
            case "midwest":
                return_midwest()
            case "northwest":
                return_northwest
            case "southwest":
                return_southwest()
            case "add wildflower":
                add_wildflower()
            case "remove wildflower":
                remove_wildflower()
            case "drought-tolerant":
                return_drought_tolerant()
            case "frost-tolerant":
                return_frost_tolerant()
            case "edible":
                return_edible()
            case "toxic":
                return_toxic()
            case "full sun":
                return_full_sun()
            case "partial shade":
                return_partial_shade()
            case "full shade":
                return_full_shade()
            case "quit":
                print("[purple]Goodbye![/purple]")
                break  # Exit the loop
            case "help":
                pass  # Help is already handled above
            case _:  # Default case for unknown commands
                print(return_wildflower(user_input))  # Pass original input to preserve formatting
                print("Type 'help' for available commands.")
        
# This ensures main() only runs when script is executed directly
if __name__ == "__main__":
    main()