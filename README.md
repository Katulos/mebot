# Telegram /me Bot

A bot that implements the IRC-style `/me` command in Telegram chats. Allows users to send messages in the format "*action*", for example:  
`*is drinking coffee*` or `*is going on vacation*`.

---

> [!CAUTION]
> ⚠️ Automating user accounts violates Telegram’s Terms of Service.
> ⚠️ The author is not responsible for any consequences of using the bot in `user` mode.
> ⚠️ For public or long-term use, the `bot` mode is strongly recommended.

---

## Features

- Supports the `/me <action>` command in group chats.  
- Automatically deletes the original command message.  
- Sends the result as an anonymous message from the group (only when running as a user account with admin anonymity enabled).

---

## Important: Two Operating Modes

The bot can run in two modes — **as an official Telegram Bot** or **as a regular user account**. The chosen mode affects appearance and functionality.

### 1. Telegram Bot Mode (Official Bot)

- **Pros**:  
  - Easy and legitimate setup via [@BotFather](https://t.me/BotFather).  
  - No phone number required.  

- **Cons**:  
  - All messages will appear **from the bot** (e.g., "@MyMeBot: *is drinking coffee*").  
  - Cannot hide the fact that a bot is being used.  

- **Required chat permissions**:  
  - Delete messages (`can_delete_messages`).  
  - Send messages.

### 2. User Account Mode

- **Pros**:  
  - If the account is added as an **anonymous admin**, messages appear **from the group itself**, with no sender name shown — visually matching the IRC `/me` style (`*is drinking coffee*`).  

- **Cons**:  
  - Requires authentication using a **real Telegram account** (phone number).  
  - Automating user accounts **violates [Telegram’s Terms of Service](https://core.telegram.org/api/terms)** and may result in account termination.  
  - Requires manual admin setup in each chat.

- **Required chat permissions**:  
  - Promote the account to **admin**.  
  - Enable **"Remain Anonymous"** during admin promotion (or in group admin settings).  
  - Grant **"Delete messages"** permission.

---

## Installation and Setup

1. Install dependencies:
   ### Use curl to download the script and execute it with sh:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   ### If your system doesn't have curl, you can use wget:
   ```bash
   wget -qO- https://astral.sh/uv/install.sh | sh
   ```
2. Install the bot:
   ```bash
   git clone https://github.com/katulos/mebot
   cd bot
   uv venv
   source .venv/bin/activate
   uv pip install -e .
   ```

3. Create a `.secrets.yml` file and configure it based on your mode:

   ### For Telegram Bot mode:
   ```yaml
   api_id: your_api_id
   api_hash: your_api_hash
   bot_token: your_bot_token_here
   ```

   ### For User Account mode:
   ```yaml
   api_id: your_api_id
   api_hash: your_api_hash
   phone: your_phone_number
   ```

   > You can obtain `api_id` and `api_hash` at [my.telegram.org](https://my.telegram.org).

4. Run the bot:
   ```bash
   mebot start
   ```

   On first launch in `user` mode, you’ll be prompted to enter a verification code sent by Telegram.

---

## Chat Configuration

### For `bot` mode:
1. Add the bot to your group.
2. Promote it to admin with **"Delete messages"** permission.

### For `user` mode:
1. Add your user account to the group.
2. Promote it to admin and **ensure "Remain Anonymous" is enabled**.
3. Grant the **"Delete messages"** permission.

Then use the command:
```
/me is dancing in the rain
```
→ The original message will be deleted, and the chat will show:
```
*Username is dancing in the rain*
```
(In `user` mode with anonymity: no sender shown; in `bot` mode: message appears from the bot.)

---

## License

MIT License. See the [LICENSE](LICENSE) file for details.

