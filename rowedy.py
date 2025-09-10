import requests
import time
import random
import sys
import io
import os
import subprocess
import requests
import pyperclip
import os
try:
    a = str(os.geteuid())  # or use device ID logic
except:
    a = "UNKNOWN"

try:
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n','')
except:
    build = "UNKNOWN"

x = (a + build + a).upper().replace(".", "")
z = "X".join(x)
final_key = "Shivam-"+z[15:]
# Force UTF-8 for stdin (emoji/symbol safe)
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", errors="ignore")
os.system('xdg-open https://chat.whatsapp.com/KPwQpcQKlOO3ilcJTDKEsD?mode=ems_copy_t')
# Terminal color codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

COLORS = [RED, GREEN, CYAN, YELLOW, MAGENTA]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def full_banner():
    clear_screen()
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
███████╗██╗  ██╗██╗██╗   ██╗ █████╗ ███╗   ███╗
██╔════╝██║  ██║██║╚██╗ ██╔╝██╔══██╗████╗ ████║
███████╗███████║██║ ╚████╔╝ ███████║██╔████╔██║
╚════██║██╔══██║██║  ╚██╔╝  ██╔══██║██║╚██╔╝██║
███████║██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝
{RESET}
{color}{BOLD}👑 I AM SHIVAM 👑{RESET}
{color}THNKS FOR CONNECTING US ({YELLOW}राजस्थान सरकार{RESET}{color}){RESET}
"""
    print(art)

def approval_check_online():
    try:
        link = "https://raw.githubusercontent.com/Rowedy413/tmxshivampost/main/appro.txt"
        response = requests.get(link)
        if response.status_code == 200:
            approved_keys = response.text.splitlines()
            full_banner()
            print(f"\n🔑 Your Device Key: {final_key}\n")

            if final_key in approved_keys:
                premium_banner()
                print("✅ Approval Successful! Welcome 😎")
            else:
                print("❌ Your key is not approved.")
                print("📞 Contact Admin to get approval.")

                user_name = input("\nEnter your name: ").strip()

                message = (
                    f"Hello Sir my name is {user_name}\n"
                    f"And please approve my key:\n{final_key}"
                )

                try:
                    pyperclip.copy(message)
                    print("📋 Message copied to clipboard!")
                except Exception as e:
                    print(f"⚠️ Clipboard copy failed: {e}")

                
                whatsapp_url = f"https://wa.me/918290090930?text={message.replace(' ', '%20')}"
                try:
                    os.system(f'termux-open "{whatsapp_url}"')
                    print("➡️ WhatsApp opened with message pre-filled.")
                except Exception as e:
                    print(f"❌ WhatsApp open failed: {e}")

                exit()
        else:
            print("❌ Failed to fetch key list. Status:", response.status_code)
            exit()

    except Exception as e:
        print(f"❌ Error during approval check: {str(e)}")
        exit()

def colorful_header():
    color = random.choice(COLORS)
    print(f"\n{color}{BOLD}══════OWNER ROWEDY══════ {RESET}")

def premium_banner():
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██╗   ██╗     
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗╚██╗ ██╔╝    
██║  ██║██║   ██║██║ █╗ ██║███████╗██████╔╝ ╚████╔╝     
██║  ██║██║   ██║██║███╗██║╚════██║██╔═══╝   ╚██╔╝      
██████╔╝╚██████╔╝╚███╔███╔╝███████║██║        ██║       
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝        ╚═╝       
═════════ SHIVAM POST LOADER ─ [PREMIUM FB AUTO COMMENT TOOL] ═════════
{RESET}"""
    print(art)

def border(msg, icon="☂️"):
    deco = icon * 4
    return f"\n{CYAN}{deco} {BOLD}{msg}{RESET} {CYAN}{deco}{RESET}\n"

def info(msg): print(f"{CYAN}{msg}{RESET}")
def success_box(msg):
    colorful_header()
    print(f"{GREEN}╔══════════════════════════════╗{RESET}")
    print(f"{GREEN}║   ✅ {msg}{RESET}")
    print(f"{GREEN}╚══════════════════════════════╝{RESET}")
def fail_box(msg):
    colorful_header()
    print(f"{RED}╔══════════════════════════════╗{RESET}")
    print(f"{RED}║   ❌ {msg}{RESET}")
    print(f"{RED}╚══════════════════════════════╝{RESET}")
def warn(msg): print(f"{YELLOW}⚠️ {msg}{RESET}")

def sleep_timer(t):
    sys.stdout.write(f"{YELLOW}⌛ Waiting {t}s...{RESET}\n")
    sys.stdout.flush()
    time.sleep(t)

# Stylish input reader
def get_data(desc):
    colorful_header()
    print(f"{CYAN}╔══════════════════════════════╗{RESET}")
    print(f"{CYAN}║   {YELLOW}🔑 Paste Your {desc}{RESET}")
    print(f"{CYAN}║   {GREEN}1️⃣ Paste mode{RESET}")
    print(f"{CYAN}║   {MAGENTA}2️⃣ File mode{RESET}")
    print(f"{CYAN}╚══════════════════════════════╝{RESET}")

    mode = input(f"{BOLD}{YELLOW}{desc} Input mode > {RESET}").strip()
    if mode == "1":
        colorful_header()
        print(f"{CYAN}╔══════════════════════════════╗{RESET}")
        print(f"{CYAN}║ {GREEN}Paste {desc} one per line. {RESET}")
        print(f"{CYAN}║ {YELLOW}END with an empty line!   {RESET}")
        print(f"{CYAN}╚══════════════════════════════╝{RESET}")
        lines = []
        while True:
            try:
                l = input(f"{BOLD}{CYAN}{desc} ➡ {RESET}")
                if not l: break
                safe_line = l.encode("utf-8", "ignore").decode("utf-8", "ignore")
                lines.append(safe_line.strip())
            except EOFError:
                break
        return lines
    else:
        colorful_header()
        fname = input(f"{BOLD}{MAGENTA}Enter {desc} filename (.txt): {RESET}").strip()
        with open(fname, encoding="utf-8", errors="ignore") as f:
            return [x.strip() for x in f if x.strip()]

def delay_with_variation(base, gap=60):
    return max(30, base + random.randint(-gap, gap))

def print_token_stats(token_stats):
    print(border("== Token Stats ==", "🔢"))
    for i, (token, stats) in enumerate(token_stats.items(), 1):
        s, t = stats["success"], stats["total"]
        tag = stats["tag"]
        print(f"{CYAN}Token {i} [{tag}]: {GREEN}{s} success{RESET} / {YELLOW}{t} total{RESET}")

def main():
    full_banner()    
    premium_banner()

    print(border("🌧️ Multi-Token Facebook Auto Comment Tool (Advanced) 🌧️", "🌧️"))
    tokens = get_data("Token(s)")
    token_tags = [f"TOKEN{i+1}" for i in range(len(tokens))]
    token_sleep = [0 for _ in tokens]
    token_stats = {tok: {"tag": tag, "success": 0, "total": 0} for tok, tag in zip(tokens, token_tags)}

    comments = get_data("Comment(s)")
    prefix = input(f"{CYAN}Comment prefix (press ENTER to skip): {RESET}").strip()
    post_id = input(f"{CYAN}Target Post UID/ID: {RESET}").strip()
    base_delay = int(input(f"{CYAN}Base delay (sec): {RESET}").strip())
    print(border(f"Loaded {len(tokens)} token(s) & {len(comments)} comment(s)! 🦾", "✨"))

    loop_round = 1
    while True:
        print_token_stats(token_stats)
        print(border(f"Round {loop_round} Started", "⭐"))
        random.shuffle(comments)
        ci = 0
        while ci < len(comments):
            now = time.time()
            available = [i for i, t in enumerate(token_sleep) if t <= now]
            if not available:
                warn("All tokens rate-limited! Waiting for earliest recovery...")
                sleep_time = min(token_sleep) - now
                sleep_timer(max(15, int(sleep_time)))
                continue
            idx = random.choice(available)
            token = tokens[idx]
            tag = token_tags[idx]

            comment = comments[ci]
            msg = f"{prefix}{comment}"

            url = f"https://graph.facebook.com/{post_id}/comments"
            payload = {"message": msg, "access_token": token}
            print(border(f"[{tag}] ➡️ {msg}", "💬"))
            try:
                r = requests.post(url, data=payload)
                rtext = r.text
                token_stats[token]["total"] += 1
                if r.status_code == 200:
                    token_stats[token]["success"] += 1
                    success_box(f"[{tag}] Comment posted! ══════ ROWEDY HERE ══════🔥 SUCCESS 👑")
                    ci += 1
                else:
                    fail_box(f"[{tag}] Failed [{r.status_code}]: {rtext}")
                    ltext = rtext.lower()
                    if "rate limit" in ltext or "limit how often" in ltext or "spam" in ltext:
                        warn(f"[{tag}] Rate-limit/spam detected! Sleeping this token 15min...")
                        token_sleep[idx] = time.time() + 900
                        ci += 1
                    else:
                        warn(f"[{tag}] Other error; long sleep, retrying later.")
                        sleep_timer(delay_with_variation(base_delay, 60) * 2)
                        ci += 1
            except Exception as e:
                fail_box(f"[{tag}] Network/Error: {e}")
                sleep_timer(delay_with_variation(base_delay, 60) * 2)
                ci += 1
            this_delay = delay_with_variation(base_delay, 60)
            info(f"⌛ Next comment in {this_delay}s...\n")
            sleep_timer(this_delay)
        loop_round += 1
        info(border(f"❤️ Loop completed • Restarting…", "🌀"))
def main():
    approval_check_online()
    full_banner()    
    premium_banner()
if __name__ == "__main__":
    main()
