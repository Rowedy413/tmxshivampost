import requests
import time
import random
import sys
sys.dont_write_bytecode = True

import io
import os
import subprocess
import pyperclip

# ------------------------------
# Simple Key Generator
# ------------------------------
try:
    device = str(os.geteuid())
except:
    device = "UNKNOWN"

try:
    build = subprocess.check_output("getprop ro.build.id", shell=True).decode().strip()
except:
    build = "UNKNOWN"

# Short Key
final_key = "KEY-" + (device + build)[-6:].upper()

# Master Key (always approved)
MASTER_KEY = "VIP-12345"

# Force UTF-8 for stdin
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", errors="ignore")

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

COLORS = [RED, GREEN, CYAN, YELLOW, MAGENTA]


# ------------------------------
# Banners
# ------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def rowedy_banner():
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
{color}{BOLD}👑 ROWEDY KIING 🦅🖤 THANKS FOR CONNECTING US (राजस्थान सरकार){RESET}
"""
    print(art)


def shivam_banner():
    clear_screen()
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
███████╗██╗  ██╗██╗██╗   ██╗ █████╗  ██████╗ ███╗   ███╗
██╔════╝██║  ██║██║╚██╗ ██╔╝██╔══██╗██╔═══██╗████╗ ████║
█████╗  ███████║██║ ╚████╔╝ ███████║██║   ██║██╔████╔██║
██╔══╝  ██╔══██║██║  ╚██╔╝  ██╔══██║██║   ██║██║╚██╔╝██║
███████╗██║  ██║██║   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝
{RESET}
{color}{BOLD}👑 SHIVAM PREMIUM ACCESS 👑{RESET}
"""
    print(art)
    print(f"{color}{BOLD}❌ Approval Required to Continue ❌{RESET}\n")


def premium_start_screen():
    clear_screen()
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██╗   ██╗
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗╚██╗ ██╔╝
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝ ╚████╔╝ 
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔═══╝   ╚██╔╝  
██║     ╚██████╔╝╚███╔███╔╝███████╗██║        ██║   
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝        ╚═╝   
{RESET}
{color}{BOLD}👑 ROWEDY PREMIUM POST TOOL 🖤🦅THANKS FOR CONNECTING US (राजस्थान सरकार){RESET}
"""
    print(art)
    print(f"{GREEN}╔══════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║ 🛡️ PREMIUM ACCESS GRANTED SUCCESS 🔑 ║{RESET}")
    print(f"{GREEN}║     ROWEDY AUTO POST TOOL READY      ║{RESET}")
    print(f"{GREEN}╚══════════════════════════════════════╝{RESET}\n")
    time.sleep(2)


# ------------------------------
# Stylish Box Printers
# ------------------------------
def success_box(msg):
    print(f"{GREEN}╔══════════════════════════════╗{RESET}")
    print(f"{GREEN}║   ✅ {msg}{RESET}")
    print(f"{GREEN}╚══════════════════════════════╝{RESET}")


def fail_box(msg):
    print(f"{RED}╔══════════════════════════════╗{RESET}")
    print(f"{RED}║   ❌ {msg}{RESET}")
    print(f"{RED}╚══════════════════════════════╝{RESET}")


def warn_box(msg):
    print(f"{YELLOW}╔══════════════════════════════╗{RESET}")
    print(f"{YELLOW}║   ⚠️ {msg}{RESET}")
    print(f"{YELLOW}╚══════════════════════════════╝{RESET}")


def owner_rowedy_box():
    print(f"{MAGENTA}{BOLD}╔══════════════════════════════╗{RESET}")
    print(f"{MAGENTA}{BOLD}║      OWNER ROWEDY 👑         ║{RESET}")
    print(f"{MAGENTA}{BOLD}╚══════════════════════════════╝{RESET}")


# ------------------------------
# Approval System (FIXED)
# ------------------------------
def approval_check_online():
    print(f"\n{CYAN}╔══════════════════════════════╗{RESET}")
    print(f"{CYAN}║   🔑 Your Device Key: {YELLOW}{final_key}{RESET}")
    print(f"{CYAN}╚══════════════════════════════╝{RESET}\n")

    # ✅ Direct pass for master key
    if final_key == MASTER_KEY:
        success_box("Master Key Detected! Always Approved 🎉")
        return True

    try:
        url = "https://raw.githubusercontent.com/Rowedy413/tmxshivampost/main/appro.txt"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            url = "https://gist.githubusercontent.com/Rowedy413/raw/appro.txt"
            response = requests.get(url, timeout=10)

        if response.status_code == 200:
            approved_keys = [line.strip() for line in response.text.splitlines() if line.strip()]

            partial_match = any(final_key in key for key in approved_keys if "KEY-" in key)

            if final_key in approved_keys or partial_match:
                success_box("Approval Successful! 😎")
                return True
            else:
                fail_box("Your Key is not Approved 💔")
                user_name = input("\n💡 Enter your name: ").strip()
                message = f"🌟 Hello Sir 🌟\nMy name is {user_name}\nPlease approve my key:\n🔑 {final_key}"
                try:
                    pyperclip.copy(message)
                    print(f"{MAGENTA}📋 Message copied to clipboard!{RESET}")
                except:
                    pass
                whatsapp_url = f"https://wa.me/918290090930?text={requests.utils.quote(message)}"
                try:
                    os.system(f'termux-open "{whatsapp_url}"')
                except:
                    try:
                        os.system(f'xdg-open "{whatsapp_url}"')
                    except:
                        print(f"{YELLOW}📱 Open WhatsApp and send this message:{RESET}")
                        print(f"{CYAN}{message}{RESET}")
                print(f"\n{RED}❌ Access denied. Please contact admin for approval.{RESET}")
                return False
        else:
            warn_box(f"Failed to fetch approval list (Status {response.status_code})")
            print(f"{YELLOW}⚠️  Continuing in offline mode...{RESET}")
            time.sleep(2)
            return True

    except Exception as e:
        warn_box(f"Connection error: {e}")
        print(f"{YELLOW}⚠️  Continuing in offline mode...{RESET}")
        time.sleep(2)
        return True


# ------------------------------
# Data Input (Safe)
# ------------------------------
def colorful_header():
    color = random.choice(COLORS)
    print(f"\n{color}{BOLD}══════OWNER ROWEDY══════ {RESET}")


def get_data(desc):
    colorful_header()
    print(f"{CYAN}╔══════════════════════════════╗{RESET}")
    print(f"{CYAN}║   {YELLOW}🔑 Paste Your {desc}{RESET}")
    print(f"{CYAN}║   {GREEN}1️⃣ Paste mode{RESET}")
    print(f"{CYAN}║   {MAGENTA}2️⃣ File mode{RESET}")
    print(f"{CYAN}╚══════════════════════════════╝{RESET}")

    mode = input(f"{BOLD}{YELLOW}{desc} Input mode > {RESET}").strip()
    if mode == "1":
        print(f"{CYAN}➡ Paste {desc} one per line. Press ENTER twice to finish.{RESET}")
        lines = []
        while True:
            try:
                l = input(f"{BOLD}{CYAN}{desc} ➡ {RESET}")
                if not l:
                    break
                lines.append(str(l).strip())  # Safe string only
            except EOFError:
                break
        return lines
    else:
        fname = input(f"{BOLD}{MAGENTA}Enter {desc} filename (.txt): {RESET}").strip()
        with open(fname, encoding="utf-8", errors="ignore") as f:
            return [str(x).strip() for x in f if x.strip()]


def sleep_timer(t):
    sys.stdout.write(f"{YELLOW}⌛ Waiting {t}s...{RESET}\n")
    sys.stdout.flush()
    time.sleep(t)


def delay_with_variation(base, gap=60):
    return max(30, base + random.randint(-gap, gap))


# ------------------------------
# Comment Tool Logic
# ------------------------------
def comment_tool():
    rowedy_banner()
    print(f"{CYAN}🌧️ Multi-Token Facebook Auto Comment Tool (Advanced){RESET}\n")

    tokens = get_data("Token(s)")
    comments = get_data("Comment(s)")
    prefix = input(f"{CYAN}📝 Comment prefix (press ENTER to skip): {RESET}").strip()
    post_id = input(f"{CYAN}🎯 Target Post UID/ID: {RESET}").strip()
    base_delay = int(input(f"{CYAN}⏳ Base delay (sec): {RESET}").strip())

    token_sleep = [0 for _ in tokens]
    loop_round = 1

    while True:
        print(f"{MAGENTA}⭐ ════OWNER ROWEDYY═══ round {loop_round} Started{RESET}")
        random.shuffle(comments)
        ci = 0
        while ci < len(comments):
            now = time.time()
            available = [i for i, t in enumerate(token_sleep) if t <= now]
            if not available:
                # All tokens sleeping, wait for the soonest to expire
                wait_time = min(token_sleep) - now
                warn_box("All tokens sleeping... waiting.")
                sleep_timer(max(15, int(wait_time)))
                continue

            idx = random.choice(available)
            token = tokens[idx]
            comment = comments[ci]
            msg = f"{prefix}{comment}"

            url = f"https://graph.facebook.com/{post_id}/comments"
            payload = {"message": msg, "access_token": token}
            try:
                r = requests.post(url, data=payload)
                if r.status_code == 200:
                    success_box(f"[TOKEN{idx + 1}] Comment posted 🎉: {msg}")
                    owner_rowedy_box()
                    ci += 1
                else:
                    fail_box(f"[TOKEN{idx + 1}] Failed [{r.status_code}] {r.text}")
                    if "limit" in r.text.lower():
                        warn_box(f"[TOKEN{idx + 1}] Rate limit! Sleeping 15min 😴")
                        token_sleep[idx] = time.time() + 900
                    # Move on to next comment anyway, but don't increment ci here so comment tries with next available token
                    # Alternative: Skip comment retry to avoid stuck loops
                    ci += 1
            except Exception as e:
                fail_box(f"[TOKEN{idx + 1}] Error: {e}")
                ci += 1

            # Use varied delay per comment, but do not delay tokens that are sleeping
            this_delay = delay_with_variation(base_delay, 60)
            sleep_timer(this_delay)

        loop_round += 1


# ------------------------------
# Main Function
# ------------------------------
def main():
    shivam_banner()  # show initially in case approval fails for visual

    if approval_check_online():
        # Show Rowedy banner after approval
        rowedy_banner()
        comment_tool()
    else:
        # On failure, keep Shivam banner and exit
        print(f"\n{RED}❌ Program terminated. Please get approval first.{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
