
def print_neon_style():
    """Вывод баннера с проверкой поддержки цветов в терминале"""


    try:

        import sys
        if sys.platform == 'win32':

            import os
            os.system('color')
    except:
        pass


    try:
        CYAN = '\033[96m'
        PINK = '\033[95m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        RESET = '\033[0m'
    except:

        CYAN = PINK = BLUE = PURPLE = RESET = ''

    banner = f"""{CYAN}{RESET}
    {CYAN}{RESET}          {PURPLE}═══  ═══  ═══  ═══  ═══  ═══  ═══  {RESET}                                                                {CYAN}{RESET}
    {PINK}{RESET}{BLUE}███████╗███╗   ███╗ █████╗ ██╗██╗{PURPLE}██████╗  █████╗ ███████╗{RESET}{PINK}{RESET}
    {PINK}{RESET}{BLUE}██╔════╝████╗ ████║██╔══██╗██║██║{PURPLE}██╔══██╗██╔══██╗██╔════╝{RESET}{PINK}{RESET}
    {PINK}{RESET}{BLUE}█████╗  ██╔████╔██║███████║██║██║{PURPLE}██████╔╝███████║███████╗{RESET}{PINK}{RESET}
    {PINK}{RESET}{BLUE}██╔══╝  ██║╚██╔╝██║██╔══██║██║██║{PURPLE}██╔══██╗██╔══██║╚════██║{RESET}{PINK}{RESET}
    {PINK}{RESET}{BLUE}███████╗██║ ╚═╝ ██║██║  ██║██║██║{PURPLE}██║  ██║██║  ██║███████║{RESET}{PINK}{RESET}
    {PINK}{RESET}{BLUE}╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝{PURPLE}╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝{RESET}{PINK}{RESET}
    {CYAN}{RESET}                                                                               {CYAN}{RESET}
    {CYAN}{RESET}           {PINK}⟦⟦{BLUE} EmailParser by CyberGolf Support {PINK}⟧⟧{RESET}           {CYAN}{RESET}
    {CYAN}{RESET}           {PURPLE}═══  ═══  ═══  ═══  ═══  ═══  ═══  {RESET}                    {CYAN}{RESET}
    {CYAN}{RESET}
    """


    if banner:
        print(banner)
    else:

        print("=" * 50)
        print("EmailParser by CyberGolf Support")
        print("=" * 50)

