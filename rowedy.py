import requests
import time
import random
import sys
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
{color}{BOLD}👑 ROWEDY KIING 👑{RESET}
"""
    print(art)

def premium_banner():
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
╔══════════════════════════════════════╗
║  🚀 PREMIUM ACCESS GRANTED SUCCESS 🚀 ║
║   ROWEDY AUTO COMMENT TOOL UNLOCKED   ║
╚══════════════════════════════════════╝
{RESET}"""
    print(art)


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
        # FIXED: Using raw GitHub URL instead of blob URL
        url = "https://raw.githubusercontent.com/Rowedy413/tmxshivampost/main/appro.txt"
        response = requests.get(url, timeout=10)
        
        # Alternative backup URL in case main fails
        if response.status_code != 200:
            url = "https://gist.githubusercontent.com/Rowedy413/raw/appro.txt"
            response = requests.get(url, timeout=10)

        if response.status_code == 200:
            approved_keys = [line.strip() for line in response.text.splitlines() if line.strip()]
            
            # Also check for partial matches (for broader approval)
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

                # REMOVED: Auto fallback to offline mode
                print(f"\n{RED}❌ Access denied. Please contact admin for approval.{RESET}")
                return False
        else:
            warn_box(f"Failed to fetch approval list (Status {response.status_code})")
            # Only allow offline mode for connection errors, not for unapproved keys
            print(f"{YELLOW}⚠️  Continuing in offline mode...{RESET}")
            time.sleep(2)
            return True

    except Exception as e:
        warn_box(f"Connection error: {e}")
        # Only allow offline mode for connection errors, not for unapproved keys
        print(f"{YELLOW}⚠️  Continuing in offline mode...{RESET}")
        time.sleep(2)
        return True


# ------------------------------
# Original Comment Tool Logic
# ------------------------------
def colorful_header():
    color = random.choice(COLORS)
    print(f"\n{color}{BOLD}══════OWNER ROWEDY══════ {RESET}")

def success_box_tool(msg):
    colorful_header()
    print(f"{GREEN}╔══════════════════════════════╗{RESET}")
    print(f"{GREEN}║   ✅ {msg}{RESET}")
    print(f"{GREEN}╚══════════════════════════════╝{RESET}")

def fail_box_tool(msg):
    colorful_header()
    print(f"{RED}╔══════════════════════════════╗{RESET}")
    print(f"{RED}║   ❌ {msg}{RESET}")
    print(f"{RED}╚══════════════════════════════╝{RESET}")

def warn(msg): 
    print(f"{YELLOW}⚠️ {msg}{RESET}")

def sleep_timer(t):
    sys.stdout.write(f"{YELLOW}⌛ Waiting {t}s...{RESET}\n")
    sys.stdout.flush()
    time.sleep(t)

def get_data(desc):
    colorful_header()
    print(f"{CYAN}╔══════════════════════════════╗{RESET}")
    print(f"{CYAN}║   {YELLOW}🔑 Paste Your {desc}{RESET}")
    print(f"{CYAN}║   {GREEN}1️⃣ Paste mode{RESET}")
    print(f"{CYAN}║   {MAGENTA}2️⃣ File mode{RESET}")
    print(f"{CYAN}╚══════════════════════════════╝{RESET}")

    mode = input(f"{BOLD}{YELLOW}{desc} Input mode > {RESET}").strip()
    if mode == "1":
        lines = []
        while True:
            try:
                l = input(f"{BOLD}{CYAN}{desc} ➡ {RESET}")
                if not l: break
                lines.append(l.strip())
            except EOFError:
                break
        return lines
    else:
        fname = input(f"{BOLD}{MAGENTA}Enter {desc} filename (.txt): {RESET}").strip()
        with open(fname, encoding="utf-8", errors="ignore") as f:
            return [x.strip() for x in f if x.strip()]

def delay_with_variation(base, gap=60):
    return max(30, base + random.randint(-gap, gap))


# ------------------------------
# Main Tool Logic
# ------------------------------
def comment_tool():
    premium_banner()
    print(f"{CYAN}🌧️ Multi-Token Facebook Auto Comment Tool (Advanced){RESET}\n")

    tokens = get_data("Token(s)")
    comments = get_data("Comment(s)")
    prefix = input(f"{CYAN}📝 Comment prefix (press ENTER to skip): {RESET}").strip()
    post_id = input(f"{CYAN}🎯 Target Post UID/ID: {RESET}").strip()
    base_delay = int(input(f"{CYAN}⏳ Base delay (sec): {RESET}").strip())

    token_sleep = [0 for _ in tokens]
    loop_round = 1

    while True:
        print(f"{MAGENTA}⭐ Round {loop_round} Started{RESET}")
        random.shuffle(comments)
        ci = 0
        while ci < len(comments):
            now = time.time()
            available = [i for i, t in enumerate(token_sleep) if t <= now]
            if not available:
                warn("All tokens sleeping... waiting.")
                sleep_time = min(token_sleep) - now
                sleep_timer(max(15, int(sleep_time)))
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
                    success_box_tool(f"[TOKEN{idx+1}] Comment posted 🎉: {msg}")
                else:
                    fail_box_tool(f"[TOKEN{idx+1}] Failed [{r.status_code}] {r.text}")
                    if "limit" in r.text.lower():
                        warn(f"[TOKEN{idx+1}] Rate limit! Sleeping 15min 😴")
                        token_sleep[idx] = time.time() + 900
                ci += 1
            except Exception as e:
                fail_box_tool(f"[TOKEN{idx+1}] Error: {e}")
                ci += 1

            this_delay = delay_with_variation(base_delay, 60)
            sleep_timer(this_delay)

        loop_round += 1


# ------------------------------
# Main Function
# ------------------------------
def main():
    full_banner()
    if approval_check_online():
        comment_tool()
    else:
        print(f"\n{RED}❌ Program terminated. Please get approval first.{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
