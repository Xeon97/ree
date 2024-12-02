
# -*- coding: utf-8 -*-

# This is a custom module for Hikka Userbot
# Author: Your Name
# Description: Creates an animated colorful heart and ends with a message.

import asyncio
from .. import loader

class AnimatedHeartMod(loader.Module):
    """Creates an animated colorful heart and a final message."""
    strings = {"name": "AnimatedHeart"}

    async def heartanimcmd(self, message):
        """Starts the animated heart sequence.
        Usage: .heartanim
        """
        heart_patterns = [
            "❤️❤️❤️       ❤️❤️❤️\n❤️❤️❤️❤️   ❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n  ❤️❤️❤️❤️❤️❤️❤️\n    ❤️❤️❤️❤️❤️\n      ❤️❤️❤️\n        ❤️",
            "💛💛💛       💛💛💛\n💛💛💛💛   💛💛💛💛\n💛💛💛💛💛💛💛💛💛\n  💛💛💛💛💛💛💛\n    💛💛💛💛💛\n      💛💛💛\n        💛",
            "💚💚💚       💚💚💚\n💚💚💚💚   💚💚💚💚\n💚💚💚💚💚💚💚💚💚\n  💚💚💚💚💚💚💚\n    💚💚💚💚💚\n      💚💚💚\n        💚",
            "💙💙💙       💙💙💙\n💙💙💙💙   💙💙💙💙\n💙💙💙💙💙💙💙💙💙\n  💙💙💙💙💙💙💙\n    💙💙💙💙💙\n      💙💙💙\n        💙",
            "💜💜💜       💜💜💜\n💜💜💜💜   💜💜💜💜\n💜💜💜💜💜💜💜💜💜\n  💜💜💜💜💜💜💜\n    💜💜💜💜💜\n      💜💜💜\n        💜"
        ]

        final_heart = "🧡🧡🧡       🧡🧡🧡\n🧡🧡🧡🧡   🧡🧡🧡🧡\n🧡🧡🧡🧡🧡🧡🧡🧡🧡\n  🧡🧡🧡🧡🧡🧡🧡\n    🧡🧡🧡🧡🧡\n      🧡🧡🧡\n        🧡"
        final_message = "🧡 <b>Manya, I love you!</b> 🧡"

        for heart in heart_patterns:
            await message.edit(f"<code>{heart}</code>")
            await asyncio.sleep(1.5)

        await message.edit(f"<code>{final_heart}</code>\n\n{final_message}")
